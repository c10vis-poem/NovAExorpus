---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aeyre/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# AGENTS.md — Agent Contracts & Operational Boundaries for novus-aeyre

## Scope
Defines operating rules, permissions, and constraints for all worker agents touching the
novus-aeyre repository.

### Operational Invariants Codified
1. **Non-1:1 Condensation Law**: Strip conversational fluff and redundant boilerplate, but
preserve 100% of technical rules, parameters, audio sampling rates, buffer configurations, and
build fidelity.
2. **Locality of Reference**: Skills and tools for sensory processing live locally inside skills/ and
tools/ within this repository.
3. **Hard Rule 5 (Extractor Independence)**: Ingestion passes must be verified by corpus-verify
using disjoint extractors.
4. **Red Auditor Stealth Invariant**: Excluded from all public manifests and trees, living strictly in
isolated ~/.red/. The only surface is red_verdict: pass|fail|n/a.
5. **Zero Audio Latency Overhead**: Voice streaming pipelines must route directly to local
model endpoints or OmniRoute without blocking main UI loops.

### Architecture References
- **Universal file configuration**:
https://docs.google.com/document/d/1oWzHeX_MIIjyVb0RUBZphdPCoc4Nw0z8ccK4cXgJhlE/e
dit
- **PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md**:
https://drive.google.com/file/d/1S2cQzDPTknjzX9fR3q6lqsRLZxkcQAcA/view
