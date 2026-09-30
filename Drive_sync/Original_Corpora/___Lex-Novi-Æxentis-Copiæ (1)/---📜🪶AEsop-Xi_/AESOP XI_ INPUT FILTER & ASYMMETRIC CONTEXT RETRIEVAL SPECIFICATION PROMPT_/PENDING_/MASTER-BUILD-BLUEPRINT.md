---
title: Master Build Blueprint — AESOP XI
status: DRAFT — awaiting the joint canon pass with the operator. Not yet fixed.
scope: the entire designed system, every layer, at full fidelity
classification: Heterogeneous Edge-Computing Mesh with Asymmetric Memory Paths
root anchor: Horizons-UI native device kernel execution engine (Node Alpha)
protocol: AESOP XI — Agentic Executions Split Operations Protocol
---

# Master Build Blueprint — AESOP XI

> **What this is.** The complete designed system, at full fidelity, across every
> layer. This is **the target**. Once defined, this is what it is.
>
> **Guiding principle — THE BLUEPRINT IS NEVER WATERED DOWN.** Nothing in this
> document is softened, hedged, or downgraded because it isn't built yet. A
> component being unwritten changes the *comparison*, never the target. If a
> future agent finds this document ambitious, that is the document working
> correctly.
>
> **Everything else in the corpus is a comparison against this.** No document
> describes the system in isolation — it describes the system *relative to this
> blueprint*. Every folder's `CLAUDE.md` opens with a State of the Union **in this
> same W5+H schema**, so target and status line up header for header: §1 here is
> the target, the folder's W5+H is the status, and the gap between them reads off
> the page. Same six headers is what makes them diffable.
>
> **Verification rule.** This document is verified against the **operator**, not
> against the code. Code disagreeing with the blueprint is a gap in the code.
> The one exception is the shipped home screen: it is done and it is not
> discussed further — see §3.1.
>
>
> **⚠ DRAFT.** Fixed only after the operator and I go through the sources together
> and decide what's canon. Sections carrying a verbatim operator quote or a
> supplied reference image are already solid; the rest is my compression of source
> material (§17) and is what that pass exists to check.

---

## 0 · Rules

> **Scaffolding — delete when the cleanup is done.** These exist to stop the
> failure modes that wrecked the last phase. They are not part of the system and
> shouldn't outlive the migration.

**1 · Ingest everything, completely, first.** Read the material in full before
acting — not skimmed, not sharded across subagents, not deferred until context
gets tight. Never claim to have read something you didn't. This is the root cause
of most downstream failure.

*2 · No unchecked writes.** Don't claim a file was written until it was.

* — enforced at the commit layer, not the read layer.
Everyone reads the vault; nobody writes outside their scope.

**3 · No cross-contamination** except through Omni Route.

**4 · Verify mechanically.** Run the check. A self-report is not evidence.

**5 · Keep AI-sourced material, don't trust it.** Mine it; promote only on
independent verification. In a transcript, an uncontested assistant claim is worth
**zero** — these get used as a scribe. Only the operator's words count. And when a
picture is attached with *"this is what it's going to look like,"* that's the spec.

**6 · Designed ≠ built.** Tag state. Never report intent as capability.

**7 · Metaphor ≠ implementation** — but two kinds, opposite handling. See §7.

---

## 1 · Core Architecture Matrix (W5 + H)

### WHO — entities

| Entity | Role |
|---|---|
| **Human-In-The-Loop (HITL)** | Root authority. Supplies intent, ethical bounds, final validation. **Sole conduit to the Red Agent.** |
| **Novus-Agenti** — the Brain | Composite multi-model execution core across MoE and MoA networks. Split executor / query. |
| **NovA-Claw** — the Body | Hardware-abstracted runtime: phone daemons, APK hooks, low-level scripts, cloud connectors. Maps reasoning plans to physical execution. |
| **Red Agent Auditor** — the Sentinel | Isolated, out-of-band validator. Checks all model output against the zero-trust **Nope Data Bank**. |

### WHAT — the tri-tailed memory engine

| Tier | Function | Carried by |
|---|---|---|
| **1 · Episodic** | micro-context, user state, conversational keys | **mem0** |
| **2 · Structural** | persistent human-readable knowledge | **Open Wiki CLI → Obsidian vault** |
| **3 · Analytical** | deep context networks, programmatic scan | **notebooklm-py**, **Graphify** |

**Transport core:** **OB1 (Open Brain Protocol)** over local Postgres — a protocol
spanning both cores, **not** a storage tier beneath one of them. All queries route
through **Omni Route**.

### WHERE — edge infrastructure

