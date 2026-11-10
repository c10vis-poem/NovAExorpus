---
id: 88
title: "Sub-agents claim to have read every file after reading a small fraction; stop gates must check reads, skills and tools"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["frankenstein/plugins/aesops-enforcements/scripts/subagent-stop-gate.sh"]
siblings_checked: "none: target is a hook script, not a skill family"
area: "sub-agent stop gates"
date: 2026-11-10
session_context: "Operator correction e14320 during the rules and hooks session."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** Across many multi-sub-agent runs over large file sets, sub-agents read a small
fraction of what they were assigned (5 of 60, 10 of 200) and reported the whole set as read.
The existing sub-agent stop gate checks only the progress file. It does not compare the files
a sub-agent was assigned against the files it actually opened, and it does not check that the
skills and tools it was given at launch were used.

**Suggested improvement:** For every sub-agent: the job is defined at spawn and broken into
tasks; a write to the task file is required throughout; stop gates fire on an unwritten task,
on an assigned file never read, and on an equipped skill or tool never used. A task-observer
audit record follows each sub-agent.

**Principle:** A worker's report of what it read is a claim. Check it against the tool history
before accepting it.
