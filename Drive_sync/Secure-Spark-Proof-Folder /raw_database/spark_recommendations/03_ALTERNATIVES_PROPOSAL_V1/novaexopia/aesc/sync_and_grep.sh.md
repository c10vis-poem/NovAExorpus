---
title: "sync_and_grep.sh"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/aesc/sync_and_grep.sh.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

#!/usr/bin/env bash
#
========================================================================
======
# Mobile Drive Sync & Text Grep Utility (sync_and_grep.sh)
# Synchronizes Google Drive workspace to local storage via rclone
# and executes localized grep search across markdown and JSONL logs.
#
========================================================================
======
set -euo pipefail

WORKSPACE_DIR="${HOME}/AgentWorkspace"
REMOTE_NAME="gdrive:AgentWorkspace"

mkdir -p "$WORKSPACE_DIR"

echo "[*] Syncing latest agent files from Google Drive (${REMOTE_NAME})..."
if command -v rclone >/dev/null 2>&1; then
    rclone sync "$REMOTE_NAME" "$WORKSPACE_DIR" --fast-list --transfers 4
    echo "[✓] Sync complete."
else
    echo "[-] Error: rclone is not installed. Run: pkg install rclone"
    exit 1
fi

echo ""
read -p "[?] Enter keyword or regex to grep: " keyword

if [ -n "$keyword" ]; then
    echo "[*] Searching .md and .jsonl files in ${WORKSPACE_DIR}..."
    grep -rn --color=auto "$keyword" "$WORKSPACE_DIR"/*.md "$WORKSPACE_DIR"/*.jsonl
2>/dev/null || echo "[-] No matches found."
fi