| Node | Hardware | Role |
|---|---|---|
| **Alpha** | Moto RAZR Ultra 2025 · Snapdragon 8 Elite · Hexagon NPU v79 · 16 GB | Heavy lifter for **agent tasking**. Perception + ambient ingress. Native Kotlin APK. |
| **Beta** | Nvidia Jetson Orin Nano Super 8 GB · 60–70 TOPS · 500+ GB NVMe | **The main computer.** Persistent core, OB1 vector backend, heavy reasoning out-of-band. |
| **Gamma** | Rubik Pi 3 Dragonwing · Qualcomm SoC · 14 TOPS | **Weakest of the three.** Drives dual monitors + keyboard + the OS — which is expected to consume most of it. Housekeeper role. See §1.1. |
| **Mesh** | Tailscale + wired home LAN | Ad-hoc P2P. No cloud round-trip for local work. |

#### 1.1 · Node Gamma — capacity is the constraint

The Dragonwing is not as powerful as Alpha or Beta. Running the dual monitors, the
keyboard, and the operating system will take up most of what it has. That is the
starting assumption, not a limitation to design around later.

Consequence: whatever agent runs there has to be small. The candidate is a
**nanoagent built in-house**, sized to what is actually left over. Depending on how
well it performs, it can be paired with a **cloud model** for anything beyond its
weight class.

The **Red Agent stays in its own separate sandbox** regardless of where the
housekeeper lands. Housekeeper ↔ Red Agent is an **open swap, not a merge.**

> **Interconnect:** there is substantial existing documentation on how these nodes
> click together. **Read it in full before writing the node topology file** — do
> not reconstruct the mesh design from this summary. Per Rule 0.

### WHEN — lifecycle

Discrete continuous step-loops. Each inference evaluates its own output before the
next. Daemons stay dormant until the operator flips a fuse. **Boots empty, boots
stable.**

### WHY

A manual, modular workbench — **not a black box.** Core law:
**"Daemons stay dumb, the user is the loader."**

### HOW

Seven rooms feed a centre-hub Router. The Terminal forges a
parameter packet; the Monitor verifies it live; the Router closes the circuit.

---

## 2 · System Dataflow

```
┌─────────────────────────────────────────────────────────────────┐
│  LOCAL P2P EDGE FABRIC  (ad-hoc, Tailscale + wired)             │
│                                                                 │
│   ┌──────────────────────┐         ┌──────────────────────┐     │
│   │  NODE ALPHA — phone  │◄───────►│  NODE BETA — Jetson  │     │
│   │  query · ambient     │         │  heavy inference     │     │
│   │  agent tasking       │         │  OB1 vector store    │     │
│   └──────────────────────┘         └──────────────────────┘     │
│              ▲                                ▲                 │
│              └──────────┬─────────────────────┘                 │
│                         ▼                                       │
│              ┌──────────────────────┐                           │
│              │ NODE GAMMA — Rubik Pi│  housekeeper, sandboxed   │
│              └──────────────────────┘                           │
└────────────────────────────┬────────────────────────────────────┘
                             │  executions & logs
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  AESOP XI MEMORY & PERCEPTION                                   │
│                                                                 │
│   ┌──────────────────────┐         ┌──────────────────────┐     │
│   │ Episodic · mem0      │         │ Analytical           │     │
│   │ Structural · OB1     │         │ Graphify ·           │     │
│   │      ── via ──       │         │ notebooklm-py        │     │
│   │    OMNI ROUTE        │         │                      │     │
│   └──────────────────────┘         └──────────────────────┘     │
└────────────────────────────┬────────────────────────────────────┘
                             │  raw interaction traces
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  ISOLATED ADVERSARIAL AUDIT                    ◄── HITL only    │
│                                                                 │
│   ┌───────────────────────────────────────────────────────┐     │
│   │  Red Agent Auditor  +  Nope Data Bank guardrail       │     │
│   │  MoA: independently-sourced models, not multi-sample  │     │
│   └───────────────────────────────────────────────────────┘     │
└────────────────────────────┬────────────────────────────────────┘
                             │  sanitized traces
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  RECURSIVE TRAINING FLYWHEEL                                    │
│                                                                 │
│   GCP buckets (.jsonl / condensed .md)                          │
│                    │                                            │
│                    ▼                                            │
│   Recursive KAG  ──►  model self-training  ──►  back to Alpha   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3 · Horizons-UI — the lifecycle root

**Nothing lives without it.** Every other layer is reached through this app.

### 3.1 · The home screen

**Done. Do not touch.**

That is the entire entry. No layout description, no positions, no diagram, no
restyling proposal, no "correction" to it. It is finished and it is correct.

### 3.2 · Rooms — functional ownership

Named components and what each one owns. This is an ownership map, not a layout.

| Room | Owns |
|---|---|
| **MONITOR** `/cognito` `$_browser` | scope gate, live verification, green light, browser |
| **CHAT** `/interface` `$_model` | multi-modal chat, artifacts, embedded web view, agentic OS tools |
| **SETTINGS** `/config` `$_utils` | vault, SAF picker, "Open With" intent catchers, keys |
| **TERMINAL** `/shell` `$_bash` | Termux staging, forges packets, launch + recovery daemons |
| **ARCHIVES** `/logs` `$_files` | verified profiles, parameter history, **recovery restore source** |
| **HORIZONS** `/about` `$_.home` | build version, model credits, attributions, hidden game payload |
| **ROUTER** `// CORE_HUB` `$_Statio` | fuse box + breaker, dual-NPU orchestrator, voice engine, DSP |

