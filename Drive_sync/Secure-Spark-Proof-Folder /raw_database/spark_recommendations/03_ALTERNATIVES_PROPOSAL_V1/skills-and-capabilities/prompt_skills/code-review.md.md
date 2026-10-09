---
title: "code-review.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/prompt_skills/code-review.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

name: code-review description: Strict AST-based code review and
verification skill. Evaluates code diffs, structural topology, security
guardrails, and compliance against architectural specs.
Code Review — Structural AST & Security
Verification Skill
Purpose & Protocol
The Code Review skill acts as an adversarial verification gatekeeper. It audits code submitted
by developer agents or automated pipelines before merging, evaluating compliance against
invariants, style canons, and AST topology.


Review Protocol & Gatekeeper Sequence
1. Invariant Compliance Check
-​
Does the change violate any hard invariants from AGENTS.md or parent specifications?
-​
Are raw files, cold archives, or external reference docs modified without authorization?
-​
Does the code attempt to self-certify without an independent verifier test?
2. AST Topology & Dependency Review
-​
Run graph_builder.py on the modified files.
-​
Inspect incoming and outgoing dependencies ($F_{in}$, $F_{out}$).
-​
Ensure no circular imports were added.
-​
Verify that internal methods remain encapsulated and public interfaces match
documented contracts.
3. Security & Context Hygiene Check
-​
Scan for hardcoded credentials, API keys, or private auth tokens
(markor_sweeper.py).
-​
Validate that all network calls, subprocess executions, and file I/O operations are strictly
parameterized with bounded timeouts.
-​
Confirm input validation handles unexpected types without throwing uncaught
exceptions.


4. Deterministic Verdict Generation
The review must conclude with one of two formal verdicts:

[VERDICT: PASS]

- Summary of verified changes.

- AST stability confirmed (I = <score>).

- All unit tests verified passing.

OR

[VERDICT: REJECT]

- Explicit list of failed assertions or invariant violations.

- Precise line numbers and remediation instructions.

- File quarantined until issues are resolved.
