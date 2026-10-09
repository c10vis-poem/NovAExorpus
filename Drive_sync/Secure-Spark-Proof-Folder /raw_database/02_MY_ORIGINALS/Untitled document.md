---
title: "Untitled document"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/02_MY_ORIGINALS/Untitled document.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

📦 vault_root/
 ├── 📜 MAP.md            # ⚪ Global map
 ├── 📊 manifest.jsonl    # ⚪ Global RAG
 │
 ├── 📁 01_raw_sources/   # 🟢 TIER 1 (Cold)
 │   ├── 📊 manifest.jsonl
 │   ├── 📑 pdf/
 │   ├── 🎬 media/
 │   └── 📝 text/
 │
 ├── 📁 02_wiki_md/       # 🟣 TIER 2 (Wiki)
 │   ├── 📊 manifest.jsonl
 │   ├── 💡 concepts/
 │   ├── 🏛️ architectures/
 │   ├── 🏷️ entities/
 │   └── 🧭 indexes/
 │
 ├── 📁 03_recall_cache/  # 🟡 TIER 3 (Cache)
 │   ├── 📊 manifest.jsonl
 │   ├── ⚡ jsonl/
 │   ├── 📐 vectors/
 │   └── 🗝️ kv_store/
 │
 ├── 📁 04_skills_runtime/# 🔵 TIER 4 (Skills)
       [ 01_raw_sources/ ]
        (Raw Tech Assets)
                │
                ▼
┌──────────────────────────────────────┐
│ OPENWIKI TUI / FILES EXEC AGENT      │
│ Dual Extraction: Skills & Tools      │
└──────────────────┬───────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 02_wiki_md/      ││ 04_skills_...    │
│ (The LLM Wiki)   ││ (Tools & Skills) │
└────────┬─────────┘└────────┬─────────┘
         │ Tokenize          │ Invocations
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 03_recall_cache/ ││ CONTEXT WINDOW   │
│ (Fast Buffer)    ││ (Query/Exec/API) │
└────────┬─────────┘└──────────────────┘
         │ RAG Chunks        ▲



 │   ├── 📊 manifest.jsonl
 │   ├── 🎯 prompt_skills/
 │   ├── 🛠️ extracted_tools/
 │   │   ├── cli/
 │   │   └── wrappers/
 │   ├── ⚙️ runtimes/
 │   └── 🛡️ policies/
 │
 └── 📁 05_episodic_logs/ # 🔴 TIER 5 (Logs)
     ├── 📊 manifest.jsonl
     ├── 📲 daily_driver_sync/
     ├── ⏱️ trajectories/
     ├── 🛑 red_audit_sandbox/
     ├── ⚖️ rlvr_verifiers/
     └── 🧹 hygiene_reports/


========================================
TIER BREAKDOWN & OPERATIONAL CARDS
========================================

[⚪ ROOT: METACOGNITIVE INDEX]
• Path:      / (vault_root)
       [ 01_raw_sources/ ]
        (Raw Tech Assets)
                │
                ▼
┌──────────────────────────────────────┐
│ OPENWIKI TUI / FILES EXEC AGENT      │
│ Dual Extraction: Skills & Tools      │
└──────────────────┬───────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 02_wiki_md/      ││ 04_skills_...    │
│ (The LLM Wiki)   ││ (Tools & Skills) │
└────────┬─────────┘└────────┬─────────┘
         │ Tokenize          │ Invocations
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 03_recall_cache/ ││ CONTEXT WINDOW   │
│ (Fast Buffer)    ││ (Query/Exec/API) │
└────────┬─────────┘└──────────────────┘
         │ RAG Chunks        ▲



• Files:     MAP.md & manifest.jsonl
• Operator:  Planning Agent
• Role:      Global routing & hashes

[🟢 TIER 1: COLD SENSORY ARCHIVE]
• Path:      01_raw_sources/
• Folders:   pdf/, media/, text/
• Operator:  Ingestion Pipeline
• Role:      Unaltered ground truth
• Invariant: Strictly Read-Only

[🟣 TIER 2: THE LLM WIKI LAYER]
• Path:      02_wiki_md/
• Folders:   concepts/, architectures/
             entities/, indexes/
• Operator:  Files Executive Agent
             (via OpenWiki TUI)
       [ 01_raw_sources/ ]
        (Raw Tech Assets)
                │
                ▼
┌──────────────────────────────────────┐
│ OPENWIKI TUI / FILES EXEC AGENT      │
│ Dual Extraction: Skills & Tools      │
└──────────────────┬───────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 02_wiki_md/      ││ 04_skills_...    │
│ (The LLM Wiki)   ││ (Tools & Skills) │
└────────┬─────────┘└────────┬─────────┘
         │ Tokenize          │ Invocations
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 03_recall_cache/ ││ CONTEXT WINDOW   │
│ (Fast Buffer)    ││ (Query/Exec/API) │
└────────┬─────────┘└──────────────────┘
         │ RAG Chunks        ▲



• Role:      Linked Markdown graph




🟡 TIER 3: RECALL CACHE]
• Path:      03_recall_cache/
• Folders:   jsonl/, vectors/, kv_store/
• Operator:  Indexing Workers
• Role:      Tokenized machine buffer
• Invariant: Ephemeral & Rebuildable

[🔵 TIER 4: PROCEDURAL RUNTIME]
• Path:      04_skills_runtime/
• Folders:   prompt_skills/, runtimes/
             extracted_tools/, policies/
       [ 01_raw_sources/ ]
        (Raw Tech Assets)
                │
                ▼
┌──────────────────────────────────────┐
│ OPENWIKI TUI / FILES EXEC AGENT      │
│ Dual Extraction: Skills & Tools      │
└──────────────────┬───────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 02_wiki_md/      ││ 04_skills_...    │
│ (The LLM Wiki)   ││ (Tools & Skills) │
└────────┬─────────┘└────────┬─────────┘
         │ Tokenize          │ Invocations
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 03_recall_cache/ ││ CONTEXT WINDOW   │
│ (Fast Buffer)    ││ (Query/Exec/API) │
└────────┬─────────┘└──────────────────┘
         │ RAG Chunks        ▲



• Operator:  Compilation Engine
• Role:      SKILL.md & CLI .sh/.py tools

[🔴 TIER 5: EPISODIC STORE & AUDIT]
• Path:      05_episodic_logs/
• Folders:   daily_driver_sync/,
             trajectories/, rlvr_verifiers/
             red_audit_sandbox/
• Operator:  Cross-Auditor & Red Auditor
• Role:      Tri-model logs & RLVR
• Invariant: Append-Only telemetry

       [ 01_raw_sources/ ]
        (Raw Tech Assets)
                │
                ▼
┌──────────────────────────────────────┐
│ OPENWIKI TUI / FILES EXEC AGENT      │
│ Dual Extraction: Skills & Tools      │
└──────────────────┬───────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 02_wiki_md/      ││ 04_skills_...    │
│ (The LLM Wiki)   ││ (Tools & Skills) │
└────────┬─────────┘└────────┬─────────┘
         │ Tokenize          │ Invocations
         ▼                   ▼
┌──────────────────┐┌──────────────────┐
│ 03_recall_cache/ ││ CONTEXT WINDOW   │
│ (Fast Buffer)    ││ (Query/Exec/API) │
└────────┬─────────┘└──────────────────┘
         │ RAG Chunks        ▲