**Floating Horizons Tile** — always-on overlay, independent of which room is
active: screen-vision capture, mic trigger, live meta-prompting.

### 3.3 · Router GUI — the Aiwa CD player, literally

The Router is a **graphical user interface with animations, built to look like the
Aiwa CD player.** This is a literal visual specification, not a metaphor — it is
why the reference was uploaded and explained in detail.

Component stereo stack: load the media, tune it, switch it on. Physical button
feel. Tactile controls. Swapping parameter packets reads like swapping CDs.
Plasma-tube connector cords in each tile's colour, beads running along them.
Violet faceted crystal, white sun glow beneath, `ROUTER` in white.

**Build it as described. Do not abstract it into "styling direction."**

### 3.4 · Monitor GUI — the arcade cabinet, literally

Neon upright cabinet: lit marquee carrying the title, CRT screen behind glass
reading as a green-graticule oscilloscope, instruction placard under glass,
control deck with joysticks and coloured buttons, coin door. Slightly more
futuristic than the raw retro reference. Walk up, look at the screen, read the
placard, hit a button. Also renders the Horizons easter-egg game.

### 3.5 · Panel treatments

| Panel | Background | Wallpaper? |
|---|---|---|
| Home | astral — deep black, haloed stars, telemetry map | no |
| Terminal | Matrix rain (`fakesteak`) | no |
| Router | circuit board / chip nodes | no |
| Monitor | sliding animated oscilloscope | no |
| Chat | wet blue-grey slate | yes |
| Horizons | butterfly nebula, gold + blue-white | yes |
| Archives | vintage film strip | yes |
| Settings | brushed-steel vault door | yes |

### 3.6 · Guardians

- **GOAT** — crash-log easter egg. `// GOAT_SAYS_NO`, synthesized bleat; 7 banner
  taps → `// GOAT_UNLOCKED`.
- **CHONK** — screen-timeout guardian. 3–5 min inactivity pauses active processing
  into low-power sleep; the chonky orange cat covers the screen. Tap or floating
  mic wakes it.

---

## 4 · The circuit — authority in series

```
       SETTINGS ──supplies──►  the packet  ──►     TERMINAL ──forges──►
                                                        │
                                                        ▼
       ARCHIVES ◄──stores verified profiles──        MONITOR
        │                                        THE SWITCH IN THE LOOP
        │ recovery daemon restores               verifies LIVE at flip time
        │                                        stores nothing · DISPATCHES
        ▼                                                │
                                                         ▼
                                              CENTRE ROUTER
                                              fuse box + breaker
                                              carries current
                                              DOESN'T ARGUE
```

- **Settings** supplies assets and keys. May hand a packet to the Router. **No
  authority to run it.**
- **Terminal** writes the packet — parameters only. **Never executes.**
- **Monitor** is the switch. Verification is **live at flip time** — a series
  switch has no memory. Open or loose ⇒ no circuit, however perfect the packet.
- **Router** carries current. Attempts to close the circuit. If the assets satisfy
  the amperage, the engine fires. If not, it **fails naturally** — no artificial
  brick wall, no lockout.
- **Archives** holds verified profiles; the recovery daemon restores from here.

---

## 5 · The parameter packet — the fuse

A **plain editable text file.** Copyable, movable, replaceable, pullable straight
out of the Archives. Four layers:

| # | Layer | Carries |
|---|---|---|
| 1 | **Weights** | model paths, INT8/ONNX quantization limits, tensor allocations |
| 2 | **Runtime** | zero-TTL flags, RAM allocation, thread bindings, **temperature, verbosity, cores** |
| 3 | **Engine** | native JNI/C++ layers, VAD sensitivity |
| 4 | **Communication** | IPC sockets, WebSocket bridges, API router endpoints |

`RuntimeDef` is shaped to these four. Parameters are not discovered ad hoc and
bolted on — they belong to a layer.

### Daemons

- **Launch daemons** — from the Terminal. Initialise C++ environments, IPC
  sockets, load zero-TTL models.
- **Recovery daemon** — traps OOM/crash on an NPU tensor op or JNI thread,
  flushes the corrupted buffer, restores from the latest verified Archives
  snapshot.

