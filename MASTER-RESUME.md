# Master RESUME overview (auto-generated — do not hand-edit)

Regenerated: 2026-09-15T22:08:32Z
Source: NovAExorpus/tools/regenerate_masters.sh

One overview across every attached project. Edit each project's own
RESUME.md, not this file — it's rebuilt from those every time.

---

## NovAExopia

# RESUME.md

Repository: `NovAExopia`

Authority: NovÆxorpus Master Canon Specifications

---

## NovAExorpus

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

---

## aesop-xi

# RESUME.md — Session Ledger

Repository: `aesop-xi`
Last session: 2026-09-15 (second session this date)

## WHAT LANDED THIS SESSION

- **terrestrial-brain MCP server brought up from scratch.** Database
  `terrestrial_brain` created (role `brain_app`, 23 migrations applied),
  pgvector `CREATE EXTENSION vector` done, MCP server running on
  `localhost:8000/mcp` via system deno. Round-trip verified with
  `tools/list` returning `search_thoughts`, `list_thoughts`, etc.
  Env vars `TB_MCP_URL=http://localhost:8000/mcp` and `TB_MCP_KEY` set
  in `~/repos/NovA-terrestrial-brain/local-mcp/.env.local`.
- **mem0 CLI plugin fixed.** API key was in wrong directory since Sep 9
  (`~/.mem0/claude-code-plugin/` instead of
  `~/.claude/plugins/data/mem0-mem0-plugins/`). All doctor checks now
  passing, hooks firing (170+ events captured this session). Both MCP
  and CLI paths verified working.
- **mem0 MCP populated.** 14+ memories written covering architecture,
  workflow, infrastructure, preferences, priorities. Was completely empty.
- **File-based auto memory updated.** 11 entries (was 7, all stale from
  Aug 28–31). Updated PENDING.md/unresolved.md workflow, added session
  startup rules, repo-must-be-runnable feedback, architecture, runtime state.
- **NovAExorpus/projects/ fully wired.** All 7 base repos now have
  symlinks for RESUME.md, CLAUDE.md, PENDING.md, AGENTS.md. Was only
  aesop-xi with 2 of 4. horizons-ui AGENTS.md created from template.
- **OmniRoute deploy-target decided.** Google Cloud VM (operator choice).
- **CLAUDE.md updated.** `unresolved.md` references changed to
  `PENDING.md` throughout session handoff workflow section.
- **scripts/bootstrap-stack.sh deleted** (duplicate bootstrap, caused
  agent confusion). CLAUDE.md historical reference marked retired.

## RUNTIME INFRASTRUCTURE VERIFIED LIVE

- **Postgres 18.2** on `localhost:5432` (data: `~/pgdata/`)
- **pgvector v0.8.6** — `CREATE EXTENSION vector` done in
  `terrestrial_brain` database
- **terrestrial-brain MCP** on `localhost:8000/mcp` (open-brain v1.0.0,
  deno process). Start: `cd ~/repos/NovA-terrestrial-brain/supabase/functions/terrestrial-brain-mcp && LOCAL_PG_URL="postgres://brain_app:brain_local_dev@127.0.0.1:5432/terrestrial_brain" MCP_ACCESS_KEY="$(grep MCP_ACCESS_KEY ~/repos/NovA-terrestrial-brain/local-mcp/.env.local | cut -d= -f2)" OPENROUTER_API_KEY="$OPENROUTER_API_KEY" deno run --allow-net --allow-env --allow-read --allow-write index.ts`
- **mem0 hosted MCP** verified with key at `~/.mem0/.env`
- **mem0 plugin** (v0.3.0) hooks firing, key at
  `~/.claude/plugins/data/mem0-mem0-plugins/api-key`
- **OmniRoute** NOT deployed — goes on Google Cloud VM (P0)

## STANDING RULES

- 3-plane split: **aesop-xi = data · novus-aexenti = cognitive ·
  NovAExopia = execution**. NovAExorpus is the vault.
- **Never call mem0/terrestrial-brain directly** — route through
  OmniRoute once deployed. Until then, direct calls are acceptable.
- Repo-specific backlog: **PENDING.md** (not unresolved.md).
  Cross-repo backlog: `~/repos/NovAExorpus/unresolved.md`.
- **Post-grill only**: Novus-Agenti demolish + repo-shape decisions.

## PRIORITY ORDER (operator-stated, do not resequence)

1. **OmniRoute on Google Cloud VM** — deploy, configure, point
   `tools/omniroute/` + `skills/omniroute/` at it
2. **Full LlmWiki ingestion** — 5000+ files
3. Post-corpus loose ends
4. **Grill session** — AFTER corpus
5. **15-20 tools/skills/scripts** build-out

## FIRST ACTION NEXT SESSION

```bash
cd ~/repos/aesop-xi
bash tools/bootstrap.sh
```

Then:
1. Read this file + CLAUDE.md + PENDING.md
2. Run `mem0:status` — verify `api_key_configured: true` and events
   incrementing (use `--plugin-data-dir ~/.claude/plugins/data/mem0-mem0-plugins`)
3. Verify terrestrial-brain is running: `nc -z localhost 8000`
   (if not, start it per the command in RUNTIME INFRASTRUCTURE above)
4. Check OmniRoute VM status — is it deployed yet?

## Related handoffs

- Cross-repo backlog: `~/repos/NovAExorpus/unresolved.md`
- Repo-specific backlog: `PENDING.md` (this repo)
- NovAExorpus/projects/ has symlinks to all 7 base repos' handoff docs

