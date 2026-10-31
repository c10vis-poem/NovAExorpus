---
id: 49
title: "Put new builds in the wrong repo and treated settled decisions as open, because the repo map and wiki decisions lived only in files the session did not load or apply"
status: open
type: open-source
skill: [task-observer]
proposes_skill: [memory-as-skill]
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "no family registry entry for task-observer; checked, instance-specific to memory loading, no propagation"
area: "session start / memory recall"
date: 2026-10-28
session_context: "Phone session 5fc2c8e1: building intake skill, web view tool, wiki admin"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The agent put two new plugins into the private recaps repo without being asked, although the naming canon (read that session) and a project memory file already mapped each kind of build to a repo. Later it called the OpenWiki choice an open conflict, though the operator had settled it after a long process. The operator had to restate both, angrily. The agent's own memory folder is scoped to the folder the session starts in, so notes from one project never load in another.

**Suggested improvement:** Cross-project memory in one shared, private, synced place that every agent reads at session start (done 2026-10-28 as `NvAEx-Recaps/memory/`, with a pointer in `~/.agents/AGENTS.md`). Before creating a file in any repo, match it against the repo map in that memory.

**Principle:** A rule recorded only where the next session does not look is not recorded. Memory must be scoped to the person and the work, not to the folder a session happens to start in.