### Model residency — external device folder, no TTL

**DECIDED (operator).** Time-to-live is gone. Models do not live in the app and
the app does not manage their lifetime.

- Weights sit in their **own clean embedded device folder**, loaded by absolute
  path at runtime. Nothing large ships inside the APK.
- Swapping a model is **drag-and-drop** into that folder. No recompile, no
  rebuild, no reinstall.
- The APK stays thin — it bundles the native execution libraries only
  (`libsherpa-onnx-jni.so`, `libonnxruntime.so`, ~20 MB) and reads everything else
  off the filesystem. It behaves like a media player reading a file off local
  storage: the player stays fixed, the media lives wherever you put it.

**What the app is then actually responsible for:**

1. **Screen timeout** (and the sleep/wake handler)
2. **Permissions**
3. **The browser** — WebView, OAuth popups, download-to-vault
4. **WebSockets** — the loopback bridges

That list is the whole job. Everything else is a path into the device folder.

The **dual-NPU orchestrator** still ping-pongs context between the two on-device
models without teardown. The constraint stands: the NPU budget carries the **two
text/tensor models**, and the voice layer is not stacked on top of it.

## 6 · Memory stack

```
                        ┌──────────────────────────┐
      agents ──────────►│       OMNI ROUTE         │
                        │   aggregation gateway    │
                        │   MCP · A2A v0.3         │
                        │   SQLite FTS5 + int8     │
                        │   vectors · typed decay  │
                        └────────┬────────┬────────┘
                                 │        │
                 ┌───────────────┘        └───────────────┐
                 ▼                                        ▼
        ┌─────────────────┐                     ┌─────────────────┐
        │      OB1        │                     │      mem0       │
        │  STRUCTURAL     │                     │   EPISODIC      │
        │  the protocol   │                     │  what's being   │
        │  how memory is  │                     │  accessed now   │
        │  doled out      │                     │  user · session │
        │  Postgres/vec   │                     │  agent state    │
        └─────────────────┘                     └─────────────────┘
                 │                                        │
                 └──────────────────┬─────────────────────┘
                                    ▼
                        ┌──────────────────────────┐
                        │     REASONING BANK       │
                        │  a PATTERN, not a backend│
                        │  Title/Description/      │
                        │  Content schema          │
                        │  LEARNS FROM FAILED      │
                        │  TRAJECTORIES — which    │
                        │  neither OB1 nor mem0 do │
                        └──────────────────────────┘
```

**OmniRoute is the shared platform OB1 and mem0 both operate from.** Agents talk
to one gateway; it dispatches structural reads to OB1 and episodic to mem0. There
is no pick-one. Per-request control via `x-omniroute-no-memory`.

Separately, OmniRoute carries **connection-level resilience** — circuit breakers,
key cooldowns, model lockout. Distinct mechanism from memory typed-decay; do not
conflate the two.

**Tier map on disk** (`file-management-system/` only — "tier" here means
information type, never stack role):

```
tier-1-episodic/     mem0 storage
tier-2-structural/   open-wiki-cli-vault/ · obsidian-vault-network/
tier-3-analytical/   graphify-pipelines/ · notebooklm-py-contexts/
```

---

## 7 · Rule 7 in full — two kinds of metaphor

The operator's analogies split into two categories with **opposite** handling.
Confusing them is what broke the last build.

### 7a · Behavioural metaphors — DO NOT COMPILE

**Fuse box · 10-amp fuse · breaker · amperage · closing the circuit.**

These describe *how the circuit behaves*. They are **config-file and interaction
design language**. They must never become enforcement code.

What went wrong: "10-amp fuse" was compiled into a rigid hardcoded four-item
`AssetCheck` list. "Router" became an automated gatekeeper throwing red
`⚡ FUSE BOX` banners and blocking any configuration that didn't match its
pre-programmed definitions — destroying the ability to run custom binaries,
fine-tuned weights, or build-in-place assets.

> The Router does not say *no*. It attempts to close the circuit.

### 7b · Visual references — BUILD THEM LITERALLY

**Aiwa CD player · upright arcade cabinet · component stereo stack.**

These are **literal build targets for the GUI**, with animations. They were
uploaded and explained in detail *because they are the spec*. Rule 7a does not
apply to them. Softening these into "styling direction" is itself the failure.

**The test:** does the analogy describe *behaviour* or *appearance*? Behaviour →
7a, never compile. Appearance → 7b, build it exactly.

---

## 8 · Voice layer

