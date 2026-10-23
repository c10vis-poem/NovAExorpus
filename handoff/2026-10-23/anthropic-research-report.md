# Anthropic research (claude-code-guide subagent, 2026-10-23), saved by parent

## Per-task auditing
- No built-in "auditor on every task". Pieces: Stop/SubagentStop hooks; `type: "prompt"` hooks (one LLM call, `{"ok","reason"}`, needs `continueOnBlock: true` on Stop); `type: "agent"` hooks (EXPERIMENTAL, subagent with Read/Grep/Glob, up to 50 turns, ok:false continues the turn); subagent definitions `.claude/agents/<name>.md` (model, tools, hooks); `/code-review` (reports, doesn't gate); workflows (JS `agent()/pipeline()/parallel()`, `.claude/workflows/`, 16 concurrent agents default); `/effort ultracode` plans a workflow per substantive task.
- Stop cap: 8 consecutive stop-hook continuations, then the turn ends (`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`).
- Sketch (settings.json hooks.Stop):
```json
{"hooks":{"Stop":[{"hooks":[{"type":"agent","model":"claude-opus-5-5","timeout":180,
 "prompt":"You are an auditor. Hook input: $ARGUMENTS. If stop_hook_active is true, return {\"ok\": true}. Otherwise read transcript_path for the user's request and this turn's changes. Return {\"ok\": true} if met, else {\"ok\": false, \"reason\": \"<specific gap>\"}."}]}]}}
```
- Runs on every turn end (cost); scope "tasks only" inside the prompt.
- Docs: code.claude.com/docs/en/hooks.md, sub-agents.md, workflows.md, code-review-local.md

## Advisor
- Exists (experimental): `/advisor <model>` saves `advisorModel` in user settings; `/advisor off`; env `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1`. Advisor must rank >= main model (Opus 5.5 main: Fable or Opus 5+ advisor). Anthropic API only; blocked if feature flags are blocked (e.g. DISABLE_TELEMETRY), main-model switch, or missing Fable consent.
- ~/.claude/settings.json has no `advisorModel` key now. Docs: code.claude.com/docs/en/advisor.md

## Orchestrator model
- Docs: "start with Opus 5.5 for most workloads; Fable 5.1 for demanding reasoning and long-horizon agentic work". Pricing per MTok: Fable $10/$50, Opus 5.5 $4/$20. No documented topology.
- Options: Opus orchestrates + Fable subagents/advisor (matches docs, cheapest); Fable throughout (~2.5x).

## JEV / REA
- Not defined in local notes (only BOARD-INTAKE line 13 "broken down by REA/JEV and Fable"); repo hits: NvAEx-rea fork, dsh-jev repo. Not found in visible parts of claude-plugins-official / -community catalogs (both truncated) or claude.com/marketplace search.

## Plugin manifest
- `.claude-plugin/plugin.json`, `name` required; keys skills, commands, agents, outputStyles, workflows, hooks, mcpServers, lspServers, channels, userConfig, dependencies; plugin agents ignore hooks/mcpServers/permissionMode frontmatter; root CLAUDE.md not loaded; `bin/` on PATH; `claude plugin validate --strict`. Docs: code.claude.com/docs/en/plugins/manifest-reference.md
