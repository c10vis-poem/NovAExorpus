---
status: staged
source: wiki-admin session 3c1dfa47, contract B task V
date: 2026-11-11
---
# Vendors and models (2026-11-11)

Read: vault `AGENTS.md`, `SOURCE-RETRIEVAL-MAP.md`, `HTP/NPU-RUNTIME-PATHS.md`, the first lines of
`Vendor-Registries/README (8).md` and `README (6).md`; file lists of every Vendor-Registries folder, HTP, Assets-Index and
`Inventory/_models`. Vendor docs themselves were not read (part 2). Phone: Razr Ultra 2025, Snapdragon 8 Elite (SM8750),
Hexagon HTP v79 (`HTP/NPU-RUNTIME-PATHS.md:4`; AGENTS.md:93). Owner rule: Qwen 3.5 only.

## Runtimes on this phone
| Runtime | Loads | Where | Source |
|---|---|---|---|
| GenieX (`geniex serve`, OpenAI-style `127.0.0.1:18181/v1`) | any GGUF on its `llama_cpp` runtime (GGML Hexagon); AI Hub bundles on its `qairt` runtime (NPU only) | `~/tools/geniex-*` v0.7.1-0.10.0, `~/repos/GenieX` | NPU-RUNTIME-PATHS.md:9-13, 46-47; AGENTS.md:93 |
| LiteRT-LM 0.18.1 (NPU dispatch) | `.litertlm` bundles | `~/npu-work/1A/venv18`, `~/npu-work/eg2-server/eg2_server.py` (port 8085) | eg2_server.py:4-9 |
| llama.cpp / llama-server | GGUF on CPU/GPU | `~/bin/llama-server`, `~/llama.cpp`, `~/downloads/llama.cpp` | |
| ORT + QNN EP (`ort_engine`) | QAI Hub `qnn_context_binary` (fallback only) | | NPU-RUNTIME-PATHS.md:21-37 |
| LocalAI v4.10.0 linux-arm64 | various | `Inventory/_models/runtimes/` (150 M) | |
| not built | TFLite, DLC (SNPE), PTE (ExecuTorch) daemons | | NPU-RUNTIME-PATHS.md:49-51 |

## Models on disk (Inventory = `/storage/emulated/0/Documents/_File-Driven-Agent-Operating-Environment/Inventory/_models`)
| Model | File(s), size | Runtime | Route it could serve |
|---|---|---|---|
| **EmbeddingGemma 2** text 270M / text-vision 440M / 740M (SM8750) | `~/models-npu/embeddinggemma-2/litert/` 188 / 447 / 544 MB; generic + Q8_0 + UD-Q4_K_XL gguf | LiteRT-LM NPU (server written) | **embeddings / index** (text now, vision later) |
| EmbeddingGemma 300M int8 | `~/downloads/embeddinggemma-300m-int8.tflite` | TFLite (daemon not built) | superseded by EG2 |
| **Qwen 3.5 0.8B** Q4_0 + mmproj F16 | Inventory gguf 507 MB + 205 MB; GenieX cache copy (no mmproj) | GenieX llama_cpp | **triage / classify**, small OCR with mmproj |
| Qwen 3.5 2B Q4_0 + mmproj | 1.21 G + 668 M | GenieX | extraction, OCR |
| Qwen 3.5 4B Q4_0 + mmproj | 2.58 G + 672 M | GenieX | multimodal Qwen (owner: "3.5 4B which is multimodal") |
| Qwen 3.5 9B Q4_0 | two builds: 5.38 G and 5.74 G (`Qwen_` prefix = the one NPU-RUNTIME-PATHS.md:10 names) | GenieX (primary NPU LLM) | local drafting, W5H |
| Gemma 4 12B it QAT | Inventory q4_0 6.98 G; `~/downloads` UD-Q4_K_XL; mmproj in `~/gemma-12b` | GenieX / llama-server | local drafting |
| Gemma 4 E4B | IQ4_NL 4.84 G, q4_0 5.15 G, q4_k_m 5.34 G, mmproj 992 M | GenieX / llama-server | |
| Gemma 4 E2B | `~/gemma-e2b/` UD-Q4_K_XL (2.5 G folder) | llama-server | light local |
| InternVL 3.5 8B Q4_0 + mmproj | 4.79 G + 678 M | GenieX | vision / OCR |
| InternVL 3.5 2B and 4B, QAIRT W4A16 | zips per chip (8 Elite for Galaxy, X Elite, X2 Elite) 2.4-3.7 G; unpacked in `installed/` | GenieX qairt (NPU) | vision / OCR on NPU |
| SmolVLM2 2.2B Q8_0 + mmproj | 1.93 G + 593 M | GenieX | vision |
| SmolLM2 1.7B it, QAIRT | 1.0 G per chip | GenieX qairt | |
| Granite 4.0 H Micro Q4_0 | 1.86 G | GenieX | |
| Qwen3 1.7B QAIRT (X Elite) | 1.54 G | | **not used** (Qwen 3.5 only) |
| qwen3_vl_4b GenieX bundle | `~/models-npu/qwen3_vl_4b_...` | | **not used** |
| Whisper large-v3-turbo W8A16, medium, small; distil-whisper (ONNX / QNN DLC / TFLite); zipformer; deepspeech2 | `speech/`, `stt/`, `installed/whisper-large-v3-turbo-8elite` (unpacked) | QAIRT / ONNX | **voice transcripts into the corpus** (STT) |
| MeloTTS en, Piper TTS en | `speech/` 260 M, 69 M | QAIRT | TTS (not wiki work) |

