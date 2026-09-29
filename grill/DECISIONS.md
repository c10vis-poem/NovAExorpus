# Grill decisions

Operator decisions from the D.U.M.B.A.S.S. grill sessions, with the date and source of each. Terms are defined in `/CONTEXT.md`.

## 2026-09-29

- **Q5, OmniRoute's own SQLite and memory tables:** they stay and do their own job. Memory is not moved out of OmniRoute.
- **The four memory layers are separate MCP servers:** mem0, OB1, Graphify (`graphify.serve`) and code-review-graph.
- **ReasoningBank is an OmniRoute plugin** with its own judge and store. The operator first chose "its own MCP server", then reversed it the same day after weighing the trade-offs. Reason: every request through OmniRoute is captured and refined whether or not the agent cooperates, while a Claude Code integration would just ignore recommendations. Starting point: the 2026-09-26 draft in `recovered/2026-09-26-ob1/omni-feat/dumbass-plugins/reasoning-bank/`.
- **Continual Harness is its own operation**, not folded into OmniRoute. Its scope is still open.
- **The Auditor** (on-device) only flags prompts that Claude didn't complete as instructed. It stores nothing and has no overlap with ReasoningBank.
- **ECC is parked** at `~/.claude/ecc-parked/` pending the operator's review. It is not deleted.
- **What ReasoningBank judges against:** ground truth, never just the agent's word. It judges more than the task outcome; it also judges whether the whole pipeline ran properly:
  - did OmniRoute route it properly;
  - was any available tool ignored;
  - was any skill loaded but not used;
  - did the episodic memory write (mem0) actually happen;
  - did OB1 actually register the write in Supabase;
  - and similar checks.
  
  Each check is verified against the system that owns it (OmniRoute's own records, mem0, Supabase), not against the agent's claim.
- **Æsop-Xi (Agentic Executions Split Operation Protocol) is the home for all of it:** OmniRoute, ReasoningBank (its own folder with subfolders, including its judge checklist), the four memory tools, the log-writing rules, where the SQL databases live, the D.U.M.B.A.S.S. protocols and the pipeline. Source: operator, 2026-09-29.
- **ReasoningBank has no crash recovery.** `aesop-xi/CLAUDE.md` calls it a "multi-model execution ledger, crash recovery (resume from step N+1)". The ReasoningBank repo never claims that; a search for crash, recover, resume and ledger finds nothing relevant. That description was invented by an agent and is to be removed from aesop-xi. The operator's position: agent-written hard rules should never have been written.
- **Keep ReasoningBank's own lesson-writing rules** (`reasoning-bank/WebArena/prompts/memory_instruction.py`):
  - explain why the run succeeded or failed before writing any lessons;
  - at most 3 lessons per run, with no overlapping lessons;
  - prefer concrete, actionable steps over abstract principles;
  - keep task-specific names and strings out of lessons;
  - each lesson has a title, a "when to use and when NOT to use" line, and 1–3 sentences of content.

  Also keep the retry when the judge's reply isn't in the expected format (as in `WebArena/agents/legacy/agent.py`).
- **The judge checks whether the run followed the expected path:** the steps it actually took, in order, against the steps it should have taken. One example is the pipeline order (read memory, then act, then write back, then log). This sits alongside the individual pipeline checks.
- **Leave ReasoningBank functioning as designed**, including its own model settings (model name or path, `model_url`). Don't strip them out in favour of OmniRoute. Those settings are simply pointed at whatever model is chosen: a local model file, or OmniRoute's endpoint. Still to check when building: whether its `model_url` accepts OmniRoute's OpenAI-compatible endpoint.
