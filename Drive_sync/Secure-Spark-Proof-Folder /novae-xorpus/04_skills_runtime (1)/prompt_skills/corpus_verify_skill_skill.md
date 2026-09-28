---
name: corpus_verify_skill
description: Procedural skill extracted from Corpus verify SKILL.md.
extracted_at: 2026-09-09T18:41:49.360678+00:00
source_doc: Corpus verify SKILL.md
extracted_tools: ['04_skills_runtime/extracted_tools/cli/corpus_verify_skill_tool_0.sh']
---

# Procedural Directives: Corpus verify SKILL

## Core Directives
---
name: corpus-verify
trigger: >
  Any corpus ingestion pipeline where source files have been converted to a
  clean or normalized format and independent verification is needed that content
  survived. Fire this skill after any clean pass — on first run, after adding
  new sources, after modifying tools/clean.py, or any time a source is suspected
  of losing detail through cleaning.
description: >
  Independent RLVR check. Reads source and clean files with different extraction
  libraries than tools/clean.py used, compares by named-atom and segment
  containment, and reports which details are missing. Hard rule 5: the tool that
  cleaned a file does not get a vote on whether the cleaning was good.
tools: [Bash, Read, Glob, Grep]
---

# Corpus-Verify Skill

## When to use

Fire this skill ... (compacted)
