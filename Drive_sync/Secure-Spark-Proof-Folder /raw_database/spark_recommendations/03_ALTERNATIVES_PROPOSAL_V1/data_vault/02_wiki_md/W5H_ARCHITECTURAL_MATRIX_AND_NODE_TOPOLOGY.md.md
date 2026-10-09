---
title: "W5H_ARCHITECTURAL_MATRIX_AND_NODE_TOPOLOGY.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/data_vault/02_wiki_md/W5H_ARCHITECTURAL_MATRIX_AND_NODE_TOPOLOGY.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

W5+H Architectural Matrix & Node Topology
Comprehensive Synthesis: Who, What, When, Where, Why, How
Derived from: W5/H-(6-files) (User explains audit.txt, Where and When.txt,
What and Why.txt, What and How.txt, Copy of Agent explanation.txt) and
4-ARCHITECTURE-cont.-(6-files).​
Status: Canonical Living Wiki Reference | Clean Markdown Layer​
Target Repository: data_vault/02_wiki_md/


1. The W5+H Ecosystem Matrix
Dimension
Architectural Specification
Real-World Hardware &
Subsystem
WHO
• Operator: Derek LeGrand
(System Architect & Sole
Deletion Authority).

• Agent Personas: Horizons
Concierge (Voice/UI), Æsc
Terminal Daemon
(Shell/ADB), Æyre Media
Daemon (Sensory VAD/TTS),
0.8B Triage Router, 9B
Executor, Home Assistant
Auditor, and Incognito Red
Gatekeeper.
Node Alpha (Motorola Razr
Ultra 2025), Node Beta
(Jetson Orin Nano Super),
Node Gamma (Rubik Pi 3),
Node Delta (GCP Cloud).
WHAT
• Sovereign, multi-tier
cognitive agent ecosystem
running local open weights
and decoupled daemons
without root or Termux
sandbox limits.
• #d.u.m.b.a.s.s. universal
memory backbone across
SQLite, PostgreSQL, mem0,
3-APK Android Suite, Local
Unix Abstract Sockets,
Tailscale Mesh, GCP Vertex
AI.


Dimension
Architectural Specification
Real-World Hardware &
Subsystem
OB1, OmniRoute, and
Reasoning Bank.

• Continuous learning loop
via asynchronous audit logs
and RLVR training.
WHEN
• Phase 1: Knowledge
Curation & Universal JSONL
Marker Indexing (Current).
• Phase 2: Tool Harness
Ingestion & Action Schemas.
• Phase 3: Repository Layout
& Multi-Agent Grill Sessions.
• Phase 4: 3-APK Native
Android Deployment.
• Phase 5: Local Dual-Model
Inference & Continuous
Improvement RLVR Loop.

• Phase 6: Multi-Node Mesh
Orchestration & Autonomous
Agent Swarm.
Phased roadmap spanning
real-time mobile execution to
scheduled cloud batch
training.
WHERE
• Edge Controller: Node
Alpha (Moto Razr Ultra 2025,
Snapdragon 8 Elite /
Hexagon v79 NPU, 16GB
RAM).
• Compute Core: Node Beta
(NVIDIA Jetson Orin Nano
Super 8GB, CUDA 60–70
TOPs, NVMe SSD).
• Workstation: Node Gamma
(Rubik Pi 3 Dragonwing,
Dual-Monitor Ribbon Display
Server).

• Cloud Pipeline: Node Delta
(Google Cloud Platform,
Peer-to-peer encrypted
Tailscale mesh with local
air-gapped Wi-Fi router
switch fallback.


Dimension
Architectural Specification
Real-World Hardware &
Subsystem
Vertex AI $1,000 credit tier,
GCS buckets).
WHY
• Eliminates mobile RAM
saturation and Android Low
Memory Killer (LMK) crashes
by decoupling UI from
execution daemons.
• Eliminates catastrophic
forgetting and prompt drift
through reset-free Continual
Harness adaptation and
immutable base anchors.

• Protects intellectual
property by separating
personal developer credits
from business workspace
storage buckets via
asymmetric IAM.
Sovereign autonomy, zero
data leakage,
high-throughput local
execution.
HOW
• Communication: Local UNIX
domain abstract sockets (\0),
Ktor/Netty WebSockets, and
ADB local TCP loopback
(127.0.0.1:5555).
• Inference Routing:
OmniRoute proxy on port
20128 applying
RTK/Caveman token
compression (15%–95%
savings) with async memory
extraction.

