# AGENTS.md

Repository: `NovAExorpus`

Authority: NovÆxorpus Master Canon Specifications

## RULE 1 — NO ACTION WITHOUT AN EXPLICIT PROMPT

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## RULE 2 — READ THE REPO'S OWN CLAUDE.MD AND RESUME.MD FIRST

Before doing anything else in any of the operator's repos — before
investigating, before answering a question about that project's state —
check for and read that repo's own CLAUDE.md and RESUME.md. This has been
the operator's standing convention for session handoff and current state
across their repos for months. It is not optional background reading; it is
step one, every session, every repo, no exceptions.

## GH workflow (every repo)

1. Feature branch (never commit to `main`/`master` directly).
2. Before every push, scan the diff for secrets/API keys; refuse to push if found.
3. Push, open a PR, track CI.
4. On green CI, auto-merge into `main` immediately.
5. Leave the branch in place after merge — do not delete it.
6. Forked repos: at the start of every session, sync the fork's default
   branch from `upstream` before any other work.

The point of this workflow is that everything reaches `main` — a branch
that never gets a PR opened, or a PR that never gets merged, is a failure
of this rule, not a valid alternative to it. Don't let work sit stranded.

Source: operator-confirmed 2026-09-13, cross-linked in `~/.claude/CLAUDE.md`
on the operator's device and in the `gh-workflow-convention` memory entry.

## Mandatory runtime pipeline (all engines)

Every agent — Claude Code, Codex, dsh, Prime Agent, Hermes — must satisfy
these layers in order before writing files or running commands.

### Layer sequence

| # | Layer | Name | Interface | Endpoint |
|---|-------|------|-----------|----------|
| 0 | Execution + routing | OmniRoute | HTTP gateway daemon | `http://34.31.112.77:20128` |
| — | Judgment | Continual Harness | OmniRoute internal | via OmniRoute |
| — | Execution ledger | Reasoning Bank | OmniRoute internal | via OmniRoute |
| 1 | Token saver | honey-for-devs | MCP tool / skill / text-strip | per-engine |
| 2 | Orchestration | task-observer | CLI / file-gen (Claude Code only) | per-engine |
| 3 | Code intel | code-review-graph | MCP Server (stdio) | local binary |
| 4 | Episodic memory | mem0 | MCP Server (HTTP) | `mcp.mem0.ai` |
| 5 | Structural memory | terrestrial-brain | MCP Server (HTTP) | `http://34.31.112.77:8000` |

**OmniRoute** is the execution layer, memory retrieval layer, and routing
layer. It distributes requests, retrieves memory context, and makes
routing decisions. Continual Harness provides the judgment — it watches
agents and their refinements mid-run, optimizes routing, and auto-rolls
back on error. Reasoning Bank records every agent execution step, maps
logic pathways, and enables crash recovery. Both are OmniRoute internals, not
standalone services.

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
