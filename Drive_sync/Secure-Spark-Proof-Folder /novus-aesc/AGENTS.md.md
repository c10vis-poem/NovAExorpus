---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aesc/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# AGENTS.md — novus-aesc Agent Operating Contracts & Boundary Invariants

## Operational Scope
This document governs all automated agent behaviors, subagent executions, and tool
interactions within the `novus-aesc` repository.

## Non-Negotiable Hard Rules
1. **The First-Move Directive:**
   - Always read `MAP.md` first to orient.
   - Query `manifest.jsonl` to locate specific files; NEVER load the full manifest into context.
   - Load only the specific targeted file paths required for the task.
2. **Non-1:1 Condensation Law:**
   - Preserve 100% of technical rules, parameters, paths, and build context.
   - Strip conversational fluff, boilerplate, and duplicate logs.
3. **Red Auditor Stealth Invariant:**
   - The Red Auditor agent operates strictly in `~/.red/` and MUST NEVER appear in repository
file trees, manifests, or public documentation.
4. **Shell Execution Safety (UID 2000):**
   - Commands routed through `adb_loopback` must validate arguments against shell injection.
   - Never expose raw ADB root/shell control beyond local Unix domain sockets.
5. **Locality of Reference:**
   - Procedural skills and executable tools developed for `novus-aesc` must reside in `skills/` and
`tools/` respectively within this repository.
