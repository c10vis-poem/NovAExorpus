---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

AGENTS.md — Agent Execution Guidelines &
Operating Invariants
Scope & Target Audience
This document governs all autonomous AI agents (Claude Code CLI via ECC, Prime Agent
RLM loops, and background maintenance daemons) executing tools or applying skills within
skills-and-capabilities/.


Core Operating Invariants
1.​ Deterministic Exit Codes: Every Python script in this repository must return exit code 0
on success and non-zero (1 or 2) on failure. Agents must verify $? == 0 before
proceeding to downstream steps.
2.​ Read-Only Inspection: Ingestion and parsing tools (graph_builder.py,
markor_sweeper.py, graph_sync.py) must operate in read-only mode across
target directories. Never mutate source code during an analysis pass.
3.​ Bounded Context Windows: When reporting results to human operators, never dump
full raw JSON dependency trees or huge bundles. Always use --format md or pipe
through markdown summary formatters to conserve context tokens.
4.​ No Unaudited Dependencies: All Python utilities in this repository rely strictly on
Python 3 standard libraries (ast, re, json, hashlib, pathlib, argparse). Do not
introduce external pip dependencies (networkx, pandas, requests) unless explicitly
authorized in UNRESOLVED.md.


Skill Application Protocol (The Matt Pocock Sequence)
When executing feature buildouts or complex refactors, agents must chain the prompt skills in
this strict sequence:

[grill-me] ────► [spec] ────► [ticket] ────► [tdd] ────► [code-review]

1.​ grill-me: Interrogate ambiguous user prompts; extract missing constraints.
2.​ spec: Generate formal architectural specifications with W5+H identity and invariants.
3.​ ticket: Deconstruct specifications into atomic work units (< 150 LOC, < 3 files).
4.​ tdd: Author failing unit tests before touching implementation code.


5.​ code-review: Run graph_builder.py and verify AST stability before committing
changes.
