---
id: 72
title: "Agent inverted the AGENTS.md / CLAUDE.md / settings.json roles (e29458)"
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

**Issue:** The agent proposed plugin installs through ~/.claude and GitHub marketplaces. The operator's design: in each repo the plugins are written to that repo's settings.json; CLAUDE.md only holds pointers; AGENTS.md is the authority the agent follows. Operator correction e29458.

**Suggested improvement:** Write the layout (AGENTS.md authority, CLAUDE.md pointers, repo settings.json plugins) into AGENTS.md and check new settings against it before any write.

**Principle:** Follow the instruction file the project names as authoritative; pointer files point, they do not decide.
