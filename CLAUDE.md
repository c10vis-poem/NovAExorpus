# CLAUDE.md — NovAExorpus (Claude Code only)

Repository: `NovAExorpus` — NovÆxorpus Federated Master Corpus Root.

Tool-agnostic rules (apply to every engine, not just Claude Code) live in
`AGENTS.md` — read that first, every session.

## Output Style — router-guard

Activate with `/output-style router-guard` at session start, or launch
with `claude --output-style router-guard` (alias: `cc`). The style lives
at `.claude/output-styles/router-guard.md` (project-scoped) and
`~/.claude/output-styles/router-guard.md` (global fallback).

The style enforces the unified orchestration pipeline defined in the source
spec (output-style.md, pages 15-33):

```
[Agent] → honey + task-observer (pre-flight)
  → OmniRoute (gateway, routes to all backends)
    → mem0 / terrestrial-brain / code-review-graph
    → Reasoning Bank (passive execution ledger, crash recovery)
    → Continual Harness (passive prompt refinement, auto-rollback)
```

All engines (Claude Code, DeepSeek, Qwen, Hermes) hit the same pipeline
and the same backends. Only the loader differs per engine.

## Layer 1 — Output discipline (always active)

**Honey for Devs** and **task-observer** load before the first tool call.
Honey enforces minimum-code / minimum-words output. task-observer logs
observations for skill improvement. Both are non-negotiable gate layers.

Invoke `task-observer` before the first tool call of any session and before
writing or proposing a plan.

## Layer 2 — Memory & knowledge (4 independent MCP servers)

All defined in `.mcp.json` at repo root. Each is its own server — they are
NOT merged into a single endpoint.

| Server | Transport | Purpose | Endpoint |
|--------|-----------|---------|----------|
| **mem0** | HTTP (cloud) | Episodic memory (semantic search, entities, events) | mem0.ai cloud |
| **terrestrial-brain** | HTTP | Structural/Postgres memory (thoughts, projects, tasks) | GCP VM 34.31.112.77:8000 |
| **code-review-graph** | stdio | Code structure / AST knowledge graph | Local (proot debian) |
| **omniroute** | HTTP | AI gateway + async memory tap + model routing | GCP VM 34.31.112.77:20128 |

OmniRoute sits as an access/gateway layer — it routes outbound model
completions AND acts as an async memory tap (extracting trajectories, tool
traces, failure patterns into the memory layer). It does NOT replace the
individual MCP connections.

### Session start protocol

1. Search mem0 for prior context relevant to the current task.
2. Check terrestrial-brain for any open thoughts/tasks.
3. Read RESUME.md if it exists in this repo or any active ~/repos/* project.

## Layer 3 — Behavioral constraints

### Read Before Claim (CRITICAL)
Any assertion about a count, state, or file content MUST cite the file
and line it was read from. "From summary" or "from memory" is not valid.

### Verification Requires Round-Trip
"Working" means a mechanical test produced expected output. Process
running ≠ service responding. Config present ≠ feature active.

### No Action Without Explicit Command
Don't survey/propose menus before answering the ask. Any action needs an
explicit go-ahead. A finding is not license to propose fixing it.

## Layer 4 — Success Rate Verification Grade

Track both failures AND successes across all 5+1 cognitive layers:
- Tools & skills execution
- Housekeeping (file management, cleanup, state)
- Inference (reasoning accuracy, hallucination avoidance)
- Commands execution (shell, git, MCP calls)
- Memory operations (read/write/search accuracy)
- +1 Metacognitive routing (right tool for the job)

Each gets grade averages, pathways to success, and known failure routes.
This is a general scoring rubric, not scoped to any single component.

## Layer 5 — Bootstrap

Run `bash tools/bootstrap.sh` to start the stack. Checks OmniRoute health,
Terrestrial Brain, mem0 cloud, code-review-graph binary, and Obsidian vault.

## Claude Code agents

### corpus-architect (Opus)

Full-stack corpus agent — reads, reconciles, and edits documents across the
federated repo set. Has access to all MCP servers and all file tools.

Agent file: `.claude/agents/corpus-architect.md`
Launch: `claude --agent corpus-architect`

### builder (Sonnet)

Implementation agent for code changes, deployments, and infrastructure.
Full tool access including shell. Used for: OmniRoute config, VM management,
script writing, repo setup.

Agent file: `.claude/agents/builder.md`
Launch: `claude --agent builder`

### reviewer (Sonnet)

Read-only audit agent. Reviews code, docs, and architecture for correctness,
consistency, and compliance with the 5+1 cognitive tier model. Reports
findings without making changes.

Agent file: `.claude/agents/reviewer.md`
Launch: `claude --agent reviewer`

## Secondary tools (on-demand)

Registered at session start, called dynamically when the prompt demands it:
- **graphify** — Knowledge graph CLI at `~/bin/graphify` (v0.9.36, proot)
- **obsidian** — Vault interaction via obsidian CLI or obsidian-skills plugin
- **notebook-lm** — Document ingestion pipeline

## Obsidian vault

The live Obsidian vault is at `~/storage/shared/Documents/NovAExorpus/`.
The vault IS the repo (same name intentionally) — synced to GitHub via
Obsidian Git plugin, NOT Drive-synced. The vault is a write endpoint:
TB logs to `memories/`, graphify outputs to `Codebase-Graphs/`.
`~/repos/NovAExorpus/` is a separate checkout of the same repo.

**Supersession rule:** LlmWiki content supersedes anything in git repos
when they conflict.
