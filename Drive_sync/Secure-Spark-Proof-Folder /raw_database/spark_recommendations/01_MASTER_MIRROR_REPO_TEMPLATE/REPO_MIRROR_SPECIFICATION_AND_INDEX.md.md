---
title: "REPO_MIRROR_SPECIFICATION_AND_INDEX.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/01_MASTER_MIRROR_REPO_TEMPLATE/REPO_MIRROR_SPECIFICATION_AND_INDEX.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# NovÆxorpus Universal Repository Mirror & Subagent Ingestion Spec

**Scope**: Standardized repository layout, mirror skeleton, and worker agent ingestion contracts
across the federated ecosystem.
**Direct Download Archive**:
[NovAeXorpus_Repo_Mirror_Template.zip](https://drive.google.com/file/d/1l_9J9nMBstLyMOFe
BoqPFQDMiZ9zxTK1/view?usp=drivesdk)

---

## 1. Federated Repositories Mirrored

1. **`aesop-xi`**: Universal orchestration, arbitration, and behavioral policy governance.
2. **`novus-aexenti`**: Cognitive MoE reasoning engine (0.8B Triage vs. 9B Executor),
in-session mem0 episodic memory, and Reasoning Bank flywheel.
3. **`novaexopia`**: Native 3-APK framework (Horizons UI, Æsc terminal daemon, Æyre media
daemon), MCP connectors, and execution harnesses.
4. **`data_vault`**: Living LLM Wiki (Karpathy standard), raw data landing buckets,
pre-tokenized RAG shards, and episodic audit telemetry.
5. **`vendor-corpora`**: Qualcomm QAIRT, Snapdragon 8 Elite Hexagon v79 HTP FastRPC
specs, and Android NDK bindings.
6. **`tools`**: Cross-subsystem production utilities and boundary sweepers.

---

## 2. Universal Subsystem Directory Layout (Inside Every Repo)

Each repository follows this exact structure:

```
<repo_name>/
├── MAP.md                # Human-readable navigation map & component ontology
├── manifest.jsonl        # Local cryptographic file index & RAG catalog
├── README.md             # Subsystem setup, scope, and operational identity
├── AGENTS.md             # Operational boundaries, agent contracts, and invariants
├── RESUME.md             # Active state tracker & progress checkpoints
├── chunk.jsonl           # Pre-tokenized machine retrieval & RAG passage layer
│
├── raw/                  # Incoming source landing zone (Interceptor extracts here)
├── clean_md/             # High-density condensed markdown (build context preserved)
├── wiki_md/              # Compounding living LLM wiki nodes with wikilinks
├── skills/               # Local procedural skills developed and applied here
├── tools/                # Local executable Python/bash tools and wrappers


├── pending/              # Staged tickets, backlog tasks, and unverified outputs
└── audit/                # Structured logs, failure traces, and divergence reports
```

*Crucial Invariant: The Red Auditor agent is completely absent from all public trees and lives
strictly in a sealed, private sandbox.*

---

## 3. Worker Agent / Subagent Ingestion Contract

When a subagent or worker agent is assigned to populate a repository from the raw corpus:

1. **Input**: Raw documents land in `raw/`.
2. **Dual Extraction**: The agent scans for:
   - Procedural heuristics, workflows, and prompts ➔ Saved as `.md` inside `skills/`.
   - Executable scripts, CLI flags, and code blocks ➔ Saved as standalone `.py` / `.sh` inside
`tools/`.
3. **Condensation**: The source is rewritten into `clean_md/`:
   - **No 1:1 file parity rule.** Fat, boilerplate, and conversation filler are stripped.
   - 100% of technical instructions, parameters, and architecture context must survive intact.
4. **RAG Indexing**: Key passages are pre-tokenized into `chunk.jsonl`.
5. **Living Wiki**: Semantic concept nodes are linked into `wiki_md/` with bidirectional
`[[wikilinks]]`.
6. **Manifest Registration**: `manifest.jsonl` is updated with SHA256 hashes for every added
asset.
