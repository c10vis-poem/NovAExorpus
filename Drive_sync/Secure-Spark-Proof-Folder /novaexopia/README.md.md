---
title: "README.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novaexopia/README.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# Novaexopia Subsystem Specification & Runbook

## Overview
`novaexopia` is the execution harness runtime and capability bridge for the NovÆxorpus
ecosystem. It provides the execution shells, agent swarms, and external tool connectors.

## Core Architectural Components
1. **OpenWiki TUI Harness (`openwiki-tui-harness/`)**:
   - Terminal user interface and interactive text dashboard.
   - Grounded in OpenWiki specs and mobile developer workflows.
2. **Modular Swarm Harnesses (`modular_harnesses/`)**:
   - `ecc-edge-compute/`: Edge computing loop and Claude Code CLI interface.
   - `prime-agent/`: Sovereign-edge on-device RLM loop with persistent Python REPL.
   - `ringer-notif-loop/`: Notification interceptor and event loop.
   - `hermes-soul/`: Hermes CLI integration.
   - `aider-workspace/`: Automated coding agent harness.
   - `local-nanobots/`: Lightweight local task runners.
   - `smol-agents/`: Minimalist functional agents.
   - `turbo-quant-swarms/`: Fast quantized model swarm orchestration.
3. **MCP Connectors (`mcp_connectors/`)**:
   - Standardized Model Context Protocol bridges to local filesystems, databases, and external
endpoints.

## Operational Invariants
- **First-Move Directive:** Orient with `MAP.md`, query `manifest.jsonl`, load targeted files only.
- **Locality of Reference:** Skills and tools live locally where they are applied.
- **Hot-Swap Design:** Decoupled interfaces (Model, Memory, Tools, Output) enable swapping
harnesses without state corruption.
