# Horizons-UI — Agent Brief

> **Derived document.** The gospel is
> [`../canon/MASTER-BUILD-BLUEPRINT.md`](../canon/MASTER-BUILD-BLUEPRINT.md) —
> the W5+H universal blueprint, the build map (§12.1), the action chart (§12.2),
> and the flip chart (§12.3). **Read the blueprint first.** This brief only adds
> what an agent working the *app repo specifically* needs on top of it: the hard
> stops, the traps, and which local documents lie.
>
> Where this brief and the blueprint disagree, the blueprint wins.

Hand this to any agent working on `c10vis-poem/Horizons-UI`. Read it fully before
touching anything. It is short on purpose.

---

## 0 · What you are building — reference docs

**You need these. They are NOT in the Horizons-UI repo** — they live in
`c10vis-poem/OBSIDIAN-Master_Wiki`. Get that repo attached, or have the operator
copy the files across. Do not start without them.

### Read these — trustworthy

| Document | What it gives you |
|---|---|
| `canon/horizons-ui/FEATURE-INVENTORY.md` | **Every feature, tagged.** The checklist form — 14 sections, ~120 rows, each with a build state. Use it to know what is wanted vs what exists. |
| `canon/SOURCE-PRECEDENCE.md` | **Which source wins when two disagree.** One page. Read it before you resolve any contradiction — several documents here describe different apps. |
| `canon/horizons-ui/WHAT-IT-IS.md` | **What the app IS and DOES** — the end product. Start here. The three-step workflow, room ownership, `greenLight`'s four named checks, RouterConfig, the three failure faces. |
| `canon/horizons-ui/ROUTER-STEREO-STACK-SPEC.md` | **Router GUI.** Aiwa-style component stereo stack. LOCKED spec, reference image supplied. |
| `canon/horizons-ui/MONITOR-ARCADE-CABINET-SPEC.md` | **Monitor GUI.** Upright arcade cabinet, CRT oscilloscope screen. LOCKED spec. |
| `canon/horizons-ui/TERMINAL-SPEC.md` | **Terminal GUI.** Matrix cascade. LOCKED spec. |
| `canon/horizons-ui/HOME-REDESIGN-SPEC.md` + `home-redesign-img/` (44 images) | Tile styling, colours, labels, icons, panel backgrounds, guardians — **in the operator's own words, with the reference images.** The model for how every spec should read. |
| `canon/horizons-ui/CRASH-ANALYSIS-2026-07-31.md` | What was wrong with the diagnostics and what got fixed. |
| `canon/MASTER-BUILD-BLUEPRINT.md` | The whole system — where this app sits, the circuit, the memory stack, runtime paths. **Marked DRAFT**; structurally right, details still being confirmed. |
| `canon/aesop/PARAMETER-PACKET.md` | The four parameter layers and the series circuit, in detail. |

### Do NOT build from these — they describe different apps

Both are still sitting in `horizons-ui/repo-docs/`. They are kept as history, not
as instructions.

| Document | Why it's poison |
|---|---|
| `FEATURE-SPEC.md` | Describes a **2×3 tile grid** with `ARTIFACTS` and a `ROUTER /route` slug. The tile was **renamed to ARCHIVES**, and the operator explicitly killed that slug: *"No /route at the bottom."* Wrong tile set, wrong arrangement. |
| `HORIZONS_UI_ARCHITECTURE.md` | Describes orchestrating **Claude artifacts** — *"Artifact A can't talk to Artifact B"* — with four control tiers, a left status panel and a right audit queue. **This is a different application.** |
| `horizons-architectural-blueprint-and-ui-spec.md` | Unverified. Treat as history until someone checks it. |
| `horizons-ui/apk-snapshot/` | A **stale** source snapshot. Predates the in-process STT work and wires STT to a dead port. Useful for archaeology, useless as a reference for current state. |

**This is the single biggest trap in this project.** Multiple documents describe
different versions of the app as though each were current. If you build from the
wrong one you will produce something that looks confidently correct and is wrong
throughout — which is exactly what happened last time.

**When documents disagree, use `canon/SOURCE-PRECEDENCE.md`.** Short version: the
shipped code wins, then the operator's line-by-line spec corrections, then the
master plan, then the locked visual specs, then everything else. **Grade, don't
average** — never blend two versions into a third that neither says. If you can't
tell which is current, ask.

---

## 1 · Hard stops

