---
id: 3
title: Two populated observation-log workspaces exist for the same device/project
status: actioned
type: open-source
skill: [task-observer]
proposes_skill: []
siblings_checked: none (no skill-families.md registry present on device)
area: environments / workspace anchoring
date: 2026-09-25
session_context: Session-start protocol for /android-termux-operator on this Termux device
resolved: 2026-09-26
resolution: "Operator chose the vault as the one shared log (NovAExorpus/skill-observations, synced by GitSync); both device logs merged, open entries re-issued as 5-6, old locations replaced by pointers, path pinned in ~/.claude/CLAUDE.md."
reference:
---

**Issue:** Two independent, populated `skill-observations/` workspaces exist:
`~/.claude/skill-observations/` (ids 0003-0005, `.id-floor`=5, files dated
Sep 17-22) and
`~/.claude/projects/-data-data-com-termux-files-home/skill-observations/`
(ids 0001-0002, `.id-floor`=2, files dated Sep 6-18). Both resolve as
plausible "stable project identity" anchors on a single-user, single-project
Termux device where CWD is always `~`, so different sessions picked
different anchors instead of discovering and adopting the existing one, per
the environments.md "search plausible anchors first" rule.

**Suggested improvement:** At next weekly review, diff both logs, merge
into one canonical location (the `~/.claude/projects/<project-id>/` form
matches the pattern already used by the memory system at
`~/.claude/projects/-data-data-com-termux-files-home/memory/`), renumber
ids to avoid collisions, and pin the resolved path explicitly in this
device's CLAUDE.md activation instruction so future sessions stop
re-deriving (and mis-deriving) the anchor.

**Principle:** On a device/project where the working directory never
varies, "search the plausible anchors" is not enough to prevent a fork —
the anchor must be pinned literally (not just described structurally) in
the activation config, or every fresh session re-derives it independently
and forks are inevitable.
