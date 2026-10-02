---
id: 15
title: "Review parked mid-session was never resumed or recorded; next session reported 'never reviewed'"
status: open
type: open-source
skill: [task-observer]
proposes_skill: []
target_file: []
siblings_checked: "none — task-observer belongs to no family"
area: "weekly-review interruption; Session Start step 3"
date: 2026-10-01
session_context: "2026-10-01 business-account session parked a review after presenting 4 decisions; 2026-10-02 session start read last-review-date=never and told the operator no review had run"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** The operator asked for a review. The agent read all open entries and presented 4 decision groups, then parked the review at the operator's request to handle earlier items. It never came back to it, and wrote no partial-review marker. Several fixes then landed as ordinary work (the SessionStart/PreToolUse hooks), but the entries were left open. The next session read `last-review-date.txt` = `never` and told the operator "no review has ever run", which contradicted what the operator remembered.

**Suggested improvement:** weekly-review.md: when a review is interrupted, write `skill-observations/review-in-progress.md` (date, decision groups, entries decided so far). Session Start step 3 reads it and offers "resume the parked review from decision N" instead of a fresh offer. Also, before calling a backlog unreviewed, the session-start step should check for that marker.

**Principle:** An interrupted multi-step procedure needs an on-disk progress marker. Otherwise its absence and its partial completion look the same to the next session, and the agent reports the absence as fact.