```
  mic / floating tile
         │
         ▼
   ┌───────────┐   speech?   ┌───────────┐   text    ┌───────────┐
   │ SILERO VAD│────────────►│    STT    │──────────►│    LLM    │
   │ endpoint  │  500–800ms  │           │           │ NPU or    │
   │ detection │   silence   │           │           │ cloud     │
   └───────────┘             └───────────┘           └─────┬─────┘
         ▲                                                 │
         │ barge-in: cancel TTS, clear buffer,             ▼
         │ reopen VAD                              ┌───────────┐
         └─────────────────────────────────────────│ KOKORO TTS│
                                    PCM → AudioTrack└───────────┘
```

- **VAD** — Silero, continuous endpointing on trailing silence. Not hardcoded
  timers. Hard max (~60 s) so background noise can't hang the stream.
- **Barge-In** — tap or speech during playback cancels the TTS queue and clears
  the buffer before feeding fresh input. Prevents the STT hearing the speaker.
- **In-process** — the voice layer runs in-process on the sherpa-onnx AAR **by
  design**. This is scoped to voice only and is not a violation of the
  daemon-only rule, which covers the LLM path.

### 8.1 · STT engine — OPEN, and the NPU question underneath it

**Whisper base vs. Moonshine is undecided.** Which performs better on **CPU/GPU**
is the actual question, and it has not been measured. Recorded, not reconciled.

Underneath it sits a bigger question that keeps getting skipped: **why push STT
onto the NPU at all?** The NPU budget already carries **two models taking turns**.
Adding speech to that contention is a decision that needs justifying, not
assuming. Previous sessions pushed hard for NPU placement without addressing it.

A `parakeet-tdt-0.6b-v3-npu-mobile` bucket exists on HF as an NPU-targeted path —
noted as available, **not** as a recommendation.

**Resolution path:** measure both on CPU/GPU on the device. Not a design debate.

---

### 8.2 · Interim path — prove the voice stack off-app first

**Operator direction.** Rather than build the voice layer inside Horizons-UI to
find out whether it works, stand it up first in an existing Sherpa-ONNX app that
already accepts uploaded models — and possibly an uploaded runtime — and that
exposes a scripting hook (the same hook used for dual-model podcast generation).

Why this is the right order:

- It tests the **models and the pipeline**, not the app's plumbing. If it fails
  there, the problem is the models; if it works there, anything failing in
  Horizons is Horizons.
- It answers §8.1 empirically — Whisper base vs. Moonshine on CPU/GPU, measured on
  the actual device, without an APK build cycle per attempt.
- The scripting hook makes the dual-model turn-taking testable before the NPU
  manager exists.
- It matches the residency model above: the models already live in a device
  folder, so **porting over is a path change, not a rewrite.**

**To confirm on device:** whether that app accepts a custom runtime as well as
custom models, and how much its scripting layer actually exposes.

---

## 9 · Runtime paths

| Path | Route |
|---|---|
| **On-device LLM** | uploadable daemon binary — **not in-process**. Qwen3.5-9B: ONNX → QNN context binary → Hexagon HTP. **No CPU fallback on that model.** |
| **Cloud** | `http_fetch` agent tool — SambaNova, OpenRouter, HuggingFace, custom endpoints |
| **Termux** | loopback. App-spawned daemon binds `:8080` under the app's UID; Termux shares loopback, so NPU access needs no inversion |
| **Inbound** | **listener required** — what Termux cannot get on its own is mic, voice, and WebView OAuth |

---

### 9.1 · NPU manager — harness inside the APK

**DECIDED (operator): harness inside the APK.** Not a separate out-of-process
layer.

Two on-device models take turns on the NPU, so something has to hold the context
switch, catch OOM, and drive recovery. In-process gives it direct access to the
orchestrator and the runtime without an IPC hop, which is the point — the
alternative bought isolation the app doesn't need and cost a lifecycle to manage.

It dies with the app. That is acceptable: the app boots empty by design, and
recovery restores from a verified profile rather than from a resident process.

**Still open:** the **dual-agent memory tier** on the phone — the split that is
the reason mem0's dual-agent architecture lives on Node Alpha. It is coupled to
the manager but is not resolved by this decision.

## 10 · Red Agent Auditor

Mixture of **independently-sourced** models — not multi-sample on one model. A
single auditor cannot catch its own blind spot; it fails identically every time
it checks itself.

- **Air-gapped, out-of-band.** Intercepts raw logs, tools, and prompts before
  anything touches persistent storage.
- **Nope Data Bank** — the guardrail corpus it cross-references against.
- **HITL is the sole conduit.** No agent reaches the Red Agent directly.
- **Housekeeper ↔ Red Agent is an open swap, not a merge.** Do not conflate.

**Open:** scope (high-stakes only vs. all traffic) and disagreement resolution
(fail-closed auto-reject vs. escalate to HITL).

---

## 11 · Recursive training flywheel

