---
source: ob1_vs_mem0_memory_division.md.pdf
type: pdf
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

OB1 vs. mem0 Memory Layer Division & OmniRoute
Coordination

Mined from: PLUGINS TOOLS AND MEMORY LAYER ARGUMENTS (Files 7, 8, 9, 11)

Executive Resolution: The Dual Memory Engine

Historically debated as competing systems, OB1 (Open Brain Protocol) and mem0 serve two
fundamentally different, complementary tiers in #d.u.m.b.a.s.s.:


Dimension
OB1 (Open Brain Protocol)
mem0

Primary Nature
Structural & Governed
Access Protocol

Episodic & Adaptive
Personalization

Storage Engine
PostgreSQL + pgvector on
Node Beta

SQLite + in-memory vector
cache on Node Alpha

Core Responsibility
Governs how memory is
captured, classified, and
doled out. Enforces time-slice
proofs, session forks, and
ground-truth specs.

Tracks what the user said 2
minutes ago, active session
preferences, and syntax
habits.

Access Interface
Model Context Protocol
(MCP) Server
(knowledge.retrieve,
knowledge.record)

Local SDK / tool invocation
hooks directly in prompt loops

OmniRoute: The Unifying Gateway

OmniRoute sits on http://localhost:20128/v1 in front of both backends:


1.​ Dynamic Dispatch: Agents do not manually choose between OB1 and mem0.
OmniRoute inspects query intent and routes to the appropriate memory provider.
2.​ Local Fallback: OmniRoute's embedded SQLite FTS5 index and typed-decay vector
cache act as a zero-latency fallback when offline.
3.​ Asynchronous Memory Tap: Every completion passing through OmniRoute is tapped
to update mem0 habits and send failure traces to the Reasoning Bank.
