<!-- Converted from What Is Graphify Self Graph - Google Search.pdf — 12 pages -->

## Page 1

AI Mode All Images Videos News More
what is graphify self graph
5:32AM
Graphify is an open-soure tool that transforms a project folder or codebase into a searchable, multi-modal knowledge graph for AI coding
assistants. Graphify +2
A "self graph" or self-updating/self-learning aspect in this context refers to how Graphify and complementary tools (like code-review-graph) build persistent, incremental, and structured memory of a project that updates as code or files change, rather than forcing AI agents to re-read raw files or drift
locally. DEV Community +2
### 📊 Key Features of Graphify
Token Reduction: Cuts token usage by 70–90% by providing structural maps instead of raw file dumps.
Multi-Modal Support: Parses code, documentation, PDFs, diagrams, and audio/video transcripts into one map.
Community Detection: Uses clustering algorithms (like Leiden) to group code into logical subsystems.
interactive graph.html visualization.www.kevinkinnett.com +5
Would you like to know how to install and configure Graphify for an assistant like Claude Code or Cursor, or do you need help setting up incremental updates?
DEV Community
Graphify + code-review-graph: Build a Self-Updating Knowledge Graph for Claude ...

---

## Page 2

Graphify — converts your folder into a queryable knowledge graph with community detection, Obsidian-compatible reports, and cross-
AI Mode All Images Videos News More
www.kevinkinnett.com
What Graphify actually does. Graphify is not just a vector index with a new label on it. The docs position it as a real graph buil...
Graphify
Graphify is a multi-modal knowledge graph builder created for AI coding assistants such as Claude Code, OpenAI Codex and OpenCode.
Show all
# Does that have a CLI my graphify self-craft rgz
5:36AM
# Yes, Graphify has a full Command Line Interface (CLI). After installing, you
# interact with it directly in your terminal using the single-letter command
graphify .Medium· Roan Brasil M… +1
# If you are seeing or downloading a file like graphify-self-graph.tar.gz from
# source mirrors (like SourceForge), that is simply the compressed archive containing
the source code distribution. SourceForge
# 🛠Quick Installation Gotcha
# The most critical thing to watch out for is that the official Python package package
# is distributed on PyPI under a double-y name, graphifyy , but the final terminal
command is singular ( graphify ):Medium· Roan Brasil Mont…
# bash
# Recommended installation via uv or pipx
uv tool install graphifyy
# or
pip install graphifyy

---

## Page 3

Use code with caution.
AI Mode All Images Videos News More
## 💻Using the CLI for Self-Updating Graphs
Once installed, you don't have to rely entirely on an AI assistant slash command; you can manage your persistent project graphs manually from the terminal using the Graphify CLI Command Reference:
Build/Update the graph incrementally:
## bash
graphify ./your-project-dir --update
Use code with caution.
Keep the graph fresh automatically via Git hooks:
## bash
graphify hook install
Use code with caution.
(This wires up post-commit and post-checkout triggers so your codebase memory updates automatically whenever code shifts).
Exporting to an Obsidian vault for visualization:
## bash
graphify ./your-project-dir --obsidian
Use code with caution.
Graphify
Are you trying to extract the .tar.gz source package manually, or would you like help setting up the terminal Git hooks so the graph updates itself when you commit code?

---

## Page 4

