---
id: 20
title: "Agent reported a small fixable bug as 'fix later' instead of fixing it in the session"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "feedback_dont_wait_on_routine_work"
area: "session discipline; deferral"
date: 2026-10-02
session_context: "npu-serve start script hung when its output was piped; agent logged it as 'Fix later' in the summary"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** The agent found a one-line bug (backgrounded `cd && … &` subshell holding stdout; 60 s load wait too short) and wrote it up as "fix later". Operator: "stop putting shit off to the next session". It was fixed and verified in two minutes once asked.

**Suggested improvement:** A defect found in code the session owns gets fixed in the same session unless it needs the operator's decision or is out of scope; "later" requires a named reason.

**Principle:** A deferral without a blocking reason is just unfinished work moved onto the next session.
