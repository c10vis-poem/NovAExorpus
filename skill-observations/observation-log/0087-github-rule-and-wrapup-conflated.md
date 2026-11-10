---
id: 87
title: "GitHub rule and the wrap-up protocol were merged into one hook; the session log had too many copies"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["frankenstein/plugins/aesops-enforcements/scripts/ship-session.sh", "~/.claude/WRAP-UP.md"]
siblings_checked: "none: target is a hook script, not a skill family"
area: "session end: shipping vs wrap-up"
date: 2026-11-10
session_context: "Operator correction e21315 during the rules review. The agent wired session-log copies into the SessionEnd shipping hook."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The agent put the session-notes copy into the GitHub shipping hook, which made the
wrap-up protocol and the GitHub rule one thing. The operator's GitHub rule: sync every touched
fork with its main branch first; hold every push and merge until the end; at the end run the
secret scan, push, open the PR, and set auto-merge and auto-delete while CI runs, with no
watching and no coming back to delete. The built hook polls CI and deletes branches itself.
The session log also had several copies (device archive, vault ledger, per-repo recaps, and
the new session-logs folder) where the operator wants two parts only: the scratchpad
narrative and the task log (skills used, tools pulled).

**Suggested improvement:** Keep shipping in its own GitHub rule. Wrap-up owns the scratchpad
and the task log, as the two parts of one session log. Remove the other copies.

**Principle:** Before adding a step to a hook, check that the hook's rule actually owns that
step. Two protocols that both run at session end are still separate protocols.
