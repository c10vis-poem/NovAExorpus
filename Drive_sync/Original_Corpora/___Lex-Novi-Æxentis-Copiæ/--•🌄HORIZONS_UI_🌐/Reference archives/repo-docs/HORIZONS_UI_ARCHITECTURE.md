# Horizons UI — The Switchboard

## Orchestration Layer for N0.V4 Distributed Agent System

**Version:** 2.0 \| **Last updated:** April 22, 2026 **Purpose:**
Persistent stateful shell that orchestrates N0.V4, Docker CLIs, artifact
API, and frontier models **Deployment:** React SPA — PWA-first,
installable on Razr Ultra 25 and desktop

## 1. Why Horizons Exists

**The problem:** Claude artifacts are sandboxed. Artifact A can't talk
to Artifact B. Each artifact is a closed box by design (which is a
security feature, not a bug).

**The solution:** A persistent orchestration shell that:

- Holds working state between artifact invocations

- Routes user intent to the right worker (artifact, frontier model, Pi
  > tool)

- Maintains the three toggles (artifact API ON/OFF, frontier endpoint,
  > edge-only mode)

- Surfaces Docker CLI \#2 reports to the general manager for gate review

- Provides the UI for wiki browsing, log review, and sharpening cadence
  > management

## 2. The Four Control Tiers

### Tier 1: Toggles (Top Bar)

- **Artifact API:** ON / OFF (controls Claude API embedded in active
  > artifact)

- **Frontier Endpoint:** Sonnet / Opus / Gemini Pro / Perplexity / Haiku
  > / Bit Model / Edge Only

- **Tool Execution:** P2P (home) / Tailscale (remote) / Queue (offline)

- **Mode:** Full Stack / Token-Conservation / Mission-Critical (pure
  > edge)

### Tier 2: Apprentice Status (Left Panel)

Live N0.V4 telemetry:

- Current session log count

- Edge execution vs. frontier escalation ratio (rolling 24hr)

- Performance-dip indicators

- Next sharpening cycle countdown

- Omni Neural 4B temperature + NPU utilization

### Tier 3: Active Workspace (Center)

- Artifact render area (N0.V4 artifact lives here when active)

- Intent input box (voice via Whisper Tiny → PTL → routed)

- Streaming response from whichever endpoint is handling the current
  > request

- Artifact switcher (jump between N0.V4, other tool artifacts, wiki
  > pages)

### Tier 4: Audit Queue (Right Panel)

- Docker CLI \#2 pending reviews (patterns awaiting general manager
  > gate)

- Confidence-scored contradictions requiring human resolution

- Recent wiki updates (what Docker CLI \#2 has compiled)

- Failure log entries flagged for attention

## 3. Routing Logic

User intent flows:

Voice/Text input

→ Horizons captures + timestamps

→ PTL (Haiku/Flash) cleans prompt

→ Horizons checks toggle state:

├── Edge Only mode? → Omni Neural 4B, Pi tools only

├── Artifact API ON? → Embedded Claude → returns to Horizons

├── Frontier set to Gemini? → PWA tab call → returns to Horizons

└── Mission-critical? → Pure edge, queue cloud actions

→ Response returned to user

→ Every step logged to /nova/logs/

→ Docker CLI \#1 picks up async for pattern analysis

**Horizons never executes — it orchestrates.** Tool execution happens on
Pi (P2P or Tailscale). Reasoning happens at whichever endpoint is
active. Horizons is the switchboard, the audit dashboard, and the
control panel.

## 4. Integration Points

### With N0.V4 (Edge)

- Horizons subscribes to N0.V4's decision events via WebSocket

- Shows live "what the apprentice is doing" indicator

- Surfaces routing decisions for user review (optional verbose mode)

### With Pi (Hub)

- Pulls Docker CLI \#1 + \#2 output via Tailscale API

- Displays wiki compilation status

- Triggers manual sharpening cycles on general manager command

### With Artifact API

- Hosts the artifact iframe when Claude API native is active

- Manages API key + rate limit visibility

- Shows token burn rate (cost transparency — Skill 7)

### With Frontier PWAs

- Maintains persistent sessions with each frontier endpoint

- Routes queries based on Tier 1 toggle

- Handles fallback cascade if primary endpoint fails

### With Wiki (/nova/wiki/)

- Browse compiled knowledge via Obsidian-style graph view

- Search via pgvector + BM25 hybrid (qmd pattern)

- Edit schema files (routing_rules.json, failure_rules.json,
  > sharpening_gates.json) with live validation

## 5. Architectural Notes

- **Stack:** React + Tailwind (no external UI library dependency)

- **State management:** Zustand (lightweight, persists to localStorage
  > via Horizons session cache only — NOT inside artifacts)

- **Network:** WebSocket to N0.V4 edge events, REST to Pi API, fetch to
  > frontier PWAs

- **Auth:** Tailscale tunnel auth for Pi endpoints, API keys managed in
  > Horizons settings (never in artifacts)

- **Offline:** Full offline mode — if everything is down, Horizons still
  > renders logs and recent wiki entries from IndexedDB cache

## 6. Single Point of Failure Analysis

**Horizons itself is a SPOF for orchestration.** Mitigation:

- **Horizons is open-source in design** — can be self-hosted on Pi (via
  > Docker container) if Anthropic-hosted version is unavailable

- **Graceful degradation:** If Horizons is down, N0.V4 on Razr still
  > handles voice input → edge execution. User loses the switchboard UI
  > but not the core agent.

- **Fallback:** Direct Claude PWA or direct artifact URLs work without
  > Horizons, just without the state layer

## 7. Build Status

- **v1.0:** Initial JSX component delivered April 15, 2026 (file system
  > issue during delivery, resolved)

- **v2.0 (this doc):** Expanded architecture with N0.V4 distributed
  > agent integration

- **Implementation:** Pending — to be rebuilt as live React artifact in
  > PWA session with full tool access

- **Priority:** Build after N0.V4 edge stack is stable (2+ weeks logged,
  > Phase 2 complete)

## 8. What Horizons Is NOT

- **Not a chat app.** Chat happens inside artifacts or in frontier PWAs.

- **Not a model.** It holds zero inference capability. Pure
  > orchestration.

- **Not a file manager.** File ops happen on Pi via Claude Code CLI.

- **Not a replacement for claude.ai.** It's a layer *above* that
  > coordinates with it.

- **Not permanent.** Once N0.V4 is mature enough to handle orchestration
  > itself, Horizons becomes optional.

*Horizons is the switchboard. You are the general manager. N0.V4 is the
apprentice. Pi is the hub. Cloud models are the specialists on call.
Horizons is how they all stay coordinated without stepping on each
other.*
