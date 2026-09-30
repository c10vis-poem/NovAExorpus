# Final Memory Layer / Inference & P2P Server Stack Model Pipeline

Source: Gemini AI-Mode research conversation (Drive folder `1vOaCRRn-gg6kED0jBtirUoHmVDoxiMvM`, doc titled by its own first-line fragment). Category: **master architecture reference** — per the user, this doc "gives the final overall picture of what we're trying to build." Mid-conversation the user free-talks through their real hardware setup and the assistant iterates the plan across several corrections (RAM budget mistakes get caught and fixed live) — that back-and-forth is preserved here because the corrections themselves are informative, not just the final answer.

**Source reliability note**: this is a Gemini search/chat session citing external blog posts, GitHub repos, and YouTube videos — not verified working code, and several specific claims (benchmark numbers, exact model file sizes, "GPT-5.2" as a real shipping model) are vendor/blogger claims relayed through Gemini's citations, not independently confirmed here. Flagged inline as `<!-- UNVERIFIED -->` where the claim is a specific number or product fact rather than general architecture concept.

## 1. The Dual-Agent Talker-Reasoner Architecture (a.k.a. Librarian/Query Agent & Sandbox Executor)

Addresses context bloat and the "lost in the middle" problem by decoupling memory tracking from task execution:

- **The Executor Agent (The Sandbox)**: zero historical context bloat. Spun up with a narrow, constrained context window optimized exclusively for one immediate subtask or code execution. Because it's never carrying past conversation baggage, reasoning efficiency spikes, token costs drop, instruction dilution is avoided.
- **The Query / Talker Agent (The Memory Layer)**: manages long-term, cross-session memory. Handles active user prompts, semantic search, historical retrieval.

**How it stops context bloat**:
1. Isolated Turn Execution — the Query Agent searches a persistent storage layer (e.g. Mem0, Memori), isolates only the needed slice, packages it as a micro-payload.
2. Stateless Passing — the Query Agent hands that micro-payload to the Executor Agent.
3. Wiping the Slate — once the Executor finishes running the tool/script, it returns output to the Query/Talker Agent and its own sandbox resets.

<!-- UNVERIFIED: this pattern is attributed to "coverage by Marktechpost and top AI labs" per the source chat; treat as a named pattern circulating in AI-engineering blog content, not a single canonical spec. -->

## 2. MiMo Code + Mem0 (the repo the user was trying to recall)

- **MiMo Code** — released by Xiaomi's AI team (per the source, early June 2026), MIT-licensed, terminal-native long-horizon AI coding harness, open-source fork of the OpenCode engine, written in TypeScript. Repo: `github.com/XiaomiMiMo/MiMo-Code`. Claimed to handle 200+ execution-step tasks without choking on context (standard coding agents allegedly choke past 200 steps) by using a strict dual-layer setup: the MiMo-V2-Flash/Pro foundation engine acts as a context-lean sandbox executor, wiping its short-term workspace constantly, while a master orchestration/memory layer feeds it micro-payloads and tracks broader engineering goals. <!-- UNVERIFIED: "beats Claude Code at ultra-long 200-step tasks" is a third-party (VentureBeat-sourced per citation) claim, not independently benchmarked here. -->
- **Mem0** (formerly Embedchain) — the memory engine commonly paired with this pattern in tutorials. Acts as a standalone intelligent memory layer: extracts facts, updates a graph/vector layer dynamically (often via Neo4j), lets a "Query Agent" pull only the precise memory vectors needed for the next step. Repo: `github.com/mem0ai/mem0`.
- **Reverse-engineering targets inside MiMo-Code** (per the source, for anyone pulling the repo apart): `packages/opencode/src/cli/cmd/tui/` for the multi-agent orchestration/sub-agent dispatch logic; files implementing `/dream`, `/distill`, `/goal` routines for compressing noisy terminal execution loops into permanent memory (with `/dream` running async between sessions as a cleanup pass — flagged as a good template for a cron-style JSONL cleanup job); and the discover/registry sandboxing files for directory-permission/file-system boundary checks (useful pattern to copy into a Red Agent auditor layer). Install for local testing: `curl -fsSL https://mimo.xiaomi.com/install | bash` (Mac/Linux) or `npm install -g @mimo-ai/cli` (Windows). <!-- UNVERIFIED: exact file paths (e.g. registry.rs) are as stated in the source conversation, not independently confirmed against the live repo. -->

## 3. The User's Real Hardware Topology

Three-device private neural mesh, connected via Tailscale P2P:

