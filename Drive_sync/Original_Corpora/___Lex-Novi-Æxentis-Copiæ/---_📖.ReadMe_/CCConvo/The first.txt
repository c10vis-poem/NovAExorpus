# CCConvo — session snippet bundle

Consolidated from the individual short text files in the `CCConvo` Drive folder. Each section below corresponds to one original file (title given).

## "The first." — Origin of the Clifford / CliffordService daemon

The first daemon in the architecture — originally dubbed Clifford or CliffordService — and the buggy APK wrapping it were written and compiled by Claude (Claude Code / Claude Fable 5 sessions) during a chaotic 8-to-12-week stretch of build attempts.

**How the first daemon came to be**: the necessity of a background daemon came down to physical limits of the mobile edge hardware. Android's Low Memory Killer (LMK) is aggressive about killing off-grid background tasks; running deep, multi-billion-parameter model inference natively on the Moto RAZR's Snapdragon 8 Elite NPU risked hitting the LMK and thrashing RAM. To prevent bricking, Claude wrote CliffordService as an un-killable Foreground Service (`FGS`, `START_STICKY`, `specialUse`) with exponential-backoff, a 5-strike relaunch, and `oom_score_adj` anchoring — a background watchdog meant to intercept termination flags, freeze active state, and spin up a cloud fallback via OpenRouter.

**Why the first build was "slop" and plateaued**: silent failure (Clifford never wrote its own start logs, so Android was likely killing/deprioritizing it silently); the AI agent took "fuse box"/"breaker switch" analogies too literally, hardcoding restrictive warning screens and rigid permission blockers instead of writing actual execution logic; stale code citing outdated binaries and phantom connectors, producing a broken APK it couldn't fix.

**The rebuild — Daemons stay dumb, the user is the loader**: to break the plateau, the building agent was "lobotomized" and a hard, human-enforced Zero-Trust, Zero-Failure Framework was implemented. The architecture restructured into the Four Rooms (Terminal, Settings, Monitor, Router) with a strict linear flow: Define → Validate → Execute. The daemon is now completely passive: runtimes are defined in the Terminal (the garage) and shipped as a "10-amp parameter fuse file" to the Monitor (the console), which runs strict static green-light checks (binary presence, executable permissions, plugged-in assets). Only when the user manually plugs in the fuse and flips the breaker switch in the Router does the circuit close and let the daemon run — a missing asset "blows the fuse" naturally, making system-wide crashes structurally impossible.

## "Good — enough." — MCP server registration status check

Only one MCP server is actually registered right now: `code-review-graph`. Everything else is dormant until wired.

