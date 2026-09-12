---
source: mem0_session_config.yaml.pdf
type: pdf
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

#
========================================================================
======
# Mem0 Episodic Session Configuration — #d.u.m.b.a.s.s.
# Controls live experience tracking, habit extraction, and memory persistence
#
========================================================================
======

version: "1.0"

storage:
  backend: "sqlite"
  local_path: "/data/data/com.termux/files/home/.dumbass/mem0_episodic.db"
  remote_sync_target: "postgres://node-beta.local:5432/dumbass_vault"
  sync_cadence: "session_close" # syncs to Postgres on session /close

scoring:
  similarity_threshold: 0.82
  decay_rate_per_day: 0.05
  reinforcement_multiplier: 1.25

extraction_triggers:
  - trigger: "user_correction"
    action: "immediate_habit_update"
    priority: "highest"
  - trigger: "operator_rule_stated"
    action: "append_architectural_law"
    priority: "highest"
  - trigger: "tool_failure_detected"
    action: "record_failure_trace"
    priority: "high"

active_filters:
  trim_conversational_filler: true
  enforce_naming_canon: true
  prohibited_memory_keys:
    - "raw_auth_tokens"
    - "transient_session_cookies"
