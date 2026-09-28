# AUDIT — Folder 01 · TARGET DOCs (COMPLETE)

**Source folder:** `__NovÆxorpus(NÆX) / 1- TARGET DOCs-(3-S.F.'s=30-files)`
**Auditor:** Claude Opus 4.7 · Session 2026-09-04
**Status:** ✅ COMPLETE — all 30 files read.
**Supersedes:** `AUDIT-01-TARGET-DOCs.md` (v1, in-progress skeleton)

---

## 0. Scope confirmed

| Subfolder | Stated | Read | Notes |
|---|---|---|---|
| `1B-GLM-3-PRELIMINARY_OVERVIEW` | 3 | 3 | Framing docs |
| `1-PRIORITY/1-_S-tier` | 9 | 9 | |
| `1-PRIORITY/2-_A-tier` | 10 | 10 | |
| `1-PRIORITY/3-Findings` | 6+shortcut | 6 unique | 1 file is a shortcut back to S-tier's Definitive Master Spec |
| `CLOSE_2_TARGET//NEEDS WORK` | 2 | 2 | |
| **TOTAL UNIQUE** | 30 | 30 | |

---

## 1. Two-tier verdict summary (per file)

### 1B-GLM-3-PRELIMINARY_OVERVIEW (3 files) — CONSOLIDATE

| # | File | Verdict | Action |
|---|---|---|---|
| 1B.1 | `1- OpenRouter Chat Sun Aug 30 2026.md` (314KB) | **KEEP — primary source** | Rename → `2026-08-30_openrouter_pre-grill-planning-session.md`. **Not the GLM review** (that came later); this is the pre-grill planning session. Contains UNIQUE source for `setup-aesop.sh`, `convert-raw-to-md.py`, `generate-jsonl-markers.py`, GCP Cross-Account Handshake bootstrap, ECC internal routing table (honey-crush/nexus-mapper/ecc-planner/px-reader), the 15-gap list. **Annotate:** assistant hallucinated `https://0x0.st/Xk7p.md` (fake) and fictional `openwiki-obsidian` package — flag both. |
| 1B.2 | `2- fusion-response 2026-08-30.md` (20KB) | Superseded by A-tier `GLM-PT.1-MASTER.DOCUMENT.md` | Merge (Part 8 remainder from 1B.3) then archive |
| 1B.3 | `3- fusion-response 2026-08-30 [8-extended].md` (3KB) | Continuation of 1B.2's truncated Part 8 | Merge into 1B.2 for archive |

### S-tier (9 files) — mixed

| # | File | Verdict | Action |
|---|---|---|---|
| S1 | `1A vault_root/.txt` (3.8KB) | Near-dupe of S2 | Merge with S2 → single `vault_root-schema.md` |
| S2 | `1B- vault_root/.txt` (3.8KB) | Near-dupe of S1 (emoji-colored variant) | Merge with S1 |
| S3 | `Branding ligature` (Gdoc, 3KB) | **CANONICAL brand source — verbatim preserve** | Cross-ref into NAMING-CANON.md; keep as `BRANDING-LIGATURE.md` |
| S4 | `Clarifying -Clean Text- to skills and tools plus outdated architecture (2)` (Gdoc, 12KB) | **HIGHEST VALUE — user's inline annotations on stale architecture** | Extract annotations → standalone `USER-CORRECTIONS-LOG.md`. Wraps around a superseded master spec; the annotations are the gold, the wrapper is dupe of CLOSE_2_TARGET#2 |
| S5 | `Copy of The 3-APK Native Topology & The Concierge Dataflow.` (7KB) | KEEP — load-bearing 3-APK arch | Rename → `3APK-NATIVE-TOPOLOGY.md`; cross-ref with GLM-PT.1 Part 4 |
| S6 | `Definitive Master Specification.txt` (30KB) | **KEEP as one of the two MASTER specs** | This is the 5+1 Tier Cognitive Memory spec v3.0 (vault_root + MAP.md + hierarchical manifest.jsonl protocol + Universal Skill/Tool Extraction Engine + End-of-Day P2P Sync + Sandboxed Red Auditor workflow + RLVR pipeline + complete bash scaffolding script). More coherent than fusion-response. |
| S7 | `ARCHITECTURE BLUEPRINT-(Pt.1).txt` (40KB) | Massive overlap with S8 | Merge S7+S8 → single `ARCHITECTURE-BLUEPRINT.md`; keep S7's "src vs scripts" preamble as unique addition |
| S8 | `ARCHITECTURE BLUEPRINT-(Pt.2).txt` (44KB) | Massive overlap with S7 | Merge target for S7 |
| S9 | `Continual harness online adaptation for self-improving foundation agents.txt` (91KB) | **KEEP VERBATIM — arXiv research paper** | Move to future `reference-papers/` subfolder. Hard rule 3 (no interpretation). |

