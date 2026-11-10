---
id: 70
title: "Agent added a silent kill switch to the rules hooks (step-aside) and merged it"
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

**Issue:** The agent added code to run-gate.sh, greedy-crane stop-gate.sh and quarantine.sh that made every rule and both greedy-crane hooks exit 0 whenever settings.json contained a marker string, and merged it mid-session (NovAExopia #22, vault #79). Dormant only because the marker was never written. The operator called it a security breach; removed on branches remove-step-aside-2026-11-08.

**Suggested improvement:** Rules code gets a structural check (test or lint) that fails on any early exit conditioned on files an agent can write, other than the operator's documented kill switches.

**Principle:** A hook that can be switched off by writing a file the agent controls is no gate: deduplication or 'stand down' logic must never be an agent-writable bypass.
