---
id: 79
title: "settings-guard blocked any command that merely mentioned the hooks-off key"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["NovAExopia frankenstein/plugins/aesops-enforcements/scripts/settings-guard.sh"]
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

**Issue:** Writing a PENDING note and a test about Aesop-Xi's hooks-off setting was blocked because the command text contained the key next to python3 or a redirect. Fixed: blocks only when a settings file is the write target.

**Suggested improvement:** Guards match the write target, not words in the payload.

**Principle:** A guard that fires on documentation of the thing it guards blocks the fix.
