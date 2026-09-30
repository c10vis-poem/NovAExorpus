---
tags: []
created: '2026-09-10'
title: '2026-09-10_procedural-mem_skills-tools'
---



----
Tier 4: 04_skills_runtime/ (Procedural Memory: Skills & Tools)
         * Write Policy: Version-controlled tooling, prompts, and instructions.
         * Prompt Skill Format (prompt_skills/): Standard modular prompt format containing purpose, required inputs, tool dependencies, and output schemas (SKILL.md).
         * Extracted Tools (extracted_tools/): Standalone executable code blocks extracted from documentation. Non-interactive scripts with standard exit codes (0 = success, non-zero = error).
Tier 5: 05_episodic_logs/ (Episodic Memory & Telemetry)
         * Write Policy: Append-only during agent task execution.
         * Trajectory Schema (trajectories/YYYYMMDD_session.jsonl):
{"timestamp": "2026-09-03T17:01:35Z", "step": 1, "task_id": "TASK-104", "prompt_hash": "a1b2c3", "tool_call": "run_linter", "exit_code": 0, "response_snippet": "OK"}

         * RLVR Log Schema (rlvr_verifiers/YYYYMMDD_eval.jsonl):
{"timestamp": "2026-09-03T17:01:40Z", "task_id": "TASK-104", "verifier_id": "syntax_test", "reward": 1.0, "feedback": "All assertions passed."}

4. The LLM Wiki Protocol & OpenWiki Files Executive Agent
The LLM Wiki (02_wiki_md/) serves as the persistent organizational spine. The Files Executive Agent manages it through the OpenWiki TUI:
 ┌─────────────────────────────────────────────────────────────┐
│                 OPENWIKI TUI WORKSPACE                      │
│        (Operated by the Files Executive Agent)              │
└──────────────────────────────┬──────────────────────────────┘
                               │ Governs, Indexes & Links
                               ▼
┌─────────────────────────────────────────────────────────────┐
│            TIER 2: THE LLM WIKI (/02_wiki_md/)              │
│            Organization-Wide Semantic Layer                 │
├─────────────────────────────────────────────────────────────┤
│ • Atomic conceptual notes & domain ontologies (*.md)        │
│ • Bidirectional cross-links ([[concept_a]] <-> [[concept_b]])│
│ • Strict YAML frontmatter metadata & provenance tracking    │
│ • Automatic sync with local & root manifest.jsonl catalogs  │
└─────────────────────────────────────────────────────────────┘

            1. TUI-Driven Lifecycle Management: The Files Executive Agent runs inside the OpenWiki TUI, monitoring file additions, moves, renames, and refactors across all tiers.
            2. Deterministic Linking & Backlinks: Automatically verifies bidirectional Markdown links ([[entity_name]]), ensuring the LLM Wiki remains an intact graph without orphaned concepts.
            3. Extraction Intake Coordination: Acts as the bridge between incoming raw sources in 01_raw_sources/, synthesizing structured knowledge into 02_wiki_md/, and passing extracted procedural artifacts to 04_skills_runtime/.
            4. Manifest Synchronization: Whenever the agent modifies a node in wiki_md/, it immediately writes updated hashes, token counts, and entity tags to both 02_wiki_md/manifest.jsonl and the root manifest.jsonl.