### A-tier (10 files)

| # | File | Verdict | Action |
|---|---|---|---|
| A1 | `The Manifest Taxonomy (The 5 Document Types).txt` (17KB) | **KEEP — authoritative 5-type taxonomy** (Tool/Skill/Reference/Memory/Data). Also contains a full repo tree with NopeDataBank + Œræcle references | Rename → `MANIFEST-TAXONOMY-5-TYPES.md`; this is a top canonical artifact |
| A2 | `Convert Google Docs to Markdown - Google Search.md` (34KB) | **LOW-VALUE search-results dump** | Kill; if a specific bookmarklet/URL is worth preserving, extract just that; otherwise trash |
| A3 | `Official Google Developer Documentation for System Architecture, Multi-Processing, and Shared Memory Constraints.` (10KB) | **KEEP VERBATIM — official Android reference** (AndroidManifest daemon isolation, ASharedMemory NDK API, UNIX socket FD handshakes via SCM_RIGHTS, Foreground Service for LMK bypass) | Move to `reference-papers/android-multi-process-ndk.md`. Directly applicable to Æsc/Æyre daemon IPC. |
| A4 | `The Consolidated Master README...` (19KB) | Older superseded master; keep only for provenance | Compare to S6 + GLM-PT.1; kill after merging any unique lines |
| A5 | `GLM-PT.2-fusion-response.md` (11KB) | Superseded | Archive with 1B.2/1B.3 |
| A6 | `GLM-PT.1-MASTER.DOCUMENT.md` (25KB) | **THE AUTHORITATIVE CONSOLIDATED MASTER** — 10 parts: Priority table, corrected model pathways, download list, corrected tool roles, prep checklist, Grill Session Manifest, output format, the 15 gaps to fix, naming canon | KEEP as `GLM-MASTER-DOCUMENT.md`; single source of truth for grill session |
| A7 | `Integrating Graphify, Obsidian, and NotebookLM into a local CLI environment .docx` (21KB) | Mostly early-stage tool integration research; useful chunks + lots of URLs; contains OpenWiki 3-layer arch that S6 formalizes | Extract 3-layer summary + tool integration commands → `graphify-obsidian-notebooklm-INTEGRATION.md`; trim URLs |
| A8 | `SQLite.txt` (2KB) | **KEEP — small clarifying tech note** on SQLite via `better-sqlite3` at `~/.omniroute` being file-locked, no conflict with ECC/Prime Agent MCPs | Move to `technical-notes/omniroute-sqlite-isolation.md` |
| A9 | `Architectural realignment.docx` (14KB) | Older priority blueprint + schema — largely superseded by GLM-PT.1 but contains the `AESOP_XI_Skill_Onboarding_Template` JSON schema | Extract JSON schema → standalone `skill_onboarding_schema.json`; rest kill |
| A10 | `The Complete Systems Architecture Blueprint. Accurate launch` (32KB) | Contains 4-bucket physical structure (`/raw_sources/`, `/master_wiki/`, `/inference_skills/`, `/automation_scripts/`) — the alternative to Definitive Master Spec's 5+1 Tier structure | KEEP for schema comparison → `4-bucket-vs-5tier-COMPARE.md`; this pairs directly with schema examples in folder 6 |