**`HomeGrid.kt` is FROZEN.** Do not edit it. Not for a layout tweak, not for a
"small" fix, not for a build-critical or CI-breaking fix. If it is implicated in a
failure: **stop, report, wait.** Frozen blob: `618cf4b6` (commit `984b061`).

**Do not touch, redesign, or "correct" the home screen.** It is finished and it is
right — a month of hands-on iteration went into it. It is the one part of this app
that is not in question. If a document disagrees with the screen, **the document is
wrong.** Fix the document. Never the screen.

**Do not push `main`.** Do not use `--no-verify`, `push --force`, or `reset --hard`
without asking first.

**Base branch trap.** `main` does **not** contain the working home screen. Run
`git branch -a` before choosing a base. The correct base is
`RELEASE-correct-home-screen-984b0610`. There is more real work on unmerged
branches in this repo than on `main`.

---

## 2 · Decisions already made — do not relitigate

| Decision | Detail |
|---|---|
| **No TTL. Models live in a device folder.** | Weights sit in their own clean folder on device and load by absolute path. Swapping a model is drag-and-drop. **Nothing large ships in the APK.** |
| **The APK ships native libs only** | `libsherpa-onnx-jni.so`, `libonnxruntime.so`. ~20 MB. Everything else is read off the filesystem. |
| **The app's whole job is four things** | screen timeout · permissions · the browser · the WebSockets. If you are writing something outside that list, stop and ask why. |
| **NPU manager = harness inside the APK** | Not a separate out-of-process layer. It holds the context switch between the two on-device models, catches OOM, drives recovery. It dies with the app; that's fine — the app boots empty and recovery restores from a verified profile. |
| **Voice gets proven off-app first** | In a Sherpa-ONNX host app that accepts uploaded models and has a scripting hook. Do **not** build the voice layer into this app to find out whether the models work. |
| **Sideloaded** | The 200 MB Play limit does not apply. Do not contort the design around it. |

---

## 3 · Do NOT build — this is how the last build got wrecked

**The Router does not say "no."**

Previous sessions took the operator's *behavioural* metaphors — "fuse box,"
"10-amp fuse," "breaker" — and compiled them into enforcement code:

- a rigid hardcoded four-item `AssetCheck` list
- a Router that threw red `⚡ FUSE BOX` banners and **blocked** any configuration
  that didn't match its pre-programmed definitions

That destroyed the ability to run custom binaries, fine-tuned weights, or
build-in-place assets. **Do not reintroduce it in any form.**

Correct behaviour:

- The parameter packet is **a plain editable text file.** Not a schema to validate
  against. Not a class. Copyable straight out of the Archives.
- The **Router carries current and doesn't argue.** It attempts to close the
  circuit. If the assets satisfy the requirements, the engine fires. If not, it
  **fails naturally** — no artificial brick wall, no lockout, no red banner.
- The **Monitor holds the gate**, live at flip time. The Router must *consult* it,
  not re-implement it.

**The opposite rule applies to visual references.** "Aiwa CD player" (Router) and
"upright arcade cabinet" (Monitor) are **literal build targets with animations** —
reference images were supplied with "this is what it's going to be." Those are
specs. Build them exactly. Do not soften them into "styling direction."

> Behaviour → never compile it. Appearance → build it exactly.

---

## 4 · Known gaps — VERIFY BEFORE TRUSTING ANY OF THIS

**Every line below is from a stale snapshot or a second-hand audit. Check the live
code before acting on it.** A vault snapshot of this repo was found to predate the
in-process STT work entirely, and a prior AI audit claimed a dozen components were
"completely missing" that in fact existed and were manifest-registered.

- **The daemon appears to suicide when no model is plugged in.** Operator
  observation: it probes for a model at start, finds none, crashes. `CliffordService`
  then relaunches it into the same empty state — a self-feeding crash loop. The fix
  is **already documented** and may have regressed: **serve-first — bind `:8080`
  first, load on a background thread, serve `503` until ready, never suicide on a
  missing model.** *Alive ≠ ready.* **No model is the normal boot state**; the app
  boots empty by design. See `canon/horizons-ui/WHAT-IT-IS.md` §11. Confirm from
  `boot.log`: a repeating `[clifford]` start→exit→start with nothing plugged in.
  **Check this early — it is cheap and it may be the ~90 s crash.**
