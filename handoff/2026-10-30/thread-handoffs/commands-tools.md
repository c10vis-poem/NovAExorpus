# Handoff: slash commands and tools list (2026-10-30)

Thread: "List all slash commands and tool prompts". Status: done. Nothing is left open.

## What was delivered
- `inventory/slash-commands-and-tools-2026-10-30.md` (about 26 KB). The full list for this account, grouped by source: built-in Claude Code commands (from https://code.claude.com/docs/en/commands), 8 plugin commands, skills callable with /name (plugin, the 20 uploaded account skills, built-in), core tools, and every connector tool with a one-line description.
- `inventory/other-account-prompt-commands-tools-2026-10-30.md`. A paste-ready prompt for the other account that carries the full list. It sets these rules: read-only, no guessing, no subagents, stop on failure, call the owner "The Builder" (or "the owner" / "the architect"). It asks that account to build the same list and report what only one account has and what differs.

## Connectors that failed to start in this cloud session
- adb-mcp: the command was not found in the container.
- context7: the network proxy refused the tunnel.
- github plugin MCP server: the network proxy refused it (403). The separate GitHub connector still works.
- jevmem: the command was not found in the container.

## How to pick this up
1. Open the other account and paste the prompt file's text below its `---` line into a project there.
2. Compare that account's output with `slash-commands-and-tools-2026-10-30.md`.
3. Teleport: `/teleport` (also `/tp`) pulls a cloud session into a local terminal. `/resume` continues a past one. `/export` saves a conversation as text.

Nothing was installed, enabled or changed. Only the files above were written.
