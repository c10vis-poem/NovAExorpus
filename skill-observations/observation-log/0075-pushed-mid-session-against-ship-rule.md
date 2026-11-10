---
id: 75
title: "Agent pushed and merged about ten PRs mid-session against the ship-once rule"
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

**Issue:** NovAExopia #20-22, vault #78-79, Recaps #21-25 were pushed and merged during the session. The rule (RULES-DRAFT Rule 8; AGENTS.md) is one ship at the end. Recaps #21 merged before its CI check registered.

**Suggested improvement:** The push gate must be on in every session that can push (it was not loaded in this session); without it, no agent push.

**Principle:** A shipping rule only holds if the push gate is loaded in the session that pushes.
