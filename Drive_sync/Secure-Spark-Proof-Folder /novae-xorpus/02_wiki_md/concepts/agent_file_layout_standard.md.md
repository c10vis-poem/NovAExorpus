---
title: "agent_file_layout_standard.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novae-xorpus/02_wiki_md/concepts/agent_file_layout_standard.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Agent File Layout & Repository Scaffolding Standard
1. Document Format Taxonomy
Agents operate with strict performance bounds across specific file formats:

-​
Markdown (.md): Primary medium for human-readable semantic notes, system
prompts, specifications, and living wikis.
-​
JSON Lines (.jsonl): Purpose-built for streaming records, pre-tokenized chunks,
training trajectories, and fast line-by-line machine retrieval.
-​
PDF (.pdf): Immutable cold-storage backups, research papers, and static vendor
manuals.
-​
Skill Definitions (SKILL.md): Procedural instruction files containing YAML frontmatter
and strict agent execution directives.
2. Universal Repository Triad
Every repository root maintains three core baseline files:

1.​ README.md — Human identity, setup instructions, and W5+H scope.
2.​ manifest.jsonl — Machine-readable inventory of all files, hashes, and retrieval tags.
3.​ MAP.md (or llm_wiki.md) — Visual navigation map and conceptual ontology.
3. High-Speed Local Search Architecture
To enable low-latency grep and AST scanning without network bottlenecks:

-​
Workspaces are mirrored or cloned to local storage.
-​
Agents execute localized grep -rn "term" ./ and AST mappers over .md and
.jsonl files directly.
