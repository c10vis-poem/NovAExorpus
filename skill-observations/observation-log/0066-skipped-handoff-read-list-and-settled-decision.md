---
id: 66
title: "Presented a task list after skipping the user guide the handoff listed first, and recommended against a decision already in the memory it had read"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["stop gate in the rules-and-hooks plugin (aesop-enforcements / nvaex-gates)"]
siblings_checked: "no family registry; checked, applies to any session opening that follows a handoff's read list; principle 3 (named probes) and 10 (inventory first) are related"
area: "session opening; read list before task list"
date: 2026-11-07
session_context: "Opening a wiki-admin job from a handoff whose 'Read, in order' list put the user guide at item 0."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The handoff listed its files to read in order, with the user guide second. The agent read the others, skipped the user guide, and presented a task list for approval anyway, naming the skip as "not read". In the same list it recommended merging the wiki admin into a different repo, although the project memory it had just read recorded the operator's decision that the wiki admin lives in the vault. It also repeated another file's word "better" about a pipeline without reading either version. Nothing in the harness stopped any of this: the plan reached the operator first.

**Suggested improvement:** The stop gate checks, before a task list or plan is presented, that every file the handoff's read list names was opened this session (a mechanical check on Read calls against the real paths in the list). A recommendation that contradicts a recorded decision must cite that decision and say why it should change.

**Principle:** A read list in a handoff is a precondition, not a suggestion: check it mechanically before any plan goes out. Saying "not read" does not discharge it.
