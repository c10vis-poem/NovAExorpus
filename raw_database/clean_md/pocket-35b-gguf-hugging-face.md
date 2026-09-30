---
source: raw/FINAL-Bench/POCKET-35B-GGUF · Hugging Face
cleaned: 2026-09-09
converter: pdftotext -layout, then manual removal of Hugging Face site chrome (top search bar, nav tabs "Model card / Files / xet / Community", "Deploy / Copy to bucket / Use this model" buttons, "Edit model card" button, footer nav "Company / TOS / Privacy / About / Careers / Website / Models / Datasets / Spaces / Pricing / Docs", "System theme" toggle)
CAVEAT: several figures in the source ("Generation speed (tok/s)" and the CPU/GPU comparison charts) are rendered as bar charts in the original page; the numeric labels next to each bar were extracted and are presented below as a table since the bars themselves cannot be reproduced in markdown. All numbers, percentages, and text are otherwise preserved verbatim.
---

# FINAL-Bench / POCKET-35B-GGUF

like 33 · Follow FINAL_Bench 254

Tags: Text Generation · GGUF · llama.cpp · conversational · on-device · mobile · iphone · android · cpu · local-llm · edge · mixture-of-experts · Mixture of Experts · quantized · imatrix · pocket · vidraft · qwen3_5_moe · darwin

License: apache-2.0

Downloads last month: 5,513

GGUF · Model size 35B params · Architecture qwen35moe · Chat template

## Hardware compatibility

| Quant | Format | Size |
|---|---|---|
| 1-bit | IQ1_M | 8.24 GB |
| 2-bit | Q2_K | 12.9 GB |
| 3-bit | Q3_K_M | 16.8 GB |
| 4-bit | Q4_K_M | 21.2 GB |

## Inference Providers

Text Generation

This model isn't deployed by any Inference Provider. 🙋 Ask for provider support

## Model tree for FINAL-Bench/POCKET-35B-GGUF

Base model: FINAL-Bench/Darwin-36B-Opus
Quantized (16): this model

Space using FINAL-Bench/POCKET-35B-GGUF: 1
- FINAL-Bench/POCKET-35B-CPU

Collection including FINAL-Bench/POCKET-35B-GGUF:
- POCKET-MODELs — Collection, 5 items • Updated 1 day ago • 14

Article mentioning FINAL-Bench/POCKET-35B-GGUF:
- "POCKET: a 35-billion-parameter model that runs on your iPhone — and on your PC with no …" — FINAL-Bench • 1 day ago • 9

---

## Model Card

> 📚 Collections
> "▶ POCKET Models — this family (on-device, no GPU) Darwin Family · Aether Foundation · VKAE Accelerated · Metacognition Adapters"

### POCKET-35B

A 35B model that runs on your iPhone — and on your PC with no GPU. **35B runs here. no GPU**

Just stock llama.cpp. No fork, no CUDA, no cloud.

| iPhone-ready | CPU-only | Stock runtime |
|---|---|---|
| 5 GB · Korean & English | 27 tok/s · no GPU needed | LM Studio · Ollama · PocketPal |

34.66B total · ~3B active/token · sparse Mixture-of-Experts, Korean-tuned

### POCKET-35B-GGUF

A 35B model that runs on your PC with no GPU — and on your phone. Just stock `llama.cpp`. No fork, no CUDA, no cloud.

> 🚀 "Try it live, no install → 🤗 Space POCKET-35B CPU chat — a 35B model answering on a CPU-only box."

License Apache 2.0 · runtime stock llama.cpp · GPU not required · base Qwen3.5-35B-A3B

Pick your build → POCKET-35B GGUF · POCKET-KR GGUF · POCKET-KR MLX (iPhone) · POCKET-EN GGUF

### The POCKET lineup — pick by your device

| Repo | File | Size | Runs on | Best for | Korean PPL* |
|---|---|---|---|---|---|
| POCKET-35B-GGUF | Q4_K_M | 21 GB | PC / server (32 GB RAM) | top quality | 5.79 |
| POCKET-35B-GGUF | Q2_K ⭐ | 13 GB | mini-PC, no GPU | daily driver | 6.49 |
| POCKET-35B-GGUF | IQ1_M | 8.2 GB | 16 GB RAM box | smallest full model | 9.69 |
| POCKET-KR-GGUF | IQ2_M | 5.1 GB | Android 8 GB+ | 🇰🇷 Korean phone | 7.95 |
| POCKET-KR-MLX | 2-bit | 5.1 GB | 🍎 iPhone / iPad / Mac | 🇰🇷 Korean, Apple-native | 7.95 |
| POCKET-EN-GGUF | iPhone-mix | 5.3 GB | 🍎 iPhone (PocketPal) | 🌍 English phone | — |
| POCKET-EN-GGUF | PC-mix | 6.8 GB | PC / Android | 🌍 English, best quality | — |

*Wikipedia-Korean perplexity, lower is better. Q4_K_M = 5.79 baseline. English builds are tuned on English; see each repo.

> 🍎 "Why MLX for Korean but GGUF for English on iPhone? Apple-native MLX only does uniform quantization. Korean survives it (96 experts hold up); English needs our mixed-precision trick, which only GGUF supports — so the English iPhone build ships as a GGUF you run with PocketPal. Honest, not lazy."

### Generation speed (tok/s) — same machine, stock llama.cpp

POCKET-35B IQ1_M (7.66 GB) vs Bonsai-27B Q1_0 (3.53 GB) · higher is better

