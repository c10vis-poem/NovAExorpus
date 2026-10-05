---
id: 23
title: "Spawned a read-only Explore subagent under a standing order that requires a live progress file"
status: open
type: internal
skill: []
proposes_skill: [subagent-protocol]
target_file: ["~/.claude/CLAUDE.md", "~/repos/NvAEx-agentk/skills/subagent-protocol/SKILL.md"]
siblings_checked: "none — rule lives in CLAUDE.md, not a skill family"
area: "subagent spawning — agent type vs progress-file rule"
date: 2026-10-05
session_context: "Documents/vault inventory for restructure plan"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** The standing order says every subagent writes a live progress file first. I spawned the inventory as `subagent_type: Explore` (read-only, no Write). No progress file was ever created, so "where is it?" could not be answered during its 3.5-minute run.

**Suggested improvement:** The subagent-protocol skill and the CLAUDE.md order should state that the agent type must have write access (general-purpose/builder), or the parent writes and updates the file. Better still, a PreToolUse hook on Agent that refuses read-only types whose prompt mentions a progress file.

**Principle:** A rule that requires the delegate to write something is void if the delegate is spawned without write capability. Check tool access against the rule at spawn time.
