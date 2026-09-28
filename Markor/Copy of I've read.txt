I've read through the full architecture document and your inline annotations carefully. Before I give you detailed recommendations, let me search for the latest information on a few key items — ECC, current model availability for your hardware, and JSONL tooling — so my advice is grounded in what's actually available right now.

I've read through both architecture documents (v1 and v2.2) and your inline annotations. I now have a clear picture of where things stand vs. where they need to go, plus current state of all the tools mentioned. Let me give you a comprehensive breakdown organized by your actual questions.

---

## 1. Inference Models — What to Download First

Your dual-model architecture (Executor 0.8B + Query 9B) is well-conceived, and the hardware targets are now confirmed by real benchmarks. Here's the download order I'd recommend:

### Tier 1: Download Immediately (Executor Core)

**Qwen 3.5 0.8B GGUF Q4_0** — This is your executor model, and Qualcomm has already pre-exported it specifically for Snapdragon 8 Elite:

- **Source**: `huggingface.co/qualcomm/Qwen3.5-0.8B` (pre-exported for Qualcomm devices) or `huggingface.co/TheStageAI/Qwen3.5-0.8B-GGUF` (general GGUF)
- **Size**: ~418 MB (TheStageAI S tier) to ~800 MB (Q8)
- **Benchmark on Snapdragon 8 Elite**: 50–73 tokens/sec at 512 context, 35–50 tokens/sec at 4096 context
- **Why first**: It's tiny, it loads fast, it gives you immediate proof-of-life that your bare-metal pathway (`Llama Server → QAIRT ModelPath → GGML → Kotlin Kernel`) actually works end-to-end on your phone. This is your "does the NPU even talk to me?" test.

```bash
# Termux
huggingface-cli download qualcomm/Qwen3.5-0.8B --include "*.gguf" --local-dir ~/models/qwen-0.8b
# Or from TheStageAI for clean GGUF
huggingface-cli download TheStageAI/Qwen3.5-0.8B-GGUF --include "Qwen3.5-0.8B-S-TS-Q4_K_S.gguf" --local-dir ~/models/qwen-0.8b
```

### Tier 2: Download Second (Query Core — Jetson Target)

**Qwen 3.5 9B GGUF Q4_0 or Q4_K_M** — Your query/metaprompt compiler. This runs on the Jetson (8GB RAM, CUDA), not the phone.

- **Source**: `huggingface.co/bartowski/Qwen_Qwen3.5-9B-GGUF`
- **Size**: Q4_0 = 5.45 GB | Q4_K_M = 5.89 GB (both fit in 8GB with room for KV cache)
- **Architecture note**: Hybrid Gated DeltaNet + Attention — needs a recent llama.cpp build (b8192+ for quantization, but runtime needs to support the new operators)
- **Why second**: You need the executor working before you wire up the query model. The query model synthesizes meta-prompts that the executor then acts on. Testing the executor alone validates the simpler half of the asymmetric loop.

```bash
# On Jetson
huggingface-cli download bartowski/Qwen_Qwen3.5-9B-GGUF --include "Qwen3.5-9B-Q4_K_M.gguf" --local-dir ~/models/qwen-9b
```

### Tier 3: Download When Ready (Voice Stack)

| Component | Source | Size | Purpose |
|---|---|---|---|
| **Moonshine ONNX (STT)** | `huggingface.co/ModelSupports/Moonshine` | ~250 MB | Speech-to-text on-device |
| **Kokoro 82M (TTS)** | `huggingface.co/hexgrad/Kokoro-82M` | ~82 MB | Text-to-speech |
| **Silero VAD** | `github.com/snakers4/silero-vad` | ~2 MB | Voice activity detection |

### Download Priority Rationale

