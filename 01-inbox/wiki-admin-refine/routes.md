---
status: staged
source: wiki-admin session 3c1dfa47, contract A2 task B
date: 2026-11-11
---
# Route inventory (no model was called)

Probes: `command -v` for 18 CLI names; `find` for model files (home, Download, Documents, depth 5) and NPU folders
(home, depth 4); `ls` of `~/models-npu`, `~/npu-work`, `~/tools/geniex-serve`, `~/.gemini/antigravity-cli`; Read of
`geniex.json`, `eg2_server.py` (lines 1-40), `~/.gemini/antigravity-cli/settings.json`. No key value was opened.

## CLIs found
| CLI | Path | Notes |
|---|---|---|
| `agy` (Antigravity CLI) | `~/.local/bin/agy` (205 MB, 10 Nov 2026) | logged in: `~/.gemini/antigravity-cli/antigravity-oauth-token` exists (not opened); one account seen; settings.json has a `permissions.allow` list and trusted workspaces `~`, `~/temp-crane`, `~/repos/NvAEx-Recaps` |
| `claude` | `~/.local/bin/claude` | this session's account; the second Claude Pro account: not checked |
| `pplx` | `~/.local/bin/pplx` | web search (cli-tools skill); key presence not checked |
| `hf`, `gh`, `notebooklm`, `rclone` | `$PREFIX/bin/` | |
| `gcloud` | `~/google-cloud-sdk/bin/gcloud` | |
| `llama-server` | `~/bin/llama-server` | llama.cpp |
| `nvaex-secret` | `~/bin/nvaex-secret` | key store; key names not listed (no command for it in this contract) |
| not found | `gemini` (Gemini CLI), `antigravity`, `openrouter`, `llama-cli`, `geniex`, `litert_lm_main`, `jev`, `typesafe` | GenieX CLI is a folder: `~/tools/geniex-cli-v0.10.0/geniex-cli-linux-arm64-v0.10.0` |

## Local models found
| Model | File | Runtime on disk |
|---|---|---|
| **EmbeddingGemma 2, all three LiteRT bundles, Snapdragon 8 Elite (SM8750) builds** | `~/models-npu/embeddinggemma-2/litert/embeddinggemma-2-{text-270m,text-vision-440m,740m}_Qualcomm_SM8750.litertlm` | `~/npu-work/eg2-server/eg2_server.py`: OpenAI-style `/v1/embeddings` on port 8085; models `eg2-text` (NPU), `eg2-vision` (text+vision NPU), `eg2-mm` (audio on CPU); Matryoshka 768/512/256/128; litert-lm 0.18.1 venv `~/npu-work/1A/venv18`; HTP compile caches exist for the 740m (8 Nov 2026) |
| EmbeddingGemma 2, generic LiteRT | `~/models-npu/embeddinggemma-2/litert-generic/` (text-270m, 740m) | CPU/GPU fallback |
| EmbeddingGemma 2, GGUF | `~/models-npu/embeddinggemma-2/gguf/embeddinggemma-2-Q8_0.gguf`; `~/downloads/embeddinggemma-2-UD-Q4_K_XL.gguf` | llama.cpp |
| EmbeddingGemma 300M (v1) | `~/downloads/embeddinggemma-300m-int8.tflite` + tokenizer | older; guide `~/EMBEDDING_GEMMA_INT8_USER_GUIDE.md` |
| **Qwen 3.5 0.8B** | `~/models-npu/geniex-cache/models/local/qwen3.5-0.8b/Qwen3.5-0.8B-Q4_0.gguf` (507 MB), no mmproj | GenieX, plugin `llama_cpp` (geniex.json); `~/tools/geniex-bench*`, `geniex-cli-v0.10.0`, `geniex-serve/server.py` |
| Gemma 4 12B | `~/downloads/gemma-4-12B-it-qat-UD-Q4_K_XL.gguf`; `~/gemma-12b/mmproj-gemma-4-12b-it-qat-q4_0.gguf` | llama-server |
| Gemma 4 E2B | `~/gemma-e2b/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf` | llama-server |
| not used | `~/models-npu/qwen3_vl_4b_instruct-geniex_qairt-...` | owner rule: Qwen 3.5 only (memory `feedback_no_qwen3_vl.md`) |

Owner said (14:44) EmbeddingGemma 2 was not fetched yet: the three SM8750 bundles and a server for them are already
on disk (folders dated 8 Nov 2026). Owner to confirm these are the ones he meant.

## Routes and what part 2 tests (one round trip each)
| Route | Invoke | Account / cost | Test in part 2 |
|---|---|---|---|
| Gemini 3.8 Flash via AGY (bulk ingestion) | `agy -p "..." --model <slug from agy models> --output-format json` | account credits | `agy models` lists slugs; one short prompt |
| Gemini 4 Argon / Carbon via AGY (large context, hard reasoning) | same, `--model` argon/carbon slug | Pro gets Argon; Ultra gets Carbon (research.md) | which account is logged in, which slugs it offers |
| AGY `/swarm` (parallel workers) | interactive `/swarm` | credits | later, after the router |
| OpenRouter (frontier: `anthropic/claude-fable-5.2`, `google/gemini-4-carbon`) | HTTPS API (no CLI on disk) | OpenRouter credits | owner names the key; one call |
| Second Claude Pro account | a second `claude` login (config dir) | Pro plan | owner says where it runs |
| JEV (TypeSafe) | already answers every prompt here (hook lines `via typesafe jev-1.14.0`) | TypeSafe | none needed; route triage questions to it |
| EmbeddingGemma 2 on NPU | `eg2_server.py --port 8085`, POST `/v1/embeddings` | on device | start, `/health`, embed one sentence with `eg2-text` |
| Qwen 3.5 0.8B on NPU | GenieX (`geniex-bench` / `geniex-serve`) | on device | one short classify prompt; confirm NPU placement |
| Gemma 4 12B / E2B | `llama-server -m <gguf>` | on device | one prompt each |
| Web search | `pplx`, Bing via claw_scrape, WebFetch | Perplexity key / free | DuckDuckGo and Google blocked bots this session |

## Not checked
Key names in `nvaex-secret`; which Google account(s) `agy` holds; the second Claude account; whether `eg2_server.py`
still starts; GenieX NPU placement for Qwen; `pplx` key.
