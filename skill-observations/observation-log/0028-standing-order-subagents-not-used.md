---
id: 28
title: "Standing order to spawn subagents ignored during a multi-repo audit"
status: open
type: internal
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none: target is an instructions file, not a skill family"
area: "Subagents standing order"
date: 2026-10-08
session_context: "Wrap-up straggler audit across 16 fork repos plus a uniqueness check of a repo slated for deletion"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The user-level instructions say independent parts get subagents unasked. The agent ran a 16-repo branch audit, PR-state checks and a whole-device hash comparison inline across many sequential turns. The operator had to ask "You're using sub agents for all this aren't you" before one was spawned.

**Suggested improvement:** Text alone is not holding. Add a structural trip-wire: a PreToolUse hook that counts inline Bash calls per turn on audit-shaped work (e.g. more than 6 calls touching more than 3 repos) and injects a reminder to delegate.

**Principle:** A standing order with no trigger point gets dropped once the work feels like "just one more command". Delegation rules need a measurable trip-wire, not just text.
