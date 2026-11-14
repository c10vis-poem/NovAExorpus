---
status: staged
source: wiki-admin session 3c1dfa47, contract C
date: 2026-11-11
---
# Wiki admin playbook: what you can run on the phone today

Every command below comes from a file read on 2026-11-11 (source in brackets). None was run in this session: first
run = first test. Report what breaks and it goes into the spec's failure mode.

## 1. Embeddings on the NPU (EmbeddingGemma 2, all three sizes)
[`~/npu-work/eg2-server/eg2_server.py` lines 1-31]
```sh
cd ~/npu-work/eg2-server
. ~/npu-work/npu-env.sh
~/npu-work/1A/venv18/bin/python eg2_server.py --port 8085
```
In a second Termux tab:
```sh
curl -s localhost:8085/health
curl -s localhost:8085/v1/models
curl -s localhost:8085/v1/embeddings -H 'Content-Type: application/json' \
  -d '{"model":"eg2-text","input":"wiki admin test","dimensions":256,"task":"document"}'
```
| Model id | Bundle | Runs on |
|---|---|---|
| `eg2-text` | text 270M (188 MB) | NPU |
| `eg2-vision` | text + images 440M (447 MB) | NPU |
| `eg2-mm` | text + images + audio 740M (544 MB) | NPU, audio on CPU |
`dimensions`: 768, 512, 256 or 128. `task`: `query` for searches, `document` for files. An image goes in as
`{"image": "/path.png"}` inside a list. The first call per model compiles for the NPU and is slow; later calls are warm.

## 2. Gemini on your account credits (Antigravity CLI, `agy`)
[antigravity.google/docs/cli/headless, read 2026-11-11; `agy` is at `~/.local/bin/agy`, logged in]
```sh
agy models                                   # the model slugs your account has
agy -p "Summarize this in 5 bullets: $(cat file.md)" --model gemini-3.8-flash-medium --output-format json
agy -p "..." --model <argon or carbon slug from agy models> --effort high
agy -p "..." --output-format json --json-schema '{"type":"object","properties":{"title":{"type":"string"}}}'
```
- Credits left: `/credits` inside `agy`; quotas: `/usage`.
- Tools that need approval are refused quietly in `-p` mode unless allowed in `~/.gemini/antigravity-cli/settings.json`.
- An unknown `--model` exits with an error; it never falls back.
- Parallel workers: `/swarm` inside an interactive `agy` session.

## 3. Local LLMs (Qwen 3.5, Gemma 4) on GenieX
[`HTP/NPU-RUNTIME-PATHS.md` lines 9-13, 46; `~/models-npu/geniex-cache/models/local/qwen3.5-0.8b/geniex.json`]
- GenieX serves GGUF over an OpenAI-style API at `http://127.0.0.1:18181/v1` (`geniex serve`). CLI folder:
  `~/tools/geniex-cli-v0.10.0/geniex-cli-linux-arm64-v0.10.0/`; bench tools `~/tools/geniex-bench*`. Exact `serve` flags were
  not read this session: run the CLI with `--help` first.
- Once it serves:
```sh
curl -s 127.0.0.1:18181/v1/chat/completions -H 'Content-Type: application/json' \
  -d '{"model":"qwen3.5-0.8b","messages":[{"role":"user","content":"Label this file: private, vendor-doc, plan, or code. File: BUILD-ORDER-1.md"}]}'
```

## 4. Which model for which job
| Job | Use | File |
|---|---|---|
| Embeddings / search index | `eg2-text` (NPU) | `~/models-npu/embeddinggemma-2/litert/` |
| Image search, screenshots | `eg2-vision` | same |
| Quick labels, triage | Qwen 3.5 0.8B (507 MB) or JEV | `Inventory/_models/gguf/Qwen3.5-0.8B-Q4_0.gguf` (+ mmproj) |
| OCR of scans | Qwen 3.5 2B/4B + mmproj, or Gemini Flash via `agy` | `Inventory/_models/gguf/` |
| Bulk reading and drafting | Gemini 3.8 Flash via `agy` | account credits |
| Hard synthesis | Gemini 4 Argon (Pro) / Carbon (Ultra) via `agy` | account credits |
| Local drafting offline | Qwen 3.5 9B Q4_0 or Gemma 4 12B | `Inventory/_models/gguf/` |
| Voice notes to text | Whisper large-v3-turbo (QAIRT, unpacked) | `Inventory/_models/installed/whisper-large-v3-turbo-8elite/` |
| Frontier second opinion | OpenRouter `anthropic/claude-fable-5.2`, `google/gemini-4-carbon` | OpenRouter key |
Not used: anything Qwen3 / Qwen3-VL (your rule: Qwen 3.5 only).
`Inventory` = `/storage/emulated/0/Documents/_File-Driven-Agent-Operating-Environment/Inventory/_models` (79 GB).

## 5. Where your material is
| What | Where |
|---|---|
| Wiki admin compilation (24 files) | `Documents/_File-Driven-Agent-Operating-Environment/Greedy-crane/` |
| Build orders, targets, plan docs | same folder: `Plan-Order-1,2&3/`, `_Target-planning_objectives/`, `plan-docs/`, `More-Argon-Builds/` |
| Jev docs (178) | same folder: `_Jev/` |
| Vendor docs | vault `Vendor-Registries/` (10 vendors), `global-documentation-vault/`, `QAIRT-QNN/` |
| Old vault copies (17 GB) | `Documents/_Merovingians_Keep/Zip/`, `.../NovAExorpus-nested-mirror/` |

## 6. The session's reports (staged, for your review)
- `01-inbox/wiki-admin-refine/research.md`: EmbeddingGemma 2, Argon/Carbon, AGY, OpenRouter, Qwen 3.5, JEV.
- `01-inbox/wiki-admin-refine/audit.md`: 26 cleanup items for greedy-crane, approve by number.
- `01-inbox/wiki-admin-refine/routes.md`: CLIs and local models found.
- `01-inbox/corpus-survey/inventory.md`: sizes and counts of everything.
- `01-inbox/corpus-survey/vendors-and-models.md`: every model, its runtime and job.
- `01-inbox/corpus-survey/part2-plan.md`: next steps and 8 questions for you.