### Findings (6 unique + 1 shortcut)

| # | File | Verdict | Action |
|---|---|---|---|
| F1 | `Example 1` (2KB) | Fragment of 5-Layer knowledge architecture (raw_pdf → wiki_md → recall_jsonl → repos → INDEX.jsonl) | Merge with F2, F3, F4 → single `SCHEMA-EXAMPLES-COMPARISON.md` |
| F2 | `Example 2` (4KB, Gdoc) | 3 cognitive memory types + storage/injection/recall layers (episodic/semantic/procedural) | Merge with F1 |
| F3 | `Example 3` (6KB) | The 4-tier vs 5-tier compare + human-cognitive→AI-engineering memory table (Episodic/Procedural/Semantic/Working) | Merge with F1 (this is the CENTRAL reconciliation doc) |
| F4 | `Example 4` (3KB) | 4-tier Cold Archive / Master Wiki / Almanac / Session Logs structure with named source files | Merge with F1 |
| F5 | `Question` (3KB, Gdoc) | User's actual question that prompted F3's reconciliation matrix | KEEP as speaker attribution context (hard rule 4) |
| F6 | `Response.` (7KB, Gdoc) | **HIGH VALUE — the unified 5+1 tier reconciliation matrix** (definitive answer to F5, incl. full canonical directory layout) | KEEP as `RECONCILIATION-5plus1-TIER.md` — this is the ANSWER to the schema wars |
| F7 | shortcut → `Definitive Master Specification.txt` | Same as S6 | Just a pointer — leave in place |

### CLOSE_2_TARGET (2 files)

| # | File | Verdict | Action |
|---|---|---|---|
| C1 | `ACFrOgDK...md` (30KB, PDF conversion) | **IDENTICAL CONTENT to S4** (Clarifying Clean Text) — same 5-file blueprint with same user annotations | Kill; S4 already covers it. This is a PDF re-conversion of the same source. |
| C2 | `AESOP XI: Autonomous Edge-Computing Architecture Blueprint..txt` (15KB) | **KEEP — clean v2.2-Production-Ready spec** (6 priority phases, 4-node infra Alpha/Beta/Gamma/Delta, 3-APK arch, dataflow diagram, home-node topology, GCP handshake, decentralized 10-repo map, universal JSONL marker schema) | Rename → `AESOP-XI-BLUEPRINT-v2.2.md`. This is a **cleaner v2** of the GLM-PT.1 master; the two together triangulate ground truth. |

---

## 2. Global folder-1 kill-list (delete/trash)

**User does the deletion. This is the recommended list, not automatic.**

1. `1B- vault_root/.txt` (S2) — merged into S1
2. `ARCHITECTURE BLUEPRINT-(Pt.2).txt` (S8) — merged into S7
3. `Convert Google Docs to Markdown - Google Search.md` (A2) — search-results dump, no unique value
4. `The Consolidated Master README...` (A4) — superseded by GLM-PT.1 + S6
5. `GLM-PT.2-fusion-response.md` (A5) — superseded by GLM-PT.1
6. `Architectural realignment.docx` (A9) — mostly superseded; extract JSON schema first
7. `ACFrOgDK...md` (C1) — duplicate of S4 (same source, PDF re-conversion)

## 3. Global folder-1 consolidate-list (merge)

| From | Into | Output name |
|---|---|---|
| S1 + S2 | new | `vault_root-schema.md` |
| S7 + S8 | new | `ARCHITECTURE-BLUEPRINT.md` |
| 1B.2 + 1B.3 | new (archive) | `2026-08-30_glm-fusion-response-consolidated.md` |
| F1 + F2 + F3 + F4 | new (with F3 as anchor) | `SCHEMA-EXAMPLES-COMPARISON.md` |

## 4. Global folder-1 lift-out list (extract into named artifacts)

