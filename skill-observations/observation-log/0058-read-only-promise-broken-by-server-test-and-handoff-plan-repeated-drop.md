---
id: 58
title: "Ran a test that started servers without an okay, and nearly executed a handoff step that repeated the defect it was meant to fix"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "none: target is the shared instructions file; principle 9 (a handoff note is a pointer, not authority) covers the second half"
area: "approval scope; following handoff steps"
date: 2026-11-05
session_context: "Resuming a rebuild from a handoff; the operator had asked only where the packages were."
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: checked afterwards that the test left no stray data folders"
---

**Issue:** Asked where some packages were, the agent also started three servers to test them, while the operator's message telling it not to act without an okay was arriving. Separately, the handoff said to unwire every hook outside a short list; the agent began on that step, and only reading the code showed it would break four kept rules.

**Suggested improvement:** A question gets reads only, and any start of a process counts as an action to disclose or ask about. Before running a handoff step that removes something, check it against the code it touches.

**Principle:** A handoff records what the last session believed. A removal step in one needs the same check as a removal proposed fresh.
