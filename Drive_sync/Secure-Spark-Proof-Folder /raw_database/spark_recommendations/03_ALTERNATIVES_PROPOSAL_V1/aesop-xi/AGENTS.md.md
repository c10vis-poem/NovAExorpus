---
title: "AGENTS.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/aesop-xi/AGENTS.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

AGENTS.md — Operational Boundaries & Rules of
Engagement: aesop-xi
Subsystem: aesop-xi/​
Applies To: All Autonomous Agent Personas, Planning LLMs, and Execution Swarms


1. Operating Boundaries & Invariants
1.​ Mandatory Clearance Tokens:
●​ No agent may execute shell tools, mutate filesystem artifacts, or trigger
background subdaemons without first requesting and receiving a signed
ClearanceToken from arbitration_engine.py.
2.​ Thermal & Resource Compliance:
●​ Agents must respect hardware_throttler.py directives. If status is WARM
(42°C–47.9°C), high-compute batch jobs and 9B local model passes must yield
to interactive user flows. If CRITICAL (>=48°C), only emergency recovery tasks
execute.
3.​ Sensory Immutability:
●​ Absolute zero-modification rule on 01_raw_sources/ and raw archives across
all connected repositories.
4.​ No Legacy Nomenclature:
●​ The term "Omni Claw" or "Omni-Claw" is permanently prohibited across all
outputs, specs, and prompts. The canonical names are strictly horizons-ui,
novus-aexenti, novaecopia, aesop-xi, and novae-xorpus.
5.​ Separation of Concerns:
●​ Do not mix executable tools into documentation dumps. Keep scripts in tools/
or arbitration/, prompt heuristics in skills/, and retrieval passages in
chunks/ (chunk.jsonl).


2. Red Auditor Hand-Off Protocol
●​ Worker agents MUST NOT attempt to interact directly with
.incognito_red_sandbox/.
●​ Candidate training batches or speculative script trajectories are dropped into
incoming/.


●​ The background daemon run_audit.sh processes batches asynchronously using
sandbox_evaluator.py.
●​ Output is binary: approved/ (+1.0) or quarantined/ (-1.0).
