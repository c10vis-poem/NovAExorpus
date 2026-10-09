---
title: "schema.sql"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/01_MASTER_MIRROR_GLIDE/_dumbass_universal_memory/sqlite/schema.sql.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

--
========================================================================
======
-- #d.u.m.b.a.s.s. (Database & Universal Memory Bank Across Split Services)
-- Local SQLite Edge Cache & State Ledger Schema (Version 1.0)
-- Target Runtimes: Node Alpha (Android/Termux/Æsc), Node Beta (Jetson), Local Daemons
--
========================================================================
======

PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA foreign_keys = ON;
PRAGMA temp_store = MEMORY;

-- 1. Low-Latency Key-Value Store
CREATE TABLE IF NOT EXISTS kv_store (
    key TEXT PRIMARY KEY,
    namespace TEXT NOT NULL DEFAULT 'global',
    value TEXT NOT NULL, -- JSON string or raw text
    data_type TEXT NOT NULL DEFAULT 'json',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ttl_seconds INTEGER DEFAULT NULL
);

CREATE INDEX IF NOT EXISTS idx_kv_namespace ON kv_store(namespace);

-- 2. Active Agent Task State Ledger
CREATE TABLE IF NOT EXISTS active_task_state (
    task_id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL,
    parent_task_id TEXT,
    agent_role TEXT NOT NULL, -- 'triage', 'query', 'executor', 'auditor'
    status TEXT NOT NULL DEFAULT 'PENDING', -- 'PENDING', 'RUNNING', 'PAUSED',
'COMPLETED', 'FAILED'
    priority INTEGER DEFAULT 5,
    state_payload TEXT NOT NULL, -- JSON state checkpoint
    recovery_checkpoint TEXT, -- JSON serialization for resume
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE INDEX IF NOT EXISTS idx_task_status ON active_task_state(status);
CREATE INDEX IF NOT EXISTS idx_task_session ON active_task_state(session_id);

-- 3. Fast Entity Lookup Cache
CREATE TABLE IF NOT EXISTS entity_lookup (
    entity_id TEXT PRIMARY KEY,
    canonical_name TEXT NOT NULL UNIQUE,
    entity_type TEXT NOT NULL, -- 'concept', 'architecture', 'daemon', 'device', 'repo'
    aliases TEXT, -- JSON array of alias strings
    summary TEXT NOT NULL,
    attributes TEXT, -- JSON key-value pairs
    last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    access_count INTEGER DEFAULT 1
);

CREATE INDEX IF NOT EXISTS idx_entity_canonical ON entity_lookup(canonical_name);
CREATE INDEX IF NOT EXISTS idx_entity_type ON entity_lookup(entity_type);

-- 4. Fast Token & Completion Cache (RTK / Inference Deduplication)
CREATE TABLE IF NOT EXISTS local_token_cache (
    prompt_hash TEXT PRIMARY KEY,
    model_id TEXT NOT NULL,
    temperature REAL DEFAULT 0.0,
    tokens_in INTEGER,
    tokens_out INTEGER,
    cached_response TEXT NOT NULL,
    latency_ms INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_token_model ON local_token_cache(model_id);

-- 5. Cross-Node Episodic Event Queue
CREATE TABLE IF NOT EXISTS episodic_event_queue (
    event_id TEXT PRIMARY KEY,
    event_type TEXT NOT NULL, -- 'trajectory', 'audit_verdict', 'habit_update', 'memory_sync'
    source_node TEXT NOT NULL, -- 'node_alpha', 'node_beta', 'node_gamma'
    payload TEXT NOT NULL, -- JSON event details
    synced_to_postgres INTEGER DEFAULT 0, -- 0 = pending, 1 = synced
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_event_synced ON


episodic_event_queue(synced_to_postgres);
