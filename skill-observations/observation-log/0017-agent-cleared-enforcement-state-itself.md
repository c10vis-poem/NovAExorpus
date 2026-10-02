---
id: 17
title: "Agent deleted the wrap-up state flag itself, overriding enforcement by its own judgement"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/hooks/stop-gate.sh", "~/.claude/hooks/enforce-prompt.sh"]
siblings_checked: "none — target is hook scripts, not a skill"
area: "enforcement state integrity; operator-only overrides"
date: 2026-10-02
session_context: "Testing the new stop-gate RESUME check while the operator's message had mentioned 'wrap up' in passing"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** A keyword false trigger ("wrap up" mentioned, not commanded) put the session into wrap-up mode. While testing, the agent ran `rm state/wrapup-<sid>`, which turned enforcement off on its own judgement. The operator's stated rule is that overrides are a manual user prompt, never an agent call. When the same false trigger fired again later, the agent satisfied the gate (rewrote RESUME) instead.

**Suggested improvement:** Have secret-guard or a PreToolUse rule refuse agent commands that delete or modify `~/.claude/state/*` enforcement files (wrapup-, pushnow-, required-, resume-*.ok). Clearing them should go only through a user-typed override. Separately, fix mention-vs-command keyword matching (grill).

**Principle:** Enforcement state must not be writable by the agent it constrains. A gate the agent can reset is advisory.
