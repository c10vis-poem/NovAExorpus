---
id: 26
title: "Auto-merge enabled on fork PRs with no required checks merged them before CI ran"
status: actioned
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none: target is an instructions file, not a skill family"
area: "GitHub fork workflow: branch, PR, CI, auto-merge"
date: 2026-10-05
session_context: "Pushing a bootstrap workflow and an app package-id change to two freshly created/synced forks"
parked_until:
resolved: 2026-10-08
resolution: "Staged as CLAUDE.md addition C at skill-updates/2026-10-08/claude-md/CLAUDE.md.additions.md (weekly review)"
reference:
---

**Issue:** The mandated pipeline (PR, CI, auto-merge) was followed literally: `gh pr merge --auto --squash` on two forks. Neither fork had branch protection with required status checks, so GitHub merged both PRs immediately. One fork's CI was still running; the other fork's workflows had never run at all (new-fork Actions gate). "CI runs, merges when green" was not true in either case. Setting required checks afterwards was denied by the permission classifier as a CI-bypass-class action, so it now needs the operator.

**Suggested improvement:** In the fork workflow rule, add a preflight before enabling auto-merge: confirm the target branch has required status checks (`gh api repos/O/R/branches/B/protection`) and that at least one workflow has run on the fork. If not, do not enable auto-merge; wait for green checks and merge by hand, and ask the operator to set protection.

**Principle:** Auto-merge only waits for checks the branch requires. On a repo with no required checks it means "merge now", so verify the gate exists before relying on it.
