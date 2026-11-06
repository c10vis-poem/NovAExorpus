---
name: cli-tools
description: Which command-line tool to use for web search, GitHub, Hugging Face, NotebookLM and Graphify. Read before searching the web or calling those services.
---

# CLI tools

Run these with Bash. They print to stdout, so pipe through `jq` or `head`. Never print a key.

## Web search: pplx
Do not use DuckDuckGo or `claw.search`. Use Perplexity:
- `pplx search web "query" -n 5`
- `pplx search web "query" --recency-filter week`
- `pplx search web "query" --domains arxiv.org,huggingface.co`
- `pplx content snippets "query" URL1 URL2`

Needs `PERPLEXITY_API_KEY`. If it is missing, say so and stop; do not fall back to another search.

## GitHub: gh
- `gh repo list c10vis-poem --limit 300`
- `gh search code "term" --owner c10vis-poem`
- `gh api repos/OWNER/REPO/contents/PATH`

## Hugging Face: hf
- `hf auth whoami`
- `hf download REPO --local-dir DIR`
- `hf --help` for the rest.

## NotebookLM and Graphify
- `notebooklm`: see the `notebooklm` skill.
- `graphify`: see the `graphify` skill.

## Google
- Gemini calls need `GEMINI_API_KEY`. Writing Gemini code: see the `gemini-api-dev` skill.
- `gcloud` is logged in for project work. Its token has no Drive scope, so use the Drive and Docs connectors for files.

## AI and dev trends: Signal Hunter
- Project root: `~/repos/signal-hunter`. Skills: `digest`, `weekly`, `test-source`, `list-sources`, `add-source`.
- Collect: `cd ~/repos/signal-hunter && .venv/bin/python -m src.collector`. Score: `.venv/bin/python -m src.scoring`.
- Notes go to `~/signal-hunter-output`, not the vault (the vault repo is public). Email is off. Do not run its `deploy` skill or the plugin-registration step in `setup`.
