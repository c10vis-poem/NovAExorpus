---
id: 44
title: "Subagent script run wrote 400 files into the vault (2nd time) and session ran a superseded RESUME plan"
status: open
type: internal
skill: [task-observer]
proposes_skill: []
target_file: ["~/repos/Aesop-Xi/hooks/resume-gate.sh", "~/repos/Aesop-Xi/hooks/change-log.sh"]
siblings_checked: "no skill-families.md registry; instance-specific to the operator's hook layer, no skill sibling applies"
area: "hooks: change-log is log-only; resume-gate never re-checks hash"
date: 2026-10-24
session_context: "RESUME items 0/3/5 run as subagents; session 2527f2c9 opened 2026-10-23 00:22, acted 2026-10-24"
parked_until:
resolved:
resolution:
reference: "~/.claude/state/changes-2527f2c9-821f-4595-bf2a-3285c7fbe10d.log (01:10:26 SCRIPT line); same accident 2026-10-23 03:03 in another session's changes log"
commands_verified: "run: git status after cleanup -> only checkpoints.log modified"
---

**Issue:** (1) A subagent ran `python3 -I tools/check.py --help` in the vault; check.py ignores --help, ran a full pass, wrote 400 untracked audit/*.check.md and rewrote audit/rlvr_verification_report.md. change-log.sh logged it but blocks nothing; checkin-gate's write-verb list doesn't treat interpreter runs as state-changing. Identical accident on 2026-10-23 (364 files). Cleanup by the subagent was denied by the classifier (event e7152); orchestrator cleaned up on operator order. (2) resume-gate stores RESUME's hash at first read but exits 0 forever after; RESUME was rewritten 14h later by another session, and this session executed the stale START HERE list (all items already done).

**Suggested improvement:** Second occurrence -> structural barrier: block interpreter runs targeting vault/keep without operator #ok-run; resume-gate compares stored hash to current RESUME on each call and blocks on mismatch.

**Principle:** A gate that records a check once and trusts it forever is stale by design on long-lived sessions; a log-only hook is not a protection.