- **No inbound listener exists.** No `ServerSocket`, no Ktor. The Termux backend is
  absent. This is what blocks Termux getting mic/voice/WebView-OAuth. NPU access
  does *not* need it — the app-spawned daemon already binds `:8080` under the app's
  UID and Termux shares loopback.
- **STT was wired to `127.0.0.1:8091`, which nothing binds.** That made the voice
  loop fall back and look like a model problem. It isn't.
- **`greenLight()` checks 2 of 4 boxes.** The four it is *supposed* to check are
  named in `WHAT-IT-IS.md` §4: **binary presence · exec bit · asset availability ·
  model plugged in.** The exec-bit and handshake checks appear to be missing.
- **`RouterPane.switchOn()` skips the gate entirely** when no `RuntimeDef` matches
  — so cloud/PWA/terminal configs never reach the Monitor.
- **`temperature` is hardcoded** (`NpuClient:101`, `CloudLlmRuntime:122`). The
  **verbosity slider in Settings is read by nothing.** Cores don't exist.
- **First-crash trigger is unproven.** Diagnostics amplifiers were fixed
  (synchronous disk-walking `FailureMonitor` on the main thread; whole-file reads
  dressed as "tails"; uncapped `crash.log`). The *trigger* is still unknown — prime
  suspect is Android LMK, which leaves no stack trace. Answer it on device:
  `cd /sdcard/Android/data/com.horizons/files/diag && tail -40 crash.log`.
  Stack trace present ⇒ JVM exception. Empty but the app died ⇒ killed from
  outside, and no trace will ever appear.
- **Two launcher icons** — `.MainActivity` and `.uilocal.LocalHomeActivity` both
  carry MAIN/LAUNCHER and run different code. Test the tile icon. Removing the
  second entry is a pending operator call.

---

## 5 · Parameter model

Four layers. Parameters belong to one of them — they are not discovered ad hoc and
bolted on:

1. **Weights** — paths, INT8/ONNX quantization limits, tensor allocations
2. **Runtime** — execution flags, RAM allocation, thread bindings, **`temperature`,
   `verbosity`, `cores`**
3. **Engine** — native JNI/C++ layers, VAD sensitivity
4. **Communication** — IPC sockets, WebSocket bridges, API endpoints

Shape `RuntimeDef` to these four **before** building the runtime-agnostic launcher,
or the launcher gets reopened twice.

Authority runs in series: **Settings** supplies · **Terminal** forges (never
executes) · **Monitor** verifies live and dispatches · **Router** carries current ·
**Archives** stores verified profiles and is what recovery restores from.

---

## 6 · How to report

**These are the rules that matter most. The last agent broke all of them.**

- **Read the whole file before editing it.** Read attached documents in full,
  up front. Do not skim, do not shard across subagents, do not defer until context
  gets tight. Burning a dozen tool calls to avoid reading two PDFs costs more than
  reading them and produces worse work.
- **Never claim you read something you didn't.** This poisons everything after it.
- **Never claim it works without evidence** — a green CI run or an on-device check.
  "Implemented" is not "working." Your own report is not evidence.
- **If you're blocked, say so.** Do not invent a path forward and describe it as
  done.
- **Do not describe designed features as built.** Tag state honestly:
  `built-verified` / `built-unverified` / `designed-only` / `absent`.

---

## 7 · Suggested order

1. **Read `crash.log` on device.** One command, answers the biggest open question,
   costs nothing. Do this first.
2. **Verify the live state** of everything in §4 against actual current code. Do
   not inherit those claims — several came from an audit that was wrong in both
   directions.
3. **Close the `switchOn()` bypass** so configs with no `RuntimeDef` reach the
   Monitor instead of skipping the gate. Make `switchOn()` consult `greenLight()`
   rather than re-implement it. **Without adding any blocking behaviour** (§3).
4. **Make the four parameter layers real** in `RuntimeDef` — wire `temperature`,
   `verbosity`, `cores`. Small, self-contained, unblocks the launcher.
5. **Inbound listener** for the Termux backend — mic/voice/OAuth over loopback.
6. Voice layer only **after** it's proven off-app.

Do 1 and 2 before touching code. Most of the last train wreck was acting on stale
claims that a five-minute check would have refuted.

---

## 8 · If something here is wrong

Say so and stop. This brief is derived from documentation that has been wrong
before. A contradiction between this brief and the live code is **information**,
not an obstacle to route around — report it and wait for the operator.

The only thing in here that is not open to question is §1.
