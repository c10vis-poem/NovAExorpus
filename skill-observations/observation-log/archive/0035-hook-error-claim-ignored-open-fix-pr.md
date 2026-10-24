---
id: 35
title: "Said 'no hook errors' after testing only the phone path; the open cloud-session fix PR was never checked"
status: actioned
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none: target is an instructions file; related absence-claim entries 0007, 0016, 0024"
area: "Read Before Claim; absence claims about defects"
date: 2026-10-21
session_context: "Operator asked whether the Aesop-Xi hook error still existed"
parked_until:
resolved: 2026-10-23
resolution: "Rule 'A defect is gone only when checked where it happens' appended to ~/.claude/CLAUDE.md; Aesop-Xi #54 (cloud stand-down) merged, cloud-standdown.test.sh 11/11."
reference: "c10vis-poem/Aesop-Xi PR #54 (fix/cloud-hook-standdown)"
commands_verified: "run: git show origin/main:hooks/run-hook.sh | grep -i remote -> no match (fix not on main)"
---

**Issue:** The operator asked if the error in the Aesop-Xi hook was still there. The agent compared the live phone hooks with main and ran the phone test suite, then said "no hook errors". The error the operator meant only happens in cloud sessions: the gates run there with no RESUME, check-in or vault, and the stop gate blocks again on `stop_hook_active`, so the turn never ends. The fix, PR #54, had been open since 2026-10-18 and was mentioned earlier in the same session. The agent didn't look at open PRs or the environment the error happens in.

**Suggested improvement:** Before saying a known defect is gone, find where it was reported (open PRs, branches, observations, the operator's description) and test in the environment where it happens. Passing tests in a different environment is not evidence.

**Principle:** A defect is gone only once it's been checked on the path where it happens. A clean run on a different path doesn't show that.
