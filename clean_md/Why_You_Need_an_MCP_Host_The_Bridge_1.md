---
source: Why You Need an MCP Host (The Bridge) (1).txt
type: condensed
condensed_from: NovA-Corpus/condensed/mcp-host-bridge (2026-08-20)
original_moved_to: Merovingian's_keep/_salvage/NovA-Corpus/originals/
---

# Why an MCP host/bridge is needed (ECC/Prime Agent don't run MCP servers automatically)

## The Direct Answer

Neither ECC nor Prime Agent "takes care" of running MCP servers automatically. An MCP host/bridge running inside the local network or Termux environment is still needed to manage them.

Harnesses like ECC and Prime Agent are MCP Clients — the "consumers" of the tools. Individual GitHub servers (Perplexity, Supabase, Linear, Playwright, Semgrep) are standalone programs speaking JSON-RPC. They cannot talk to an agent unless an MCP Host boots them up, assigns them ports, and translates their inputs/outputs.

## 1. Why an MCP Host (The Bridge) Is Needed

Because on-device open-weights models (Qwen 3.5 0.8B/9B) have no native concept of what an "MCP server" is:

- **The Problem**: if Qwen 3.5 wants to run a Perplexity search, it can only output a text request — it cannot physically touch the network card or execute code.
- **The Solution**: a central MCP Host (e.g. Node-RED, Smithery, or a simple Python script) running locally.
- **The Workflow**: Qwen 3.5 says "I need to run a Perplexity search" → the Harness (ECC/Prime) catches that intent → forwards it to the MCP Host → the MCP Host wakes up the Perplexity GitHub script, runs the search, grabs results, passes clean text back to the model.

## 2. How the Memory Layer Plugs into MCP

For a multi-tool memory system (mem0 + OmniRoute + ob1 + graphify + LLM Wiki), MCP is the glue connecting them. Rather than hardcoding mem0/Reasoning Bank directly into the Kotlin app or model context window, wrap the memory tools as Custom MCP Servers.

```
[ YOUR AGENT / HARNESS (ECC) ]
            │ (Asks to read/write memory)
            ▼
[ LOCAL MCP HOST (The Orchestrator) ]
            │ (Routes requests to specialized tools)
   ┌────────┼────────┐
   ▼        ▼        ▼
[MEM0]  [GRAPHIFY]  [OB1]
(User    (Concept   (P2P Sync
Entities) Mesh)      Server)
```

- **Memory-as-a-Tool**: one MCP configuration file registers mem0 as `get_long_term_memory` and graphify as `query_knowledge_graph`.
- **Token savings**: OmniRoute calls `query_knowledge_graph` instead of stuffing the whole Obsidian vault into the model — the server fetches only the needed relationships, keeping the Qwen 3.5 context window lean on the Hexagon NPU.

## 3. The "No Subscription" Setup for Termux / Home

**On the phone (Termux)**: a simple open-source Python tool, a Node-based mcp-cli, or a Python gateway hosts local servers. A single `mcp_config.json` lists local paths to Semgrep, the Perplexity substitution, and the Supabase connection string. The Kotlin UI Foreground Service initializes this local host bridge on wake, letting both Qwen models call them instantly.

**On the home node**: Prime Agent interacts with MCP servers natively because it runs a persistent IPython kernel — a small Python utility script imports MCP servers as raw Python functions directly into Prime Agent's execution pipeline.

## Summary

1. Don't code the servers yet — keep the GitHub forks of Perplexity, Supabase, Playwright, and Semgrep in their folders.
2. ECC and Prime Agent are the "bosses" reading the memory layouts; the MCP setup is the "switchboard" letting them talk to each other.

Open question raised in the source: pass data payloads (screen arrays, compressed prompt contexts) as standard JSON strings over local network ports, or write them to shared local files (`/sdcard/cache`) that daemons read dynamically?
