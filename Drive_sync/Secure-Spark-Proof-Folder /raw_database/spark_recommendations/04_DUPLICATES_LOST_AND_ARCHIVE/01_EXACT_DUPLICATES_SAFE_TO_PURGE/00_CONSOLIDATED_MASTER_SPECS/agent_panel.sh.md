---
title: "agent_panel.sh"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/04_DUPLICATES_LOST_AND_ARCHIVE/01_EXACT_DUPLICATES_SAFE_TO_PURGE/00_CONSOLIDATED_MASTER_SPECS/agent_panel.sh.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

#!/usr/bin/env bash
#
========================================================================
======
# ON-DEVICE AGENT WORKSPACE MANAGER (ÆSC / TERMINAL DAEMON MENU)
#
========================================================================
======

WORKSPACE_DIR="${HOME}/novae-xorpus"
LOG_SCRIPT="${WORKSPACE_DIR}/tools/log_builder.py"
GDRIVE_REMOTE="gdrive:NovA-Corpus"

show_menu() {
    clear
    echo "=================================================="
    echo "  ÆSC TERMINAL AGENT CONTROLLER"
    echo "=================================================="
    echo "1) Sync Files from Google Drive (rclone)"
    echo "2) Add Structured JSONL Telemetry Entry"
    echo "3) Grep Workspace Files (.md, .jsonl, .py)"
    echo "4) Run System Housekeeper & Blueprint Sweep"
    echo "5) Recompile Universal Manifest (manifest.jsonl)"
    echo "6) Exit"
    echo "=================================================="
}

while true; do
    show_menu
    read -rp "Select option [1-6]: " opt
    case "$opt" in
        1)
            echo -e "\nRunning rclone sync from ${GDRIVE_REMOTE}..."
            rclone sync "${GDRIVE_REMOTE}" "${WORKSPACE_DIR}" --progress
            read -rp "Press Enter to continue..."
            ;;
        2)
            echo ""
            if [ -f "$LOG_SCRIPT" ]; then
                python3 "$LOG_SCRIPT"
            else
                echo "log_builder.py not found at ${LOG_SCRIPT}"
            fi


            read -rp "Press Enter to continue..."
            ;;
        3)
            echo ""
            read -rp "Enter search query: " query
            echo "--------------------------------------------------"
            grep -rn --color=always "$query" "${WORKSPACE_DIR}" --include=\*.md
--include=\*.jsonl --include=\*.py || echo "No matches found."
            echo "--------------------------------------------------"
            read -rp "Press Enter to continue..."
            ;;
        4)
            echo ""
            bash "${WORKSPACE_DIR}/tools/system_housekeeper.sh"
            read -rp "Press Enter to continue..."
            ;;
        5)
            echo ""
            python3 "${WORKSPACE_DIR}/tools/compile_manifest.py"
            read -rp "Press Enter to continue..."
            ;;
        6)
            echo "Session closed."
            exit 0
            ;;
        *)
            echo "Invalid selection. Please choose 1-6."
            sleep 1.5
            ;;
    esac
done