```
0.8B Executor (phone, NPU)  ← Validates bare-metal pathway
     ↓
9B Query (Jetson, CUDA)     ← Validates asymmetric context alignment
     ↓
Voice stack (phone)          ← Validates full concierge loop (voice → STT → prompt → inference → TTS)
     ↓
Frontier fallback (cloud)    ← Already have via Claude Code / OpenRouter
```

---

## 2. Setting Up Claude Code with ECC — The Proper Way

ECC (by affaan-m) is now at v1.10+ with a mature plugin system. Here's the correct setup path as of now:

### Install ECC as a Claude Code Plugin

```text
# Inside a Claude Code session:
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

That's it for the base install. **Do not also run a manual install** — that's explicitly warned against in ECC's docs (you'd end up with duplicate skills).

### Choose Your Install Profile

ECC uses a manifest-driven system with three profiles:

| Profile | What You Get | Good For |
|---|---|---|
| **Minimal** | Core rules + runtime hooks only | Low-overhead, just guardrails |
| **Core** | Standard agents + commands + hooks | Daily development work |
| **Full** | Everything — all domain skills, orchestration, research APIs | Your use case — you want the full ecosystem |

For your project, go **Full**. You need the orchestration agents, research skills, and the full skill catalog (286 skills) because you're building a multi-agent mesh, not just writing a web app.

### Configure Hook Profile

```bash
# ECC supports runtime hook profiles
ECC_HOOK_PROFILE=strict   # Most enforcement, best for your audit-heavy setup
# Options: minimal | standard | strict
```

For your Red Agent Auditor architecture, `strict` makes sense — you want maximum enforcement of the plan→test→implement→review→verify→remember loop.

### The Key Insight About ECC + Your Architecture

ECC's flow is literally:

```
plan → test → implement → review → verify → remember → improve
```

This maps **directly** to your Priority 3 (Tool Harness Ingestion) and Priority 4 (Emulated Runtime Loop Validation). ECC is not just a tool you use — it's the **execution engine** that your grill session will define how to use. The grill session should output a manifest that tells ECC which skills map to which agents.

---

## 3. Installing All the Harnesses — Current State & Integration Strategy

### Pocock Skills (21 composable skills)

```bash
# As Claude Code plugin (managed, auto-updates):
npx skills@latest add mattpocock/skills
# Then run in Claude Code:
/setup-matt-pocock-skills
```

Key skills for your project:
- `grill-with-docs` — This is literally your Phase 1 session
- `to-spec` — Converts grill output to formal spec
- `to-tickets` — Breaks spec into implementable tickets
- `implement` — Builds from tickets with TDD
- `code-review` — Dual-axis review (standards + spec)
- `domain-modeling` — Builds shared vocabulary (your CONTEXT.md)
- `wayfinder` — Plans multi-session work as decision tickets

**Critical**: `grill-with-docs` is different from plain `grill-me` — it also builds the project domain model and updates `CONTEXT.md` and ADRs inline. This is exactly what you need for the grill session.

### GSD v2 (Get Shit Done — now a CLI)

GSD v2 is no longer a prompt framework — it's a **standalone CLI built on the Pi SDK** that has direct programmatic control over agent sessions:

```bash
npm install -g gsd-pi@latest
```

What GSD v2 gives you that GSD v1 didn't:
- Fresh context window per task (programmatic, not "hope the LLM does it")
- Git branch-per-slice with squash merge
- Cost tracking per task
- Crash recovery with lock files
- Auto-advance through milestones

### ECC + Pocock + GSD — How They Stack

This is where the grill session needs to make decisions. These three overlap significantly. Here's the honest overlap map:

```
ECC:          plan → test → implement → review → verify → remember
Pocock:       grill → spec → tickets → implement(TDD) → review → domain-modeling
GSD v2:       discuss → plan → execute(fresh context) → verify → reassess
```

**My recommendation for your grill session**: Use **Pocock's `grill-with-docs`** as the entry point for Phase 1 planning, then use **GSD v2** as the execution engine for the actual build phases (it controls context windows programmatically), with **ECC** providing the skills/rules/hooks/agents layer that both Pocock and GSD sit on top of.

### Other Tools Quick Reference

| Tool | Install | Role in Your Stack |
|---|---|---|
| **Honey for Devs** | `npx honey add` | Developer-focused skill harness; overlaps with ECC but has unique workflow skills |
| **Prime Agent** | `npx claude-prime install` | Installs CLAUDE.md + skills/ + rules/ + MCP config; lightweight alternative to ECC if you want minimal overhead |
| **mem0** | `pip install mem0ai` | Episodic memory — your hot-plate context cache for the executor model |
| **Omni Route / LocalAI** | `pip install localai` or docker | Modality routing + OpenAI/Anthropic format translation |
| **Code Review Graph** | (Check repo) | Visual code review dependency mapping |

---

## 4. JSONL Manifest Creation — Tooling

This is where I want to be very specific because it's the critical pipeline for your 93 files:

### Primary Tool: Docling (IBM)

```bash
pip install docling
# For your use case (PDFs with tables, diagrams, code blocks):
pip install "docling[vlm]"  # GraniteDocling for vision-language model pipeline
```

Docling gives you:
- **Lossless JSON export**: `result.document.export_to_json()` gives you the complete node hierarchy, cell matrices, font attributes
- **Structured Markdown**: `result.document.export_to_markdown()` for your Obsidian vault
- **Air-gapped execution**: Runs 100% locally — critical for your Red Agent Auditor's nope data bank
- **MCP server**: `docling-serve` lets Claude Code call Docling directly as a tool

```python
from docling.document_converter import DocumentConverter

