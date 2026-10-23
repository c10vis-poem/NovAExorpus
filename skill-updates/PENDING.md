# Staged updates manifest
Producer: weekly review 2026-10-08 (dispatched worker, subagent item4). Root $V/PENDING.md is a different file.
Reconciled by weekly review 2026-10-23 (subagent). Final state per entry below; headings without `[installed` are still pending for staged-updates.sh.

## android-termux-operator -> skill-updates/2026-10-08/android-termux-operator/ (user-owned, category a; install = copy over ~/.claude/skills/android-termux-operator) [installed 2026-10-23: 3 Safety rules applied to live ~/.claude/skills/android-termux-operator/SKILL.md (no repo source); obs 0004 sed replaced with a tested one]
- obs 0004 -> Safety -> redact secrets when inspecting config (sed command NOT RUN)
- obs 0025 -> Safety -> operator-shell fit, fail closed on empty secret
- obs 0009 -> Safety -> edit only verified-false lines; handoff note is not authorisation
No .skill bundle packed (worker run, no packer step); install by directory copy.
- Reconciled 2026-10-23: diff -rq staged vs live: only SKILL.md line 63 differs, and live's line is the tested replacement of the staged sed. State (b), live supersedes. Done.

## ~/.claude/CLAUDE.md additions -> skill-updates/2026-10-08/claude-md/CLAUDE.md.additions.md (paste by hand) [installed 2026-10-23: operator installed the agents-md-v2 split (check-lines MISSING: 0); C and D live in ~/.agents/AGENTS.md (Preflight before auto-merge; Long CI jobs), E live in ~/.claude/CLAUDE.md (Session End: durable, not scratchpad)]
- A absence claims (0007, 0016, 0024, 0008-pt3); B subagent progress-file writer + delegation (0023, 0028); C auto-merge preflight (0026); D long-CI preflight (0027); E durable-not-scratchpad (0008)
- State 2026-10-23: A and B are live in ~/.claude/CLAUDE.md ("Behavioral Constraints, from observations (added 2026-10-22)", lines 119, 132, 134). C, D, E are NOT live: they are carried by the staged AGENTS.md drafts at ~/.claude/session-work/2026-10-23/agents-md/ (global/AGENTS.md lines 54, 61, 132; install steps in INSTALL.md there). This file is superseded by those drafts; the entry clears when the operator installs them (then mark `[installed <date>]`) or types #staged-defer.

## Hook specs -> skill-updates/2026-10-08/proposals/hooks-spec.md (design only; operator decides which to build)
- 0017, 0005, 0012, 0023, 0028, 0024, 0006
- State 2026-10-23 (mapped against ~/repos/Aesop-Xi/hooks/): item 8 (obs 0030) built and live (carryover.sh, H9). Items 2 (half: H2 sync-on-use does the fork sync), 4 (partly: subagent-stop-gate.sh) and 7 (partly: stop-gate scan check) are partial; items 1, 3, 5, 6 not built. Everything not built was handed to BOARD-INTAKE.md "Thread: skills and plugins" (item "Unbuilt hook specs"). Not installed: the board thread or the operator decides; #staged-defer clears it per session.

## Upstream draft -> skill-updates/2026-10-08/proposals/task-observer-upstream.md (0015; not sent)
- State 2026-10-23: the fix is already in the operator's fork (c10vis-poem/aesop-task-observer PR #1, 09a4101; obs 0015 archived actioned 2026-10-22). Open question for the operator: send it to rebelytics/one-skill-to-rule-them-all (duplicate search not yet run) or drop the draft.
