---
id: 19
title: "Cleanup deleted the newer version (Kokoro v1.1) and kept the older; an ambiguous 'yeah' was read as approval of two open questions"
status: actioned
type: open-source
skill: []
proposes_skill: []
target_file: ["~/.claude/projects/-data-data-com-termux-files-home/memory/feedback_keep_newest_version.md"]
siblings_checked: "feedback_keep_cross_chip_variants, feedback_same_model_bytes_differ"
area: "device cleanup / dedup decisions; approval interpretation"
date: 2026-10-02
session_context: "Model and voice-stack cleanup on the phone; cleanup table asked two questions (cut Kokoro v1.1? cut MTP Gemma + E2B?) and the operator replied 'Yeah cuz I know we're going to be deleting way more than six'"
parked_until:
resolved: 2026-10-08
resolution: "Already applied in live ~/.claude/CLAUDE.md lines 103-106 (Keep the newest; Approval is per item); found by weekly review presence check"
reference:
---

**Issue:** The cleanup table recommended cutting Kokoro v1.1 because no script referenced it, while the older v1.0 stayed because scripts pointed at it. The agent then treated a general "yeah" as a yes to both open questions and deleted v1.1. Operator: "if I have a more up-to-date version don't fucking cut the newer one and keep the older one." (Mitigation found afterwards: hexgrad's v1.1-zh card says it is not a strict upgrade; still the wrong default.)

**Suggested improvement:** In any cleanup table, mark version pairs explicitly with default verdict "keep newest; repoint scripts". "Referenced by scripts" is never a reason to keep the older version. When a reply doesn't name the numbered questions, ask them again before any delete.

**Principle:** Deletion approval must be specific to the item; a general assent covers only what was unambiguous.
