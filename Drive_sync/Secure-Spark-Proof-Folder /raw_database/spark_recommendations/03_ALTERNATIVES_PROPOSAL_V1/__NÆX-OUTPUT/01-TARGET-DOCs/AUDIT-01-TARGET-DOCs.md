# AUDIT — Folder 01 · TARGET DOCs

**Source folder:** `__NovÆxorpus(NÆX) / 1- TARGET DOCs-(3-S.F.'s=30-files)`
**Auditor:** Claude Opus 4.7 · Session 2026-09-04
**Status:** IN PROGRESS (S-tier + GLM prelim complete; A-tier / Findings / CLOSE_2_TARGET pending)

---

## 0. Reading order (strict, per user instruction "do not bounce around")

1. `1B-GLM-3-PRELIMINARY_OVERVIEW/` — 3 files (frame-setter, all consolidated post-GLM ground truth)
2. `1-PRIORITY/1-_S-tier/` — 9 files
3. `1-PRIORITY/2-_A-tier/` — 10 files
4. `1-PRIORITY/3-Findings/` — 7 files (incl 1 shortcut → S-tier)
5. `CLOSE_2_TARGET//NEEDS WORK/` — 2 files

**Actual unique-file count: 30** (7 in Findings but one is a shortcut; matches user's stated "30")

---

## 1. GLM Preliminary Overview (subfolder `1B-GLM-3-PRELIMINARY_OVERVIEW`)

These three files together constitute the **consolidated post-GLM-5.2-review ground truth** and should be treated as authoritative context for interpreting every other doc in the corpus.

| # | File | Size | Verdict |
|---|---|---|---|
| 1 | `1- OpenRouter Chat Sun Aug 30 2026.md` | 314KB | RAW conversation log; delegated to subagent for structured extraction (in progress) |
| 2 | `2- fusion-response 2026-08-30.md` | 20KB | **AUTHORITATIVE.** The final consolidated post-corrections master doc — Parts 0-8 (Branding, Priority Sequence, Model Pathways, Downloads, Tool Roles, Repo Partitioning, Salvaged APK, Prep Checklist, Grill Session Manifest). |
| 3 | `3- fusion-response 2026-08-30 [8-extended].md` | 3KB | Extended Part 8 (Grill Session Manifest) that got truncated in file 2. Merge target: append to file 2. |

**Consolidation call:** Files 2 + 3 → merge into a single "GLM-CORRECTED-MASTER.md" (adds file 3's Part 8 remainder to file 2's Parts 0-7). File 1 (OpenRouter chat) preserve as raw provenance in archive; extract citation-ready notes into a "GLM-REVIEW-NOTES.md."

### Corrections established by the GLM review (must-preserve ground truth)

- **Executor model** = Qwen 3.5 0.8B via **QAI Hub → QAIRT runtime → HTP0 (Hexagon NPU v79)**. NOT llama.cpp, NOT GenieX.
- **Query model** = Qwen 3.5 9B (Unsloth GGUF) via **GenieX `llama_cpp` → GGML Hexagon backend → librc → kernel → HTP0**. `--device npu` pinned. Can call frontier models (Claude, GLM 5.2, Fable 5, Opus, Gemini) as tool calls.
- **Memory pipeline canonical order:** OmniRoute/SQL → Reasoning Bank → OB1 → mem0 → Daemons/Models
- **RLVR = Reinforcement Learning with Verifiable Rewards** (verifier is exogenous/deterministic — compiler, linter, graph engine — NEVER a neural network). Not "Vector Reasoning."
- **OmniRoute (not LocalAI)** is the routing gateway. `novae-xorpus` still mistakenly cites "OpenAI" in places — must be corrected.
- **Voice stack (Silero VAD + Moonshine STT + Kokoro TTS)** = Phase 3 (post-APK build). Greenfield work; no prior art on Android.
- **12-repo partition** (canonical): `file-management-and-skills`, `horizons-ui`, `nova-daemon-shell`, `nova-daemon-media`, `agent-harness-hub`, `omni-route-gateway`, `obsidian-knowledge-vault`, `aesop-xi`, `novae-xorpus`, `red-agent-auditor`, `node-beta-jetson`, `gcp-training-flywheel`.
  - **⚠ Naming drift from NAMING-CANON.md:** GLM-corrected repo names use `nova-daemon-shell` / `nova-daemon-media` while the current NAMING-CANON.md canonicalizes as `aesc` / `aeyre`. **Flagged for user resolution.**
- **4-Bucket physical / 5-Layer conceptual data flow:** `raw_sources → master_wiki → inference_skills → automation_scripts` (physical); `raw_pdf → wiki_md → recall_jsonl → repos/scripts → INDEX.jsonl` (conceptual).

---

## 2. S-tier (subfolder `1-PRIORITY/1-_S-tier`)

9 files. Reading order (numbered prefix where present, then largest→smallest):

| # | File | Size | Content class | Verdict |
|---|---|---|---|---|
| S1 | `1A vault_root/.txt` | 3.8KB | Vault directory schema (5-tier + metacognitive) | **DUPLICATE of S2** (near-identical, only emoji-comment styling differs). Merge → keep S1 as canonical, retire S2 |
| S2 | `1B- vault_root/.txt` | 3.8KB | Same as S1 with color-coded emoji labels ([METACOGNITIVE], TIER 1-5) | **Merge into S1 as a "styling variant" appendix**, or drop entirely |
| S3 | `Branding ligature` (Gdoc) | 3KB | **CANONICAL brand source** — Xçineribus motto, Æsc/Æyre pairing, "It Isn't dumbass-proof if it hasn't been #d.u.m.b.a.s.s. proven" tagline, ASCII trick (`Æ`/`æ`) | **KEEP VERBATIM.** Cross-ref target for NAMING-CANON.md |
| S4 | `Clarifying -Clean Text- to skills and tools plus outdated architecture (2)` (Gdoc) | 12KB | Older master architecture with **user's own inline annotations flagging what's stale** (priority-sequence swap, 3-APK not integrated, "LocalAI" superseded, references outdated) | **HIGHEST VALUE — user annotations = ground truth.** Extract the annotations into a standalone "USER-CORRECTIONS-LOG.md" (they belong in NAMING-CANON.md discipline as well) |
| S5 | `Copy of The 3-APK Native Topology & The Concierge Dataflow.` | 7KB | Concrete 3-APK arch (Horizons UI + Shell Daemon Æsc + Media Daemon Æyre) w/ Webview/WebSocket bridge, executor/query tandem, Universal JSONL KAG/RAG marker system, Prime Agent Continual Harness detail | **KEEP** — current & load-bearing. Cross-ref against fusion-response Part 4 |
| S6 | `Definitive Master Specification.txt` | 30KB | **The 5+1 Tier Cognitive Memory spec** (v3.0) — vault_root, MAP.md, hierarchical manifest.jsonl protocol, Universal Skill & Tool Extraction Engine, End-of-Day P2P Sync + Cross-Auditor + Sandboxed Red Auditor workflow, RLVR pipeline, complete bash scaffolding script | **KEEP as MASTER SPEC.** This is the most coherent single document in the S-tier. Wraps and formalizes what 1A/1B sketch out. |
| S7 | `ARCHITECTURE BLUEPRINT-(Pt.1).txt` | 40KB | Contains: "What src means" preamble, 3 cognitive memory types, unified memory bank tree, Manifest Taxonomy (5 doc types), YAML profile configs (File Administrator + Œræcle Help Desk) | **DUPLICATE OF S8.** ~70% overlap. Everything in Pt.1 also appears in Pt.2. Merge → keep the unique preamble ("src vs scripts") from Pt.1, drop the rest. |
| S8 | `ARCHITECTURE BLUEPRINT-(Pt.2).txt` | 44KB | Same content as Pt.1 (redundancy analysis, 4-plane rewrite, Manifest Taxonomy, YAML profiles) — **starts with the Lex-Novi audit that Pt.1 has later on** | **Merge target for Pt.1's unique preamble** → produce single "ARCHITECTURE-BLUEPRINT.md" |
| S9 | `Continual harness online adaptation for self-improving foundation agents.txt` | 91KB | arXiv research paper (verbatim per hard rule 3) — Continual Harness / Online Adaptation for foundation agents | **KEEP VERBATIM.** Do not summarize; this is a research reference. Move to a `reference-papers/` subfolder in the final tree. |

### New canonical entity discovered

**Œræcle** (rendered `Œræcle-Oracle` in YAML) — the on-device Help Desk Oracle profile. Qwen 3.5 9B GGUF Q4_0 via QAIRT-HTP-Hexagon-NPU, 32K context. Sits inside `novaexopia/openwiki-tui-harness/config_profiles/` per S7/S8. **Not in NAMING-CANON.md yet.** Ties directly to user's Post-session Target #6 in `aesop-xi/RESUME.md` ("On-device help desk"). **Flag for user: adopt as canonical name or drop?**

### Named YAML profiles worth extracting as standalone tools

- `file_administrator.yaml` — File Administrator (GLM-5.2, native-libc-cpu, 8K ctx, write-mutation to novae-xorpus)
- `oeracle_helpdesk.yaml` — Œræcle Help Desk (Qwen-9B-Q4_0, qairt-htp-hexagon-npu, 32K ctx, read-only to source docs, mem0 + ob1_static_protocol)

Both should live in `novaexopia/openwiki-tui-harness/config_profiles/` per the S7/S8 spec. **Extract as .yaml files** into the OUTPUT folder for the future repo bootstrap.

---

## 3. A-tier (10 files) — PENDING
## 4. Findings (7 files) — PENDING
## 5. CLOSE_2_TARGET (2 files) — PENDING

---

## Running kill-list / consolidate-list (folder 01 only, will update)

**Consolidate:**
- S1 + S2 → single vault_root.md (near-dupes)
- S7 + S8 → single ARCHITECTURE-BLUEPRINT.md (major overlap)
- 1B-GLM #2 + #3 → single GLM-CORRECTED-MASTER.md

**Extract & lift out:**
- S3's brand assets → into NAMING-CANON.md discipline
- S4's user annotations → standalone USER-CORRECTIONS-LOG.md
- S7/S8's YAML configs → real .yaml files in config_profiles/

**Verbatim preserve (do not touch):**
- S9 (Continual Harness paper)
- S3 (Branding ligature — canonical source)
- All 3 GLM prelim files (as archive of the review session that established ground truth)

**Flag for user:**
- Naming drift: `nova-daemon-shell`/`nova-daemon-media` (GLM) vs `aesc`/`aeyre` (NAMING-CANON.md). Which wins?
- New entity Œræcle — canonize or drop?

---
*Audit continues — A-tier next batch.*
