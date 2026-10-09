---
title: "unsloth_studio_local_ui_setup.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/02_MY_ORIGINALS/unsloth_studio_local_ui_setup.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Unsloth Studio & Local UI Setup
1. System Overview & Architecture
Unsloth Studio provides a standalone local web user interface (UI) and orchestration CLI for
training, fine-tuning, and deploying large language models (LLMs) on consumer hardware
(Windows, Linux, WSL, and macOS) without requiring cloud GPU clusters.

-​
Local Host Default: http://127.0.0.1:8888
-​
Network Interface: Pass -H 0.0.0.0 to allow external device/LAN connections (e.g.
tablet or phone access).
-​
Secure Remote Tunneling: Launch via unsloth studio --secure to generate an
encrypted Cloudflare HTTPS tunnel with zero-config port forwarding.


2. Installation Runbook
macOS, Linux & WSL
# Automated install script (configures isolated environment and packages)

curl -fsSL https://unsloth.ai/install.sh | sh

# Launch Unsloth Studio on local port 8888

unsloth studio -p 8888 -H 0.0.0.0
Windows (PowerShell)
irm https://unsloth.ai/install.ps1 | iex
Isolated Developer / Staging Location
To prevent environment collisions with other agent runtimes, set UNSLOTH_STUDIO_HOME:

UNSLOTH_STUDIO_HOME="$HOME/.unsloth_studio" ./install.sh --local

UNSLOTH_STUDIO_HOME="$HOME/.unsloth_studio" unsloth studio -p 8888




3. Unsloth Start: Agent-to-Model Linking
Unsloth provides the unsloth start command to bind local models directly to command-line
AI agents without manual reverse-proxy setup:

# Connect local model to Claude Code CLI

unsloth start claude

# Connect local model to Hermes 3 Agent

unsloth start hermes

# Connect to OpenAI Codex / OpenClaw

unsloth start codex

unsloth start openclaw


4. Visual Data Recipes
Unsloth Studio includes a node-based visual workflow editor for data transformation:

1.​ Ingest raw PDFs, CSVs, and markdown documentation.
2.​ Clean, filter, and extract structured QA datasets.
3.​ Export directly to pre-tokenized training buffers for QLoRA and GRPO reinforcement
learning.
