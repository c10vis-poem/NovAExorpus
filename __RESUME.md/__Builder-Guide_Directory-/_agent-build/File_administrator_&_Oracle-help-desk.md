<!-- Converted from File_administrator_&_Oracle-help-desk.pdf — 3 pages -->

## Page 1

📂 Profile 1: File Administrator Configuration
yaml#
# Æsop-Xi Execution Protocol: File Administrator Profile Configuration # Profile Target: Structural Repo Housekeeping & Manifest Mutation # ====================================================================
====================================================================
profile: id: "file_administrator_v1" codename: "NovusÆxenti-Housekeeper" purpose: "Automated codebase sanitization, raw-to-markdown parsing, and manifest indexing"
engine_runtime: core_model: "glm-5.2"
| " | try:\n", |
|---|---|
| backend_driver: "native-libc-cpu" | # Saves the heavy NPU for active chat inference |
| cpu_priority: "low_background_ionice" | # Prevents disk crawling from stuttering your GUI tile |
| context_window_ceiling: 8192 | # Tight window for rapid stream parsing |
backend_driver: "native-libc-cpu" # Saves the heavy NPU for active chat inference cpu_priority: "low_background_ionice" # Prevents disk crawling from stuttering your GUI tile context_window_ceiling: 8192 # Tight window for rapid stream parsing
hardware_routing: npus: allow_hexagon_access: false # Hard boundary set by Æsop-Xi thermals: max_allowable_temp_celsius: 42 throttle_action: "pause_execution"
memory_layer_binding: episodic: provider: "none" # Housekeeping doesn't need personal memory semantic: provider: "local_directory_map" target_vault: "novae-xorpus/" # Full sight across your master knowledge corpus allow_write_mutation: true # Permissions to turn raw docs into clean markdown
plugin_allocations: - id: "local_fs_crawler" path: "skills-and-capabilities/early-trend-scraper/stack_analyzer.py" permissions: ["read", "write", "delete_stale"] - id: "sha256_hasher" path: "novaexopia/openwiki-tui-harness/src/plugins/hasher.py" permissions: ["read"]

---

## Page 2

enforce_aesop_xi_rules: true concurrency_policy: "YIELD_TO_NPU_INFERENCE" # Instantly sleeps if Œræcle calls for NPU cycles output_format_constraint: "strict_jsonl" master_index_hook: "novae-xorpus/master_manifest.jsonl”
====================================================================
📂 Profile 2: Œræcle Help Desk Configuration
#yaml==================================================================== # Æsop-Xi Execution Protocol: Œræcle Help Desk Profile Configuration # Profile Target: Interactive Troubleshooter & Tech Oracle # ====================================================================
profile: id: "oeracle_helpdesk_v1" codename: "Œræcle-Oracle" purpose: "On-device hardware/software troubleshooting, PDF manual digestion, and error cross-referencing"
engine_runtime: core_model: "qwen-3.5-9b-gguf-q4_0" backend_driver: "qairt-htp-hexagon-npu" # Dual-NPU Tandem Hexagon route via Genie X HTP SDK kotlin_bridge_lib: "librc_kotlin_kernel" # Llama.cpp Kotlin backend hook context_window_ceiling: 32768 # Deep context for multi-page manual mining
hardware_routing: npus: allow_hexagon_access: true allocation_floor_gb: 5.2 # Preserves RAM from the Android OOM killer via Laptop Trick thermals: max_allowable_temp_celsius: 45 # Higher limit allowed under video game SDK flags throttle_action: "fallback_to_openrouter" # Switches to cloud fallback instead of crashing mid-task
memory_layer_binding: episodic: provider: "mem0" # Tracks user preferences and historical sessions protocol_type: "ob1_static_protocol" # Restricts history via time-slice constraint proofs

---

## Page 3

provider: "vector_knowledge_graph" target_vault: "data_vault_sandbox/personal_knowledge/" # Reads manual PDFs and forum crawls allow_write_mutation: false # Read-only boundary (cannot overwrite manuals)
plugin_allocations: - id: "pdf_miner_extractor" path: "novaexopia/mcp_connectors/filesystem_mcp/pdf_parser.js" permissions: ["read"] - id: "url_web_scraper" path: "skills-and-capabilities/early-trend-scraper/daily_scraper.py" permissions: ["read", "network_fetch"]
orchestration_guardrails: enforce_aesop_xi_rules: true concurrency_policy: "ACQUIRE_NPU_LOCK" # Takes absolute priority over background swarms output_format_constraint: "conversational_voice_ast" zero_memory_sandbox_hook: "novus-aexenti/nope_databank/" # Volatile data clearance route