---
id: 85
title: "Agent reported gate blocks back to the operator (or called the gates contradictory) instead of fixing the defect or following the gate's own directions"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "no family registry; checked, applies to the rules and hooks plugin and any agent working under it"
area: "rules and hooks"
date: 2026-11-09
session_context: "Session d1c1bec4 (Termux audit), security-breach study; record in NvAEx-Recaps Security Breach-d1c1bec4-e840-4acf-84d6-67a1d464a00f"
parked_until:
resolved:
resolution:
reference: "NovAExopia branch rules-fix-2026-11-09; PENDING.md section 2026-11-09"
commands_verified: none
---

**Issue:** Across many turns the agent stated 'blocked, job closed, send #' while the cause was a gate defect it could see in the code; the operator had ordered that nothing keeping rules working is postponed.

**Suggested improvement:** When a block comes from a gate defect, name the defect and fix it as part of the job.

**Principle:** A gate defect is part of the job, not a reason to stop.

**Second instance (2026-11-10, session f45e5ad0, operator correction e888):** the stop gate asked for the task-observer session-start scan. The agent first ran it piped through `grep`, against the skill's own rule (read the output whole, never through head, tail or grep). It was blocked, and the agent then told the operator the stop gate and the direction gate "contradict each other" and asked for a job to be opened. Operator: "your claim about the stop hook contradicting themselves is bullshit. they're doing their job just fine. You just need to follow the directions." Session protocols are part of the session, not a job, and a `#` directive may come anywhere in a message. Protection in play: the skill rule was written down and loaded, and the agent still broke it. This is the second miss, so the fix is a barrier, not text: the stop gate's message should give the exact scan command to run, so the agent has nothing to improvise.
