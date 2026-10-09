---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aexenti/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# AGENTS.md — novus-aexenti Agent Operational Contract

## 1. Operational Invariants & Rules of Engagement

1. **Locality of Reference**:
   - Skills and tools developed for cognitive routing and reasoning must live directly inside `skills/`
and `tools/` within this repository. Never export local heuristics to arbitrary global trees.

2. **Non-1:1 Condensation Law**:
   - Ingestion and normalization must eliminate conversational filler and duplicate logs, but
preserve 100% of technical rules, parameters, models, and build fidelity.

3. **Red Auditor Stealth Invariant**:
   - The Red Auditor lives strictly in isolated `~/.red/` outside of visible repository trees and
manifests. The only valid surface in this repository is the `red_verdict: pass|fail|n/a` metadata
field.

4. **Hard Rule 5 (Extractor Independence)**:
   - Any verification pass must use disjoint tools/parsers from those used during initial extraction.

5. **Beginner-Proof Standard (Hard Rule 8)**:
   - Any script, config, or routing rule must be structured so that an independent developer or
junior model can pick up and execute without implicit assumptions.

6. **First-Move Directive**:
   - Always read `MAP.md` before searching or loading files. Never load `manifest.jsonl` whole
into context; query and filter it.

## 2. Reference Pointers
- Invariant Authority: `MAPS/Universal file configuration`
- Architecture Reference:
`MAPS/PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md`
- Master Deliverables: `MAPS/A OPERATOR_MAP.md`