Red-Agent-cleansed traces → condensed `.jsonl` → GCP buckets → **Recursive KAG**
loop → model self-training → back to Node Alpha. The system converts its own
everyday interactions into structured training data while staying air-gapped at
the edge.

---

## 12 · Repository layout

Four repos: **NovA-Claw + Novus-Agenti** · **Horizons-UI** · **skills/tools** ·
**NovA-Corpus**.

Every folder and every major subsection carries the **section kit**:
`README.md` · `CLAUDE.md` · `llm_wiki.md` · `skill_manifest.json`.

**Every `CLAUDE.md` opens with the State of the Union** — the blueprint slice for
that scope, then observed reality, then the delta. An agent reads it first and
immediately knows what it is supposed to have versus what it does have.

**Document convention** — siblings in one folder, shared basename:

```
fragmented-qat/
├── fraqat-paper.pdf      original, untouched
├── fraqat-paper.md       cleaned markdown
├── fraqat-paper.jsonl    only when large/structured enough
└── skills.md             routes the folder
```

**Same basename = same document** is the join key the mechanical audit runs on.

**One axis on disk.** The tree is organised by **domain**. Format tier and corpus
type are frontmatter tags, never folders.

---

## 12.1 · Build map — order of construction

What gets built, in what order, and what each thing unblocks. Read down; nothing
below a row starts before the rows above it are real.

```
  PHASE 0 · PROVE THE PARTS                        blocks everything
  ├── voice stack in a Sherpa host app  ─────────┐  §8.2
  │     └─ answers Whisper vs Moonshine          │
  ├── read crash.log on device                   │  §3.6
  │     └─ answers the first-crash trigger       │
  └── verify live repo state vs. the docs        │  Rule 0 + Rule 4
                                                 ▼
  PHASE 1 · THE APK'S FOUR JOBS                    the app's whole remit
  ├── screen timeout / sleep + wake              │  §3.6
  ├── permissions                                │
  ├── browser — WebView, OAuth, download-to-vault│  §3.2
  └── WebSockets — loopback bridges              │  §9
                                                 ▼
  PHASE 2 · THE CIRCUIT                            makes the workbench work
  ├── parameter packet as a plain file           │  §5
  ├── RuntimeDef shaped to the four layers       │  §5
  ├── switchOn() consults the Monitor            │  §4
  │     └─ closes the no-RuntimeDef bypass       │
  └── Archives stores + restores verified profiles  §5
                                                 ▼
  PHASE 3 · ON-DEVICE EXECUTION                    the point of the thing
  ├── models load from the device folder         │  §5
  ├── NPU manager harness (in-APK)               │  §9.1
  │     └─ dual-model context switch, OOM catch  │
  ├── recovery daemon ── restores from Archives  │  §5
  └── voice layer ported in from Phase 0         │  §8
                                                 ▼
  PHASE 4 · THE MESH                               off-device
  ├── inbound listener  ── Termux gets mic/OAuth │  §9
  ├── OmniRoute gateway ── OB1 + mem0 behind it  │  §6
  ├── node interconnect ── READ THE DOCS FIRST   │  §1.1
  └── nanoagent on Node Gamma                    │  §1.1
                                                 ▼
  PHASE 5 · THE GUI BUILD                          design already locked
  ├── Router  ── Aiwa CD player, animated        │  §3.3
  ├── Monitor ── arcade cabinet                  │  §3.4
  └── Terminal ── matrix cascade                 │  §3.5
                                                 ▼
  PHASE 6 · EVOLUTION                              operator-undefined
  ├── Red Agent auditor                          │  §10
  └── recursive training flywheel                │  §11
```

**The home screen appears nowhere in this map. It is done.**

---

## 12.2 · Action chart — how one request moves through the system

Trace of a single voice request, end to end. Every arrow is a handoff; every box
is owned by exactly one component.

```
  USER speaks
     │
     ▼
  ┌────────────┐   silence 500–800ms
  │ SILERO VAD │──────────────────────┐
  └────────────┘                      ▼
                              ┌──────────────┐
                              │     STT      │  device folder → by path
                              └──────┬───────┘
                                     │ text
                                     ▼
                              ┌──────────────┐
                              │  ROUTER hub  │  which runtime?
                              └──┬────────┬──┘
                                 │        │
                    on-device ◄──┘        └──► cloud
                         │                       │
                         ▼                       ▼
                 ┌──────────────┐        ┌──────────────┐
                 │ NPU MANAGER  │        │  http_fetch  │
                 │ in-APK       │        │  agent tool  │
                 │ ping-pong    │        └──────┬───────┘
                 │ 2 models     │               │
                 └──┬────────┬──┘               │
                    │        │ OOM              │
                    │        ▼                  │
                    │  ┌──────────────┐         │
                    │  │  RECOVERY    │         │
                    │  │  DAEMON      │         │
                    │  └──────┬───────┘         │
                    │         │ restore         │
                    │         ▼                 │
                    │  ┌──────────────┐         │
                    │  │   ARCHIVES   │         │
                    │  └──────────────┘         │
                    │                           │
                    └──────────┬────────────────┘
                               │ tokens
                               ▼
                        ┌──────────────┐
                        │ AGENT LOOP   │  tool call?
                        └──┬────────┬──┘
                           │        │
                      no ◄─┘        └─► yes ─► TOOL ─► result ─┐
                           │                                   │
                           │◄──────────────────────────────────┘
                           ▼
                    ┌──────────────┐
                    │  KOKORO TTS  │──► AudioTrack ──► USER hears
                    └──────────────┘
                           ▲
                           │ barge-in: cancel queue, clear buffer,
                           └──────────── reopen VAD
```

