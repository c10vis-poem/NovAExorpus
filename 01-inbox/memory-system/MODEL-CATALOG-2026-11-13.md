# Model catalog: Documents/_File-Driven-Agent-Operating-Environment/Inventory (113 GB), 2026-11-13 05:5x
Names, formats, chips and sizes from a file listing only; weights not opened. Run status from BUILD-ORDER-1.md.
Chip key: 8 Elite (SM8750, this phone, HTP v79) | X Elite / X2 Elite (laptop chips) | QCS8275 (IoT chip).

## Embeddings (retrieval, vector map, Layer 5)
| Model | Format / chip | Size | Status |
|---|---|---|---|
| EmbeddingGemma 2 270M text | LiteRT-LM, SM8750 | 0.17 GB | runs on HTP, 15.5 ms warm, dim 768 |
| EmbeddingGemma 2 440M text+vision | LiteRT-LM, SM8750 (2 copies, same size) | 0.42 GB x2 | runs on HTP |
| EmbeddingGemma 2 740M multimodal (text, vision, speech) | LiteRT-LM, SM8750 | 0.51 GB | runs; audio CPU/GPU only |

## Router / small LLMs (Layer 0)
| Model | Format | Size | Status |
|---|---|---|---|
| Qwen 3.5 0.8B (+ mmproj F16 0.19 GB) | GGUF Q4_0 | 0.47 GB | runs on HTP0 via GenieX, 39 tok/s; not served |
| Qwen 3.5 2B (+ mmproj 0.62 GB) | GGUF Q4_0 (2 copies) | 1.13 GB x2 | not run |
| Qwen3 1.7B | QAIRT w4a16, X Elite only | 1.43 GB | wrong chip for the phone |
| SmolLM2 1.7B instruct | QAIRT w4a16, 8 Elite + X2 Elite | 0.94 GB each | not run |
| Granite 4.0 H micro | GGUF Q4_0 (2 copies) | 1.73 GB x2 | not run |
| LFM3 1.7B (Liquid) | GGUF Q4_0 QAD | 0.98 GB | not run |

## Executors (mid/large LLMs)
| Model | Format | Size | Status |
|---|---|---|---|
| Qwen 3.5 4B (+ mmproj 0.63 GB) | GGUF Q4_0 | 2.41 GB | runs on GPU, 11.6 tok/s |
| Qwen 3.5 9B | GGUF Q4_0 (2 copies: Qwen3.5-9B 5.01 GB, Qwen_Qwen3.5-9B 5.35 GB) | ~5 GB | runs on GPU, 4.8 tok/s, RAM 14.6 GB peak |
| Gemma 4 E2B it | GGUF q4_0 3.12 GB; LiteRT-LM for QCS8275 2.54 GB (not this phone's chip) | | not started |
| Gemma 4 E4B it (+ mmproj 0.92 GB) | GGUF q4_0 4.80 GB; IQ4_NL 4.50 GB | | not started |
| Sakura Gemma4 E4B DualMode | GGUF Q5_K_M | 5.38 GB | not run |
| Gemma 4 12B it QAT | GGUF q4_0 | 6.50 GB | not run (RAM) |

## Vision-language
| Model | Format / chip | Size | Status |
|---|---|---|---|
| InternVL 3.5 2B | QAIRT w4a16 installed for 8 Elite and X Elite; zips for 8 Elite, X Elite, X2 Elite (x2 each: root and qairt/) | 2.2 GB per zip | 4B ran 2026-10-02 |
| InternVL 3.5 4B | QAIRT w4a16 installed for 8 Elite; zips 8 Elite, X Elite | 3.47 GB per zip | ran 2026-10-02 |
| InternVL 3.5 8B (+ mmproj 0.63 GB) | GGUF Q4_0 | 4.46 GB | not run |
| SmolVLM2 2.2B (+ mmproj 0.55 GB) | GGUF Q8_0 | 1.80 GB | not run |
| LFM3-VL 2B (Liquid) | GGUF Q4_0 QAD | 0.98 GB | not run |

## Omni / voice LLMs
| Model | Format | Size | Status |
|---|---|---|---|
| LFM3 Omni 2B RP (Liquid) | GGUF i1-Q4_0 | 0.98 GB | not run |
| d1 Omni 2B (+ mmproj 0.30 GB) | GGUF Q8_0 | 1.72 GB | not run |

## Speech to text
| Model | Format / chip | Size |
|---|---|---|
| Whisper large v3 turbo | QNN ONNX w8a16 8 Elite (installed 0.92 GB + zip 0.77 GB); QNN context float 8 Elite and X Elite (1.88 GB each) | |
| Whisper medium | QNN ONNX float, 8 Elite | 1.41 GB |
| Distil-Whisper | ONNX, QNN DLC, TFLite (float) | 0.36-0.45 GB |
| Parakeet TDT | QNN DLC mixed | 2.07 GB |
| Zipformer | QNN ONNX float 8 Elite + X2 Elite, mixed 8 Elite | 0.07-0.12 GB |
| DeepSpeech2 | TFLite float (2 copies) | 0.30 GB |

## Text to speech
| Model | Format / chip | Size |
|---|---|---|
| MeloTTS en | Voice AI, 8 Elite + X Elite | 0.24 GB each |
| Piper TTS en | Voice AI, 8 Elite (2 copies) + 8 Elite Gen5 | 0.06 GB each |

## Runtimes and tools
GenieX CLI (`geniex-cli.exe`, Windows, 68 MB); `runtimes/local-ai-v4.10.0-linux-arm64`; VoiceAI ASR 2.7.1.0 release
note; Node 26.10.0 tarballs (arm64, ppc64le, x64); `geniex-chat` APK; `horizons.apk`.
Vendor docs (13): GenieX CLI install, QPM3, AI Hub fraQtl model cards (Gemma 4 E2B, LFM2 1.2B, Qwen 3.5 4B NPU),
EmbeddingGemma 2 740M card, llama serve notes.

## Plugins and assets (zips, small): not models
_plugins: 16minds, Agent Protocols, Agent Smith, BigQuery, Learn Wiki, Project Memory, Scaffold, Shorty, Snowflake,
agent-architecture-designer, claude-memory, maddog, thinking-partner, wiki-wonka, llm-wiki compiler, MCP Kotlin SDK.
_assets: Memory Bank 0.1.0, jevmem 0.7.6, supabase 0.1.17, supabase-expert, Cache Guard, Forge, signal-hunter,
skill-creator, Agent os, Argon evals, Third party evals, Rev.Eng.ify, Target, CloviX-AEyre & Œræcle Fast-Track (2),
GitHub forks (Mobile_Harness, procedural skills and MCP tool registry, Open interpreter), cromite, google_ag.

## Duplicates seen by name (same size): owner decides
EmbeddingGemma 440M (2), Qwen 3.5 2B (2), Granite (2), InternVL 2B zips (root + qairt/, per chip), Qwen 3.5 9B (2,
different sizes = different builds), Piper 8 Elite (2), DeepSpeech2 (2), CloviX fast-track zip (2).