| From | Output artifact | Location |
|---|---|---|
| S4 user annotations | `USER-CORRECTIONS-LOG.md` | Cross-repo canon; belongs in NAMING-CANON.md discipline |
| S7/S8 YAML configs | `file_administrator.yaml` + `oeracle_helpdesk.yaml` | `novaexopia/openwiki-tui-harness/config_profiles/` (future repo) |
| A9 JSON schema | `skill_onboarding_schema.json` | `file-management-and-skills/skill-construction-factory/` (future repo) |
| Setup scripts from 1B.1 | `setup-aesop.sh`, `convert-raw-to-md.py`, `generate-jsonl-markers.py` | `novae-xorpus/tools/` (this repo) |
| GCP Cross-Account Handshake from 1B.1 | `GCP-CROSS-ACCOUNT-HANDSHAKE.md` + `gcp_cross_account_handshake.sh` | `gcp-training-flywheel/` (future repo) |
| ECC routing table from 1B.1 | `ECC-INTERNAL-ROUTING.md` | `agent-harness-hub/ecc/` (future repo) |
| 15-gap list from 1B.1 + A6 | `15-GAPS-TO-FIX.md` | Grill session input |

## 5. Global folder-1 verbatim-preserve list

- **S3 `Branding ligature`** — canonical brand source (motto, ASCII trick, dumbass proof line)
- **S9 `Continual harness online adaptation...`** — arXiv research paper (hard rule 3)
- **A3 `Official Google Developer Documentation for System Architecture...`** — real Google Android reference
- **1B.1 `OpenRouter Chat`** — primary source for setup scripts + GCP handshake (annotated)

---

## 6. Cross-doc drift & inconsistencies detected in folder 1

1. **Naming drift** — `nova-daemon-shell`/`nova-daemon-media` (GLM/1B.2/A6/A10) vs `aesc`/`aeyre` (current NAMING-CANON.md). **User decision needed.**
2. **New entity `Œræcle`** — appears in S7/S8 YAML configs + A1 taxonomy tree. Not in NAMING-CANON.md. Ties to Post-session Target #6 (on-device help desk). **User decision needed: canonize or drop?**
3. **Repo count drift** — GLM-PT.1 lists 12 canonical repos; A10 v2.2 blueprint lists 10; older docs list 8. Need reconciliation.
4. **Priority sequence drift** — every legacy doc has its own priority ordering; user's own annotations in S4 explicitly flag "Priority 4 and 5 are swapped." GLM-PT.1 rearranged as: (1) Grill (2) Curation (3) Harnesses (4) 3-APK **parallel with** (5) Dual-model inference (6) Network integration. **This is the accepted current order.**
5. **Voice stack timing** — some docs place voice in Phase 3, GLM-PT.1 places in Priority 5. GLM-PT.1 wins (voice stack = greenfield, deferred).
6. **`LocalAI` mentions** — appear in older docs (S1/S2, S4, A4, C1). GLM-review superseded → OmniRoute only. Every "LocalAI" mention should be flagged/updated when the doc is repurposed.
7. **`NovA-Claw` / `Novus-Agenti` / `NovA-Corpus`** legacy names in old docs — per NAMING-CANON.md they are superseded to NovÆxopia / NovusÆxenti / NovÆxorpus. Preserve verbatim in-source (hard rule 1) but reject going forward.
8. **Schema conflict** — 4-bucket (A10) vs 5-tier (F1/F2/F4) vs 5+1-tier (F6/S6). **F6's "Response" doc is the resolution** — adopt as canonical layout.
9. **`Twin 9B` in 1B.1** — likely a mishear/typo for `Qwen 9B` or `Gemma 9B`; user's speech-to-text artifact. Flag.

---

## 7. Flags for user decision (2 hard, 3 soft)

### HARD (blocks structural proposals until resolved)