---

## horizons-ui

# RESUME.md — horizons-ui

**2026-09-15:** Repo wiped and recreated empty. Old history (38 PRs,
"Novus Agenti / Omni Claw") archived in `raw-databank/horizons-ui-full-history.bundle`.
Nothing built yet — this is session zero.

---

## novus-aesc

# RESUME.md — novus-aesc (Æsc)

**Status:** Scaffold. Nothing runs yet. Build order item #2 (see `docs/BUILD-ORDER.md`), blocked on #1 (DroidDesk install) per operator sequencing — do not re-sequence.

## Current state

- Repo layout, docs (`CLAUDE.md`, `README.md`, `STACK-MAP.md`, `docs/BUILD-ORDER.md`, `protocol/README.md`, `salvage/README.md`) already written and operator-declared — not touched here.
- `salvage/` — 5 extraction targets defined (NPU loader, ADB loopback, Chromium integration, terminal render, model router), none pulled from `horizons-ui` yet (all unchecked in `salvage/README.md`).
- `manifest.jsonl` — empty (`entries: []`).
- Known blocker: the Watchdog daemon doesn't survive Android process management (MIUI/One UI/Android 13+ kill it). Fix is a `ForegroundService`, not yet built.

## Prior art not yet reviewed (per `docs/BUILD-ORDER.md`)

`NovAExorpus/unresolved.md` item 10: a bridge daemon (`deploy/phone/bridge/aesopd.py`), a supervised `llamad` daemon with real NPU/Hexagon offload (`deploy/phone/daemons/`), `protocol/bridge-protocol.md`, and a `termux-helper` skill already exist in `aesop-xi` — merged from `origin/claude/wiki-quinn-npu-local-m1crql`, never reviewed. May already cover most of this repo's task. Read before writing new daemon code.

## Document 05 vs. this repo's actual plan — flagged, not reconciled

`05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` sketches this repo's contents generically:
`src/main/java/com/horizons/ui/adb/`, `npu_watchdog/`, `scripts/`, `process-isolation/`,
`lmk-mitigation/`, `wireless-adb/`. This repo's actual operator-declared plan is more
specific and different in shape: `laptop-trick-tunnel/` (ADB loopback), `npu-watchdog/`
(underscore vs. hyphen naming also differs), `protocol/`, `salvage/` with 5 named targets.
Did not force this repo's layout to match Document 05's sketch — the existing plan is more
detailed and explicitly operator-declared ("Do not re-sequence"). Needs the user's call on
whether Document 05's sketch should be updated to match reality, or whether this repo should
be reshaped to match Document 05.

## Second master Drive folder — not found

Per Document 05, this repo's content source is `___Lex-Novi-Æxentis-Copiæ/--•💻_TERMUX_[>_]_main.` and `.../Reverse-Engineering` (both subfolders of a second master Drive folder). That folder has not been shared with this session as of this pass — checked `sharedWithMe = true and mimeType = 'application/vnd.google-apps.folder'`, only `__NovÆxorpus_LIVING_MASTER_CANON`, `22-Hooks`, `Termux ECC`, and `__NovÆxorpus(NÆX)` are shared. Nothing to pull from it yet.

## Next

1. Read the `aesop-xi` prior art above before writing any daemon code.
2. DroidDesk install (build order #1) is the actual blocker, not this repo.
3. `ForegroundService` rewrite for the Watchdog whenever salvage starts.

---

## novus-aexenti

# RESUME.md

Repository: `novus-aexenti`

Authority: NovÆxorpus Master Canon Specifications

---

## novus-aeyre

# RESUME.md — novus-aeyre

**Last updated:** 2026-09-07
**Branch:** `restructure/drive-file-tree`

## Current state

Voice: working scaffold, confirmed end-to-end via `--demo` (TTS → speaker →
STT round-trip, text matched). Currently lives in `aesop-xi/voice-engine/`
under Termux + Debian proot — temporary, moves here and gets wiped from
`aesop-xi`. Live mic loop not yet verified — only `--demo` has run.

Vision: not started. No code, no design beyond the stub directories.

Two real bugs already found and fixed, documented in `README.md` — don't
rediscover them: Moonshine STT's ~10s silent-failure ceiling, and the
two-part PulseAudio/proot audio bridge fix (ALSA-over-Pulse routing +
client-side SHM disabled).

## What was done this session

Checked this repo's Drive source material (`Æsc&Æyre` subfolder of
`___Lex-Novi-Æxentis-Copiæ`, per `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md`'s
14-subfolder mapping table, entry `Reverse-Engineering`). Confirmed via
`AUDIT_LEX_NOVI_AESOP_XI.md` that this material was already fully synthesized
into `NovAExopia/README_NOVAEXOPIA.md` and
`NovAExopia/01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md` — out of scope for this
repo. The raw subfolder itself is not shared with this Claude Code session
(only the audit summary is), so nothing further was retrievable to place
here. Added the missing section-kit files (`agent.md`, this file,
`unresolved.md`) per the corrected per-repo layout in
`NovAExorpus/project_novae_xorpus_repo_layout_correction.md` (see project
memory, not committed to this repo).

## Next

- Extract the voice engine from `aesop-xi/voice-engine/` into `app/audio/`,
  `app/vad/`, `app/stt/`, `app/tts/` per the planned layout in `README.md`.
- Verify the live mic loop before building further on it.
- Start the vision path — no design exists yet; check `aesop-xi` and
  `NovAExopia` first for anything already decided.

