---
tags: []
created: '2026-09-10'
title: '2026-09-10_wiki.RAG.imdex.prot-'
---



----
///////////////   wiki_rag_indexing_protocol=


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