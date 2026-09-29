# CLAUDE.md — NovAExorpus (Claude Code only)

Repository: `NovAExorpus` — NovÆxorpus Federated Master Corpus Root.

Tool-agnostic rules (apply to every engine, not just Claude Code) live in
`AGENTS.md` — read that first, every session.

## Meta-skill activation

Invoke the `task-observer` skill (`.claude/skills/task-observer/`) before
the first tool call of any session and before writing or proposing a plan.
Description matching alone under-triggers it — this line is the enforceable
trigger.

## MCP servers

Defined in `.mcp.json` at repo root: `omniroute` (gateway),  `mem0`
(episodic memory), and `terrestrial-brain` (structural memory). All take
endpoint/credentials from env vars — see `.mcp.json` for the exact
variable names. Set them locally; never commit values.

## Mandatory pipeline

The 6-layer pipeline, multi-write protocol, secondary tools, and
enforcement rules are in `AGENTS.md` §Mandatory runtime pipeline — that's
the canonical, engine-agnostic version. This file does not duplicate them.

**Launch**: `bash tools/launch.sh` (aliased as `cc`) — sources secrets,
runs pre-flight health checks, starts Claude Code with the `router-guard`
output style.
