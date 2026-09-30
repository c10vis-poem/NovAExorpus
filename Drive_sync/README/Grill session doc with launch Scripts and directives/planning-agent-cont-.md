---
tags: []
created: '2026-09-10'
title: '2026-09-10_planning-agent-cont-'
---



----
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

## 02. The LLM Wiki Layer (`wiki_md/`)
- Concepts: `02_wiki_md/concepts/`
- Architectures: `02_wiki_md/architectures/`
- Entities: `02_wiki_md/entities/`
- Indexes (MOCs): `02_wiki_md/indexes/`
- Governed via OpenWiki TUI by the Files Executive Agent.

## 03. Recall Cache (High-Speed Working Memory)
- Pre-tokenized Chunks: `03_recall_cache/jsonl/`
- Vector Indices: `03_recall_cache/vectors/`
- KV Store: `03_recall_cache/kv_store/`

## 04. Procedural Runtimes, Skills & Extracted Tools
- Prompt Skills: `04_skills_runtime/prompt_skills/`
- Extracted Tools: `04_skills_runtime/extracted_tools/`
- Execution Runtimes: `04_skills_runtime/runtimes/`
- Policies & Guards: `04_skills_runtime/policies/`

## 05. Episodic Logs & Trajectories
- Daily Driver Sync: `05_episodic_logs/daily_driver_sync/`
- Trajectories: `05_episodic_logs/trajectories/`
- Red Audit Sandbox: `05_episodic_logs/red_audit_sandbox/`
- RLVR Verifiers: `05_episodic_logs/rlvr_verifiers/`
EOF
fi