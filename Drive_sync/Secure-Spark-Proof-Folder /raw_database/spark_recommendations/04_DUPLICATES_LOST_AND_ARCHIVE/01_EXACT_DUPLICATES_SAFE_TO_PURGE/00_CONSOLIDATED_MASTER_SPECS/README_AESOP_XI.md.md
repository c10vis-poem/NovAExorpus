---
title: "README_AESOP_XI.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/04_DUPLICATES_LOST_AND_ARCHIVE/01_EXACT_DUPLICATES_SAFE_TO_PURGE/00_CONSOLIDATED_MASTER_SPECS/README_AESOP_XI.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

README — aesop-xi/
Universal Orchestration Layer & Ethical Safety Protocols
W5+H Subsystem Identity
●​ WHO: Governed by the Chief Ethical Orchestration Agent; enforces boundaries across
all worker swarms.
●​ WHAT: Policies, permission boundaries, resource arbitration engines, and the sealed
Red Auditor sandbox.
●​ WHEN: Invoked prior to every mutating tool execution, repo update, or hardware
allocation request.
●​ WHERE: novae-xorpus/aesop-xi/ (Federated Subsystem Root).
●​ WHY: Prevents runaway recursive model loops, unauthorized filesystem mutations,
context poisoning, and hardware thermal throttling.
●​ HOW: Evaluates JSON/YAML guardrails, checks FastRPC/NPU hardware headroom,
and enforces the .incognito_red_sandbox/ gate.


Internal Directory Topology
aesop-xi/

├── README.md                                # This document (Subsystem architecture & rules)

├── manifest.jsonl                           # Local cryptographic catalog of policies & engines

│

├── arbitration/                             # Resource & priority steering

│   ├── arbitration_engine.py                # Inter-agent priority arbitrator

│   └── hardware_throttler.py                # Monitors Hexagon NPU thermal & RAM thresholds

│

├── policies/                                # Hard operational boundaries & constraints

│   ├── tool_usage_guardrails.json           # Explicit limits on code modification tools



│   ├── security_clearance.yaml              # Multi-tenant and agent access boundaries

│   └── zero_trust_rules.md                  # Strict sensory immutability directives

│

└── .incognito_red_sandbox/                  # [SHADOW ISOLATION] Sealed Red Gatekeeper

    ├── manifest.jsonl                       # Isolated quarantine index

    ├── sandbox_evaluator.py                 # Adversarial compliance & hallucination checker

    └── quarantine_logs/                     # Rejected run traces (-1.0)


Beginner-Proof Implementation Rules
1.​ Zero Direct Execution: No worker agent may execute shell or file-writing tools without
arbitration_engine.py approving the clearance token.
2.​ Shadow Validation: The .incognito_red_sandbox/ is completely unlisted in public
manifests; all worker agents hand off solely to the official Enterprise Cross-Auditor.
