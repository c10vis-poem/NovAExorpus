---
id: 76
title: "Rule 1 gate opened only on a # at the very start of a message"
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

**Issue:** The operator wrote '#go ahead' at the end of a message, and Claude Code can drop a leading #; the gate ignored both, so the operator's direction did not open the job. Fixed on rules-fix-2026-11-09 (any # word or 'hashtag').

**Suggested improvement:** Test the opener against the operator's real messages, dictation and the CLI's own handling of #.

**Principle:** A gate's trigger must match how the operator actually types and dictates, not an idealised format.
