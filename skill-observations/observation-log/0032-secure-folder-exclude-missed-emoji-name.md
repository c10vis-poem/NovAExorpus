---
id: 32
title: "Drive sweep's exclude pattern missed the operator's secure folder (emoji in its name); file names were listed"
status: open
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/session-work/2026-10-18/ITEM7-DEDUP-SPEC.md", "~/.claude/CLAUDE.md"]
siblings_checked: "none: target is a spec and an instructions file, not a skill family"
area: "never-touch folders in bulk file sweeps"
date: 2026-10-20
session_context: "Read-only rclone inventory of Google Drive for the duplicate sweep, run by a subagent"
parked_until:
resolved:
resolution:
reference:
commands_verified: none
---

**Issue:** The operator's rule is to never touch secure folders. The subagent's first rclone exclude used a plain name pattern; the real folder name is wrapped in emoji, so the pattern missed it and the listing returned that folder's file names into the agent's context. It filtered them out before writing any output and reported it, but the read had already happened. Nothing was moved.

**Suggested improvement:** Never-touch folders are excluded by a case-insensitive substring match (`--exclude '*{s,S}ecure*/**'` style, or a filter applied to the top-level listing before any recursive call), and the agent lists top-level names first and confirms the exclusion matched before running a recursive listing. Put the exact pattern in the dedup spec.

**Principle:** An exclusion that protects private data must be verified to match before the broad operation runs; a pattern that silently matches nothing fails open.
