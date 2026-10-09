---
title: "ecc-agent-harness.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/prompt_skills/ecc-agent-harness.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

name: ecc-agent-harness description: Everything Claude Code
(ECC) multi-agent harness protocol for managing instincts,
memory access, and cross-CLI execution consistency.
Everything Claude Code (ECC) Agent Harness
Protocol
Mined from: PLUGINS TOOLS AND MEMORY LAYER ARGUMENTS (File 6)
Purpose & Scope
The ECC Harness governs how Claude Code CLI, Codex, and local execution agents maintain
shared operational memory, behavioral instincts, and security constraints.
Invariants & Rules
1.​ Universal Memory Reach: Agents executing through ECC must query the local
#d.u.m.b.a.s.s. SQLite/OmniRoute interface before proposing file changes.
2.​ Context Window Protection: Never inject full source files if AST structural maps (e.g.
via graphify) are available.
3.​ Session Closure: Every execution session must terminate with a clean state summary
written to RESUME.md and an inventory update in manifest.jsonl.
