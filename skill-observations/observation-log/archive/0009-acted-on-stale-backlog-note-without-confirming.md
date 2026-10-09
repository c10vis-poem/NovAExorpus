---
id: 9
title: "Removed content on the strength of a stale backlog note, then had to revert"
status: actioned
type: open-source
skill: [android-termux-operator]
proposes_skill: []
target_file: []
siblings_checked: "no family registry entry; instance-specific to doc-editing housekeeping"
area: "housekeeping edits to instruction files"
date: 2026-09-30
session_context: "NovAExorpus housekeeping: fixing false claims in AGENTS.md / aesop-xi"
parked_until:
resolved: 2026-10-08
resolution: "Staged for android-termux-operator at skill-updates/2026-10-08/android-termux-operator (weekly review)"
reference:
---

**Issue:** Asked to fix verified-false claims, the agent also removed a "Honey applies universally" rule in two instruction files because a backlog note said the operator had "dropped Honey". The operator had not asked for that and said to leave Honey alone; one removal had already merged, so it took a second PR to revert.

**Suggested improvement:** When a housekeeping pass is scoped to "fix verified-false claims", edit only lines proven false against source. Anything justified only by a backlog or handoff note gets listed for the operator, not edited.

**Principle:** A handoff note is a pointer to a possible change, not authorisation for it; keep edits to the scope that was actually verified.
