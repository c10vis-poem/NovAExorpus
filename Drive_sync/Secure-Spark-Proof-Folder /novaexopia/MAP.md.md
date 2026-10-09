---
title: "MAP.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novaexopia/MAP.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# MAP.md — Novaexopia Component & Navigation Map

## Subsystem Identity
- **Repository:** `novaexopia`
- **Role:** Tool harness runtime, OpenWiki TUI harness, modular swarm harnesses, and MCP
capability bridge.
- **Reference Spec:**
[PROPOSAL-V2-CORRECTED-WIKI-TERMINOLOGY-AND-s-tier-ALTERNATIVE.md](https://dri
ve.google.com/file/d/1S2cQzDPTknjzX9fR3q6lqsRLZxkcQAcA/view)
- **Federated Architecture:**
[05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md](https://docs.google.com/document/
d/1mhJbcx30lBFOu_WjbcHb0dlHFBzaN7p03Vzk2W017Rw/edit)
- **Pointers & Checkouts:** [The Federated Repositories & Pointer
Checkouts](https://docs.google.com/document/d/1Nb-QEhUXMSdwcQ9-3Q4AQihMmw6jxj5l_4
wRL2jhQUE/edit)

---

## Directory Ontology

### Baseline Control Files
- `MAP.md`: This file — Human and agent navigation map.
- `manifest.jsonl`: Cryptographic index and machine RAG catalog.
- `README.md`: Subsystem scope, operational invariants, and runbooks.
- `AGENTS.md`: Agent execution contracts, boundaries, and hard rules.
- `RESUME.md`: Verified state of progress and session handoff ledger.
- `chunk.jsonl`: Pre-tokenized machine retrieval passage chunks.

### Universal Subdirectories
- `raw/`: Unprocessed intake landing zone.
- `clean_md/`: Normalized, high-density condensed markdown (100% build context preserved).
- `wiki_md/`: Compounding living wiki knowledge nodes with [[wikilinks]].
- `skills/`: Local procedural skills and prompts.
- `tools/`: Local executable scripts and CLI utilities.
- `scripts/`: Production shell and Python execution scripts.
- `hooks/`: Subsystem lifecycle, git, and audit hooks.
- `pending/`: Staged tasks, tickets, and unverified outputs.
- `audit/`: Test traces, failure logs, and hygiene verification reports.
- `archive/`: Deprecated drafts and historical snapshots.

### Domain Subdirectories
- `openwiki-tui-harness/`: OpenWiki TUI terminal frontend, interactive views, and text dashboard.
- `modular_harnesses/`: 8 modular swarm harnesses (`ecc-edge-compute/`, `prime-agent/`,


`ringer-notif-loop/`, `hermes-soul/`, `aider-workspace/`, `local-nanobots/`, `smol-agents/`,
`turbo-quant-swarms/`).
- `mcp_connectors/`: Model Context Protocol capability adapters, tool bridges, and server
configs.
