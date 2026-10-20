# Proposed structural barriers (SPECS ONLY, nothing built or installed)
Staged by weekly review 2026-10-08. Each repeated-failure rule needs a barrier, not new wording.
Hooks live in aesop-xi/hooks/ (live copies ~/.claude/hooks/); building them is a code change and goes through the fork pipeline once approved.

1. secret-guard.sh (obs 0017): PreToolUse Bash refuses rm/mv/truncate/redirect targeting `~/.claude/state/*` (wrapup-, pushnow-, required-, resume-*.ok). Verified gap: current secret-guard.sh has no state/ rule. Clearing only via user-typed override.
2. Install preflight (obs 0005, 3rd+ instance incl. this review): PreToolUse Bash blocks `pip install|npm install|make|cargo build` inside a git checkout until a marker shows the platform/install doc was Read and the fork was compared with upstream this session.
3. context-diff.sh (obs 0012): SessionStart prints the 3 newest sessions across ALL `~/.claude/projects/*` dirs (title, folder, time). Current script only diffs CLAUDE.md/MEMORY.md (hooks/context-diff.sh line 4).
4. Agent PreToolUse (obs 0023): refuse subagent_type Explore/Plan when the prompt mentions a progress file.
5. Delegation trip-wire (obs 0028): PreToolUse Bash counter per turn; above ~6 calls touching >3 repos inject "delegate to subagents".
6. Stop-hook absence-claim flag (obs 0024, 0007, 0016): flag reply text matching "none chosen|never decided|not installed|does not exist" with no Read/grep/ls in the same turn.
7. stop-gate.sh (obs 0006 remainder): currently checks skill loaded (stop-gate.sh lines 46-50) and scan written; it does not check protocol steps beyond the scan (hand-rolled scan, skipped staged-work reconciliation). Optional: require the checkpoints.log line format the snippet writes.
8. stop-gate.sh (obs 0030): count how many consecutive RESUME snapshots a START HERE item appears in (match by item text). From the second carry-over, refuse `/defer` for that item unless the operator types a reason; wrap-up blocks until the item is done with evidence or blocked on a named operator action. "Partly done" is not an accepted status. Verified gap 2026-10-09: stop-gate.sh handles done/deferred per item (lines 27-34) but keeps no carry-over history.

Coverage check 2026-10-09 (obs 0029 rule): items 1, 3, 4, 5, 6, 8 are not covered by H1 to H8 (README read this date; secret-guard.sh has no state/ rule, context-diff.sh only diffs CLAUDE.md/MEMORY.md, settings.json has no Agent matcher). Item 2 is half covered: H2 sync-on-use does the fork-vs-upstream sync; the "platform doc was read" half is not. Item 7 is partly covered by H1 stop-gate (skill loaded, scan written).
