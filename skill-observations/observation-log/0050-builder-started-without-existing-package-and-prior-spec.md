---
id: 50
title: "Started a build agent before inventorying what already existed: missed the pre-built package and the prior full spec"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "no family registry entry; checked, applies to any delegation of a build; principle 10 (inventory before building) already covers it"
area: "delegation / build start"
date: 2026-10-28
session_context: "Phone session 5fc2c8e1: wiki admin build"
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: find ~/repos -iname '*file*admin*' found NovusAExenti/executor-core/file-administrator only after the operator asked"
---

**Issue:** The wiki-admin builder was launched with a plan from one Drive folder. It was not told about the prior full spec (vault handoff 2026-10-24 wiki-admin extract), the toolset guide, or the pre-built agent package already on the agents repo's main branch. The operator had to point at each, in three corrections, while the builder was already writing new files.

**Suggested improvement:** Before delegating any build, run a fixed inventory: search every repo, the vault and its branches for the target's names and synonyms (agent name, codename, role), and the latest handoff folder; pass every hit to the builder. Make the delegation template require an "existing assets found" section.

**Principle:** Inventory what exists before building. A builder told only about new sources rebuilds what is already there. This is cross-cutting principle 10 failing a second time; the next fix must be structural (a required field in the delegation prompt), not a reminder.
