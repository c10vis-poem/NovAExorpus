---
id: 62
title: "Told the operator 'ready' and asked them design questions after reading only the memory index and summary write-ups"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/repos/Aesop-Xi/hooks/stop-gate.sh"]
siblings_checked: "no family registry; checked, applies to any session start; principle 3 and 10 are related"
area: "session start; read before asking"
date: 2026-11-06
session_context: "Resuming the Frankenstein review. The agent read MEMORY.md (index), handoff and write-ups, then listed four questions for the operator."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The agent reported ready and asked about JEV placement, capability card fields, Prime Agent and RLM. The memory files and source documents that answer them had not been read: memory holds RLM's meaning and the reverse-engineering decision, and the operator's folder holds how JEV is used. Operator: "Next time I actually fucking read everything before you start asking me stupid questions." Same failure shape as memory notes feedback_find_context_before_asking and feedback_read_fully_not_sampled, so this is a repeat: the fix must be a barrier.

**Suggested improvement:** Have the stop gate refuse a turn that puts a design question to the operator when the session has not opened the memory files and the sources the handoff's write-ups cite. An index or a summary does not count as reading them.

**Principle:** A summary of a source does not license a question about it; read the source, decide what it settles, and ask only what remains.
