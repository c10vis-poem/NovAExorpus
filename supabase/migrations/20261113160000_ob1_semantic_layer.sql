-- OB1 (Open Brain = Terrestrial Brain), layer 2 of the owner's memory spec: semantic/static memory and governing
-- principles. Ported from the owner's fork c10vis-poem/OB1 @238df6c (FSL-1.1-MIT): docs/01-getting-started.md (thoughts,
-- match_thoughts, RLS), recipes/content-fingerprint-dedup (SHA-256 fingerprint, upsert_thought, trigger),
-- schemas/agent-memory/schema.sql (governed sidecars). One change: embedding vector(768) for EmbeddingGemma 2
-- (OB1 uses 1536). project_id = repo, workspace_id = enterprise.

create extension if not exists vector;

create table if not exists public.thoughts (
  id uuid default gen_random_uuid() primary key,
  content text not null,
  embedding vector(768),
  metadata jsonb default '{}'::jsonb,
  content_fingerprint text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
create index if not exists thoughts_embedding_hnsw on public.thoughts using hnsw (embedding vector_cosine_ops);
create index if not exists thoughts_metadata_gin on public.thoughts using gin (metadata);
create index if not exists thoughts_created on public.thoughts (created_at desc);
create unique index if not exists idx_thoughts_fingerprint on public.thoughts (content_fingerprint) where content_fingerprint is not null;

create or replace function public.update_updated_at() returns trigger as $$
begin new.updated_at = now(); return new; end; $$ language plpgsql;
drop trigger if exists thoughts_updated_at on public.thoughts;
create trigger thoughts_updated_at before update on public.thoughts for each row execute function public.update_updated_at();

create or replace function public.set_content_fingerprint() returns trigger as $$
begin
  if new.content is not null and (new.content_fingerprint is null
     or (tg_op = 'UPDATE' and new.content is distinct from old.content)) then
    new.content_fingerprint := encode(sha256(convert_to(lower(trim(regexp_replace(new.content, '\s+', ' ', 'g'))), 'UTF8')), 'hex');
  end if;
  return new;
end; $$ language plpgsql;
drop trigger if exists trg_set_content_fingerprint on public.thoughts;
create trigger trg_set_content_fingerprint before insert or update on public.thoughts for each row execute function public.set_content_fingerprint();

create or replace function public.upsert_thought(p_content text, p_payload jsonb default '{}') returns jsonb as $$
declare v_fingerprint text; v_id uuid;
begin
  v_fingerprint := encode(sha256(convert_to(lower(trim(regexp_replace(p_content, '\s+', ' ', 'g'))), 'UTF8')), 'hex');
  insert into public.thoughts (content, content_fingerprint, metadata)
  values (p_content, v_fingerprint, coalesce(p_payload->'metadata', '{}'::jsonb))
  on conflict (content_fingerprint) where content_fingerprint is not null do update
    set updated_at = now(), metadata = public.thoughts.metadata || coalesce(excluded.metadata, '{}'::jsonb)
  returning id into v_id;
  return jsonb_build_object('id', v_id, 'fingerprint', v_fingerprint);
end; $$ language plpgsql;

create or replace function public.match_thoughts(query_embedding vector(768), match_threshold float default 0.7,
  match_count int default 10, filter jsonb default '{}'::jsonb)
returns table (id uuid, content text, metadata jsonb, similarity float, created_at timestamptz) language plpgsql as $$
begin
  return query select t.id, t.content, t.metadata, 1 - (t.embedding <=> query_embedding) as similarity, t.created_at
  from public.thoughts t
  where t.embedding is not null and 1 - (t.embedding <=> query_embedding) > match_threshold
    and (filter = '{}'::jsonb or t.metadata @> filter)
  order by t.embedding <=> query_embedding limit match_count;
end; $$;

alter table public.thoughts enable row level security;
drop policy if exists "Service role full access" on public.thoughts;
create policy "Service role full access" on public.thoughts for all using (auth.role() = 'service_role');
grant select, insert, update, delete on table public.thoughts to service_role;

CREATE TABLE IF NOT EXISTS public.agent_memories (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  thought_id UUID REFERENCES public.thoughts(id) ON DELETE SET NULL,
  workspace_id TEXT NOT NULL,
  project_id TEXT,
  channel_kind TEXT,
  channel_id TEXT,
  channel_thread_id TEXT,
  visibility TEXT NOT NULL DEFAULT 'project' CHECK (
    visibility IN ('personal', 'channel', 'project', 'workspace', 'organization')
  ),
  memory_type TEXT NOT NULL CHECK (
    memory_type IN (
      'decision',
      'output',
      'lesson',
      'constraint',
      'open_question',
      'failure',
      'artifact_reference',
      'work_log'
    )
  ),
  summary TEXT NOT NULL,
  content TEXT NOT NULL,
  lifecycle_status TEXT NOT NULL DEFAULT 'active' CHECK (
    lifecycle_status IN ('active', 'stale', 'superseded', 'disputed', 'rejected')
  ),
  provenance_status TEXT NOT NULL DEFAULT 'generated' CHECK (
    provenance_status IN (
      'observed',
      'inferred',
      'user_confirmed',
      'imported',
      'generated',
      'superseded',
      'disputed'
    )
  ),
  confidence NUMERIC(3,2) NOT NULL DEFAULT 0.50 CHECK (confidence >= 0 AND confidence <= 1),
  created_by TEXT NOT NULL DEFAULT 'agent' CHECK (created_by IN ('user', 'agent', 'system', 'import')),
  runtime_name TEXT,
  runtime_version TEXT,
  provider TEXT,
  model TEXT,
  task_id TEXT,
  flow_id TEXT,
  can_use_as_instruction BOOLEAN NOT NULL DEFAULT false,
  can_use_as_evidence BOOLEAN NOT NULL DEFAULT true,
  requires_user_confirmation BOOLEAN NOT NULL DEFAULT true,
  review_status TEXT NOT NULL DEFAULT 'pending' CHECK (
    review_status IN (
      'pending',
      'confirmed',
      'evidence_only',
      'restricted',
      'rejected',
      'stale',
      'merged'
    )
  ),
  last_confirmed_at TIMESTAMPTZ,
  stale_after TIMESTAMPTZ,
  idempotency_key TEXT,
  content_hash TEXT,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CHECK (
    can_use_as_instruction = false
    OR provenance_status IN ('user_confirmed', 'imported')
  )
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_agent_memories_idempotency_key
  ON public.agent_memories (idempotency_key)
  WHERE idempotency_key IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_agent_memories_scope
  ON public.agent_memories (workspace_id, project_id, visibility);

CREATE INDEX IF NOT EXISTS idx_agent_memories_review
  ON public.agent_memories (review_status, lifecycle_status, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_agent_memories_runtime_task
  ON public.agent_memories (runtime_name, task_id, flow_id);

CREATE INDEX IF NOT EXISTS idx_agent_memories_content_hash
  ON public.agent_memories (workspace_id, content_hash)
  WHERE content_hash IS NOT NULL;

CREATE TABLE IF NOT EXISTS public.agent_memory_source_refs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  memory_id UUID NOT NULL REFERENCES public.agent_memories(id) ON DELETE CASCADE,
  source_kind TEXT NOT NULL,
  uri TEXT,
  title TEXT,
  source_timestamp TIMESTAMPTZ,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_agent_memory_source_refs_memory
  ON public.agent_memory_source_refs (memory_id);

CREATE TABLE IF NOT EXISTS public.agent_memory_artifacts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  memory_id UUID NOT NULL REFERENCES public.agent_memories(id) ON DELETE CASCADE,
  artifact_kind TEXT NOT NULL,
  uri TEXT NOT NULL,
  description TEXT,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_agent_memory_artifacts_memory
  ON public.agent_memory_artifacts (memory_id);

CREATE TABLE IF NOT EXISTS public.agent_memory_relations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  from_memory_id UUID NOT NULL REFERENCES public.agent_memories(id) ON DELETE CASCADE,
  to_memory_id UUID NOT NULL REFERENCES public.agent_memories(id) ON DELETE CASCADE,
  relation TEXT NOT NULL CHECK (
    relation IN ('related_to', 'supersedes', 'superseded_by', 'conflicts_with', 'merged_into')
  ),
  confidence NUMERIC(3,2) DEFAULT 0.50 CHECK (confidence IS NULL OR (confidence >= 0 AND confidence <= 1)),
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (from_memory_id, to_memory_id, relation),
  CHECK (from_memory_id <> to_memory_id)
);

CREATE TABLE IF NOT EXISTS public.agent_memory_review_actions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  memory_id UUID NOT NULL REFERENCES public.agent_memories(id) ON DELETE CASCADE,
  action TEXT NOT NULL CHECK (
    action IN (
      'confirm',
      'edit',
      'evidence_only',
      'restrict_scope',
      'mark_stale',
      'merge',
      'reject',
      'dispute',
      'supersede'
    )
  ),
  actor_id TEXT,
  actor_label TEXT,
  notes TEXT,
  before JSONB,
  after JSONB,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_agent_memory_review_actions_memory
  ON public.agent_memory_review_actions (memory_id, created_at DESC);

CREATE TABLE IF NOT EXISTS public.agent_memory_recall_traces (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  request_id UUID NOT NULL DEFAULT gen_random_uuid(),
  workspace_id TEXT NOT NULL,
  project_id TEXT,
  runtime_name TEXT,
  runtime_version TEXT,
  task_id TEXT,
  flow_id TEXT,
  channel_kind TEXT,
  channel_id TEXT,
  query TEXT NOT NULL,
  schema_version TEXT NOT NULL,
  request_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  response_policy JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (request_id)
);

CREATE INDEX IF NOT EXISTS idx_agent_memory_recall_traces_scope
  ON public.agent_memory_recall_traces (workspace_id, project_id, created_at DESC);

CREATE TABLE IF NOT EXISTS public.agent_memory_recall_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  trace_id UUID NOT NULL REFERENCES public.agent_memory_recall_traces(id) ON DELETE CASCADE,
  memory_id UUID NOT NULL REFERENCES public.agent_memories(id) ON DELETE CASCADE,
  rank INTEGER NOT NULL,
  similarity NUMERIC(5,4),
  ranking_score NUMERIC(7,4),
  returned BOOLEAN NOT NULL DEFAULT true,
  used BOOLEAN,
  ignored_reason TEXT,
  use_policy_snapshot JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (trace_id, memory_id)
);

CREATE INDEX IF NOT EXISTS idx_agent_memory_recall_items_trace
  ON public.agent_memory_recall_items (trace_id, rank);

CREATE TABLE IF NOT EXISTS public.agent_memory_audit_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type TEXT NOT NULL CHECK (
    event_type IN (
      'recall_requested',
      'memory_returned',
      'memory_used',
      'memory_ignored',
      'memory_written',
      'memory_confirmed',
      'memory_edited',
      'memory_rejected',
      'memory_superseded',
      'memory_disputed'
    )
  ),
  workspace_id TEXT,
  project_id TEXT,
  memory_id UUID REFERENCES public.agent_memories(id) ON DELETE SET NULL,
  trace_id UUID REFERENCES public.agent_memory_recall_traces(id) ON DELETE SET NULL,
  actor_kind TEXT NOT NULL DEFAULT 'system' CHECK (actor_kind IN ('user', 'agent', 'system', 'import')),
  actor_label TEXT,
  runtime_name TEXT,
  task_id TEXT,
  payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_agent_memory_audit_scope
  ON public.agent_memory_audit_events (workspace_id, project_id, created_at DESC);

CREATE OR REPLACE FUNCTION public.agent_memories_set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_agent_memories_updated_at ON public.agent_memories;
CREATE TRIGGER trg_agent_memories_updated_at
  BEFORE UPDATE ON public.agent_memories
  FOR EACH ROW EXECUTE FUNCTION public.agent_memories_set_updated_at();

CREATE OR REPLACE FUNCTION public.agent_memory_hash_text(p_content TEXT)
RETURNS TEXT
LANGUAGE plpgsql
IMMUTABLE
AS $$
BEGIN
  RETURN encode(sha256(convert_to(lower(trim(regexp_replace(coalesce(p_content, ''), '\s+', ' ', 'g'))), 'UTF8')), 'hex');
END;
$$;

ALTER TABLE public.agent_memories ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.agent_memory_source_refs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.agent_memory_artifacts ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.agent_memory_relations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.agent_memory_review_actions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.agent_memory_recall_traces ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.agent_memory_recall_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.agent_memory_audit_events ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS agent_memories_service_role_all ON public.agent_memories;
CREATE POLICY agent_memories_service_role_all ON public.agent_memories
  FOR ALL TO service_role USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS agent_memory_source_refs_service_role_all ON public.agent_memory_source_refs;
CREATE POLICY agent_memory_source_refs_service_role_all ON public.agent_memory_source_refs
  FOR ALL TO service_role USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS agent_memory_artifacts_service_role_all ON public.agent_memory_artifacts;
CREATE POLICY agent_memory_artifacts_service_role_all ON public.agent_memory_artifacts
  FOR ALL TO service_role USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS agent_memory_relations_service_role_all ON public.agent_memory_relations;
CREATE POLICY agent_memory_relations_service_role_all ON public.agent_memory_relations
  FOR ALL TO service_role USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS agent_memory_review_actions_service_role_all ON public.agent_memory_review_actions;
CREATE POLICY agent_memory_review_actions_service_role_all ON public.agent_memory_review_actions
  FOR ALL TO service_role USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS agent_memory_recall_traces_service_role_all ON public.agent_memory_recall_traces;
CREATE POLICY agent_memory_recall_traces_service_role_all ON public.agent_memory_recall_traces
  FOR ALL TO service_role USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS agent_memory_recall_items_service_role_all ON public.agent_memory_recall_items;
CREATE POLICY agent_memory_recall_items_service_role_all ON public.agent_memory_recall_items
  FOR ALL TO service_role USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS agent_memory_audit_events_service_role_all ON public.agent_memory_audit_events;
CREATE POLICY agent_memory_audit_events_service_role_all ON public.agent_memory_audit_events
  FOR ALL TO service_role USING (true) WITH CHECK (true);

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.agent_memories TO service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.agent_memory_source_refs TO service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.agent_memory_artifacts TO service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.agent_memory_relations TO service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.agent_memory_review_actions TO service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.agent_memory_recall_traces TO service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.agent_memory_recall_items TO service_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.agent_memory_audit_events TO service_role;
GRANT EXECUTE ON FUNCTION public.agent_memory_hash_text(TEXT) TO service_role;

NOTIFY pgrst, 'reload schema';
