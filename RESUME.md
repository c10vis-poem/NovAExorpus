# RESUME.md — Session Ledger

Repository: NovAExorpus (renamed from `novae-xorpus` 2026-09-15)
Last session: 2026-09-15

## REPO WAS RENAMED THIS SESSION

`novae-xorpus → NovAExorpus` (machine-retrievable, no Æ, matches the Obsidian
vault name at `Documents/NovAExorpus/`). GitHub redirect still works, but the
canonical URL is now `github.com/c10vis-poem/NovAExorpus`. Cross-refs in live
docs (README/CLAUDE/AGENTS/RESUME/PENDING/MAP/NAMING-CANON) swept across all
7 base repos; historical archive dirs (`02_wiki_md/`, `clean_md/`, `03-check/`)
deliberately left as-is.

Same-session renames for context:
- `novaexopia → NovAExopia`
- `one-skill-to-rule-them-all-aesop → aesop-task-observer`

## WHAT LANDED THIS SESSION

- **3 GitHub renames** (above) + full cross-ref sweep across 7 base repos
  (all PRs merged: NovAExorpus #14, NovAExopia #5, aesop-xi #12, novus-aesc
  #5, novus-aexenti #5, novus-aeyre #5, horizons-ui #1)
- **314-file diverged content restored to main** — the `~/novae-xorpus`
  second checkout (branch `session-close-master-regen-2`) held content that
  had been on this repo pre-Doc-05-cleanup (commit `b075262`) and got merged
  back via PR 15 (bulk merge with `-X ours`) + PR 16 (cherry-pick the
  root-level files the squash-merge missed: `NAMING-CANON.md`,
  `MASTER-{RESUME,CLAUDE}.md`, `SOURCE-RETRIEVAL-MAP.md`, `LAPTOP-TRICK.md`,
  `GRILL-MANIFEST.md`, `unresolved.md`, `tools/regenerate_masters.sh`,
  `handoffs/`, `skills/corpus-verify/`, `projects/`)
- **`~/novae-xorpus` diverged checkout `rm -rf`'d** after merge
- **Post-commit hook repointed** from `~/novae-xorpus/tools/regenerate_masters.sh`
  to `~/repos/NovAExorpus/tools/regenerate_masters.sh` (hook lives in
  `~/repos/aesop-xi/.git/hooks/post-commit`; `.bak-2026-09-15` preserved)
- **Memory-layer reference section + `tools/bootstrap.sh` wrapper** added
  (PR 17 merged). `CLAUDE.md` now points at `aesop-xi/CLAUDE.md §Runtime
  memory stack` as the canonical source; not duplicated here.
- **`CLAUDE.md.original.md` backup** created per honey-memory restore-path
  rule.

## THE ARCHITECTURE (SHORT VERSION)

NovAExorpus is **the vault** — 5+1 tier cognitive memory:
- `01_raw_sources/` — cold sensory archive (read-only)
- `02_wiki_md/` — semantic memory (OpenWiki TUI-managed)
- `03_recall_cache/` — working memory accelerator (JSONL + vectors)
- `04_skills_runtime/` — procedural memory (skills + runtimes)
- `05_episodic_logs/` — episodic (trajectories + RLVR + Reasoning Bank
  flushes)
- `MAP.md` + `manifest.jsonl` — metacognitive routing index

**Runtime memory infrastructure** (mem0, terrestrial-brain, OmniRoute,
reasoning-bank, continual-harness) lives canonically in **aesop-xi**, not
here. See `aesop-xi/CLAUDE.md §Runtime memory stack`. This repo is the DATA;
that repo is the RUNTIME.

3-plane split confirmed 2026-09-15:
- **aesop-xi** = data plane (memory + routing)
- **novus-aexenti** = cognitive plane (MoE brain)
- **NovAExopia** = execution plane (harnesses + tools)

## RUNTIME INFRA VERIFIED LIVE

- Postgres 18.2 on `localhost:5432` (data: `~/pgdata/`)
- pgvector v0.8.6 available
- mem0 hosted MCP round-trip verified with `~/.mem0/.env`
  (`MEM0_API_KEY` + `MEM0_MCP_TOKEN`, chmod 600, auto-loaded by ~/.zshrc)
- `mem0@mem0-plugins v0.3.0` plugin already installed (2026-09-09)
- `memory-triage` skill symlinked into `~/.claude/skills/`

## CORRECTION TO PRIOR "PHASE 1-4 COMPLETE" CLAIM

Still stands from earlier this session: 585 files cleaned via `tools/clean.py`
is a fraction of the ~5000+ real corpus scope in `Drive_sync/LlmWiki/` (7,307
files in vault total). Not "complete" — a fraction. See PENDING.md #2.

## PRIORITY ORDER (operator-stated, do not resequence)

1. **Wire 4 layers operationally** — biggest open call: OmniRoute
   deploy-target (see `aesop-xi/PENDING.md`).
2. **Full LlmWiki ingestion** — 5000+ files, every one (not sampled), via
   `tools/check.py` / `clean.py` / `chunk.py`. Distribute condensed content
   into the correct base repo per RFMC's 8-repo model.
3. Post-corpus loose ends.
4. **Grill session** — mattpocock-skills:grilling / grill-with-docs. AFTER
   corpus.
5. **15-20 tools/skills/scripts** build-out.

## FIRST ACTION NEXT SESSION

```bash
cd ~/repos/NovAExorpus
bash tools/bootstrap.sh
```

Then read `aesop-xi/CLAUDE.md §Runtime memory stack` for the architecture,
and pick the OmniRoute deploy target.

## Sources actually read this session (not from memory/summary)

7 RFMC files in full (`Repo-Files-Map-core/`), `Unified architecture and
memory detailed guide.txt`, `Knowledge and memory subsystem..txt`,
`02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md`, `ob1_vs_mem0_memory_division.md.pdf`,
`~/repos/OmniRoute/README.md`, `~/repos/clovis-mem0-vingiaN/`'s
`integrations/openclaw/skills/memory-triage/SKILL.md` +
`claude-code-plugin/.claude-plugin/plugin.json` + `marketplace.json`, all 7
base repos' current CLAUDE.md/AGENTS.md/PENDING.md/RESUME.md, mem0 hosted
MCP verified via 5 real memory writes with event IDs.
