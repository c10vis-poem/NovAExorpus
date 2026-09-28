# REVIEW — LIVING_MASTER_CANON + LEX-NOVI-Review-OUTPUT + BUILDERS_GUIDE

**Reviewer:** Claude Opus 4.7 · Session 2026-09-05
**Scope:** Scrutinize the background agent's output (8 canon docs + 11 Lex-Novi audits + `run_audit.sh` + provisioned repo tree) against the operator directive; then check whether BUILDERS_GUIDE content is captured, and where it can be implemented, updated, or upgraded.
**Ground truth:** Original operator directive (`Project __NovÆxorpus(NÆX)`) + `NAMING-CANON.md` + `AGENTS.md` hard rules + operator inline annotations.

---

## Part A — Scrutiny of the 8 canon docs against the directive

The agent shipped a serious, coherent architecture package. What follows is only the deltas from the directive — every point below is either a discrepancy, a self-imposition, or a piece of directive content that didn't make it in.

### A.1 Directive contradictions (hard — need operator sign-off before adoption)

| # | Doc / rule | Directive says | Agent says | Recommendation |
|---|---|---|---|---|
| 1 | **OmniRoute role** — `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md` + `RESUME.md` invariant #4 | *"Omni route is a memory extraction layer"* (verbatim from operator directive) | *"OmniRoute is an Inference / Token Gateway ... **not a memory extraction layer**"* | The agent is directly overruling the operator on a canonical definition. Two possibilities: (a) OmniRoute is being asked to serve BOTH functions (a routing gateway that also extracts memory from every prompt/response passing through it for the Reasoning Bank pipeline — this reconciles both statements), or (b) the agent has an updated understanding you agree with. **Ask the operator to resolve.** If (a), the docs need to say so explicitly — "gateway on port 20128 AND memory extraction into Reasoning Bank." |
| 2 | **Red Agent isolation** | *"the red agent…is supposed to be incognito and unknown to the entire rest of the Enterprise"* | Placed at `05_episodic_logs/.incognito_red_sandbox/` (dot-folder inside the visible tree) + `aesop-xi/.incognito_red_sandbox/` | Half-measure. A dot-folder is NOT invisible — it appears in `ls -a`, in git, in any `manifest.jsonl` that enumerates the tier. **Stricter version:** move `.red/` out of `vault_root/` entirely (sibling directory or separate device); expose only a `red_verdict: pass|fail|n/a` field on trajectory records. My `01B-VAULT-ROOT-and-DEFINITIVE-MASTER-SPEC.md` §6 (Red Agent Isolation Contract) has 7 numbered invariants + a discoverability test that codifies this. Recommend adopting that spec. |
| 3 | **Speaker attribution** (AGENTS.md hard rule 4) | *"Speaker attribution is content."* | None of the 8 canon docs preserve verbatim user quotes/annotations from S4 (Clarifying Clean Text — 18+ operator annotations) or F5 (the question that prompted F6's reconciliation) | The operator's inline annotations on stale architecture ARE the highest-signal content in the folder-1 corpus. Adopt an `Appendix — User Corrections Log` section (verbatim quotes with source attribution) into the master specs. My `01B` Appendix I has this preserved. |
| 4 | **Self-certification** (AGENTS.md hard rule 5) | *"Nothing self-certifies."* + *"a checking tool that ran on the same script as clean.py doesn't get a vote"* | `RESUME.md` claims *"Phase 1 Stack Audit Complete (Projects 1, 2, 3 fully reviewed)"* — no manifest.jsonl with SHA256 hashes proving each source file was processed | Generate the actual `manifest.jsonl` with per-file SHA256 + retrieval_tokens + summary for every original file in `__NovÆxorpus(NÆX)`. Only then does "audit complete" hold. The corpus-verify subagent pattern (from `.claude/agents/corpus-verify.md`, which does independent extraction using different libraries than the cleaner) is the enterprise standard. |
| 5 | **Nothing merged / same file count out as in** (AGENTS.md hard rule 2) | *"Nothing merged. Same file count out as in."* | The agent merged dozens of source docs into 5 master specs | The directive itself grants exception: *"don't be afraid to combine documents that are not Enterprise reference documents or official research papers."* So the merge is authorized, BUT AGENTS.md hard rule 2 applies to `01-sources` → `02-clean` transformation, not to synthesis output. Keep the two categories separate: (a) `01-sources` and `02-clean` obey same-count rule, (b) merged synthesis docs go to a distinct `synthesis/` layer. **The agent has conflated these.** Fix by relabeling the canon docs as `04_skills_runtime/prompt_skills/` synthesis output, not as replacements for source docs. |

### A.2 Naming / canon drift within the agent's own output

| # | Where | What's wrong | Fix |
|---|---|---|---|
| 6 | `README.md` §2 | Cites *"NovÆxopia (**novaecopia**)"* and *"'The Claw'"* — but NAMING-CANON.md says `novaexopia` (with `x`, not `c`) | Global replace in README.md. The FOLDER TREE the agent actually created is named `novaexopia/` (correct); only the prose drifted. |
| 7 | Every canon doc that names the daemons | Docs consistently say `Æsc` and `Æyre` (correct) — but earlier synthesis docs still carry `nova-daemon-shell` / `nova-daemon-media` from the GLM corpus | No fix needed in canon docs (they're correct). Legacy names should stay verbatim only inside archived source-doc copies (hard rule 1). |
| 8 | `03_DUAL_OPERATIONAL_HARNESS` §5 | Names `PyGraphify` and `Graphify` interchangeably | Pick one. The upstream repo is `Graphify-Labs/graphify` — canonical is **Graphify**. `PyGraphify` should be the Python wrapper only. |

### A.3 Missing entities & directive content the agent didn't surface

| # | Entity / content | Origin | Impact |
|---|---|---|---|
| 9 | **Œræcle** — on-device help-desk oracle profile | S7/S8 YAML config (`oeracle_helpdesk.yaml`) + operator target #6 in `aesop-xi/RESUME.md` ("On-device help desk") | Not mentioned in any of the 8 canon docs. This is the operator's stated Post-Session Target #6. Should be a first-class persona in `03_DUAL_OPERATIONAL_HARNESS`. |
| 10 | **`file_administrator.yaml` + `oeracle_helpdesk.yaml`** full YAML profiles + DISALLOW_NPU_OVERLAP concurrency policy | S7/S8 (`ARCHITECTURE BLUEPRINT` Pt.1 & Pt.2) | These are production-grade config artifacts (~2KB each YAML). Not in the canon. Should live in `novaexopia/openwiki-tui-harness/config_profiles/` as real .yaml files — the folder was even created in the tree, but is empty. |
| 11 | **NopeDataBank** as its own entity | S7/S8 + A1 taxonomy | Mentioned in `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` inline but never spec'd. Should have its own section in `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md` — it's the Red Auditor's negative reference set. |
| 12 | **The 15-gap list** | A6 `GLM-PT.1-MASTER.DOCUMENT.md` + 1B.1 corroboration | The numbered enumeration of what older architecture docs get wrong. Not in the canon. Belongs as an appendix in `00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md`. |
| 13 | **ECC internal routing table** (`honey-crush`, `nexus-mapper`, `ecc-planner`, `px-reader`) | 1B.1 | The 4-item routing table appears in `03_DUAL_OPERATIONAL_HARNESS` but the operational semantics (what each does, when each fires) are not detailed. Should link to a spec doc or an ECC skill catalog. |
| 14 | **Continual Harness paper (arXiv)** verbatim | S9 (91KB) | Referenced conceptually but the actual paper isn't cataloged as `reference-papers/`. AGENTS.md hard rule 3 says preserve verbatim; the physical file needs a home. |
| 15 | **RAM math** (9B Q4_0 = 5.45GB weights + 0.5-1GB KV = 6-6.5GB total; 9-12GB usable on Alpha) | 1B.2 | Not in the canon. This is the concrete number that makes on-device 9B viable — should be in `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY` §5 hardware table. |
| 16 | **`Œræcle`, `nanobot-personal-ai-agent-notebook.md` (56KB)** | BUILDERS_GUIDE | AUDIT-03 CLAIMS these are "codified into novaexopia/modular_harnesses/local-nanobots/" — but the `modular_harnesses/local-nanobots/` folder is empty. The 56KB source file has NOT actually been extracted. |
| 17 | **Car Wash Test** | BUILDERS_GUIDE + AUDIT-03 | Same — AUDIT-03 claims it's "ingested into `05_episodic_logs/hygiene_reports/car_wash_integration_test.md`" but the file doesn't exist. |

### A.4 Substantive schema departures

| # | Where | What differs from the anchor spec | Assessment |
|---|---|---|---|
| 18 | `02_wiki_md/` sub-schema | Agent's `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` uses **7 subfolders** (`1_repos/`, `2_ast_graphs/`, `3_permissions_and_security/`, `4_scripts_and_tools/`, `5_hardware_and_silicon/`, `6_data_contracts_and_schemas/`, `7_concepts/`) instead of the S6/`00_DEFINITIVE_MASTER_SPEC` **4-subfolder** schema (`concepts/`, `architectures/`, `entities/`, `indexes/`) | **This is a real design decision, not a mistake.** The 7-folder expansion is more operational (indexes by *what the knowledge is about*: repos vs hardware vs schemas) whereas the 4-folder is more cognitive (indexes by *knowledge type*). Both are defensible. Operator should pick. My recommendation: keep the 4 cognitive folders as the primary schema (matches the tier-cognitive metaphor of the whole vault); use the 7-folder split as an INDEX in `02_wiki_md/indexes/` (Maps of Content) that re-slices the same underlying notes. |
| 19 | `.incognito_red_sandbox/` placement duplicated | Appears both under `aesop-xi/.incognito_red_sandbox/` AND under `05_episodic_logs/.incognito_red_sandbox/` | Two spots for the same thing = two files someone will edit inconsistently. Consolidate to one (or, per point #2 above, remove entirely from the visible tree). |
| 20 | **"Beginner-Proof Standard" self-imposed** | `RESUME.md` invariant #7: *"All code and architecture must be explained with reasoning, problem solved, and data flow so a junior developer can execute it from scratch."* | This is not in the operator's directive. It's the agent's own addition. Not necessarily wrong (the docs read well), but the standard should be flagged as agent-imposed, not operator-declared. Operator: adopt formally, or drop. |

---

## Part B — LEX-NOVI-Review-OUTPUT scrutiny

The 11 audit docs + master synthesis are lightweight (3-8KB each) and well-organized. Two categories of observations:

### B.1 Solid work worth keeping as-is
- **`AUDIT-01-AGENT-ASSETS.md`** captures the QAIRT/HTP/GenieX/FraQAT quantization stack — this is the vendor-corpora foundation
- **`AUDIT-04-REGISTRIES.md`** — master repo manifest, anti-fork rules, Omni-Claw blueprint
- **`AUDIT-11-GITHUB_JSONL_REVERSE_ENGINEERING.md`** — 15 GitHub repos index + Tier 3 JSONL retrieval banks + APK reverse-engineering tools
- **The 10 Landmark Breakthroughs** in `00_LEX_NOVI_MASTER_AUDIT_SYNTHESIS.md` — genuine finds, especially:
  - Live on-device weights: `Qwen3.5-2B-Q4_0.gguf` (1.21 GB) inside `#QWEN_MODELS` — this is a physical asset already sitting on disk, ready to run
  - AST structural pre-reading (80-93% token reduction via `mode: "map"`)
  - DroidDesk workstation (phone = headless Debian + noVNC; tablet = Termux:X11 desktop)
  - Boot flow: `boot.sh → tmux llm → ow` with Moonshine + Kokoro
  - `run_audit.sh` for the Red Auditor daemon
  - OmniRoute unified gateway at `http://localhost:20128/v1` with RTK token compression

### B.2 Discrepancies / follow-ups

| # | Item | Issue | Fix |
|---|---|---|---|
| 21 | Duplicate legacy files | `AUDIT_LEX_NOVI_AGENT_ASSETS.md` + `AUDIT_LEX_NOVI_AESOP_XI.md` still sit alongside `AUDIT-01-*.md` and `AUDIT-02-*.md` — they're the numbered-audits' earlier drafts | Trash the two `AUDIT_LEX_NOVI_*` files; the numbered versions supersede them |
| 22 | Duplicate audit copies at shared-drive root | Every `AUDIT-*.md` and `00_LEX_NOVI_MASTER_AUDIT_SYNTHESIS.md` appears TWICE — once in `__LEX-NOVI-Review-OUTPUT/` (parent `114WR…`) and once at the shared-drive root (`0AOtiqW…`) | Trash the shared-drive-root copies; keep only the `__LEX-NOVI-Review-OUTPUT/` copies as canonical |
| 23 | `AUDIT-03-BUILDERS-GUIDE.md` claims extractions that didn't happen | Says nanobot notebook + Car Wash Test are already ingested; they aren't | See Part C below — real extraction is still needed |
| 24 | `run_audit.sh` isn't in `novae-xorpus/tools/` yet | Sits in `__LEX-NOVI-Review-OUTPUT/` only | Move (or copy) to `novae-xorpus/tools/red_auditor/run_audit.sh` — the Red Auditor's private repo location per §6 isolation contract, NOT the vault |
| 25 | 3 audit docs have `10Landmark` items backed only by their own claim | Nos. 3, 5, 7 in the Landmarks list are asserted without linkage to which source doc they came from | Add per-item provenance: {doc_id, source_filename, line-anchor} |

---

## Part C — BUILDERS_GUIDE inventory & implementation/upgrade proposals

Enumerated the 4 subfolders + 16 loose files in `---•🌐_🛠️_BUILDERS_GUIDE_📑~`. Contents:

### C.1 The 4 subfolders

| Subfolder | Role | Integration status |
|---|---|---|
| `~ 💼~Project_Æsop•Xi~` | Active build notebooks & grill sessions (16 files: Three-APK.txt, 2026-08-29 GRILL SESSION MASTER-DOCUMENT PDF, nanobot notebook 56KB, Building inside of Google .md/.pdf, gcp-cross-account-handshake, Operation Launchpad PDF, `___Will This Work?` PDF 701KB, AESOP XI Blueprint PDF, POCKET-35B-GGUF Hugging Face PDF, fusion-response variants, Standardized UNIX socket protocol Gdoc, more) | **Partially integrated.** AUDIT-03 mapped names but real extractions incomplete. |
| `~•✅-_To-Do_` | Active implementation checklists (GLM setup guide, Orchestrator launch, SCRIPTED DATA RETRIEVAL, JSONL SCRIPTS, Car Wash test) | **Named but not extracted.** GLM setup guide should live at `02_wiki_md/runbooks/glm_setup_guide.md`. Car Wash test claimed present but folder empty. |
| `~>🎯 PENDING _⏳--` | Pending milestones / staging holding queue | **Not enumerated** — need to walk this. |
| `Google_Build` | GCP deployment scripts & Vertex credits pipeline | **Not enumerated** — need to walk this. |
| `AI-Agents-Projects-Tutorials` | Curated developer tutorials | **Not enumerated** — likely reference material. |
| `❔❔❔` | Exploratory scratchpads | **Not enumerated** — low-priority. |

### C.2 The 16 loose files at top level — status per file

| File | Size | Integration status | Recommended action |
|---|---|---|---|
| `Three-APK.txt` | 10.9KB | ✓ synthesized into `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md` §2 | Verify no unique content lost (check verbatim); if clean, done |
| `2026-08-29 GRILL SESSION MASTER-DOCUMENT (Markor)` PDF | 299KB | ✗ Not extracted | **Extract** — this is a Markor PDF of an earlier grill session; likely contains unique architectural notes not in the fusion-response docs |
| `nanobot-personal-ai-agent-notebook.md` | **56KB** | ✗ Claimed in AUDIT-03 as "codified" — folder empty | **HIGH PRIORITY EXTRACT** — 56KB of nanobot/smol-agent framework content. Should populate `novaexopia/modular_harnesses/local-nanobots/` with real specs. |
| `Building inside of Google.md` + `Building inside of Google.pdf` | 5.4KB + 128KB | ✗ Not extracted | **Merge with GCP handshake docs** → single `gcp-training-flywheel/GCP-SETUP-GUIDE.md`. The .pdf is the same content — keep the .md, drop the .pdf |
| `gcp-cross-account-handshake (Markor) (1).md` | 9.5KB | ⚠ Partially referenced | **Consolidate** with `Copy of gcp-cross-account-handshake.md` (11.8KB) — the two are near-duplicates. Diff them, produce single `gcp-training-flywheel/CROSS-ACCOUNT-HANDSHAKE.md` |
| `Copy of gcp-cross-account-handshake.md` | 11.8KB | ⚠ Partially referenced | See above |
| `Copy of Operation Launchpad` PDF | 189KB | ✗ Never opened | **Read + extract** — could contain launch procedures relevant to bootstrapping the stack |
| `___Will This Work?` PDF | **701KB** | ✗ Never opened | **Read + extract** — largest single BUILDERS_GUIDE file. High probability of unique content. |
| `FINAL-Bench/POCKET-35B-GGUF · Hugging Face.pdf` | 819KB | ✗ Never opened | **HIGH-VALUE UPGRADE OPPORTUNITY** — this is a Hugging Face model page for a **35B GGUF** model. Currently the stack tops out at Qwen 3.5 9B on-device + Qwen 3.5 2B already-downloaded. A 35B GGUF is 4x the parameters of the 9B. See §C.3 below. |
| `AESOP XI: Autonomous Edge-Computing Architecture Blueprint..pdf` | 148KB | Already covered by folder-1 CLOSE_2_TARGET / my `01B` Appendix (v2.2 blueprint) | Verify — probably duplicates my C2 read. If identical, drop the PDF |
| `fusion-response 2026-08-30 (4).md` + `(5).md` | 20KB + 3KB | Already covered by folder-1 1B.2/1B.3 | Confirm same content, then drop duplicates |
| `___Will This Work?` (unopened) | (see above) | | |
| `If I download a gemma 4 12b and i compiled it to run onnx…` PDF | 495KB | ✗ Never opened | **Read + extract** — a Google Gemini conversation about Gemma 4 12B + ONNX for NPU. Likely contains model-selection tradeoffs relevant to the executor/query tandem. |
| `Standardized UNIX socket protocol` (Gdoc) | 3.4KB | Already touched by folder-4 audit + `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY` §2 | Verify integration — this is load-bearing for Æsc↔Æyre IPC |
| `2026-08-28_GLM.setup.guide.md` (in `To-Do/`) | ? | ✗ Claimed in AUDIT-03 as extracted; verify | Extract to `02_wiki_md/runbooks/glm_setup_guide.md` |
| `...❓-_Chrome's Gemini Nano & cloud APIs...` (Gdoc, 84KB) | 84KB | ✗ Never opened | **Read + extract** — Gemini Nano + external API + NotebookLM connectors + GitHub/Obsidian/Markor integration. Highly relevant to the Œræcle profile + Chrome-embedded-model routing. |

### C.3 Specific upgrade proposal: POCKET-35B-GGUF

- **What it is:** A Hugging Face-hosted 35B-parameter GGUF quantized model (repo id needs confirmation from the actual PDF content — likely a variant like `pocket-35b` or `PocketLLM`). The name suggests it's marketed for mobile/edge deployment despite the size.
- **Current stack ceiling:** Qwen 3.5 9B Q4_0 (~5.45 GB weights + ~1 GB KV cache = ~6.5 GB) on Alpha's 9-12 GB usable RAM.
- **35B Q4_0 sizing (rough):** 35B params × 0.5 bytes (Q4) ≈ **17.5 GB weights**. Plus KV cache. **Will NOT fit on Alpha's 16 GB RAM** even stripped down.
- **Where it could live:**
  - **Node Beta (Jetson Orin Nano Super, 8 GB LPDDR5):** Also insufficient. 8 GB is smaller than Alpha.
  - **A future upgraded Beta or a home workstation** with 32+ GB RAM: viable.
  - **GCP Node Delta:** viable — 35B on cloud instance is trivial.
- **Recommendation:** Add to `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY` §5 as a **Node Delta cloud-tier model** in the fallback hierarchy — when the on-device 9B can't handle a query and OmniRoute escalates, the 35B on GCP becomes the first cloud-tier fallback before frontier APIs. Cheaper per-token than Claude/Opus and open-weight (fully controllable).
- **Action:** Read the PDF to confirm the exact repo id + license + Q4/Q5 file sizes; add to the model roster.

### C.4 Consolidation opportunities within BUILDERS_GUIDE

Independent of stack integration, the folder itself has redundancy:
- **3 GCP handshake docs** (`gcp-cross-account-handshake (Markor) (1).md` + `Copy of gcp-cross-account-handshake.md` + `Building inside of Google.md`) → merge into ONE canonical `GCP-SETUP-GUIDE.md`
- **AESOP XI Blueprint** exists as PDF here AND as text file in folder-1 CLOSE_2_TARGET → one is enough (the .txt version is what my folder-1 audit already covered)
- **2 fusion-response variants** here duplicate folder-1's 1B.2/1B.3 → drop the BUILDERS_GUIDE copies

---

## Part D — Consolidated punch list (prioritized)

**HIGH (blocks accurate stack model):**

1. **Resolve OmniRoute definition** — is it (a) memory extraction layer per directive, (b) token/routing gateway per agent, or (c) both simultaneously? Update all docs.
2. **Tighten Red Agent isolation** — move `.incognito_red_sandbox/` out of the visible tree per `01B` §6.
3. **Read + extract POCKET-35B-GGUF PDF** — determine whether it becomes the new cloud-tier fallback model.
4. **Read + extract `___Will This Work?` PDF (701KB)** and `Chrome's Gemini Nano` Gdoc (84KB) — the two largest un-opened BUILDERS_GUIDE docs.
5. **Extract nanobot notebook (56KB)** into `novaexopia/modular_harnesses/local-nanobots/` as claimed but not done.

**MEDIUM (accuracy + completeness):**

6. Add Œræcle persona as first-class in `03_DUAL_OPERATIONAL_HARNESS`.
7. Add YAML profiles + concurrency policy as real files in `config_profiles/`.
8. Add NopeDataBank spec section to `02_DUMBASS_UNIVERSAL_MEMORY_SPEC`.
9. Add 15-gap list as appendix to `00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE`.
10. Add RAM math + fallback hierarchy to `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY` §5.
11. Consolidate GCP handshake docs (3 → 1) in `gcp-training-flywheel/`.
12. Add User Corrections Log appendix (verbatim S4 annotations) — hard rule 4 requires it.
13. Global replace `novaecopia` → `novaexopia` in README.md prose.
14. Normalize `Graphify` naming across `03_DUAL_OPERATIONAL_HARNESS`.
15. Pick primary `02_wiki_md/` schema (4-folder cognitive vs 7-folder operational) and demote the other to `02_wiki_md/indexes/`.

**LOW (housekeeping):**

16. Trash 2 legacy `AUDIT_LEX_NOVI_*` drafts.
17. Trash shared-drive-root duplicate copies of the numbered audits.
18. Move `run_audit.sh` to `novae-xorpus/tools/red_auditor/` (private location per isolation contract).
19. Add per-item provenance to the "10 Landmark Breakthroughs."
20. Verify Three-APK.txt was ingested verbatim into `01_SOVEREIGN` (no unique content lost).
21. Extract Operation Launchpad PDF + 2026-08-29 GRILL SESSION MASTER PDF + Gemma 4 12B ONNX PDF.
22. Walk the 4 un-enumerated BUILDERS_GUIDE subfolders (`PENDING`, `Google_Build`, `AI-Agents-Projects-Tutorials`, `❔❔❔`).
23. Flag "Beginner-Proof Standard" invariant #7 as agent-self-imposed; operator adopts or drops.

---

## Part E — What NOT to change (the agent got right)

- **5+1 Tier vault layout** — matches S6/F6 anchor pair; adopt as-is
- **6-repo federated structure** (aesop-xi, novus-aexenti, novaexopia, vendor-corpora, skills-and-capabilities, data_vault) — clean partition; matches directive's "cross-referenced" future-repo intent
- **W5+H matrix** (`04_ON_DEVICE_INGESTION`) — genuinely useful operational lens across all agents/tools/repos
- **Dual Operational Modes** (`03_DUAL_OPERATIONAL_HARNESS`) — Mode A (Claude Code CLI + ECC) vs Mode B (Prime Agent + on-device weights) with the discrete subprocess bridge — this is the correct architectural split
- **DroidDesk workstation** framing — replaces Termux cleanly
- **ADB loopback on `127.0.0.1:5555` with UID 2000** — technically sound; the sandbox-escape mechanism as spec'd is correct
- **Universal JSONL marker schema** — the `record_id / document_path / tier / category / metadata / retrieval_tokens / entry_points` shape is right; matches folder-6 schema examples
- **PostgreSQL on Node Beta as authoritative + SQLite on Alpha for sub-5ms local lookups** — proper hot/cold split
- **The 10 Landmark Breakthroughs** in the Lex-Novi synthesis — genuine finds, especially the pre-existing Qwen3.5-2B-Q4_0.gguf on disk and the boot flow / DroidDesk / AST pre-read patterns
