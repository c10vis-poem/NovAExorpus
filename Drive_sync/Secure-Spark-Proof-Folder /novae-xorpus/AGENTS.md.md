---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novae-xorpus/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

AGENTS.md — Operational Contracts & Hard
Invariants (novae-xorpus)
Scope: Binding constraints and execution laws for all agents and subagents operating within
novae-xorpus.


1. Canonical Invariants
●​ Hard Rule 1 (Ask The Builder): No destructive actions, bulk deletions, or irreversible
file overwrites without explicit permissions.
●​ Hard Rule 2 (No Synthesized Authority): Agent-generated rules must not override
authoritative Builder specifications.
●​ Hard Rule 5 (Extractor Independence): Ingestion passes must be validated via
corpus-verify (tools/check.py) using disjoint extractors before cataloging.
●​ Non-1:1 Condensation Law: Strip conversational fat, greetings, and boilerplate, but
maintain 100% build fidelity so raw and clean markdown build the exact same output.
●​ Red Auditor Stealth Invariant: The Red Auditor operates strictly in ~/.red/ outside
the visible tree. The visible tree only exposes red_verdict: pass|fail|n/a on
execution records.
●​ Locality of Reference: Procedural heuristics live in skills/ and scripts in tools/
co-located directly where they execute.


2. Navigation Protocol (First-Move Directive)
Every agent operating in the vault MUST follow: MAP.md (Orient) ➔ Tier MAP.md (Focus) ➔
manifest.jsonl (Stream/Filter) ➔ Targeted File Read.


3. Authority Pointers
●​ Architecture Authority: 1 main dumbass map
●​ Invariant Grounding:
PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md