| Device | Role | Model(s) | Notes |
|---|---|---|---|
| Motorola Razr Ultra 25 | Mobile Orchestrator / STT Router ("daily driver") | Qwen 3.5 9B (Q4_0 GGUF) | Also carries OmniNeural-4B for persistent STT → meta-prompt transformation while in a Claude/Gemini session; decides whether a request is answerable locally, needs a tool call, or needs to be shot off to a cloud front-end (Claude, etc.) |
| Jetson (Nano Super) | Home hub, headless | Cloud API fallback (e.g. Gemini Flash/GPT-4o mini) or local high-quant SLM, running via vLLM if RAM allows | Hosts the 500GB SSD with Open-Wiki/LLM-Wiki flattened JSONL data; runs OB1 for memory orchestration; runs OmniRoute as the token-preserving API gateway |
| Dragon Wing Rubik Pi 3 (Thundercomm, Qualcomm Dragonwing QCS6490) | Headless display/desktop GUI + vision model + "Red Agent" auditor | Small quantized model, ~2GB budget out of 8GB total LPDDR4x RAM (2GB weights + 1GB runtime/KV cache, 5GB reserved for OS/display/vision) | Corrected mid-conversation: original guidance assumed only 2GB total RAM and suggested unworkable 8B models; once the user corrected to 8GB total, the answer shifted to Gemma 4 E2B/E4B |

Connection: when home, the phone "tailscales in" to the home network, forming one continuous neural mesh loop. Away from home, the phone's on-device Qwen model just needs to know how to act (tool-call/orchestrate), not carry heavy knowledge — the heavier dual-agent memory layer only engages once connected to the home hub.

## 4. The Three-Layer Agent Pipeline

**Layer 1 — The Inquisitor & Router (the phone, Qwen 3.5 9B)**: acts strictly as a traffic controller, never reads raw docs or long logs. Local STT → structured Meta-Prompt JSON. Routing logic: simple request → answer on-device; complex coding/file query → package intent as a lightweight MCP tool call; cloud engine front-end → forward to Claude Code CLI or Gemini APIs directly.

**Layer 2 — The Governed Continuity Memory (home hub, via OB1 + Tailscale)**: when connected home, the phone reaches Nate Jones' OB1 (Open Brain) infrastructure on the Jetson. The Jetson's 500GB SSD holds Open-Wiki-compiled JSONL. When Qwen requests info, OB1's MCP server intercepts, runs a localized vector-match/semantic query against the Obsidian graph/PDF vaults, and returns a precise context slice (e.g. ~2K tokens) rather than dumping the whole file system into the prompt.

**Layer 3 — The Stateless Executor & Red Agent (sandbox + guardrails)**: the heavy execution model (Jetson) runs in a transient environment — receives the Layer 2 context slice, calls the CLI or builds the script, outputs the result, destroys its own chat history immediately. The Rubik Pi 3 acts as a Red Agent/Code Auditor: before any generated script executes or returns to the phone, it passes through the Rubik Pi for a secondary verification sweep (syntax, correctness, guardrail matching).

## 5. The Auditor Layer — Detailed Architecture

The Rubik Pi 3 is an asynchronous gatekeeper, not a direct executor. The Jetson compiles code/scripts but never runs them directly on the main filesystem — it pipes the proposed payload to the Auditor first.

**Verification pipeline**:
1. **Interception** — every generated CLI script/code block is packaged into a structured JSON payload (`intended_task`, `proposed_code`, `target_directory`).
2. **Static analysis (deterministic step)** — before invoking any LLM, run basic checks (e.g. Python `ast` parsing, standard linters) to catch blatant syntax errors.
3. **The Red Agent audit (cognitive step)** — a small, specialized model reviews the payload against a strict, immutable system prompt focused on security boundaries, optimization, logical validation.
4. **Gatekeeping** — approved payloads get an execute signal; failed payloads get an `error_log` JSON block appended and are returned to the Executor for correction.

**Lightweight runtimes considered for the constrained dev boards**:
- `llama.cpp` via a persistent server binary (ARM NEON-optimized) — lightweight local HTTP/JSON API.
- Llamafile — single-file portable executable, stable for long-running headless edge servers.
- vLLM with PagedAttention — reserved for the Jetson Nano specifically (needs real CUDA cores/unified memory), NOT recommended for the Rubik Pi 3's constrained footprint.

