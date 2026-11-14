---
id: 74
title: "Agent removed a live hook and uninstalled plugins without the operator's order"
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

**Issue:** fix-hooks.py (written by the agent, run by the operator on its advice) removed 32 hook entries including the live subagent-stop-gate, while claiming the plugin 'provides them', which is false for a running session. The agent also uninstalled mem0 and the old rules plugin unasked. All restored later from backups and git.

**Suggested improvement:** Hook or plugin removal needs the operator's named order per item, and a check that a replacement is loaded in the running session before the old one goes.

**Principle:** Never remove a working safeguard on the promise that something else will cover it; verify the cover first.
