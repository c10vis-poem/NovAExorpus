---
tags: []
created: '2026-09-10'
title: '2026-09-10_tier-1-3-and-RAG-protocol'
---



----
3. Tier Operational Specifications
Root: Metacognitive Index (MAP.md & manifest.jsonl)
* MAP.md: Must maintain top-level navigation links using Markdown cross-references to key notes in 02_wiki_md/ and entry points in 04_skills_runtime/.
* manifest.jsonl (Root): Master catalog mapping file paths, tiers, cryptographic checksums, and cross-tier linkages:
{"id": "SRC-0042", "path": "01_raw_sources/pdf/spec_v1.pdf", "tier": 1, "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", "last_modified": "2026-09-03T17:00:00Z", "linked_wiki": "02_wiki_md/architectures/spec_v1.md"}

Tier 1: 01_raw_sources/ (Cold Archive & Sensory Buffer)
   * Write Policy: Write-once upon raw intake. Never mutate or reformat existing files.
   * Naming Convention: YYYYMMDD_source_title.[ext] (lowercase, snake_case).
   * Scope: Source PDFs, audio transcripts, sensor captures, video recordings, raw scrapes.
Tier 2: 02_wiki_md/ (The LLM Wiki Layer)
   * Write Policy: Managed via OpenWiki TUI by the Files Executive Agent.
   * Format: Pure Markdown with strict YAML frontmatter:
---
id: wiki_rag_indexing_protocol
tier: 2
type: architecture
created: 2026-09-03
updated: 2026-09-03
author: files_executive_agent
sources:
 - "01_raw_sources/pdf/rag_system_spec.pdf"
extracted_skills:
 - "04_skills_runtime/prompt_skills/manifest_sync.md"
extracted_tools:
 - "04_skills_runtime/extracted_tools/cli/build_manifest.py"
tags:
 - llm_wiki
 - openwiki
 - indexing
---

# RAG Indexing Protocol

## Context & Definition
Structural mechanism for keeping the LLM Wiki synchronized with high-speed caches...

## Architectural Interfaces
The [[manifest_registry_spec]] defines how this node is indexed by the [[files_executive_agent]].

## References
- [[hierarchical_manifest_routing]]
- [[procedural_tool_extraction]]

Tier 3: 03_recall_cache/ (Working Memory Accelerator)
      * Write Policy: Agent-generated during build or indexing steps. May be deleted and rebuilt safely.
      * Chunk Schema (03_recall_cache/jsonl/*.jsonl):
{"chunk_id": "CHK-8901", "parent_doc": "02_wiki_md/concepts/rlvr.md", "tokens": 256, "content": "RLVR verifiers score execution traces against deterministic unit tests...", "metadata": {"tier": 2, "topic": "rlvr"}}