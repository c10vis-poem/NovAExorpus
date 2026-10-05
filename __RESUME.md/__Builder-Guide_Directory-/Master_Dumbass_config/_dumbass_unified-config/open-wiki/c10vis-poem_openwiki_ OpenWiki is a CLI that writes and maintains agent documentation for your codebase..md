<!-- Converted from c10vis-poem_openwiki_ OpenWiki is a CLI that writes and maintains agent documentation for your codebase..pdf — 4 pages -->

## Page 1

c10vis-poem openwiki
More
Security and quality
Watch 0 Fork 0
## OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
MIT License
0stars 0forks 0watching 7branches 0tags Activity
Public repository · Forked from langchain-ai/openwiki
Your main branch isn't protected Dismiss Protect this branch
Protect this branch from force pushing or deletion, or require status checks before merging. View documentation.
7Branches 0Tags Go tofile T Go to file Add file Code
This branch is 5 commits ahead of and 368 commits behind langchain-ai/openwiki:main .
Contribute Sync fork
| c10vis-poem and claude fix: forbid execute from browsing outside the target repo |  |  | 0478e0b · 2 weeks ago |
|---|---|---|---|
| .github/workflows | ci: gate merges on checks + secret sc … | 2 weeks ago |  |
| examples | fix: Readme improvements (langchai … | 3 months ago |  |
| openwiki | docs: add openwiki's own SKILL.md —… | 2 months ago |  |
| src | fix: forbid execute from browsing out … | 2 weeks ago |  |
| static | fix: Readme improvements (langchai … | 3 months ago |  |
| .gitignore | init commit | 3 months ago |  |
| .prettierignore | refactor, auto-write gh workflow | 3 months ago |  |
| AGENTS.md | cr | 3 months ago |  |
| CLAUDE.md | cr | 3 months ago |  |
| DEVELOPMENT.md | cli improvements | 3 months ago |  |
| LICENSE | init commit | 3 months ago |  |
| README.md | feat: project-scoped openwiki/SKILL. … | 2 months ago |  |
   
 
 
 
 
 
.gitignore init commit 3 months ago
 
AGENTS.md cr 3 months ago
CLAUDE.md cr 3 months ago
 
LICENSE init commit 3 months ago

---

## Page 2

| eslint.config.js | refactor, auto-write gh workflow | 3 months ago |
|---|---|---|
| package.json | release: 0.0.1 (langchain-ai#20) | 3 months ago |
| pnpm-lock.yaml | feat: Support multiple model providers | 3 months ago |
| tsconfig.json | init commit | 3 months ago |
 
 
 
tsconfig.json init commit 3 months ago
README License
## OpenWiki
### OpenWiki is a CLI that writes and maintains documentation for your codebase, built specifically for agents.
## Install
npm install -g openwiki
## Quick Start
### Initialize OpenWiki, configure your model and API key, then generate documentation

---

## Page 3

openwiki --init
Then to ensure your documentation stays up-to-date, add the GitHub action to your repository to automatically open a PR once a day with documentation updates: openwiki-update.yml
Copy the contents of that file into .github/workflows/openwiki-update.yml in your repository.
### Usage
Start the interactive CLI:
openwiki
Start OpenWiki with an initial request:
openwiki "Please generate documentation for this repository"
Run a single command and exit:
openwiki -p "Summarize what you can do"
Initialize OpenWiki:
openwiki --init
Update existing documentation:
openwiki --update
Show help:
openwiki --help
openwiki openwiki/ creates initial documentation in when no wiki exists. If openwiki/ already exists, it
send follow-up messages. Use -p or --print for a one-shot non-interactive run that prints the final assistant
output.
openwiki AGENTS.md will automatically append prompting to your and/or CLAUDE.md files to instruct your
coding agent to reference it when searching for context. If the file does not already exist in your repository, OpenWiki will create it for you.
On the first interactive run, OpenWiki will have you configure your inference provider, API key, and LLM. You will also be able to set a LangSmith API key to trace your OpenWiki runs to a LangSmith tracing project named "openwiki" (optional).

---

## Page 4

These configuration options and secrets will be saved to ~/.openwiki/.env on your local machine.
# Customizing
# OpenWiki supports OpenRouter, Fireworks, Baseten, OpenAI and Anthropic out of the box. By default, there are a
# few models pre-defined (GLM 5.2, Kimi K2.6, Sonnet 5, etc) but for each inference provider, OpenWiki will allow
# you to specify your own custom model ID.
# If there's an inference provider or model you'd like to see added, please open a PR!
# Project skill file
Drop an openwiki/SKILL.md file in your repository to customize how OpenWiki behaves for that specific project
# —conventions, terminology, areas to focus on or avoid, anything you'd want a documentation writer joining the
--init project to know upfront. OpenWiki reads it on every run (chat, , and --update ) and follows it in addition to
# its built-in instructions.
# openwiki/SKILL.md
Always refer to the database layer as "the vault", never "the DB". Skip documenting anything under legacy/ — that code is being deleted.
# This file is optional. Repositories without one see no change in behavior. It does not override OpenWiki's security
.env rules (it can't get OpenWiki to read secrets, files, or write outside openwiki/ ) or the restriction on which
# top-level files it may edit.
# Releases
No releases published Create a new release
# Packages
No packages published Publish your first package
# Contributors
No contributors
# Languages
TypeScript 99.8% JavaScript 0.2%