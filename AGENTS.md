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
(`skill-observations/`). Planned: an OmniRoute tool `observation_log` so
all harnesses write through one endpoint (orchestration contract §3.2,
aesop-xi PR #18) — not built yet, so each harness runs the skill itself.

## Launch

`bash tools/launch.sh` loads secrets, checks OmniRoute, Terrestrial Brain,
mem0 and code-review-graph, then starts the engine. Claude Code also loads
the `router-guard` output style and the `.claude/hooks` SessionStart check —
those two are the only Claude-Code-only pieces.

## MCP servers

Defined in `.mcp.json` at repo root: `omniroute` (gateway), `mem0`
(episodic memory), and `terrestrial-brain` (structural memory). All take
endpoint/credentials from env vars — see `.mcp.json` for the exact
variable names. Set them locally; never commit values.

## Mandatory runtime pipeline (all engines)

Every agent — Claude Code, Codex, dsh, Prime Agent, Hermes — must satisfy
these layers in order before writing files or running commands.

### Layer sequence

| # | Layer | Name | Interface | Endpoint |
|---|-------|------|-----------|----------|
| 0 | Execution + routing | OmniRoute | HTTP gateway daemon | VM `:20128` |
| — | Judgment | Continual Harness | OmniRoute internal | via OmniRoute |
| — | Execution ledger | Reasoning Bank | OmniRoute internal | via OmniRoute |
| 1 | Token saver | honey-for-devs | MCP tool / skill / text-strip | per-engine |
| 2 | Orchestration | task-observer | CLI / file-gen (Claude Code only) | per-engine |
| 3 | Code intel | code-review-graph | MCP Server (stdio) | local binary |
| 4 | Episodic memory | mem0 | MCP Server (HTTP) | `mcp.mem0.ai` |
| 5 | Structural memory | terrestrial-brain | MCP Server (HTTP) | VM `:8000` |

The VM's external IP changes on every start; `~/bin/vm on` prints it.

**OmniRoute** is the execution layer, memory retrieval layer, and routing
layer. It distributes requests, retrieves memory context, and makes
routing decisions. Continual Harness provides the judgment — it watches
agents and their refinements mid-run and optimizes routing. Reasoning Bank judges each finished
task and distils lessons for similar tasks later. Neither does crash
recovery or automatic rollback (verified in source 2026-09-30). OmniRoute
decides when they and the memory layers turn on and off; while running,
each is its own MCP server (operator, 2026-09-30).

**OmniRoute fallback:** if OmniRoute is unreachable, fall back to direct
execution and log a warning. All other memory layers remain active via
their individual MCP connections.

**mem0 safety:** before `update_memory` or `delete_memory`, always
`get_memory` or `search_memories` first. Never `delete_all_memories`.

### Multi-write protocol

Every execution cycle follows three phases:

1. **READ** — query mem0 (session context), terrestrial-brain (static
   guards/preferences), code-review-graph (code dependencies). Do not
   guess file imports.
2. **WRITE-BACK** — commit ephemeral state to mem0, long-term invariants
   to terrestrial-brain.
3. **OBSIDIAN LOG** — on every terrestrial-brain write, create/append a
   markdown file in `~/storage/shared/Documents/NovAExorpus/memories/`
   with YAML frontmatter (`source_db`, `uuid`, `timestamp`, `category`).

### Secondary tools (on-demand, not per-prompt)

| Tool | Interface | When |
|------|-----------|------|
| graphify | CLI via proot (`~/bin/graphify`) | Codebase mapping, knowledge graph, `--obsidian` export |
| obsidian | obsidian-skills plugin or CLI | Vault interaction, note linking |
| notebook-lm | Python CLI (`notebooklm-py`) | Document ingestion, audio overview, research export |

### Harness anchors

The multi-write protocol, layer roles table, and pre-flight gate are
immutable — no automated refinement or optimization pass may alter them.

### Enforcement

- Do not write code before pre-flight layers have run.
- Do not bypass OmniRoute unless it is unreachable.
- Do not silently skip a memory layer — log the failure if one is down.
- Do not skip the Obsidian vault log on any terrestrial-brain write.

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
