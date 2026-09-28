# OBSIDIAN Master Wiki — vault root

Canonical knowledge vault for **Novus Agenti / Omni Claw / Horizons** and the
**AESOP** split-agent stack. Markdown is the source of truth; the JSONL indexes
are derived and rebuildable.

## Tree

```
#AESOP_HORIZONS-UI_Master/   the build corpus
  (AESOP) REPO.data_bank/      WHAT THE APP IS — read first
  (AESOP.]build/               HOW IT'S BUILT — per-tool folders
  (BUILD.it)_JHA/              running state: SOTU, action plan, job log
#HORIZONS-main/              the app repo's own docs, mirrored
#RESEARCH DOSSIER 1&2/       research corpus
#Useful_knowledge_/          general reference
RAG_LIBRARY/                 JSONL chunks + BM25 index + query script
yJSONL_data.bank_/           per-topic JSONL chunk files
_DUPLICATES_REVIEW/          quarantined dupes from the migration
CLAUDE.md                    migration pipeline + vault conventions
```

**1,305 files · 363 markdown · 96 jsonl.** Originals (docx/pdf/mht/txt) are kept
alongside their Markdown conversions.

## Reading order

1. `#AESOP_HORIZONS-UI_Master/(AESOP) REPO.data_bank/(1a)-Horizons.Ui-defined/4. Technical Specification The Four Rooms & Seven-Tile Modular Architecture.md`
2. `.../The Horizons Workflow From Storage to Switch.md` — Landing → Verification → Activation
3. `.../The Horizons Workbench A Guide to Your Modular Intelligence Engine.md`
4. `#AESOP_HORIZONS-UI_Master/(BUILD.it)_JHA/SOTU-2026-07-27.md`
5. [[CRASH-ANALYSIS-2026-07-31]] — boot-stability investigation
6. [[ROUTER-STEREO-STACK-SPEC]] · [[MONITOR-ARCADE-CABINET-SPEC]] · [[TERMINAL-SPEC]] — tile UI direction

## The core law

> **Daemons stay dumb, the user is the loader.**
> Never auto-grab runtimes or files mid-flight.
> The pipeline is strictly linear: **Define → Validate → Execute.**

## Authority model (operator, 2026-07-31)

The circuit is **in series** — two independent authorities, both required:

| Tile | Role |
|---|---|
| **Settings** | supply. Holds assets/keys. Can hand a config to the Router. **No authority to run it.** |
| **Terminal** | writes the fuse spec (parameters only). Defines; never executes. |
| **Monitor** | **the switch in the loop.** Verifies the wiring. Open or loose → no circuit, however perfect the fuse. Stores nothing, but **dispatches**. |
| **Router** | fuse box + breaker. The fuse must carry the load; you throw the breaker. Doesn't argue — carries current. |

A perfect fuse in a good breaker with a loose wire on the dial is a dead
circuit. Settings handing something to the Router is just running wire — it
confers no permission.

**Validation must be live, not cached.** A switch in series is a continuous
conductor; it holds no memory of having been fine earlier. Green-light state
must be checked at the moment of the flip — but the check is the **Monitor's**,
not the Router's. That is the one real defect in the current code
(`RouterPane.switchOn()` re-implements the check instead of consulting it).

## Source-trust warning

Two documents in the data bank are **AI chat transcripts, not specifications**:

- `Gemini oils up The Builder and challenges Claude to a duel...md` — its author
  **retracts its own central claim** partway through (that `geniex` can drive the
  NPU from a Termux shell — it cannot; SELinux blocks non-privileged shells from
  `/vendor/lib64`). Its `GenieX_*` C API is invented.
- `2. 2026-07-17.md` — the operator's own verdict on most of it: *"a complete
  snow job... it failed every single aspect but it made everything worse."*
  The **architecture** dictated in it is canon; the **claims of implementation**
  are not.

Where transcripts and specs disagree, **the specs win** — they were written
afterwards to overrule them.

## Provenance note — read before "adding" anything

The complete Drive→Obsidian migration lives on
`claude/drive-obsidian-migration-th115b` and was merged here on 2026-07-31.
Before that, `main` had been reset to an **empty tree** and four
`docs/mirror-*` chunk branches carried only 82 files between them
(`chunk3`'s head is a *Revert* of the AESOP/AIDER/CLAUDE.CODE mirror).

**Always `git branch -a` before choosing a base.** More work exists on
unmerged branches in these repos than on `main`.

To pull more Drive content, use the `drive-to-obsidian-migration` skill —
don't hand-sync. Google Drive is reachable directly via the
`mcp__Google_Drive__*` tools.
