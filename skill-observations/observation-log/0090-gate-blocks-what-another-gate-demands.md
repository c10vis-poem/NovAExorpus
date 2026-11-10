---
id: 90
title: "One gate blocks what another gate demands; three test sessions in a row deadlocked at the opening"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["Aesop-Xi plugins/aesops-enforcements/scripts/direction-gate.sh", "Aesop-Xi plugins/aesops-enforcements/scripts/stop-gate.sh"]
siblings_checked: "none: target is a hook pair, not a skill family"
area: "session opening: stop-gate vs direction-gate"
date: 2026-11-10
session_context: "crane test sessions on 2026-11-10 (operator's Documents/Fixit/1-3.txt, Download/'without the.txt', Download/'else..txt'), fixed piecemeal from session 437a362c"
parked_until:
resolved:
resolution:
reference: "NvAEx-Recaps handoff/2026-11-10/evidence/"
commands_verified: none
---

**Issue:** The stop-gate holds the turn until the opening protocol (the opening reads, then the task-observer
Session Start Protocol) is done. The direction-gate blocks every tool until the operator opens the job. The two
were fixed one case at a time: first the scan command, then the pointed-to reads, then the protocol's other
commands, then the agent definition lookup. Each test session still deadlocked on the next case. The operator's
verdict after the third test: nothing that was done fixed it.

**Suggested improvement:** One rule in code, not per-case exceptions: whatever the stop-gate demands as an
opening step, the direction-gate lets through. Generate the direction-gate's allow-list from the stop-gate's
opening checklist, so the two cannot disagree, and test them together: one end-to-end test that runs a fresh
session's opening through both gates and expects it to finish with no okay.

**Principle:** Two gates that both judge the same step need one shared source for what that step is. Fixing the
disagreement case by case leaves the next case to the operator.
