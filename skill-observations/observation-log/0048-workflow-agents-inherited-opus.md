---
id: 48
title: "Workflow agents launched without a model, so 40+ mechanical read/check agents inherited Opus despite the size-the-model standing order"
status: open
type: open-source
skill: [workflow-authoring]
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "no family registry; checked, the same gap applies to Agent-tool spawns, which the standing order already covers; Workflow agent() calls are the uncovered path"
area: "model sizing for workflow agents"
date: 2026-10-28
session_context: "Session 37dc78ed, Drive ingest wave 1 (21 batches of reader+checker)"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The CLAUDE.md standing order says to size the model per task (haiku for lookups, sonnet for normal reading and audits, opus/fable for hard reasoning). The agent wrote a Workflow script with no `model` option on the reader and checker agents, so all of them inherited the session model (Opus 5.5). The workflow-authoring reference itself says "default to omitting it", which directly conflicts with the operator's standing order. The operator caught it: "Don't tell me you use 10 opus 5.5 agents for this did you". The run was stopped after 2 of 21 batches and relaunched with sonnet for read/check.

**Suggested improvement:** Add a barrier, not more text: a PreToolUse hook on Workflow that refuses a script containing agent() calls without an explicit `model:` option (or a phase-level model), unless the operator typed an override. Also state in CLAUDE.md that the operator's sizing rule overrides the workflow-authoring "omit model" default.

**Principle:** When a tool's own guidance sets a default ("inherit the session model") that conflicts with a standing operator rule, the operator rule wins, and the conflict should be checked mechanically at the call, because the tool's guidance is loaded fresh right before the call and outweighs a rule read hours earlier.