**CPU · Xeon 16 threads**

| Model | tok/s |
|---|---|
| POCKET | 27.0 |
| Bonsai | 10.1 |

POCKET 2.69x faster

**GPU · H100 NVL**

| Model | tok/s |
|---|---|
| POCKET | 197 |
| Bonsai | 89 |

POCKET 2.22x faster

**Honest caveat**: GPU prompt-processing: Bonsai wins (1816 vs 753 tok/s). Quality (HellaSwag 400): tie, 61.0% vs 60.0%.

### Benchmarks — what is measured, what is not

We measure Bonsai on the same machine with the same stock `llama.cpp`, and we tell you where we lose.

**[measured] Generation speed — POCKET wins on both CPU and GPU:**

| Metric | POCKET-35B IQ1_M | Bonsai-27B Q1_0 | Result |
|---|---|---|---|
| CPU generate (Xeon, 16t) | 27.0 tok/s | 10.1 | 🟢 2.69× |
| GPU generate (H100) | 197 tok/s | 89 | 🟢 2.22× |
| GPU prompt (H100) | 753 | 1816 | 🔴 0.41× |
| Quality (HellaSwag, 400q) | 61.0% | 60.0% | ⚪ tie (CI overlaps) |

**[measured on a MacBook M3 Pro, 18 GB]** — and on a laptop, POCKET wins every axis, including prompt processing:

| Metric | POCKET-35B IQ1_M | Bonsai-27B Q1_0 | Result |
|---|---|---|---|
| Metal generate (tg64) | 25.4 tok/s | 12.8 | 🟢 1.99× |
| CPU generate (8 threads) | 13.8 tok/s | 4.4 | 🟢 3.13× |
| Metal prompt (pp128) | 240.7 tok/s | 73.4 | 🟢 3.28× |
| CPU prompt (pp128) | 45.5 tok/s | 9.6 | 🟢 4.75× |

On a laptop GPU the arithmetic headroom that let Bonsai win prefill on an H100 is gone, so MoE sparsity wins across the board. POCKET-35B-Q2_K runs on the M3 Pro's CPU at 19.5 tok/s — on an 18 GB Mac, run Q2_K on CPU ( -ngl 0 ); its 13 GB exceeds the recommended Metal budget.

**[measured — GPQA Diamond, 198q, greedy] reasoning quality vs quantization:**

| Model | GPQA-Diamond (greedy) |
|---|---|
| Qwen3.6-35B-A3B | 73.2% |
| POCKET-35B Q4_K_M | 68.7% |
| POCKET-35B Q2_K | 60.1% |

**[pending — community reports welcome]** on-device iPhone and Strix Halo throughput. We publish only what we ran ourselves; help us fill the rest.

> "The same-size rival Ternary-Bonsai-27B-Q2_0 (7.2 GB) fails to load in upstream llama.cpp — it needs the PrismML fork. POCKET runs on the tools you already have."

### Files in this repo

| File | Size | bpw | Runs on | Korean PPL |
|---|---|---|---|---|
| POCKET-35B-Q4_K_M.gguf | 21 GB | 4.5 | PC 32 GB RAM | 5.79 (top) |
| POCKET-35B-Q3_K_M.gguf | 16 GB | 3.4 | PC 24 GB | 6.06 |
| POCKET-35B-Q2_K.gguf ⭐ | 13 GB | 2.6 | mini-PC 16–24 GB | 6.49 (best value) |
| POCKET-35B-IQ1_M.gguf | 8.2 GB | 1.9 | 16 GB RAM | 9.69 (smallest) |

### Quickstart — no fork needed

```bash
# any recent llama.cpp — brew / winget / apt, or LM Studio / Ollama
llama-cli -m POCKET-35B-Q2_K.gguf -p "안녕하세요" -ngl 0 -t 8
# reproduce our CPU numbers:
llama-bench -m POCKET-35B-IQ1_M.gguf -p 128 -n 64 -ngl 0 -t 16
```

Use physical-core count for `-t` (max ~32). Do not pass all threads — it can slow down sharply.

### Lineage — where POCKET comes from

POCKET is quantized from Darwin-36B-Opus, VIDRAFT's flagship — a model bred and evolved over several generations on the Darwin platform (crossbreeding, healing, expert surgery). Darwin-36B-Opus itself traces back to a Qwen3.5-family MoE architecture.

| Component | Origin |
|---|---|
| Starting checkpoint | Darwin-36B-Opus — VIDRAFT, multi-generation Darwin evolution |
| Base architecture | Qwen3.5-family MoE (256 experts, top-8), unchanged |
| Quantization ( Q4_K_M … IQ1_M ) | stock llama.cpp — no custom format |
| Runtime | upstream llama.cpp / Apple MLX — unmodified |
| Expert pruning + domain imatrix (KR/EN builds) | ours (VIDRAFT) |

The CPU/GPU speed comes from the sparse-MoE architecture plus ordinary quantization — reproducible with the same base and the same tools. What we add is the Darwin-evolved weights, the honest measurement, the Korean tuning, and the pruning that makes the 5 GB phone builds.

### Limitations

- The iPhone/Mac speed is not yet measured by us — community reports welcome.
- Extreme quants ( IQ1_M ) hurt Korean ~2.8× more than English; use Q2_K or larger for quality.
- English phone builds trade quality for size; the PC build ( PC-mix ) is much closer to full quality.

### License

Apache-2.0.
POCKET is a VIDRAFT model family. 35B, in your pocket. No GPU.
