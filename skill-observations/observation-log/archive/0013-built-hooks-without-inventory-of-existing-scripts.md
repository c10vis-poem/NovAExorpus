---
id: 13
title: "New hooks were written before inventorying the existing scripts, hooks and skills"
status: actioned
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/ENFORCEMENTS.md", "~/.claude/INVENTORY.md"]
siblings_checked: "no family registry; checked — workflow rule, not tied to one skill"
area: "building tooling"
date: 2026-10-01
session_context: "Agent wrote ~10 Claude Code hooks (sync, ship, ledger, gates) before auditing ~/bin, repo git hooks, vault scripts and custom skills. The later audit found overlaps (old sync-forks/ship-session, unwired interceptors), dead paths, and scripts broken by the session's own clone deletion."
parked_until:
resolved: 2026-10-01
resolution: "Three-part audit (inventory-code, inventory-vault-scripts, inventory-skills) consolidated in ~/.claude/INVENTORY.md; ENFORCEMENTS row 'inventory' blocks tools on any prompt about writing/adding a hook/script/skill/tool until INVENTORY.md is read."
reference: "~/.claude/session-work/2026-10-01/inventory-*.md"
---

**Issue:** Tooling was designed from scratch while equivalent or conflicting tools already existed on the device. The overlap and breakage only surfaced afterwards.

**Suggested improvement:** Done: inventory first, enforced by a blocking rule, and a row is added whenever something new is built.

**Principle:** Before building a capability, enumerate what already exists for it. Rebuilding blind creates duplicates and breaks whatever depended on the old pieces.
