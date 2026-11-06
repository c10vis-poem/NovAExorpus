---
id: 57
title: "Gave a verdict on a hook set and a mapping of what it loses after reading only its docs, not the scripts"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.agents/AGENTS.md"]
siblings_checked: "none: target is the shared instructions file (Read Before Claim); principle 3 and 10 are related"
area: "audits of existing code; claims about what a change disables"
date: 2026-11-05
session_context: "Reviewing a consolidated hook set and a plan to wire only part of it."
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: read all 26 hook scripts afterwards; grep of marker writers at the commit showed one script writes the check-in, wrap-up and push markers"
---

**Issue:** The agent told the operator a consolidation had just switched hooks off, and gave a table of losses and a folding map, while having read one of 26 scripts. The table came from the package's own docs. Reading the code changed the finding: some hooks are still called by others, and one unwired hook is the only writer of markers that four kept rules depend on.

**Suggested improvement:** Before stating what removing or wiring a component does, read the component and grep for writers of the state it produces. Report descriptions taken from docs as descriptions, not findings.

**Principle:** A dependency between components lives in the code, usually as shared state. A document listing what each part does cannot show what breaks when one is removed.
