---
title: "Yeah, that makes sense. Um, that last file tree th..."
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/02_MY_ORIGINALS/Yeah, that makes sense. Um, that last file tree th....pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Here is an expanded, visually organized breakdown of the unified architecture. It includes
distinct iconography, color-coded functional tags, and detailed descriptions for each tier and
subfolder.
🗺️ Visual Architecture Map
📦 vault_root/​
 ├── 📜 MAP.md                           # ⚪ [METACOGNITIVE] Master human-readable index &
ontology graph​
 ├── 📊 manifest.jsonl                   # ⚪ [METACOGNITIVE] Fast machine catalog, hashes &
dependency index​
 │​
 ├── 📁 01_raw_sources/                  # 🟢 [SENSORY / COLD ARCHIVE] Immutable ground
truth inputs​
 │   ├── 📑 pdf/                         #   ├── Original research papers, whitepapers, tech specs​
 │   ├── 🎬 media/                       #   ├── Raw video lectures, audio memos, diagram
screencaps​
 │   └── 📝 text/                        #   └── Web scrapes, raw transcripts, source code dumps​
 │​
 ├── 📁 02_master_wiki/                  # 🟣 [SEMANTIC MEMORY] Curated conceptual
knowledge vault​
 │   ├── 💡 concepts/                    #   ├── Atomic markdown notes (Zettelkasten / topic cards)​
 │   ├── 🏛️ architectures/               #   ├── High-level design docs, system blueprints, specs​
 │   └── 🏷️ entities/                    #   └── Domain models, API registries, entity relationships​
 │​
 ├── 📁 03_recall_cache/                 # 🟡 [WORKING MEMORY ACCELERATOR] High-speed
retrieval assets​
 │   ├── ⚡ jsonl/                       #   ├── Pre-tokenized chunks, metadata-dense passage cards​
 │   ├── 📐 vectors/                     #   ├── Local embedding indices (FAISS / Chroma / HNSW)​
 │   └── 🗝️ kv_store/                    #   └── Key-value cache for low-latency exact-match queries​
 │​
 ├── 📁 04_skills_runtime/               # 🔵 [PROCEDURAL MEMORY] Behavioral policies, tools
& skills​
 │   ├── 🎯 prompt_skills/               #   ├── Modular agent definitions (YAML frontmatter +
instructions)​
 │   ├── ⚙️ runtimes/                     #   ├── Executable shell scripts, Python hooks, API
adapters​
 │   └── 🛡️ policies/                    #   └── Self-correction heuristics, backoff rules, schema
guards​
 │​
 └── 📁 05_episodic_logs/                # 🔴 [EPISODIC MEMORY] Trajectories, telemetry &
verifiers​
     ├── ⏱️ trajectories/                #   ├── Time-stamped execution runs, tool calls, step traces​
     ├── ⚖️ rlvr_verifiers/              #   ├── Pass/fail scores, reward signals, compiler feedback​
     └── 🧹 hygiene_reports/             #   └── Linter outputs, schema validation logs, stale-cache
audits​



🧩 Detailed Tier Breakdown
Tier & Icon
Directory
Cognitive Role
I/O Cadence
Primary Function
& Formats
⚪ Metacognitive / (Root)
Global Router
Read-Heavy
Contains MAP.md
(human
navigation) and
manifest.jsonl
(machine index).
Acts as the central
directory mapping
cross-tier
references without
loading full file
bodies.
🟢 Tier 1
01_raw_sources/ Sensory Buffer
Write-Once
Stores raw,
immutable source
materials (.pdf,
.mp4, .wav, .html).
Protected against
automated agent
modification to
guarantee
reproducible
provenance.
🟣 Tier 2
02_master_wiki/
Semantic
Memory
Continuous Sync Human- and
agent-readable
Markdown notes
(.md) linked via
wiki-links.
Synthesizes
concepts,
architectures, and
domain schemas
extracted from Tier
1.
🟡 Tier 3
03_recall_cache/ Working Memory Ephemeral /
Rebuilt
High-speed
machine cache
(.jsonl, vector
indices).
Formatted
specifically for
sub-second
retrieval into the
LLM context
window during
reasoning loops.


Tier & Icon
Directory
Cognitive Role
I/O Cadence
Primary Function
& Formats
🔵 Tier 4
04_skills_runtime/ Procedural
Memory
Version-Controlled Houses
executable code,
prompt skills, and
corrective
heuristics (.py, .sh,
SKILL.md).
Encodes how the
system works and
uses tools.
🔴 Tier 5
05_episodic_logs/ Episodic Memory Append-Only
Time-series
records of agent
attempts,
trajectory traces,
and RLVR reward
signals (.log,
.jsonl). Provides
the training and
refinement data for
Tier 4.
🔄 Dynamic Data Flow
[ Tier 1: Raw Sources ] ──(Ingest & Synthesize)──► [ Tier 2: Master Wiki ]​
                                                            │​
                                                     (Chunk & Embed)​
                                                            ▼​
                                                [ Tier 3: Recall Cache ]​
                                                            │​
                                                    (Stream to Prompt)​
                                                            ▼​
┌───────────────────────────────────────────────────────────
─────────────────────────────┐​
│                        ACTIVE CONTEXT WINDOW (Working Memory)                          │​
└───────────────▲──────────────────────────────────────────
──────────────┬───────────────┘​
                │ Invokes Tool / Skill                                   │ Emits Trace​
  [ Tier 4: Skills & Runtime ]                           [ Tier 5: Episodic Logs ]​
                ▲                                                        │​
                │                                                        │​
                └─────────────── Evaluates Reward / Loss ────────────────┘​
                                  (RLVR Feedback Loop)​

1.​ Extraction: New inputs hit 01_raw_sources/ and are distilled into atomic notes in
02_master_wiki/.
2.​ Indexing: The wiki is indexed and chunked into 03_recall_cache/ for fast machine
retrieval.


3.​ Execution: The agent pulls prompt context from Tier 3, executes tasks using routines
from 04_skills_runtime/, and streams every intermediate step into 05_episodic_logs/.
4.​ Refinement: The RLVR verifier grades the episodic logs; passing trajectories become
refined skills in Tier 4 or updated architectural notes in Tier 2.
