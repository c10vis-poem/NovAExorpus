---
title: "home_node_topology.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/data_vault/02_wiki_md/home_node_topology.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Sovereign 3-Node Physical Hardware Topology &
Workstation Breakdown
Mined from: PLUGINS TOOLS AND MEMORY LAYER ARGUMENTS (Files 3, 4, and
'Now that was.txt')
1. Physical Node Division of Labor
┌────────────────────────────────┐
┌────────────────────────────────┐

│           NODE ALPHA           │       │           NODE BETA            │

│    (Motorola RAZR Ultra 2025)  │◄─────►│   (NVIDIA Jetson Orin Nano)    │

│  - Snapdragon 8 Elite / HTP v79│       │  - 8GB RAM / CUDA Cores        │

│  - Primary On-Device Controller│       │  - Heavy Background Inference  │

│  - Horizons UI + Æsc + Æyre    │       │  - PostgreSQL + pgvector Master│

└───────────────┬────────────────┘
└────────────────┬───────────────┘

                │                                         │

                │        Encrypted Tailscale Mesh         │

                └───────────────────┬─────────────────────┘

                                    │

                                    ▼

                         ┌────────────────────┐

                         │     NODE GAMMA     │

                         │   (Rubik Pi 3)     │



                         │  - Housekeeper Task│

                         │  - Red Auditor Gate│

                         │  - Zero-Trust Audit│

                         └────────────────────┘
2. Dedicated Node Roles
●​ Node Alpha (Mobile Engine):
○​ Hardware: Motorola RAZR Ultra 2025 (Snapdragon 8 Elite).
○​ Role: Primary daily driver and user interface. Runs the decoupled 3-APK suite
(horizons-ui, aesc, aeyre), local Qwen 3.5 0.8B/9B weights, Silero VAD
voice ingress, and local ADB loopback.
●​ Node Beta (Compute Server):
○​ Hardware: NVIDIA Jetson Orin Nano Super (8GB).
○​ Role: Central database hub. Hosts PostgreSQL master persistence, OB1 vector
protocol, and heavy background reasoning models.
●​ Node Gamma (Autonomous Housekeeper & Red Gatekeeper):
○​ Hardware: DragonWing Rubik Pi 3.
○​ Role: Dedicated sandboxed housekeeper running automated repository linting,
git symlink verification, and the sealed Red Auditor daemon (run_audit.sh).
