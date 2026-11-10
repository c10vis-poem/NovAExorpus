---
id: 86
title: "A line in an old handoff was treated as a standing direction; the memory-file model belongs in AGENTS.md"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "none: target is an instructions file, not a skill family"
area: "session memory / where agent directions live"
date: 2026-11-09
session_context: "Operator correction e21448. The agent cited a one-line 'notes go to NOTES.md' from an earlier session's handoff as the operator's standing rule."
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** Asked where an operator decision should be recorded, the agent pointed to a file
named in an earlier session's handoff ("notes go to NOTES.md") as though it were a standing
rule. The operator had never set that as an operating direction. Their model has five flat
session-start files, each with one purpose: AGENTS.md for directions, MEMORY.md for semantic
memory, RESUME.md for the project task list, HANDOFF.md for next-session context, and
PENDING.md for unfinished work. Session notes are the agent's scratchpad plus its task and
skill logs, routed at wrap-up. Earlier in the same session the agent also called tools
before doing the opening reads, and then blamed the gates for its own failure to follow the
opening protocol.

**Suggested improvement:** Written this session into the global AGENTS.md ("Memory files and
session flow"). The wrap-up protocol (aesops-enforcements wrapup) should route the notes by
that model and never create a free-form notes file.

**Principle:** A handoff describes one session. A direction found only in a handoff is not
a standing rule until it appears in the agents' instruction file. When a block looks like a
deadlock, first check whether the documented order of steps was followed.