**Auditor model candidates iterated across the conversation** (each superseded by the next as RAM constraints were corrected):
1. First pass (assumed generic small footprint): Llama-3-8B-Instruct (Q4_K_M), Qwen-2.5-Coder-7B-Instruct (Q4_0/Q4_K_S), Granite-3.0-8B-Instruct.
2. Second pass (assumed only 2GB total RAM, corrected down): Qwen-2.5-Coder-1.5B-Instruct (~1.1-1.2GB, best fit, code-syntax-trained), Phi-3.5-mini-instruct heavily quantized to Q2_K/Q3_K_S (~1.6-1.9GB), Granite-3.0-Light-2B/1B variants.
3. Third pass (corrected again once the user clarified 8GB total RAM, ~3GB AI-layer budget): Qwen-2.5-Coder-1.5B-Instruct (~1.1-1.2GB) still fits; Phi-3.5-mini-instruct quantized to Q2_K/Q3_K_S (~1.6-1.9GB); Google Gemma-2-2B-IT (~1.6GB at Q4_K_M).
4. **Final recommendation**: **Gemma 4 E2B or E4B** — uses Per-Layer Embeddings (PLE) for high intelligence density at small size. Gemma 4 E2B (2.3B effective params) ≈1.4GB at Q4_K_M; Gemma 4 E4B (4.5B effective params) ≈2.8GB, pushes near the 3GB cap but claimed to punch like an old 15B+ model. <!-- UNVERIFIED: "Per-Layer Embeddings" claim and the 15B-class reasoning comparison are as stated in the source chat, not independently benchmarked. --> Natively multimodal (text/image/audio in one model), which matters here because the Rubik Pi 3 is simultaneously the desktop vision model — no need for a separate CLIP/vision encoder alongside the text auditor model. Has day-one native llama.cpp GGUF support per the source.

## 6. Token Preservation & Context Slicing — OmniRoute + Open-Wiki

- **OmniRoute** runs on the Jetson Nano as the core traffic gateway between the local network and the external web, routing across 230+ API endpoints per the source (<!-- UNVERIFIED: specific endpoint count and "75% token reduction" figure are as claimed in the source chat's citations -->), automatically routing heavy coding requests to a free high-tier cloud provider, and stripping repetitive/bloated system context headers from incoming streams to preserve free-tier token budgets during large project builds. Site referenced: `omniroute.online`. (Note: this is the same OmniRoute project already in this session's repo scope at `/home/user/OmniRoute` — the source material's marketing framing of "16 billion free tokens monthly" / "160+ AI models" should be checked against OmniRoute's own docs/CLAUDE.md rather than taken from this Gemini citation.)
- **Open-Wiki** holds the flattened Obsidian MD graphs / PDFs / codebase schemas on the Jetson's 500GB SSD, compiled into JSONL. When a task triggers, Open-Wiki pulls a specific compressed JSONL context payload rather than uploading whole folders to the cloud model.

## 7. Network Architecture: Tailscale P2P Mesh + WebSocket Protocol

