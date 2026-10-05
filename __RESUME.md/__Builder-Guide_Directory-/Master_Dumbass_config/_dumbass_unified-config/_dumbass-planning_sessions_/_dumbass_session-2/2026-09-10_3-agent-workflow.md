---
tags: []
created: '2026-09-10'
title: '2026-09-10_3-agent-workflow'
---



----
Tri-Model Trace Alignment
            1. Query Model: Captures initial intent decomposition, system prompts, and task planning.
            2. Executor Model: Captures deterministic tool invocations, bash runs, and code snippets.
            3. Frontier Model: Captures fallback escalations, complex conceptual synthesis, and recovery reasoning.
Sandbox Evaluation & Dispositions
            * Determinism: The extracted script must execute in isolation without hidden dependencies.
            * Grounding Authority: Must agree with the universal memory bank without invented parameters.
            * Dispositions:
            * VERDICT_APPROVED (+1.0): Moved to upload queue for recursive training.
            * VERDICT_REJECTED (-1.0): Logged to 05_episodic_logs/red_audit_sandbox/ with an explicit failure reason, triggering recursive self-correction in Tier 4 policies.
8. Cloud Scripter & RLVR Recursive Training Pipeline
  [ Approved Trajectories ] 
            │
            ▼
┌────────────────────────────────────────┐
│ Cloud Pipeline Intake: GCS Bucket      │
│ gs://<repo>-rlvr-training-pipeline/    │
└────────────────────┬───────────────────┘
                    │ Triggers Cloud Function / Cloud Run
                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ GCP Scripter Application                                               │
│                                                                        │
│ 1. Ingests approved trajectory batches.                                │
│ 2. Formats dataset into standard recursive RLVR JSONL records.         │
│ 3. Executes automated verifier harness:                                │
│    - Syntax verification (AST parsing)                                 │
│    - Execution testing against mocked inputs                           │
│    - Behavioral reward scoring (+1.0 for valid recovery, -1.0 fail)    │
│ 4. Produces updated model weights / adapter checkpoints / prompt packs.│
└────────────────────┬───────────────────────────────────────────────────┘
                    │ Downstream Artifact Sync
                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Deployment Back to Edge & Local Tiers                                  │
│ - Updated Prompt Skills   ──► 04_skills_runtime/prompt_skills/         │
│ - Updated Extracted Tools ──► 04_skills_runtime/extracted_tools/       │
│ - Verified Run Logs       ──► 05_episodic_logs/rlvr_verifiers/         │
└────────────────────────────────────────────────────────────────────────┘

9. Agent Execution & Planning Protocols
               ┌────────────────────────────────────────┐
              │ 1. INGESTION & PLAN STAGE              │
              │    - Consult MAP.md / manifest.jsonl   │
              │    - Pull fast context from Tier 3     │
              └───────────────────┬────────────────────┘
                                  │
                                  ▼
              ┌────────────────────────────────────────┐
              │ 2. REASONING & PROCEDURAL DISPATCH     │
              │    - Load skills from Tier 4           │
              │    - Formulate execution plan          │
              └───────────────────┬────────────────────┘
                                  │
                                  ▼
              ┌────────────────────────────────────────┐
              │ 3. EXECUTION & LOGGING                 │
              │    - Run scripts or emit updates       │
              │    - Append step event to Tier 5       │
              └───────────────────┬────────────────────┘
                                  │
                                  ▼
              ┌────────────────────────────────────────┐
              │ 4. VERIFICATION & RECOVERY (RLVR)      │
              │    - Check reward signal (-1.0 / +1.0) │
              │    - Fail: Backtrack via episodic trace│
              │    - Pass: Commit changes to Tier 2/4  │
              └────────────────────────────────────────┘