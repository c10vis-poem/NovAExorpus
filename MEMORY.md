# MEMORY.md — NovAExorpus (the vault)
Durable facts about this repo. Dated; newest first. Updated at session wrap-up.

## 2026-11-03
- **Operator order: never tell the operator "no repo, folder or session is attached" or "I can't find it".** In a cloud session that starts with an empty `/home/user`, the vault is already cloned at `/root/storage/shared/Documents/NovAExorpus`. About 200 repos are reachable (`list_repos`), and any of them attaches with `add_repo`. Find it yourself and read the startup files (AGENTS, RESUME, PENDING, MEMORY, newest `handoff/<date>/`) before the first reply. Then run `git log -10`: the newest commits can be newer than RESUME.
- **NvAEx-Recaps is the session archive, not a startup read** (operator, 2026-11-03). It's where every session drops its scratchpad and session archive. Open it only when broader session history is needed.
- **No CLAUDE.md is auto-loaded in cloud sessions.** The phone's `~/.claude/CLAUDE.md` isn't there, and the vault root only has `CLAUDE.md.original.md`. The operator wants startup instructions account-wide, not in a repo: the claude.ai profile preferences, plus the cloud environment setup script writing `~/.claude/CLAUDE.md`. A repo CLAUDE.md was made unasked and dropped (PR #70 closed, branch `claude/startup-claude-md` left).
- **The "Informations folder" in the claude.ai profile preferences doesn't exist.** Don't hunt for it; it stands for the startup files above.
- **Hooks are back on with a safety net** (operator, 2026-11-03; Aesop-Xi PR #84). In `hooks/run-hook.sh`: `#hooks-off`/`#hooks-on` master switch; override phrases in `hooks/override-phrases.txt` ("override", "I told you", "go ahead", ...) let every block through for the turn; a hook yields after 2 blocks per turn (6 for all hooks). Operator rule: no hook may hand the operator either/or choices, and the operator's word overrides any hook.
- **Last work before this session (2026-11-03):** vault PRs #67/#68 (greedy-crane consolidation, merged) and NvAEx-Recaps PR #10 (v3.3 Master Execution Runbook recovered). Neither RESUME was updated for them.

## 2026-10-31
- **greedy-crane** is the wiki admin plugin, stored at `plugins/greedy-crane/` (agents `wiki-admin` and `corpus-ingest`, skills, scripts, docs). Agent definitions use the full plugin path, because sessions don't always start in the vault root.
- **The wiki in `02_wiki_md` is not a wiki yet:** 519 of 537 pages are byte copies of clean files, and `manifest.jsonl` hashes the clean file instead of the raw source (P4, 2026-10-30).

## 2026-10-05
- **Private files were removed** from the public repo (PR #34); old commits still hold them until the operator runs the fresh-repo step (RESUME item 0b). `main`, `vault-sync` and GitSync's `lastSyncedCommit` were aligned 2026-10-05.
- **Private material never goes in here.** Personal memory, legal/financial, unfiled designs, billing → `Documents/private-memory/` (outside the vault, never synced). `*BILLING*.csv` is gitignored.
- **MASTER-AGENTS.md / MASTER-RESUME.md, `tools/build_masters.sh` and `master-files.yml` are retired (2026-10-20).** Decision 2026-10-16: pointers, not mirrors: the vault indexes the base repos instead of copying their files. Base repos' `notify-vault.yml` dispatches now have no receiver until the pointer index is built.
- **AGENTS.md is the only instruction file** (no CLAUDE.md in any base repo).
- **Target layout:** `__RESUME.md/__Builder-Guide_Directory-/Master_Dumbass_config/_#Repository-layout.txt` (00-governance … 10-exports), PRIORITY ONE together with `Master_dumbass_plan-session/`. `__RESUME.md/` is the work queue and dissolves into the layout during/after the grill. Docs 00–05 at the root are wrong (AGENTS Rule 3).
- **Device vault = exact mirror of this repo** (end goal): no nested copies, duplicates or extras. `Documents/Zip/` is a full backup copy (refreshed 2026-10-05). The nested mirror was moved to `Documents/NovAExorpus-nested-mirror/`.
- **GitSync** syncs on Obsidian startup only (no timer). It writes `*.conflict-android-*` copies when a file changes on both sides.

## 2026-10-08
- PDFs moved to `Merovingian's_keep/vault-pdfs/` (1,046 → 12 in the vault); rule: PDFs live in the keep unless no text version exists.
- NovA-Corpus condensed versions replaced their originals (17 docs, `type: condensed` frontmatter); originals in `_salvage/NovA-Corpus/originals/`.
- `tools/clean.py` + `tools/check.py` work again (vault-root layout, mutool, keep-aware source lookup, canary); `.migrate/` complete, BM25 index is JSON.
- `_quarantine/` → keep `vault-moved/`; `WebView/` deleted + gitignored; `qairt_/` stays (gitignored, referenced by NPU-ON-DEVICE.md).
