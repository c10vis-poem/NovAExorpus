---
id: 84
title: "Agent guessed what 'Rule 13' and 'Rule 8' meant instead of reading the rule list"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["RULES-DRAFT.md"]
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

**Issue:** The agent mapped rule numbers from an interim draft, wrote code for a guessed 'menus' rule, and reverted it. The final eleven rules were in RULES-DRAFT.md the whole time.

**Suggested improvement:** Resolve every rule number against the current rule file before acting.

**Principle:** Numbers without the list are guesses.
