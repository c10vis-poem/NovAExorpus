---
title: "MASTER_COMPILATION_EXECUTION_PLAN_AND_HANDOFF.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/01_MASTER_MIRROR_GLIDE/MASTER_COMPILATION_EXECUTION_PLAN_AND_HANDOFF.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# MASTER COMPILATION EXECUTION PLAN & HANDOFF PROTOCOL
**Ecosystem**: Project NovÆxorpus (NÆX) & NovusÆxenti Living Master Canon
**Motto**: *Xçineribus, in-variis-nunquam-varius, Novi-Æxentis-Copiæ, Vincent*
**Scope**: Complete end-to-end execution blueprint and operational handoff for compiling raw
corpus assets into the canonical repository mirrors.
**Archive Package**: `NovAeXorpus_Complete_Mirrors.zip` (Local Sandbox & Drive Mirror)

---

## 1. Executive Summary & Architectural Foundation

This execution plan provides the definitive, self-contained handoff for the next agent session to
finalize the compilation of the raw documentation corpus into the standardized repository
structure.

### The Canonical Repositories
1. **`novae-xorpus`**: Central Living Wiki vault (18 first-class cuts) and `#d.u.m.b.a.s.s.`
integrated memory core.
2. **`novus-aexenti`**: Cognitive MoE reasoning engine (0.8B Triage vs 9B Executor) and
Reasoning Bank recovery flywheel.
3. **`novaexopia`**: "The Claw" runtime, OpenWiki TUI, 8 modular swarm harnesses, and MCP
capability bridge.
4. **`aesop-xi`**: Universal orchestration, ethical policy governance, and hardware arbitration.
5. **`horizons-ui`**: Master visual presentation shell (Android Chromium WebView / Jetpack
Compose tiles).
6. **`novus-aesc`**: Native system terminal daemon (`WirelessAdbBridgeService.kt` on
`127.0.0.1:5555`).
7. **`novus-aeyre`**: Native media & sensory ingress daemon (Silero VAD, Moonshine ONNX
STT, Kokoro-82m TTS).

---

## 2. Non-Negotiable Operational Laws

Every incoming agent must strictly comply with these core invariants:
1. **The Non-1:1 Condensation Law**: Strip conversational filler, redundant logs, and duplicate
boilerplate, but preserve 100% of technical rules, parameters, build flags, and schemas so that
raw and clean markdown build the exact same output.
2. **Red Auditor Complete Stealth Invariant**: The Red Auditor is strictly excluded from all
public manifests, maps, and repository trees. It resides exclusively in `~/.red/`, exposing only
`red_verdict: pass|fail|n/a` on trajectory records.
3. **Locality of Reference**: Skills (`skills/`) and executable tools (`tools/`) must be co-located
directly inside the repository where they are applied.


4. **MAP.md vs. manifest.jsonl (The First-Move Directive)**:
   - `MAP.md`: Human/agent orientation index in Markdown with `[[wikilinks]]`. Read on session
start.
   - `manifest.jsonl`: Machine RAG index, JSON Lines with SHA256, tokens, category,
retrieval_tokens. Queried via stream filter, never loaded whole into context.
   - Sequence: Read root `MAP.md` ➔ Read tier `MAP.md` ➔ Query `manifest.jsonl` ➔ Load
targeted files only.
5. **Extractor Independence (Hard Rule 5)**: The tool that cleaned a file cannot grade the
cleaning. Verification must run via `corpus-verify` (`tools/check.py`) using disjoint extraction
libraries (`pypdf`, `zipfile+xml.etree`, `html.parser`).

---

## 3. Phase-by-Phase Compilation Workflow

### Phase 1: Ingestion & Normalization (`raw/` ➔ `clean_md/`)
* **Input**: Raw source documents in `02_MY_ORIGINALS`
(`1Zy4qUXM999ojqaYj-ByZ-6n3rbsll0wo`) and vendor archives.
* **Execution**:
  1. Run `convert_raw_to_markdown.py` to normalize documents into clean UTF-8 Markdown
with standardized YAML frontmatter (`id`, `tier`, `category`, `sources`, `tags`).
  2. Execute `doc_to_skill_and_tool.py`:
     - Reasoning heuristics and workflows ➔ `skills/` (`SKILL.md` format).
     - Executable bash/python code ➔ `tools/` (with standard argument parsing and exit codes).