AI Mode All Images Videos News More
Graphify
Every Graphify command, grouped by intent. All commands are callable from your AI coding assistant as a slash command ( /graphify ...
Medium · Roan Brasil Monteiro
First, the gotcha: the PyPI package is graphifyy , with two y's. This trips up almost everyone on the first install, so let's get ...
DEV Community
This guide walks through installing both tools, connecting them to any AI coding agent — Claude Code, Cursor, Gemini CLI, Windsurf...
Show all
# And how can I set that up with my notebook LMPY skills and
# my Obsidian vault that I have in hooked my repo and the …
5:37AM
# To connect Graphify's CLI with your Jupyter Notebooks ( LMPY / Langchain-Meta
# Python workflows) and sync it seamlessly with an Obsidian vault linked to your
# repositories, you need to configure an automated pipeline.
# 1. Configure the GraphifyCLI for Obsidian
# Graphify includes a native markdown export engine designed to generate
# formatted notes, frontmatter tags, and internal wiki-links ( [[Note]] ) directly into
# an Obsidian vault directory.
# Run the CLI targeting your active repository and point the output directly to your
# local Obsidian vault folder:

---

## Page 5

AI Mode All Images Videos News More
graphify ./your-repo-folder --output-dir /path/to/your/Obsidian/Vault
Use code with caution.
### Automate with Git Hooks: To ensure your Obsidian vault updates every time
### you commit code in your repo, install the Git hook:
## bash
cd ./your-repo-folder
graphify hook install --output-dir /path/to/your/Obsidian/Vault/Co
Use code with caution.
## 2. Connect Notebooks to the Knowledge Graph
### To utilize these graph outputs inside your Jupyter Notebooks ( .ipynb ) for custom
### LLM prompts, agent memory, or data analysis, you can parse the exported graph
### data programmatically. Graphify saves structural details in a graph.json file.
### You can load and query this map inside your notebook using standard Python
### logic:
## python
import json
import os
# Load the graph database exported by the CLI
graph_path = "/path/to/your/Obsidian/Vault/Codebase-Graphs/graph.json
with open(graph_path, "r") as f:
code_graph = json.load(f)
# Quick function to fetch dependencies for a specific file/module
def get_file_context(file_name):
nodes = code_graph.get("nodes", {})

---

## Page 6

return nodes.get(file_name, "Module not found in graph.")
AI Mode All # Example: InjectImagesthisVideosstructureNewsintoMoreyour local LLM context window
print(get_file_context("auth_service.py"))
Use code with caution.
# 3. Integrating with the Obsidian Official Skills Repo
# If you are linking this setup to community plugins or tools within official Obsidian
# community repositories (such as local AI plugins, canvas generators, or dataview
# configurations), ensure your Graphify configuration matches these settings:
Integration
| Element | Configuration / Step |
|---|---|
| Frontmatter | Use --include-tags in the CLI to prepend metadata properties that |
| Tags | Obsidian plugins look for. |
| Obsidian | Graphify can output an abstract graph layout. You can point canvas |
| Canvas | plugins to parse the generated graph.json to draw visual connections |
Element Configuration / Step
 
Dataview Ensure your target output folder is inside your vault root so Dataview
Queries indices can read the automatic Markdown reports
( GRAPH_REPORT.md ).
# Would you like help writing a custom bash script to automate running the
# notebook execution right after Graphify updates your Obsidian vault, or do you
# need the exact CLI parameters to filter out specific folders like node_modules or
.venv ?
# I didn't say Jupiter notebook I said notebook lmpy it's official
# skills repo for Notebook LM

---

## Page 7

5:39AM
My apologies for misreading that—you are referring to notebooklm-py, the
unofficial Python API and agentic skill layer for Google NotebookLM (Gemini
Notebook), paired with an agent framework like Claude Code.
To connect your codebase Graphify tool, your Obsidian Vault, and notebooklm-
py inside your agent's skills ecosystem, you can establish an automated data
pipeline.
## 🪵The Integration Pipeline Architecture
[ Your Repository ]
│
▼ (Run Graphify CLI)
[ Obsidian Vault ] ◄─── (Visualized by Agent Skill Graph Plugin)
│
▼ (Run notebooklm-py CLI / Skill Ingestion)
[ Google NotebookLM ] ◄── (Source-grounded querying via AI Agent)
## Step 1: Export your Codebase Map to your Obsidian Vault
Graphify converts your project structure into Obsidian-ready Markdown notes with
cross-linked tags. Route your Graphify build output directly into your active
Obsidian vault directory: YouTube· Chase AI
## bash
graphify ./your-repo --output-dir /path/to/your/Obsidian/Vault/Codeba
Use code with caution.
Tip: Install a git hook ( graphify hook install ) so Graphify automatically rewrites
these markdown files every time you commit code.DEV Community

---

## Page 8

## Step 2: Ingest Graphify's Markdown Notes into NotebookLM
Because Google NotebookLM accepts source documentation to ground its RAGAI Mode All Images Videos News More
mechanism, you can use the notebooklm-py CLI to automatically upload the highly compressed, token-saving Markdown documents created by
Graphify. Korben +1
In your terminal or notebook environment, initialize and feed the Graphify notes
folder to a designated notebook: Medium
## bash
# Auth into your Google account (runs one-time browser login setup) notebooklm login
# Create a notebook for your project architecture notebooklm create "My Project Graph Architecture"
# Bulk add the Graphify markdown folder from your Obsidian vault as a notebooklm source add "/path/to/your/Obsidian/Vault/Codebase-Graph/"
Use code with caution.
Now, NotebookLM has full, token-efficient structural awareness of your codebase without bloating its context window with thousands of lines of raw
code. YouTube· Charlie Automat…
## Step 3: Map your Agent Skills in Obsidian
To track your agent skills (like the notebooklm-skill or standard agent tools), you can map them natively in Obsidian using tools from the community
ecosystem. Obsidian Community
1. Download the Agent Skill Graph Plugin repository and place/symlink it into your vault's hidden plugin directory ( .obsidian/plugins/obsidian-skill-graph ).
2. Point your vault folder configuration to your agent’s local installation path where the skills live (e.g., ~/.claude/skills/ if using Claude Code).
3. Enable the plugin in Obsidian's settings. When you open your vault's Graph View, your custom code execution workflows and notebooklm skill blocks will

---

## Page 9

# render as colored, structured nodes alongside your project
| files. | Obsidian Community |
|---|---|
| AI Mode   All |   Images   Videos |
# Step 4: Querying Grounded Code Data via your AI Agent
# Once fully linked, your coding assistant uses the notebooklm skill to communicate
# with Google. Instead of parsing raw code repositories, it requests high-level maps
directly from the NotebookLM backend: Medium
# bash
# In your terminal agent (Claude Code / OpenClaw):
"Hey, check my notebook lm skill and tell me if auth_service.py has a
Use code with caution.
# The agent taps into the notebooklm-py skill structure, pulls down the exact source
# citation from your Google notebook, and references it safely without
hallucination. Medium +1
# Would you like help writing a single Bash/automation script that hooks into your
# Git workflow to rebuild the Graphify docs, trigger notebooklm-py folder updates,
# and push everything to your vault automatically, or do you need help configuring
# the SKILL.md format for your environment?
GitHub
A Comprehensive Google Gemini Notebook Skill & Unofficial Python API. Full programmatic access to NotebookLM's features—including ...
Reddit · r/ClaudeAI
Part 3 - Setting Up Claude Code. Alright, the structure's in place. Time to bring in the AI. This part's quick, install, connect, ...
Korben

---

## Page 10

Google has never released a public API for NotebookLM , its tool that turns your AI Modedocuments into podcasts, quizzes, and other AI-ge...All Images Videos News More
Show all
# Let's do the skill MD first before we do the other one and then
# make that for my open Wiki agent openwiki tui in my termina…
5:42AM
# Here is the SKILL.md specification tailored specifically for your terminal’s
OpenWiki TUI agent. Regolo.AI +1
# This definition instructs your agent on how to manage the multi-layered knowledge
# base, bridging Graphify's structural map, Obsidian's visual storage, and
# notebooklm-py's high-level semantic retrieval without overwhelming its context
footprint. LangChain
# Save this file directly to your system's agent instructions folder (e.g.,
~/.openwiki/skills/notebooklm-sync.md or your workspace root).
# markdown
# Name: notebooklm-sync
# Description: Synchronizes structural codebase maps with Google Note
# Trigger Phrases: "update notebooklm", "sync wiki docs", "refresh co
## System Context & Strategy
You are the OpenWiki TUI local terminal agent. Your goal is to keep c
1. **Graphify:** Extracts token-reduced structural files and JSON gra
2. **Obsidian Vault:** Houses versioned, human-readable visual markdo
3. **NotebookLM (via notebooklm-py):** Acts as the remote, high-capac
Never read raw repository folders directly for global architecture ta
---
## Required Environment Setup
Before executing any tools, verify the availability of these CLI bina
- `graphify` (Python package: `graphifyy`)

