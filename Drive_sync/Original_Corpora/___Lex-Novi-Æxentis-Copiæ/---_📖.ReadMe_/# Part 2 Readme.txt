┌────────────────────────────┴────────────────────────────┐
▼ ▼
┌───────────────┐ ┌───────────────┐
│ EXECUTOR CORE │ │ QUERY ENGINE │
│ (Local Small) │ │ (Local Large) │
└───────┬───────┘ └───────┬───────┘
│ │
▼ ▼
┌───────────────┐ ┌───────────────┐
│ mem0 │ │ OB1 │
│(Episodic State) │(Knowledge Base)
└───────────────┘ └───────────────┘
1. **The Local Small Execution Agent:** Continuously cycles in a tight loop to evaluate
immediate tasks and actions. It hooks directly into **mem0** to fetch short-term user
preferences, temporary state variables, and rolling habit keys. It restructures raw inputs into
optimized meta-prompts before anything touches external models.
2. **The Local Large Query Model:** Dedicated to processing technical documentation,
technical guides, and heavy technical text. It references **OB1 (Open Brain Protocol)** over
your local Postgres instance, working alongside **Reasoning Bank**, **Graphify**, and
**notebooklm-py** to pull deep reference contexts without flooding active context windows.
---
## 📁 3. Ground-Truth Development Priority Sequence
To ensure zero-trust file safety and prevent workspace corruption, development must progress
through these exact phases. Lower tiers remain locked until upper phases are validated by the
human:
1. **Priority 1: Global Data Curation & Architecture (Current Phase)** - Gather, clean, and
manually sort raw technical text documents (Qualcomm QAIRT SDK, Android Media, Unsloth,
Llama Server) into your master file vaults.
2. **Priority 2: Skill Building Schemas & Directions Layers** - Formalize your strict JSON
validation rules to turn raw text info into modular tool files, defining how OB1 and Reasoning
Bank call upon your data engines.
3. **Priority 3: Local Workspace Infrastructure & First Repo Bootstrap** - Initialize your
`file-management-and-skills` directory. Deploy your local markdown vaults, `llm_wiki.md`
parameters tracker, and your **Termux Open Wiki CLI/Housekeeper janitor script** to sweep
your Markor, Obsidian, and Drive folders.
4. **Priority 4: Emulated Runtime Loop Validation & Data Routing** - Set up your local testing sandbox using on-device **Claude Code** inside Termux. Run simulation loops to verify
**mem0** and **Omni Route**. Map model weights, memory constraints, and data paths to
verify your data flows are 100% compliant before writing app source files.
5. **Priority 5: Horizons UI App Deployment & Model Experimentation** - Fork a pristine branch
into a custom GitHub repository for `horizons-ui-v1.2`. Write the native Java/Kotlin codebase to
activate your NPU offload channels, local Llama server, screen vision layers, and voice tools.
Test model parameters bare-metal on the Snapdragon NPU and code deep recovery loops.
6. **Priority 6: Network-Wide Integration & Sovereign Scale** - Perfect Horizons UI, flash your
headless computing hardware (Jetson, Rubik Pi), route your Tailscale mesh network, and
isolate your out-of-band **Red Agent Auditor** pipeline.
------------------------------
## Part 2: The Data Curation & Skills Manual (/file-management-and-skills/README.md)
# 📂 File Management System & Skill Generation Engine## Target Data Curation, System
Schemas, & Tool Generation Guidelines### Architectural Subsystem: Priority 1 & Priority 2
Core---## 🚨 0. Operational Mandate: Strict Output IsolationThis directory acts as the central
intelligence library and verification foundry for the entire network. While all downstream building
models share read-access to the reference files in this repo, no model can write code or update
files here without a manual human review pass.
---## 🗂️ 1. Directory Tree & Global File Partitions
📁 file-management-and-skills/
│
├── 📁 target-docs-curation/ # Core Technical Knowledge Vault
│ ├── 📁 qualcomm-qairt-sdk/ # HTP specifications, quantization guidelines, & NPU pathways
│ ├── 📁 android-media-assistant/ # System alert structures, camera frameworks, & gaming
SDK hooks
│ ├── 📁 llama-kernel-ggml/ # GGUF weights configurations, librc runtimes, & local servers
│ └── 📁 unsloth-fine-tuning/ # Low-level dataset parameters & token formatting rules
│
├── 📁 skill-construction-factory/ # Standardized Tool Conversion Environment
│ ├── 📄 base_skill_guideline.md # Rules for creating decoupled, single-purpose tool files
│ ├── 📄 skill_onboarding_schema.json # Target JSON parameter verification model
│ └── 📄 compiled_capabilities.jsonl # Streaming instruction-tuned dataset repository
│
├── 📁 reasoning-bank-ledger/ # Multi-Model State Tracking Vault
│ ├── 📄 active_execution_paths.json # Suspended intermediate token sequences and plans
│ └── 📄 baseline_recovery_matrix.md # Rules for managing multi-model recovery daemons
│
└── 📄 master_blueprint.txt # Global system verification registry index file