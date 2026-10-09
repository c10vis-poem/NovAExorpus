# Proposed additions to ~/.claude/CLAUDE.md (STAGED, not applied)
Staged by weekly review 2026-10-08. Review, then paste each block yourself. Anchors are current live lines (CLAUDE.md read this review).

## A. Read Before Claim, after the "Canonical example" paragraph (obs 0007, 0016, 0024; also 0008 point 3)
- **Absence claims name their probes.** Before saying X "doesn't exist / was never
  decided / isn't installed", check the record that would hold it: decision docs
  (RESUME, PENDING, docs/*GUIDE*, memory), `ls`/config for installed tools, and for
  repos the default branch plus fork branches plus upstream PR heads. Report "not
  found by <probes>", never "does not exist". For a vendor source, run its documented
  CLI/API first. Subagent reports say what their batch contained, never what exists.
  Before "no records", grep raw transcripts (`~/.claude/projects/*/*.jsonl`).

## B. Subagents section, after the progress-file bullet (obs 0023, 0028)
- The progress file needs a writer: spawn with a type that has Write (general-purpose
  or builder), never Explore/Plan; or the parent writes and updates the file itself.
- Audit-shaped work (more than ~6 Bash calls across more than 3 repos/dirs) goes to
  subagents, not inline. (Text has failed twice; a trip-wire hook is in
  proposals/hooks-spec.md items 4 and 5.)

## C. GitHub Fork Workflow, step 2, before `gh pr merge --auto` (obs 0026)
- Preflight before auto-merge: `gh api repos/O/R/branches/B/protection` shows required
  status checks AND at least one workflow has run on the fork. If not, do not enable
  auto-merge: wait for green, merge by hand, ask the operator to set protection.
  Auto-merge on a branch with no required checks means "merge now".

## D. New short section "Long CI jobs" (obs 0027)
- Before dispatching CI expected to run over ~10 minutes, validate every input the job
  resolves (package names, paths, secrets, refs) against the source tree in a cheap
  preflight; add caching so a failure resumes. Never push to a ref with
  cancel-in-progress while a useful run is active on it.

## E. Session End section (obs 0008)
- Anything a future session needs never lives only in the session scratchpad: copy it
  to a durable path before closing. (`archive-scratchpad.sh` already copies the
  scratchpad on SessionEnd/PreCompact; this rule covers the "write it durably at
  creation" half.)
