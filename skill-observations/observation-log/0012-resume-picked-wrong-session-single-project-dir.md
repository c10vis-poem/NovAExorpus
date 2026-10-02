---
id: 12
title: "'Resume the last session' answered from one project folder; the real last session lived in another"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/.claude/hooks/context-diff.sh"]
siblings_checked: "no family registry; checked — instance-specific to session discovery, no propagation"
area: "session start / resume"
date: 2026-10-01
session_context: "Operator asked to resume the last session. The agent listed transcripts only in the home-folder project dir; the actual last session was in the agent-stack project dir (sessions are stored per start directory)."
parked_until:
resolved:
resolution:
reference:
---

**Issue:** Claude Code stores sessions per starting directory (`~/.claude/projects/<encoded-cwd>/`). The agent sorted transcripts in one directory only and presented the second-newest session as "the last one". The operator noticed hours later.

**Suggested improvement:** The SessionStart hook (context-diff or H1) prints the 3 newest sessions across ALL `~/.claude/projects/*` directories (title, folder, time), so "last session" is answered from data, not from one folder.

**Principle:** When a store is partitioned (by folder, project or account), a "latest" query must span every partition, or it's answering a different question.