**Memory runs alongside, not inline:** every turn writes episodic state to mem0
and reads structural context from OB1 — both through **Omni Route**, never
directly (Rule 3).

---

## 12.3 · Flip chart — what happens when the operator throws the switch

```
  TERMINAL forges packet ──► file on disk
                                  │
  SETTINGS supplies assets/keys ──┤
                                  ▼
                          ROUTER ── operator flips
                                  │
                                  ▼
                          ┌───────────────┐
                          │    MONITOR    │  LIVE check, at flip time
                          │  greenLight() │  (a series switch has
                          └───┬───────┬───┘   no memory)
                              │       │
                        pass ─┘       └─ fail
                              │            │
                              ▼            ▼
                    circuit closes    circuit does not close
                    daemon runs       ── NO brick wall
                              │       ── NO red banner
                              ▼       ── NO lockout
                    ARCHIVES stores   the operator sees why
                    verified profile  and changes the packet
```

**The Router never refuses.** It attempts. Failure is a circuit that didn't
energise, not an application saying no.

---

## 13 · Configurations

| Setting | Value |
|---|---|
| Device | Motorola Razr Ultra 2025 · SM8750 · 16 GB · Hexagon HTP v79 |
| Weight bounds | 8.0 – 11.5 GB dynamic |
| Build | AGP 8.8.0 · Kotlin 2.1.0 · compileSdk 35 · minSdk 31 · JDK 17 · arm64-v8a |
| Signing | `release/debug.keystore`, committed by design |
| Loopback | daemon `:8080` · media daemon STT/TTS · GenieX `:18181` |
| Distribution | sideload / direct install — the 200 MB Play limit does not apply |
| Brand | bg `#222C34` · surface `#35414A` · teal `#2DD4D9` · highlight `#4FE7EC` · backplate `#050709` · action `#F5C518` |
| Backdrop | pure Compose `Brush.radialGradient` — **not** XML shape |
| Env | `HF_TOKEN`, `QAI_HUB_API_TOKEN` from environment. **Never hardcoded.** |

**Mobile working rules:** phone only, no laptop. No tokens or long URLs in
paste-able commands. Short alias then `$VAR`. Keep commands under ~50 chars.

---

## 14 · Credits & attribution

| Component | Source |
|---|---|
| **OB1 — Open Brain Protocol** | Nate B. Jones |
| **mem0** | mem0ai |
| **reasoning-bank** | Google Research (ICLR) — pattern reused, not the code |
| **sherpa-onnx** | k2-fsa |
| **Kokoro TTS** | 82M parameter ONNX voice model |
| **Silero VAD** | Silero Team |
| **Moonshine / Whisper** | Useful Sensors / OpenAI |
| **Parakeet-TDT 0.6B** | NVIDIA |
| **QAIRT · QNN · Hexagon HTP** | Qualcomm |
| **ONNX Runtime** | Microsoft |
| **llama.cpp** | Georgi Gerganov + contributors |
| **fakesteak** — Matrix rain | CC0 |
| **Via** — WebView browser | Via fork |
| **crewAI** | crewAI Inc. |
| **Tailscale** | Tailscale Inc. |

Full open-source attribution renders in the **Horizons** room.

---

## 15 · Superseded

Record of how the build arrived here — **not a ban list.** If one of these is the
right tool again, that is an open question, not a violation. Scoped to the
Qwen3.5-9B path; other model families ship their own runtimes.

| Old | Replaced by |
|---|---|
| Track 1 / Track 2 | single path: ONNX → QNN context binary → Hexagon HTP |
| LiteRT / LiteRT-LM | ort_engine daemon |
| genie_engine | ort_engine (ORT + QNN EP) |
| Separate Watchdog | CliffordService (CLIFFORD == Watchdog) |
| Nexa SDK, OmniNeural | dead |
| Cloud failover in app LLM | `http_fetch` agent tool |

| Router as hardened gatekeeper | Monitor holds the gate; Router carries current |