---

## Page 11

- `notebooklm` (Python package: `notebooklm-py[browser]`)
AI Mode--- All Images Videos News More
## Core Agent Workflows
### Workflow 1: Absolute Synchronization (Build & Push)
When requested to update, sync, or initialize the documentation stack
1. **Run Graphify Mapping:** Extract code metadata directly into the
```bash
graphify ./ --output-dir "${OBSIDIAN_VAULT_PATH}/Codebase-Graph" -
```
2. **Authenticate with Google NotebookLM:** Check session state or pr
```bash
notebooklm status || notebooklm login
```
3. **Upsert Document Corpus:** Look up or create the project-specific
```bash
# Identify or initialize the target notebook container
NOTEBOOK_ID=$(notebooklm list --json | grep -i "Codebase Graph" |
if [ -z "$NOTEBOOK_ID" ]; then
NOTEBOOK_ID=$(notebooklm create "Codebase Graph Architecture"
fi
# Sync the token-saving Graphify documentation output
notebooklm source add "${OBSIDIAN_VAULT_PATH}/Codebase-Graph/" --n
```
### Workflow 2: Deep Grounded Architecture Querying
When the user asks architecture questions via the OpenWiki TUI ("Wher
1. Intercept the prompt. Do **not** run local grep commands over the
2. Dispatch a precise semantic lookup directly to the target `noteboo
```bash
notebooklm chat prompt --message "${USER_PROMPT}" --notebook-id "$
```
3. Filter the response, preserve all Google NotebookLM source citatio
---
## Output Contract & Validation
- **Metadata Protection:** Never overwrite frontmatter formatting hea
- **Fail-Safe Constraints:** If `notebooklm-py` reports a connection

---

## Page 12

Use code with caution.
AI Mode All Images Videos News More
# Now that the SKILL.md template is defined, should we build the Git automation
# script to wire this sync flow directly into your code commits, or do you need help
# assigning your local environmental vault paths for the openwiki TUI
# configuration?
LangChain
OpenWiki follows that model. It generates a repo wiki, then updates your agent instruction files with a reference to that wiki. Fr...
Regolo.AI
Without flags, OpenWiki opens a TUI chat (built with Ink/React) where you converse with an agent that has full repo context: openw...
Reddit · r/claudeskills
... generates and maintains documentation for your codebase in an openwiki/ directory. The prompts behind it are genuinely good (s...
Show all