# AGENTS.md

Repository: `NovAExorpus`

Authority: NovÆxorpus Master Canon Specifications

## RULE 1 — NO ACTION WITHOUT AN EXPLICIT PROMPT

A skipped or unanswered question is NOT consent. No action — reading,
searching, or anything else — without an explicit prompt or permitted
request. State-changing or not, it doesn't matter.

## RULE 2 — READ THE REPO'S OWN CLAUDE.MD AND RESUME.MD FIRST

Before doing anything else in any of the operator's repos — before
investigating, before answering a question about that project's state —
check for and read that repo's own CLAUDE.md and RESUME.md. This has been
the operator's standing convention for session handoff and current state
across their repos for months. It is not optional background reading; it is
step one, every session, every repo, no exceptions.

## GH workflow (every repo)

1. Feature branch (never commit to `main`/`master` directly).
2. Before every push, scan the diff for secrets/API keys; refuse to push if found.
3. Push, open a PR, track CI.
4. On green CI, auto-merge into `main` immediately.
5. Leave the branch in place after merge — do not delete it.
6. Forked repos: at the start of every session, sync the fork's default
   branch from `upstream` before any other work.

Source: operator-confirmed 2026-09-13.

## Cross-engine compatibility (tool-agnostic)

- **Honey for Devs applies universally** — natively in Claude Code, as a
  text-strip layer in Codex, as a Cordis plugin in DeepSeek Harness (dsh).
- **task-observer / GSD-style skill scaffolding is Claude-Code-only.** Codex
  and dsh cannot parse markdown skill wrappers.
- Claude Code and any local engine are never active in the same repo
  directory at the same time.

## Agent roles (engine-neutral descriptions)

### corpus-architect

Full-stack agent for corpus operations — reading, reconciling, and editing
documents across the NovÆxorpus federated repo set. Has access to all
memory servers (mem0, terrestrial-brain, code-review-graph, omniroute) and
all file tools. Deep reasoning over large document sets.

### builder

Implementation agent for code changes, deployments, and infrastructure
work. Full tool access including shell. Used for: gateway config, VM
management, script writing, repo setup.

### reviewer

Read-only audit agent. Reviews code, docs, and architecture for
correctness, consistency, and compliance with the 5+1 cognitive tier
model. Reports findings without making changes.

## Unified orchestration pipeline (router-guard)

Every agent, regardless of engine, flows through one pipeline
(see `output-style.md` pages 15-33 for the original specification;
canonical file: `.claude/output-styles/router-guard.md`):

```
[Agent] → honey + task-observer (pre-flight)
  → OmniRoute (gateway, routes to all backends)
    → mem0 / terrestrial-brain / code-review-graph
    → Reasoning Bank (passive execution ledger, crash recovery)
    → Continual Harness (passive prompt refinement, auto-rollback)
```

- **Pre-flight:** honey-for-devs (token compression) + task-observer (task mapping) gate all code output.
- **Gateway:** OmniRoute (port 20128) handles routing to all memory/code-intelligence backends.
- **Backends:** mem0 (episodic), terrestrial-brain (structural/Postgres), code-review-graph (AST/blast-radius).
- **Passive infra:** Reasoning Bank (execution ledger, crash recovery) and Continual Harness (prompt refinement, auto-rollback) run underneath — agents don't invoke them.
- **Secondary tools:** graphify, obsidian, notebook-lm — on-demand, not per-prompt.

All engines (Claude Code, DeepSeek, Qwen, Hermes) hit the same pipeline
and the same backends. Only the loader differs per engine.