All three devices run **Tailscale**, forming a secure encrypted overlay network (100.x.y.z address range) with direct device-to-device communication and no port-forwarding/public IP exposure. Example addressing used in the source conversation (illustrative, not necessarily the user's real assigned IPs):

- `100.64.0.10` — Motorola Razr Ultra 25 (Mobile Orchestrator / Qwen 3.5 9B)
- `100.64.0.20` — Jetson Nano Super (Hub / Open-Wiki / vLLM / OmniRoute)
- `100.64.0.30` — Rubik Pi 3 (Auditor / Gemma 4 E2B / llama.cpp server)

Rather than fragile polling REST APIs, the architecture uses a **centralized WebSocket router on the Jetson Nano** for persistent bidirectional connections.

**Connection/keep-alive handshake** (phone or Rubik Pi → Nano):
```json
{
  "event": "connection:init",
  "client_id": "razr_ultra_25",
  "timestamp": 1783467120,
  "capabilities": ["stt", "orchestration", "local_inference"]
}
```
Heartbeat ping every 10 seconds to keep the P2P pipe alive over cellular data.

**Task inference workflow, phase by phase**:

- **Phase 1 — Meta-Prompt Handshake (Phone → Nano)**: phone STT + Qwen 3.5 9B build a structured routing meta-prompt, sent over `ws://<nano-ip>:8000/stream`:
```json
{
  "session_id": "sess_2026_07_07_abc",
  "event": "orchestrator:route_request",
  "intent": "code_generation",
  "meta_prompt": "Generate a network configuration script for my local interface, verify routing matrices against the project design documentation.",
  "context_requirements": {
    "source": "open-wiki:obsidian-vault",
    "query_tags": ["network-config", "routing-rules"]
  }
}
```
- **Phase 2 — Core injection/processing (inside the Nano)**: Nano hits Open-Wiki CLI for a ~2KB context slice, sends filtered context + instructions through OmniRoute to the cloud engine, receives a proposed script (not executed yet).
- **Phase 3 — Auditor gatekeeper handshake (Nano → Rubik Pi 3)**: generated code routed to a dedicated audit WebSocket namespace `ws://<nano-ip>:8000/audit`:
```json
{
  "session_id": "sess_2026_07_07_abc",
  "event": "auditor:review_request",
  "runtime_environment": "bash",
  "proposed_payload": "#!/bin/bash\nip route add 192.168.10.0/24 dev eth0",
  "context_rules": "Ensure interface eth0 target constraints match local routing limitations."
}
```
- **Phase 4 — Gemma-4 vision/text audit (inside Rubik Pi 3)**: script piped into Gemma 4 E2B via llama.cpp; optionally appends a desktop screencap via the model's native multimodal layer to confirm the change won't break the visual setup.
- **Phase 5 — Execution resolution (Rubik Pi → Nano)**: structured pass/fail verdict returned.

Approved:
```json
{
  "session_id": "sess_2026_07_07_abc",
  "event": "auditor:verdict",
  "status": "APPROVED",
  "error_log": null,
  "execution_token": "token_auth_validated_9981"
}
```
Rejected (recursive-loop prevention — error routed back through OmniRoute for a zero-cost automated rewrite before re-submission):
```json
{
  "session_id": "sess_2026_07_07_abc",
  "event": "auditor:verdict",
  "status": "REJECTED",
  "error_log": "Syntax Error: Target network block overlaps with default interface allocation on line 2.",
  "execution_token": null
}
```

## 8. Key CLIs / Utilities Named for This Pipeline

- **Claude Code CLI** — run in an isolated terminal session on the Jetson Nano so the mobile device can offload intensive coding logic while the local executor stays focused on the attached SSD.
- **Fabric CLI** — patterns-based AI orchestration (e.g. `extract_wisdom`, `verify_code` patterns); suggested to sit on the Rubik Pi for automated validation over incoming text/scripts.
- **LiteLLM** — internal proxy gateway on the home hub, exposing local models (llama.cpp), private cloud keys, and free cloud endpoints through one OpenAI-compatible API stream.
- **Steampipe CLI** — SQL-style querying of local infrastructure/directories/the 500GB SSD, integrating with the OB1 MCP layer so models can query file metrics like a database.

<!-- UNVERIFIED: this whole utility list is suggested tooling from the Gemini chat, not confirmed as already installed/working in the user's actual setup. -->

## Relationship to OpenWiki + OB1 + reasoning-bank + Omni Claw

This document is the clearest single statement (per the user) of how the three memory-system repos already surveyed in this project (OpenWiki, OB1, reasoning-bank) and the Omni Claw/AESOP vision fit into one real, physical, multi-device deployment:

- **OB1** is named directly and explicitly here as the memory orchestration layer (`Nate Jones' OB1 (Open Brain)`, MCP server + Postgres/Supabase-style memory) running on the home hub.
- **Open-Wiki / LLM-Wiki** is named directly as the PDF/Obsidian-graph-to-JSONL compiler feeding the SSD-backed context store — this is the same tool covered in the `llm-wiki-termux-setup` skill package, but here it's the home-hub-scale version rather than the on-phone Termux version.
- The **Dual-Agent Talker-Reasoner pattern** (Executor/Sandbox + Query/Talker memory agent) described here is architecturally the same shape as **reasoning-bank**'s success/failure memory-item retrieval concept and as Omni Claw's "Local Knowledge Synthesis" step (C++ engine pulling skill blocks/context before compiling a meta-prompt) — all three describe the same underlying idea: keep the execution/reasoning layer context-lean, and let a separate memory/retrieval layer feed it precise slices on demand.
- The **Rubik Pi 3 Red Agent Auditor** is a new capability not previously covered in the OpenWiki/OB1/reasoning-bank/AESOP/Omni Claw docs — a dedicated code-review/guardrail gate sitting between generation and execution. Worth carrying into the eventual integration architecture doc as an additional layer beyond the three repos already scoped.
- **Third repo the user couldn't name**: during the conversation the user mentions three repos they're weaving together — OB1, "Mimir Claw / OpenClaw" (recalled here as the dual-agent session persistence engine), and "Open-Wiki / Model Wiki CLI" — plus a repo "in between" OB1 and Open-Wiki they couldn't recall the name of. Not resolved in this document; flag as an open item if the user wants to identify it later.
