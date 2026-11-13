-- Memory layer, first tables (session 8e3a65ec, 2026-11-13).
-- What it solves: the vault's JSONL (05_episodic_logs/observations/*.jsonl) is the source of truth that git carries
-- to every device; these tables are its queryable mirror, plus the enterprise-wide SHA-256 ledger (OB1 pattern) and a
-- slot for EmbeddingGemma 2 vectors (768 dimensions; Matryoshka sizes 512/256/128 fit by truncation).
-- Row level security is on with no policies: only the service role (server-side scripts) can read or write.

create extension if not exists vector;

create table if not exists public.mem_observations (
  id          text primary key check (id ~ '^[0-9a-f]{64}$'),   -- sha256 of the record body, same as the JSONL id
  kind        text not null default 'observation',             -- observation | summary
  project     text not null,
  session     text,
  type        text,                                             -- decision, fact, finding, bugfix, ... summary
  created_at  timestamptz not null,
  title       text,
  subtitle    text,
  narrative   text,
  text        text,
  facts       jsonb not null default '[]',
  concepts    jsonb not null default '[]',
  files       jsonb not null default '[]',
  source      text,
  raw         jsonb not null,                                   -- the JSONL line exactly as stored in git
  embedding   vector(768),                                      -- EmbeddingGemma 2, filled later
  search      tsvector generated always as (
                to_tsvector('english', coalesce(title,'') || ' ' || coalesce(subtitle,'') || ' ' ||
                coalesce(narrative,'') || ' ' || coalesce(text,''))) stored,
  loaded_at   timestamptz not null default now()
);
create index if not exists mem_observations_project on public.mem_observations (project, created_at desc);
create index if not exists mem_observations_search on public.mem_observations using gin (search);

create table if not exists public.mem_cas (
  sha256      text primary key check (sha256 ~ '^[0-9a-f]{64}$'),
  label       text,                                             -- what the hash is of: claim, file path, observation
  repo        text,                                             -- per-repo rows and enterprise-wide in one table
  bytes       bigint,
  first_seen  timestamptz not null default now()
);

alter table public.mem_observations enable row level security;
alter table public.mem_cas enable row level security;
