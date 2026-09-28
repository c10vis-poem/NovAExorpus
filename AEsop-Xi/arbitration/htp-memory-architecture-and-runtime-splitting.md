---
source: raw/htp-memory-architecture-and-runtime-splitting.txt
cleaned: 2026-09-09
converter: manual verbatim extraction (fluff-stripped)
extracted_skill: skills/snapdragon-npu-partitioner/SKILL.md
extracted_tool: tools/htp_partition_calc.py
---

# Qualcomm Hexagon HTP Memory Architecture, Multi-Device Virtualization, and Runtime Splitting

## W5+H Artifact Specification

- **WHO:** Future System Installer, Automated Build Agent, or Human Maintainer.
- **WHAT:** Engineering manual & diagnostic tooling for Hexagon NPU model partitioning.
- **WHEN:** Required before staging, quantizing, or running any local LLM > 3.5GB (e.g., Qwen 3.5 9B Q4_0, Gemma 4 12B QAT) on Snapdragon hardware.
- **WHERE:** On-device (Snapdragon 8 Elite / FastRPC / Termux) & host CI toolchains.
- **WHY:** Prevents driver crashes, uncatchable SIGSEGV faults, and OS reboots caused by exceeding the 32-bit FastRPC User Process Domain ceiling.
- **HOW:** Enforces multi-device layer distribution (`D=HTP0,HTP1`) in llama.cpp, or dynamic DMA context chunking in Qualcomm QAIRT / GENIE SDKs.

**Problem solved:** Bypasses the ~3.5GB FastRPC User Process Domain (uPD) memory-mapping barrier on 64-bit Snapdragon SoCs, enabling 5.5GB–12GB+ models to run entirely on NPU silicon.

## Part 1: The Hardware Reality (CPU vs. Hexagon NPU)

A 64-bit SoC with 16GB of LPDDR5X RAM does not mean model buffers can be allocated anywhere in physical memory — the Oryon CPU and the Hexagon NPU/DSP operate under fundamentally different memory models:

| Oryon CPU (64-bit Arm) | Hexagon NPU / DSP (QuRT) |
|---|---|
| Full 64-bit virtual addressing | Sandboxed User Process Domain |
| Can map all 16GB contiguous | 32-bit FastRPC address space |
| No 3.5GB session ceiling | Hard ~3.5GB usable limit/PD |

**Why the 3.5GB ceiling exists:** The FastRPC User Process Domain (uPD) sandboxes user NPU tasks inside a QuRT-micro-kernel-managed domain to prevent an untrusted user process from corrupting core modem or sensor DSP routines. This domain operates within a 32-bit address space (4GB max). QuRT kernel mappings, FastRPC driver page tables, hardware stack frames, and DMA scatter-gather buffers occupy ~500MB of that space.

**Net usable window:** any single mapped buffer (model weights + runtime KV cache) cannot exceed ~3.5GB. Allocating a contiguous 5.5GB buffer (such as Qwen 3.5 9B Q4_0) results in an immediate `QNN_MEM_ALLOC_ERROR` or kernel crash.

## Part 2: The Two Solutions for Running >3.5GB Models

### Solution A: Multi-Device Virtualization (llama.cpp / FastRPC)

In llama.cpp with the Snapdragon backend (`libggml-htp.so`), the driver treats Hexagon like a multi-GPU cluster by instantiating multiple virtual Process Domains. For Qwen 3.5 9B Q4_0 GGUF (~5.6GB), split across virtual Process Domains:

- **Virtual Device HTP0** (Process Domain 1: max 3.5GB) — Transformer layers 0–24
- **Virtual Device HTP1** (Process Domain 2: max 3.5GB) — Transformer layers 25–48

Command-line execution flag:

```bash
# Split execution across two 3.5GB virtual process domains
D=HTP0,HTP1 ./llama-cli \
  -m models/qwen3.5-9b-q4_0.gguf \
  -p "System initialized." \
  --n-gpu-layers 49
```

**Inter-domain transfer:** layers 0–24 execute inside HTP0. Intermediate activations pass over the high-speed internal chip RPC to HTP1, which completes layers 25–48 and returns the output tokens.

### Solution B: Qualcomm QAIRT & GENIE Context Chunking

For precompiled native graphs (`.bin` assets via QAI-Hub or LiteRT):

- **Model pipeline compilation:** the model is not compiled into a single flat buffer. The compiler chunks the tensor graph into subgraphs matching target HTP slice sizes.
- **DMA streaming:** weights stream dynamically from system RAM into the HTP scratchpad through Direct Memory Access (DMA), avoiding static 32-bit address exhaustion.

## Part 3: Executable Skill

Extracted to [`skills/snapdragon-npu-partitioner/SKILL.md`](../skills/snapdragon-npu-partitioner/SKILL.md) — validates and configures the multi-device split for a given model automatically.

## Part 4: Validation & Diagnostic Script

Extracted to [`tools/htp_partition_calc.py`](../tools/htp_partition_calc.py) — computes the required Process Domain count from model file size and context length before launch, eliminating trial-and-error memory allocation faults.
