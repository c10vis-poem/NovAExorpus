---
id: 10
title: "Session-start RESUME.md read skipped; resume handled from transcript tail instead"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "no family registry; checked — instance-specific to the session-start handoff read, no propagation"
area: "session start / handoff ingestion"
date: 2026-10-01
session_context: "Operator asked to resume the previous session; agent summarised the prior transcript's last messages but did not Read the vault RESUME.md that CLAUDE.md requires at session start, until ~20 turns later."
parked_until:
resolved:
resolution:
reference:
---

**Issue:** CLAUDE.md says "If the active project ... contains a RESUME.md, read it before proceeding to any task. Not ls — Read." The agent ran the task-observer start protocol, then answered "resume the last session" from the tail of the previous transcript, and did not Read RESUME.md. RESUME.md held facts that would have changed answers (GitSync target branch history, the operator to-do, the open items order). Protection in play: written down and loaded into context only — no checkpoint.

**Suggested improvement:** Structural, not wording: a SessionStart hook that injects the vault RESUME.md "NEXT SESSION" section (or at least its path + mtime) into context, so the read happens without depending on the agent noticing the rule.

**Principle:** A "read X first" rule that competes with the user's first request loses; inject the handoff into context mechanically at session start.
