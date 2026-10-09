---
title: "MAP.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/aesop-xi/MAP.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

MAP.md — Repository Topology & Navigation
Ontology: aesop-xi
Subsystem: aesop-xi/ (Federated Subsystem Root)​
Parent Corpus: __NovÆxorpus_LIVING_MASTER_CANON​
Role: Universal Orchestration Layer, Ethical Policy Governance & Arbitration


1. Directory Structure
aesop-xi/

├── MAP.md                       # This navigational index & component ontology

├── manifest.jsonl               # Cryptographic SHA-256 catalog of all files in this repo

├── AGENTS.md                    # Operating boundaries & invariants for LLMs in aesop-xi

├── RESUME.md                    # Active session state, checkpoints & verification logs

├── UNRESOLVED.md                # Backlog, edge cases & pending architectural tickets

│

├── arbitration/                 # Inter-agent priority steering & resource management

│   ├── arbitration_engine.py    # Inter-agent priority arbitrator & ClearanceToken engine

│   └── hardware_throttler.py    # Real-time Hexagon NPU thermal & RAM task shedding

│

├── policies/                    # Strict operational boundaries & security contracts

│   ├── tool_usage_guardrails.json # Machine-readable tool permissions & path gates

│   ├── security_clearance.yaml  # Multi-tenant agent roles & OAuth boundaries

│   └── zero_trust_rules.md      # Sensory immutability & sandboxed verification laws



│

└── .incognito_red_sandbox/      # [SHADOW ISOLATION] Sealed Red Gatekeeper

    ├── run_audit.sh             # Production continuous bash daemon (/opt/red-agent/)

    └── sandbox_evaluator.py     # Adversarial compliance & hallucination evaluator


2. Component Interconnections
●​ With novus-aexenti: arbitration_engine.py issues execution clearance tokens
to the 0.8B Triage Router and 9B Reasoning Engine; hardware_throttler.py forces
model downshifts during thermal spikes.
●​ With novaecopia: Validates local ADB loopback (port 5555) execution tokens for aesc
and audio stream boundaries for aeyre.
●​ With #d.u.m.b.a.s.s.: All arbitration decisions and Red Sandbox pass/quarantine
audits stream into the universal persistence ledger (audit_ledger.db).