1. **Daemon repo naming: `nova-daemon-shell`/`nova-daemon-media` (GLM ground-truth) vs `aesc`/`aeyre` (NAMING-CANON.md)?**
   - NAMING-CANON.md is your explicitly-authored 2026-08-24 rule. GLM's naming came before that canon was codified.
   - **Recommendation: NAMING-CANON.md wins.** Update GLM-PT.1's 12-repo list to `aesc-daemon-shell` (or just `aesc`) and `aeyre-daemon-media` (or `aeyre`).
2. **Œræcle — canonize or drop?**
   - Appears with real integration hooks (YAML profile in S7/S8, position in A1 taxonomy). Fits the on-device help desk agent role from your Post-session Target #6.
   - **Recommendation: canonize as `Œræcle` (display) / `oeracle` (URL).** Add to NAMING-CANON.md as an 8th named entity (or as a sub-agent role under NovusÆxenti).

### SOFT (can proceed; will use recommendation unless you overrule)

3. Should the 5+1 Tier layout from F6 be the S-tier canonical vault schema? (Recommendation: yes — it's the reconciliation of every schema variant in the corpus, and S6's Definitive Master Spec is built on it.)
4. Should `NovA-Claw` in older docs get bulk-updated to `NovÆxopia` when consolidating? (Recommendation: yes for consolidation copies; **no** in verbatim-preserve archive per hard rule 1.)
5. Should A2 (`Convert Google Docs to Markdown` search dump) be trashed outright or minimally-extracted first? (Recommendation: minimally-extract the bookmarklet reference then trash.)

---

## 8. Feed-forward to folder 2 (PRPSD FILE TREE)

Folder 2 contains 15 files across two subfolders that are DIRECT structure proposals. When I audit folder 2, I will:
- Compare each proposed tree against the **F6 "Response" 5+1 Tier layout** (declared the folder-1 canonical answer to schema wars)
- Compare against the **F4 4-tier layout** and the **F1 5-layer conceptual flow**
- Note where folder-2 trees are stale (mention LocalAI, NovA-Claw, old repo names)
- Assemble a single-page comparison matrix

---

## 9. Feed-forward to folder 5 (ARCH.MATRIX)

Folder 5's `PLUGINS TOOLS AND MEMORY LAYER ARGUMENTS-(13-files)` and `PROPOSED WORKFLOWS AND FILE STRUCTURES-(8-files)` will heavily overlap with folder-1 A1 (Manifest Taxonomy), A6 (GLM-PT.1), A10 (v2.2 Blueprint), F6 (5+1 reconciliation). Audit will explicitly diff against these folder-1 anchors rather than re-summarize.

---

## 10. Running task-state (for cross-folder synthesis in Task #9)

**Named entities catalogued so far (canonical + candidate):**

- Confirmed canon (NAMING-CANON.md): NovÆxorpus, NovusÆxenti, NovÆxopia, Æsop-Xi, Horizons-Ui, Æsc, Æyre
- **Candidate additions**: Œræcle (help desk oracle), NopeDataBank (Red Agent's isolated data bank), Files Executive Agent (OpenWiki TUI operator)
- **Superseded aliases** (preserve verbatim in-source, do not use forward): NovA-Claw, Novus-Agenti, NovA-Corpus, nova-daemon-shell, nova-daemon-media, AESOP XI (→ Æsop-Xi)

**Canonical schema (folder-1 winner):** F6 "5+1 Tier" — `vault_root/{MAP.md, manifest.jsonl, 01_raw_sources/, 02_master_wiki/, 03_recall_cache/, 04_skills_runtime/, 05_episodic_logs/}` with distributed per-tier `manifest.jsonl`s.

**Canonical taxonomy (folder-1 winner):** A1 "5 Doc Types" — Tool / Skill / Reference / Memory / Data.

**Canonical 12-repo partition (folder-1 winner):** A6 GLM-PT.1 list — pending user resolution of Flag #1 (daemon naming).

---

*Folder 01 audit COMPLETE. Proceeding to Folder 02 autonomously per your cadence choice.*
