---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novaexopia/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# AGENTS.md — Operational Contracts & Hard Rules for Novaexopia

## Core Invariants

1. **Non-1:1 Condensation Law:**
   - Strip conversational filler and duplicate boilerplate.
   - Maintain 100% build fidelity so that raw and clean markdown build the exact same output.
2. **Red Auditor Stealth Invariant:**
   - The Red Auditor agent lives strictly outside the repository tree in `~/.red/`.
   - Never write to or create `.red/` or `.incognito_red_sandbox/` within the repository.
   - Only expose the `red_verdict: pass|fail|n/a` field on trajectory records.
3. **Locality of Reference:**
   - Skills and tools live locally inside the repository where they are applied (`skills/`, `tools/`,
`scripts/`, `hooks/`).
4. **Hard Rule 5 (Extractor Independence):**
   - Ingestion passes must be verified using disjoint extractors (`tools/check.py`) before
committing to the wiki.
5. **The First-Move Directive:**
   - Read `MAP.md` (orient) ➔ Read tier `MAP.md` (focus) ➔ Query `manifest.jsonl` (filter) ➔
Load targeted files only.
