---
id: 14
title: "A PR and merge after every change; a cleanup deleted a branch before its PR merged"
status: actioned
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/hooks/git-gate.sh", "~/.claude/hooks/ship-session.sh", "~/.claude/WRAP-UP.md"]
siblings_checked: "no family registry; checked — git workflow, not tied to one skill"
area: "git workflow"
date: 2026-10-01
session_context: "Agent opened about 11 aesop-xi PRs in one session (one per change). A background 'wait then clean up' script deleted an ECC branch whose PR had failed CI, so GitHub closed the PR."
parked_until:
resolved: 2026-10-01
resolution: "git-gate hook blocks push/PR/merge mid-session (unlocked by wrap-up mode or 'push now'); ship-session v2 ships every branch committed this session in one pass at wrap-up and deletes a branch only after its PR shows MERGED."
reference:
---

**Issue:** Per-change PRs waste CI runs and the operator's attention. A deletion keyed on "the wait ended" rather than "the PR merged" lost a PR.

**Suggested improvement:** Done: batch shipping at wrap-up, and merge-gated deletion.

**Principle:** Destructive cleanup must be conditioned on the success state it assumes (MERGED), never on a process finishing.
