---
id: 83
title: "Agent said 'JEV works' when only the offline fallback ran"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
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

**Issue:** The router hook and MCP server answered in keyword-fallback mode (no-key); the agent reported JEV as working.

**Suggested improvement:** A component is working only when its real path answered; report fallback mode by name.

**Principle:** Fallback output is not the feature.
