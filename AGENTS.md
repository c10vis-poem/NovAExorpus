# AGENTS.md

Repository: `NovAExorpus`

Authority: NovÆxorpus Master Canon Specifications

## RULE 1 — NO ACTION WITHOUT AN EXPLICIT PROMPT

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## RULE 2 — READ THE REPO'S OWN AGENTS.MD AND RESUME.MD FIRST

Before doing anything else in any of the operator's repos — before
investigating, before answering a question about that project's state —
check for and read that repo's own AGENTS.md and RESUME.md. Step one,
every session, every repo, no exceptions.

`AGENTS.md` is the single instruction file for every engine. A repo's
`CLAUDE.md` is only `@AGENTS.md` plus things only Claude Code can use.

## RULE 3 — DOCUMENTS 00–05 ARE WRONG

`00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md`,
`01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md`, `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md`,
`03_DUAL_OPERATIONAL_HARNESS_AND_MCP_SPEC.md`,
`04_ON_DEVICE_INGESTION_AND_W5H_FRAMEWORK.md` and
`05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` all contain inconsistencies
and incorrect statements (operator, 2026-09-28). Never cite them as truth.
The grill-with-docs session replaces them. (The `01_raw_sources/`…
`05_episodic_logs/` folders are unrelated.)

## RULE 4 — MOST OF THE CORPUS HAS NOT BEEN READ

Fewer than ~150 files have honestly been read and implemented into the
plan; 1,000+ remain (operator estimate, 2026-09-28; the vault holds ~4,000
markdown files). No record exists of which files were read —
`manifest.jsonl` only lists 585 converted files, and `GRILL-MANIFEST.md` is
empty. Never claim the plan reflects "the corpus". Say which files you
actually read.

## GH workflow (every repo)

1. Use the operator's `c10vis-poem` fork of every tool. At session start,
   sync every fork with upstream so everything is current. A fork with its
   own commits gets an upstream PR — never a force-sync.
2. Work on a branch, never directly on `main`/`master`.
3. At the END of the session — once, not after every change — push.
   GitHub's secret scanning and push protection are the secret scan (plus
   the gitleaks CI job); an agent grepping is not a substitute.
4. CI runs, PR opens, auto-merge into `main` on green.
5. Leave the branch in place after merge — do not delete it.
6. Nothing sits unmerged: every pending change, unpushed commit and open
   PR is merged or flagged as needing a fix.
7. Never change these rules or invent exceptions when something breaks —
   report the problem and ask the operator.

Enforced by `~/bin/sync-forks` (session start) and `~/bin/ship-session`
(session end) on the operator's phone. The vault syncs through the
GitSync Portal plugin on the `vault-sync` branch, which goes through the
same PR → CI → auto-merge gate.

Source: operator-confirmed 2026-09-13, restated and extended 2026-09-28.

## Task observer (every engine)

Run the task-observer skill (`c10vis-poem/aesop-task-observer`) before the
first tool call of any session and before proposing a plan. Every harness
carries the skill; observations go to one shared log in this vault
(`skill-observations/`). Each harness runs the skill itself.

## Start here (any device, any agent, any account)
Everything a new session needs is in this vault (synced to `c10vis-poem/NovAExorpus`), not on one phone:
1. `RESUME.md`: current state, open items in order, exact commands.
2. `PENDING.md`: durable backlog. `BOARD-INTAKE.md`: decisions and long-term threads.
3. `handoff/<date>/`: the reports behind RESUME (NPU install plan, branch review, models, voice, remote access, skills inventory, principles table).
4. `agents/AGENTS.global.md`: the shared rules every agent follows (copy of the phone's `~/.agents/AGENTS.md`; Claude Code imports the phone copy from `~/.claude/CLAUDE.md`).
5. `skill-observations/`: the one shared task-observer log, plus `cross-cutting-principles.md`.
Paths under `~/.claude/` (session-work, memory, hooks) exist only on the phone; RESUME never depends on them.

## Current stack (2026-10-23)
- **Dropped, do not set up, test or route through:** OmniRoute, mem0, Terrestrial Brain, OpenWiki, Qwen3-VL. (Strip-and-judge may still mine their ideas; see BOARD-INTAKE.)
- **On-device models:** GenieX on the Snapdragon 8 Elite NPU (HTP v79). AI Hub precompiled bundles run on GenieX's `qairt` runtime; any GGUF runs on its `llama_cpp` runtime (GGML Hexagon backend). Same GenieX endpoint. Details: `handoff/2026-10-23/npu-install-plan.md`.
- **Code intel / graphs:** code-review-graph (MCP), graphify. **Vault:** Obsidian + GitSync.
- **Secrets:** sops+age store in the private repo `c10vis-poem/NvAEx-Recaps` (`nvaex-secret`). Never write keys here: this repo is PUBLIC.
- **Enforcement (Claude Code on the phone):** hooks in `c10vis-poem/Aesop-Xi/hooks/` (README there). Agents may not change Claude Code settings, delete enforcement state, or turn anything off in any repo without the operator naming it.

## Cross-engine compatibility (this file only — tool-agnostic)

This file is read by any agent, not just Claude Code. Two rules that follow
directly from testing across engines:

- **Honey for Devs applies universally** — natively in Claude Code, as a
  text-strip layer in Codex, as a Cordis plugin in DeepSeek Harness (dsh).
  Apply its rules regardless of which engine is running.
- **task-observer / GSD-style skill scaffolding is Claude-Code-only.** Codex
  cannot parse markdown skill wrappers or the dual-layer activation protocol;
  dsh's sandboxed plugin layer blocks task-observer's observation-log writes
  entirely. Do not expect either to work, or try to force them, under Codex
  or dsh — that's the `.claude/` directory's job, not this file's.
- Claude Code and any local engine (Prime Agent, Codex, dsh) are never active
  in the same repo directory at the same time — running two simultaneously
  causes git-lock and file-write races.

## Agent skills

### Issue tracker

GitHub Issues on `c10vis-poem/NovAExorpus`, via `gh -R c10vis-poem/NovAExorpus`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: root `CONTEXT.md` + `docs/adr/`, created lazily by `/domain-modeling`. See `docs/agents/domain.md`.
