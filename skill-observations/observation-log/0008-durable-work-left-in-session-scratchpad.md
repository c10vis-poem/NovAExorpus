---
id: 8
title: "Multi-hour research output written only to the session scratchpad and lost at session end"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "no family registry found; checked — instance-specific to scratchpad lifecycle, no propagation"
area: "session-end handoff / durable persistence of deliverables"
date: 2026-09-27
session_context: "Next session could not find a prior multi-hour repo deep-dive; transcript 18a82005 (2026-09-25..26) shows reading notes and plugin drafts written to $TMPDIR scratchpad, which was deleted; memory notes never mention the main subject"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** A long session produced its core deliverables (a reading-notes file over a large repo, three plugin drafts, an orchestration contract) inside the per-session scratchpad directory. The scratchpad was removed after the session. Memory notes were updated during the same session but only for side topics (VM, cost guardrails); the main subject appears 0 times in memory versus thousands of times in the transcript. The next session answered "no records" after reading a memory file whose middle was truncated in tool output.

**Suggested improvement:** (1) Structural: a Stop/SessionEnd hook that lists files in the session scratchpad and warns/blocks if any non-throwaway file (.md, source) was not copied to a durable path. (2) Rule: anything the user would want next session never lives only in scratchpad. (3) Before claiming "no records", grep the raw transcripts (~/.claude/projects/*/*.jsonl), and never conclude from truncated tool output.

**Principle:** Ephemeral working directories are for intermediates only; the moment an artefact becomes something a future session needs, it moves to durable storage — and absence claims must be checked against the rawest surviving record, not a summary.
