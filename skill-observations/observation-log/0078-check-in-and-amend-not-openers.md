---
id: 78
title: "Rule 2's check-in (okay, amend, override, defer) was flagged as either/or and amend did not open the job"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["NovAExopia frankenstein/plugins/aesops-enforcements/scripts/question-gate.sh, direction-gate.sh"]
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

**Issue:** question-gate blocked 'Okay, amend or override?'; direction-gate did not accept 'amend', 'override: ...' or 'defer'. Both fixed.

**Suggested improvement:** Every word of the operator's check-in vocabulary is an opener and an allowed ending.

**Principle:** Two gates must not contradict the rule format the operator wrote.
