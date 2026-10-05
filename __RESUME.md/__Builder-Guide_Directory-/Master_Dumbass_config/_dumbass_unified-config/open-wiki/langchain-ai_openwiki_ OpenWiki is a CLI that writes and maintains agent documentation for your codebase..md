<!-- Converted from langchain-ai_openwiki_ OpenWiki is a CLI that writes and maintains agent documentation for your codebase..pdf — 11 pages -->

## Page 1

langchain-ai openwiki
Code Issues 72 Pull requests 85 Agents Actions Projects Security and quality Insights
Watch 54 Fork 1.2k
OpenWiki is a CLI that writes and maintains agent documentation for your codebase.
MIT License
Code of conduct
Contributing
Security policy
16.8k stars 1.2k forks 54 watching 50 branches 25 tags Activity Custom properties
Public repository
m 50 Branches 25 Tags Go to file T Go to file Add file Code
| 3 people docs: update OpenWiki (#931) |  |  | 60c8eea · yesterday |
|---|---|---|---|
| .changeset | chore: version packages (#920) | 2 days ago |  |
| .claude | feat: Add gemini 3.6 flash and 3.5 flash lite ( … | 2 months ago |  |
| .github | ci: link generated OpenWiki pull request | last week |  |
| docs | feat: add Oh My Pi (omp) coding-agent integ … | 3 days ago |  |
| evals | feat: add LEDGER, a longitudinal benchmark … | last month |  |
| examples | ci: link generated OpenWiki pull request | last week |  |
| integrations/openwiki | feat: implement openwiki search, read, and l … | 2 days ago |  |
| openwiki | docs: update OpenWiki (#931) | yesterday |  |
| scripts | add antigravity coding agent target (#922) | 3 days ago |  |
| skills | feat: add built-in custom-mcp connector for … | last month |  |
| src | fix(bob): stream responses so long generati … | 2 days ago |  |
| static | update readme for 0.6.0 release (#927) | 2 days ago |  |
| test | fix(bob): stream responses so long generati … | 2 days ago |  |
| .gitignore | docs: update OpenWiki (#680) | last month |  |
| .prettierignore | add changeset (#730) | last month |  |
| AGENTS.md | docs: update OpenWiki (#931) | yesterday |  |
| CHANGELOG.md | chore: version packages (#920) | 2 days ago |  |
| CLAUDE.md | docs: update OpenWiki (#925) | 2 days ago |  |
| CONTRIBUTING.md | feat: implement openwiki search, read, and l … | 2 days ago |  |
| DEVELOPMENT.md | fix: require current node runtime (#863) | last week |  |
 
 
 
 
 
 
 
 
openwiki docs: update OpenWiki (#931) yesterday
 
 
 
 
 
.gitignore docs: update OpenWiki (#680) last month
.prettierignore add changeset (#730) last month
AGENTS.md docs: update OpenWiki (#931) yesterday
 
CLAUDE.md docs: update OpenWiki (#925) 2 days ago

---

## Page 2

LICENSE
| README.md | update readme for 0.6.0 release (#927) | 2 days ago |
|---|---|---|
| eslint.config.js | docs: document windows bun installation re … | 2 months ago |
| package.json | chore: version packages (#920) | 2 days ago |
| pnpm-lock.yaml | chore(deps): broad dependency modernizati … | 3 weeks ago |
| pnpm-workspace.yaml | chore(deps): broad dependency modernizati … | 3 weeks ago |
| tsconfig.client.json | feat: implement native wiki visualizer for op … | 2 months ago |
| tsconfig.eslint.json | feat: implement native wiki visualizer for op … | 2 months ago |
| tsconfig.json | feat: implement native wiki visualizer for op … | 2 months ago |
| vitest.config.ts | feat: add LEDGER, a longitudinal benchmark … | last month |
 
 
 
 
 
 
 
 
 
# A living wiki for your code, your agents, and you.
n p m v0.6.0 downloads 140k/month node > = 2 2 . 2 2 . 0 license MIT built with DeepAgents
1 #1 Repository Of The Day
# OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. Your coding agent can use it to
# understand a repository, answer questions, and find context across related projects. You can read the same pages or explore them
# as an interactive graph.
# For repository wikis, OpenWiki tracks facts back to source evidence so updates can focus on what changed. Start inside your coding
# agent, or use the standalone CLI for repository docs, personal knowledge, and scheduled updates.
# Get started · Search and link wikis · Explore · Standalone CLI · Command reference
# 🎉 What's new
Linked wiki workspaces: group related repositories with openwiki link , search across their wikis, and read relevant sections
# through MCP. See how it works →
# More coding-agent integrations: Oh My Pi, Antigravity, IBM Bob / Bob Shell, and Kiro join Codex, Claude Code, OpenCode, and
# Cursor. Connect your agent →

---

## Page 3

Parallel page workers: native CLI runs can now document multiple pages concurrently while saving progress page by page and adapting to provider rate limits. Configure concurrency →
Resumable updates and grounded Claims: completed pages survive interruptions, and versioned source evidence identifies facts that need attention. Explore the architecture →
Portable OKF v0.2 output and publishable visualizers are also available.
## Quick start
The easiest way to get started is inside the coding agent you already use. OpenWiki uses that agent's authenticated model session and repository tools, so there is no separate model provider to configure.
## 1. Install OpenWiki
You'll need Node.js 22.22.0 or newer.
npm install -g openwiki
## 2. Connect your coding agent
Choose the integration for your agent:
| README.md | update readme for 0.6.0 release (#927) | 2 days ago |
|---|---|---|
| Coding agent |  | Install |
| Codex | openwiki integrations install codex |  |
| Claude Code | openwiki integrations install claude |  |
| OpenCode | openwiki integrations install opencode |  |
| Cursor | openwiki integrations install cursor |  |
| IBM Bob / Bob Shell | openwiki integrations install bob |  |
| Kiro | openwiki integrations install kiro |  |
| Oh My Pi | openwiki integrations install omp |  |
| Antigravity | openwiki integrations install antigravity |  |
Coding agent Install
Codex openwiki integrations install codex
Claude Code openwiki integrations install claude
OpenCode openwiki integrations install opencode
Cursor openwiki integrations install cursor
IBM Bob / Bob Shell openwiki integrations install bob
Kiro openwiki integrations install kiro
Oh My Pi openwiki integrations install omp
Antigravity openwiki integrations install antigravity
## 3. Create your wiki
Restart your coding agent, open a repository, and ask:
Initialize this repository's OpenWiki from the current source and tests.
Your agent researches the repository and writes a linked wiki in openwiki/ . OpenWiki tracks its source evidence and saves progress
as each page completes.

---

## Page 4

Once your wiki is ready, ask questions, link related repositories, or explore it visually.
Installation scope, host-specific paths, and removal
What the coding-agent integration supports
### Search your wiki
Ask your agent to look up a question in the wiki:
Search this repository's OpenWiki for how retry handling works, then read the relevant sections.
openwiki_search finds compact, ranked results; openwiki_read retrieves the complete sections your agent selects. Agents are
guided to use retrieval for concrete questions, read relevant sections, and stop once grounded. It is optional context, not a routine step at the start of every task.
openwiki_list_workspaces and openwiki_list_wikis provide discovery when repositories are linked.
### Create wiki workspaces
A service often spans several repositories: a control plane, a data plane, and infrastructure. Use openwiki link to group their
existing wikis into a named workspace. Your agent can then search across the whole service and read relevant sections from any member wiki.

---

## Page 5

Start the workspace manager from a directory such as ~/dev :
cd ~/dev openwiki link
Create a workspace such as Payments , then select the repositories to include. They keep their own wikis, can belong to more than one workspace, and do not need to share a parent directory.
Finding repositories and choosing a search workspace
### Explore your wiki
Turn any wiki into an interactive node graph with a live, side-by-side Markdown reader:
openwiki visualize

---

## Page 6

The graph updates as you edit your wiki.
Local server options and publishing a static visualizer
### Keep your wiki current
After changing your code, ask your coding agent:
Update this repository's OpenWiki for changes since its last successful run.
OpenWiki checks repository changes and the evidence behind existing Claims to decide what needs updating. Clean updates skip model work and leave the wiki content untouched.
### Scheduled updates
Keep it current automatically by adding a scheduled CI job that opens a docs PR whenever the wiki changes:
openwiki-update.yml GitHub Actions: copy into .github/workflows/openwiki-update.yml .
GitHub Actions with auto-merge: copy openwiki-update-auto-merge.yml instead, then follow the setup details below.
openwiki-update.gitlab-ci.yml GitLab CI: copy into .gitlab-ci.yml or include it from your pipeline.
openwiki-update.bitbucket-pipelines.yml Bitbucket Pipelines: copy into bitbucket-pipelines.yml , then schedule the openwiki-update pipeline.
Auto-merge OpenWiki PRs
### Run OpenWiki directly
You can also use OpenWiki's own Deep Agents documentation agent, including for scheduled runs and personal wikis. After installing the CLI, initialize a repository wiki:
openwiki --init
The first run walks you through choosing a provider, credentials, and model, then writes docs to openwiki/ . OpenWiki supports
thirteen model providers, including hosted models and local OpenAI-compatible endpoints.

---

## Page 7

# Update an existing wiki from repository changes since its last successful run and any stale Claims:
openwiki --update
# Reinitializing a wiki and resuming interrupted runs
# Two modes
openwiki openwiki --init OpenWiki runs in one of two modes. Bare , , and openwiki --update default to code mode; add the
personal positional (or --mode personal ) for the personal brain.
# Mode Documents Writes to Get started
openwiki/ Code (default) The current repository in the repo openwiki --init
Personal Your connected sources ~/.openwiki/wiki openwiki personal --init
By default the CLI stays open after a run so you can send follow-up messages. Add -p / --print for a one-shot, non-interactive
--init run that prints the final output and exits. and --update auto-exit on success in an interactive terminal, so the same
# command works one-shot or interactively.
# Parallel page workers
init Native repository and update runs can document several pages at once:
OPENWIKI_PAGE_CONCURRENCY=4 openwiki --update
1 1 8 Concurrency defaults to and accepts values from to . Start at 2 to 4 and watch your provider's rate limits. Coding-agent
# integrations use their host's sequential page lifecycle; this setting controls the native CLI's workers.
# Worker ordering, rate limits, and retries
# Local state directory
# How it stays yours
# Your wiki stays in the repository as plain Markdown you own, with OpenWiki-managed grounding and run metadata versioned
# alongside it.
code AGENTS.md Agents read it as context. On each run, OpenWiki maintains an and CLAUDE.md at the repo root. Their
managed instructions use selective, progressive openwiki_search / openwiki_read retrieval for concrete questions when
openwiki/quickstart.md available and use as the fallback. OpenWiki only rewrites its own <!-- OPENWIKI:START -->…<!--
OPENWIKI:END --> block and leaves the rest of each file untouched.
Grounding stays with the wiki. Versioned claim sidecars under openwiki/.claims/ travel with the Markdown, so the evidence
# needed to maintain factual pages is inspectable and reviewable.
You set the brief. Repository-specific instructions live in openwiki/INSTRUCTIONS.md , a user-authored file OpenWiki reads for
# scope and priorities but never rewrites during normal runs.
No-op runs do not churn docs. A clean update skips model work and leaves wiki content untouched while refreshing .last-
update.json to record that the check ran.
Local, private config. Provider choice, keys, and optional LangSmith tracing are saved to ~/.openwiki/.env on your machine.
# Ignoring paths
# Create a
# .openwikiignore file in the repository root to keep generated docs from reading or describing private, generated, or
# irrelevant paths. The syntax supports comments, blank lines, * and ** globs, directory rules, and ! negation:

---

## Page 8

secrets/ *.log !logs/keep.log
When .openwikiignore has active rules, OpenWiki filters filesystem discovery and restricts shell execute so ignored paths stay out
of the run. This is a read boundary: ignored paths are never read, scanned, or reproduced in the docs. It does not guarantee a topic is never mentioned, since the agent may still infer an ignored area from other allowed evidence such as tests, the README, or commit messages.
### How it works
OpenWiki separates repository research and writing from the bookkeeping that keeps a wiki consistent. Repository pages carry their source evidence, and completed work is saved for future updates.
### OpenWiki architecture
Repository generation follows an ordered queue of independently durable page jobs. Native CLI runs can process eligible pages concurrently; coding-agent integrations consume the queue sequentially. openwiki/.run.json checkpoints the active run and its progress. A page advances only after its Markdown, Claims, verification, and openwiki/.page-manifest.json entry are durable, preserving completed work and page-specific source baselines across interruptions and future runs.
### Grounded Claims
as repo://src/server.ts#L40-L82 . When that evidence changes or disappears, OpenWiki identifies which facts need to be
confirmed, rewritten, or retired.

---

## Page 9

How Claims are reconciled and persisted
Grounded Claims currently apply to repository code wikis and repository evidence. Connector-derived facts, including LangSmith-only observations, are not claimed.
## Open Knowledge Format (OKF v0.2)
OpenWiki emits Google Open Knowledge Format (OKF) v0.2 bundles in both modes, so your wiki is portable to any OKF-aware tool.
Front matter, provenance, and verification metadata
## Diagrams
OpenWiki embeds Mermaid diagrams wherever they make a concept clearer than prose: sequence diagrams for runtime flows, ER diagrams for data models, state diagrams for lifecycles, and flowcharts for control flow. Diagrams are grounded in the inspected source, added where they add signal, and kept in sync on --update . No configuration is required.
Diagram validation and repair
## Connect your sources
Beyond repository docs, OpenWiki has nine built-in connectors. In personal mode, OpenWiki ingests knowledge from the tools you already use, synthesizing them into your local wiki. First-run onboarding offers setup for Custom MCP, local git repositories, Notion, Gmail, X/Twitter, Web Search, and Hacker News. Slack is also available with its OAuth app and HTTPS callback configured.
Start a personal wiki with openwiki personal --init , then authenticate and ingest sources as needed:
| openwiki auth notion | # run a local browser OAuth flow for a provider |
|---|---|
| openwiki ingest all | # run every configured source |
| openwiki ingest web-search | # run one connector's sources |
openwiki auth notion # run a local browser OAuth flow for a provider openwiki ingest all # run every configured source openwiki ingest web-search # run one connector's sources
Connector details and OAuth
## LangSmith connector (code mode)

---

## Page 10

personal The connectors above feed a wiki. The LangSmith connector instead enriches a code wiki: it pulls recent LangSmith
traces (tool calls, outcomes, and latency) for the projects you choose through the official LangSmith SDK, so a repository's docs reflect how its code actually behaves at runtime, not just what the source says.
Configure LangSmith projects, regions, and credentials
### Model providers
These settings apply when running OpenWiki directly. Coding-agent integrations use the host's authenticated model session.
OpenWiki supports thirteen providers. The onboarding default is OpenAI with gpt-5.6-terra . Choose from preset models where available or supply a custom model ID. Provider credentials are stored in ~/.openwiki/.env .
Provider Credential
OpenAI (default) OPENAI_API_KEY
OpenAI (ChatGPT login) Browser sign-in, uses your ChatGPT plan
Anthropic ANTHROPIC_API_KEY
Gemini (AI Studio) GEMINI_API_KEY
Gemini Enterprise (Vertex AI) Google ADC, keyless
AWS Bedrock IAM credentials
GitHub Copilot GitHub CLI session
OpenRouter OPENROUTER_API_KEY
Nebius / Fireworks / Baseten / NVIDIA NIM Provider API key
OpenAI-compatible (LiteLLM, Ollama, LM Studio, gateways) Base URL + key
GitHub Copilot
AWS Bedrock
Gemini (AI Studio) and Gemini Enterprise (Vertex AI)
OpenAI (ChatGPT login)
OpenAI-compatible endpoints (LiteLLM, Ollama, LM Studio, gateways)
Alternative base URLs, OpenRouter pinning, and retries
Note
If there is an inference provider or model you would like to see added, please open a PR.
### Command reference
openwiki # interactive chat, code mode, current repo openwiki personal # interactive chat, personal brain openwiki "generate docs" # start with an initial request openwiki -p "what can you do?" # one-shot, print, and exit iki i i i i i li d d l iki l i i
Releases 25
2 days ago

---

## Page 11

+ 24 releases
## Packages
No packages published
Contributors 94
+ 80 contributors
## Languages
TypeScript 96% Python 2.4% JavaScript 1.3% CSS 0.3%