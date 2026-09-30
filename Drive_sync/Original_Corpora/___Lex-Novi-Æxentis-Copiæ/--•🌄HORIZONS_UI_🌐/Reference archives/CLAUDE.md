# CLAUDE.md — Horizons-UI — the app

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
The lifecycle root — **nothing lives without it.** Operator is sole authority on the UI.

### WHAT
The Kotlin APK. Rooms: Monitor, Chat, Settings, Terminal, Archives, Horizons, and the Router hub. Plus the floating tile and the sleep handler.

### WHERE
Node Alpha, the phone.

### WHEN
Boots **empty and stable**. Nothing heavy runs until the operator flips a fuse.

### WHY
It is the surface the whole stack is reached through. Core law: *daemons stay dumb, the user is the loader.*

### HOW
**The app's whole job is four things:** screen timeout · permissions · the browser · the WebSockets. Models live in an external device folder and load by path. Anything outside that list needs justifying.

---

## Delta

**The home screen is DONE — do not touch it.** Everything else: see `AGENT-BRIEF.md` for the hard stops, the traps, and which local documents describe different apps entirely.

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
