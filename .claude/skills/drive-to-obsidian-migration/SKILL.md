---
name: drive-to-obsidian-migration
description: "Migrate a Google Drive folder into this Obsidian vault repo via Termux: rclone bulk transfer, dedupe, Markdown conversion, and JSONL RAG chunking. Use when the operator wants more Drive content pulled into the vault, or is setting up this same pipeline from scratch on a new device."
---

# Drive → Termux → GitHub Obsidian Vault Migration

Full pipeline for pulling a Google Drive folder into this repo as a clean,
deduped, Markdown vault with a JSONL RAG library. Written after actually
doing this once, including every wrong turn — follow this and skip the
mistakes below.

## The shape of the pipeline

1. **Drive → phone** (Termux + `rclone`) — bulk download, not selective.
2. **Phone → GitHub** (`git push`) — raw dump lands in a single `INBOX/`
   staging folder on a dedicated branch.
3. **Cloud session → clean vault** — dedupe, convert to Markdown, build the
   RAG library, all from a cloud sandbox with the branch cloned in, not from
   the phone (much faster, real conversion tooling available).

Do the bulk transfer via `rclone` on-device, not via a Drive API/MCP crawl
one file at a time — a folder-by-folder API crawl for thousands of files
will not finish in reasonable time and burns enormous tool-call budget. Use
Drive API access (if available) only for targeted lookups (finding one
file's exact name/link), never as the primary transport.

## Step 1: Termux + rclone setup

```
command -v git >/dev/null || pkg install git -y
command -v rclone >/dev/null || pkg install rclone -y
termux-setup-storage   # if not already done
```

**Use a real Google API client_id, not rclone's shared default key.** The
default key is rate-limited across every rclone user on earth; for a
thousand-plus-file transfer this WILL throttle. Create one:
1. console.cloud.google.com → any project → enable "Google Drive API"
2. APIs & Services → OAuth consent screen → External, Testing mode is fine,
   add the Drive account's own email as a test user
3. APIs & Services → Credentials → Create OAuth client ID → **Desktop app**
4. Copy the Client ID + Secret into `rclone config` when prompted

```
rclone config
```
`n` (new) → name it → `drive` (Google Drive) → paste client_id → paste
client_secret → scope `1` (full access) → blank → blank → advanced config
`n` → auto config `y` → **this opens a browser link; log in as the account
that owns the target Drive folder** → team drive `n` → `y` to confirm → `q`.

**Trap: the OAuth browser callback times out if Termux gets backgrounded.**
Android suspends background apps' network activity, and rclone's local
callback server (`127.0.0.1:53682`) stops responding the moment you fully
switch away from Termux to the browser. Fix: run `termux-wake-lock` first,
and/or use split-screen so Termux stays visibly active while you complete
login in the browser. If it times out anyway ("no code returned by remote
server"), `rclone config` → `e` (edit) the broken remote → hit enter through
the already-filled fields to reach "Use auto config?" again for a fresh link
— no need to start over from scratch, the client_id/secret are retained.

## Step 2: the actual transfer

```
git clone -b <branch> https://github.com/<owner>/<repo>.git ~/some-clean-folder
```

**Trap: never reuse an existing local folder name blind.** If
`git clone` fails with "already exists and not empty," that is a hard stop
— investigate what that folder actually is before proceeding
(`readlink -f`, check for `.git`, check for unrelated dotfiles like
`.cargo`/`.oh-my-zsh`/other project clones). Picking a folder name that
happens to collide with the user's home directory or another project and
plowing ahead anyway is how `git add -A` ends up trying to commit the user's
entire dev environment — package caches, shell plugin managers, unrelated
repos — into this vault. It happened once during this project's own
migration; caught it before push (Ctrl+C on `git add`, `git reset`, redo
into a genuinely fresh directory name) — but check the destination FIRST
next time instead of recovering after.

```
rclone copy "gdrive:<source folder>" ~/some-clean-folder/INBOX -P --transfers 16 --log-file=$HOME/toolong.log --log-level INFO
```
(`$HOME`, not `~`, inside `--log-file=`: `~` does not expand when glued to
`=` with no space.)

**Trap: filenames over 255 bytes fail with "file name too long."** Common
cause on this kind of vault: Gemini/voice-conversation exports and GitHub
README exports get auto-titled from the first line of content or the repo
description — these run hundreds of characters. Find and fix them:
```
grep "too long" $HOME/toolong.log
```
Rename the offending file directly in Drive (any app, doesn't need to be
on-device) to under ~100 characters, then just re-run the same `rclone copy`
— it skips everything already transferred and only retries what's missing.
**Delete `$HOME/toolong.log` between retries** — `--log-file` appends, so a
stale log shows old failures mixed with new ones and looks like renames
aren't taking effect when they actually are.

**The 100MB limit is a GitHub push limit, not an rclone/Drive limit.** Don't
pre-screen for it before downloading. Let `rclone copy` pull everything,
THEN check locally, THEN decide what to do about anything oversized:
```
find ~/some-clean-folder/INBOX -size +100M -exec du -h {} \;
```
If what's flagged is genuinely non-wiki content (model weights, SDK
archives — check before assuming), don't fight it with Git LFS; drop it and
leave a small reference stub in its place:
```bash
find ~/some-clean-folder/INBOX -size +100M -print0 | while IFS= read -r -d '' f; do
  size=$(du -h "$f" | cut -f1)
  cat > "$f.EXCLUDED.md" <<EOF
# Excluded from repo — too large for git
- Original file: $(basename "$f")
- Size: $size
- Reason: exceeds GitHub's 100MB per-file limit
EOF
  rm "$f"
done
```

```
cd ~/some-clean-folder && git add -A && git commit -m "raw dump" && git push
```

## Step 3: dedupe + Markdown conversion + RAG chunking (cloud sandbox)

Do this part from a cloud session with the branch cloned in, not on-device
— real conversion tooling (`pandoc`, PyMuPDF, `trafilatura`) and no
phone-battery/backgrounding constraints.

```
apt-get install -y pandoc
pip install pymupdf trafilatura
```
(If `pip install pypdf`/`pdfminer.six` fails with a `cryptography`/`_cffi_backend`
Rust panic, that's a broken system `cryptography` package — skip those
libraries and use `pymupdf` instead, it has no such dependency.)

Use `.migrate/process_folder.py` (in this repo) per top-level source folder:
```
python3 .migrate/process_folder.py "INBOX/<folder>" "_DUPLICATES_REVIEW/<folder>" "<folder>"
```
- Dedupes by content hash **within each folder only** — cross-folder
  duplicates of the same file are left alone (intentional per-folder
  organization, not junk).
- Converts `.docx`/`.pdf`/`.txt`/`.mht` to Markdown; everything else
  (code, images, binaries, `.jsonl`, already-`.md`) passes through
  unchanged. Check the file-type breakdown before assuming everything in a
  folder is "wiki content" — several folders in this vault turned out to be
  full cloned reference repos (hundreds of `.ts`/`.rs`/`.kt` files), which
  should never be run through document conversion.
- Converted output always keeps the source extension folded in
  (`Foo.pdf.md`, not `Foo.md`) — this prevents same-titled files of
  different source types from silently overwriting each other. If working
  from a fork/copy of this script, do not "simplify" this away.

After each folder: verify the count reconciles (`source count − duplicates
== destination count`) before deleting the source and committing. A
mismatch means a collision happened — check for it with a script grouping
files by `(dir, base-without-extension)` restricted to only the convertible
extensions (a `.ts` and `.tsx` sharing a base name is NOT a collision, they
keep distinct extensions; only two files that BOTH end up as `.md` collide).
If files went missing this way, they're still recoverable from git history
via `git show <earlier-commit>:<path>` as long as the source folder deletion
hasn't been committed and pushed yet over that history.

Finally, build the RAG library once all folders are converted:
```
python3 .migrate/build_rag_chunks.py . RAG_LIBRARY
```
Dedupes by content hash **across the whole vault** (different scope than
the per-folder step above, deliberately) — the same doc landing in 5
folders should only be chunked once for retrieval, or it just adds noise.
Only docs over ~3000 words get chunked; chunks by `##`/`###` heading where
present, else fixed word-count windows with overlap.

## What NOT to do

- Don't try to be the primary transport for bulk Drive content via an MCP
  Drive connector's file-by-file API — it's for lookups, not bulk transfer.
- Don't assume a pre-existing local folder is a clean destination; verify.
- Don't fight GitHub's 100MB limit with LFS for content that isn't actually
  wiki material in the first place.
- Don't let converted Markdown filenames collide — always fold in the
  source extension.
- Don't dedupe cross-folder at the file-storage layer (that's intentional
  user organization) — only dedupe cross-folder at the RAG-chunk layer
  (where redundant chunks are pure waste).
