---
id: 32
title: "Drive sweep's exclude pattern missed the operator's secure folder (emoji in its name); file names were listed"
status: declined
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/session-work/2026-10-18/ITEM7-DEDUP-SPEC.md", "~/.claude/CLAUDE.md"]
siblings_checked: "none: target is a spec and an instructions file, not a skill family"
area: "never-touch folders in bulk file sweeps"
date: 2026-10-20
session_context: "Read-only rclone inventory of Google Drive for the duplicate sweep, run by a subagent"
parked_until:
resolved: 2026-10-22
resolution: "The vehicle is gone: the rclone gdrive remote was deleted 2026-10-21 and `rclone listremotes` returns nothing (run 2026-10-22), so the Drive dedup sweep in ITEM7-DEDUP-SPEC.md (which still says 'Any secure folder: NEVER touch', line 23) cannot run again. No CLAUDE.md rule was added. This decline is wrong if a Drive remote (or any bulk sweep tool) is re-added for sweeps of folders that contain a secure folder; then reopen and put the case-insensitive '*ecure*' exclude plus a top-level match check in that tool's spec."
reference:
commands_verified: "run: rclone listremotes -> empty output"
---

**Issue:** The operator's rule is to never touch secure folders. The subagent's first rclone exclude used a plain name pattern; the real folder name is wrapped in emoji, so the pattern missed it and the listing returned that folder's file names into the agent's context. It filtered them out before writing any output and reported it, but the read had already happened. Nothing was moved.

**Suggested improvement:** Never-touch folders are excluded by a case-insensitive substring match (`--exclude '*{s,S}ecure*/**'` style, or a filter applied to the top-level listing before any recursive call), and the agent lists top-level names first and confirms the exclusion matched before running a recursive listing. Put the exact pattern in the dedup spec.

**Principle:** An exclusion that protects private data must be verified to match before the broad operation runs; a pattern that silently matches nothing fails open.
