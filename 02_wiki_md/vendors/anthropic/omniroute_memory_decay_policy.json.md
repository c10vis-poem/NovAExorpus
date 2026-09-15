---
source: omniroute_memory_decay_policy.json.pdf
type: pdf
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

{
  "system": "OmniRoute Memory Subsystem",
  "version": "1.0",
  "storage_engine": "SQLite FTS5 + int8 Vector Quantization",
  "port": 20128,
  "protocols_supported": ["MCP", "A2A", "OpenAI_v1"],
  "bypass_header": "x-omniroute-no-memory",
  "typed_decay_policy": {
    "session_context": {
      "ttl_hours": 12,
      "decay_type": "exponential",
      "prune_on_overflow": true
    },
    "user_syntax_habits": {
      "ttl_days": 90,
      "decay_type": "linear",
      "reinforce_on_hit": true
    },
    "technical_spec_markers": {
      "ttl_days": null,
      "decay_type": "permanent",
      "immutable": true
    },
    "error_traces": {
      "ttl_days": 14,
      "decay_type": "step",
      "export_target": "reasoning_bank/failure_logs"
    }
  },
  "resilience": {
    "circuit_breaker": true,
    "key_cooldown_seconds": 60,
    "max_consecutive_failures": 3
  }
}