---

## 16 · Open — named, never quietly filled in

**Nearest priority: a working voice agent on the phone**, proved off-app first
(§8.2). The node build-out follows it, not the other way round.

**Decided this session — no longer open:** NPU manager is a **harness inside the
APK** (§9.1). Model residency is an **external device folder with no TTL** (§5).

1. **STT: Whisper base vs. Moonshine** — measure on CPU/GPU on device (§8.1). And
   the prior question of whether STT belongs on a contended NPU at all.
2. **Dual-agent memory tier** on the phone — coupled to the NPU manager but not
   resolved by that decision (§9.1).
3. **Node Gamma agent** — in-house nanoagent sized to what the OS leaves; cloud
   pairing depending on how it performs (§1.1).
4. **Sherpa host app capability** — does it accept a custom *runtime* as well as
   custom models, and how far does its scripting layer reach (§8.2)?
5. OmniRoute built-in memory: local cache / offline fallback, or disabled per request?
6. Red Agent MoA scope, and disagreement resolution.
7. `discovery/` folder name.
8. NovA-Claw + Novus-Agenti: one repo or two.
9. `global-documentation-vault/` weight — Git LFS or its own repo.
10. `nodes/` internal layout — **existing interconnect documentation must be read in
   full first** (§1.1). Do not reconstruct it from summaries.
11. Packet serialisation format (JSON / YAML / key=value). Any satisfies canon.

**Recursive-training and Red-Agent internal flows are operator-undefined.** The
sections above state their role in the mesh. Their internals are **not** to be
populated with invented architecture.

---

## 17 · Sources this draft was assembled from

> Precedence when they disagree: **[`SOURCE-PRECEDENCE.md`](SOURCE-PRECEDENCE.md)**.
> The spec-by-spec PDFs (§2 there) are the most accurate material and the base for
> chiselling any new spec.

Listed so the joint canon pass has something concrete to check, accept, or reject
section by section. **Rule 0 applies to that pass**: the sources get read in full,
not sampled.

| Source | Used for | Grade |
|---|---|---|
| `horizons-ui/HOME-REDESIGN-SPEC.md` | the canon format itself; room labels; guardians | **canon** — operator verbatim + images |
| `horizons-ui/ROUTER-STEREO-STACK-SPEC.md` | §3.3 Router GUI | **canon** — locked spec, reference image supplied |
| `horizons-ui/MONITOR-ARCADE-CABINET-SPEC.md` | §3.4 Monitor GUI | **canon** — locked spec, reference image supplied |
| `horizons-ui/TERMINAL-SPEC.md` | §3.5 panel treatments | **canon** — locked spec |
| Gemini thread 2026-08-04/05 — **operator turns only** | §5 four layers, daemons, zero-TTL, §8.1 | **canon** — operator's own words |
| Gemini thread — assistant prose | *nothing.* Explicitly excluded | **rejected** |
| neuromesh / AESOP XI master plan (Aug-2) | §0–§2 structure, §6 memory stack, §10–§11, §14 credits | **unverified** — operator calls the prose sloppy; **the visuals were good**. Compressed and redrawn here; **needs the joint pass** |
| `Horizons-UI/CLAUDE.md` | §9 runtime paths, §13 configurations, §15 superseded | **mixed** — carries a superseded room layout; other content not independently checked |
| `omniroute` documentation | §6 OmniRoute capabilities | **verified** — read directly |
| Operator, this session | Rule 0, §1.1 Node Gamma, §8.1, §9.1, §3.1, §7 split | **canon** — operator's own words |

### Known to be missing from this draft

- **Node interconnect.** Substantial documentation exists on how the nodes click
  together. **It has not been read.** §1.1 and §16 item 9 flag this; the node
  topology file must not be written until it is.
- **The "do have" column.** This draft is pure target. The comparison side needs
  an audit against the **live `Horizons-UI` repo** — the vault's Kotlin snapshot
  is provably stale (no in-process STT, wired to a dead `:8091`) and cannot serve
  as the reference.
- **Everything in `pending-corpora/`**, which has not been triaged against canon.

---

## 18 · Where the compiled documentation lands

**Output goes to a device folder**, same as the models (§5). Not to Drive.

The repo is the transport: work is committed here, then pulled down into a clean
device folder on the phone. Nothing has to be written back to Drive, so the
billing state is irrelevant to the pipeline.

**Drive is a source, not a destination.** Reads work fine (verified this session).
The operator is restructuring and mostly *deleting* there in parallel.

**Consequence — snapshot anything cited.** Because Drive is being pruned while
this work is in progress, any Drive document used as a source gets **copied into
this repo at the point it is used**. A citation to a Drive path that later gets
deleted is a broken citation, and Rule 4 can't verify what isn't there.
