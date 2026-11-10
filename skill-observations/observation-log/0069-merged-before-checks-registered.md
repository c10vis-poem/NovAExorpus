---
id: 69
title: "Merged a private-repo PR before its CI check registered, then claimed the repo had no CI"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: ["aesop-enforcements scripts/ship-session.sh (private-repo wait-for-green path)"]
siblings_checked: "no family registry; checked, applies to any agent shipping a PR on a repo without auto-merge"
area: "shipping; CI verification"
date: 2026-11-08
session_context: "Shipping a memory file to a private repo on the free plan (no auto-merge). gh pr checks --watch ran seconds after the PR was created, printed 'no checks reported', and the merge ran in the same command."
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: gh run list showed the pull_request run (success) created 16 s after the push; the merge had already happened"
---

**Issue:** 'No checks reported' right after PR creation was read as 'no CI', the PR was merged in the same command, and the operator was told the repo had no CI. The workflow existed (.github/workflows/ci.yml, on: pull_request) and passed.

**Suggested improvement:** Ship scripts wait until at least one check run exists for the head SHA (poll gh run list --commit <sha> for up to 2 minutes) before reading the check result. An empty check list means "not yet", never "none", unless the workflow listing is also empty.

**Principle:** An empty result from a status probe taken right after an event is a timing artifact until a second probe, or a listing of the source (here, the workflow files), confirms it.
