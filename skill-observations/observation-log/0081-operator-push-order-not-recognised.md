---
id: 81
title: "git-gate held a push the operator had ordered in plain words (e31333)"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["NovAExopia frankenstein/plugins/aesops-enforcements/scripts/git-gate.sh"]
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

**Issue:** The operator wrote 'PUSH EACH branch'; the gate recognises only 'push now' or wrap-up, so the push was held. The agent should have told the operator the exact phrase at the start.

**Suggested improvement:** Accept the operator's explicit push order, or state the required phrase when the job opens.

**Principle:** When a gate needs a specific phrase, say so before the work, not after the block.