# Convert a single doc
converter = DocumentConverter()
result = converter.convert("your-doc.pdf")

# Export to JSON (not JSONL yet — you need to post-process)
doc_json = result.document.export_to_dict()
```

### JSONL vs JSON — The Conversion Step

Docling exports lossless JSON, not JSONL. To convert to the JSONL marker format from your architecture doc, you need a post-processing step. Here's a starter:

```python
import json
from pathlib import Path
from docling.document_converter import DocumentConverter

converter = DocumentConverter()

def doc_to_jsonl_marker(doc_path, output_path, record_id, category, target_runtime, retrieval_tokens):
    """Convert a document to a JSONL marker line matching your Universal JSONL Marker Schema."""
    result = converter.convert(str(doc_path))
    markdown = result.document.export_to_markdown()
    
    record = {
        "record_id": record_id,
        "document_path": str(doc_path),
        "category": category,
        "target_runtime": target_runtime,
        "metadata": {
            "title": doc_path.stem,
            "description": markdown[:200].replace("\n", " "),
            "primary_tools": [],
            "required_context_keys": []
        },
        "retrieval_tokens": retrieval_tokens,
        "entry_points": {
            "repl_command": f"/skill run {record_id.lower()}",
            "jsonrpc_method": "agent.skills.execute"
        },
        "content_chunk": markdown  # The actual document text
    }
    
    with open(output_path, "a") as f:
        f.write(json.dumps(record) + "\n")

# Batch process your 93 files
docs_dir = Path("~/your-93-files").expanduser()
output = Path("~/file-management-and-skills/universal-index.jsonl")

for pdf in docs_dir.glob("*.pdf"):
    doc_to_jsonl_marker(
        doc_path=pdf,
        output_path=output,
        record_id=f"DOC_{pdf.stem.upper()[:40]}",
        category="TECHNICAL_REFERENCE",
        target_runtime="QUERY_CORE_9B",
        retrieval_tokens=pdf.stem.lower().split("-")[:5]
    )
