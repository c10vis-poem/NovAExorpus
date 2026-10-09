---
title: "README.md — Master Federated Multi-Corpora Specification"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/02_MY_ORIGINALS/README.md — Master Federated Multi-Corpora Specification.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Federated Multi-Corpora Master
README (README.md)
Project: __NovÆxorpus(NÆX) &
___Lex-Novi-Æxentis-Copiæ
Motto: Xçineribus, in-variis-nunquam-varius,
Novi-Æxentis-Copiæ, Vincent
System Ground Truth: Æsc & Æyre • Living Truth &
Universal Memory: #d.u.m.b.a.s.s.
1. Executive Summary & Architecture Overview
This repository orchestrates a federated, multi-corpora agentic system operating across a
tri-node asymmetric mesh: Node Alpha (Moto RAZR Ultra 2025 / Snapdragon 8 Elite), Node
Beta (NVIDIA Jetson Orin Nano Super), and Node Gamma (Rubik Pi 3 Dragonwing). The
architecture strictly enforces sensory immutability, zero-trust daemon sandboxing, decoupled
background execution via loopback ADB, and sub-5ms local memory retrieval.
2. Federated Multi-Corpora Directory Layout
novae-xorpus/ (FEDERATED MASTER CORPUS ROOT & LIVING TRUTH)​
├── 📜 MAP.md                                # Top-level human
navigation ontology & concept graph​
├── 📊 master_manifest.jsonl                 # Federated SHA256 hash
table linking all child repos​
├── 📖 README.md                             # Master System
Documentation & Beginner Runbook​
│​
├── 📁 aesop-xi/                             # Core Ethical
Orchestration Protocol​
│   ├── manifest.jsonl                       # Local tier catalog​
│   ├── arbitration/                         # Resource scheduling &
agent priority arbiters​
│   ├── policies/                            # Hard boundary rules &
security clearance tables​
│   └── .incognito_red_sandbox/              # Hidden shadow
gatekeeper & isolated eval sandbox​
│​
├── 📁 novus-aexenti/                        # Reasoning Engine &
Multi-Agent Intelligence​


│   ├── manifest.jsonl​
│   ├── dual_agent_router/                   # 0.8B Triage vs 4B/9B
Query routing contracts​
│   ├── mem0_episodic/                       # Rolling in-session
habit keys & preferences​
│   │   ├── ob1_static_protocols/            # Static ground-truth
queries over Postgres/MCP​
│   │   └── vector_recall_engine.py          # Local semantic vector
index​
│   └── reasoning_bank/                      # Multi-model state
ledger & recovery flywheel​
│       ├── active_execution_paths.json      # Step-by-step
transaction ledger​
│       ├── failure_logs/                    # Structured post-mortem
failure schemas​
│       └── post_regression/                 # Rollback snapshots
preventing capability drift​
│​
├── 📁 novaexopia/                           # Native Daemons,
Runtimes & "The Claw"​
│   ├── manifest.jsonl​
│   ├── horizons-ui/                         # APK 1: Chromium WebView
frontend & chat tiles​
│   ├── aesc/                                # APK 2: Shell/Terminal
Daemon & ADB Loopback (5555)​
│   ├── aeyre/                               # APK 3: Sensory Ingress,
Silero VAD, Moonshine, Kokoro​
│   ├── openwiki-tui-harness/                # Interactive TUI Help
Desk & AST Knowledge Graph​
│   ├── modular_harnesses/                   # Execution harnesses
(Prime Agent RLM, ECC skills)​
│   └── mcp_connectors/                      # Node.js Filesystem,
SQLite, and Postgres MCP servers​
│​
├── 📁 vendor-corpora/                       # Isolated Immutable
External Libraries​
│   ├── qualcomm-qairt-sdk/                  # Dedicated Qualcomm NPU
/ FastRPC Knowledge Base​
│   │   ├── manifest.jsonl​
│   │   ├── htp-specs/                       # Hexagon v79 HTP
micro-architecture​
│   │   ├── headers/                         # libQnnHtp.so &
/dev/adsprpc-smd ioctl contracts​
│   │   └── quantization-guides/             # INT4/INT8 GEMM rules &
tensor layout bounds​
│   └── google-android-platform/             # Android OS Internal
Protocols​
│       ├── manifest.jsonl​


│       ├── system-services/                 # Foreground Service,
LMK, and AIDL architecture​
│       ├── media-gaming-sdk/                # Frame capture &
low-latency audio pipelines​
│       └── developer-options/               # Wireless Debugging &
loopback pairing specs​
│​
├── 📁 skills-and-capabilities/              # Shared Plugin &
Analytical Library​
│   ├── manifest.jsonl​
│   ├── code-review-graph/                   # PyGraphify / Graphify
AST dependency mappings​
│   ├── notebook-lmpy/                       # Deep corpus analytical
query scripts​
│   ├── obsidian-skills/                     # Vault hygiene and
graph-sync definitions​
│   └── early-trend-scraper/                 # Web research &
telemetry intake daemons​
│​
└── 📁 data_vault/                           # Living Semantic Memory
(02_wiki_md/)​
    ├── manifest.jsonl​
    ├── concepts/                            # Atomic linked notes
(Zettelkasten)​
    ├── architectures/                       # System blueprints
connecting child repositories​
    └── entities/                            # Hardware profiles,
register maps & device contracts​

