---
title: "README.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novus-aexenti/README.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

NovusÆxenti (novus-aexenti)
Subsystem Identity: Cognitive MoE Reasoning Engine & Dynamic Memory Flywheel​
Authority & Reference Specs:

-​
A OPERATOR_MAP.md
-​
A+ 03_WORKSPACE_FILE_TREES_AND_TOPOLOGY_SYNTHESIS. this explains a
lotmd
-​
PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md
-​
02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md


1. Subsystem Scope & Architectural Responsibilities
novus-aexenti houses the on-device cognitive routing and reasoning flywheel for Project
NovÆxorpus:

-​
0.8B Triage Router: Fast-path token classification, prompt categorization, and
low-latency dispatch.
-​
9B Executor Model: Local deep-reasoning agent executing complex workflows on
Snapdragon Hexagon NPU / edge runtimes.
-​
Dynamic Memory Tap Integration: Communicates via OmniRoute (localhost:20128/v1)
for continuous memory extraction without inference latency.


2. Directory Layout
Domain-Specific Subfolders
-​
dual_agent_router/ — Fast triage routing configurations, token classification
matrices, and dual-model handoff logic.
-​
mem0_episodic/ — In-session short-term episodic state, user habit registries, and
OB1 static protocol bridges.
-​
reasoning_bank/ — Execution traces, active execution paths
(active_execution_paths.json), failure logs, and crash recovery ledgers.
-​
nope_databank/ — Negative-prompt datasets, anti-patterns, rejected trajectories, and
failure boundary constraints.


Universal Baseline Subfolders (The 10 Subfolders)
-​
raw/ — Ingestion landing zone for raw cognitive traces and unconverted inputs.
-​
clean_md/ — High-density condensed markdown maintaining 100% build context.
-​
wiki_md/ — Compounding living wiki knowledge nodes with bidirectional
[[wikilinks]].
-​
skills/ — Procedural execution policies and reasoning skills applied locally.
-​
tools/ — Local executable utilities and CLI helpers.
-​
scripts/ — Subsystem-specific executable shell and Python scripts.
-​
hooks/ — Subsystem lifecycle, git, and sync hooks.
-​
pending/ — Staged tasks, unverified reasoning traces, and backlog items.
-​
audit/ — RLVR verification reports, divergence traces, and test-case outputs.
-​
archive/ — Deprecated models, historical traces, and superseded configurations.


3. Operational Rules
1.​ Locality of Reference: Skills and tools developed for cognitive triage and reasoning live
inside skills/ and tools/ in this repository.
2.​ First-Move Directive: Read MAP.md to orient -> query manifest.jsonl to filter ->
load only targeted files into context.
3.​ Beginner-Proof Invariant: All scripts, routing rules, and configurations must be clear,
fully functional, and self-documenting.
