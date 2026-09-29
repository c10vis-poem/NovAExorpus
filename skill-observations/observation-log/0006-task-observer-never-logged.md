---
id: 6
title: task-observer loaded via command but session-start protocol and logging never ran
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
siblings_checked: "task-observer family: task-observer, novae-xorpus:task-observer — shared, both affected"
area: Session Start Protocol / How to Log
date: 2026-09-23
session_context: long Termux/Obsidian/OpenWiki/dsh session
---

**Issue:** Skill content was injected at session start, but the agent never ran the Session Start Protocol, never logged an observation, and made no mem0 calls until the operator called it out hours in. Also found two forked observation workspaces (global ~/.claude/skill-observations and a project-keyed one) — the silent fork the skill warns about. Relates to existing obs 0002 (CLAUDE.md trigger not self-enforcing) in the project-keyed log.

**Suggested improvement:** Enforce via a harness hook (SessionStart/PreToolUse gate) rather than instructions; consolidate the two workspaces (quarantine, no delete) and pin the path in CLAUDE.md.

**Principle:** Instruction-only activation for a meta-skill decays under task load; it needs a mechanical trigger.
