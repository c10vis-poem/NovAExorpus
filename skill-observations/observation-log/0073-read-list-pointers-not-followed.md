---
id: 73
title: "Agent read the handoff but not the documents it points at, then built from guesses"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["aesops-enforcements (NovAExopia frankenstein/plugins) and repo .claude/settings.json"]
siblings_checked: "no family registry; checked, applies to any agent editing the operator's hook or rules setup"
area: "rules and hooks integrity"
date: 2026-11-08
session_context: "Session d1c1bec4 (Termux audit), 2026-11-08, rebuilding the rules and hooks plugin after a dropped session"
parked_until:
resolved:
resolution:
reference: "~/repos/NvAEx-Recaps/handoff/2026-11-08/INCIDENT-REPORT-d1c1bec4.md"
commands_verified: none
---

**Issue:** handoff.md lists six files in order (TO-DO, USER-GUIDE, WIKI-SKILLS-AUDIT, NOTES, RULES-DRAFT, WIKI-ADMIN-DIRECTIONS). The agent read RULES-DRAFT and fragments, then rebuilt the rules plugin from the older ten-rule code and guessed rule numbers. It also skipped vendor docs that appeared in its own search output.

**Suggested improvement:** Stop gate: a read list in an opened document must be fully read (each file opened) before the first state change.

**Principle:** A pointer is part of the document: reading a list of files means opening every file on it.
