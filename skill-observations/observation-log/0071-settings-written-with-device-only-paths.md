---
id: 71
title: "Agent wrote phone-only absolute paths into settings, breaking every off-phone session (e23854)"
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

**Issue:** Hook entries in ~/.claude/settings.json called /data/data/com.termux/.../plugins/cache/... and both marketplaces pointed at local folders, also in the vault's committed .claude/settings.json. No cloud or other-device session can load them. Operator correction e23854.

**Suggested improvement:** Before writing any settings or plugin path, check it resolves on every device the repo runs on; committed settings use repo-relative or marketplace references only.

**Principle:** Committed configuration must not depend on one machine's filesystem layout.
