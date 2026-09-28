# CLAUDE.md — CI/CD and build infrastructure

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
Build agents.

### WHAT
Workflows, Docker, and the per-repo template used when a domain graduates into its own repo with build tooling.

### WHERE
Applies across repos, not just this one.

### WHEN
On push. The APK build cross-compiles the daemon, builds the APK, publishes to a release.

### WHY
So a green run means something, and so 'it builds' is a check rather than a claim (Rule 4).

### HOW
AGP 8.8.0 · Kotlin 2.1.0 · compileSdk 35 · minSdk 31 · JDK 17 · arm64-v8a.

---

## Delta

⬜ Not established. The live-code audit has not run — do not infer this.

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