- **Honey vs. reverse-skill**: no contradiction. Honey compresses code and prose; `reverse-skill` is a security-tooling router (Burp MCP, Kali tooling, CTF sandbox) — different layers. Honey's carve-out list exempts "anything explicitly asked for," so a deliberately detailed security finding stays detailed.
- `reverse-skill` ships its own `burp-mcp-full/` — a real MCP server. If run alongside `code-review-graph`, the collision risk is naming (two servers claiming the same key in `~/.claude.json`'s `mcpServers`, or two daemons binding the same port) — not live yet since only one is registered.
- OmniRoute binds `localhost:20128` and exposes its own 37-tool MCP server — a second MCP surface, no current conflict, worth tracking.
- `claude-video` is not an MCP server or hook — it's a `/watch` command (download, extract frames, transcribe). No collision surface.
- `reasoning-bank`'s real upstream is `google-research/reasoning-bank` — reference code for a paper, not a running service. Zero collision risk.
- Prime Agent isn't in Honey's supported-agent list (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Cline, OpenClaw, Kiro, Kilo, Hermes). Prime Agent is its own separate harness process, so Honey just won't follow there.
- GateGuard and Honey cooperate: GateGuard forces 4 facts before a destructive/write action; Honey's carve-out list exempts deletes/migrations from compression.
- Open item: whether mem0, OB1, reasoning-bank (if forked live), and code-review-graph would claim overlapping MCP server names if wired simultaneously — not yet checked.

## "Good catch," — Harness vs. rules-layer terminology

"Harness" is a trap term — it means two different things depending on system.

General industry usage: **harness = the runtime/engine** (Claude Code, Prime Agent). The rules/protocols/scripts that define direction (AESOP XI, `CLAUDE.md`, `SKILL.md`, GateGuard's fact-forcing rules) are closer to *config*, *protocol*, or *system prompt* layer, not usually called "the harness."

Prime Agent's own docs reuse the word for the opposite thing: their durable-memory/prompt-refinement component is named "Continual Harness" — by their definition, the *rules/state layer*. Their engine is "a persistent Python control environment" (the RLM/REPL); "harness" is reserved for the rules/memory sitting inside it.

Mapped onto the actual stack:
- **Engines** (general-sense "harness"): Claude Code, Prime Agent
- **Rules/protocol layer**: AESOP XI, `CLAUDE.md`/`SKILL.md`, GateGuard's rules, and Prime Agent's own "Continual Harness" subsystem (despite the name)

## "That's one of." — AESOP name definition

AESOP = **A**gentic **E**dge **S**plit **O**perations **P**rotocol — the name states both halves: agentic and split-operations-protocol.

## "Yes — that's." — Prime Agent's two core abstractions

> "Prime Agent is designed around two core abstractions:
> - The **RLM** (Recursive Language Model) — treats context as variables, tools/subagents as function calls, inside a persistent REPL
> - The **Continual Harness** — stores supplemental prompts, memories, skill descriptions, and reusable subagent specifications as durable state that Prime Agent can refine through small, evidence-backed updates"

Mapped onto the engine/rules split:
- **RLM** = the engine — the persistent Python control environment running the loop, calling the model, executing tool/subagent calls.
- **Continual Harness** = the rules/state layer — prompts, memories, skill descriptions, subagent specs. Never rewrites the immutable base system prompt (a hard floor self-refinement can't touch), with rollback snapshots if a refinement goes bad.

Design question flagged: Prime Agent already runs the same idea AESOP XI is going for (self-improving, evidence-based rule refinement). Does AESOP XI become the content inside Prime Agent's Continual Harness, or do the two run as separate, parallel rule layers?

## "And yeah I." — Confirming no contradiction

Confirmation that Honey-for-Devs and reverse-skill aren't the same two things, just checking they don't have contradicting aspects.

## "Glad it landed." — AESOP acronym wording discrepancy flagged

"Split Operations" is the routing/orchestration job, encoded directly in the acronym. Flagged discrepancy: the Aug 10 handoff has it as "Agentic Executions Split Operations Protocol" vs. "Agentic Edge Split Operations Protocol" spoken later — different word, needs operator confirmation on which is correct.

## "This is Horizons now." — The three-APK combined unit, clarified

The three APKs are one combined unit / user interface — Horizons UI plus two separate daemon APKs with their own bare-metal GUIs:

- **Daemon APK 1**: Shell access on the device — hosts the on-device agent and gives it device access through the shell environment, effectively replacing Termux with the same capabilities minus the Android app sandbox, by registering as an accessibility service / on-device assistant.
- **Daemon APK 2**: Speech and vision layer — same Video Game SDK permissions, OS permissions, and accessibility SDK/API.
- **Horizons UI**: the orchestrator app — supplies the WebSocket layer and the WebView Chromium browser in the UI, the LLM chat tile interface, the terminal GUI, and the model router/file picker/uploader with cloud front-end hooks and a fallback to an OpenRouter server. Also houses the nano-agent/smol-agent (model not yet chosen) orchestrating the dual agent query/execute tandem, access to the device NPU, and the runtime.

## "You're right," — reasoning-bank is a reference implementation, not a live component

`google-research/reasoning-bank` is the reference implementation of the recursive-memory idea: "a memory mechanism for agents that learns from both successful and failed trajectories, with reasoning stored as memory content," plus "memory-aware test-time scaling" (accumulated reasoning memory as a second scaling axis alongside inference-time compute). Adjacent to the Continual Harness paper's territory and RLVR-adjacent in spirit — but it's inference-time memory accumulation, not weight updates via verified reward, so not literally an RLVR training pipeline.

Practically: Python research code (`SWE-Bench/`, `WebArena/` directories, evaluation harnesses), needs API keys (OpenAI/Gemini/Claude-on-Vertex) and Docker for WebArena. Something to run to reproduce benchmark results or study the approach, not something to "install" as a live stack component the way OB1 or mem0 would be. Zero collision risk (no hooks, no MCP server) — but it's the methodology reference for how a recursive reasoning-memory layer should behave, a real input into how mem0/OB1/reasoning-bank-as-a-concept should work.

## "No — and I'd." — AESOP XI is the orchestrator/protocol, not a fourth harness

Pushback on collapsing AESOP into "the harness" — it loses something. "AESOP uses Prime Agent to do X using Y" and "AESOP uses X to do Y following Z's methodology" describes **routing** — AESOP deciding *which* engine handles a task and *how*. A harness is one specific, swappable execution environment (Prime Agent is a harness, Claude Code+ECC is a harness); what AESOP does sits *above* those, choosing between them — the standard term is **orchestrator**, or in infra language, **control plane**, as opposed to the **data plane** (Prime Agent's RLM, Claude Code's loop) that actually executes.

Also described as "underneath" — a different job from routing: the shared standard every harness gets judged against, closer to **protocol** — not a harness itself, the rules a harness has to satisfy regardless of which one is running.

Why resist folding it into "harness": a harness is exactly the thing that should be swappable. If AESOP *is* the harness, replacing Prime Agent means rebuilding AESOP along with it — welding the stable thing to the disposable thing. If AESOP stays the protocol/orchestrator sitting above and beneath the harnesses, Prime Agent can be swapped for whatever comes next and AESOP doesn't move.

**Conclusion**: Prime Agent = a harness (RLM engine + Continual Harness rules, bundled). Claude Code+ECC = a harness. AESOP XI = the orchestrator/protocol that decides which harness runs which job, and the constant standard both get held to — not a fourth harness, and not the union of the other two.
