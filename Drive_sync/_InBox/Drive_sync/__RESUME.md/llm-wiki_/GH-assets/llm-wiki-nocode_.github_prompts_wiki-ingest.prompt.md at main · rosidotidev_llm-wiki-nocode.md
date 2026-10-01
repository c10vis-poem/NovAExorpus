<!-- Converted from llm-wiki-nocode_.github_prompts_wiki-ingest.prompt.md at main · rosidotidev_llm-wiki-nocode.pdf — 2 pages -->

## Page 1

rosidotidev llm-wiki-nocode
Code Issues Pull requests Agents Actions Projects Security and quality Insights
main llm-wiki-nocode / .github / prompts / wiki-ingest.prompt.md
rosidotidev first commit of a working solution for LLM WIKI with no code 0595424 · 4 months ago
12 lines (8 loc) · 661 Bytes
Preview Code Blame Raw
Ingest raw documents, approved questions, and approved lint fixes into the wiki.
description
agent wiki-ingestor
### Wiki Ingest
automatically scan all three source directories ( raw/ , questions_approved/ , lint_approved/ ) and process anything not yet ingested — no questions asked.
Specifying a single file or a specific command is supported for advanced use only and is generally discouraged — prefer the auto-scan.
${input:source?Leave empty for auto-scan (recommended). Advanced only: specific file (e.g. raw/my-doc.md) or --RESET-ALL.}