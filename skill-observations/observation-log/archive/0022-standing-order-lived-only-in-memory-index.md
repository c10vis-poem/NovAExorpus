---
id: 22
title: "Operator standing order (spawn subagents unasked) lived only in a memory file whose one-line index pointer was all that loaded"
status: actioned
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md", "~/repos/aesop-xi/CLAUDE.md"]
siblings_checked: "none — target is an instructions file, not a skill"
area: "where durable operator rules are stored"
date: 2026-10-04
session_context: "Operator asked whether the subagent rule had been put in a hook; it existed only as a memory note"
parked_until:
resolved: 2026-10-04
resolution: "Rule written in full into global and aesop-xi CLAUDE.md (always loaded), plus live progress-file requirement for subagents"
reference:
---

**Issue:** A standing behavioural order from the operator was saved as a memory file. Only its one-line index entry loads at session start, so the rule was easy to miss and the operator had to restate it.

**Suggested improvement:** Standing orders that change default behaviour go into the always-loaded instructions file (and the repo-level copy where the harness may start), not only into on-demand memory.

**Principle:** A rule's storage location decides whether it is in context when needed; on-demand memory suits facts, not standing behavioural orders.
