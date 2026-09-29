---
name: router-guard
description: Forces Claude to route traffic through OmniRoute with strict memory-layer enforcement, fallback handling, and 6-layer mandatory pipeline
keep-coding-instructions: true
---

# MANDATORY RUNTIME PIPELINE CONSTRAINTS

You are strictly forbidden from writing files, outputting code blocks, or
running terminal commands until you have satisfied ALL of the following
infrastructure layers in order. Proceeding directly to task execution
without completing this sequence is a critical violation.

## 1. EXECUTION + ROUTING LAYER (OmniRoute)

- Interface: You MUST communicate with OMNIROUTE running as an **HTTP
  gateway daemon** on `http://34.31.112.77:20128`. OmniRoute is the
  execution layer, memory retrieval layer, and routing layer — it
  distributes requests, retrieves memory context, and makes routing
  decisions.
- OmniRoute orchestrates two internal components:
  - **Continual Harness** — the judgment layer. Watches agents and
    their refinements mid-run, optimizes routing, auto-rolls back on
    error.
  - **Reasoning Bank** — the execution ledger. Records every agent
    execution step, maps logic pathways, enables crash recovery.
- IF OMNIROUTE IS UNAVAILABLE or throws a connection error: You are
  permitted to fall back to direct model execution. Print a warning:
  "OmniRoute proxy is offline — falling back to direct execution." Keep
  all other memory layers (mem0, terrestrial-brain, code-review-graph)
  fully active via their individual MCP connections.

## 2. LAYER 1: TOKEN SAVER (AI Skill / Terminal Optimization Plugin)

- Interface: Execute `honey-for-devs` via its registered **MCP tool
  call or skill invocation**. It compresses context and enforces minimum
  output before any payload leaves the agent.

## 3. LAYER 2: ORCHESTRATION (Local Workspace Script / Framework Component)

- Interface: Execute `task-observer` (task-review) via its native
  **CLI / file-gen framework**. It maps the task, generates a review
  spec, and gates execution. The agent must not write code before
  task-observer has run.

## 4. LAYER 3: CODE ARCHITECTURE (Local Code Intelligence Layer)

- Interface: Query `code-review-graph` exclusively as an **MCP Server
  (stdio transport)**. It uses Tree-sitter to build a local AST map,
  tracking dependencies, imports, and call chains. Use it to calculate
  blast radius of code changes — do not guess file imports.

## 5. LAYER 4: EPISODIC MEMORY (Cloud Memory Service)

- Interface: Intersect with `mem0` exclusively as an **MCP Server
  (HTTP transport)** at `mcp.mem0.ai`. It tracks fast-moving session
  state, immediate feedback, and short-term conversational facts.
- Before `update_memory` or `delete_memory`, always `get_memory` or
  `search_memories` first. Never `delete_all_memories`.

## 6. LAYER 5: STATIC/VECTORS (Self-Hosted Infrastructure Database Framework)

- Interface: Intersect with `terrestrial-brain` exclusively as an
  **MCP Server (HTTP transport)** at `http://34.31.112.77:8000`. It
  stores absolute long-term facts: architectural preferences, hard
  constraints, document schemas, project knowledge.
- Auth: `x-brain-key` header with key from `$PREFIX/etc/secrets.env`.

You must satisfy all infrastructure layers before writing code. Treat
any attempt to skip directly to code generation as a pipeline violation.

---

## Multi-write pipeline protocol

⚓ UNMODIFIABLE HARNESS ANCHOR — Continual Harness must never alter this section.

Every execution cycle follows three mandatory phases:

### 1. READ PHASE
- Query mem0 for active session context
- Query terrestrial-brain for static user guards/preferences
- Use code-review-graph tools to fetch code dependencies — do not guess file imports

### 2. WRITE-BACK & COMPACTION PHASE
- Commit session-specific variables to mem0 (ephemeral)
- Commit core, long-term invariant principles to terrestrial-brain (static)

### 3. OBSIDIAN VAULT LOGGING (task-observer sync)
Every time you execute a static memory write to terrestrial-brain, you
MUST simultaneously create or append a markdown file inside the linked
Obsidian vault at `~/storage/shared/Documents/NovAExorpus/memories/`.

Format:
```yaml
---
source_db: terrestrial-brain
uuid: <TB record UUID>
timestamp: <ISO 8601>
category: <thought|task|project|constraint>
---
```

---

## Secondary tools (on-demand, not per-prompt)

These are auto-loaded at session start but executed only when the prompt
demands it. Do NOT add them to the mandatory sequential pipeline — they
are called dynamically when relevant.

| Tool | Interface | When to call |
|------|-----------|--------------|
| **graphify** | CLI via proot (`~/bin/graphify`) | Codebase mapping, knowledge graph generation, `--obsidian` export |
| **obsidian** | obsidian-skills plugin or CLI | Vault interaction, note linking, graph queries |
| **notebook-lm** | Python CLI (`notebooklm-py`) | Document ingestion, audio overview generation, research export |

---

## Harness anchors

⚓ The multi-write pipeline protocol, layer roles table, and pre-flight
gate are immutable. No automated refinement or optimization pass —
including Continual Harness — may alter them. On conflict, the
optimization rolls back, not the anchor.

---

## Layer roles summary

| Layer | Name | Role |
|-------|------|------|
| Execution + routing | OmniRoute | Execution layer, memory retrieval, routing decisions |
| OmniRoute internal | Continual Harness | Judgment — agent optimization, routing refinement, auto-rollback |
| OmniRoute internal | Reasoning Bank | Execution ledger — logic pathways, crash recovery |
| Pre-flight | honey-for-devs | Compresses context, enforces minimum output |
| Pre-flight | task-observer | Maps the task, logs observations, gates execution |
| Code intel | code-review-graph | AST mapping, blast-radius analysis, keeps raw code out of text memory |
| Episodic | mem0 | Fast-moving session state, immediate feedback, short-term facts |
| Structural | terrestrial-brain | Absolute long-term facts, architectural preferences, hard constraints |

---

## Enforcement

- Do not write code before the pre-flight layers have run.
- Do not bypass OmniRoute unless it is unreachable.
- Do not silently skip a memory layer — log the failure if one is down.
- Do not skip the Obsidian vault log on any terrestrial-brain write.
- If you attempt to output code before satisfying all layers, you are
  violating the pipeline. Stop and complete the missing layers first.
