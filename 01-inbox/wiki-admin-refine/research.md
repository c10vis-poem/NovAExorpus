---
status: staged
source: wiki-admin session 3c1dfa47, contract A2 task R
date: 2026-11-11
---
# Research: terms the owner named (2026-11-11)

Every fact below came back from the page named in its row, read 2026-11-11. "Not stated" means the page read did not say.

## EmbeddingGemma 2 (the owner's "embedding Gemma2")
Base model: `google/embeddinggemma-2`, 744.4M parameters, Apache-2.0, multimodal (text, vision, audio, video), updated
28 Oct 2026 (hf.co/google/embeddinggemma-2, Hugging Face Hub details).

**The three LiteRT bundles** (org `litert-community`, library `litert-lm`, created 29 Sep 2026, updated 10 Nov 2026).
These are "the light RT bundle ... all three":

| Bundle | What it is (model card) | Generic file | Snapdragon files |
|---|---|---|---|
| `embeddinggemma-2-text-270m-litert-lm` | text only; 130M transformer + 140M embedder; 100+ languages, code; Matryoshka down to 128d | 164.6 MB | SM8750 187.6 MB, SM8850 202.3 MB, SM8650 207.8 MB |
| `embeddinggemma-2-text-vision-440m-litert-lm` | text + images; 270M text + 170M vision encoder; one 768-d space | 387.7 MB | SM8750 446.6 MB, SM8850 462.5 MB |
| `embeddinggemma-2-740m-litert-lm` | full: text, code, images, video, audio (+300M audio encoder); 768-d; 8,192-token context | 484.6 MB | SM8750 543.5 MB, SM8850 559.4 MB; also `NPU_Uncompiled` 569.6 MB |

- Each bundle ships a generic `.litertlm` plus chip-specific builds (Google Tensor G5/G6, MediaTek, Intel PTL,
  Qualcomm QCS8275, SM8550, SM8650, SM8750, SM8850). Which one fits this phone depends on its chip: Task B checks it.
- Runtimes named on the cards: LiteRT-LM (developers.google.com/edge/litert-lm/overview), MediaPipe (Universal
  Embedder, Semantic Retriever, Decision Maker), the Google AI Edge Gallery app on Android.
- Owner's plan fits the cards: text 270M for extraction now; text-vision 440M or 740M later for image/vector work.
- Other formats exist (ONNX, GGUF incl. `lufficcv/embeddinggemma-2-vision-GGUF`, CoreML, MLC) but are not the
  owner's pick. A 4th litert-community repo is a medical LoRA (`embeddinggemma-2-medical-lora-litertlm`), not a size.

## Gemini 4 Argon and Gemini 4 Carbon (the owner's "argon and carbon")
They are two models, not account names.
- **Argon:** "the ideal choice for the majority of software engineering and knowledge work" (blog.google, Gemini 4
  Carbon post, 10 Nov 2026). In Antigravity: plans Pro (paid or eligible trial), Ultra, Enterprise; thinking Low,
  Medium, High (antigravity.google/docs/models, no date shown).
- **Carbon:** released 10 Nov 2026, Google's strongest model: long agentic work, software, science, cybersecurity;
  uses more tokens to reason and verify. API id appears to be `gemini-4-carbon` (blog). API price $2/$10 per million
  tokens, rising to $4/$20 on 30 Nov 2026. Consumer: Google AI Ultra in the Gemini app, AI Mode, Antigravity. In
  Antigravity: Ultra and Enterprise only (docs/models). OpenRouter lists `google/gemini-4-carbon`, 1.05M context
  (openrouter.ai/models, 11 Nov 2026).
- So "2 accounts with gemini argon and carbon": a Pro-level account gets Argon, an Ultra account gets Carbon (and
  Argon). Owner to confirm which account is which plan.

## AGY = Google Antigravity CLI
- Binary `agy` (antigravity.google/docs/cli/headless). Headless: `agy -p "<prompt>"`; `--output-format text|json|
  stream-json`; `--json-schema`; `agy models` lists model slugs; `--model gemini-3.8-flash-medium` (unknown model exits
  non-zero, no fallback); `--effort low|medium|high`; `--agent <name>`; `-c` / `--conversation <id>`;
  `--print-timeout`; `--sandbox`; tools needing approval are soft-denied unless allowed in
  `~/.gemini/antigravity-cli/settings.json` `permissions.allow` (or `--dangerously-skip-permissions`).