```

### Alternative: Jina AI Reader (for URL sources)

For the web-sourced documents (Firecrawl/Jina approach from your notes):

```bash
# Jina Reader API — strips web junk, returns clean markdown
curl -s "https://r.jina.ai/https://example.com/docs" | python3 -c "
import sys, json
content = sys.stdin.read()
record = {
    'record_id': 'WEB_DOC_001',
    'content_chunk': content,
    'source_url': 'https://example.com/docs'
}
print(json.dumps(record))
" >> web-index.jsonl
```

### Your JSONL Manifest Tool Stack Summary

```
PDFs/DOCX/PPTX → Docling → lossless JSON → post-process → .jsonl marker lines
Web URLs       → Jina Reader → markdown → post-process → .jsonl marker lines  
Manual notes   → Obsidian .md → script parse → .jsonl marker lines
All combined   → universal-index.jsonl → consumed by OB1 vector store + Vertex AI Discovery Engine
```

---

## 5. Practice Runs — What to Test and in What Order

Your "Step 3" from the v2.2 doc mentions practice runs. Here's a concrete sequence:

### Run 1: NPU Proof-of-Life (Phone Only)

```bash
# Install llama.cpp in Termux
pkg install llama-cpp

# Run the 0.8B model
llama-cli -m ~/models/qwen-0.8b/Qwen3.5-0.8B-S-TS-Q4_K_S.gguf \
  -p "List the files in the current directory" \
  --n-gpu-layers 99 \
  --ctx-size 4096
```

**What you're validating**: Does the Snapdragon NPU actually accelerate inference? Expected: 50+ tokens/sec.

### Run 2: Claude Code + ECC + Pocock Integration (Cloud)

```
# In Claude Code:
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
npx skills@latest add mattpocock/skills
/setup-matt-pocock-skills

# Then test:
/grill-with-docs
```

**What you're validating**: Can all three harness systems coexist without skill conflicts? Does the grill skill actually start?

### Run 3: Docling Pipeline (Termux)

```bash
pip install docling
python3 -c "
from docling.document_converter import DocumentConverter
c = DocumentConverter()
r = c.convert('test-doc.pdf')
print(r.document.export_to_markdown()[:500])
print('---')
print(r.document.export_to_json()[:500])
"
```

**What you're validating**: Can Docling process your actual documentation PDFs in Termux? (Some heavy models may need the `--device cpu` flag on phone.)

### Run 4: Dual-Model Asymmetric Loop (Phone + Jetson)

This is the big one — test whether the executor (0.8B on phone) and query model (9B on Jetson) can actually communicate:

```
Phone (0.8B Executor):
  1. Receives user voice/input
  2. Accesses mem0 + Reasoning Bank
  3. Synthesizes a task prompt
  4. Sends to Jetson (9B Query) via Tailscale mesh

Jetson (9B Query):
  1. Receives task prompt
  2. Queries OB1 vector store + Universal JSONL index
  3. Synthesizes markdown meta-prompt
  4. Returns to phone

Phone:
  1. Displays meta-prompt in Horizons UI
  2. User verifies
  3. Executor acts on verified prompt