3. Subsystem Breakdown: Roles & Responsibilities
Repository / Layer
Physical Target
Primary Runtimes
Operational Role
aesop-xi
Universal Mesh
Python / Bash /
JSON
Enforces ethical
boundaries, split
execution rules, and
houses the isolated
.incognito_red_sand
box/ gatekeeper.
novus-aexenti
Node Alpha / Node
Beta
Python / SQLite /
MCP
Hosts the 0.8B/9B
model router, mem0
episodic habits, OB1
static ground truth,
and the Reasoning


Repository / Layer
Physical Target
Primary Runtimes
Operational Role
Bank ledger.
novaexopia
Node Alpha (Moto
RAZR)
Kotlin / Java / C++
FastRPC
Runs the decoupled
3-APK native
framework (Horizons
UI, Æsc terminal
daemon, Æyre
media daemon) and
DroidDesk.
vendor-corpora
Node Alpha / Node
Beta
Markdown / C++
Headers
Isolated, immutable
reference
repositories for
Qualcomm QAIRT
SDK and Google
Android internals.
skills-and-capabiliti
es
All Nodes
Python / Node.js /
CLI
Houses extracted
procedural tools (cli/,
wrappers/),
PyGraphify code
graphs, and
NotebookLM
pipelines.
data_vault
Node Alpha / Mesh
Sync
Obsidian Markdown /
TUI
Semantic knowledge
base managed via
OpenWiki CLI with
bi-directional
wikilinks and atomic
concept cards.
4. The Lean On-Device Runtime Architecture
To eliminate background terminations by the Android Low Memory Killer (LMK) and maximize
battery efficiency, the mobile runtime operates strictly on bare-metal native daemons:
●​ GenieX (Qualcomm Hexagon v79 NPU): Executes GGUF Q4_0 quantizations of Qwen
3.5 via the GGML Hexagon backend with zero-copy ASharedMemory FastRPC buffers.
LocalAI is completely purged.
●​ OmniRoute (Port 20128): Runs under Node.js LTS as an intelligent local gateway.
Conserves tokens by routing prompts dynamically across local GenieX weights and
remote APIs based on prompt cache hit rates and rate limits.
●​ Prime Agent (Prime Intellect): Persistent Python REPL driving the Recursive Language
Model (RLM) loop and the Continual Harness online adaptation framework.
●​ Decoupled Native 3-APK Topology:


○​ Horizons UI: Presentation shell, WebSocket client, and model picker.
○​ Æsc: Registered Accessibility Service / Assistant daemon executing shell
commands via ADB Loopback (127.0.0.1:5555) with UID 2000 shell privileges.
○​ Æyre: Low-latency sensory ingress daemon running Silero VAD, Moonshine ONNX
STT, and Kokoro TTS.
5. Dual Operational Modes (ECC vs. Prime Agent)
Operational Vector
Mode A: Terminal Developer
Session
Mode B: Sovereign Edge
Assistant
Primary Driver
Claude Code CLI (Desktop /
Termux Terminal)
Local On-Device Weights
(Snapdragon Hexagon NPU)
Governing Harness
ECC (Everything Claude
Code)
Prime Agent (Prime
Intellect)
Active Tool Suite
honey-crush, nexus-mapper,
ecc-planner, Pocock skills
Native Python REPL tools,
SQLite KV lookups, FastRPC
NPU calls
Harness Interaction
Autonomous developer loop
inside the Claude CLI.
Prime Agent invokes Claude
Code CLI strictly as a
discrete external tool. No
nested wrapping.
6. Beginner Runbook & Step-by-Step Initialization
1.​ Clone & Verify Submodules:​
git clone --recurse-submodules <repo-url> ~/novae-xorpus && cd
~/novae-xorpus
2.​ Establish Local ADB Loopback (One-Time Pairing on Node Alpha):​
# Enable Wireless Debugging in Developer Options, then pair:​
adb pair 127.0.0.1:<PAIRING_PORT> <PAIRING_CODE>​
adb connect 127.0.0.1:5555
3.​ Launch the NPU Hot-Swap & Inference Daemon:​
python3
~/novae-xorpus/04_skills_runtime/extracted_tools/wrappers/npu_mana
ger.py
4.​ Start OmniRoute Local Gateway:​
omniroute --port 20128 --config
~/novae-xorpus/novaexopia/modular_harnesses/omniroute_config.json
5.​ Run Zero-Trust System Housekeeper & Audit Sweep:​
bash
~/novae-xorpus/04_skills_runtime/extracted_tools/cli/system_housek
eeper.sh
6.​ Open the Æsc Interactive Control Panel:​


bash
~/novae-xorpus/04_skills_runtime/extracted_tools/cli/agent_panel.s
h
7. Associated Canonical Master Specifications
For exhaustive technical contracts, register layouts, and schema definitions, refer to the
following canonical documents:
●​ 00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md — Apex system
architecture, directory schema, tier access rules, and bash scaffolding.
●​ 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md — Decoupled 3-APK framework,
ADB loopback, and tri-node hardware specifications.
●​ 02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md — Ubiquitous #d.u.m.b.a.s.s. memory
engine, Mem0, OB1, SQLite, and Continual Harness.
●​ 03_DUAL_OPERATIONAL_HARNESS_AND_MCP_SPEC.md — Mode A (ECC) vs Mode
B (Prime Agent), MCP infrastructure, and PyGraphify code graphs.
●​ 04_ON_DEVICE_INGESTION_AND_W5H_FRAMEWORK.md — W5+H matrix,
Markdown-first ingestion, and atomic JSONL marker generation.