- Auth (antigravity.google/docs/install): run `agy` once interactively; browser OAuth with a personal Google
  account (Free, Pro or Ultra); over SSH it prints a URL and takes the code back. Credentials go to the OS keyring
  (Linux: Secret Service/dbus). API key mode exists (`"modelProvider": "gemini"` + `GEMINI_API_KEY`), but the owner's
  rule is account credits, not the API. Multiple accounts at once: not stated; `/logout` switches.
- Credits (antigravity.google/docs/cli/credits): the CLI uses the subscription's AI Premium credits; `/credits`,
  `/usage`; `"useG1Credits": true` spends credits after plan quota runs out. Per-model cost: not stated (Plans page).
- Antigravity has `/swarm` (preview, 10 Nov 2026): coordinator + parallel workers in isolated git worktrees +
  adversarial verifiers on a shared message board (antigravity blog). Matches the owner's parallel-worker design.
- Gemini CLI: Antigravity CLI keeps Gemini CLI's constructs; `agy plugin import gemini` converts extensions to plugins;
  GEMINI.md and AGENTS.md work unchanged; MCP config moves to `~/.gemini/config/mcp_config.json` or
  `.agents/mcp_config.json` (antigravity.google/docs/cli/gcli-migration). No retirement date stated for Gemini CLI.
- Platforms: not stated on the pages read (no mention of Linux arm64, Android or Termux). Task B checks this phone.

## Models in Antigravity (docs/models, no date shown)
Gemini 4 Carbon (Ultra, Enterprise); Gemini 4 Argon (Pro paid/trial, Ultra, Enterprise); Gemini 3.8 Flash (all
plans; thinking Low/Medium/High + Fast); Gemini 3.7/3.6 Flash and 3.1 Pro (Enterprise); Claude Sonnet 5.5 and Opus
5.5 Thinking (Pro non-trial, Ultra, Enterprise); Claude 4.6 models and GPT-OSS 120B removed 18 Nov 2026.
Gemini 3.8 Flash is the bulk-ingestion model on every plan.

## Qwen 3.5 0.8B
`Qwen/Qwen3.5-0.8B`, image-text-to-text (vision-language), Apache-2.0, created 28 Feb 2026 (Hugging Face Hub search).
Builds exist as GGUF (unsloth, ggml-org, bartowski, turintech Artemis), ONNX, AWQ, MLX. The owner already runs it
on the NPU; which build and runtime: Task B.

## JEV
TypeSafe Jev: a "System One" decision model that answers typed questions with calibrated probabilities (the
`typesafe:typesafe-ai` skill description in this session). It routes every prompt here already (hook lines show
`via typesafe jev-1.14.0`). OpenRouter also lists `google/gemini-decision-1` and `parallel/decisions-fast:free`
(11 Nov 2026), same class of model.

## OpenRouter, newest frontier models (openrouter.ai/models?order=newest, 11 Nov 2026)
- `anthropic/claude-fable-5.2` (9 Nov 2026), 1M context, $8 in / $40 out per million; `:batch` half price.
- `google/gemini-4-carbon` (10 Nov 2026), 1.05M context, $2 / $10; `:batch` $1 / $5.
- `google/gemini-omni-1.2-flash` (5 Nov 2026), 131K. Free long-context options: `baidu/ernie-5.5-flash-preview:free`
  (1.02M), `thinkingmachines/inkling-2-small:free` (1.05M).
- The 20 newest models listed no OpenAI, xAI (text), DeepSeek or Qwen frontier model; older ones were not looked up.
- OpenRouter is a paid API (credits on the OpenRouter account); it is the owner's named route for frontier inference.

## Searches that failed
- DuckDuckGo HTML: bot challenge, no results (3 tries). Google search: "trouble accessing" page. Bing worked.
- antigravity.google pages via claw_scrape returned only navigation; WebFetch read them.
