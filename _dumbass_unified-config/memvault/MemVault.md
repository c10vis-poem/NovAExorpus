
## Page 1

MemVault
Code Issues More
Fork 0
## MemVault — The Shared Memory Layer for Every AI Agent You Run. MCP-native memory router with auto-injection, hybrid search, and zero-config sync.
MIT License
Code of conduct
Contributing
Security policy
0 stars 0 forks 0 watching 1 branch 2 tags Activity
Public repository
mast… 1 Branch 2 Tags T Go to file Add file Code
| dreamor ci(release): upload built binaries directly to GitHub Release |  |  | 7473aca · yesterday |
|---|---|---|---|
| .agents/ plugins | feat(codex): install the shared Claude plugin … | 2 weeks ago |  |
| .claude-plugin | fix: make Claude plugin load and honor ME … | 2 weeks ago |  |
| .github | ci(release): upload built binaries directly to … | yesterday |  |
| .grok-plugin | feat(plugins): native plugin adapters across … | 2 weeks ago |  |
| .openclaw/ skills | feat(plugins): batch-3 adapters (Hermes, pi, … | 2 weeks ago |  |
| .qoder-plugin | feat(plugins): native plugin adapters across … | 2 weeks ago |  |
| .qoder/ rules | feat(plugins): native plugin adapters across … | 2 weeks ago |  |
| assets | docs: keep full-resolution mascot as assets/ … | last month |  |
| commands | feat(plugins): native plugin adapters across … | 2 weeks ago |  |
| crates | fix(ci): resolve env_file race, upgrade actions … | 2 weeks ago |  |
| dashboard | chore(release): v0.4.0 | 2 weeks ago |  |
| docs | feat(mcp): embed the web dashboard in the … | 2 weeks ago |  |
| dsh-plugin | fix(dsh-plugin): match repo URL case to Git … | 2 weeks ago |  |
| integrations | chore(release): v0.4.0 | 2 weeks ago |  |
| obsidian-plugin | chore(obsidian): sync plugin copy with defer … | 2 weeks ago |  |
| pi-extension | feat(plugins): batch-3 adapters (Hermes, pi, … | 2 weeks ago |  |
| plugins/ memvault | feat(codex): install the shared Claude plugin … | 2 weeks ago |  |
| scripts | fix(homebrew): use the dispatch version inp … | last week |  |
| skills | feat(plugins): batch-3 adapters (Hermes, pi, … | 2 weeks ago |  |
| .dockerignore | chore: add container build plumbing | last month |  |
| .env.example | fix: make Claude plugin load and honor ME … | 2 weeks ago |  |
| .gitattributes | docs: drop DISTRIBUTION-TODO.md referen … | 2 weeks ago |  |
| .gitignore | refactor: drop VS Code extension, slim Obsi … | 2 weeks ago |  |
 
.agents/plugins feat(codex): install the shared Claude plugin… 2 weeks ago
.claude-plugin fix: make Claude plugin load and honor ME… 2 weeks ago
.github ci(release): upload built binaries directly to … yesterday
.grok-plugin feat(plugins): native plugin adapters across … 2 weeks ago
.openclaw/skills feat(plugins): batch-3 adapters (Hermes, pi, … 2 weeks ago
.qoder-plugin feat(plugins): native plugin adapters across … 2 weeks ago
.qoder/rules feat(plugins): native plugin adapters across … 2 weeks ago
assets docs: keep full-resolution mascot as assets/… last month
commands feat(plugins): native plugin adapters across … 2 weeks ago
crates fix(ci): resolve env_file race, upgrade actions… 2 weeks ago
dashboard chore(release): v0.4.0 2 weeks ago
docs feat(mcp): embed the web dashboard in the … 2 weeks ago
dsh-plugin fix(dsh-plugin): match repo URL case to Git… 2 weeks ago
integrations chore(release): v0.4.0 2 weeks ago
obsidian-plugin chore(obsidian): sync plugin copy with defer… 2 weeks ago
pi-extension feat(plugins): batch-3 adapters (Hermes, pi, … 2 weeks ago
plugins/memvault feat(codex): install the shared Claude plugin… 2 weeks ago
scripts fix(homebrew): use the dispatch version inp… last week
skills feat(plugins): batch-3 adapters (Hermes, pi, … 2 weeks ago
.dockerignore chore: add container build plumbing last month
.env.example fix: make Claude plugin load and honor ME… 2 weeks ago
.gitattributes docs: drop DISTRIBUTION-TODO.md referen… 2 weeks ago
.gitignore refactor: drop VS Code extension, slim Obsi… 2 weeks ago

---

## Page 2

| AGENTS.md | refactor: drop VS Code extension, slim Obsi … | 2 weeks ago |
|---|---|---|
| CHANGELOG.md | ci(release): upload built binaries directly to … | yesterday |
| CONTRIBUTING.md | build: switch TLS to rustls; document prebuil … | 2 weeks ago |
| Cargo.lock | chore(release): v0.4.0 | 2 weeks ago |
| Cargo.toml | chore(release): v0.4.0 | 2 weeks ago |
| Dockerfile | fix(docker): define the web stage before the … | 2 weeks ago |
| LICENSE | chore: establish project metadata | last month |
| README.md | docs(readme): list crates.io and npm core p … | last week |
| README.zh-CN.md | docs(readme): list crates.io and npm core p … | last week |
| SECURITY.md | feat(core): add identity verification + MUST … | 2 weeks ago |
| agents.example.yaml | feat(core): add identity verification + MUST … | 2 weeks ago |
| deny.toml | chore: open-source readiness pass (secrets, … | 2 weeks ago |
| gemini-extension.json | feat(plugins): native plugin adapters across … | 2 weeks ago |
| mcp-config.example.json | chore(root): untrack personal mcp-config.js … | last month |
| plugin.json | docs(readme): sync bilingual README with r … | 2 weeks ago |
| proxy.example.yaml | chore: fix all clippy warnings and fmt issues | last month |
AGENTS.md refactor: drop VS Code extension, slim Obsi… 2 weeks ago
CHANGELOG.md ci(release): upload built binaries directly to … yesterday
CONTRIBUTING.md build: switch TLS to rustls; document prebuil… 2 weeks ago
Cargo.lock chore(release): v0.4.0 2 weeks ago
Cargo.toml chore(release): v0.4.0 2 weeks ago
Dockerfile fix(docker): define the web stage before the … 2 weeks ago
LICENSE chore: establish project metadata last month
README.md docs(readme): list crates.io and npm core p… last week
README.zh-CN.md docs(readme): list crates.io and npm core p… last week
SECURITY.md feat(core): add identity verification + MUST … 2 weeks ago
agents.example.yaml feat(core): add identity verification + MUST … 2 weeks ago
deny.toml chore: open-source readiness pass (secrets,… 2 weeks ago
gemini-extension.json feat(plugins): native plugin adapters across … 2 weeks ago
 
plugin.json docs(readme): sync bilingual README with r… 2 weeks ago
proxy.example.yaml chore: fix all clippy warnings and fmt issues last month
README More
# MemVault
# The Shared Memory Layer for Every AI Agent You Run
# Not "agent learns to search memory" — memory finds the agent.
# MCP Native · Hybrid Retrieval · Auto-Injection · Zero-Config Sync
# Open Source · Self-Hosted · Private · MIT Licensed
crates.io v0.4.0 release v0.4.0 build pas ing License MIT Rust stable MCP compatible status beta
# English ·

---

## Page 3

If MemVault solves a real problem for you, a star helps others find it.
Star on GitHub · Report Bug
curl -fsSL https://raw.githubusercontent.com/dreamor/memvault/master/scripts/install.sh | bash
Every AI agent session starts from scratch. Claude Desktop doesn't know what Cursor just learned. DeepSeek Harness (dsh) doesn't know what you told Claude Code yesterday. Whatever agent you're running — international or domestic, IDE plugin or CLI harness — it forgets your preferences every time you start a new conversation.
You've been manually repeating context — project conventions, personal preferences, past decisions — across agents that should already know. This isn't a limitation of the models. It's a missing infrastructure layer.
MemVault is that layer. A lightweight, self-hosted memory router that sits between your agents and their context. It speaks plain MCP — no MemVault-specific SDK, no per-agent API integration. Any MCP-compatible agent, from any vendor, automatically shares the same persistent memory the moment it connects.
Who it's for:
• Anyone running an MCP-capable agent — Claude Code, Claude Desktop, Cursor, Cline, Continue, DeepSeek Harness (dsh), or any other MCP client, domestic or international — who wants preferences, project context, and past decisions to persist across sessions without repeating yourself
• Multi-agent power users running several of the above side by side, on different models, from different vendors — all sharing the same memory without configuration
• Platform teams deploying AI-assisted workflows where consistency matters across a mixed agent fleet: code review conventions, architecture decisions, project-specific preferences
• Anyone tired of telling their AI the same thing twice — MemVault works the way your brain should: you say it once, it's there when you need it, no matter which agent is asking
Quick Start · How It Works · What MemVault Gives You · Why MemVault · MCP Server · CLI Reference · Integrations · Architecture · Project Status · Testing · Documentation · Contributing · License
### Quick Start

---

## Page 4

# Install (Linux / macOS): official script, auto-verifies SHA-256 curl -fsSL https://raw.githubusercontent.com/dreamor/memvault/master/scripts/install.sh | bash export PATH="$HOME/.memvault/bin:$PATH"
# Windows (PowerShell): # powershell -ExecutionPolicy Bypass -File scripts\install.ps1
# Homebrew (Apple Silicon): # brew install dreamor/tap/memvault
# Or from crates.io: # cargo install memvault-cli memvault-mcp
# Save a MUST-level preference (injected as instruction, agent must follow) memvault save --content "User prefers Python" --priority MUST --type preference \ --instruction "Use Python for code, not Java" --tags "coding,python"
# Search across all memory (hybrid: keyword + semantic when embedding is enabled) memvault search --query "Python"
# See what context gets injected when a specific agent connects memvault session-start --agent-id claude-desktop --context "Help me write code"
# Extract structured memories from free text memvault extract --text "I prefer dark mode. Our project uses Rust." --save
# Auto-generate agent instruction files from memory memvault sync
# All in one: dedup, decay, archive stale memories memvault dedup && memvault decay
# System requirements:
# • Prebuilt Linux binaries (install script / GitHub release): glibc ≥ 2.38 + GLIBCXX_3.4.31 (GCC 13-era runtime — Ubuntu 24.04+ / Fedora
# 39+ / Arch; memvault-proxy additionally wants glibc ≥ 2.39). TLS is rustls, so no OpenSSL dependency. Ubuntu 22.04 / RHEL or EL8/
# EL9 users: use the Docker image ( dreamor/memvault ) or build from source.
# • Building from source ( cargo install / cargo build ): links fastembed's prebuilt ONNX Runtime static library and needs a GCC 13-
# class toolchain. Older toolchains (e.g. GCC 8, CentOS 7/8-era libstdc++) fail at link time with missing C++20/23 stdlib symbols
# ( std::format , std::to_chars ). macOS / Windows (MSVC) / Homebrew / Docker are unaffected.
# Verify your install in 5 seconds:
memvault-cli --version # memvault 0.3.0
# sanity check: list saved memories (verifies DB is healthy) memvault-cli list
# Local Ollama Demo (Zero Cost, Stays on Your Machine)
# MemVault is plug-and-play with a local Ollama: unconfigured LLM extraction (full-text understanding / failure reflection / relation extraction)
# auto-detects a local Ollama; embeddings use the local model with the ollama or auto provider.

---

## Page 5

# 1. Install and start Ollama brew install ollama && brew services start ollama # or the official installer
# 2. Pull models ollama pull nomic-embed-text # embeddings, 768-dim (default for ollama/auto) ollama pull qwen2.5:3b-instruct # chat: LLM extraction/reflection (default qwen2.5:7b, use 3b on small machines)
# 3. (Optional) Pin the providers explicitly — persist them in ~/.memvault/.env # (shell exports also work — env vars take precedence over the file — but the file survives reboots) mkdir -p ~/.memvault cat >> ~/.memvault/.env <<'EOF' MEMVAULT_EMBEDDING_PROVIDER=ollama MEMVAULT_LLM_EXTRACTION_PROVIDER=ollama MEMVAULT_LLM_EXTRACTION_MODEL=qwen2.5:3b-instruct EOF
# 4. Verify memvault status # Embedding provider: configured and reachable memvault save --content "Build server IP is 10.20.30.40" # output (embedded int8) memvault outcome --task "Deploy trading service" --status failure --cause "Disk space insufficient" --task-type deplo # → Lesson (Llm): ... means failure reflection ran through the local LLM (not the rule-based fallback)
# With no configuration at all (neither env vars nor ~/.memvault/.env ), LLM extraction auto-detects a local Ollama and enables itself (default
# model qwen2.5:7b ; pull it in advance with ollama pull qwen2.5:7b , or point MEMVAULT_LLM_EXTRACTION_MODEL at an installed model).
# Embeddings still default to the in-process native embedder; set MEMVAULT_EMBEDDING_PROVIDER=auto in ~/.memvault/.env to prefer Ollama
# and fall back to native when it isn't running.
# How It Works
# MemVault is a pipeline, not a single script. Every stage below is a shipping module:
Agent connects (MCP stdio/SSE) │ ▼ ┌───────────────────┐ │ Agent Router │ ← match agent type/tag → filter relevant memory │ (Agent Registry) │ └────────┬──────────┘ │ ▼ ┌───────────────────┐ │ Memory Retrieval │ ← keyword (BM25) + vector (embedding) + RRF fusion │ (3 search modes) │ synonym expansion · scoring · soft filtering └────────┬──────────┘ │ ▼ ┌───────────────────┐
| │ Auto-Injection | │ ← MUST-level → instruction prompt |  |
|---|---|---|
| │ | │ REFERENCE → context resource |  |
| │ | │ NORMAL | → search result |
   
│ │ REFERENCE → context resource │ │ NORMAL → search result └────────┬──────────┘ │ ▼ Agent receives context ──→ makes better decisions
# • Storage: SQLite with bundled FTS5 (full-text search); embeddings stored int8-quantized (~1/4 the size of f32 at near-identical ranking
# quality, legacy f32 rows still readable)
# • Retrieval: BM25 keyword search over FTS5 with CJK bigram tokenization (Chinese two-character words match correctly) and tiered match
# fallback (strict → relaxed unigram → synonym OR; relaxations are reported, never silent), local-first embedding (in-process native by
# default — switch to local Ollama or any OpenAI-compatible model), RRF fusion with per-result recall provenance ( kw#2 / vec#5 ), synonym
# expansion, relevance scoring, soft intent filtering
# • Pipeline: Automatic entity extraction, delta-write on save (near-duplicates skipped, similar memories absorb only the residual), semantic
# deduplication, time-based decay, archive of stale memories
# • Sync: Zero-invasion file generation — memvault sync produces CLAUDE.md, AGENTS.md, etc. directly from database contents

---

## Page 6

### What MemVault Gives You
• Auto-Injected Context: Session start automatically pulls relevant memory by agent identity — MUST-level rules land as instructions, not just chat history
• Hybrid Retrieval: BM25 + vector + RRF fusion with synonym expansion, relevance scoring, and per-result provenance (which path recalled each memory, at what rank) — available via CLI, MCP tool, and REST API
• Explainable Injection: every candidate dropped on the way into an agent's context is recorded with a reason (budget, caps, intent/type penalties) — "why didn't the agent get this memory?" always has an answer
• MUST Enforcement: MUST-priority memories are never filtered or truncated. Always in context, always obeyed — trust comes from provenance (human-authored/reviewed), with an opt-in fallback for memories independently corroborated by multiple identity-verified agents ( MEMVAULT_CORROBORATION_GATE ), so a single spoofed/compromised agent can't unilaterally inject a binding MUST
• Multi-Agent Awareness: Agent Registry with type/tag-based soft filtering (score demotion, not hard exclusion)
• MCP Proxy: Transparent proxy that injects memory into ANY upstream MCP server's responses — zero client changes
• Compliance Tracking: inject_session_id traces what was injected and measures follow-through rate
• Cross-Platform: CLI + MCP Server (stdio & SSE) + Web Dashboard (browser) + Obsidian Plugin
• Zero-Invasion Sync: Generate AGENTS.md / CLAUDE.md from memory — no per-agent config files to edit
• Contextual Extraction, Local-First: Rule-based keyword extraction by default; optionally understands a full user+assistant exchange via an LLM, auto-detecting a local Ollama for free before ever touching a remote API
• History & Rollback: Every update/delete is snapshotted into memory_history — memvault checkpoints + memvault restore roll one memory back without touching the rest
• Self-Diagnostics: memvault status reports exactly which features are degraded when no embedding provider is configured, plus a schema fingerprint (migration version + checksum) for cross-database comparison
• Episodic Memory: record_outcome records task results; failures are distilled into lessons and auto-injected next time (REFERENCE → MUST only with human approval), so the same trap isn't hit twice
• Procedural Skill Activation: skills whose trigger matches intent are injected as structured [SKILL] blocks with success-rate stats (shown after ≥3 runs); failures flag the skill for revision ( version++ on human edit), repeated successes auto-draft new skills into the review inbox
• Semantic Knowledge Links: lightweight relation triples, repeated facts consolidated into a linked semantic fact with provenance, and superseded facts archived (never re-injected, still listable & restorable)
• Team Shared Pool & SOP Import: memories marked shared are injected into every session (capped at 20); Markdown SOPs can be batch-imported as verifiable skills
force_insert bypasses
• Task-Level Evaluation: memvault bench samples your own failure history (episodes that distilled a lesson) and measures lesson retrieval/injection rates — and with --judge , an LLM scores "plan without vs. with memory" against the known failure cause, so you see task-success lift, not just retrieval recall
• Two-Phase Injection (never blocks): MUST rules resolve deterministically with zero embedding calls and are served immediately; the semantic pipeline prefetches in the background and lands within a short window (250ms) — if it doesn't, the deterministic baseline is served and the request moves on (two-phase design)
• Conversation-N-Gram Retrieval: retrieval keys are conditioned on the recent turn window, weighted by recency so the current focus dominates — not a single flat query
• Single Canonical Injection Channel: per-agent inject_channel ( mcp / proxy / sync in agents.yaml ) restricts automatic injection to one delivery path, so the same memory is never sent to the same agent twice
• Data You Own: Single SQLite file. Full export/import. No cloud dependency. Your data, your machine.
### Why MemVault
Feature Plain CLAUDE.md Vector DB + RAG MemVault
Context injection Manual edits Query-time only Auto on session start
Multi-agent sharing Copy-paste Separate indexes Single shared store
MUST enforcement None None Instruction-layer injection

---

## Page 7

Feature Plain CLAUDE.md Vector DB + RAG MemVault
Search modes File grep Embedding only BM25 + Vector + Hybrid
Synonym expansion No No Built-in
Deduplication No No Semantic dedup pipeline
Write-time delta merge No No Near-dupes skip, similar absorb the residual at save
Task-level evaluation None Recall metrics only bench : with-vs-without-memory task success delta
Decay / archival No No Time-based + auto archive
Memory extraction Manual N/A Rule-based by default; optional local-first LLM extraction
MCP native No No stdio + SSE + Proxy
Agent differentiation Global file Query filter Type/tag registry
Compliance tracking None None inject_session_id + rate
Self-hosted Yes Varies Single binary, no cloud
MemVault complements your existing agent setup rather than replacing it. Keep your LLM, your IDE, and your workflow exactly as they are. MemVault adds the memory layer underneath.
### MCP Server
Tier-1 agents (Claude Code, OpenCode, dsh, Gemini CLI, Codex) have one-command plugin installs — see Installing into your agents first. Everything below is the universal fallback for any other MCP client.
### stdio (any standard MCP client)
MemVault speaks plain MCP stdio — the same mcpServers JSON works verbatim in Claude Desktop, Cursor, Cline, Continue, and any other client that reads this format:
{
"mcpServers": { "memvault": { "command": "/path/to/memvault-mcp", "args": ["--db", "~/.memvault/data.db"], "env": { "OPENAI_API_KEY": "sk-..." } } }
}
A couple of clients use their own one-liner instead of hand-editing JSON:
# Claude Code claude mcp add memvault /path/to/memvault-mcp -- --db ~/.memvault/data.db
DeepSeek Harness (dsh) — a domestic (China) agent harness — gets deeper treatment than a generic stdio config: a native Cordis plugin ( dsh-plugin/ ) that auto-injects memory into the system prompt and auto-extracts at turn end, with no per-turn cooperation required from the agent. See docs/INSTALL.md §2.5 for both the zero-code MCP route and the deep-integration plugin.
Other MCP-compatible agents — international or domestic, IDE plugin or CLI harness — should work the same way: any client implementing standard MCP stdio/SSE can connect without MemVault-side changes. The ones above are the ones we've actually verified; if you get MemVault working with another one, a PR to this list is welcome.
### SSE (multi-client, network-accessible)
memvault-mcp --transport sse --port 3777 # Clients connect at http://127.0.0.1:3777/mcp

---

## Page 8

SSE features: multi-client simultaneous connections, auto-triggered embedding backfill on initialization, HTTP remote access.
Note: --transport sse only mounts the MCP-over-HTTP endpoint ( /mcp ) — it does not expose the REST API ( /api/* ). The Web Dashboard is served by the REST backend ( memvault-mcp --transport http --serve-web <dist> ), and the Obsidian plugin also uses the REST API and requires --transport http instead. See docs/INSTALL.md §2.6.
### 18 MCP Tools
Tool Description
bypass
| record_outcome | Record a task outcome (episodic memory); failures reflect into lessons |
|---|---|
| import_skills | Import skills from a Markdown SOP (headings → skills, list items → steps) |
| search_memory | Keyword / semantic / hybrid |
record_outcome Record a task outcome (episodic memory); failures reflect into lessons
  
search_memory Keyword / semantic / hybrid
another channel is canonical)
| review_memory | Approve / reject / edit |
|---|---|
| delete_memory | Remove a memory |
| extract_memories | Structured extraction from text |
| run_dedup | Deduplication scan |
| run_decay | Decay + auto-archive |
| confirm_read | Mark read (updates access_count) |
| list_inbox | List memories pending human review |
| run_promote | Promote pipeline (L1 → L2 → L3), archive sources to L0 |
| report_compliance | Report follow/violate status for an injected session |
| get_compliance_report | Compliance rates per session or aggregate |
| add_evidence | Record evidence relations: supports / contradicts / sourced_from |
review_memory Approve / reject / edit
delete_memory Remove a memory
extract_memories Structured extraction from text
run_dedup Deduplication scan
run_decay Decay + auto-archive
confirm_read Mark read (updates access_count)
list_inbox List memories pending human review
run_promote Promote pipeline (L1→L2→L3), archive sources to L0
report_compliance Report follow/violate status for an injected session
get_compliance_report Compliance rates per session or aggregate
add_evidence Record evidence relations: supports / contradicts / sourced_from
read-only grounding, so an agent can quote the original session text and name its sources
rates, judged from record_outcome ) — independent of the manual report_compliance flow
### 2 MCP Resources
URI Content
memory://user-profile MUST-level rules, auto-loaded on connect
memory://project-context REFERENCE-level project context
### Configuration (.env file & environment variables)
Copy .env.example to ~/.memvault/.env and uncomment what you need — it is also the single source of truth documenting every key.
Precedence (high → low): CLI flags > process environment > ~/.memvault/.env > built-in defaults. Every binary loads the env file first thing at startup; --env-file <path> or MEMVAULT_ENV_FILE points elsewhere, and a missing file is silently skipped. memvault status prints where each setting came from (env / file / default).
proxy.yaml ).
Variable Purpose Default

---

## Page 9

Variable Purpose Default
native compatible (any OpenAI-compatible endpoint)
native local model)
https://
|  | Any OpenAI-compatible base URL (OpenAI / Azure / vLLM / | api.openai.com/v1 / |
|---|---|---|
| MEMVAULT_EMBEDDING_API_BASE | gateway...). For ollama / local the embedder uses Ollama's | http:// |
|  | native endpoint http://localhost:11434/api | localhost:11434/api |
api.openai.com/v1 /
bge-small-zh
|  | Embedding model: bge-small-zh (zh, ~95MB) / | (native) / nomic- |
|---|---|---|
| MEMVAULT_EMBEDDING_MODEL | multilingual / e5-base for native; nomic-embed-text (768- | embed-text (Ollama) / |
|  | dim) for Ollama; or any model name for API providers | text-embedding-3- |
small (API)
768 (local/Ollama) / MEMVAULT_EMBEDDING_DIM Vector dimensions 1536 (API)
Optional: enables LLM-based contextual memory extraction (understands a full user+assistant exchange, not just keyword lines). Unset/ auto → local-first: auto-detects a running local
|  | Ollama and uses it for free, no config needed; falls back to | (unset — local-first, |
|---|---|---|
| MEMVAULT_LLM_EXTRACTION_PROVIDER | rule-based if none is running. openai / openai-compatible / | rule-based if no local |
|  | custom → explicit remote provider (never auto-enabled just | Ollama) |
(unset — local-first,
  —   remote calls cost
  off   /   disabled   /   none
force pure rule-based, even if local Ollama is running
MEMVAULT_LLM_EXTRACTION_MODEL api.openai.com/v1 / gpt-4o-mini
contradicts / sourced_from triples
force_insert
retrieval key used by proxy auto-injection
reach before it saves anything. 0 disables the gate — extracts on every Stop, as before this existed
decisions
MEMVAULT_CORROBORATION_MIN_AGENTS ) is treated as trusted

---

## Page 10

Variable Purpose Default
even without human review. true turns it on — off by default, so is_trusted output is unchanged unless you opt in
corroboration gate above
MEMVAULT_DB_POOL_SIZE SQLite connection pool size 5
(localhost only) localhost only)
$MEMVAULT_HOME/ data.db when
MEMVAULT_DB SQLite database path MEMVAULT_HOME is set,
else   ~/.memvault/
data.db
RUST_LOG Log verbosity info
— it can't be set inside the .env file itself (a file can't define its own location)
(e.g. https://hf-mirror.com on CN networks)
confidence — nothing agent-produced is trusted before human (on — downgraded) review). off / disabled / false / 0 disables extracting from agent responses entirely
### CLI Reference
save · outcome · search · list · review · delete · session-start · resource · extract · dedup · decay · doctor · promote · backup · export · import · import-skills · import-agent · ingest · confirm-read · sync · checkpoints · restore · supersede · status · bench · eval-history
memvault <command> --help # detailed usage per command
### Key Commands
Command What It Does
memories absorb the residual; --force to bypass
| outcome | Record a task result (success/failure/partial); failures are distilled into lessons that auto-inject into similar future tasks |
|---|---|
| search | Hybrid retrieval with relevance scoring; flags: --query , --top-k , --namespace |
| session- | Simulate what context an agent receives on connect; a multi-line --context is treated as a turn sequence and |
| start | weighted by recency |
| extract | Parse free text, extract structured memories |
| import- | Import skills from a Markdown SOP ( # / ## headings → skills, list items → steps); enters the review inbox unless -- |
| skills | approve |
outcome Record a task result (success/failure/partial); failures are distilled into lessons that auto-inject into similar future tasks
   
 
extract Parse free text, extract structured memories
Import skills from a Markdown SOP ( # / ## headings → skills, list items → steps); enters the review inbox unless --
inbox unless --approve

---

## Page 11

Command What It Does
per-session watermark means each turn is processed once. --dry-run to preview, --approve to skip the review inbox, --agent / --home / --max-sessions to scope
sync Generate agent instruction files (AGENTS.md / CLAUDE.md / MEMORY-INDEX.md, …) from memory (with --watch )
dedup Scan and merge semantically duplicate memories (vector-assisted when an embedding provider is configured)
checkpoints List memory history snapshots (per-memory or global); flags: --memory-id , --limit
restore Revert a memory to the state captured by a checkpoint ( --history-id )
supersede Archive an old fact and point it at its replacement (nothing is deleted; search skips superseded, list keeps them)
and which features degrade without it
doctor Read-only memory hygiene lint: dangling/stale/duplicate/contradicted + machine-readable --json
adds an LLM-scored "plan without vs. with memory" success delta; each run persists itself for eval-history
accumulated
| outcome | Record a task result (success/failure/partial); failures are distilled into lessons that auto-inject into similar future tasks |
|---|---|
| decay | Archive stale memories based on access recency |
| backup | Create a consistent point-in-time SQLite backup |
| export / | Backup and restore — JSON to a file or a directory (writes export.json inside); Markdown to/from a directory or a |
| import | single .md file; import is idempotent (ids already present are skipped, never overwritten) |
| confirm-read | Mark memories as read (updates access_count) |
decay Archive stale memories based on access recency
backup Create a consistent point-in-time SQLite backup
export /
confirm-read Mark memories as read (updates access_count)
### Integrations
### Installing into your agents
MemVault ships native adapters for most agents — one shared store, per-host identity via MEMVAULT_AGENT_ID , four tiers (Tier 1/2/3 details below; per-client registration snippets in integrations/mcp-clients/).
Core packages & versions:
Package Version Install / Source
memvault-core (crates.io) 0.4.0 library dependency
0.4.0 (crates.io) proxy
@dreamor/dsh-memvault (npm) 0.4.0 npm registry (dsh Cordis plugin, below)
Shipped plugins & versions — each bumps on its own schedule:
Plugin Version Distributed via
Claude Code / Codex plugin bundle ( plugins/memvault/ ) 0.3.0 dreamor/memvault marketplace
Gemini CLI extension ( gemini-extension.json ) 0.4.0 gemini extensions install
Qoder plugin ( .qoder-plugin/ ) 0.4.0 in-repo manifest
Obsidian plugin ( obsidian-plugin/ ) 0.3.3 dreamor/memvault-obsidian (BRAT / community dir)
dsh Cordis plugin ( dsh-plugin/ ) 0.4.0 npm @dreamor/dsh-memvault
Tier 1 — one-command native plugins (memory injected by hooks; extraction opt-in where the host exposes lifecycle hooks):

---

## Page 12

Agent Install Recall Extract
commands
merge integrations/opencode/opencode.json into your OpenCode system transform on session.idle project
DeepSeek built-in Cordis plugin dsh-plugin/ — see docs/ Harness system prompt turn-end INSTALL.md §2.5 (dsh)
tools
SessionStart hook then install memvault@memvault from the plugin browser Stop hook bundled; verify Codex CLI (trust bundled hooks — the same plugins/memvault/ bundle; manual fallback behavior on Codex on first run) in integrations/codex/
= the host has no injection hooks; recall is rule-driven (the agent calls session_start once) with the bundled canonical rule text.
Tier 2 — paste an MCP snippet. Strict-JSON registrations with per-host identities in integrations/mcp-clients/ (target paths in its README): Cursor · Windsurf · Cline/Roo · Continue · Zed · JetBrains AI/Junie · VS Code (Copilot Chat) · Claude Desktop.
Tier 3 — native manifests, verify-on-install. Qoder ( .qoder/rules/ + .qoder-plugin/ + a UserPromptSubmit hook template), Grok Build ( grok plugin install dreamor/memvault --trust ), the Hermes Python plugin (integrations/hermes/, pre_llm_call recall + extraction helper) and the pi extension ( pi-extension/ , pi install git:github.com/dreamor/memvault ) ship in-repo; OpenClaw and Swival consume the generated root skills/ (also exported to .openclaw/skills/ ); Devin stays a manual recipe in integrations/README.md.
Tier 4 — instruction-only rule copies. Canonical text + scripts/gen-rule-copies.sh (parity-checked in CI) produce AGENTS.md / CLAUDE.md blocks, .cursor/rules/ , .clinerules/ , .kiro/steering/ , Junie guidelines; memvault sync --watch keeps them fresh from the store.
Any other MCP-speaking client (domestic or international, IDE plugin or CLI harness) connects with zero MemVault-side changes via the standard stdio config below — not individually verified; PRs adding a verified entry are welcome.
GUI surfaces are independent of agent installs: Web Dashboard (9 tabs) · Obsidian plugin (α — Vault sync + browse/capture) · MCP Proxy (transparent memory injection for any upstream server).
### Architecture

---

## Page 13

┌────────────────────────────────────────────────┐
| │ Clients (any MCP-compatible agent) | │ |  |
|---|---|---|
| │ ┌────────────┐ ┌────────┐ ┌─────┐ ┌────────┐ |  | │ |
| │ │ Claude Code │ │ Cursor │ │ dsh │ │ Others │ | │ |  |
| │ └────────────┘ └────────┘ └─────┘ └────────┘ |  | │ |
│ │ Claude Code│ │ Cursor │ │ dsh │ │ Others │ │
└──────────────────┬───────────────────────────────┘
│   MCP   (stdio   /   SSE   /   HTTP)
┌──────────────────▼───────────────────────────────┐
│   memvault-mcp   (rmcp   3.1.1) │
│   ┌────────────────┐ ┌────────┐   │
│   │   18   tools   │   │   2   Resources   │   │   SSE   │   │
│   │   +   REST   │   │   +   Auto-Inject   │   │   Server   │   │
│   └──────┬─────────┘ └────────┘   │
│ └────────┬───────┘ │
│   ┌───▼────────┐ │
│   Agent   │   (Agent   Registry │
│   Router   │   type/tag   filter)   │
│   └───┬────────┘ │
├──────────────────┼────────────────────────────────┤
│   memvault-core   │ │
│   ┌──────────┐   ┌─▼───────┐ ┌────────────┐   ┌───┐   │
  2 │   │   storage   │ retrieval │   │   pipeline   │   │ sync │   │
│   │   SQLite   │ BM25+Vec   │   │ extractor   │   │   │   │
  Latest
│   │     │ RRF+syn   │   │ dedup/decay   │   │   │   │
2 weeks ago
│   │ embed   │ onym   │   │ export/   │   │   │   │
Packages 1
memvault
# Project Status
Contributors 1
# MemVault is in beta. The Rust core (storage / search / injection) is CI-gated and stable; plugin adapters and GUI surfaces evolve faster. All
dreamor Scott
# configuration is environment-driven (see .env.example ), and every change is recorded in CHANGELOG.md.
# LanguagesTesting
cargo test # ~1000 tests (full workspace) cargo clippy --all-targets # zero warnings cargo fmt --all -- --check # format check cargo llvm-cov --workspace --all-features # CI gate: line ≥92% / region ≥90% / function ≥85%
# Documentation
# Doc Content
# docs/DESIGN.md Product & architecture design
# docs/INSTALL.md Installation guide (all platforms)
# docs/DOCKER.md Docker deployment
# docs/RUNBOOK.md Deployment / health check / rollback runbook
# docs/
# Symptom → cause → fix troubleshooting guide
# TROUBLESHOOTING.md
# Hypothesis-validation experiments (H1–H7, 2026-08-11 → 2026-08-27, all CONFIRMED) + runtime
# docs/experiments/
# plumbing regression (2026-08-28)
# Release process — what CI automates (Linux/macOS binaries, Docker image, dashboard archive, Obsidian
# docs/RELEASING.md
# zip) vs. manual steps (Obsidian submission — no macOS signing needed)
# Distribution channel map — automated vs. manual channels, required credentials, MCP registries, optional
# docs/DISTRIBUTION.md
# channels

---

## Page 14

Doc Content
CHANGELOG.md Release history
CONTRIBUTING.md Contribution guide
SECURITY.md Security disclosures
.env.example Configuration template — single source of truth for every config key
## Contributing
• Bugs: Issue Tracker
• Ideas: Feature Request
• Guide: CONTRIBUTING.md
• Security: SECURITY.md
## License
MemVault is released under the MIT License.