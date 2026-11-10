---
id: 77
title: "A comment sent mid-job closed tools, against Rule 1's one-okay-covers-the-job"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["NovAExopia frankenstein/plugins/aesops-enforcements/scripts/direction-gate.sh"]
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

**Issue:** Mid-turn messages without an opener ('its erasing the hashtag', 'What closed the job?') closed the job; the agent then reported 'the job is closed'. Fixed: only stop, hold or wait closes.

**Suggested improvement:** Gate tests include mid-turn comments during an open job.

**Principle:** The unit of permission is the job; only an explicit stop ends it.
