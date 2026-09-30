---
tags: []
created: '2026-09-10'
title: '2026-09-10_planning-agent'
---



----
Operational Steps for the Planning Agent
Step 1: Locating Information (Read Pass)
            1. When asked a domain question, check 03_recall_cache/ first for relevant chunks.
            2. If full context is required, resolve the source path via MAP.md and read the relevant note in 02_wiki_md/.
            3. Only query 01_raw_sources/ if source verification or citation check is explicitly requested.
Step 2: Scaffolding or Modifying Repo Content (Write Pass)
            1. When processing new source material:
            * Subsection 1: Place the original asset into 01_raw_sources/<type>/.
            * Subsection 2: Screen document and synthesize conceptual notes into 02_wiki_md/<category>/ via OpenWiki TUI conventions.
            * Subsection 3: Extract procedural skills to 04_skills_runtime/prompt_skills/ and executable tools to 04_skills_runtime/extracted_tools/.
            * Subsection 4: Regenerate the corresponding search chunks in 03_recall_cache/jsonl/, update the sub-tier manifest.jsonl, and append the record to the root manifest.jsonl and MAP.md.
Step 3: Executing Tools & Self-Correction (RLVR Loop)
            1. Retrieve relevant executable scripts or skills from 04_skills_runtime/.
            2. Stream execution status and tool payloads into 05_episodic_logs/trajectories/.
            3. If a step fails (reward: -1.0 or non-zero exit code):
            * Subsection 1: Do not discard the error context.
            * Subsection 2: Ingest the error trace from Tier 5 into active Working Memory.
            * Subsection 3: Search 04_skills_runtime/policies/ for documented recovery heuristics.
            * Subsection 4: Attempt remediation and log the retry attempt.
10. Complete Repository Scaffolding Script
Execute this non-interactive bash sequence to bootstrap or audit the entire 5+1 Tier cognitive filesystem topology, establishing all subdirectories, tier-level manifest.jsonl files, and root metacognitive indexes:
#!/usr/bin/env bash
set -euo pipefail

echo "===> Initializing 5+1 Tier Cognitive Repository Architecture..."

# 1. Scaffold all directory hierarchies
mkdir -p 01_raw_sources/{pdf,media,text}
mkdir -p 02_wiki_md/{concepts,architectures,entities,indexes}
mkdir -p 03_recall_cache/{jsonl,vectors,kv_store}
mkdir -p 04_skills_runtime/{prompt_skills,extracted_tools/{cli,wrappers},runtimes,policies}
mkdir -p 05_episodic_logs/{daily_driver_sync,trajectories,red_audit_sandbox,rlvr_verifiers,hygiene_reports}

# 2. Touch distributed manifest.jsonl files across all tiers
touch manifest.jsonl
touch 01_raw_sources/manifest.jsonl
touch 02_wiki_md/manifest.jsonl
touch 03_recall_cache/manifest.jsonl
touch 04_skills_runtime/manifest.jsonl
touch 05_episodic_logs/manifest.jsonl

# 3. Initialize Root MAP.md if absent
if [ ! -f "MAP.md" ]; then
 cat << 'EOF' > MAP.md
# Master Repository Ontology Map

## 01. Raw Sources (Cold Archive)
- Sensory ground truth cataloged in `01_raw_sources/manifest.jsonl`.