• Memory: mem0 (in-session
habit caching) + OB1 (static
MCP retrieval) + Reasoning
Bank
(active_execution_path
s.json).
Hardware acceleration
(Hexagon HTP FastRPC +
Jetson CUDA) and
automated scripts.




2. Multi-Node Sovereign Mesh Topology
┌───────────────────────────────────────────────────────────
─────────────┐

│ NODE ALPHA: Motorola Razr Ultra 2025 (Snapdragon 8 Elite / Hexagon v79) │

│ - 16 GB RAM (8.0–11.5 GB carved out for local GGUF weights)           │

│ - Decoupled 3-APK Native Android Suite:                                │

│   ├─ Horizons UI: Chromium WebView frontend & persistent WebSockets    │

│   ├─ Æsc: System Terminal Daemon (Local ADB loopback 127.0.0.1:5555)   │

│   └─ Æyre: Media Daemon (Silero VAD + Moonshine STT + Kokoro TTS)      │

│ - Models: Qwen 3.5 0.8B (Triage) + Qwen 3.5 9B (Executor)              │

│ - Memory: mem0 in-session episodic state                               │

└───────────────────────────────────┬───────────────────────
─────────────┘

                                    │ (Encrypted Tailscale Mesh)

                                    ▼

┌───────────────────────────────────────────────────────────
─────────────┐

│ NODE BETA: NVIDIA Jetson Orin Nano Super 8GB (Headless Ubuntu Server)  │

│ - Dedicated CUDA Core Array (60–70 TOPs), 500+ GB NVMe Storage         │

│ - #d.u.m.b.a.s.s. Core Hub: PostgreSQL 16+ with pgvector OB1 database  │

│ - Multi-Agent Home Swarm:                                              │

│   ├─ Home Assistant: Cross-Agent Auditor & daily log compiler          │



│   ├─ Red Agent Auditor: Air-gapped compliance & hallucination checker  │

│   ├─ IT Help Desk Agent: Hardware specs & diagnostic runbooks          │

│   └─ NPU / Thermal Watchdog: Cluster headroom & task-shedding daemon   │

└───────────────────────────────────┬───────────────────────
─────────────┘

                                    │ (Encrypted Tailscale Mesh)

                                    ▼

┌───────────────────────────────────────────────────────────
─────────────┐

│ NODE GAMMA: Rubik Pi 3 Dragonwing (Qualcomm SoC / 14+ TOPs)            │

│ - Dual-Monitor Ribbon Display Server & hardware keyboard hub           │

│ - System log visualizer, telemetry dashboard & DroidDesk workstation   │

└───────────────────────────────────┬───────────────────────
─────────────┘

                                    │ (Cloud Cross-Account IAM Handshake)

                                    ▼

┌───────────────────────────────────────────────────────────
─────────────┐

│ NODE DELTA: Google Cloud Platform (Enterprise Asymmetric Cloud)        │

│ - $1,000 Vertex AI Agent Builder credit pool (Personal Account)        │

│ - gs://business-vault-bucket (Business Secure Workspace)               │

│ - Heavy batch training, RLVR fine-tuning (Unsloth/GRPO), JSONL stream  │

└───────────────────────────────────────────────────────────
─────────────┘




3. The Four-Part Auditing & Trapdoor Protocol
As detailed in User explains audit.txt, the audit loop operates with four distinct
components:

1.​ On-Device Dual Agent: The live interaction tandem (0.8B Triage + 9B Executor)
generating step-by-step task executions.
2.​ Main Computer Twin Agent (Node Beta): Mirrors execution state, logs prompts, tool
calls, and outputs into daily JSONL staging buffers.
3.​ The Systems Secretary / Files Manager: Packages candidate scripts, strips
conversational boilerplate, and attempts to forward the batch to the cloud editor.
4.​ The Incognito Red Gatekeeper (The Trapdoor): Sits directly at the hand-off point. The
files manager drops the batch into the queue, but the Red Agent intercepts it inside a
sealed sandbox (.incognito_red_sandbox/), evaluating it against
nope_data_bank.json. If verified (+1.0), it moves to approved/ for cloud RLVR
training; if flawed (-1.0), it is quarantined with full error traces.
