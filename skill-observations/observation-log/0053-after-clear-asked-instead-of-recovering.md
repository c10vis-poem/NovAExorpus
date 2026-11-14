---
id: 53
title: "After /clear in a resumed session, the agent asked what to work on instead of recovering the session from its records"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "none: target is a global instruction file, not a skill"
area: "session start after /clear or resume"
date: 2026-10-31
session_context: "Operator resumed last night's session after a usage-limit reset, then ran /clear. The first reply said 'What do you want to work on?'"
parked_until:
resolved:
resolution:
reference: "session 07d9a60a (resumed from 5fc2c8e1)"
commands_verified: "run: jq over the previous session's transcript, progress-P*.md files, memory/active/wiki-admin.md recovered the full state in four reads"
---

**Issue:** After a /clear, the agent treated the session as new and asked the operator what to work on. The operator expected it to know: the previous transcript, the subagent progress files and the shared memory file held the whole state, a few reads away.

**Suggested improvement:** At session start (and after /clear or a resume), read the newest transcript tail, today's and yesterday's `~/.claude/session-work/` progress files, and the active memory file before replying. Ask only if those are empty.

**Principle:** The operator should never have to re-explain work that is on disk; recover first, ask second.
