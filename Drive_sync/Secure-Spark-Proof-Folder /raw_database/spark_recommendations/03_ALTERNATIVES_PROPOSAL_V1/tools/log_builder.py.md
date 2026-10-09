---
title: "log_builder.py"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/tools/log_builder.py.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

#!/usr/bin/env python3
"""
Mobile Agent JSONL Telemetry Logger
Appends structured operational event logs to episodic memory.
"""
import os
import json
from pathlib import Path
from datetime import datetime, timezone

LOG_FILE = Path(os.environ.get("LOG_FILE",
"~/novae-xorpus/05_episodic_logs/daily_driver_sync/agent_logs.jsonl")).expanduser()

def log_event():
    print("\n--- New Agent Interaction Event ---")
    agent_id = os.environ.get("CURRENT_AGENT", input("Agent ID (e.g., A-102, EXEC-01):
").strip())
    client_or_task = input("Task / Client Identifier: ").strip()
    status = input("Execution Status (active/pending/complete/flagged): ").strip()
    summary = input("Log Details / Action Output: ").strip()

    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent_id": agent_id,
        "task": client_or_task,
        "status": status,
        "interaction_summary": summary,
        "device_location": os.environ.get("DEVICE_LOC", "local_mobile_node")
    }

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

    print(f"--> Appended event to {LOG_FILE}\n")

if __name__ == "__main__":
    log_event()
