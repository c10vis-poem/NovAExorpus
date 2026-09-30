#!/usr/bin/env python3
"""
htp_partition_calc.py
----------------------
Hexagon NPU Partition Calculator & Command Generator.

WHY: The FastRPC User Process Domain (uPD) on Qualcomm Snapdragon SoCs has a
hard ~3.5GB usable memory ceiling per domain (32-bit FastRPC address space,
~500MB reserved for QuRT kernel/driver overhead). A model + KV cache exceeding
that in one domain causes a QNN_MEM_ALLOC_ERROR or kernel crash. This script
computes how many virtual HTP domains (D=HTP0,HTP1,...) a model needs before
launch, so the split is sized mathematically instead of by trial and error.

Source: aesop-xi/raw/htp-memory-architecture-and-runtime-splitting.txt
"""
import os
import sys
import argparse

MAX_PD_USABLE_GB = 3.25  # Conservative ceiling leaving margin for driver heaps


def calculate_npu_allocation(model_path: str, context_len: int, layers: int = 48) -> dict:
    if not os.path.exists(model_path):
        return {"status": "error", "message": f"Model file not found: {model_path}"}

    file_size_gb = os.path.getsize(model_path) / (1024 ** 3)

    # Rough estimate of FP16 KV cache overhead for standard architectures
    kv_cache_gb = (2 * layers * 4096 * context_len * 2) / (1024 ** 3) * 0.05
    total_required_gb = file_size_gb + kv_cache_gb

    if total_required_gb <= MAX_PD_USABLE_GB:
        domains = ["HTP0"]
    elif total_required_gb <= (MAX_PD_USABLE_GB * 2):
        domains = ["HTP0", "HTP1"]
    elif total_required_gb <= (MAX_PD_USABLE_GB * 3):
        domains = ["HTP0", "HTP1", "HTP2"]
    else:
        return {
            "status": "warning",
            "message": f"Model ({total_required_gb:.2f} GB) exceeds 3-domain limit. Heterogeneous offloading required."
        }

    device_string = ",".join(domains)
    return {
        "status": "success",
        "file_size_gb": round(file_size_gb, 2),
        "total_memory_gb": round(total_required_gb, 2),
        "domains_required": len(domains),
        "device_flag": f"D={device_string}",
        "export_cmd": f"export D={device_string}"
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Qualcomm Hexagon NPU Partition Calculator")
    parser.add_argument("--model", type=str, required=True, help="Path to GGUF or BIN model file")
    parser.add_argument("--ctx", type=int, default=4096, help="Target context window size")
    args = parser.parse_args()

    result = calculate_npu_allocation(args.model, args.ctx)
    if result["status"] == "success":
        print(f"[OK] Model: {result['file_size_gb']} GB | Total Req: {result['total_memory_gb']} GB")
        print(f"[OK] Partitions: {result['domains_required']} Domain(s) -> {result['device_flag']}")
        print(f"\nExecution Prefix:\n{result['export_cmd']}")
    else:
        print(f"[{result['status'].upper()}] {result['message']}")
        sys.exit(1)