"8 Elite for Galaxy" bundles target the Galaxy variant of the same SM8750; whether they run on this Razr: part 2 test.

## Vendor-Registries (vault, 650 M, 73 files)
| Vendor folder | Files | What it holds | Route |
|---|---|---|---|
| `google-gemma-litert/` | 17, 614 M | LiteRT / LiteRT-LM / AI Edge pages (.mht), Gemma 4 overviews (.md), Gemini fine-tuning page, `model.safetensors` 561 M (unnamed: which model is unknown), `google-cloud-cli-linux-arm.tar.gz` 61 M | embeddings, NPU |
| `qwen/` | 10, 34 M | Qwen 3.5 paper (PDF 35 M + 2 MD), 0.8B / 2B / unsloth-2B cards, two 9B Q4_0 compile docs, one Qwen3 search export (not used) | triage, drafting |
| `qualcomm-ai-hub/` | 20, 2.0 M | model pages (SmolLM2, Qwen3.5-2B, Intern3.5-VL-4B, Llama-3.2-3B SSD, Granite .mht 1.9 M, Qwen3-1.7B), GenieX Android docs + chat app README, 8 speech model pages, VoiceAI ASR release note | NPU runtime |
| `internvl/` | 1, 196 K | InternVL3.5 paper (2508.18265v2) | OCR / vision |
| `huggingface-smolvlm/` | 2, 20 K | SmolVLM2 2.2B cards | vision |
| `agents-gateways/` | 2, 32 K | agent gateway overview; OmniRoute wiki page (OmniRoute is dropped, AGENTS.md:92) | reference |
| `opencode/`, `piper/` | 1 README each | | |
| `guides/` | 2 | `LOCAL-AI-GUIDE.md`, `operator_guide.md` | |
| `skills-references/` | 1 | mattpocock `ask-matt` SKILL | |
| root | 2 READMEs | `README (8).md` = Netresearch skills marketplace; `README (6).md` = Prime Agent (FLAGGED by quarantine hook) | |
None of the vendor folders has the standalone vendor document + manifest.jsonl the vault rule asks for (AGENTS rule
2026-11-10: "a standalone vendor document sits next to its raw files there, with its manifest").

## Other vendor-doc stores
- `global-documentation-vault/` (74 M): google-dev-docs 26 M, qairt-docs 26 M, unsloth-docs 16 M, qwen-models 5.5 M,
  llama-docs 408 K, research 1.2 M, reverse-engneering 472 K, fragmented-qat, reference, readme-notes.
- `QAIRT-QNN/` (7.1 G, 2,258 entries): QAIRT SDK dump with model JSONs; `~/npu-work/qc.log` lists 57 QAIRT doc pages by size.
- `HTP/` (5): `NPU-RUNTIME-PATHS.md`, `HTP-Memory-Architecture-and-runtime-splitting.md`, partitioner note, runtime server.
- `_File-Driven-.../_Jev/` (178): TypeSafe Jev docs, SDKs, cookbooks.
- `Assets-Index/` (5): only POINTER.md for ecc, mem0, omniroute, prime-agent, terrestrial-brain (3 of them are dropped
  tools, AGENTS.md:92).
