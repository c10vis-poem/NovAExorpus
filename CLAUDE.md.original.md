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

Defined in `.mcp.json` at repo root: `mem0` (memory) and `terrestrial-brain`
(corpus knowledge base). Both take their endpoint/credentials from env vars
— see `.mcp.json` for the exact variable names. Set them locally; never
commit values.
