---
title: "zero_trust_rules.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/aesop-xi/policies/zero_trust_rules.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Zero-Trust Operating Rules & Sensory Immutability
Canon
Subsystem: aesop-xi/policies/​
Governing Authority: Chief Ethical Orchestration Protocol (Æsop-Xi)​
Target Audience: All Autonomous Edge Agents, Verification Daemons, and Planning Nodes


1. Principle of Sensory Immutability (Tier 1 Canon)
1.​ Absolute Write Prohibition: Raw intake folders (01_raw_sources/, raw/, and
incoming sensory assets) are immutable cold archives. Under no circumstances may
any agent write, delete, move, or modify any file within these paths.
2.​ Read-Only Derived Workflows: All processing of raw sources must operate by reading
the source and emitting new derivative files into clean_md/, chunks/, or wiki_md/.
3.​ Cryptographic Ground Truth: Every file ingested into raw/ receives an immediate
SHA-256 hash stamped in manifest.jsonl. If a file's hash changes in place, the
integrity monitor halts processing immediately.


2. Sandboxed Verification ("Nothing Self-Certifies")
1.​ Independent Verification: No script, cleaner, or transformation pipeline may certify its
own output.
2.​ Separation of Extraction and Audit: The agent that extracts text or generates
candidate scripts is strictly barred from issuing the approval signature.
3.​ Fail-Closed Default: If an audit script, verifier, or syntax checker crashes or encounters
an unknown condition, the candidate batch is marked FAIL and quarantined.


3. The Incognito Red Gatekeeper Isolation Contract
1.​ Sealed Sandbox: The Red Auditor lives inside .incognito_red_sandbox/ (or
/opt/red-agent/). It runs headlessly and asynchronously.
2.​ Zero Discovery Invariant: The Red Auditor must not be registered in public user-facing
manifests or exposed in general agent system prompts.


3.​ Narrow Contract: Worker agents drop candidate batches into incoming/. The Red
Daemon evaluates the batch against strict guardrails and moves it to either approved/
(+1.0) or quarantined/ (-1.0).
4.​ No Direct Inter-Agent Negotiation: The Red Auditor does not debate, chat, or
negotiate. It outputs a deterministic verdict and error trace.


4. Execution Clearance & Tool Gating
1.​ Pre-Flight Clearance: Before invoking any shell command, executing Python scripts, or
writing files, the worker agent must obtain a signed ClearanceToken from
arbitration_engine.py.
2.​ Thermal & RAM Headroom Check: If hardware_throttler.py detects thermal
state CRITICAL (>48°C) or RAM <1024MB, background tasks must yield immediately to
preserve system responsiveness and prevent Android LMK eviction.
3.​ Audit Ledger Logging: Every granted clearance, task rejection, and thermal throttling
event must be written to the local audit ledger.
