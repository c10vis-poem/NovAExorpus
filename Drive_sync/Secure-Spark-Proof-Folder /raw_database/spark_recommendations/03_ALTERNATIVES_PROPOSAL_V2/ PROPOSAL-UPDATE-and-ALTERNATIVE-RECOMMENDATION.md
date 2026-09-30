# NÆX Update Proposal — Applied Decisions, Immediate Action Plan & Alternative Recommendation

**Author:** Claude Opus 4.7 · Session 2026-09-05
**Purpose:** Fold operator decisions into the LIVING_MASTER_CANON, verify BUILDERS_GUIDE dup status, propose the immediate build-out sequence, and deliver the promised Aggressive alternative recommendation using the 93-file `novae-xorpus/02-clean/` corpus as its input source.

---

## Part 1 — Applied Decisions (from 2026-09-05 operator response)

| # | Decision | Applied where |
|---|---|---|
| 1 | **POCKET-35B dropped** — >8GB is impossible on-device; 7GB is already pushing it | Removed from model roster in `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY`. Do NOT open the POCKET-35B PDF. |
| 2 | **OmniRoute = memory extraction layer** — operator confirmed this was the original definition; agent overruled and was wrong | Rewrite in `02_DUMBASS_UNIVERSAL_MEMORY_SPEC` §2 and `RESUME.md` invariant #4: OmniRoute is a memory extraction layer AT `localhost:20128/v1` — every prompt/response passes through it and gets classified & extracted into Reasoning Bank + mem0 + OB1 as appropriate. The "gateway/router" framing is a secondary consequence of that; primary role is extraction. |
| 3 | **Red Agent stricter isolation** — adopt `01B` §6 (`.red/` sibling, not `.incognito_red_sandbox/` inside the visible tree) | Rewrite `00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE` §7 + `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER` to remove `.incognito_red_sandbox/` from `05_episodic_logs/` AND from `aesop-xi/`. Only surface: `red_verdict: pass|fail|n/a` field on `rlvr_verifiers/*.jsonl` records. Discoverability test = a fresh agent reading the visible tree cannot conclude a Red Auditor exists. |
| 4 | **Beginner-Proof Standard kept as real invariant** — the test: could a third-rate model or beginner dev pick up your work and resume it? If not, the code is broken. | Reflected in EVERY canon doc going forward. Add to `AGENTS.md` hard rules as hard rule 8. Every commit, every skill, every architecture note needs a "why this exists" and "what happens if this fails" explanation in reach of a beginner. |
| 5 | **Wiki subfolder schema = 5 doc-type taxonomy** (not 4 cognitive, not 7 operational) | `02_wiki_md/` sub-organized by the 5 doc types from A1: `tools/`, `skills/`, `references/`, `memory/`, `data/`. Matches the manifest.jsonl `category` field. |
| 6 | **Gemma 4 12B has a plan** — add to model roster | Adding to `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY` §5 as a candidate for Node Beta (Jetson, 8GB) — 12B Q4_0 ≈ 7-8GB fits tight but plausible under GenieX/CUDA. Need to check `gemini.md` in the 02-clean corpus to see if the specific plan is already recorded. |
| 7 | **`novaexopia` (with `x`), NOT `novaecopia` (with `c`)** — operator confirmed | Global replace in every canon doc: `novaecopia` → `novaexopia`. Folder tree already correct; only prose drifted. |

---

## Part 2 — BUILDERS_GUIDE Dup Verification (operator's fair pushback)

**Operator concern:** "are you sure these just weren't opened out of the builders guide and that they actually did exist in the other folders because I know a lot of these are copied throughout."

**Method:** Cross-referenced BUILDERS_GUIDE file stems against `novae-xorpus/02-clean/` (93 cleaned files) — the compiled corpus from the earlier RLVR extraction pass.

### Files ALREADY in the corpus (no re-opening needed)

