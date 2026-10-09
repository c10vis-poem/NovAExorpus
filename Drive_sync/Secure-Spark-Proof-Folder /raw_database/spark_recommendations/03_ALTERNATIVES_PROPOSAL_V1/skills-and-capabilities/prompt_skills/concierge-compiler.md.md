---
title: "concierge-compiler.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/prompt_skills/concierge-compiler.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

name: concierge-compiler description: "Transforms unstructured
voice transcripts and multi-paragraph stream-of-consciousness
user prompts into clean, structured Markdown meta-prompts
ready for execution."
Concierge Meta-Prompt Compiler Skill
Use this skill when processing voice ingress, speech-to-text transcripts, or raw phone inputs to
prepare a clean prompt for execution models without conversational boilerplate.
Operating Principles
1.​ Strip Transcription Artifacts:
-​
Remove repetitions, false starts, and filler phrases ("um", "you know", "basically",
"or whatever").
-​
Fix speech recognition typos and run-on sentences.
2.​ Isolate Concrete Intent:
-​
Clearly state the user's primary goal in 1–2 crisp sentences.
-​
Separate contextual background from actionable imperatives.
3.​ Explicitly Inject Invariants:
-​
Enforce system rules (e.g., non-destructive operations, exact naming
conventions, required directory targets).
4.​ Define Structured Output:
-​
Request bounded, verifiable deliverables (e.g., specific file types, tables, exit
codes).
