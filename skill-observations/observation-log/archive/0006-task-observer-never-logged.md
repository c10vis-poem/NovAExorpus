---
id: 6
title: task-observer loaded via command but session-start protocol and logging never ran
status: actioned
type: open-source
skill: [task-observer]
proposes_skill: []
siblings_checked: "task-observer family: task-observer, novae-xorpus:task-observer — shared, both affected"
area: Session Start Protocol / How to Log
date: 2026-09-23
session_context: "long Termux/Obsidian/OpenWiki/dsh session; 2026-10-18/20 phone housekeeping session (post-compaction)"
parked_until:
resolved: 2026-10-22
resolution: "Park condition met and the later-instance barriers exist. aesop-task-observer PR #1 merged 2026-10-18 as 09a4101 (scripts/session-start-hook.sh injects the scan); ~/.claude/settings.json line 182 registers it for startup|resume|clear|fork. Compaction: Aesop-Xi PR #56 hooks/observe-event.sh (SessionStart source=compact re-arms and tells the agent to re-run session-start-scan.sh); hooks/stop-gate.sh lines 58-67 require the skill loaded plus a fresh scan after RESUME and after compaction, and every friction event logged or dismissed."
---

**Issue:** Skill content was injected at session start, but the agent never ran the Session Start Protocol, never logged an observation, and made no mem0 calls until the operator called it out hours in. Also found two forked observation workspaces (global ~/.claude/skill-observations and a project-keyed one) — the silent fork the skill warns about. Relates to existing obs 0002 (CLAUDE.md trigger not self-enforcing) in the project-keyed log.

**Suggested improvement:** Enforce via a harness hook (SessionStart/PreToolUse gate) rather than instructions; consolidate the two workspaces (quarantine, no delete) and pin the path in CLAUDE.md.

**Principle:** Instruction-only activation for a meta-skill decays under task load; it needs a mechanical trigger.

**Recurrence 2026-09-30:** Same failure again. The session opened with `/android-termux-operator` and `/ask-matt`, and task-observer was not invoked until the operator called it out. The CLAUDE.md trigger line was in context the whole time. This is the third instance (0002, 0006, and now this one), so the fix has to be a structural barrier, not more wording: a SessionStart hook that injects the protocol output itself.

**Further instance (2026-10-02):** task-observer was invoked and the scan ran, but with a hand-rolled scan rather than the snippet. Step 6 (PENDING/staging reconciliation) was skipped, and the session's own violations were not logged until the operator pointed them out. The ENFORCEMENTS `observer` row is satisfied by loading the skill alone, so nothing structural checks the protocol steps.

**Further instance (2026-10-18/20, phone housekeeping session):** The skill was invoked at the start, and later only to satisfy stop-gate. After compaction the Session Start Protocol was not re-run, and no observation was logged across a long session that had loggable friction: cwd bounced by `cd`, an auto-mode classifier denial on `git rm -f`, and asking the operator a decision question in jargon ("revert the fold"). It ran again only when the operator asked "why is /task-observer available and not being used?". stop-gate checks for a Skill call and a checkpoint line, and both can be met without any logging. Barrier still missing: a SessionStart `compact` matcher that re-runs session-start-scan.sh, and a stop-gate check that the session wrote an observation or a checkpoint line naming what was considered.
