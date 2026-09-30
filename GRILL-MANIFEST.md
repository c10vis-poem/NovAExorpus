# GRILL-MANIFEST — agenda for the grill-with-docs session

**Nothing is off the table. Everything needs to be reviewed.** (operator, 2026-09-28)

This file is the agenda: what the grill session must cover. The results live
where `/grill-with-docs` writes them — `CONTEXT.md` (glossary) and
`docs/adr/` (decisions). When a topic is settled, tick it and link its ADR.

Sequence: `/setup-matt-pocock-skills` → `/cleanmyharness` →
`/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`.

## Ground rules

- Documents 00–05 contain inconsistencies and incorrect statements. Never cite
  them as truth (AGENTS.md Rule 3).
- Fewer than ~150 corpus files have honestly been read; 1,000+ remain
  (AGENTS.md Rule 4). Every claim names the file it was read from.
- Canonical names (`NAMING-CANON.md`): NovÆxorpus, NovusÆxenti, NovÆxopia,
  Æsop-Xi, Æsc, Æyre, Horizons-Ui.

## Topics

- [ ] **1. Corpus read-through.** Actually read the remaining 1,000+ files and
  implement them into the plan. Read ledger: file → read by → what it changed.
  ADR:
- [ ] **2. Rebuild documents 00–05** from what the read-through establishes.
  ADR:
- [ ] **3. Enterprise repos — rebuild or build every repo**, addressing all
  open issues; renames to canonical GitHub names (`NovusAExenti`, `AEsop-Xi`,
  `AEsc`, `AEyre`, `Horizons-Ui`); CLAUDE.md folded into AGENTS.md.
  ADR:
- [ ] **4. Agent harnesses.** Hermes, DeepSeek Harness and Antigravity become
  the managing agents; Claude Code becomes a builder tool they call.
  ADR:
- [ ] **5. LLM wiki** across the entire corpus and every repo; configuration of
  the OpenWiki replacement (candidate `jatinmayekar/openwiki-for-claude-code`,
  fork first).
  ADR:
- [ ] **6. Files execution mandate** — define it and how it is enforced.
  ADR:
- [ ] **7. D.U.M.B.A.S.S. orchestration mandates** — the fan-out below,
  Reasoning Bank, Continual Harness, Task Observer's OmniRoute half
  (`observation_log`), OB1 with Supabase on the Jetson Orin Nano Super,
  router-guard. Prior draft: orchestration contract v0.1 (Æsop-Xi PR #18);
  plugin drafts in `recovered/2026-09-26-ob1/`.
  ADR:
- [ ] **8. Æsop-Xi master definitions and orchestration layer.**
  ADR:
- [ ] **9. Three-APK topology** — one definition, so the corpus stops saying
  five different things.
  ADR:
- [ ] **10. Infrastructure build plan** — Oracle and the Google Developer
  $1,000 credits; where the VM, Jetson and phone each fit.
  ADR:
- [ ] **11. Launch script** — upgrade `tools/launch.sh`: live VM IP, checks that
  stop the launch when a layer is down, starts in the vault, ships at exit,
  starts whichever engine topic 4 decides.
  ADR:

- [ ] **12. Session enforcement / auditor.** A customized Happy Ending skill
  for session close (RESUME.md full rewrite, unresolved → PENDING.md), and
  the designed-but-unbuilt on-device auditor agent (small/nano model) that
  checks the managing agent actually follows directions: loads tools, runs
  skills, does session open/close and the GitHub workflow. Is it redundant
  with OmniRoute's schema, guardrails and audit log, and with Continual
  Harness? Prior design: the Official / Red Auditor pair (in Doc 00 — treat
  as unverified per Rule 3).
  ADR:

## Fan-out as stated by the operator (input to topic 7)

OmniRoute runs its compression plugins first (RTK, Caveman, and a third —
likely Headroom or OmniGlyph), then plan mode, then its multi-agent options
hand data to four MCP tools in parallel.
Open: Ponytail instead of Honey-for-devs on the back end? A customized Happy
Ending skill to wrap up sessions?

| Layer | Tool | Handles |
|---|---|---|
| Episodic — "what you did" | Mem0 | session action history, LLM-extracted episodic memories |
| Semantic + governed — "what things are" + "who said it, when, under what policy" | OB1 | facts, provenance, use-policy, audit, recall-trace, cross-tool shared memory, schema-aware routing, AI gateway |
| Navigational — "how you get there" | Graphify | concept graph, Leiden communities, god nodes, shortest paths, no embeddings |
| Structural — "what breaks if I touch this" | code-review-graph | AST blast radius, dependency flow, call graphs, SQLite |
| Governance + continuity (overlaps) | OB1 OpenClaw recipes | Agent Memory API, Code Review Memory, TaskFlow Work Log |
| Gateway / model routing | OmniRoute | 359 providers, 1200+ models, 110 MCP tools, parallel tool_calls |
| Recursive training | ReasoningBank | strategy extraction from trajectories, MaTTS parallel scaling |
| In-place harness mutation | Continual Harness | CRUD on prompt/skills/memory mid-episode via Refiner LLM |
| Observation | Task Observer | session watching, correction capture, pattern extraction |

OB1 is also the governance layer with its own routing intelligence: its Agent
Memory schema (provenance, use-policy, recall-trace, audit) and Schema-Aware
Routing tell you who said it, under what policy, and which table it belongs in.

## Already enforced

GitHub workflow — fork sync at session start; once at session end, GitHub
secret scanning → CI → PR → auto-merge on green; nothing left unmerged; rules
never changed without the operator (`~/bin/sync-forks`, `~/bin/ship-session`).
