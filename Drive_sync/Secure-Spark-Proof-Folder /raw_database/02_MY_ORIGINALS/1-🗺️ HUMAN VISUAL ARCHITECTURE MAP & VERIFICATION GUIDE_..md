---
title: "1-🗺️ HUMAN VISUAL ARCHITECTURE MAP & VERIFICATION GUIDE_."
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/02_MY_ORIGINALS/1-🗺️ HUMAN VISUAL ARCHITECTURE MAP & VERIFICATION GUIDE_..pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

🗺️ Visual Architecture Map
📦 vault_root/​
 ├── 📜 MAP.md                           # ⚪ [METACOGNITIVE] Master
human ontology & cross-tier map​
 ├── 📊 manifest.jsonl                   # ⚪ [METACOGNITIVE] Global
RAG catalog, sha256 hashes & index​
 │​
 ├── 📁 01_raw_sources/                  # 🟢 [TIER 1: COLD ARCHIVE]
Immutable sensory ground truth​
 │   ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of
all raw assets & provenance​
 │   ├── 📑 pdf/                         #   ├── Source research
papers, whitepapers, manuals​
 │   ├── 🎬 media/                       #   ├── Raw video lectures,
audio memos, screen recordings​
 │   └── 📝 text/                        #   └── Web scrapes, raw
transcripts, raw API payload dumps​
 │​
 ├── 📁 02_wiki_md/                      # 🟣 [TIER 2: THE LLM WIKI]
Semantic Memory (OpenWiki TUI)​
 │   ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of
conceptual nodes & graph links​
 │   ├── 💡 concepts/                    #   ├── Atomic markdown notes
(Zettelkasten / topic cards)​
 │   ├── 🏛️ architectures/               #   ├── System blueprints,
data contracts, interface specs​
 │   ├── 🏷️ entities/                    #   ├── Schemas, hardware
registers, device profiles​
 │   └── 🧭 indexes/                     #   └── Maps of Content
(MOCs) & taxonomy graph hubs​
 │​
 ├── 📁 03_recall_cache/                 # 🟡 [TIER 3: RECALL CACHE]
Working Memory Accelerator​
 │   ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of
vector & chunk shards​
 │   ├── ⚡ jsonl/                       #   ├── Pre-tokenized chunks
for low-latency context injection​
 │   ├── 📐 vectors/                     #   ├── Dense embedding
indices (FAISS / Chroma / HNSW)​
 │   └── 🗝️ kv_store/                    #   └── Key-value tables for
fast exact-match lookups​
 │​
 ├── 📁 04_skills_runtime/               # 🔵 [TIER 4: PROCEDURAL
MEMORY] Dual Skills & Extracted Tools​
 │   ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of
all extracted skills & tools​


 │   ├── 🎯 prompt_skills/               #   ├── Modular agent
definitions (YAML frontmatter + SKILL.md)​
 │   ├── 🛠️ extracted_tools/             #   ├── Deterministic tools
mined by Files Executive Agent​
 │   │   ├── cli/                        #   │   └── Shell utilities &
command wrappers (*.sh)​
 │   │   └── wrappers/                   #   │   └── Python API
wrappers & micro-utilities (*.py)​
 │   ├── ⚙️ runtimes/                     #   ├── Master operational
scripts & execution hooks​
 │   └── 🛡️ policies/                    #   └── Self-correction
heuristics & validation schemas​
 │​
 └── 📁 05_episodic_logs/                # 🔴 [TIER 5: EPISODIC
TELEMETRY] Trajectories & RLVR Audits​
     ├── 📊 manifest.jsonl               #   ├── Local RAG catalog of
sessions, audits & verifiers​
     ├── 📲 daily_driver_sync/           #   ├── Ingested logs from
edge device sessions​
     ├── ⏱️ trajectories/                #   ├── Tri-model traces
(Query, Executor, Frontier)​
     ├── 🛑 red_audit_sandbox/           #   ├── Red Auditor
evaluations & quarantine reports​
     ├── ⚖️ rlvr_verifiers/              #   ├── Graded assertions &
reward signals (+1.0 / -1.0)​
     └── 🧹 hygiene_reports/             #   └── Schema validation
logs & broken link audits​

🧩 Detailed Tier & Component Breakdown
Tier & Icon
Directory Path
Cognitive Role
Managing Entity
Primary Artifacts &
Formats
⚪ Metacognitive / (Root)
Global Routing
Index
Planning Agent
MAP.md (ontology
links),
manifest.jsonl
(global file hash
registry).
🟢 Tier 1
01_raw_sources/ Sensory Buffer
(Cold)
Ingestion Pipeline Immutable original
files: .pdf, .mp4,
.wav, .txt, .html.
🟣 Tier 2
02_wiki_md/
Semantic
Memory
Files Executive
Agent (OpenWiki
TUI)
Linked Markdown
wiki notes (.md)
with YAML
frontmatter.
🟡 Tier 3
03_recall_cache/ Working Memory
Buffer
Indexing Workers Machine-readable
.jsonl chunks,


