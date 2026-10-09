---
title: "agent_panel.sh"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/aesc/agent_panel.sh.pdf"
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
# Terminal UI script for system status, rclone sync, process monitoring,
# housekeeper sweeps, and universal manifest compilation.
#
========================================================================
======

WORKSPACE_DIR="${HOME}/novae-xorpus"
LOG_SCRIPT="${WORKSPACE_DIR}/tools/log_builder.py"
GDRIVE_REMOTE="gdrive:NovA-Corpus"

show_menu() {
    clear
    echo "=================================================="
    echo "       ÆSC TERMINAL AGENT CONTROLLER (NODE ALPHA)"
    echo "=================================================="
    echo "1) Sync Files from Google Drive (rclone)"
    echo "2) Add Structured JSONL Telemetry Entry"
    echo "3) Grep Workspace Files (.md, .jsonl, .py)"
    echo "4) Run System Housekeeper & Blueprint Sweep"
    echo "5) Inspect NPU Model & Daemon Socket Status"
    echo "6) Recompile Universal Manifest (manifest.jsonl)"
    echo "7) Exit"
    echo "=================================================="
}

check_daemon_status() {
    echo "--------------------------------------------------"
    echo " DAEMON & SOCKET STATUS:"
    echo "--------------------------------------------------"
    for sock in "/dev/socket/aesc_shell.sock" "/dev/socket/aeyre_media.sock"
"/dev/socket/npu_manager.sock"; do
        if [ -S "$sock" ]; then
            echo " [ACTIVE] $sock"
        else
            echo " [OFFLINE] $sock"


        fi
    done
    if pgrep -f "WirelessAdbBridge" > /dev/null; then
        echo " [ACTIVE] WirelessAdbBridgeService"
    else
        echo " [OFFLINE] WirelessAdbBridgeService"
    fi
    echo "--------------------------------------------------"
}

while true; do
    show_menu
    read -rp "Select option [1-7]: " opt
    case "$opt" in
        1)
            echo -e "\nRunning rclone sync from ${GDRIVE_REMOTE}..."
            rclone sync "${GDRIVE_REMOTE}" "${WORKSPACE_DIR}" --progress || echo "rclone
sync failed or remote not configured."
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
--include=\*.jsonl --include=\*.py 2>/dev/null || echo "No matches found."
            echo "--------------------------------------------------"
            read -rp "Press Enter to continue..."
            ;;
        4)
            echo ""
            if [ -f "${WORKSPACE_DIR}/novaexopia/aesc/system_housekeeper.sh" ]; then
                bash "${WORKSPACE_DIR}/novaexopia/aesc/system_housekeeper.sh"
            elif [ -f "${WORKSPACE_DIR}/tools/system_housekeeper.sh" ]; then


                bash "${WORKSPACE_DIR}/tools/system_housekeeper.sh"
            else
                echo "system_housekeeper.sh not found."
            fi
            read -rp "Press Enter to continue..."
            ;;
        5)
            echo ""
            check_daemon_status
            read -rp "Press Enter to continue..."
            ;;
        6)
            echo ""
            if [ -f "${WORKSPACE_DIR}/tools/compile_manifest.py" ]; then
                python3 "${WORKSPACE_DIR}/tools/compile_manifest.py"
            else
                echo "compile_manifest.py pending deployment."
            fi
            read -rp "Press Enter to continue..."
            ;;
        7)
            echo "Session closed."
            exit 0
            ;;
        *)
            echo "Invalid selection. Please choose 1-7."
            sleep 1.5
            ;;
    esac
done
