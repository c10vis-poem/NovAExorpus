---
source: omniroute_config.yaml.pdf
type: pdf
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

#
========================================================================
======
# OmniRoute Unified Gateway & Inference Routing Configuration
# Port: 20128 | Protocol: OpenAI-Compatible /v1/chat/completions & /v1/embeddings
# Core Mission: Single-endpoint routing, token compression, and memory extraction
#
========================================================================
======

server:
  host: "0.0.0.0"
  port: 20128
  keep_alive_timeout: 120
  max_concurrent_requests: 16

token_compression:
  enabled: true
  engine: "rtk_caveman"
  target_savings_range: "15% - 95%"
  rules:
    strip_polite_phrasing: true
    abbreviate_json_keys_in_transit: true
    deduplicate_repeated_system_prompts: true
    cached_prompt_prefix_injection: true

routing_matrix:
  # 1. Edge Fast-Path (0.8B Triage & Fast Vector Filtering)
  triage:
    primary:
      provider: "local_geniex"
      endpoint: "http://127.0.0.1:8081/v1"
      model: "qwen-2.5-0.5b-instruct-q4_0"
      device: "node_alpha_snapdragon_htp"
      timeout_ms: 800
    fallback:
      provider: "local_llamacpp"
      endpoint: "http://127.0.0.1:8080/v1"
      model: "qwen-2.5-0.5b-instruct"

  # 2. Daily Driver Inference (4B / 9B Core Brain)
  core_reasoning:
    primary:


      provider: "local_npu"
      endpoint: "http://127.0.0.1:8081/v1"
      model: "qwen-3.5-9b-instruct-q4_0"
      device: "node_alpha_npu"
      timeout_ms: 4500
    secondary:
      provider: "node_beta_jetson"
      endpoint: "http://node-beta.local:8080/v1"
      model: "deepseek-r1-distill-qwen-8b"
      device: "jetson_orin_cuda"
      timeout_ms: 6000
    fallback:
      provider: "openrouter_cloud"
      endpoint: "https://openrouter.ai/api/v1"
      model: "anthropic/claude-3.5-sonnet"
      api_key_env: "OPENROUTER_API_KEY"

  # 3. High-Compute Long-Context / Frontier Tasks
  frontier_eval:
    primary:
      provider: "openrouter_cloud"
      endpoint: "https://openrouter.ai/api/v1"
      model: "anthropic/claude-3.7-sonnet"
    secondary:
      provider: "google_vertex"
      endpoint: "https://aiplatform.googleapis.com/v1"
      model: "gemini-2.5-pro"

memory_extraction_hooks:
  enabled: true
  async_tap: true # Extracts memory asynchronously without adding prompt latency
  target_subsystem: "reasoning_bank"
  extraction_rules:
    log_failure_trajectories: true
    capture_tool_invocations: true
    sample_successful_reasoning_paths: true
    export_to_mem0: true
