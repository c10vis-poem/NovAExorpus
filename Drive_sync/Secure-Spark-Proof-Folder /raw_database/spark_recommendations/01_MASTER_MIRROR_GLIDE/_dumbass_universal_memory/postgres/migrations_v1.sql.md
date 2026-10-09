---
title: "migrations_v1.sql"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/01_MASTER_MIRROR_GLIDE/_dumbass_universal_memory/postgres/migrations_v1.sql.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

--
========================================================================
======
-- #d.u.m.b.a.s.s. (Database & Universal Memory Bank Across Split Services)
-- Master PostgreSQL Schema & Migrations (Version 1.0)
-- Target Host: Node Beta (NVIDIA Jetson Orin Nano / Headless Ubuntu Server)
-- Database Engine: PostgreSQL 16+ with pgvector & pgcrypto
--
========================================================================
======

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "vector";

-- 1. Master Repositories & Subsystem Registry
CREATE TABLE IF NOT EXISTS repositories (
    repo_id VARCHAR(64) PRIMARY KEY, -- 'novaecopia', 'aesop-xi', 'novus-aexenti',
'skills-and-capabilities'
    canonical_name VARCHAR(128) NOT NULL,
    root_path VARCHAR(256) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 2. Universal Vector Memory Bank (Embeddings & Semantic Chunks)
CREATE TABLE IF NOT EXISTS vector_embeddings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    repo_id VARCHAR(64) REFERENCES repositories(repo_id) ON DELETE CASCADE,
    file_path VARCHAR(512) NOT NULL,
    chunk_index INT NOT NULL,
    token_count INT NOT NULL,
    content TEXT NOT NULL,
    embedding vector(1536), -- Standard embedding dimension (Text-Embedding-3 / local BGE)
    metadata JSONB DEFAULT '{}'::jsonb, -- Includes source headers, wikilinks, tags
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_embeddings_repo ON vector_embeddings(repo_id);
CREATE INDEX IF NOT EXISTS idx_embeddings_metadata ON vector_embeddings USING
gin(metadata);


-- HNSW index for high-speed approximate nearest neighbor search
CREATE INDEX IF NOT EXISTS idx_embeddings_hnsw ON vector_embeddings USING hnsw
(embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- 3. Enterprise Audit & Execution Ledger (Immutable Telemetry)
CREATE TABLE IF NOT EXISTS audit_ledger (
    log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id VARCHAR(128) NOT NULL,
    agent_role VARCHAR(64) NOT NULL, -- 'triage_0.8b', 'query_9b', 'executor_qwen',
'claude_code'
    action_name VARCHAR(128) NOT NULL,
    input_payload JSONB,
    output_payload JSONB,
    verdict VARCHAR(32) NOT NULL DEFAULT 'PENDING', -- 'PASS', 'FAIL', 'QUARANTINED',
'PENDING'
    reward_score NUMERIC(4, 2), -- e.g. +1.00 or -1.00
    latency_ms INT,
    node_origin VARCHAR(64) NOT NULL, -- 'node_alpha', 'node_beta', 'node_gamma'
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_audit_session ON audit_ledger(session_id);
CREATE INDEX IF NOT EXISTS idx_audit_verdict ON audit_ledger(verdict);
CREATE INDEX IF NOT EXISTS idx_audit_created ON audit_ledger(created_at);

-- 4. Quarantined & Failure Trace Register (Incognito Red Sandbox Integration)
CREATE TABLE IF NOT EXISTS quarantine_traces (
    quarantine_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    log_id UUID REFERENCES audit_ledger(log_id) ON DELETE SET NULL,
    batch_hash VARCHAR(64) NOT NULL,
    source_path VARCHAR(512) NOT NULL,
    rejection_code VARCHAR(64) NOT NULL, -- 'SYNTAX_ERROR', 'HALLUCINATED_PATH',
'SECURITY_VIOLATION'
    error_trace TEXT NOT NULL,
    is_resolved BOOLEAN DEFAULT FALSE,
    resolution_notes TEXT,
    quarantined_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_quarantine_hash ON quarantine_traces(batch_hash);

-- 5. Canonical Living Entity Knowledge Graph


CREATE TABLE IF NOT EXISTS canonical_entities (
    entity_id VARCHAR(128) PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    entity_type VARCHAR(64) NOT NULL, -- 'system', 'subsystem', 'daemon', 'apk',
'hardware_node'
    canonical_repo VARCHAR(64) REFERENCES repositories(repo_id) ON DELETE SET
NULL,
    definition TEXT NOT NULL,
    properties JSONB DEFAULT '{}'::jsonb,
    relations JSONB DEFAULT '[]'::jsonb, -- Array of {target_id, relation_type}
    last_synced TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_entities_type ON canonical_entities(entity_type);
CREATE INDEX IF NOT EXISTS idx_entities_props ON canonical_entities USING
gin(properties);
