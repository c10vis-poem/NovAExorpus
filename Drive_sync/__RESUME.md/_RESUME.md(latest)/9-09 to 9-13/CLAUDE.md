# CLAUDE.md — Obsidian-Wiki.md----


## What this is

A migration of a personal Google Drive knowledge vault (`(MASTER_REPO).&WIKI.MD_VAULT`)
into this GitHub repo as a clean, Obsidian-compatible Markdown vault, plus a
JSONL chunk library for RAG retrieval over the large reference docs.

**STATUS 2026-07-31: the migration has been MERGED** into
`claude/app-crash-landing-yc955p` — the active branch for both this repo and
`c10vis-poem/Horizons-UI`. It originated on
`claude/drive-obsidian-migration-th115b`.

`main` is **still an empty tree** and must not be used as a base. Four
`docs/mirror-*` chunk branches also exist carrying only 82 files between them
(`chunk3`'s head is a *Revert*) — they are superseded, ignore them.

**Always `git branch -a` before choosing a base.** In these repos more real
work sits on unmerged branches than on `main`.

## Repo structure

```
#AESOP_HORIZONS-UI_Master/   \
#HORIZONS-main/                > mirror the 5 top-level Drive folder names exactly
#RESEARCH DOSSIER 1&2/        /
#Useful_knowledge_/          /
yJSONL_data.bank_/           /

_DUPLICATES_REVIEW/    files that were exact-duplicate (same content hash) within
                        the SAME source folder — quarantined here instead of kept
                        twice. Cross-folder duplicates are NOT touched; the same
                        doc appearing in multiple top-level folders is intentional
                        (operator's own access-pattern organization) and both
                        copies stay in place.

RAG_LIBRARY/            JSONL chunks of large/dense reference docs (≥3000 words),
                        mirroring the source doc's path with a .jsonl extension.
                        Deduped by CONTENT HASH ACROSS THE WHOLE VAULT (not just
                        per-folder) — a doc that appears in 5 folders only gets
                        chunked once here, since redundant chunks would just add
                        noise to retrieval. This is a different dedup scope than
                        the file-storage layer above; both are correct for their
                        own purpose.

.migrate/               the conversion pipeline scripts (see below) — kept in
                        the repo in case another pass over Drive is needed later.
```

## What's still binary/excluded

Six files (model weights, an SDK zip, tool archives — none of it "wiki"
content) exceeded GitHub's 100MB hard limit and were dropped from the
migration entirely rather than fought with Git LFS, since they don't belong
in a docs vault. Each has a `<original-name>.EXCLUDED.md` stub left in its
original location noting what was there and why. The operator has copies of
these elsewhere.

## Conversion rules used

- **Documents convert to Markdown**: `.docx`/`.doc` (via `pandoc`), `.pdf`
  (via PyMuPDF text extraction), `.txt` (direct), `.mht`/`.mhtml` (parsed as
  MIME email via Python's `email` module to extract the `text/html` part,
  then run through `trafilatura` for clean article-text extraction — raw
  pandoc HTML conversion keeps nav/header chrome, trafilatura strips it).
- **Everything else passes through unchanged** — source code (`.ts`, `.rs`,
  `.kt`, `.py`, etc.), images, binaries, `.jsonl`, already-`.md` files. Several
  Drive folders (especially under `(AESOP.]build`) contain full cloned
  reference repos, not just notes — converting source code to Markdown would
  be destructive and pointless.
- **Converted filenames keep the source extension folded in**
  (`Foo.pdf.md`, `Foo.mht.md`) rather than just `Foo.md`. This is load-bearing,
  not cosmetic: a `.pdf` and a `.mht` of the same title in one folder used to
  collide on `Foo.md` and silently overwrite each other — three files were lost
  this way before the fix (recovered from git history; see commit history
  around 2026-07-30 for the incident). Do not revert to bare `{base}.md` naming.

## Scripts (`.migrate/`)

- `process_folder.py <src> <dupes_dest> <clean_dest>` — per-folder dedupe +
  Markdown conversion + relocation. Run once per top-level Drive folder.
- `build_rag_chunks.py <vault_root> <rag_out>` — content-hash-deduped chunking
  of large docs into `RAG_LIBRARY/`. Chunks by `##`/`###` heading when a doc
  has them, else fixed 500-word windows with 50-word overlap.

## Full skill

The complete Drive → Termux → GitHub migration workflow (including the
Termux/rclone/OAuth setup, the traps hit along the way, and how to run this
again for future Drive content) is documented as a skill:
`.claude/skills/drive-to-obsidian-migration/SKILL.md`.

## Known open items

- `_DUPLICATES_REVIEW/` (15 files) needs a human pass to actually delete —
  nothing auto-removes it.
- The six `.EXCLUDED.md` stubs point at binaries not stored in this repo.
- This branch has not been merged to `main`.


---

## Session 20 handoff — 2026-07-31

### What landed

The full migration (1,300 files) was merged after being found sitting unmerged
while `main` was empty and a competing 82-file partial mirror was in use. Vault
is now **1,305 files · 363 md · 96 jsonl**, plus `RAG_LIBRARY` (46 docs / 1,786
chunks) and its BM25 index.

New docs at the vault root:

| File | What |
|---|---|
| `CRASH-ANALYSIS-2026-07-31.md` | the Horizons boot-crash investigation, with the on-device procedure to get the missing stack trace |
| `ROUTER-STEREO-STACK-SPEC.md` | Router tile = component stereo stack (CD=models, tuner=params, cassettes=runtimes) |
| `MONITOR-ARCADE-CABINET-SPEC.md` | Monitor tile = arcade cabinet, CRT screen, pop-out tabs |
| `TERMINAL-SPEC.md` | Terminal = fakesteak matrix cascade + in-shell saved-command drop-down |

All three UI specs are **direction only — not to be built yet.**

### The authority model (operator, LAW)

Series circuit. **Settings** supplies and may hand a config to the Router but has
**no authority to run it**. **Monitor is the switch in the loop** — stores
nothing, dispatches, and holds the verdict. **Router** is fuse box + breaker:
carries current, doesn't argue. Validation is **live at flip time** but the check
is the **Monitor's**. The operator explicitly rejected Router-as-gatekeeper.

### Source-trust

Two data-bank documents are AI transcripts, not specs — the "Gemini duel" doc
retracts its own central claim mid-document, and `2. 2026-07-17.md` is one the
operator calls a snow job. Architecture in them is canon; implementation claims
are not.

### Getting more from Drive

Drive is the **source of truth** and is directly reachable via
`mcp__Google_Drive__*`. Never conclude something doesn't exist from the git
repos alone. Use the `drive-to-obsidian-migration` skill to pull more — do not
hand-sync file by file.

<!-- code-review-graph MCP tools -->
## MCP Tools: code-review-graph

**IMPORTANT: This project has a knowledge graph. ALWAYS use the
code-review-graph MCP tools BEFORE using Grep/Glob/Read to explore
the codebase.** The graph is faster, cheaper (fewer tokens), and gives
you structural context (callers, dependents, test coverage) that file
scanning cannot.

### When to use graph tools FIRST

- **Exploring code**: `semantic_search_nodes_tool` or `query_graph_tool` instead of Grep
- **Understanding impact**: `get_impact_radius_tool` instead of manually tracing imports
- **Code review**: `detect_changes_tool` + `get_review_context_tool` instead of reading entire files
- **Finding relationships**: `query_graph_tool` with callers_of/callees_of/imports_of/tests_for
- **Architecture questions**: `get_architecture_overview_tool` + `list_communities_tool`

Fall back to Grep/Glob/Read **only** when the graph doesn't cover what you need.

### Key Tools

| Tool | Use when |
| ------ | ---------- |
| `detect_changes_tool` | Reviewing code changes — gives risk-scored analysis |
| `get_review_context_tool` | Need source snippets for review — token-efficient |
| `get_impact_radius_tool` | Understanding blast radius of a change |
| `get_affected_flows_tool` | Finding which execution paths are impacted |
| `query_graph_tool` | Tracing callers, callees, imports, tests, dependencies |
| `semantic_search_nodes_tool` | Finding functions/classes by name or keyword |
| `get_architecture_overview_tool` | Understanding high-level codebase structure |
| `refactor_tool` | Planning renames, finding dead code |

### Workflow

1. The graph auto-updates on file changes (via hooks).
2. Use `detect_changes_tool` for code review.
3. Use `get_affected_flows_tool` to understand impact.
4. Use `query_graph_tool` pattern="tests_for" to check coverage.
# 