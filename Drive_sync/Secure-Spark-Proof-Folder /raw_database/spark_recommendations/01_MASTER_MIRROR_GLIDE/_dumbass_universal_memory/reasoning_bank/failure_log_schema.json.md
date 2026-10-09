---
title: "failure_log_schema.json"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/01_MASTER_MIRROR_GLIDE/_dumbass_universal_memory/reasoning_bank/failure_log_schema.json.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ReasoningBankFailureLogSchema",
  "type": "object",
  "properties": {
    "log_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "node_id": { "type": "string", "enum": ["node_alpha", "node_beta", "node_gamma"] },
    "model_name": { "type": "string" },
    "task_id": { "type": "string" },
    "step_number": { "type": "integer" },
    "error_type": { "type": "string", "enum": ["SYNTAX", "HALLUCINATION",
"PERMISSION_DENIED", "LMK_KILLED", "TIMEOUT"] },
    "failed_prompt_snippet": { "type": "string" },
    "error_trace": { "type": "string" },
    "quarantine_status": { "type": "string", "enum": ["QUARANTINED", "TRIAGED", "RESOLVED"]
},
    "reward_score": { "type": "number", "minimum": -1.0, "maximum": 1.0 }
  },
  "required": ["log_id", "timestamp", "node_id", "error_type", "quarantine_status"]
}