5. Universal Skill & Tool Extraction Engine
The compilation agent processes incoming documentation through a dual-channel extraction filter:
                           [ Ingested Source Document ]
                                       │
                   ┌───────────────────┴───────────────────┐
                   ▼                                       ▼
       ┌───────────────────────┐               ┌───────────────────────┐
       │  SKILL EXTRACTION     │               │    TOOL EXTRACTION    │
       └───────────┬───────────┘               └───────────┬───────────┘
                   │                                       │
                   ▼                                       ▼
       • Reasoning heuristics                  • Standalone shell/python scripts
       • Step-by-step workflows                • API wrappers & micro-utilities
       • Formatting / prompt templates         • CLI invocation syntax & flags
       • Edge-case recovery rules              • Data conversion routines
                   │                                       │
                   ▼                                       ▼
       [ 04_skills_runtime/    ]               [ 04_skills_runtime/    ]
       [ prompt_skills/*.md    ]               [ extracted_tools/*     ]

Extraction Classification Rules
            1. Targeting Skills: If a passage describes how to reason, how to structure an analysis, or how to coordinate a sequence of tasks, format it as a markdown skill with YAML frontmatter into 04_skills_runtime/prompt_skills/.
            2. Targeting Tools: If a passage contains executable code, CLI command flags, API request formats, or data transformation utilities, extract it into an executable script (.py or .sh) with explicit argument parsing into 04_skills_runtime/extracted_tools/.
            3. Registration: Update the local 04_skills_runtime/manifest.jsonl immediately upon extraction.
6. Hierarchical manifest.jsonl Specification for Distributed RAG
Every directory root must hold a dedicated manifest.jsonl file. This prevents full-vault scanning during localized RAG operations.
JSONL Schema Structure
Each line in any manifest.jsonl must strictly adhere to this schema:
{
 "id": "UUID-OR-PATH-HASH",
 "path": "relative/path/to/file.ext",
 "tier": 4,
 "category": "extracted_tool",
 "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
 "tokens": 412,
 "semantic_summary": "CLI utility to extract audio streams from MP4 video containers.",
 "entities_extracted": ["ffmpeg", "audio_processing", "mp4_to_wav"],
 "skills_tools_extracted": [
   {"type": "tool", "name": "extract_audio_stream", "path": "04_skills_runtime/extracted_tools/cli/extract_audio.sh"},
   {"type": "skill", "name": "audio_preprocessing_policy", "path": "04_skills_runtime/prompt_skills/audio_prep.md"}
 ],
 "provenance_source": "01_raw_sources/pdf/media_processing_guide.pdf",
 "last_synced": "2026-09-03T17:05:00Z"
}

RAG Query Traversal Protocol
            1. Directory-Level Scope Matching: The RAG agent inspects root manifest.jsonl to identify candidate subdirectories.
            2. Localized Search: The agent reads only the relevant sub-tier manifest.jsonl (e.g., 04_skills_runtime/manifest.jsonl), matching semantic summaries and entities.
            3. Targeted Ingestion: Only the exact chunk or tool indicated by the manifest record is loaded into active Working Memory.
7. End-of-Day P2P Sync, Cross-Auditor & Sandboxed Red Auditor Workflow
When the daily driver reconnects to the home environment via the peer-to-peer server mesh, the Home Script Collector / Auditor Agent executes the cross-audit:
┌───────────────────────────┐
│ DAILY DRIVER (Edge Run)   │
│ - Query Model Traces      │
│ - Executor Model Logs     │
│ - Frontier/Cloud API Logs │
└─────────────┬─────────────┘
             │ P2P Sync (End of Day)
             ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ HOME NODE: Script Collector & Cross-Auditor Agent                                      │
│                                                                                        │
│ 1. Ingests raw session logs into: 05_episodic_logs/daily_driver_sync/                  │
│ 2. Reconstructs full inference trajectories across models:                            │
│    [User Intent] ──► [Query Model] ──► [Executor Model] ──► [Frontier/Cloud Fallback]   │
│ 3. Judges compiled tool usages and scripts against Universal Source of Truth (DB/Vault)│
└─────────────────────────────────────────────┬──────────────────────────────────────────┘
                                             │ Unverified Trajectories
                                             ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ HOME NODE: Sandboxed Red Auditor Gatekeeper                                            │
│                                                                                        │
│ - Operates in an isolated execution sandbox.                                           │
│ - Queries shared database / memory bank for independent truth verification.            │
│ - Performs adversarial compliance, error boundary, and anti-hallucination checks.      │
└──────────────────────┬──────────────────────────────────┬──────────────────────────────┘
                      │ PASS                             │ FAIL (-1.0)
                      ▼                                  ▼
┌──────────────────────────────────────┐       ┌─────────────────────────────────────────┐
│ Quarantined Package for RLVR Cloud   │       │ Quarantine Log: 05_episodic_logs/       │
│ Upload to GCS Bucket                 │       │ Ingest back into Tier 4 / Policy Update │
└──────────────────────────────────────┘       └─────────────────────────────────────────┘