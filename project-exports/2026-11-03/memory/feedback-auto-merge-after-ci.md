---
name: feedback-auto-merge-after-ci
description: User wants PRs set to auto-merge once CI passes, not left as drafts waiting on them
metadata:
  type: feedback
  modified: 2026-10-25T20:53:24.968Z
---

On 2026-10-25 the user said: "Just set it to auto merge after the CI passes like every other GitHub workflow."

**Why:** they don't want to merge by hand after green CI.

**How to apply:** after opening a PR, mark it ready and enable auto-merge. On NvAEx-Recaps (private, GitHub Free) auto-merge is off in repo settings and branch protection isn't available, so there the equivalent is to squash-merge once every check on the head commit is green. Still never merge on red CI. Related: [[plugins-panel-mod]].
