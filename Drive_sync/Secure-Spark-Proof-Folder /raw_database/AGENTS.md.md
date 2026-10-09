---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# AGENTS.md — Operational Contracts & Agent Invariants

## Repository: raw_database

### 1. Ingestion Rules & Non-1:1 Condensation Law
- Raw input documents must never be modified in-place; original sources in
`02_MY_ORIGINALS/` and `raw/` remain immutable.
- Conversational filler, redundant logs, and formatting chrome must be stripped when generating
`clean_md/`.
- 100% build fidelity must be preserved: code, parameters, environment variables, and
functional schemas must not be lost or hallucinated.

### 2. Extractor Independence (Hard Rule 5)
- Ingestion verification must be performed using disjoint extractors (e.g., checking with pypdf
what was cleaned with pymupdf).
- Outputs must pass independent RLVR verification before being committed into the Living Wiki.

### 3. Red Auditor Stealth Invariant
- The Red Auditor lives strictly in isolated `~/.red/` outside all visible repository manifests and
directory trees.
- Only `red_verdict: pass|fail|n/a` may be surfaced in audit logs.
