# Reading log: Documents/_File-Driven-Agent-Operating-Environment (session 8e3a65ec, from 05:51)

Folder: 13 folders, ~280 md/txt (Inventory = 113 GB model weights, not read). Each file below read in full.

## Read so far (12 files) and what each gives the memory build
1. `_README.txt/Copy of Memory-as-skill v-next design brief.docx.txt` (2026-10-29): memory = plugin with read-only
   SessionStart + nudge-only Stop; canonical memory in git (md + JSONL); pointer manifest `memory/layers.jsonl`;
   12 parts from 11 plugins (anchor-memory, continuity, whydone, llm-wiki, memory-agent, create-smartfolder,
   memory-toolkit, claude-memory, context-distill, cut-weight, drunken-master) = what nvaex-memory already holds;
   5 patterns to strip (silent save, auto-commit, blocking Stop, background transcript upload, one-machine store).
   9 open questions (layers.jsonl place, delivery, one vs several plugins, settings.jsonl, handoff format, ...).
   NOTE: its off-switch list conflicts with the owner's later "no switches" order.
2. `plan-docs/Rev.Eng.ify (1)/Copy of Continual-harness.txt`: the "heart": ContinualHarnessHeart python class:
   SHA-256 gate + registry `vault/.dumbass/sha256_registry.txt`; episodic SQLite `execution_timeline(session_id,
   action, payload_hash, status, confidence)`; compaction = Headroom (trace trim), Honey for Devs (filler strip),
   Ponytail (minimal code); Jev triage (route: local_tree_sitter | browser_cdp_inference | cloud_frontier) with SHA
   dedup first; OB1 governance strike; raw-CDP browser inference; MCP trio (continual-harness-core,
   code-review-graph, postgres-supabase-hub). Draft code, not run (bugs: python uses process.env, asyncio unimported).
3. `_Target-planning_objectives/Local-first-multi-agent-state-MACHINE.md`: 6 layers; Layer 2 = Supabase +
   static SQLite + episodic SQLite + tree-sitter/Graphify; Layer 4 = Prime Agent (recursive only) + Reasoning Bank +
   Continual Harness + task-observer at the end; Phase B "quad-stream fan-out" on every request: episodic, static,
   code graph, knowledge graph (Graphify-Obsidian + Supabase). Names "Halogen Engine" (algebraic, non-regex
   extraction) = likely the owner's "holograph". ob1 & mem0 stripped of cloud sync, run from local SQLite.
4. `Cloudflare/cloudflare_memory_stack_deployment_guide.md` (+ identical copy in plan-docs): vault md + manifest.jsonl
   in R2 bucket `obsidian-vault`; Worker MCP (`get_manifest_index`, `read_vault_note`, `search_memory`); bearer secret.
5. `Cloudflare/obsidian_cloudflare_mcp_architecture.md`: keep hooks local, host corpus + tools on Workers, pointer
   manifest for near-zero start context.
6-8. `Plan-Order-1,2&3/BUILD-ORDER-1/2/3.md`: Order 1 = NPU models (EG2 270M/440M/740M run on HTP v79; EG2 server
   written never started, port 8085; Qwen 3.5 0.8B on HTP0 via GenieX 39 tok/s, not served; JEV not live).
   Order 2 = wiki admin endcaps (rules, MCPs incl. reasoning bank, mods, Æsc). Order 3 = housekeeping, Cialdini +
   RLVR, lane D "Continual Harness = our REA versions of Prime Agent and ECC agents keeps state outside the model",
   lane E memory per harness (SQLite, Postgres, SHA-256, Supabase).
9. `plan-docs/Rev.Eng.ify (1)/Copy of Rev.eng-core.txt`: bootstrap loop: code-review-graph AST -> Jev/REA tags each
   function (hook / plugin / skill) -> #dumbass Postgres with SHA-256 dedup at table root; MoE board (Fable 5.1
   architect, DeepSeek V4.1 Flash adversary, Gemini 4 Argon arbitrator) writing to episodic DB.
10. `plan-docs/Rev.Eng.ify (1)/Copy of Deconstruct-schema.txt`: Mem0-Lite (SQLite `episodic_facts(entity, fact,
   UNIQUE)` + recall/update), OB1-Lite (pre-flight stop gate from `ob1_rules.json`), notebooklm chunker (header
   split, sha256 chunk_id, wikilinks); tool schemas mem0_recall, ob1_intercept.

## Vault 01-inbox reports from session 3c1dfa47 / a5b45d30 (read in full 05:56)
compiled/WIKI-ADMIN-REPORT-2026-11-12.md, compiled/PLAYBOOK.md, corpus-survey/inventory.md, part2-plan.md,
vendors-and-models.md. Adds over my catalog: runtimes (GenieX serve 127.0.0.1:18181/v1; LiteRT-LM 0.18.1 eg2 server
:8085; llama-server; ORT+QNN; LocalAI), copies outside Inventory (~/models-npu, ~/downloads, ~/gemma-e2b, ~/gemma-12b),
agy (Antigravity CLI, logged in) as the bulk route, OpenRouter models, 26 greedy-crane audit items (none approved),
8 owner questions (unanswered), Assets-Index POINTER.md for ecc, mem0, omniroute, prime-agent, terrestrial-brain.
Owner rule seen there: Qwen 3.5 only (no Qwen3 / Qwen3-VL).

## Ingest pipeline run (wiki-admin-ingest), work dir ~/repos/wt/fdaoe-ingest
- Injection scan: 277 files; 1 quarantine (Greedy-crane/Wiki.Admin/Untitled.html, hidden-html); 36 soft review.
  Scanner defect: --out appends instead of overwriting (repeated rows when re-run).
- Convert: 242 converted; 11 unsupported (code .py/.js/.bash, one .jsonl, 5 zips incl.
  NvAEx-hologram-cognitive-main.zip = the holograph source). Workers read those raw.
- Ledger: 11 batches (b001-b011). b001-b004 running (Sonnet corpus-ingest) since 05:5x; findings -> findings/bNNN.md.

## Not read yet
_Jev (144), Greedy-crane (34), Jev Observation Database (10), Cialdini (20), embeddinggemma-2- (7),
Live OpenRouter (6), More-Argon-Builds (4), plan-docs: Local.core.nodes, SystemBlueprint, Architecture planning (3),
FABLE brief, Dynamic Workflows (38K), notebooklm chunk, #; _Target: Agent Engineering, Archive & JEV Stage-0,
agent_architecture_report; _README: HyperionXi, repo map, Mobile Extraction, local_agent_architecture_blueprint (50K);
gcloud_auth_login.
