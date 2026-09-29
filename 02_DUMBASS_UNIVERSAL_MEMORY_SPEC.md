Tab 1
02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md
The Database & Universal Memory Bank Across Split Services (#d.u.m.b.a.s.s.)
1. Document Authority & Supersession
This specification establishes the official architecture for the #d.u.m.b.a.s.s. memory subsystem across mobile edge devices, local servers, and cloud instances. It envelops, unifies, and supersedes:


* **SQLite.txt
* Attaching #dumbass and Æsop-Xi
* Continual harness online adaptation for self-improving foundation agents.txt
* The Global Information Layer & Storage Matrix.txt
* Mem0 architecture notes (Folder 4)


________________


2. Core Operational Law: The Integrated Memory Engine
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐


│                               #d.u.m.b.a.s.s. MEMORY SUBSYSTEM                                  │


├───────────────────┬─────────────────────────────────────────────────┬────────────────────────────┤


│ Component         │ Architectural Responsibility                    │ Hardware & Network Binding │


├───────────────────┼─────────────────────────────────────────────────┼────────────────────────────┤


│ mem0              │ In-session episodic state & user habits         │ Node Alpha (Mobile RAM)    │


│ OB1 Protocol      │ Ground-truth static retrieval protocols via MCP │ Ubiquitous Network-Wide    │
│ OmniRoute Gateway │ Data routing, memory extraction tap, token conservation & cost routing │ Localhost Port 20128       │
│ OmniRoute Gateway │ Token conservation, prompt caching & cost route │ Localhost Port 20128       │


│ Reasoning Bank    │ Multi-model execution ledger & crash recovery   │ JSON / KV Store            │


│ SQLite            │ Embedded zero-latency relational/KV tables      │ Node Alpha Flash / Disk    │


│ PostgreSQL        │ Authoritative relational & vector persistence   │ Node Beta (Jetson Server)  │


│ Continual Harness │ Online reset-free self-improvement loop        │ Supervisory State Machine  │


└───────────────────┴─────────────────────────────────────────────────┴────────────────────────────┘
Beginner-Proof Explanation: How the Layers Work Together
1. mem0: Remembers what you said 2 minutes ago and how you like your answers structured. It maintains short-term personalization so the model doesn't ask you the same questions repeatedly.
2. OB1 (Open Brain Protocol): When the model needs to reference a 500-page Qualcomm manual or system schema, it queries OB1 over MCP. OB1 extracts the exact grounded paragraphs so the model never has to guess or hallucinate.
3. OmniRoute: OmniRoute is a core data routing and memory extraction layer operating on port 20128. Beyond token caching and routing queries between local NPU, Jetson, and cloud endpoints, it acts as an asynchronous memory tap on every request and response—extracting candidate trajectories, tool invocation traces, and failure patterns directly into the Reasoning Bank and mem0 without adding inference latency.
4. Reasoning Bank (active_execution_paths.json): When an agent undertakes a 10-step programming task, it writes each step to this ledger. If the battery dies or the process is killed at Step 6, the system reads this ledger upon reboot and resumes at Step 7 without losing state.
5. SQLite: The local database on your phone. Requires zero setup, zero network connection, and answers queries in under 5 milliseconds.
6. PostgreSQL: The master database on your Jetson server that backs up all history, code graphs, and enterprise records across the network.
7. Continual Harness: Allows agents to learn and refine prompt instructions during live execution. If an update causes an error, it immediately triggers an automated snapshot rollback. The base system prompt is never modified.


________________


3. Universal JSONL Marker Schema
Every asset indexed by #dumbass receives an atomic JSONL marker record matching this schema:


{


  "record_id": "MEM_A102_20260904_SCHEMA",


  "document_path": "02_wiki_md/architectures/npu_topology.md",


  "tier": 2,


  "category": "TECHNICAL_REFERENCE",


  "metadata": {


    "title": "NPU Memory Topology & FastRPC Bindings",


    "description": "Zero-copy shared memory allocation for Snapdragon 8 Elite Hexagon NPU.",


    "content_hash": "e3b0c44298fc1c14",


    "file_size_bytes": 4820,


    "last_modified": "2026-09-04T07:45:00Z"


  },


  "retrieval_tokens": ["qualcomm", "qnn", "fastrpc", "asharedmemory", "dma_buf", "htp"],


  "entry_points": {


    "mcp_method": "knowledge.retrieve",


    "cli_command": "/skill run npu-topology"


  }


}


________________


4. Git Orchestration & Cross-Repo Sync Hook
To ensure #dumbass (novae-xorpus) and consumer repositories (like aesop-xi) stay synchronized across sessions without duplication, use this automated Git post-commit hook:


#!/usr/bin/env bash


# ==============================================================================


# Git Post-Commit Synchronization Hook for #dumbass


# Location: ~/repos/aesop-xi/.git/hooks/post-commit


# ==============================================================================


set -euo pipefail


VAULT_DIR="${HOME}/novae-xorpus"


CONSUMER_DIR="${HOME}/repos/aesop-xi"


echo "[*] Triggering #dumbass master ledger regeneration..."


# 1. Ensure symlinks exist


mkdir -p "${VAULT_DIR}/projects/aesop-xi"


ln -sfn "${CONSUMER_DIR}/RESUME.md" "${VAULT_DIR}/projects/aesop-xi/RESUME.md"


ln -sfn "${CONSUMER_DIR}/CLAUDE.md" "${VAULT_DIR}/projects/aesop-xi/CLAUDE.md"


# 2. Execute master regeneration utility


if [ -f "${VAULT_DIR}/tools/regenerate_masters.sh" ]; then


    bash "${VAULT_DIR}/tools/regenerate_masters.sh"


    echo "[✓] MASTER-RESUME.md and MASTER-CLAUDE.md synchronized successfully."


fi


Tab 2