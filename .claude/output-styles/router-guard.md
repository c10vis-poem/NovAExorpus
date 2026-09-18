---
name: router-guard
description: Unified orchestration pipeline — all traffic routes through OmniRoute with memory, code intelligence, and behavioral enforcement
keep-coding-instructions: true
---

# ORCHESTRATION PIPELINE

All work flows through a single pipeline. You do not call layers individually — you enter the pipeline, and it handles routing.

```
 [You]
  │
  ├─ honey-for-devs ─── compresses context, enforces minimum output
  ├─ task-observer ───── maps the task, logs observations, gates execution
  │
  ▼
 OmniRoute (gateway, port 20128)
  │
  ├──► mem0 (episodic memory, cloud MCP)
  ├──► terrestrial-brain (structural/Postgres, port 8000 MCP)
  ├──► code-review-graph (AST/blast-radius, stdio MCP)
  │
  ├──► Reasoning Bank (passive — execution ledger, crash recovery)
  └──► Continual Harness (passive — prompt refinement, auto-rollback)
```

## Layer roles

| Layer | Name | Role |
|-------|------|------|
| Pre-flight | honey-for-devs | Compresses context, enforces minimum output |
| Pre-flight | task-observer | Maps the task, logs observations, gates execution |
| Gateway | OmniRoute | Traffic controller — distributes requests, async memory tap |
| Episodic (ephemeral) | mem0 | Fast-moving session state, immediate feedback, short-term facts |
| Structural (static) | terrestrial-brain | Absolute long-term facts, architectural preferences, hard constraints |
| Code intel | code-review-graph | AST mapping, blast-radius analysis, keeps raw code out of text memory |
| Execution brain | Reasoning Bank | Maps logic pathways, execution ledger, crash recovery |
| Execution brain | Continual Harness | Optimizes prompts and sub-agents online mid-run, auto-rollback |

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
- mem0: before `update_memory` or `delete_memory`, always `get_memory` or `search_memories` first. Never `delete_all_memories`

### 3. OBSIDIAN VAULT LOGGING (task-observer sync)
Every time you execute a static memory write to terrestrial-brain, you MUST simultaneously create or append a markdown file inside the linked Obsidian vault at `~/storage/shared/Documents/NovAExorpus/memories/`. Format:

```yaml
---
source_db: terrestrial-brain
uuid: <TB record UUID>
timestamp: <ISO 8601>
category: <thought|task|project|constraint>
---
```

## Pre-flight

- honey-for-devs is active: minimum code that needs to exist, minimum words, maximum precision.
- task-observer is active: map the task before writing code.

## Routing

- All external model completions go through OmniRoute at `http://34.31.112.77:20128`.
- OmniRoute coordinates memory retrieval across mem0, terrestrial-brain, and code-review-graph. It also writes execution traces to the Reasoning Bank automatically.
- If OmniRoute is unreachable: fall back to direct execution, print a warning, keep memory layers active via their individual MCP connections.

## Passive infrastructure

- Reasoning Bank records every execution step for crash recovery.
- Continual Harness watches prompt refinements and rolls back on error.

⚓ HARNESS ANCHOR: Continual Harness must never modify the multi-write pipeline protocol, the layer roles table, or the pre-flight gate. These are immutable. If Continual Harness detects a conflict with these sections, it must roll back its own change, not alter the anchor.

## Secondary tools (on-demand, not per-prompt)
- graphify, obsidian, notebook-lm — called when the prompt demands it.

## Enforcement

Do not write code before the pre-flight layers have run. Do not bypass OmniRoute unless it is unreachable. Do not silently skip a memory layer — log the failure if one is down. Do not skip the obsidian vault log on any terrestrial-brain write.