### Phase 2: Independent RLVR Verification (`clean_md/` ➔ `audit/`)
* **Execution**:
  1. Run `corpus-verify` (`tools/check.py`) across all generated clean Markdown notes.
  2. Evaluate `find_atoms()` (URLs, measurements, paths, version strings) and `chunk_split()`
segment containment.
  3. Output discrepancies to `audit/03-check/`. If any named technical atom was dropped, block
compilation and regenerate.

### Phase 3: Machine Cache Generation (`clean_md/` ➔ `chunk.jsonl`)
* **Execution**:
  1. Run `generate_jsonl_markers.py` to generate pre-tokenized 256-token passages into
`chunk.jsonl`.
  2. Compute SHA-256 checksums, token counts, and retrieval tags.
  3. Compile the local repository `manifest.jsonl`.

### Phase 4: Living Wiki Population (`clean_md/` ➔ `wiki_md/` in `novae-xorpus`)
* **Execution**:
  1. Ingest clean notes into the 18 first-class branches of `02_wiki_md/`:


     - `vendors/`: Deep trees for Google, Qualcomm, Nvidia, GitHub, Anthropic, PrimeIntellect,
DeepSeek.
     - `weights/`: Active (0.8B, 9B, 2B), candidates (Gemma 4 12B, Phi-4-Mini), voice, and vision
models.
     - `runtimes/` & `engines/`: QAIRT, GenieX, llama.cpp, ONNX RT, Moonshine, Kokoro.
     - `harnesses/` & `agents/`: ECC, Prime Agent, DeepSeek harness; Œræcle, File
Administrator, Cross-Auditor.
     - `protocols/`: Æsop-Xi, MCP, W5+H, ADB loopback, OmniRoute extraction.
     - `memory-subsystem/`: OmniRoute (20128), Reasoning Bank, OB1, mem0, SQLite,
Postgres, Continual Harness.
     - `architectures/`, `runbooks/`, `entities/`, `projects/`, `references/`, `operator-log/`, `indexes/`.
  2. Enforce bidirectional `[[wikilinks]]` across all concepts.

---

## 4. Subsystem Wiring Invariants

* **OmniRoute Gateway**: Configured as an asynchronous memory extraction tap on
`localhost:20128/v1`. Intercepts all traffic, extracts trajectories into `reasoning_bank/` and habits
into `mem0/`, then routes to providers.
* **The Laptop Trick**: `WirelessAdbBridgeService.kt` in `novus-aesc` maintains the
`127.0.0.1:5555` ADB loopback with UID 2000 shell privileges and a `ws://localhost:8080/shell`
terminal pipeline, running as a `START_STICKY` Foreground Service.
* **Hexagon Dual-Payload Asset Pattern**: In `novus-aexenti` and `horizons-ui`, `.gguf` paths
are dynamically mapped to pre-compiled `_htp.bin` context binaries when the QAIRT backend is
active.

---

## 5. Copy-Paste Resume Prompt for Next Agent

```markdown
RESUME INSTRUCTION:
Continue execution on Project NovÆxorpus living canon compilation.
1. Reference MASTER_COMPILATION_EXECUTION_PLAN_AND_HANDOFF.md and
NovAeXorpus_Complete_Mirrors.zip in Secure-Spark-Proof-Folder /
01_MASTER_MIRROR_GLIDE.
2. The 7 canonical repository skeletons (novae-xorpus, novus-aexenti, novaexopia, aesop-xi,
horizons-ui, novus-aesc, novus-aeyre) are staged.
3. Execute Phase 1 (Ingestion & Normalization) on the raw files in 02_MY_ORIGINALS:
   - Convert raw inputs to clean Markdown with YAML frontmatter.
   - Extract procedural heuristics to skills/ and executable scripts to tools/.
   - Enforce the Non-1:1 Condensation Law (preserve 100% build context, eliminate


conversational fat).
4. Run corpus-verify (tools/check.py) per Hard Rule 5 for independent RLVR validation before
committing.
5. Populate the 18-branch Living Wiki in novae-xorpus/02_wiki_md/ and index in manifest.jsonl.
Strict Invariant: The Red Auditor lives exclusively in ~/.red/ and must never appear in repository
manifests or trees.
```
