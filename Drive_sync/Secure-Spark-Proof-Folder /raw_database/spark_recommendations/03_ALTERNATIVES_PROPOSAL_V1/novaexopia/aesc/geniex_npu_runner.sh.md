---
title: "geniex_npu_runner.sh"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/aesc/geniex_npu_runner.sh.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

#!/usr/bin/env bash
#
========================================================================
======
# GenieX Snapdragon 8 Elite (Hexagon v79 HTP) NPU Execution Daemon
#
========================================================================
======
set -euo pipefail

MODEL_PATH="${1:-/data/local/tmp/models/Qwen3.5-0.8B-GGUF}"
DEVICE_MODE="${2:-hybrid}" # hybrid (default/fastest ~90 tok/s prefill) | npu (pinned HTP0) |
cpu
SOCKET_PATH="/dev/socket/npu_manager.sock"

echo "[*] Initializing GenieX runtime on device: ${DEVICE_MODE}"
echo "[*] Model: ${MODEL_PATH}"

case "$DEVICE_MODE" in
    hybrid)
        # Per-tensor scheduler: HTP for supported ops, CPU fallback
        EXEC_FLAGS="--device hybrid"
        ;;
    npu)
        # Pinned deterministic HTP0 execution
        EXEC_FLAGS="--device npu"
        ;;
    cpu)
        EXEC_FLAGS="--device cpu"
        ;;
    *)
        echo "[-] Unknown device mode: $DEVICE_MODE. Defaulting to hybrid."
        EXEC_FLAGS="--device hybrid"
        ;;
esac

# Check for existing daemon socket
if [ -S "$SOCKET_PATH" ]; then
    echo "[*] Verified NPU manager socket at ${SOCKET_PATH}"
fi

exec geniex infer "$MODEL_PATH" $EXEC_FLAGS