Tier & Icon
Directory Path
Cognitive Role
Managing Entity
Primary Artifacts &
Formats
.faiss vector
indices, .db KV
tables.
🔵 Tier 4
04_skills_runtime/ Procedural
Repertoire
Extraction Engine SKILL.md prompt
files, extracted CLI
tools (.sh), Python
tools (.py).
🔴 Tier 5
05_episodic_logs/ Episodic Store &
Auditing
Cross-Auditor &
Red Auditor
Multi-model run
traces (.jsonl),
verifier rewards,
quarantine logs.
🔄 Dynamic System Data Flow
                                [ Ingested Raw Assets ]​
                                           │​
                                           ▼​
                                ┌─────────────────────┐​
                                │ 01_raw_sources/     │​
                                └──────────┬──────────┘​
                                           │​
                                           ▼​

┌───────────────────────────────────────────────────────────┐​
             │ OPENWIKI TUI / FILES EXECUTIVE AGENT
│​
             │ Dual Extraction: Mins Knowledge, Skills & Tools
│​

└─────────────┬───────────────────────────────┬─────────────┘​
                           │                               │​
                Concepts & Ontologies               Extracted Tools &
Skills​
                           │                               │​
                           ▼                               ▼​
             ┌───────────────────────────┐
┌───────────────────────────┐​
             │ 02_wiki_md/ (LLM Wiki)    │   │ 04_skills_runtime/
│​
             └─────────────┬─────────────┘
└─────────────┬─────────────┘​
                           │                               │​
                 Pre-tokenized Indexing             Tool Invocations​
                           │                               │​
                           ▼                               │​
             ┌───────────────────────────┐                 │​


             │ 03_recall_cache/          │                 │​
             └─────────────┬─────────────┘                 │​
                           │ Fast Context                  │​
                           ▼                               ▼​
┌─────────────────────────────────────────────────────────────────────
───┐​
│ ACTIVE CONTEXT WINDOW (Edge Daily Driver Run)
│​
│
│​
│   [Query Model]        ──►       [Executor Model]  ──► [Frontier
API]  │​
│   (Task Decomposition)           (Tool Calling)        (Deep
Fallback) │​
└───────────────────────────────────┬─────────────────────────────────
───┘​
                                    │​
                                    │ End-of-Day P2P Mesh Sync​
                                    ▼​
┌─────────────────────────────────────────────────────────────────────
───┐​
│ 05_episodic_logs/ & HOME NODE CROSS-AUDITOR
│​
│
│​
│ 1. Aligns tri-model traces into unified trajectories
│​
│ 2. Compiles candidate execution scripts against Universal Database
│​
└───────────────────────────────────┬─────────────────────────────────
───┘​
                                    │​
                                    ▼​
┌─────────────────────────────────────────────────────────────────────
───┐​
│ 🛑 SANDBOXED RED AUDITOR GATEKEEPER
│​
│ Isolated evaluation against ground truth memory bank
│​
└───────────────────┬───────────────────────────────┬─────────────────
───┘​
                    │                               │​
         VERDICT_APPROVED (+1.0)         VERDICT_REJECTED (-1.0)​
                    │                               │​
                    ▼                               ▼​
       ┌─────────────────────────┐     ┌─────────────────────────┐​
       │ Cloud GCS Bucket Ingest │     │ Quarantine Sandbox Log  │​
       │ gs://<repo>-rlvr/       │     │ Updates Tier 4 Policies │​


       └────────────┬────────────┘     └─────────────────────────┘​
                    │​
                    ▼​
       ┌─────────────────────────┐​
       │ Cloud Scripter / RLVR   │​
       │ Recursive Model &       │​
       │ Prompt Skill Training   │​
       └────────────┬────────────┘​
                    │​
                    └──► Deploys Updated Skills & Adapters to Edge
Nodes​

✅ Human Verification Reference
Target Component
Inspection Point
Expected Verification State
Distributed Manifests
Root + all 5 tier folders
Every tier contains a valid,
non-empty manifest.jsonl.
LLM Wiki Interlinking
02_wiki_md/ via OpenWiki TUI Zero dead [[wikilinks]];
frontmatter sources resolve to
Tier 1.
Tool/Skill Extraction
04_skills_runtime/
New sources produce both
.sh/.py tools and SKILL.md
prompts.
P2P Sync Logs
05_episodic_logs/daily_driver_
sync/
Day's session logs present with
aligned
Query/Executor/Frontier tags.
Red Gatekeeper
05_episodic_logs/red_audit_sa
ndbox/
Only scripts marked
VERDICT_APPROVED exist in
the cloud upload batch.
RLVR Verifier Logs
05_episodic_logs/rlvr_verifiers/ Verified runs show explicit +1.0
or -1.0 reward evaluations.
