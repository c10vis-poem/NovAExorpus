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

**Recurrence 2026-09-30:** Same failure again. The session opened with `/android-termux-operator` and `/ask-matt`, and task-observer was not invoked until the operator called it out. The CLAUDE.md trigger line was in context the whole time. This is the third instance (0002, 0006, and now this one), so the fix has to be a structural barrier, not more wording: a SessionStart hook that injects the protocol output itself.

**Further instance (2026-10-02):** task-observer was invoked and the scan ran, but with a hand-rolled scan rather than the snippet. Step 6 (PENDING/staging reconciliation) was skipped, and the session's own violations were not logged until the operator pointed them out. The ENFORCEMENTS `observer` row is satisfied by loading the skill alone, so nothing structural checks the protocol steps.
