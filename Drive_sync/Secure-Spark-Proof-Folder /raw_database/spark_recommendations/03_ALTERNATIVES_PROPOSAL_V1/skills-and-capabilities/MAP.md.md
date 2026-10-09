---
title: "MAP.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/MAP.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

MAP.md — skills-and-capabilities Navigation &
Topology
Repository Identity & Purpose
skills-and-capabilities/ is the shared analytical, code review, vault hygiene, and
procedural skills repository. It centralizes reusable tools and workflows so individual agents
across other repositories do not rewrite common utilities.


Directory Topology
skills-and-capabilities/

├── MAP.md                                # This navigation index & ontology map

├── manifest.jsonl                        # Machine-readable registry of all modules, tools & skills

├── README_SKILLS_AND_CAPABILITIES.md     # Subsystem overview & W5+H identity

├── AGENTS.md                             # Operational boundaries & CLI guidelines for agents

├── RESUME.md                             # Active tool registry state & verification records

├── UNRESOLVED.md                         # Pending feature enhancements & open backlog
tickets

│

├── code-review-graph/                    # PyGraphify / AST Code Review Engine

│   ├── graph_builder.py                  # Python AST parser generating dependency graphs

│   └── visual_topology_map.md            # Structural guide for interpreting code graphs

│

├── notebook-lmpy/                        # Deep Corpus Analytical Query Engine



│   ├── query_notebook.py                 # Multi-document analytical querying script

│   └── source_packager.py                # Curated markdown source packager & bundler

│

├── obsidian-skills/                      # Vault Integration & Hygiene Engine

│   ├── graph_sync.py                     # Syncs markdown wikilinks & generates graph metadata

│   └── markor_sweeper.py                 # Scans for unregistered notes and context leaks

│

├── prompt_skills/                        # Matt Pocock Engineering Skills Suite

│   ├── grill-me.md                       # Aggressive question-based specification refining

│   ├── spec.md                           # Architectural specification drafting

│   ├── ticket.md                         # Atomic issue/task ticket creation

│   ├── tdd.md                            # Test-driven development implementation

│   └── code-review.md                    # Strict AST-based code review & verification

│

└── early-trend-scraper/                  # Autonomous Pre-Trend Research Daemon

    ├── daily_scraper.py                  # Scheduled web scraper monitoring repos

    ├── stack_analyzer.py                 # Divergence analyzer between web and vault

    └── trending_databank.jsonl           # Telemetry tracking early tech trends




Core Tool Invocations
Subsystem
Tool
Invocation Pattern
AST Code Graphs
graph_builder.py
python3
code-review-graph/grap
h_builder.py --dir
<target_repo> --format
md
Notebook Research
query_notebook.py
python3
notebook-lmpy/query_no
tebook.py --query
"<topic>" --source-dir
<path>
Source Bundler
source_packager.py
python3
notebook-lmpy/source_p
ackager.py --dir
<notes_dir> --output
bundle.md
Obsidian Sync
graph_sync.py
python3
obsidian-skills/graph_
sync.py --dir
<vault_dir> --format
md
Markor Sweeper
markor_sweeper.py
python3
obsidian-skills/markor
_sweeper.py --dir
<notes_dir> --manifest
manifest.jsonl
