---
id: 36
title: "git-gate drops an operator's 'push now' when any later message arrives before the push runs"
status: actioned
type: internal
skill: []
proposes_skill: []
target_file: ["~/repos/Aesop-Xi/hooks/git-gate.sh", "~/.claude/hooks/git-gate.sh"]
siblings_checked: "none: target is a hook script, not a skill family"
area: "push authorization scope"
date: 2026-10-21
session_context: "Shipping Aesop-Xi #54 (cloud hook stand-down) and #53. Friction events e14466, e8822."
parked_until:
resolved: 2026-10-23
resolution: "Aesop-Xi #61 merged: push now lasts the session, 'hold push' revokes. Live ~/.claude/hooks/git-gate.sh and enforce-prompt.sh equal origin/main (cmp, 2026-10-23); gitgate.test.sh 17/17 after the stale-expectation fix on branch test/gitgate-session-pushnow."
reference:
commands_verified: "run: git push after a mid-turn operator message with no 'push now' -> BLOCKED (git-gate)"
---

**Issue:** git-gate only lets a push through if the latest operator message contains "push now". This happened twice in one session:
- e14466: the push spanned two turns.
- e8822: the operator sent a message mid-turn, while conflicts were being resolved.

Both times the operator had already said "push now" for that exact work. Each block made them repeat it ("How many times do I have to say push now", "3 days later"), and that is where the anger in this session came from.

**Suggested improvement:** git-gate should treat a "push now" as active until the push it named has run, or until the operator says to stop. It should not reset on the next message. One way: write a state file when the phrase is seen and clear it at wrap-up.

**Principle:** An approval gate should last for the task that was approved, not for one message. If routine conversation resets it, the operator ends up repeating themselves for nothing, and the gate starts to look like an obstacle instead of a safety check.
