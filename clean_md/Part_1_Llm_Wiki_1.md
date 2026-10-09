---
source: ## Part 1꞉ Llm Wiki (1).txt
type: condensed
condensed_from: NovA-Corpus/condensed/master-system-orchestration-matrix (2026-08-20)
original_moved_to: Merovingian's_keep/_salvage/NovA-Corpus/originals/
---

# AESOP XI: Master System Orchestration Matrix

## Part 1: The Consolidated Master README (/master_build-guide/README.md)

Unifies hardware topologies, the corrected role of OB1 and the Reasoning Bank, and the final operational parameters for the system. Operating infrastructure: NovÆcopia / NovusÆxenti Engine.

### 0. Operational Core Law: The Horizons UI Dependency

The Horizons UI native Kotlin/Java APK is the absolute framework foundation of this computing mesh. No local model can load onto the Snapdragon 8 Elite NPU, no bare-metal voice pipeline can process audio, and no screen-vision tool can execute frame context if Horizons UI is inactive. All configuration parameters, memory layers, and routing architectures serve strictly to support operations initiated via Horizons UI.

### 1. Hardware Node Topology & Mesh Integration

Ad-hoc peer-to-peer network connected over wired data interfaces and Tailscale tunnels:

- **Node Alpha (The Mobile Engine) [Moto RAZR Ultra 2025]**: Primary on-device controller. Snapdragon 8 Elite (Gen 4) SoC, Hexagon NPU (v.79), 40+ INT8 TOPs. 16GB total RAM, 8.0–11.5 GB sandboxed for local model weights. Houses the native Horizons UI APK, Moonshine Small ONNX (STT), and Kokoro-82m/Sherpa ONNX (TTS) voice engines.
- **Node Beta (The High-Compute Core) [Nvidia Jetson Orin Nano Super]**: Headless Ubuntu server, 8GB RAM, 500+GB NVMe storage, CUDA tensor pipelines pushing 60–70 TOPs. Hosts global vector storage engines, heavy background reasoning models, and the local OB1 Postgres backend server.
- **Node Gamma (The Display Station) [Rubik Pi 3 Dragonwing]**: Thundercomm/Qualcomm SoC, 14+ TOPs, dual-monitor terminal workstation via high-speed hardware data ribbons.

### 2. The Asymmetric Dual-Model Context & Memory Stack

All user interactions, device inputs, and tool execution paths run through a Dual-Model Asymmetric Workflow, bare-metal on Node Alpha:

```
[ HORIZONS UI INGRESS CONDUIT ]
            │
            ▼
[ OMNI ROUTE CONTEXT DISPATCHER ]
            │
   ┌────────┴────────┐
   ▼                  ▼
[ EXECUTOR CORE ]  [ QUERY ENGINE ]
(Local Small)      (Local Large)
   │                  │
   ▼                  ▼
[ mem0 ]           [ OB1 ]
(Episodic State)   (Knowledge Base)
```

1. **The Local Small Execution Agent** — continuously cycles to evaluate immediate tasks/actions. Hooks into mem0 for short-term user preferences, temporary state variables, rolling habit keys. Restructures raw inputs into optimized meta-prompts before anything touches external models. Honey+for-Devs governs output on most frontier models and any agents not subject to the Aesop-Xi RLVR Protocol.
2. **The Local Large Query Model (Qwen 3.5 9B GGUF Q4_0)** — dedicated to technical documentation, guides, and heavy technical text. References OB1 (Open Brain Protocol) over the local Postgres instance, alongside Reasoning Bank, Graphify, Claude-Video, Open Code Review, and notebooklm-py, to pull deep reference contexts without flooding active context windows.

### 3. Ground-Truth Development Priority Sequence

Zero-trust file safety — lower tiers stay locked until upper phases are human-validated:

1. **Priority 1: Global Data Curation & Architecture (current phase)** — gather, clean, manually sort raw technical text (Qualcomm QAIRT SDK, Android Media, Unsloth, Llama Server) into master file vaults.
2. **Priority 2: Skill Building Schemas & Directions Layers** — formalize strict JSON validation rules turning raw text into modular tool files; define how OB1/Reasoning Bank call the data engines.
3. **Priority 3: Local Workspace Infrastructure & First Repo Bootstrap** — initialize `file-management-and-skills/`; deploy local markdown vaults, `llm_wiki.md` tracker, Termux Open Wiki CLI/housekeeper script to sweep Markor, Obsidian, and Drive folders.
4. **Priority 4: Emulated Runtime Loop Validation & Data Routing** — local testing sandbox via on-device Claude Code in Termux; simulate mem0/Omni Route; map model weights, memory constraints, data paths before writing app source.
5. **Priority 5: Horizons UI App Deployment & Model Experimentation** — fork `horizons-ui-v1.2`; write native Java/Kotlin to activate NPU offload channels, local Llama server, screen vision, voice tools; test bare-metal on Snapdragon NPU; code deep recovery loops.
6. **Priority 6: Network-Wide Integration & Sovereign Scale** — finish Horizons UI, flash Jetson/Rubik Pi, route the Tailscale mesh, isolate the out-of-band Red Agent Auditor pipeline.

## Part 2: The Data Curation & Skills Manual (/file-management-and-skills/README.md)

Target Data Curation, System Schemas, & Tool Generation Guidelines. Architectural subsystem for Priority 1 & 2.

### 0. Operational Mandate: Strict Output Isolation

This directory is the central intelligence library and verification foundry for the network. All downstream building models share read-access to reference files here; no model can write/update files without a manual human review pass.

### 1. Directory Tree & Global File Partitions