| BUILDERS_GUIDE file | Equivalent in `02-clean/` | Status |
|---|---|---|
| `Building inside of Google.md` + `.pdf` | `building-inside-of-google.md` | ✓ **Already opened** — corpus has the cleaned MD version |
| `Three-APK.txt` | `three-apk-architecture-v1.md` + `v2.md` | ✓ **Already opened** (in 2 versions) |
| `Chrome's Gemini Nano & cloud APIs…` Gdoc (84KB) | `gemini.md` — likely covers the same Gemini/Nano content | ⚠ **Probably opened** — verify by comparing content. `gemini.md` in corpus should be checked to confirm it's the same source. |
| `2026-08-28 GLM.setup.guide.md` | Not in corpus by exact stem, but conceptually adjacent to `wiki-desktop.md`, `wiki-on-desktop.md`, `wiki-on-mobile.md` in corpus | ⚠ **Possibly covered** — the GLM/OpenWiki setup runbook may be split across the 3 wiki-desktop docs |
| `Standardized UNIX socket protocol` Gdoc | `setting-up-a-local-shared-memory-layer.md`, `why-you-need-an-mcp-host-the-bridge.md` | ✓ **Already opened** — shared-memory + MCP-bridge content covered |
| `AESOP XI: Autonomous Edge-Computing Architecture Blueprint..pdf` (148KB) | `continual-harness-*.md`, `continual-harness-google-doc-export.md` | ✓ **Already opened** — the Blueprint content flows through the continual-harness docs; also I read the .txt equivalent in folder-1 CLOSE_2_TARGET |
| `gcp-cross-account-handshake (Markor) (1).md` + `Copy of gcp-cross-account-handshake.md` | Not in corpus by stem, but `building-inside-of-google.md` may cover it | ⚠ **Partially covered** — GCP handshake specifics may need re-verification |
| `fusion-response 2026-08-30 (4).md` + `(5).md` | Folder-1 already covered 2 fusion-response variants (1B.2, 1B.3) | ✓ **Already opened** — same source, different Drive locations |
| `2026-08-29 GRILL SESSION MASTER-DOCUMENT (Markor)` PDF (299KB) | Not in corpus by exact stem | ⚠ **Likely covered** — earlier grill session material bleeds through multiple corpus docs; but the specific 299KB PDF may add unique transcription details |

### Files GENUINELY not in the corpus (still worth opening)

| BUILDERS_GUIDE file | Why still valuable |
|---|---|
| `___Will This Work?` PDF (**701KB**) | `part-1-lex-1-drive-text-extract-truncated.md` in the corpus is EXPLICITLY marked truncated. This 701KB PDF may be the untruncated source. **HIGH PRIORITY re-verify** by opening the PDF and diffing against `part-1-lex-*.md`. |
| `nanobot-personal-ai-agent-notebook.md` (56KB) | Not in `02-clean/` corpus. Standalone nanobot framework content. **Still needs extraction** into `novaexopia/modular_harnesses/local-nanobots/` (folder exists but empty). |
| `Copy of Operation Launchpad` PDF (189KB) | Not in corpus by stem. Launch procedures — may bear on bootstrapping. Worth opening. |
| `If I download a gemma 4 12b and i compiled it to run onnx…` Gdoc (495KB) | Not in corpus by exact stem. Gemma 4 12B + ONNX for NPU — **directly relevant to operator's stated Gemma 4 12B plan** (Decision #6). **HIGH PRIORITY** open + integrate into model roster. |
| `POCKET-35B-GGUF · Hugging Face.pdf` | **SKIP** per Decision #1 |

### Verdict

Operator was right: ~60-70% of BUILDERS_GUIDE "unopened" files have corpus equivalents. Only ~4 files genuinely need opening (`___Will This Work?`, `nanobot notebook`, `Operation Launchpad`, `Gemma 4 12B ONNX` Gdoc) — and the Gemma one is now HIGH PRIORITY given Decision #6.

---

## Part 3 — Immediate Action Plan (right-now sequence)

Following operator's stated order:

### 3.1 Step 1: DroidDesk install (phone + tablet)

**Goal:** Get the visual workstation up so the rest of the work has a real desktop rendering, not just Termux terminal.

