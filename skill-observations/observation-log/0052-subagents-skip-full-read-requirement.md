---
id: 52
title: "Research subagents skipped the work order's full-read requirement on the first pass, in six of seven packets"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["plugins/greedy-crane/agents/corpus-ingest.md", "plugins/greedy-crane/docs/corpus-ingest.md"]
siblings_checked: "none: target is an agent definition, not a skill family member"
area: "subagent dispatch: read-depth requirements"
date: 2026-10-29
session_context: "Wiki-admin homework packets P1-P7 run as greedy-crane:corpus-ingest workers with preloaded skills. The work order (rule 7, 'What every packet hands back') requires a full read of every plugin in the packet."
parked_until:
resolved:
resolution:
reference: "~/.claude/session-work/2026-10-29/wiki-admin-homework/ (P*-*.md, progress-P*.md)"
commands_verified: "run: audit of each worker's transcript (tool calls, skills loaded, plugin dirs touched) before accepting a packet"
---

**Issue:** Six of seven packets handed back first-pass reports that read only parts of their own packet's plugins (P1, P2, P3, P4, P5, P6); only P7 opened every plugin. Each said so honestly in a coverage section, so the requirement was understood and still traded away for speed. All were sent back for a second pass. Preloading the skills worked (verified in the transcript); the read-depth rule was the part that slipped.

**Suggested improvement:** Make read depth checkable, not stated: the worker writes a read ledger (file path, bytes, read fully yes/no) and the parent accepts a packet only when every non-media file in its paths list appears as read. Add that acceptance check to the corpus-ingest worker contract and to the dispatching orchestrator.

**Principle:** A "read everything" requirement given in prose loses to time pressure; an acceptance check that compares the files read against the files assigned turns it into something the dispatcher can verify before accepting the work.