```
file-management-and-skills/
├── target-docs-curation/          # Core Technical Knowledge Vault
│   ├── qualcomm-qairt-sdk/        # HTP specs, quantization guidelines, NPU pathways
│   ├── android-media-assistant/   # System alert structures, camera frameworks, gaming SDK hooks
│   ├── llama-kernel-ggml/         # GGUF weight configs, librc runtimes, local servers
│   └── unsloth-fine-tuning/       # Low-level dataset parameters & token formatting rules
├── skill-construction-factory/    # Standardized Tool Conversion Environment
│   ├── base_skill_guideline.md
│   ├── skill_onboarding_schema.json
│   └── compiled_capabilities.jsonl
├── reasoning-bank-ledger/         # Multi-Model State Tracking Vault
│   ├── active_execution_paths.json
│   └── baseline_recovery_matrix.md
└── master_blueprint.txt           # Global system verification registry index
```

### 2. Hardware-Abstracted Middleware Configuration

- **OB1 (Open Brain Protocol) Base Layer** — local Postgres on Node Beta, unified MCP mapping engine. Translates heavy technical reference text into semantic vectors so the Large Query Model can pull detail without flooding context.
- **Reasoning Bank Ledger** — persistent JSON tracking DB at `reasoning-bank-ledger/active_execution_paths.json`. Records fractional thoughts/tool selections/step progress so a crash or timeout can resume exactly where it left off.
- **mem0 Layer Caching** — localized, low-latency episodic tracking cache. Records temporary user adjustments, short-term conversational variables, personal habit keys; feeds the Local Small Execution Agent for personalized meta-prompts.

### 3. Skill Conversion & Context Extraction Laws

1. **Sovereign Decoupling** — a skill does exactly one thing; storage-folder code cannot also reference network sockets or cloud endpoints.
2. **Asymmetric Context Routing** — query `.jsonl` for direct execution/bash/terminal/tool calls (stream line-by-line via regex); scan raw `.txt` for debugging/kernel/hardware-math questions (parse every word verbatim).
3. **Web-Tool Verification** — if an argument needs live-repo or online-doc validation, pause, structure a secure JSON-RPC scrape token, pass to the Horizons UI WebView container.

## Part 3: The Native Application Manual (/horizons-ui-v1.2/README.md)

Target Version v1.2. Compilation environment: Java/Kotlin native Android SDK APK.

### 0. Operational Core Law: The Sovereign Entry Point

Horizons UI is the physical heart of the entire agentic neuro-mesh — not a secondary dashboard. It is the central permissions gatekeeper, NPU allocation manager, and low-latency audio capture harness. No local model weight loads onto the Hexagon NPU, and no automated tool script executes, if this application environment is compromised or offline.

### 1. Technical Framework Architecture & Drivers

**The Bare-Metal Voice Subsystem** — the stock Termux audio pipeline needs complex, inefficient workarounds (high latency, broken speech capture). Fix: Horizons UI handles voice processing directly on bare metal — Silero VAD wrapper monitors mic input; on detection, audio pipes into a Whisper Small ONNX engine for STT; TTS via Kokoro-82m/Sherpa ONNX over a local Llama Server. Custom compiled pathway: `Llama -> QAIRT ModelPath -> GGML Layer -> Kotlin Kernel -> librc Runtimes`, landing on the Snapdragon 8 Elite Hexagon NPU via the Qualcomm HTP SDK — used only for the execution and query models.

**OS Allowance & Hardware Boost Hooks** — the APK registers as the device's Default Assistant Application (Screen Vision Analysis via accessibility keys); hooks into Android's Performance Hint API / Vendor Gaming SDKs for high-priority CPU/GPU scheduling and thermal-limit unlock during inference; integrates an active secure Android shell terminal wrapper for real-time system monitoring from inside the main app screen.

### 2. Application Component Directory Mapping

```
horizons-ui-v1.2/
├── app/src/main/java/com/horizons/ui/
│   ├── core/       # MainActivity, UI lifecycle, Home Screen tile views
│   ├── voice/      # Silero VAD, Moonshine ONNX, Kokoro audio drivers
│   ├── vision/     # Android Media SDK screen capture & vision matrices
│   └── services/   # Background daemons handling model offloads & web scraping
├── app/src/main/jni/               # C/C++ Native Libs Layer
│   ├── qairt-htp/                  # Qualcomm HTP SDK headers, modelpath bindings
│   └── ggml-kernel/                # Native GGML, GGUF runtimes, librc libraries
├── sandboxed-chromium/             # WebView environment for isolated internet searches
└── daemons-recovery/               # Self-healing runtime managers
```

### 3. Asynchronous Task Lifecycle & Self-Healing Daemon

```
[ Human Interaction Event / Floating Mic Tile Tap ]
            │
            ▼
[ MAIN INTERFACE UI THREAD ]  ◄═══ Zero Rendering Latency
            │  (Asynchronous Event Dispatch)
            ▼
[ BACKGROUND DAEMON THREAD POOL ]
  • Thread A: Continuous Silero VAD Audio Stream Capture
  • Thread B: Local Llama Server Token Processing
  • Thread C: Tailscale Network Sockets / Web Scraper
            │
            ▼
[ THE RECOVERY DAEMON WATCHDOG ]  ◄═══ Isolation Safety Net
```

**The Recovery Watchdog System (Anti-Crash Layer)** — a dedicated background recovery manager whose sole purpose is keeping the edge interface alive. If a local model or NPU kernel crashes, the recovery engine intercepts the hardware termination flag, freezes active workspace variables, and prevents app shutdown. Failback path: spins up a temporary connection via the OpenRouter API to a cloud-hosted fallback model, updates it with the latest state from the Reasoning Bank, and re-initializes the local NPU model variables silently in the background.