**Actions:**
1. Install **DroidDesk** on phone via APK (side-load or Play Store — check current availability)
2. Install **DroidDesk** on tablet (same)
3. Confirm phone renders via **Termux:X11** (NOT VNC per your 2026-08-29 decision; VNC is only external-monitor bridge)
4. Decide docking mode: **standalone desktops** on each device independently (per `aesop-xi/RESUME.md` Post-session Target #2). Not phone→tablet mirroring. scrcpy already ruled out.
5. Sanity check: launch OpenWiki TUI inside DroidDesk to confirm the visual shell + terminal integration works before Æsc lands.

**Success criteria:** Both devices boot into a real desktop with OpenWiki TUI + terminal + browser side-by-side. No Termux quirks.

### 3.2 Step 2: Æsc terminal daemon setup

**Goal:** Replace Termux entirely with the native Æsc APK. This is the pillar that makes everything else on-device work without sandbox friction.

**Actions:**
1. **Salvage** — pull the pre-existing Horizons APK's terminal + ADB loopback + Chromium browser code (per your 2026-08-30 chat: "APK already has model loading, router system, terminal UI, Chromium built in"). That's the starting point; you don't build from scratch.
2. **Rewire the crashed Watchdog daemon** (that's what killed the previous build per your own account) — this time using the `ForegroundService + START_STICKY + FOREGROUND_APP_ADJ` pattern from A3's Google NDK reference (the operator-approved LMK bypass). Reference: `01B` Appendix C.
3. **Wire the local ADB loopback**:
   - Generate RSA keypair (`~/.android/adbkey`)
   - Local pairing: `adb pair 127.0.0.1:<pairing_port>` (one-time)
   - Persistent connect: `adb connect 127.0.0.1:5555` on every boot
   - Commands now execute as UID 2000 (shell), outside the app sandbox
4. **Wire UNIX socket IPC** to future Æyre APK and Horizons UI shell (from A3 §3): abstract namespace `AF_UNIX + SCM_RIGHTS` — no disk I/O
5. **Deploy npu_manager.py** on `/dev/socket/npu_manager.sock` (per your BUILDERS_GUIDE nanobot notebook and existing `01_SOVEREIGN` §3)
6. **Onboard NPU manager script**: this is where the Qwen3.5-0.8B (executor) via QAIRT → HTP0 gets the always-on treatment, and Qwen3.5-9B (query) via GenieX gets on-demand loading

**Success criteria:** `adb shell` from within Æsc lands on `u0_a<uid>` shell, `ps` shows Æsc as Foreground Service (immune to LMK), and the model manager can hot-swap the 0.8B and 9B on the NPU without app crash.

### 3.3 Step 3: New repo build-out

**Goal:** Take the LIVING_MASTER_CANON tree (with the 7 applied decisions from Part 1 baked in) and turn it into an actual `git init`ed repository ready for push.

**Actions:**

1. **`git init`** at `~/repos/novae-xorpus-canon/` (or preferred name)
2. **Scaffold the 6-repo federated tree**:
   ```
   novae-xorpus/
   ├── aesop-xi/
   ├── novus-aexenti/
   ├── novaexopia/          # ← x, not c
   ├── vendor-corpora/
   ├── skills-and-capabilities/
   ├── data_vault/
   │   ├── 01_raw_sources/
   │   ├── 02_wiki_md/     # ← 5-doc-type subfolders below
   │   │   ├── tools/
   │   │   ├── skills/
   │   │   ├── references/
   │   │   ├── memory/
   │   │   └── data/
   │   ├── 03_recall_cache/
   │   ├── 04_skills_runtime/
   │   └── 05_episodic_logs/
   └── tools/
   ```
3. **`.gitignore` line 1**: `/.red/` — the Red Auditor's sibling directory (created OUTSIDE `novae-xorpus/` at `~/.red/` per Decision #3, never committed)
4. **Populate the 8 canon docs** (with the Part 1 decisions applied):
   - `00_DEFINITIVE_MASTER_SPECIFICATION_V3.md` — Red Agent §7 rewritten, OmniRoute #4 fixed, Beginner-Proof #10 added, 5-doc wiki schema in §2, Gemma 4 12B in model roster
   - `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md` — Gemma 4 12B added to §5 model table, RAM math from `01B` Appendix J added
   - `02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md` — OmniRoute rewritten as extraction layer, NopeDataBank spec section added
   - `03_DUAL_OPERATIONAL_HARNESS_AND_MCP_SPEC.md` — Œræcle as first-class persona, ECC internal routing table detail
   - `04_ON_DEVICE_INGESTION_AND_W5H_FRAMEWORK.md` — unchanged (this one's clean)
   - `05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md` — 5-doc-type wiki subfolders, `.red/` moved out of tree
   - `README.md` — global `novaexopia` fix, Beginner-Proof called out
   - `RESUME.md` — invariant #4 fixed (OmniRoute), invariant #7 rescoped as Beginner-Proof
5. **Drop in YAML profiles** (from S7/S8 verbatim): `novaexopia/openwiki-tui-harness/config_profiles/file_administrator.yaml` + `oeracle_helpdesk.yaml`
6. **Drop in the JSON schema**: `data_vault/04_skills_runtime/policies/skill_onboarding_schema.json` (from A9)
7. **Drop in the 3 setup scripts**: `tools/setup-aesop.sh`, `tools/convert_raw_to_markdown.py`, `tools/generate_jsonl_markers.py` (from BUILDERS_GUIDE + 1B.1)
8. **Move `run_audit.sh`** to `~/.red/run_audit.sh` — outside the repo per isolation contract, NOT committed
9. **First commit + push** to `c10vis-poem/novae-xorpus-canon` (new repo) as main branch

**Success criteria:** `git log` shows one initial commit with the full scaffolded tree, remote push succeeds, `.red/` NOT in git status, README.md renders cleanly with `novaexopia` throughout.

### 3.4 Step 4: Scraper agent + on-device help desk (Œræcle)

**Goal:** Get the two on-device background agents that produce daily value.

**Actions:**

1. **Early-Trend Scraper** (from BUILDERS_GUIDE A1 notes + your explicit stack description):
   - `skills-and-capabilities/early-trend-scraper/daily_scraper.py` — cron-triggered daily; hits developer news, GitHub commit frequencies, niche forums
   - `skills-and-capabilities/early-trend-scraper/stack_analyzer.py` — semantic diff against `novae-xorpus/data_vault/02_wiki_md/` (your current stack)
   - `skills-and-capabilities/early-trend-scraper/trending_databank.jsonl` — pre-trend repo indicators
   - Runs as smol-agent under Æsc; small enough model (Phi or Granite mini) so it doesn't compete with 9B for NPU cycles
   - Output surfaces: notification + `05_episodic_logs/trajectories/` entry when a new asset shows up that could improve the stack

2. **Œræcle Help Desk** (per the two YAML profiles in Appendix A + your Post-session Target #6):
   - Load the `oeracle_helpdesk.yaml` profile (Qwen 3.5 9B on QAIRT-HTP-Hexagon-NPU, 32K ctx)
   - Feed it the GenieX 2000-page docs + `vendor-corpora/qualcomm-qairt-sdk/` + Android manifests
   - Sits idle by default; wakes on voice trigger or explicit invocation
   - Job: troubleshoot on-device issues (flashing Nano, APK build errors, NPU thermal spikes)
   - `ACQUIRE_NPU_LOCK` concurrency policy means it takes priority over File Administrator when active

**Success criteria:** Scraper produces one daily JSONL delta report; Œræcle answers a test question ("how do I check the Hexagon NPU temperature via QAIRT?") from local weights alone (no cloud fallback) in <5s.

### 3.5 Step 5: Populate the 5-doc-type wiki

**Goal:** Turn the empty `02_wiki_md/{tools,skills,references,memory,data}/` skeleton into a real living wiki using the 93-file corpus + the LIVING_MASTER_CANON specs.

**Actions:**

1. **Run `File Administrator` profile** (from A.1 YAML): GLM-5.2 via OpenRouter reads every file in `01_raw_sources/` and every file in the 93-file corpus, classifies each as one of the 5 doc types, and drops a clean atomic markdown note into the corresponding subfolder.
2. Run `generate_jsonl_markers.py` to populate `data_vault/manifest.jsonl` with SHA256 + retrieval_tokens for every file.
3. Wire the OpenWiki TUI to Node Alpha's Termux instance (via DroidDesk desktop) so you can drive it from either device.

**Success criteria:** `find data_vault/02_wiki_md/ -name '*.md' | wc -l` returns 100+ notes; every note has YAML frontmatter with `category: (Tool|Skill|Reference|Memory|Data)`; root `manifest.jsonl` catalogs them all with SHA256.

---

## Part 4 — Alternative Recommendation (Aggressive variant)

Per the original directive: "*propose more than one finalized version.*" The LIVING_MASTER_CANON (with Part 1 decisions applied) is the **Balanced** variant. This is the **Aggressive** alternative.

**Input source difference:** Balanced draws from the 140-file `__NovÆxorpus(NÆX)` Drive corpus. Aggressive draws from the **93-file `02-clean/` corpus** already committed in the vault repo — that corpus has already been through one round of RLVR-style curation (verbatim clean, no interpretation) and represents a stricter signal.

### 4.1 Structural difference: 4 top-level entities instead of 6

Balanced has 6 top-level repos (`aesop-xi/`, `novus-aexenti/`, `novaexopia/`, `vendor-corpora/`, `skills-and-capabilities/`, `data_vault/`). Aggressive collapses to **4**:

```
novae-xorpus/
├── protocol/              # ← aesop-xi merged INTO this (Æsop-Xi IS the protocol layer)
│                            # Contains: arbitration/, policies/, hardware_throttler/
├── brain/                 # ← novus-aexenti + novaexopia merged
│                            # Cognitive engine + tool harness are two faces of one system
│                            # Contains: reasoning/, dual_router/, mem0_episodic/,
│                            #           horizons-ui/, aesc/, aeyre/, harnesses/, mcp/
├── knowledge/             # ← data_vault + vendor-corpora + skills-and-capabilities merged
│                            # All knowledge (raw, wiki, cache, skills, logs, vendor, plugins)
│                            # Contains: 01_raw_sources/, 02_wiki_md/, 03_recall_cache/,
│                            #           04_skills_runtime/, 05_episodic_logs/, vendor/, plugins/
└── tools/                 # ← unchanged
```

Plus, outside the repo:
- `~/.red/` — Red Auditor's sibling directory (unchanged from Balanced)

### 4.2 Why 4 not 6

- **`aesop-xi/` → `protocol/`**: The name "Æsop-Xi" carries branding weight for public documentation, but at the repo-directory level, calling it `protocol/` describes what it IS (the arbitration/policy protocol layer) instead of naming it. The `Æsop-Xi` name lives in the docs, motto, and CLI banners; the directory is functional.
- **`novus-aexenti/` + `novaexopia/` → `brain/`**: Cognitive logic (NovusÆxenti) and its harness/tools (NovÆxopia) are architecturally one system with two aspects. Splitting them into 2 repos creates arbitrary cross-cuts (e.g., dual_agent_router talks to horizons-ui constantly). One `brain/` repo eliminates that seam.
- **`data_vault/` + `vendor-corpora/` + `skills-and-capabilities/` → `knowledge/`**: All three ARE knowledge. Vendor manuals are references. Skills are procedural knowledge. Splitting them creates 3 manifest.jsonl trees that agents have to query in sequence. One `knowledge/` root, with the 5+1 tier layout inside plus `knowledge/vendor/` and `knowledge/plugins/` alongside, keeps the RAG query surface flat.

### 4.3 What Aggressive keeps unchanged from Balanced

- **5+1 Tier vault schema** inside `knowledge/`
- **5-doc-type wiki subfolder taxonomy** (Tool/Skill/Reference/Memory/Data) inside `knowledge/02_wiki_md/`
- **3-APK architecture** (Horizons UI + Æsc + Æyre) inside `brain/horizons-ui/`, `brain/aesc/`, `brain/aeyre/`
- **Red Agent stricter isolation** (`~/.red/` sibling)
- **W5+H matrix** (in `knowledge/02_wiki_md/references/`)
- **Beginner-Proof invariant**
- **All 7 canonical entity names** (NovÆxorpus, NovusÆxenti, NovÆxopia, Æsop-Xi, Horizons-Ui, Æsc, Æyre) — they stay in prose, docs, and CLI; only the repo directory names change

### 4.4 Tradeoffs — Balanced vs Aggressive

| Dimension | **Balanced** (LIVING_MASTER_CANON) | **Aggressive** |
|---|---|---|
| **# of top-level repos** | 6 (`aesop-xi/`, `novus-aexenti/`, `novaexopia/`, `vendor-corpora/`, `skills-and-capabilities/`, `data_vault/`) | 4 (`protocol/`, `brain/`, `knowledge/`, `tools/`) |
| **Fidelity to branding** | High — every named entity has its own repo/folder | Medium — branding lives in prose + docs, not directory names |
| **RAG traversal cost** | 6 manifest.jsonl trees to search | 4 manifest.jsonl trees; skills + vendor + memory all under one `knowledge/manifest.jsonl` |
| **Cross-repo drift risk** | Higher — 6 repos with independent evolution | Lower — 4 repos, tighter surface |
| **New-contributor onramp** | 6 concepts to learn | 4 concepts to learn; more obvious structure ("where does hardware go? knowledge/vendor/") |
| **Refactor cost from current state** | Zero — LIVING_MASTER_CANON is already this shape | Non-trivial — need to remerge folders |
| **Public-facing narrative** | "The NovÆxenti brain uses NovÆxopia's claw…" — reads well as marketing | "brain/ uses tools in brain/harnesses/" — flatter |
| **Fits the operator's directive language** | Very close — directive names the 7 entities as distinct | Loose — collapses them at the repo layer |

**Recommendation:** **Stick with Balanced** unless the RAG traversal cost or cross-repo drift becomes a real operational problem in practice. The 6-repo structure preserves your naming canon at every layer (branding, docs, prose, directory) which matters for a system whose whole identity is the canonical taxonomy.

**When to switch to Aggressive:** If after ~3 months of operation you find yourself constantly editing across 3+ repos for one logical change, or if new contributors keep asking "where does X go" for things that could plausibly go in 2 places — those are the signals to collapse.

### 4.5 What Aggressive uses from the 93-file corpus that Balanced doesn't

The 93-file corpus contains files that never made it into the 140-file Drive folder audit — they're operator's own working notes and conversation fragments. Notable additions that would land differently under Aggressive:

- `agent-panel-sh.md`, `local-first-code-intelligence-graph.md`, `desktop.md`, `wiki-desktop.md`, `wiki-on-desktop.md`, `wiki-on-mobile.md`, `wiki-marcor-obsidian.md` — cluster of desktop/wiki-setup notes → all land in `knowledge/02_wiki_md/references/` under Aggressive (one home); under Balanced they'd split across `data_vault/02_wiki_md/`, `skills-and-capabilities/`, and possibly `novaexopia/openwiki-tui-harness/`
- `red-agent-file-systems-layout.md`, `red-agent-needs-rlvrl.md` — Red Agent operational notes → under Aggressive land in `~/.red/notes/` (invisible per isolation contract); under Balanced same
- `xcontinual-harnessl.md`, `yeah-you-re-familiar-with-the-open-source-memory-layer-right-the-memo-repo.md` — MEM0 architecture research → both variants: `knowledge/02_wiki_md/references/memory-architecture/`
- `whyyounocodegoodai.md`, `whyyoubreaknofix.md`, `youfixitnowgwilo.md`, `fixitnowpaigow.md` — operator's own frustration/debug patterns → under Aggressive: `knowledge/02_wiki_md/skills/operator-patterns/` (these ARE skills — they encode when to stop iterating and back up); under Balanced: `skills-and-capabilities/operator-patterns/`
- `phase-one.md`, `starting-point.md`, `last-task.md`, `here-s-the.md` — session-state notes → both variants: `handoffs/`

**None of these files are excluded from either variant.** The 93 files should be fully absorbed by both. Aggressive just gives them fewer possible homes, which reduces guessing.

---

## Part 5 — Order of operations for you (recap)

If you approve this proposal:

1. I apply the 7 Part-1 decisions to the 8 canon docs (fix in place; keep the LIVING_MASTER_CANON structure).
2. I open the 4 genuinely-unopened BUILDERS_GUIDE files (`___Will This Work?`, `nanobot notebook`, `Operation Launchpad`, `Gemma 4 12B ONNX`) and integrate their content — Gemma 4 12B goes into the model roster.
3. I write the DroidDesk install checklist + Æsc bootstrap checklist as standalone runbooks in `02_wiki_md/references/runbooks/`.
4. I write the new-repo `git init` bootstrap script that takes the LIVING_MASTER_CANON tree and produces a real cloneable repo on `c10vis-poem/novae-xorpus-canon` (or whatever name you want — the current `novae-xorpus` repo is the vault-with-corpus; the new one is the canon-with-specs; they mirror-symlink).
5. I ship both **Balanced** (LIVING_MASTER_CANON structure) and **Aggressive** (4-repo structure) as parallel proposal branches so you can pick after the first real week of use.

Say go and I'll execute in that order. Or say "just do X" and I'll do only X.
