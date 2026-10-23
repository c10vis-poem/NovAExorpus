---
id: 18
title: "resume-gate and enforce-gate deadlock (body lost in an interrupted write)"
status: superseded
type: internal
skill: []
proposes_skill: []
target_file: ["~/repos/Aesop-Xi/hooks/enforce-gate.sh", "~/repos/Aesop-Xi/hooks/resume-gate.sh"]
siblings_checked: "none: target is hook scripts, not a skill family"
area: "PreToolUse gate ordering"
date: 2026-10-02
session_context: "Unknown: the file was created 2026-10-02 08:36 and left 0 bytes by an interrupted write; only the filename survives."
parked_until:
resolved: 2026-10-22
resolution: "Lost in an interrupted write (0-byte file); topic known only from the filename. Covered by later hook work: Aesop-Xi hooks/enforce-gate.sh line 7 exits until state/resume-<sid>.ok exists ('resume-gate goes first; no deadlock'), and resume-gate.sh writes that file once RESUME.md is read, so the two gates cannot block each other. Present on origin/main 44cb472."
reference:
commands_verified: none
---

Body lost. Kept as a placeholder so id 18 is never reused.
