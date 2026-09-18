# RESUME.md — Session Ledger

Repository: NovAExorpus (renamed from `novae-xorpus` 2026-09-15)
Last session: 2026-09-18

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

## RUNTIME INFRA VERIFIED LIVE (updated 2026-09-18)

- **Terrestrial Brain**: running on GCP VM 34.31.112.77:8000, systemd-managed.
  Full round-trip proven 2026-09-18: phone→TB→OpenRouter→Postgres→vault markdown.
  Verification code LUNAR-42-DELTA in DB (id `8c79f79f`) and vault file
  `memories/2026-09-18-The-NovAExorpus-vault-verification-code.md`.
  Auth: `x-brain-key` header, key in `$PREFIX/etc/secrets.env` as `TB_MCP_KEY`.
- **mem0**: cloud MCP at `mcp.mem0.ai`, search + write verified 2026-09-18.
  Plugin `mem0@mem0-plugins v0.3.0` installed, doctor passes, auth connected.
- **code-review-graph**: 2 repos indexed (NovA-terrestrial-brain, aesop-xi).
  Runs via proot-distro debian.
- **OmniRoute**: running on VM port 20128, has dashboard UI. Not yet wired
  as MCP (placeholder in `.mcp.json`).
- Postgres 18.2 on VM `127.0.0.1:5432` (DB: `terrestrial_brain`, role: `brain_app`)
- pgvector v0.8.6 available
- Obsidian vault at `~/storage/shared/Documents/NovAExorpus/` — TB writes
  to `memories/` subfolder automatically on every thought/task/project insert.
- `memory-triage` skill symlinked into `~/.claude/skills/`
- task-observer: 2 observations recorded, working

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

## WHAT LANDED 2026-09-18

- **TB round-trip proven end-to-end** — LUNAR-42-DELTA fact written through
  full chain: phone → TB MCP → OpenRouter (split + embed) → Postgres insert
  → vault markdown file with YAML frontmatter
- **TB MCP auth fixed** in `~/.claude.json` — placeholder `REPLACE_WITH_MCP_ACCESS_KEY`
  replaced with actual key from `$PREFIX/etc/secrets.env`
- **NovAExorpus repo**: committed router-guard output style, MCP config
  (`.mcp.json`), agents (corpus-architect, builder), pipeline wiring,
  hooks, settings (16 files, commit `55ca7fc` / cherry-picked to `f31cdb3`)
- **TB schema fixes on VM** (not in repo migrations):
  `thoughts.reliability` changed double precision→text, added columns
  `reference_id`, `note_snapshot_id`, `metadata`, granted `brain_app` access
- **Launch script**: `tools/launch.sh` — sources secrets, starts Claude Code
  with router-guard output style in corpus root
- **Stale branches identified** — 6 local branches from merged PRs,
  `master` remote branch 6 ahead / 23 behind (superseded content)

## WHAT'S NOT DONE

- Push `feat/pipeline-wiring-2026-09-18` branch + PR (credential classifier
  blocked earlier push; may need manual push or history rewrite)
- Delete stale remote branches (master, claude/*, happy-ending-*, session-close-*)
- Close draft PR #7 (`restructure/drive-file-tree`) if superseded
- OmniRoute MCP wiring (placeholder in `.mcp.json`, needs API key)
- mem0 vault export (write mem0 memories to vault markdown like TB does)
- Vault git remote not added, Obsidian Git plugin not configured
- Shell alias `cc` in `.zshrc`
- Global `~/.claude/CLAUDE.md` rewrite (deferred per memory)
- Reasoning Bank / Continual Harness (spec-only, not on disk)

## FIRST ACTION NEXT SESSION

```bash
cd ~/repos/NovAExorpus
bash tools/launch.sh
```

The CLAUDE.md session start protocol auto-fires: searches mem0, checks TB
for open tasks, reads this RESUME.md. No manual prompt needed.

## Sources actually read this session (not from memory/summary)

7 RFMC files in full (`Repo-Files-Map-core/`), `Unified architecture and
memory detailed guide.txt`, `Knowledge and memory subsystem..txt`,
`02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md`, `ob1_vs_mem0_memory_division.md.pdf`,
`~/repos/OmniRoute/README.md`, `~/repos/clovis-mem0-vingiaN/`'s
`integrations/openclaw/skills/memory-triage/SKILL.md` +
`claude-code-plugin/.claude-plugin/plugin.json` + `marketplace.json`, all 7
base repos' current CLAUDE.md/AGENTS.md/PENDING.md/RESUME.md, mem0 hosted
MCP verified via 5 real memory writes with event IDs.
