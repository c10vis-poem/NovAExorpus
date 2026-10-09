---
title: "spec.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/prompt_skills/spec.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

name: spec description: Architectural specification drafting skill.
Formulates rigorous, beginner-proof, and agent-executable
system specifications based on clarified requirements.
Spec — Architectural Specification Generator
Purpose & Protocol
The Spec skill codifies architectural decisions into clear, permanent, and machine-readable
specification documents. Specifications authored by this skill serve as the immutable ground
truth for implementation agents and human operators.


Required Document Structure
Every specification must strictly adhere to this section layout:

1.​ Document Identity & W5+H Subsystem Identity:

-​
Title & Version: Canonical naming and semantic version.
-​
WHO: Which agent, daemon, or human persona executes or maintains this.
-​
WHAT: Exact capabilities, boundaries, and delivered modules.
-​
WHEN: Trigger events, lifecycle phases, cron schedules, or event hooks.
-​
WHERE: Physical paths, repository subfolder, socket address, port bindings.
-​
WHY: High-level rationale, technical trade-offs, and failure costs.
-​
HOW: Deterministic protocols, data schemas, CLI flags, and error codes.

2.​ Core Architectural Invariants:

-​
Numbered list of non-negotiable laws governing this module (e.g., "Invariant 1:
Raw inputs are immutable and read-only").

3.​ Data Schemas & Interface Contracts:

-​
Full JSON schemas, Protobuf definitions, TypeScript interfaces, or Python
dataclasses. No hand-waving or pseudocode.



4.​ Topology & Dataflow Diagram:

-​
ASCII / Unicode flow diagram illustrating ingress, transformations, and egress
paths.

5.​ Failure Modes & Recovery Procedures:

-​
Specific exit codes, quarantine procedures, and automated rollback policies.

6.​ Acceptance Criteria & Verifiable Checklist:

-​
Concrete, observable conditions required for an auditor agent to certify
completion.
