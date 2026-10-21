---
id: 33
title: "Keyword ENFORCEMENTS fired on a subagent hand-back and blocked work until five unrelated reads/skills were done"
status: open
type: internal
skill: []
proposes_skill: []
target_file: ["~/repos/Aesop-Xi/hooks/enforce-prompt.sh"]
siblings_checked: "none: target is a hook script, not a skill family; sibling hook observe-event.sh already gets the same skip on branch fix/observe-skip-agent-messages"
area: "UserPromptSubmit keyword classification"
date: 2026-10-21
session_context: "Drive dedup subagent returned its report; its text named naming/hooks/npu/vault/voice topics"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** A subagent's final report arrives as a UserPromptSubmit prompt. enforce-prompt.sh classified its words (naming, hooks, NPU, vault, voice) as if the operator had asked about them, and enforce-gate blocked the next Bash call until the naming canon, hooks README and NPU file were read and two skills loaded. None was relevant. The same shape already hit observe-event.sh (false correction events on hand-backs).

**Suggested improvement:** In enforce-prompt.sh, skip classification when the prompt contains `<agent-message` / `<task-notification>` or starts with "Another Claude session sent a message", the same test added to observe-event.sh. Put the test in one shared helper both hooks source.

**Principle:** Hooks that act on "what the user asked" must first establish that the prompt came from the user; machine-delivered prompts need an explicit, shared skip.
