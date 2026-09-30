# CLAUDE.md — AESOP — memory protocol layer

> **THIS IS WHERE WE'RE AT.** The State of the Union for this folder, in the same
> **W5+H** schema as the blueprint — so target and status line up header for
> header and the gap is readable at a glance.

## Gospel

**[`../canon/MASTER-BUILD-BLUEPRINT.md`](../canon/MASTER-BUILD-BLUEPRINT.md)** is
the target: the W5+H universal blueprint (§1), the build map (§12.1), the action
chart (§12.2), the flip chart (§12.3), the file architecture (§12).

**This folder is a comparison against it.** Same six headers below. If this folder
and the blueprint disagree, the blueprint is the target and this is the status.

---

## State of the Union — W5+H

### WHO
Novus-Agenti reads and writes through this layer. No component touches another's memory directly (Rule 3).

### WHAT
**OB1** — structural, the protocol governing how memory is doled out. **mem0** — episodic, user/session/agent state. **OmniRoute** — the gateway both operate from; SQLite FTS5 + int8 vectors + typed decay, MCP and A2A. **reasoning-bank** — a *pattern*, not a backend: Title/Description/Content, and learning from failed trajectories.

### WHERE
Node Beta hosts the OB1 vector backend on Postgres. OmniRoute fronts everything. mem0's dual-agent architecture lives on Node Alpha.

### WHEN
Every turn: episodic state written, structural context read — both through OmniRoute, never inline with inference (blueprint §12.2).

### WHY
One gateway instead of each component wiring its own memory. It is what makes Rule 3 enforceable rather than aspirational.

### HOW
Agents call OmniRoute; it dispatches structural to OB1 and episodic to mem0. Per-request opt-out via `x-omniroute-no-memory`.

---

## Delta

**Open:** does OmniRoute's own memory stay on as local cache / offline fallback, or get disabled per request? Nothing here is wired yet.

**Build state is not recorded here.** It is recorded once, in
[`../canon/STATE-OF-EXISTENCE.md`](../canon/STATE-OF-EXISTENCE.md). No folder
asserts its own status.

---

## The kit

| File | Holds |
|---|---|
| `README.md` | what this folder is, for a human |
| `CLAUDE.md` | **this file** — where we're at, W5+H, for an agent |
| `llm_wiki.md` | machine-facing index, generated not hand-written |
| `skill_manifest.json` | structured metadata |

## Working rules

- **Read everything, completely, before acting** (Rule 0).
- **One axis on disk** — organised by **domain**. Format tier and corpus type are
  frontmatter tags, never folders.
- **Four-artifact documents** — `name.pdf` + `name.md` + `name.jsonl` (when large)
  + `skills.md`. **Same basename = same document** is the audit's join key.
- **Metaphors:** behavioural ones never become enforcement code; visual references
  supplied with a picture *are* literal specs and get built exactly (Rule 7).
- **Verify mechanically** (Rule 4). Your own report is not evidence.