```

**What you're validating**: Tailscale connectivity, OB1 Postgres reachability, context routing through Omni Route, and the full asymmetric loop timing.

---

## 6. Key Corrections to Your Architecture Docs

Based on your inline annotations and current tool state, here are the critical updates the grill session needs to address:

<details>
<summary><strong>Click to expand: Architecture corrections summary</strong></summary>

### From v1 → What Changed in v2.2 (and what still needs fixing)

1. **3-APK Architecture** — v2.2 correctly splits into Horizons UI + Shell Daemon + Media Daemon. v1 had this as a single app. ✅ Fixed.

2. **Priority 4 & 5 should run parallel** — You annotated this. v2.2 does say "Parallel with Priority 5" on Priority 4. But the reality is:
   - Priority 4 (3-APK deployment) needs the Kotlin/Java code written first
   - Priority 5 (dual-model inference) needs the bare-metal pathway proven first
   - These CAN run in parallel if you have two agents: one building APKs, one testing inference
   - GSD v2's multi-agent orchestration actually supports this natively

3. **The 4+ additional agents** — v2.2 adds: Home Assistant (cross-agent auditor), Red Agent Auditor, IT Help Desk, Web Ingestion Monitor, NPU Inference Manager. Your annotations confirm this. v1 only had the Red Agent.

4. **Repository expansion** — v2.2's repo map (`horizons-ui-v2.0`, `nova-daemon-shell`, `nova-daemon-media`, `agent-harness-hub`, `localai-omni-route`, `gcp-training-flywheel`) is more accurate than v1's. But your annotations call out that `termux-building-skills` scope needs to expand "far beyond just Termux into all device agent setups."

5. **ECC version** — The v2.2 doc references ECC generically. Current ECC is v1.10+ with manifest-driven install, 68 agents, 286 skills, and a plugin marketplace. The grill session should spec out exactly which ECC agents/skills map to which of your system agents.

6. **JSONL Marker Schema** — v2.2's Universal JSONL Marker Schema is well-formed. The `target_runtime` field should be expanded to include your actual runtimes: `NODE_ALPHA_NPU`, `NODE_BETA_CUDA`, `PRIME_AGENT_RLM`, `HORIZONS_UI`, etc.

7. **GSD v2 vs v1** — v2.2 mentions GSD generically. GSD v2 is now a fundamentally different tool (standalone CLI with Pi SDK, not a prompt framework). The grill session should decide: GSD v2 as execution engine, or ECC's built-in orchestration, or both?

</details>

---

## 7. Recommended Grill Session Prep Checklist

Before you start the actual `grill-with-docs` session, make sure you have:

- [ ] ECC installed as Claude Code plugin (`/plugin install ecc@ecc`, Full profile)
- [ ] Pocock Skills installed (`npx skills@latest add mattpocock/skills`)
- [ ] `/setup-matt-pocock-skills` run in your `file-management-and-skills` repo
- [ ] Qwen 3.5 0.8B GGUF downloaded to phone (`~/models/qwen-0.8b/`)
- [ ] Qwen 3.5 9B GGUF Q4_K_M downloaded to Jetson (`~/models/qwen-9b/`)
- [ ] Docling installed in Termux (`pip install docling`)
- [ ] Your 93 files staged in `~/file-management-and-skills/target-docs-curation/`
- [ ] The v2.2 architecture doc (the second one you pasted) saved as your reference spec
- [ ] Tailscale configured between phone, Jetson, and Rubik Pi
- [ ] Postgres + pgvector installed on Jetson for OB1

The grill session agent should be your "traffic director" — it reads the architecture doc, interrogates the 93 files, and outputs:
1. The definitive repo partition plan
2. Skill-to-agent allocation matrix
3. Data tiering boundaries (hot plate vs. cold vault)
4. The execution roadmap with GSD v2 as the build engine

---

## TL;DR — Do This First

1. **Download**: `huggingface-cli download TheStageAI/Qwen3.5-0.8B-GGUF --include "Qwen3.5-0.8B-S-TS-Q4_K_S.gguf"` — 418 MB, your proof-of-life model
2. **Install ECC**: `/plugin marketplace add https://github.com/affaan-m/ECC` then `/plugin install ecc@ecc` in Claude Code
3. **Install Pocock**: `npx skills@latest add mattpocock/skills` then `/setup-matt-pocock-skills`
4. **Install Docling**: `pip install docling` in Termux — your JSONL pipeline tool
5. **Run NPU test**: `llama-cli -m ~/models/qwen-0.8b/*.gguf -p "Hello" --n-gpu-layers 99` — confirm the NPU talks to you
6. **Then grill**: `/grill-with-docs` in your `file-management-and-skills` repo, feed it the v2.2 architecture doc + your annotations

Want me to go deeper on any of these — particularly the JSONL conversion pipeline, the ECC skill-to-agent mapping, or the dual-model inference loop wiring?