---
title: "security_clearance.yaml"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/aesop-xi/policies/security_clearance.yaml.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

#
========================================================================
======
# ÆSOP-XI SECURITY CLEARANCE & OAUTH BOUNDARY SPECIFICATION
# ------------------------------------------------------------------------------
# Subsystem: aesop-xi/policies/
# Defines access control boundaries, cryptographic token scopes, and inter-repo
# authorization levels for all autonomous agent personas in the ecosystem.
#
========================================================================
======

version: "3.0.0"
policy_id: "aesop-xi-sec-clearance-canon"
updated_at: "2026-09-07T02:00:00Z"

security_realms:
  sovereign_local:
    network_interface: "127.0.0.1"
    auth_method: "HMAC-SHA256-UNIX-SOCKET"
  tailscale_mesh:
    nodes: ["node-alpha-razr", "node-beta-jetson", "node-gamma-rubik"]
    auth_method: "TAILSCALE-WIREGUARD-MTLS"
  cloud_federated:
    provider: "Google-Cloud-Vertex-AI"
    auth_method: "OAUTH2-SERVICE-ACCOUNT"

agents:
  horizons_concierge:
    role: "User-Facing Presentation & Intent Ingress"
    allowed_repos:
      - repo: "novaecopia"
        access: ["read", "write_ui_state"]
        paths: ["horizons-ui/**"]
    network_access:
      allowed_sockets: ["/dev/socket/aesc_shell.sock", "/dev/socket/aeyre_media.sock"]
      outbound_internet: false

  aesc_terminal_daemon:
    role: "System Terminal Daemon & ADB Loopback Bridge"
    uid: 2000
    allowed_repos:
      - repo: "novaecopia"


        access: ["read", "write", "execute"]
        paths: ["aesc/**", "openwiki-tui-harness/**"]
    special_permissions:
      - "ADB_WIRELESS_DEBUGGING_127_0_0_1_PORT_5555"
      - "NDK_ASHMEM_ZERO_COPY"

  aeyre_media_daemon:
    role: "Sensory Ingress & Vocal Synthesis Daemon"
    allowed_repos:
      - repo: "novaecopia"
        access: ["read", "write"]
        paths: ["aeyre/**"]
    special_permissions:
      - "SILERO_VAD_RECORD_AUDIO"
      - "SHERPA_ONNX_SYNTHESIS"

  novus_aexenti_brain:
    role: "Cognitive Dual-Agent Router & Execution Engine"
    allowed_repos:
      - repo: "novus-aexenti"
        access: ["read", "write", "execute"]
        paths: ["dual_agent_router/**", "mem0_episodic/**", "reasoning_bank/**"]
      - repo: "novae-xorpus"
        access: ["read_only"]
        paths: ["01_raw_sources/**", "02_wiki_md/**", "03_recall_cache/**"]
    special_permissions:
      - "HEXAGON_HTP_V79_NPU_EXECUTE"
      - "CUDA_TORCH_JETSON_EXECUTE"

  enterprise_cross_auditor:
    role: "Official Cross-Auditor & Data Log Collector"
    allowed_repos:
      - repo: "*"
        access: ["read", "write_manifest", "write_hygiene_reports"]
        paths: ["manifest.jsonl", "**/hygiene_reports/**"]

  incognito_red_gatekeeper:
    role: "Sealed Shadow Auditor & Verification Gate"
    isolation_tier: "AIR_GAPPED_SANDBOX"
    allowed_repos:
      - repo: "aesop-xi"
        access: ["read", "write", "quarantine"]
        paths: [\".incognito_red_sandbox/**\"]


    prohibitions:
      - "NO_PUBLIC_MANIFEST_EXPOSURE"
      - "NO_DIRECT_CHAT_INTERACTION"
      - "NO_PERSISTENT_NETWORK_LISTENER"

revocation_policy:
  auto_expire_tokens_after_seconds: 300
  emergency_killswitch_signal: "SIGUSR2"
