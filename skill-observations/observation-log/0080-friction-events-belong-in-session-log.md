---
id: 80
title: "Friction events were stop-hook demands instead of session-log entries"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["NovAExopia frankenstein/plugins/aesops-enforcements/scripts/observe-event.sh, stop-gate.sh"]
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

**Issue:** observe-event queued gate blocks, failures and corrections and stop-gate held every turn until each was logged or dismissed; the operator: they go in the session log, and the stop hook only applies if wrap-up did not write them. Fixed.

**Suggested improvement:** Logging is automatic; enforcement is at wrap-up.

**Principle:** Record as it happens; gate only where the record can be missing.
