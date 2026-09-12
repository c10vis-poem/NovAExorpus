---
source: continual_harness_policy.md.pdf
type: pdf
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

Continual Harness Policy: Reset-Free Online
Adaptation

1. Architectural Mandate

The Continual Harness implements reset-free online adaptation for autonomous foundation
agents operating within #d.u.m.b.a.s.s. It enables agents to improve from real-world execution
feedback (such as syntax mistakes, model timeouts, and operator corrections) without suffering
catastrophic forgetting or destabilizing production prompt stacks.




2. Core Operational Rules

Rule 1: Immutable Base Anchor

-​
Base system prompts (system.md) and core behavioral invariants are strictly read-only
during runtime.
-​
Agents are forbidden from directly modifying their base prompt files.

Rule 2: Layered Prompt Refinement (/refine)

-​
Online adaptations are expressed strictly as delta layers appended to the agent's
contextual skills:

[Immutable Base Prompt] + [Domain Rules] + [Layered Refinement Delta]

-​
Deltas are versioned with semantic commit tags (refine_v1.0.1, refine_v1.0.2).

Rule 3: Automated Snapshot Rollbacks

-​
Before any delta layer is activated, the harness takes a cryptographic snapshot of the
current state (snapshot_hash).
-​
The agent must pass a standardized regression test suite (Car Wash test harness)
before the delta is marked permanent.
-​
If regression is detected (regression score drop > 2%), the harness automatically
executes an instant rollback to the previous snapshot without requiring operator
intervention.





3. Feedback Loop & Verification

1.​ Trigger: An error occurs during tool execution or the operator provides an inline
correction.
2.​ Analysis: The triage auditor identifies the root cause and drafts a candidate refinement
rule.
3.​ Verification: The candidate rule is tested against historical test cases in the Reasoning
Bank.
4.​ Adoption: Upon passing verification (+1.0), the refinement rule is written to the agent's
local skills/ directory and synced to #d.u.m.b.a.s.s..
