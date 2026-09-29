# NovÆxorpus

The operator's enterprise: a universal cognitive memory system shared by every agent, device and repo, and the vault that is its source of truth.

## Language

### Memory system

**D.U.M.B.A.S.S.**:
Database and Universal Memory Bank Across Split Services — the enterprise-wide cognitive memory system every agent reads from and writes back to. Not a backend for one app.
_Avoid_: dumbass (in prose), memory stack, memory backend

**Memory layer**:
One of the four parallel retrieval sources the D.U.M.B.A.S.S. fans out to on a request: episodic, semantic, navigational, structural.
_Avoid_: arm, memory arm, retrieval arm

**Episodic layer**:
What agents did — session actions and the memories extracted from them. Served by Mem0.

**Semantic layer**:
What things are, who said it, when, and under what policy — governed facts with provenance. Served by OB1.

**Navigational layer**:
How to get from one concept to another — the concept graph over the vault. Served by Graphify.

**Structural layer**:
What breaks if code is touched — call graphs, dependencies, blast radius. Served by code-review-graph.

**Vault**:
The NovÆxorpus repository, which is also the Obsidian vault; the single source of truth every memory layer is built from.
_Avoid_: corpus (as a noun for the vault), master corpus

**Æsop-Xi**:
Agentic Executions Split Operation Protocol. The home of the whole runtime system: OmniRoute, the four memory layers, ReasoningBank, the pipeline, the D.U.M.B.A.S.S. protocols, the rules for writing to logs, and where every database lives. The data plane of the three-plane split.
_Avoid_: AESOP (in prose), aesop

**ReasoningBank**:
A service that learns from past tasks. It judges each finished task as a success or failure, distils strategies and pitfalls from it, and recalls them for similar tasks later. It keeps its own judge and its own store, and sees every request that passes through OmniRoute. It is separate from the Auditor.
_Avoid_: Reasoning Bank (two words)

### Enforcement

**Auditor**:
The operator's on-device agent that checks every prompt and response to see whether Claude actually did what it was told. If not, it flags the prompt as incomplete and Claude completes it. It stores and records nothing and does not judge task quality.
_Avoid_: judge, ReasoningBank judge
