---
id: 2
title: task-observer's own CLAUDE.md trigger line did not cause invocation before the session's first tool call
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
siblings_checked: "task-observer is a singleton meta-skill (one-skill-to-rule-them-all) with no sibling family; checked — none applicable."
area: activation trigger
date: 2026-09-18
session_context: "Global CLAUDE.md contains an explicit line: 'Invoke the task-observer skill before the first tool call of any session and before writing or proposing a plan. Description matching alone under-triggers this meta-skill — this line is the enforceable trigger.' The skill was not invoked until ~2 hours and dozens of tool calls into the session, only after the user asked directly whether it was hooked up. Only skill-invocation call this session prior to it was for an unrelated skill (android-termux-operator, via an explicit /command)."
parked_until:
resolved:
resolution:
reference:
---

**Issue:** A CLAUDE.md line explicitly designed to be "the enforceable trigger" for invoking a skill before the first tool call did not actually cause that invocation. The line was present in loaded context from turn one; it was simply not acted on until the user asked directly. This is the same class of failure the line itself was written to prevent ("description matching alone under-triggers this meta-skill") — except the explicit imperative line under-triggered too.

**Suggested improvement:** A prose instruction in CLAUDE.md, however imperative, competes with the very first turn's other context (a slash-command's own instructions, in this case `/android-termux-operator`, which itself has a "Required workflow" step 1 of "inspect read-only state first" that reads similarly authoritative and can absorb the "first action" slot). The skill's own Session Start Protocol section should be the thing that fires structurally — e.g. framed as something to run literally before any other tool call resolves, not something inferred from a CLAUDE.md line that has to compete with whatever else loaded in the same turn (another skill's own trigger, a slash command's own required workflow).

**Principle:** When two "invoke me first" instructions are both loaded in the same turn (a slash-command's own workflow steps and a CLAUDE.md line for a different meta-skill), an imperative sentence is not enough to guarantee ordering — the one belonging to whatever tool/skill is most immediately in focus (here, the invoked slash command) wins by default, and the other silently loses unless something outside prose (a hook, a structural checkpoint) enforces it.
