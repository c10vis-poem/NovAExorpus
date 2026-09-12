---
source: 🌌 The Master Æsop-Xi - NovÆ-Core Repository Map-.docx
type: docx
cleaned: 2026-09-10
cleaner: tools/clean.py (mutool)
---

🌌 The Master Æsop-Xi / NovÆ-Core Repository Map

novae-xorpus/                                  # 📚 THE UNIVERSAL TRUTH & MASTER CORPUS ROOT

├── master_manifest.jsonl                     # 🚀 The Master Cross-Repository Index (JSONL streaming)

│

├── aesop-xi/                                  # ⚖️ UNIVERSAL ORCHESTRATION LAYER (Ethical Core)

│   ├── manifest.jsonl

│   ├── arbitration_engine.py                  # Inter-agent resource & priority steering rules

│   ├── policies/                              # Hard boundaries, permissions, and tool rules

│   │   ├── tool_usage_guardrails.json         # Explicit constraints on what tools can alter code

│   │   └── security_clearance.yaml            # Defines OAuth boundaries between agents and repos

│   └── hardware_throttler.py                  # Checks NPU thresholds; manages hardware allocations

│

├── novus-aexenti/                             # 🧠 COGNITIVE MOE ENGINE (The Multi-Agent Brain)

│   ├── manifest.jsonl

│   ├── dual_agent_router/                     # Query Model vs. Executor Model handshake logic

│   │   ├── query_analyzer.py                  # Directs incoming strings to specific vectors

│   │   └── executor_bridge.py                 # Formats tasks for the execution agents

│   │

│   ├── mem0_episodic/                         # MEM0 live experience tracking infrastructure

│   │   ├── ob1_static_protocols/              # Session forks, time-slice proofs, and constraints

│   │   └── vector_recal_engine.py             # Pulls historical chat events mid-session

│   │

│   ├── reasoning_bank/                        # 📈 SYSTEM FLYWHEEL (RLVR Model Training Workspace)

│   │   ├── manifest.jsonl

│   │   ├── failure_logs/                      # Tracked JSONL files containing model errors

│   │   ├── reward_variables/                  # Strict parameters measuring model efficiency

│   │   ├── frontier_traces/                   # Logs detailing actions taken by heavy API models

│   │   └── post_regression/                   # ⏪ POST REGRESS ZONE (Ensures updates don't break old skills)

│   │       ├── baseline_tests/                # Standardized capability tests for the swarms

│   │       └── regression_audit_report.jsonl  # Keeps track of accuracy degradation over model versions

│   │

│   └── nope_databank/                         # 🕳️ ZERO-MEMORY LAYER (Isolated Sandboxed Workspace)

│       ├── manifest.jsonl                     # Volatile index (wipes/expires without persistence)

│       └── raw_intercept/                     # Temporary landing pad for scripts bound for GCP

│

├── novaexopia/                                # 🦾 THE "CLAW" (Harness Runtimes & Multi-APK Architecture)

│   ├── manifest.jsonl

│   │

│   ├── openwiki-tui-harness/                  # 📟 UNIFIED TERMINAL USER INTERFACE SHELL

│   │   ├── src/                               # Shared TUI layout, views, inputs, and render code

│   │   └── config_profiles/                   # 🎭 ONE ENGINE, DUAL RUNTIMES

│   │       ├── file_administrator.yaml        # Profile A: Structural database housekeeper parameters

│   │       └── oeracle_helpdesk.yaml          # Profile B: Interactive troubleshooting oracle parameters

│   │

│   ├── horizons-ui/                           # 📱 TIER 1 APK: Main Graphical User Interface

│   │   ├── model_loaders/                     # Binds Qwen 3.5 9B (HTP Kernel) & 0.8B (Jeanie X SDK)

│   │   ├── ui_tiles/                          # Chat Interface tile, Terminal tile, File Picker tile

│   │   └── connectivity/                      # WebSockets, WebHooks, and OpenRouter failback routes

│   │

│   ├── aesc/                                  # 🖥️ TIER 2 APK: System Terminal Daemon

│   │   ├── laptop_trick_tunnel/               # 🔌 ADB-to-WebSocket local Unix host bridge logic

│   │   └── npu_watchdog/                      # Real-time Genie SDK thermal & OOM monitoring loop

│   │

│   ├── aeyre/                                 # 🎙️ TIER 3 APK: Media Daemon

│   │   ├── screen_vision/                     # Real-time pixel canvas parsing & vision capture

│   │   └── voice_ast_stack/                   # Native low-latency VAD, TT, TTS, and STT pipelines

│   │

│   ├── modular_harnesses/                     # 🤖 MICRO-AGENT SWARM HARNESS EXTENSIONS

│   │   ├── ecc-edge-compute/                 # Independent computing harness for remote processing

│   │   ├── prime-agent/                       # Main local code execution/self-improvement harness

│   │   ├── ringer-notif-loop/                 # Background system notification and trigger manager

│   │   ├── hermes-soul/                       # Contextual agent rules and cognitive core settings

│   │   ├── aider-workspace/                   # Git-tracked automatic command-line workspace agent

│   │   ├── local-nanobots/                    # Container hooks for your 4 specialized micro-bots

│   │   ├── smol-agents/                       # Minimal, low-overhead script fragment generator pods

│   │   └── turbo-quant-swarms/                # Quantized reasoning models handling high-speed traffic

│   │

│   └── mcp_connectors/                        # 🔌 PLUGINS & CAPABILITIES GATEWAY

│       ├── anthropic_official/                # Local mirror of Anthropic open-source plug-in library

│       ├── custom_node_mcp/                   # Your planned custom Node.js server configurations

│       └── filesystem_mcp/                    # MCP server interface giving agents local folder sight

│

├── skills-and-capabilities/                   # 🛠️ GENERAL CAPABILITY INJECTIONS (Shared Library)

│   ├── manifest.jsonl

│   ├── notebook-lmpy/                         # Official NotebookLMPy skills repository

│   ├── obsidian-skills/                       # Official Obsidian community skill definitions

│   ├── graphify-visual/                       # Knowledge graph creation & repo visual topology map

│   ├── claude-video/                          # Video analysis and temporal sequence processing

│   ├── code-review-graph/                     # Structural graph code checking tool injects

│   └── early-trend-scraper/                   # 📡 PRE-TREND RESEARCH DAEMON

│       ├── daily_scraper.py                   # Automated cron/timer web scraper

│       ├── stack_analyzer.py                  # Evaluates changes between web logs & NovÆxorpus

│       └── trending_databank.jsonl            # Raw data logs storing pre-trend repo indicators

│

└── data_vault_sandbox/                        # 📊 LOCAL AIRGAPPED USER OBSERVATORY (Safety Sandbox)

    ├── manifest.jsonl                         # Manual staging layout index (NO RCLONE SYNC)

    ├── .obsidian/                             # Graphical metadata workspace for Obsidian/Markor

    └── personal_knowledge/                    # Hand-written notes, troubleshooting logs, user manuals
