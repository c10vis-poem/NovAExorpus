---
name: snapdragon-npu-partitioner
description: Validates and configures large LLMs for Qualcomm Hexagon NPU multi-device execution. Use when staging, quantizing, or launching a local LLM larger than ~3.2GB on Snapdragon hardware, or when a QNN_MEM_ALLOC_ERROR / kernel crash occurs from exceeding the FastRPC User Process Domain memory ceiling. Trigger on "run model on npu", "partition llm weights", "configure htp execution".
triggers:
  - "run model on npu"
  - "partition llm weights"
  - "configure htp execution"
inputs:
  model_path: string
  context_length: integer
tools_required:
  - terminal_exec
  - file_inspector
source_doc: aesop-xi/raw/htp-memory-architecture-and-runtime-splitting.txt
---

# Operating Instructions

1. **Inspect Model Footprint:**
   - Query the target model size in gigabytes.
   - Calculate estimated KV Cache: `(2 * layers * heads * head_dim * context_len * precision)`.

2. **Evaluate Process Domain (PD) Allocation:**
   - Total Memory = `Model Size + KV Cache Overhead`.
   - If Total Memory <= 3.2 GB: Allocate single domain (`D=HTP0`).
   - If 3.2 GB < Total Memory <= 6.5 GB: Allocate dual domain (`D=HTP0,HTP1`).
   - If Total Memory > 6.5 GB: Enforce 3-way split (`D=HTP0,HTP1,HTP2`) or offload embedding heads to CPU/GPU.

3. **Verify Runtime Environment:**
   - Check presence of `libQnnHtp.so` or `libggml-htp.so` in dynamic linker path.
   - Confirm `/dev/adsprpc-smd` (FastRPC character device) is accessible with read/write permissions.

4. **Emit Verified Run Command:**
   - Return the exact execution flags to the executor daemon without manual user intervention.

Use `tools/htp_partition_calc.py` to compute the domain split mechanically rather than doing this by hand.
