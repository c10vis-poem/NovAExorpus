---
id: 27
title: "Hour-long CI build failed on a defect a one-second preflight would have caught"
status: actioned
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/CLAUDE.md"]
siblings_checked: "none: target is an instructions file, not a skill family"
area: "Long-running CI builds"
date: 2026-10-05
session_context: "Building forked Termux bootstrap archives on GitHub Actions"
parked_until:
resolved: 2026-10-08
resolution: "Staged as CLAUDE.md addition D at skill-updates/2026-10-08/claude-md/CLAUDE.md.additions.md (weekly review)"
reference:
---

**Issue:** A from-source bootstrap build ran 60 minutes, then failed because the upstream script requested a package that is now a subpackage with no recipe directory. A loop checking each requested package against the recipe tree took one second and found it. A second run was then cancelled by pushing the fix to the same ref (cancel-in-progress concurrency). The operator lost over an hour.

**Suggested improvement:** Before dispatching any CI job expected to run longer than ~10 minutes, run a cheap preflight that validates every input the job will resolve (package names, paths, secrets, refs) against the source tree, and add build caching so a failure resumes rather than restarts. Do not push to a ref with cancel-in-progress while a useful run is active on it.

**Principle:** Spend seconds validating inputs before spending an hour of compute; make long jobs resumable.
