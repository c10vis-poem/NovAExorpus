
You need a **source-of-truth corpus pipeline**, not a generic “second brain.” Build a versioned working vault that compiles raw assets into durable knowledge, then exposes separate retrieval views for Claude Code, local models, and other devices.

## Recommendation document

### Objective

Create one **canonical repository vault** from your existing documents, notes, code, conversations, exports, logs, and research. It must support:

- Incremental corpus intake without losing originals.
- LLM-assisted extraction into a navigable open Markdown wiki.
- Multi-vector retrieval without allowing any vector store to become the source of truth.
- Explicit architecture/decision records.
- Multi-device replication and controlled local access.
- A future RLVR training/evaluation pipeline based on verified evidence and task outcomes.
- Claude Code behavior that is constrained by executable workflow rules—not hopeful prose in one giant `CLAUDE.md`.

The governing rule:

> **Raw assets are immutable evidence. The Markdown vault is the human/auditable compiled layer. Indexes and vector stores are rebuildable derivatives.**

Karpathy’s wiki pattern supports this general separation: raw sources are ingested, then an LLM incrementally compiles and maintains an interlinked Markdown wiki rather than retrieving and re-synthesizing everything from raw data each time.[^4_1][^4_2]

______________________________________________________________________

## Architecture

```text
                         ┌──────────────────────┐
                         │  Raw source corpus   │
                         │ PDFs / MD / repos /  │
                         │ chats / logs / media │
                         └──────────┬───────────┘
                                    │
                              manifest + hashes
                                    │
                         ┌──────────▼───────────┐
                         │  Intake / staging    │
                         │ normalize, OCR,      │
                         │ transcript, classify │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
      ┌──────────▼─────────┐ ┌──────▼─────────┐ ┌─────▼────────────┐
      │ Compiled Markdown  │ │ Chunk registry  │ │ Extraction ledger │
      │ wiki / decisions   │ │ canonical spans │ │ claims + evidence │
      └──────────┬─────────┘ └──────┬─────────┘ └─────┬────────────┘
                 │                  │                 │
                 └──────────────────┼─────────────────┘
                                    │
                   ┌────────────────▼─────────────────┐
                   │ Rebuildable retrieval derivatives │
                   │ lexical + dense + late interaction│
                   │ metadata + graph + reranking      │
                   └────────────────┬─────────────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
     ┌───────▼────────┐   ┌─────────▼────────┐   ┌────────▼─────────┐
     │ Claude Code    │   │ Local edge model │   │ Evaluation / RLVR │
     │ skills/agents  │   │ retrieval client │   │ trajectories/data │
     └────────────────┘   └──────────────────┘   └──────────────────┘
```

Do **not** make Obsidian, a database, an embedding model, or a cloud drive your primary truth layer. Use Git-managed files and manifests as the durable core. Obsidian is a viewer/editor for the Markdown layer; retrieval databases are caches that can be deleted and rebuilt.

______________________________________________________________________

## Repository layout

Start with this exact logical separation:

```text
master-corpus/
├── README.md
├── CLAUDE.md
├── .gitignore
├── .claude/
│   ├── agents/
│   ├── skills/
│   ├── hooks/
│   └── settings.json
│
├── 00-governance/
│   ├── architecture-principles.md
│   ├── data-classification.md
│   ├── source-policy.md
│   ├── naming-conventions.md
│   ├── retrieval-policy.md
│   └── device-access-policy.md
│
├── 01-inbox/
│   ├── unprocessed/
│   ├── needs-review/
│   └── rejected/
│
├── 02-raw/
│   ├── documents/
│   ├── conversations/
│   ├── repositories/
│   ├── code-snippets/
│   ├── logs/
│   ├── media/
│   └── exports/
│
├── 03-normalized/
│   ├── markdown/
│   ├── transcripts/
│   ├── ocr/
│   └── extracted-text/
│
├── 04-registry/
│   ├── sources.jsonl
│   ├── chunks.jsonl
│   ├── entities.jsonl
│   ├── claims.jsonl
│   ├── relationships.jsonl
│   └── ingestion-log.jsonl
│
├── 05-wiki/
│   ├── index.md
│   ├── domains/
│   ├── systems/
│   ├── projects/
│   ├── concepts/
│   ├── decisions/
│   ├── experiments/
│   ├── devices/
│   ├── tools/
│   ├── models/
│   ├── procedures/
│   ├── open-questions/
│   └── sources/
│
├── 06-retrieval/
│   ├── lexical/
│   ├── dense/
│   ├── multivector/
│   ├── graph/
│   ├── metadata/
│   └── manifests/
│
├── 07-evals/
│   ├── query-set/
│   ├── relevance-judgments/
│   ├── extraction-tests/
│   ├── retrieval-tests/
│   ├── agent-trajectories/
│   └── reports/
│
├── 08-training/
│   ├── approved-examples/
│   ├── preference-pairs/
│   ├── reward-spec/
│   └── exclusions/
│
├── 09-tools/
│   ├── ingest/
│   ├── normalize/
│   ├── extract/
│   ├── index/
│   ├── query/
│   ├── eval/
│   └── sync/
│
└── 10-exports/
    ├── device-bundles/
    ├── read-only-context-packs/
    └── reports/
```

The number prefixes are intentional. They make the lifecycle obvious and prevent the working wiki, raw artifacts, indexes, and generated exports from blurring together.

______________________________________________________________________

## Data rules

### Raw sources

Everything first lands in `01-inbox/unprocessed/`.

Each source is assigned:

- Stable `source_id`.
- SHA-256 or BLAKE3 checksum.
- Ingestion timestamp.
- Original filename and original location.
- Source type: document, repository, issue thread, conversation, terminal log, dataset, audio, image, video, and so on.
- Sensitivity classification.
- Processing status.
- Parent/derived relationship if it was exported or converted from another asset.

Never let an agent silently rewrite files in `02-raw/`. It may create normalized derivatives in `03-normalized/`, but originals remain untouched.

### Canonical chunks

Your chunk registry is the bridge between every retrieval method.

Every normalized source is split into stable spans with IDs such as:

```text
chunk:src_20260924_a81f:000142
```

Each chunk records:

```json
{
  "chunk_id": "chunk:src_20260924_a81f:000142",
  "source_id": "src_20260924_a81f",
  "normalized_path": "03-normalized/markdown/example.md",
  "start_char": 12840,
  "end_char": 15812,
  "heading_path": ["Architecture", "Retrieval"],
  "content_hash": "blake3:...",
  "created_at": "2026-09-24T...",
  "sensitivity": "private",
  "language": "en"
}
```

Every embedding, lexical posting, graph edge, claim, wiki reference, evaluation item, and RLVR example should refer to **these stable chunk IDs**. That prevents index drift and lets you rebuild any retrieval backend without re-deciding what an “evidence unit” is.

### Claims and decisions

Do not write free-floating “facts” into a wiki page with no evidence.

Use claim records:

```yaml
id: claim:retrieval:00017
statement: "The canonical retrieval unit is a stable normalized chunk."
status: accepted
confidence: high
evidence:
  - chunk:src_20260924_a81f:000142
decision: decision:00004
created: 2026-09-24
supersedes: []
```

Use separate decision records for choices you need to revisit:

```yaml
id: decision:00004
title: "Use file-first canonical storage with rebuildable indexes"
status: proposed
owner: user
date: 2026-09-24
decision: "..."
alternatives:
  - "Database-first corpus"
  - "Vector-store-first corpus"
criteria:
  - auditability
  - offline/local usability
  - multi-device synchronization
  - rebuildability
evidence: []
review_trigger:
  - "Corpus exceeds local storage limits"
  - "Concurrent editing requires transaction semantics"
```

This is what prevents an LLM from treating its own prior output as unquestionable truth.

______________________________________________________________________

## Multi-vector retrieval

Do not begin by deploying five databases. First establish one chunk registry, one evaluation set, and one retrieval contract. Then add retrieval lanes one at a time.

Your retrieval layer should contain these independent signals:


| Retrieval lane | What it finds well | Store |
| :-- | :-- | :-- |
| Lexical/BM25 | Exact terms, filenames, APIs, error strings, identifiers, commands | Local lexical index |
| Dense embeddings | Semantic similarity across paraphrases | Vector index |
| Multi-vector / late interaction | Long technical chunks where token-level matches matter | ColBERT-style or equivalent index |
| Metadata filtering | Device, project, date, sensitivity, source type, status | SQLite/DuckDB or sidecar metadata |
| Knowledge graph | Explicit entities, decisions, dependencies, contradictions | JSONL/SQLite/graph derivative |
| Reranker | Reorders candidate chunks using the actual question | Local or remote cross-encoder |

A query flow:

```text
query
  → normalize / classify intent
  → apply access + device filters
  → retrieve lexical top-K
  → retrieve dense top-K
  → retrieve multi-vector top-K
  → graph-expand only from high-confidence entities
  → reciprocal-rank fusion
  → rerank the merged evidence set
  → return cited chunks + compiled wiki context
  → answer or execute only within authorization policy
```


### Correct order of implementation

1. **Lexical search first**: It is fast, local, debuggable, and catches exact technical tokens that embeddings miss.
2. **Dense retrieval second**: Adds semantic recall.
3. **Reranking third**: This usually has more impact than prematurely adding another vector store.
4. **Multi-vector retrieval fourth**: Add only after you can prove dense + lexical retrieval misses relevant technical spans.
5. **Graph expansion last**: Graphs are useful for known relationships, not as an excuse to infer relationships without evidence.

The retrieval result must return provenance, not just text:

```json
{
  "chunk_id": "chunk:src_20260924_a81f:000142",
  "score": 0.842,
  "retrieval_lanes": ["bm25", "dense", "reranked"],
  "source_path": "03-normalized/markdown/...",
  "heading_path": ["Architecture", "Retrieval"],
  "sensitivity": "private"
}
```

No agent should use uncited corpus output to create a decision, a training label, or an irreversible action.

______________________________________________________________________

## Wiki layer

Use the wiki for synthesis, navigation, and decisions—not as a duplicate archive.

Recommended page types:

```text
system
project
device
model
runtime
tool
concept
procedure
decision
experiment
incident
source
open-question
```

Every wiki page should have frontmatter:

```yaml
---
id: system:corpus-vault
type: system
status: active
updated: 2026-09-24
confidence: mixed
source_chunks:
  - chunk:src_...
related:
  - "[[Multi-vector Retrieval]]"
  - "[[Corpus Intake Pipeline]]"
review_after: 2026-10-24
---
```

Use three content zones:

1. **Current compiled view**: What is currently believed or decided.
2. **Evidence**: Linked source chunks and source pages.
3. **Change/conflict history**: What changed, what conflicts, what remains unresolved.

That makes the wiki suitable for later fine-tuning or RLVR data review because you can distinguish supported policy from model-generated prose.

______________________________________________________________________

## Claude Code control plane

A single long `CLAUDE.md` is insufficient. Claude Code skills are filesystem-based directories containing a `SKILL.md`; they can live in `.claude/skills/` at the project level or `~/.claude/skills/` for a personal installation. The YAML description helps Claude choose a skill, while the instruction body governs the task when loaded.[^4_3][^4_4]

Use the following control layers:


| Layer | Role | Put here |
| :-- | :-- | :-- |
| `CLAUDE.md` | Short global repository contract | Non-negotiable principles, commands, forbidden actions |
| Skills | Reusable procedures invoked by task | Intake, extraction, wiki update, index build, query, evaluation |
| Subagents | Isolated specialized work | Extractor, librarian, retrieval evaluator, architecture reviewer |
| Hooks | Deterministic enforcement | Block raw-file edits, require manifests, run validation |
| Scripts | Actual repeatable operations | Hashing, conversion, chunking, indexing, linting, export |
| CI | Regression protection | Schema validation, broken links, citation coverage, eval baseline |

Skills are good for procedures, but do **not** trust them for non-negotiable enforcement: Claude can decide whether a skill is relevant unless you invoke it explicitly. Hooks run on configured lifecycle events, making them appropriate for guardrails such as blocking writes to immutable raw directories or requiring a manifest update before accepting an ingestion result.[^4_4][^4_5]

### Core `CLAUDE.md` contract

Keep it short and hard-edged:

```markdown
# Corpus Vault Contract

- `02-raw/` is immutable. Never modify, rename, or delete raw sources.
- All new sources enter through `01-inbox/` and must receive a manifest record.
- Every derived artifact must preserve `source_id` and source checksum.
- Do not create unsupported wiki claims. Cite `chunk_id` values.
- Do not update an accepted decision without creating a change record.
- Treat `06-retrieval/` as rebuildable output; do not hand-edit indexes.
- Never add private data to `08-training/` without explicit approval.
- Before finishing: run the relevant validation command and report modified paths.
- Ask before destructive operations, remote uploads, broad corpus moves, or index replacement.
```


### Required skills

```text
.claude/skills/
├── corpus-intake/
├── source-normalization/
├── evidence-extraction/
├── wiki-librarian/
├── decision-record/
├── retrieval-index/
├── retrieval-eval/
├── corpus-query/
├── rlvr-dataset-curator/
└── device-context-export/
```

Each skill should be narrow. Example:

```yaml
---
name: corpus-intake
description: Intake a new file or directory into the master corpus. Use for adding documents, source exports, repositories, transcripts, logs, or media. Preserves originals, creates a manifest record, hashes assets, and never directly edits the wiki.
---
```

Do not make an “all knowing master skill.” It becomes untestable, bloated, and weak at routing.

### Required hooks

At minimum:

- **PreToolUse**: Block write/delete actions under `02-raw/`.
- **PreToolUse**: Block writes to `06-retrieval/` except approved index scripts.
- **PostToolUse**: After an approved intake, require source manifest validation.
- **Stop**: Run lightweight linting and report unresolved failures.
- **Pre-commit/CI**: Validate JSONL schemas, frontmatter, chunk references, link integrity, duplicate IDs, and citation coverage.

Skill-scoped hooks can be registered when a skill is invoked and remain active for the session; use `once: true` only for one-time initialization checks.[^4_5][^4_4]

______________________________________________________________________

## RLVR preparation

Do not begin with “training.” First produce a trustworthy, versioned evaluation and feedback substrate.

Your RLVR-like loop should be:

```text
task request
  → retrieval plan
  → evidence selection
  → agent answer/action
  → deterministic checks
  → human accept/reject/correction
  → reward record
  → curated training/evaluation example
```

Store the full trajectory:

```json
{
  "trajectory_id": "traj:000001",
  "task": "Find the accepted corpus-storage architecture and explain why.",
  "retrieved_chunks": [
    "chunk:...",
    "chunk:..."
  ],
  "agent_output": "...",
  "tool_calls": [],
  "verifiers": {
    "all_citations_resolve": true,
    "decision_status_matches": true,
    "forbidden_paths_untouched": true
  },
  "human_verdict": "accepted",
  "reward": 1.0,
  "notes": "Answer cited accepted ADR and did not invent a storage backend."
}
```

Use **verifiable rewards**, not “the model sounded good” rewards:

- Every cited `chunk_id` resolves.
- The cited evidence actually contains the claimed support.
- No invented files, commands, paths, IDs, or device assumptions.
- Required schema and lint checks pass.
- Raw files remain unchanged.
- The answer respects sensitivity/access labels.
- The plan uses the required retrieval lanes.
- A human accepts, rejects, or corrects the output.

Keep unreviewed model output out of `08-training/`. Put it in a quarantine/staging area until you approve it.

______________________________________________________________________

## Multi-device strategy

The repository is canonical; devices consume a role-specific view.


| Device role | Local contents | Write access |
| :-- | :-- | :-- |
| Primary control/development host | Full vault, raw assets, indexes, scripts, evals | Full, with Git history |
| Mobile edge device | Curated context bundles, selected indexes, retrieval client, task queue | Usually read-only corpus; limited append-only capture inbox |
| Secondary device | Read-only wiki snapshot or specific project bundle | No direct canonical writes |
| Cloud/remote compute | Explicitly exported encrypted/minimized bundle only | No access unless deliberately provisioned |

Use **exports**, not ad hoc copies:

```text
10-exports/device-bundles/
├── mobile-core-context/
├── retrieval-lite/
├── project-specific/
└── offline-emergency/
```

Each bundle needs:

- Export manifest.
- Corpus/vault revision.
- Included sources/chunks.
- Model/index versions.
- Sensitivity level.
- Expiry or review date.
- Integrity hashes.

Mobile capture should go only to `01-inbox/` through a controlled sync path. Do not allow multiple devices to edit compiled wiki pages independently unless you are prepared to resolve Git conflicts and enforce a merge policy.

______________________________________________________________________

## First decisions to lock now

Create ADRs for these before mass ingestion:

1. **Canonical storage**: Git-managed filesystem repository plus immutable raw assets.
2. **Chunk identity**: Stable chunk IDs derived from source ID plus ordinal or content-aware range.
3. **Metadata authority**: JSONL or SQLite registry, with schema versioning.
4. **Embedding policy**: Which embedding model, dimensions, normalization, and model-version metadata every vector must store.
5. **Retrieval fusion**: Start with BM25 + dense; use reciprocal-rank fusion; add reranking before multi-vector.
6. **Access model**: What data can exist on mobile, remote, or cloud nodes.
7. **Training boundary**: Nothing moves into RLVR/training sets without explicit approval and provenance.
8. **Sync policy**: One canonical write branch; devices submit capture artifacts, not uncontrolled wiki edits.
9. **Conflict policy**: Preserve contradictions as records; never overwrite an earlier claim without marking it superseded or disputed.
10. **Acceptance tests**: A small manually labeled query set before you claim retrieval works.

______________________________________________________________________

## Build order

### Phase 1: Establish control

- Create the repository skeleton.
- Write `00-governance/architecture-principles.md`.
- Create the first ADRs listed above.
- Add the short `CLAUDE.md`.
- Add immutable-raw and manifest-validation hooks.
- Build a manifest generator and hashing command.

**Exit condition:** You can intake a source without ambiguity, and no agent can casually alter an original asset.

### Phase 2: Normalize and register

- Ingest a small representative sample—roughly 20–50 sources, not the whole corpus.
- Convert content into normalized Markdown/text derivatives.
- Create source and chunk registries.
- Define chunking rules for prose, code, logs, conversations, and transcripts.
- Validate stable IDs and provenance.

**Exit condition:** Any compiled statement can be traced to an original source and location.

### Phase 3: Compile wiki

- Create pages only for recurring entities, systems, projects, concepts, procedures, and decisions.
- Build source pages first; then synthesize shared concepts.
- Require evidence links for significant claims.
- Add a decision log and open-question queue.
- Use an extraction agent and a separate librarian/reviewer agent; do not let one agent both generate and blindly approve its own synthesis.

**Exit condition:** You can answer core architecture questions from a small, linked compiled wiki and inspect the evidence.

### Phase 4: Retrieval baseline

- Implement BM25/lexical retrieval over canonical chunks.
- Add dense embeddings.
- Use metadata filters.
- Fuse results and add a reranker.
- Create 30–100 realistic evaluation queries based on actual questions you expect to ask.
- Score recall and citation quality before expanding complexity.

**Exit condition:** You can prove that retrieval finds the correct supporting chunks better than browsing manually.

### Phase 5: Multi-vector and graph

- Add a late-interaction/multi-vector index only if evaluation shows a real recall or precision gain.
- Add graph traversal for decisions, dependencies, and entity relationships.
- Keep each derivative indexed against the same canonical chunk IDs.
- Re-run the same eval set and compare metrics.

**Exit condition:** Each added layer demonstrates a measurable gain and does not break reproducibility.

### Phase 6: RLVR/evaluation loop

- Log agent trajectories.
- Add deterministic verifiers.
- Record your accept/reject/correction signals.
- Curate only high-confidence, permissioned examples.
- Version the reward specification and test it like code.

**Exit condition:** You have a clean evaluation set and reward records before considering any training run.

______________________________________________________________________

## Bottom line

Build the **vault first**, the **retrieval contract second**, and the **training loop last**.

Your first concrete deliverable should not be a vector database or a giant generated wiki. It should be a small but strict corpus repository where every source is immutable, every chunk is stable, every synthesized claim has evidence, every index is rebuildable, and Claude Code is prevented from bypassing the pipeline. Claude Code’s Skills, subagents, and hooks can support that division of labor, but deterministic enforcement belongs in hooks/scripts/CI—not natural-language instructions alone.[^4_3][^4_4][^4_5]

<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15][^4_16][^4_17][^4_18][^4_19][^4_20][^4_21][^4_22][^4_23][^4_24][^4_25][^4_6][^4_7][^4_8][^4_9]</span>

<div align="center">⁂</div>

[^4_1]: https://x.com/karpathy/status/2039805659525644595

[^4_2]: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

[^4_3]: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

[^4_4]: https://code.claude.com/docs/en/skills

[^4_5]: https://code.claude.com/docs/en/hooks

[^4_6]: https://academy.claude.com/courses/introduction-to-agent-skills/what-are-skills

[^4_7]: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

[^4_8]: https://anthropic.skilljar.com/introduction-to-subagents

[^4_9]: https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a

[^4_10]: https://kenhuangus.substack.com/p/what-andrej-karpathy-got-right-how

[^4_11]: https://hidekazu-konishi.com/entry/claude_code_skills_complete_guide.html

[^4_12]: https://dev.to/kenimo49/claude-code-hooks-vs-skills-vs-subagents-three-ways-to-extend-the-agent-and-when-each-backfires-1728

[^4_13]: projects.ai.local_deployment

[^4_14]: tools.devices.razr_8_elite

[^4_15]: projects.ai.local_deployment.turboquant

[^4_16]: projects.ai.claude_interface

[^4_17]: projects.ai.razor_pie.architecture

[^4_18]: projects.ai.edge_computing_stack

[^4_19]: https://www.perplexity.ai/search/3bb29bcf-27b8-4698-aee4-e4b18c145794

[^4_20]: https://www.perplexity.ai/search/7c627d0f-94ee-4c44-a427-e5634ca63407

[^4_21]: https://www.perplexity.ai/search/b5481261-bc9f-44b2-8230-ceceaa4bb8b2

[^4_22]: https://www.perplexity.ai/search/b2efc26f-ea98-41f0-a815-4fed1d92cca3

[^4_23]: https://github.com/alirezarezvani/claude-skills/blob/main/CLAUDE.md

[^4_24]: https://www.kunalganglani.com/blog/llm-wiki-karpathy-local-knowledge-base

[^4_25]: https://theaioperator.io/p/i-rebuilt-karpathys-llm-wiki-heres


---

# How does this document vary from your input and what edits to the recommended workflows do i need to implement

Your uploaded proposal is **far more concrete** than my prior recommendation on vault navigation, ontology, harness separation, and operating modes. My prior document is stronger on provenance, retrieval evaluation, and preventing index/wiki drift.

You should keep the proposal’s `MAP.md` + `manifest.jsonl` model, but change several workflow rules before treating it as canonical.[^5_1]

## Main differences

| Area | Your proposal | My prior recommendation | What to adopt |
| :-- | :-- | :-- | :-- |
| Navigation | Every tier has bounded `MAP.md`; agents read it first, then query manifest | One top-level index plus registries | **Use your model.** It is better for agent orientation and token control. |
| Machine registry | File-level `manifest.jsonl` with hashes, tags, summaries, entities | Source, chunk, claim, entity, relation registries | Keep the manifest, but add **chunk, claim, and relation registries**. File-level indexing alone is not enough for evidence retrieval or RLVR. |
| Wiki organization | Rich, faceted master wiki: vendors, weights, runtimes, engines, harnesses, agents, protocols, projects, memory, etc. | Simpler content-type-first wiki | Use the proposal’s faceted tree, but avoid duplicating the same primary content under several branches. Use canonical pages plus MOCs/indexes. |
| Retrieval | Manifest filter → FAISS semantic lookup → chunks → recursive KAG loop | BM25 + dense + fusion + reranker; multi-vector later; graph last | Replace the proposal’s dense-only retrieval core with a **hybrid retrieval baseline**. |
| Evidence model | Per-file provenance; wiki is organized knowledge | Stable source/chunk IDs; every important claim cites evidence | Add stable evidence IDs. This is the biggest missing piece. |
| Agent control | Strong first-move directive, harness coexistence, hot-swap interfaces | Skills, subagents, hooks, scripts, CI | Merge both. Instructions define workflow; hooks/scripts enforce it. |
| Memory architecture | OmniRoute extracts every request/response into downstream memory stores | Explicit raw → compiled → index → eval/training separation | Narrow OmniRoute capture; do not auto-promote every interaction into memory. |
| RLVR | Reasoning Bank + trajectories + later GCP loop | Evaluation-first, deterministic verification, reviewed training curation | Use my gating rules. The proposal needs a formal data-quality and approval boundary. |
| Multi-device | Alpha/Beta/Gamma/Delta node architecture and role separation | Canonical host plus generated device bundles | Keep node roles, but use **signed/versioned bundles** and one canonical writer. |
| Hot swapping | Four common interfaces: model, memory, tools, output | Role-specific exports and agent contracts | Keep the interface idea, but add versioned schemas and capability declarations. |

The proposal correctly distinguishes `MAP.md` as bounded orientation/navigation and `manifest.jsonl` as a queryable machine registry; it explicitly prohibits loading the full manifest into model context or editing it manually. That should become the standard agent entry procedure.[^5_1]

## Edits required

### 1. Add an evidence layer

Your proposed `manifest.jsonl` is per-file. That is necessary but insufficient.

A file can contain many unrelated assertions; a vector hit on a file does not prove an individual claim. Add this below each tier’s manifest or in a central registry:

```text
04-registry/
├── sources.jsonl
├── chunks.jsonl
├── claims.jsonl
├── relations.jsonl
├── decisions.jsonl
└── ingestion-log.jsonl
```

Minimum requirements:

- `source_id`: immutable identity for an original asset.
- `chunk_id`: stable retrieval unit tied to source ID, normalized content, offsets, heading path, and content hash.
- `claim_id`: a material assertion with one or more supporting `chunk_id`s.
- `decision_id`: architecture choice, alternatives, status, rationale, evidence, owner, and review trigger.
- `relation_id`: explicit graph edge, such as `uses`, `runs_on`, `depends_on`, `supersedes`, `contradicts`, or `implements`.

Example:

```json
{
  "claim_id": "claim:memory:000017",
  "statement": "The retrieval corpus uses immutable source assets and rebuildable indexes.",
  "status": "accepted",
  "confidence": "high",
  "evidence": [
    "chunk:src:architecture:000042"
  ],
  "decision_id": "adr:00004",
  "created_at": "2026-09-24"
}
```

**Workflow edit:** A Claude Code wiki agent cannot write an “accepted” technical claim unless it includes at least one resolved `chunk_id`. Unsupported material goes to `open-questions/`, `hypotheses/`, or `needs-verification`, never silently into canonical prose.

Your proposal already tracks per-file hashes and provenance. This extends it from file cataloging into an auditable knowledge system.[^5_1]

______________________________________________________________________

### 2. Split raw, normalized, compiled, and derived assets harder

The proposal’s five-plus-one tier model is generally sound:

```text
01_raw_sources/
02_wiki_md/
03_recall_cache/
04_skills_runtime/
05_episodic_logs/
```

But revise it so that raw material and generated/normalized text are never conflated.

Recommended adjustment:

```text
data_vault/
├── 00_governance/
├── 01_raw_sources/          # Immutable originals only
├── 02_normalized_sources/   # OCR, transcripts, Markdown conversions
├── 03_compiled_wiki/        # Human/agent maintained knowledge pages
├── 04_registry/             # Manifest, chunks, claims, decisions, relations
├── 05_retrieval_derivatives/# BM25, embeddings, multi-vector, graph outputs
├── 06_skills_runtime/       # Skills, tools, prompt templates, schemas
├── 07_episodic_logs/        # Append-only trajectories/events/costs
├── 08_evals/                # Query set, labels, verifier results
├── 09_training_candidates/  # Quarantined/approved RLVR examples
└── 10_exports/              # Role/device-specific bundles
```

The critical correction is renaming or replacing `03_recall_cache/`. Calling an index a “cache” encourages treating it as temporary or informal, even though it is central to retrieval. It is a **derived retrieval layer**, regenerated from canonical normalized content plus the chunk registry.

**Workflow edit:** No human or agent directly edits:

```text
05_retrieval_derivatives/
manifest.jsonl
chunks.jsonl
embeddings/
faiss/
bm25/
graph/
```

Only reproducible scripts can generate them.

______________________________________________________________________

### 3. Fix the retrieval pipeline

The proposal uses:

```text
MAP.md → manifest filter → FAISS similarity → chunk load → KAG recursion
```

That is workable, but too semantic-vector-dependent for your corpus. Exact technical terms matter: model IDs, package names, Android APIs, error strings, hardware names, paths, commits, ports, environment variables, and script names.

Replace its retrieval section with:

```text
1. Read root MAP.md for orientation.
2. Determine task class and access constraints.
3. Query manifest metadata to select plausible tiers/scopes.
4. Retrieve canonical chunk candidates through:
   - lexical/BM25 search,
   - dense embedding search,
   - metadata filters,
   - optionally known graph links.
5. Merge using reciprocal-rank fusion.
6. Rerank the merged candidate set.
7. Load only top evidence chunks and linked compiled-wiki pages.
8. If evidence is insufficient, perform bounded KAG recursion.
9. Return the answer/action with source and chunk provenance.
```


### Retrieval lanes to build in order

1. **Manifest + lexical search.**
2. **Dense embeddings.**
3. **Fusion and reranker.**
4. **Evaluation harness.**
5. **Multi-vector/late interaction retrieval.**
6. **Graph expansion.**

Do not start with multi-vector retrieval just because it is the target architecture. First prove that BM25+dense+rering fails on your real queries.

**Workflow edit:** Define a fixed benchmark before adding retrieval layers:

```text
08_evals/query-set/
├── architecture-questions.jsonl
├── device-runtime-questions.jsonl
├── code-and-script-questions.jsonl
├── decision-retrieval-questions.jsonl
└── failure-analysis-questions.jsonl
```

For each query, record expected source/chunk IDs, not only a natural-language “good answer.” That gives you measurable recall@K, evidence precision, and citation validity.

The proposal’s bounded recursive KAG loop is worth keeping, but it needs a hard stop: maximum rounds, maximum retrieved tokens, and a required “insufficient evidence” result rather than infinite scavenging.[^5_1]

______________________________________________________________________

### 4. Prevent ontology duplication

Your proposal gives first-class cuts to vendors, weights, runtimes, engines, harnesses, agents, protocols, projects, entities, architectures, memory components, and references. That is good as an ontology, but it becomes a duplication trap.

Example: a Qwen deployment could appear under:

```text
vendors/qualcomm/
weights/
runtimes/qairt/
engines/genie-x-engine/
harnesses/prime-agent/
agents/query-9b/
entities/nodes/
architectures/
memory-subsystem/
projects/
```

Do not duplicate the full content in all ten places.

Use one canonical object page, then cross-cutting views:

```text
03_compiled_wiki/
├── objects/
│   ├── models/qwen-3.5-9b.md
│   ├── runtimes/qairt.md
│   ├── engines/genie-x.md
│   ├── harnesses/prime-agent.md
│   ├── agents/query-9b.md
│   └── nodes/alpha.md
├── decisions/
├── runbooks/
├── projects/
└── mocs/
    ├── by-vendor/
    ├── by-node/
    ├── by-project/
    ├── by-memory-layer/
    └── by-agent/
```

Then a vendor page is a MOC that links to canonical object pages:

```markdown
# Qualcomm

## Runtime
- [[QAIRT]]

## Hardware targets
- [[Alpha Node]]

## Model bundles
- [[Qwen 3.5 0.8B QAI Hub Bundle]]

## Related decisions
- [[ADR-0007 NPU Runtime Selection]]
```

**Workflow edit:** Define a canonical-location field in every wiki file:

```yaml
canonical: true
aliases:
  - "[[vendors/qualcomm/qairt]]"
  - "[[runtimes/qairt]]"
```

Or simpler: a page is canonical only in one folder; every other view is links/indexes only.

______________________________________________________________________

### 5. Correct the OmniRoute memory workflow

The proposal states OmniRoute should intercept **every** prompt/response, classify it, and extract memory-worthy information into `mem0`, OB1, and a Reasoning Bank.[^5_1]

That is too broad by default. It will generate:

- Repeated low-value memories.
- Sensitive-data propagation.
- Model-generated contamination.
- Expensive extraction workloads.
- Contradictory “facts” from speculative conversation.
- Unclear consent and deletion boundaries.
- A training corpus full of weak trajectories.

Use a **capture → stage → verify → promote** pipeline instead:

```text
Prompt/response/tool trace
  → append-only event log
  → candidate extraction
  → classifier + policy filter
  → quarantine/staging
  → evidence check / dedupe / conflict check
  → human or rule-based approval
  → promotion to appropriate durable store
```

Make the stores semantically distinct:


| Store | What belongs there | What does not |
| :-- | :-- | :-- |
| Session state | Short-lived task context and resumable state | Durable facts or project decisions |
| Episodic log | Append-only prompts, outputs, actions, tool traces | Curated knowledge |
| Semantic/wiki store | Evidence-backed concepts, configurations, decisions | Raw chats or unverified model assertions |
| Retrieval index | Derived chunks/embeddings/lexical postings | Hand-authored facts |
| RLVR candidate store | Full evaluated trajectories with verifier outcomes | Every conversation |
| Training-approved set | Reviewed, legally/permission-cleared examples | Raw private logs by default |

**Workflow edit:** Only promote an extracted item to the compiled wiki or semantic store when it has:

- A source/trajectory ID.
- An evidence span or deterministic task result.
- A category.
- Confidence.
- A duplication/conflict check.
- An approval status.

Treat OmniRoute as an **event and routing gateway with optional extraction**, not an unconditional memory-authority daemon.

______________________________________________________________________

### 6. Make harness hot-swap safer

The proposal’s four-interface abstraction is good:

1. Model endpoint.
2. Memory interface.
3. Tool interface.
4. Output/trajectory interface.[^5_1]

Add two more:

5. **Identity/capability interface**: who is this harness/agent, which tools/models/data classifications it may use.
6. **Evaluation/policy interface**: required verifiers, allowed side effects, budget, task timeout, retry behavior.

Do not allow all harnesses to read/write the same memory stores directly. Give each a declared capability profile.

Example:

```yaml
agent_id: query-9b
harness: prime-agent
mode: sovereign-edge
permissions:
  corpus:
    read:
      - public
      - private-device-bundle
    write:
      - 01-inbox/capture
      - 07-episodic-logs
  tools:
    allowed:
      - retrieval.query
      - notes.capture
    denied:
      - shell.exec
      - git.push
      - cloud.frontier_call
memory:
  read:
    - device-context
  write:
    - episodic-staging
network:
  allowed: false
budget:
  max_tool_calls: 8
  max_retrieval_rounds: 3
```

**Workflow edit:** The shared output location should be append-only. A new harness may read a bounded, filtered handoff summary—not automatically hydrate every raw trajectory from a prior harness.

Also revise the claim that no RPC between harnesses is always desirable. Direct shared state is indeed bad, but a narrow **explicit handoff artifact** is better than forcing a new harness to reconstruct context from broad memory stores:

```text
handoffs/
└── handoff_2026-09-24T2240Z.json
```

It should contain task state, validated references, pending decisions, available tool permissions, and the last verified result—not a free-form conversation dump.

______________________________________________________________________

### 7. Tighten RLVR workflow

The proposal has the beginnings of an RLVR loop through Reasoning Bank, trajectories, auditors, and later GCP training. It needs quality gates before it becomes training input.[^5_1]

Use this progression:

```text
1. Agent execution trajectory
2. Deterministic verifier output
3. Human verdict where needed
4. Redacted/permission checked record
5. Candidate dataset
6. Curated approved dataset
7. Offline evaluation
8. Only then training experiment
9. Post-training regression and safety evaluation
```

Every trajectory record should include:

```json
{
  "trajectory_id": "traj:20260924:0001",
  "task_id": "task:retrieval:0042",
  "inputs": ["reference or redacted payload"],
  "retrieved_chunk_ids": [
    "chunk:src:00042",
    "chunk:src:00177"
  ],
  "tool_calls": [],
  "output": "reference or stored artifact hash",
  "verifier_results": {
    "citation_resolves": true,
    "schema_valid": true,
    "raw_assets_untouched": true,
    "task_complete": true
  },
  "human_verdict": "accepted",
  "reward": 1.0,
  "dataset_status": "candidate"
}
```

**Workflow edit:** Red Auditor and Cross-Auditor may contribute verdicts, but neither should be the sole source of truth for training labels. Audit agents can be wrong, biased, or operating from incomplete context. Use deterministic checks plus your review for high-value examples.

______________________________________________________________________

### 8. Add device bundle boundaries

Your proposal is clearer than mine about node roles, but it needs a hard distribution format.

Do not synchronize the whole master corpus to every device. Create declared bundles:

```text
10_exports/
├── alpha-edge/
│   ├── manifest.json
│   ├── wiki-slice/
│   ├── retrieval-index/
│   ├── allowed-tools.json
│   └── bundle.sig
├── beta-home/
├── gamma-control/
└── delta-cloud/
```

Each bundle must state:

- Vault commit/revision.
- Bundle generation time.
- Included source and chunk IDs.
- Included embeddings/index version.
- Sensitivity classification.
- Recipient node.
- Expiration/review date.
- Integrity hash/signature.

**Workflow edit:** Mobile or edge devices capture new material only into an append-only inbox or event log. Canonical wiki and architecture changes merge on the control host through Git review or an explicit approved sync process.

______________________________________________________________________

## What to preserve

Keep these parts of your document:

- The `MAP.md` first-read directive.
- Fractal per-tier maps and manifests.
- Terminology glossary for SDK/runtime/engine/harness/agent/model/protocol.
- First-class documentation categories for runtimes, weights, engines, harnesses, agents, protocols, tools, skills, and memory.
- Explicit multi-harness operating modes.
- The distinction between KV cache and durable SQL/semantic storage.
- Cost attribution as a continuous event-log attribute.
- Salvage-not-reference treatment for legacy code.
- The vendor visibility concern, especially where it helps actual navigation.

The proposal’s strongest operational rule is this sequence:

```text
MAP.md → scoped manifest query → specific file load
```

Retain it, but insert retrieval evidence as the middle layer:

```text
MAP.md
→ scoped manifest query
→ hybrid chunk retrieval
→ top evidence chunks + linked canonical wiki pages
→ bounded KAG recursion only if required
→ cited answer or explicit insufficiency
```

That preserves its token discipline while giving you actual multi-vector, auditable retrieval.[^5_1]

## What to remove or defer

- **Do not** create the giant full wiki tree before you have a working intake/manifest/chunk pipeline. Much of that tree will be empty or wrong.
- **Do not** treat FAISS alone as “multi-vector retrieval.”
- **Do not** capture and promote every OmniRoute exchange into memory automatically.
- **Do not** treat every agent trace as RLVR data.
- **Do not** allow every harness direct read/write access to all shared memory stores.
- **Do not** use vendor folders and functional folders as duplicate document homes.
- **Do not** make an agent read all manifests, all logs, or all wiki pages at startup.
- **Defer** a DeepSeek-specific harness, multi-vector late-interaction index, full graph traversal, and training runs until the corpus pipeline and retrieval eval suite exist.


## Revised workflow

This is the working sequence I would implement:

```text
A. Governance
   → Define terminology, IDs, sensitivity labels, write permissions, ADR format.

B. Ingest
   → Place original asset in inbox.
   → Hash and register it.
   → Move or copy immutable original to raw storage.
   → Create normalized derivative.
   → Generate source/chunk records.

C. Extract
   → Extract entities, claims, decisions, procedures, tools, and open questions.
   → Stage all outputs.
   → Verify evidence, deduplicate, detect conflicts.
   → Promote approved output to canonical wiki pages.

D. Index
   → Generate manifest.
   → Build lexical index.
   → Build dense index.
   → Fuse + rerank.
   → Generate optional graph derivative.
   → Never hand-edit generated data.

E. Query
   → Read MAP.
   → Determine scope/access.
   → Query manifest.
   → Retrieve/rerank chunks.
   → Load limited evidence.
   → Recursively retrieve only within limits.
   → Produce answer with evidence IDs.

F. Evaluate
   → Run fixed query set.
   → Measure source/chunk recall, citation validity, answer usefulness.
   → Add multi-vector retrieval only if the baseline is inadequate.

G. Learn
   → Log agent trajectories.
   → Verify + review.
   → Curate approved RLVR candidates.
   → Train only from a permissioned, versioned, evaluated dataset.

H. Distribute
   → Build signed device-specific context and index bundles.
   → Devices read their role bundle and append new capture to inbox.
   → Canonical changes merge centrally.
```

That is the merge: your proposal supplies the operational topology and vocabulary; my earlier plan supplies the data integrity, retrieval rigor, and training-quality controls needed to keep it from becoming an impressive but unreliable pile of generated notes.

<div align="center">⁂</div>

[^5_1]: PROPOSAL_V2_CORRECTED_WIKI_TERMINOLOGY_AND_s_tier_ALTERNATIVE.md.txt


---

# Okay well here's some edits that I was already going to have one Omni route was absolutely going to be the retrieval pipeline and I was going to route it basically every query every input every prompt carried by Omni route and it's SQL Data Bank and Omni route is going to do the following -every session starts like this: \\ honey for Devs SDK is attached and model extracts setup and skills deployment, \\ Task-observer (AKA one skill to rule them all), Startup script is activated and Task-olbservers skills plug-in available \\ OmniRoute server path for the context protocol and agents runtimes, Reasoning Bank and Continual Harness are both skills/tools WRITTEN INTO and UTILIZED by OmniRoute itself during the session, \\ Code,Review,Graph , the AST and graph vector database for retrieval \\ mem0, the episodic memory layer for writing to agent sessions memory and session context \\ Terrestrial Brain (OB1 fork with Obsidian plug-in) the static retrieval protocols similar to the llm wiki evolving data but works from a structured SQLdatabase graph index similar to what OmniRoute is operating on. These are all derived from the "source of truth" docs that are in my main corpus repository that git syncs to Obsidian, Markor, Graphify, Notebooklmpy and possibly a custom SQL database compiled from the same exact data. (These are also the cross agent auditor and red agent auditors own sandboxed databases) (Refered to in my enterprise as the \#d.u.m.b.a.s.s, the \#dumbass or simply "the dumbass" [database and universal memory bank across split services]). I plan on setting up a local OpenWiki tui and have that agent compile, distribute and maintain the upkeep of the repository vault \\ Secondary skills - besides the retrieval pipeline the secondary skills available would be the official Obsidian Skills, Graphify skills for access and retrieval. \\ Alternative and ancillary Repo skills and tools; im also looking at several different alternatives or supplementary assets to implement such as (name of GitHub Repo); MemTensor/MemOS \\ Ar9av/obsidian-wiki \\ runkids/skillshare \\ zillztech/memsearch \\ XiaomiMiMo/MiMo-Code \\ diegosauzapw/OmniGlyph \\ headroom-labs-ai/headroom \\ NevaMind-AI/menU \\ upstash/context7 \\ huytieu/COG-second-brain \\ a5c-ai/babysitter \\ benmaster82/Kwipu \\ netresearch/context7-skill \\ clean my AI harness \\ LEJ-Perplexity powered search for Claude \\ Android reverse engineering skill \\ open interpreter \\ some of those would be used to help enforce the protocols and the orchestration layer some of them would be either replacements or supplementary to the database itself some would replace others that I've already mentioned up above and then I also have other agent harnesses that I would like to try such as the dsh, Hermes, Qwen Code, Prime Agent, openship, Pi, anything llm, langflow , crewAI , Orca , localA, homebrewi and Fabric. Can you give advice as to how to best decide which to use, what to build with, alternative versions, orcastratiion contracts, output style prompt, setup scripts and the best way to move forward. I've been wanting to do a query session like this for a while now using matt pococks skills design with grill-with-docs, so far I have over 10000+ files over 1700+ folders and a complete build out guide but I don't think its perfect and the RUNTIME and EXTRACTION layers definitely needs the most help. Another pending issue is Claude code has proven worthless for ingesting large databases, following any kinds of hard rules or even utilizing any skill or tool its plugged into whatsoever, it even ignored its own protocols that are plugged into it directly from anthropics servers. For this reason I want to move away from it as a primary agent harness and strictly use it as a BUILD TOOL only, something the agent has access to in order to query, prompt and use to build and code with. So besides Hermes i am not sure what I want to use. I've heard good things about dsh and deep seek V4 flash but I've been trying it out with the Android app on my device and that thing is fucking retarded and useless I'm wondering if the actual repo and API routed models would be a lot better or not I mean anything has to be better than what it is right now, its trash

Your correction changes the architecture materially: **OmniRoute is not merely an optional memory extractor; it is the mandatory session gateway and retrieval control plane.** That is workable, but it means OmniRoute must be treated as a versioned platform with strict contracts—not as one large server that directly “owns” every database, skill, and agent behavior.

Your main decision now is not “which agent is smartest.” It is: **what is the smallest stable control plane that every harness can use without becoming coupled to the same fragile runtime.**

Your existing proposal already has useful foundations: bounded `MAP.md` navigation, query-only manifests, recursive retrieval, distinct harness modes, and an OpenAI-compatible model interface through OmniRoute.[^6_1]

## Revised target architecture

Keep your `#dumbass` / D.U.M.B.A.S.S. as the **logical enterprise data plane**, but separate its components operationally.

```text
                       Canonical corpus repository
                 Git + immutable source assets + Markdown
                                  │
                     normalize / chunk / extract / verify
                                  │
       ┌──────────────────────────┴──────────────────────────┐
       │                                                     │
Compiled knowledge plane                              Derived retrieval plane
Obsidian / Markor / OpenWiki                         SQL + lexical + vectors + graph
Markdown wiki + decisions                            rebuildable from corpus
       │                                                     │
       └───────────────────────┬─────────────────────────────┘
                               │
                       D.U.M.B.A.S.S. contracts
                               │
                         OmniRoute gateway
    session bootstrap · policy · retrieval planning · routing · logging
                               │
     ┌───────────┬─────────────┼─────────────┬───────────────┐
     │           │             │             │               │
   mem0     Reasoning Bank     OB1      CodeReviewGraph   tool/MCP layer
 episodic    trajectories      static     code evidence    skills, shell,
 session      + verdicts       corpus     + AST graph      filesystem, etc.
     │           │             │             │               │
     └───────────┴─────────────┴─────────────┴───────────────┘
                               │
                    Harness-neutral Agent Contract
                               │
      DSH / Hermes / Prime / Qwen Code / Pi / Claude Code-build
```


### The non-negotiable rule

OmniRoute should be the **only normal entry point** for an interactive agent session:

```text
agent/harness → OmniRoute → policy + retrieval + model/tool routing → outputs/logs
```

But OmniRoute should **not** directly become:

- The source of truth for your corpus.
- The source of truth for decisions.
- The only implementation of retrieval.
- The owner of every tool’s internal schema.
- The unrestricted writer to every memory database.
- The only way to access model APIs during development/emergency recovery.

Use it as a gateway and orchestrator with explicit adapters. Your corpus remains canonical; every SQL, vector, graph, cache, and audit database is a derived or scoped service.

______________________________________________________________________

## Correct OmniRoute contract

You want every prompt, input, and query carried through OmniRoute. Good. The implementation should be **event-sourced**, policy-scoped, and promotion-based.

### Session startup

Every session should begin with a bootstrap payload. Do not make a model “remember” or infer the setup order.

```json
{
  "protocol_version": "1.0",
  "session_id": "sess_20260925_0001",
  "agent_id": "corpus-librarian",
  "harness_id": "dsh",
  "mode": "corpus-maintenance",
  "operator": "local",
  "requested_capabilities": [
    "corpus.read",
    "retrieval.query",
    "wiki.stage_write",
    "tool.graph_query"
  ],
  "policy_profile": "private-local",
  "context_bundle_ref": "bundle:master-vault:revision:abc123",
  "budget": {
    "max_retrieval_rounds": 3,
    "max_tool_calls": 20,
    "max_context_tokens": 48000,
    "max_cost_usd": 2.00
  }
}
```

OmniRoute responds with:

```json
{
  "session_id": "sess_20260925_0001",
  "granted_capabilities": [
    "corpus.read",
    "retrieval.query",
    "wiki.stage_write",
    "tool.graph_query"
  ],
  "denied_capabilities": [
    "raw.delete",
    "git.push",
    "training.promote",
    "cloud.write"
  ],
  "startup_context": {
    "map_ref": "MAP.md@abc123",
    "active_project_refs": [
      "wiki:architectures/memory-pipeline"
    ],
    "skill_refs": [
      "skill:task-observer@1.0",
      "skill:corpus-query@1.0"
    ],
    "tool_catalog_ref": "tools:catalog@abc123"
  },
  "retrieval_contract": "retrieval:v1",
  "write_contract": "write:staging-only:v1"
}
```

This makes the startup state inspectable, replayable, and portable between DSH, Hermes, Prime Agent, or any later harness.

### What OmniRoute does

1. **Authenticates and identifies** the requesting harness, agent, node, and session.
2. **Loads a bounded context bundle**, not the entire corpus or all memory.
3. **Classifies the request**: query, build, extraction, tool use, execution, audit, capture, or research.
4. **Applies policy**: data sensitivity, node scope, cloud permission, tool permission, cost ceiling, and write allowance.
5. **Executes hybrid retrieval** against the derived D.U.M.B.A.S.S. stores.
6. **Routes the task** to a model or tool adapter.
7. **Logs every event** in append-only form.
8. **Stages candidate memories, claims, skills, tools, and trajectories.**
9. **Promotes only verified items** into durable stores.

### What OmniRoute must not do automatically

Do **not** let it write every raw prompt/response straight into `mem0`, OB1, the wiki, or training data.

Every interaction can be **logged**. Not every interaction deserves to become **memory**.

Use:

```text
all events
  → append-only event log
  → candidate extraction
  → policy/deduplication/conflict check
  → evidence verification
  → staged object
  → approval or deterministic promotion
  → correct durable layer
```

That preserves your “everything runs through OmniRoute” principle without turning every speculative model response into permanent system truth.

______________________________________________________________________

## Your memory and retrieval roles

Your current components overlap. Lock their boundaries now.


| Component | Correct job | May write automatically? | Must not become |
| :-- | :-- | --: | :-- |
| Main corpus Git repo | Canonical source assets, normalized assets, compiled Markdown, ADRs, schemas | No, except controlled commits/staging | A live runtime database |
| Obsidian / Markor | Human-facing local Markdown client/editor | Human edits only, or explicit staged agent edits | The authoritative retrieval engine |
| OpenWiki TUI | Librarian/operator interface for navigating, compiling, validating, and maintaining the vault | Staged wiki proposals | A hidden independent source of truth |
| `manifest.jsonl` | File-level discovery, integrity, metadata filtering | Generated only | Full semantic retrieval index |
| Canonical chunk registry | Stable evidence units for retrieval and citations | Generated only | A manually edited note collection |
| OmniRoute SQL database | Sessions, request events, policy decisions, routing, cost, task state, extraction staging | Yes, append-only and scoped updates | A duplicate master corpus |
| mem0 | Short/medium-lived episodic context and selected user/agent facts | Only through promotion rules | Long-term technical truth |
| Terrestrial Brain / OB1 fork | Persistent static retrieval over canonical corpus derivatives | Rebuilt/synchronized from corpus | A hand-maintained alternate vault |
| CodeReviewGraph / Graphify | AST, symbols, dependencies, code-to-doc links, code evidence | Generated from code/repo snapshots | General-purpose memory |
| Reasoning Bank | Auditable task trajectories, verified outcomes, recovery/handoff records | Append-only | Unreviewed RLVR training set |
| Vector stores | Dense and multi-vector retrieval derivatives | Generated only | Canonical storage |
| Red/Cross auditor stores | Isolated read-only snapshots or scoped derivative indexes | Auditor annotations only | Backdoor canonical writers |

Your proposal identifies mem0 as episodic, OB1 as semantic/static retrieval, Reasoning Bank as trajectory/recovery memory, and OmniRoute as an extraction/routing layer; preserve that distinction.[^6_1]

### Terrestrial Brain / OB1 rule

If Terrestrial Brain is the static SQL/graph retrieval layer built from the same corpus, treat it as a **read model**:

```text
canonical repository
  → normalizer/chunker
  → registry
  → SQL graph + embeddings + lexical indexes
  → Terrestrial Brain / OB1 query API
```

Not:

```text
Obsidian + corpus ↔ Terrestrial Brain ↔ OmniRoute
```

with all three editing each other. That will fork reality.

______________________________________________________________________

## Retrieval pipeline to implement

Replace “the SQL data bank does retrieval” with a formal retrieval service contract. SQL is one store; retrieval is the orchestrated process.

```text
Request through OmniRoute
  → classify intent and permitted data scope
  → read bounded MAP.md for orientation when needed
  → metadata candidate selection from manifest/SQL
  → BM25/lexical retrieval
  → dense embedding retrieval
  → AST/code graph retrieval for code tasks
  → structured SQL/graph retrieval for entities/relationships/decisions
  → reciprocal-rank fusion
  → reranker
  → evidence pack
  → optional bounded KAG round
  → answer/action with provenance
```


### Retrieval lanes

| Query type | First retrieval lane | Supporting lanes |
| :-- | :-- | :-- |
| Exact command, path, model ID, API, error | Lexical/BM25 | Metadata, reranker |
| “Why did we choose X?” | Decisions/claim SQL graph | BM25, dense, wiki links |
| Semantic research question | Dense retrieval | BM25, reranker, graph |
| Code location or dependency question | CodeReviewGraph / AST | Lexical, repo metadata |
| Cross-system architecture question | Wiki MOCs + decision graph | Dense, graph, reranker |
| Session continuation | Reasoning Bank + mem0 | Relevant corpus retrieval |
| Agent policy/tool selection | Capability catalog + policy SQL | Skill registry, task observer |
| Audit question | Event/trajectory log | Corpus evidence and cost ledger |

### Multi-vector order

Do **not** deploy every alternative at once.

1. `manifest.jsonl` + SQLite/DuckDB metadata.
2. BM25/FTS over chunks.
3. Dense embeddings.
4. Fusion and reranker.
5. Evaluation suite.
6. Code graph retrieval.
7. Multi-vector/late-interaction index.
8. Recursive KAG.
9. Cross-agent retrieval/audit snapshots.

Your earlier design already treats manifests as query-only and never as full-context input; retain that rule.[^6_1]

______________________________________________________________________

## Task Observer: make it a protocol

“Task Observer” can be your central skill, but do not make it a gigantic prompt that tries to do ingestion, planning, retrieval, tool selection, audit, and coding directly.

Make it a **controller contract** with hooks/adapters.

### Task Observer responsibilities

```text
1. Receive normalized task request.
2. Identify task class.
3. Request session policy and capability grant from OmniRoute.
4. Choose allowed skills/tools from catalog.
5. Request evidence pack.
6. Generate a plan with explicit side effects.
7. Dispatch specialized worker.
8. Run completion and evidence checks.
9. Emit a signed/stored result envelope.
10. Stage reusable skills/tools/memory candidates.
```


### Task Observer must not

- Directly write to the canonical wiki.
- Decide that its own output is true.
- Give itself more permissions.
- Directly train/update models.
- Select a provider solely because it has a higher benchmark.
- Bypass OmniRoute for normal work.
- Load all memory stores at startup.


### Output envelope

Require every worker to return this structure:

```json
{
  "task_id": "task:20260925:0001",
  "status": "complete",
  "summary": "Short human-readable result.",
  "artifacts": [
    {
      "path": "staging/wiki/omniroute-contract.md",
      "kind": "proposed_wiki_update",
      "sha256": "..."
    }
  ],
  "evidence": {
    "source_ids": ["src:..."],
    "chunk_ids": ["chunk:...", "chunk:..."],
    "query_rounds": 2
  },
  "tool_calls": [
    {
      "tool": "retrieval.query",
      "result_ref": "event:..."
    }
  ],
  "validation": {
    "schema_valid": true,
    "citations_resolve": true,
    "policy_compliant": true,
    "tests_passed": true
  },
  "side_effects": {
    "writes_staged": true,
    "canonical_writes": false,
    "network_calls": false
  },
  "open_questions": [],
  "handoff": {
    "next_recommended_action": "review-staged-wiki-update"
  }
}
```

This is how you make an agent system reliable: not with “follow hard rules,” but by making completion require an artifact, evidence, policy result, and validation result.

______________________________________________________________________

## Harness decision framework

You should not pick one forever harness tonight. Build against the interface above, then run a controlled bake-off.

### Roles

| Role | Recommendation |
| :-- | :-- |
| **Primary orchestration candidate** | DSH, if its plugin model and lifecycle meet your needs after a small proof-of-concept |
| **Personal/local interactive agent candidate** | Hermes, especially if you want local memory/skills and an operator-facing assistant layer |
| **On-device local model harness** | Prime Agent or a minimal custom runner, depending on whether it can honor your contracts and local runtime constraints |
| **Build/coding executor** | Claude Code as an explicitly bounded build tool, not your control plane |
| **Alternative coding executor** | Qwen Code / DeepSeek harness / Pi, tested against the same build tasks |
| **Flow prototyping** | Langflow only for visual experimentation and integration diagrams; not your primary control plane |
| **Multi-agent experiments** | CrewAI or similar only after the single-agent contract is stable |
| **Local tool execution** | Open Interpreter only in a constrained sandbox/capability profile, never unrestricted on your canonical vault |
| **Research/skill assets** | Fabric, Context7 variants, Android RE skill, Perplexity search connector—treat as tools/skills, not harnesses |

### DSH

DSH is worth evaluating as the primary **modular harness** because its published design emphasizes replaceable model adapters, tool registries, session logging, and agent loops through plugins. The important downside is that it is still described as developer preview with expected breaking changes.[^6_2]

Use it if it passes:

- You can enforce your session bootstrap contract.
- It can invoke OmniRoute as the only normal model/tool gateway.
- It has scoped capability grants.
- Plugin unload/reload cannot leave ghost permissions or state.
- It can produce your result envelope and append-only event logs.
- It can run your Task Observer as controller rather than burying it in a prompt.
- It survives an upgrade without corrupting sessions or memory.

Do **not** make it irreplaceable. Pin it to a commit/version, wrap it in your adapter, and retain a harness-neutral `agent-contract` test suite.

### Hermes

Hermes is a reasonable parallel evaluation candidate for an operator-facing personal/local agent. More importantly, the MemOS ecosystem explicitly advertises a local plugin for Hermes and DeepSeek Harness, with layered traces, policies, world-model-style memory, crystallized skills, hybrid retrieval, and a unified editable memory API.[^6_3]

But that does **not** mean MemOS should replace your corpus vault. It can become an optional memory backend behind the OmniRoute memory adapter only after it passes:

- Export/import without loss.
- Clear deletion semantics.
- Read/write provenance.
- No silent promotion of model output to durable truth.
- Local deployment you control.
- No dependency on a proprietary hosted API for your core path.
- No conflict with your D.U.M.B.A.S.S. schemas.


### Claude Code

Your conclusion is reasonable: use Claude Code as a **build worker**, not as your primary orchestrator or corpus custodian.

Claude Code can still do well at bounded tasks:

```text
- Implement one script from a written specification.
- Refactor a named package with a test suite.
- Generate a migration under a branch.
- Build a particular adapter against your OmniRoute contract.
- Run a narrowly scoped review against supplied files.
- Produce a proposed patch, not autonomous architecture truth.
```

Do not assign it:

```text
- “Understand and ingest 10,000 files.”
- “Follow all global rules forever.”
- “Maintain the full ontology autonomously.”
- “Choose which memory is true.”
- “Infer your system state from scattered notes.”
```

The fix is not primarily a better prompt. It is task slicing, filesystem boundaries, manifest-driven evidence retrieval, staged writes, and deterministic validation.

### DeepSeek models / app quality

I cannot tell from an Android app experience whether the same branded model through an API, repo, or different harness will be materially better. It may differ because of model version, system prompt, quantization, decoding parameters, context truncation, tool implementation, or application-level routing—but that is not guaranteed.

The correct answer is: **do not buy into “DeepSeek V4 Flash is better” based on reputation or dismiss it based only on one mobile app. Benchmark the actual endpoint and exact model/version you will operate.**

Measure it on your own tasks:

- Correctly follows a constrained build spec.
- Uses only allowed tools.
- Produces valid structured output.
- Cites correct retrieved evidence.
- Completes code changes with tests.
- Recovers from failed tools without improvising.
- Works under long but bounded retrieval context.
- Runs acceptably on your intended device/node.
- Cost, latency, reliability, and data exposure.

A good model behind a bad Android wrapper can feel useless; a bad fit remains bad even behind a better harness. Your test suite decides.

______________________________________________________________________

## Alternatives: classify, don’t install

Your list mixes several categories. Do not install them as a pile of “AI infrastructure.” Put each through a role gate.


| Asset | Likely role | Recommendation now |
| :-- | :-- | :-- |
| MemTensor/MemOS | Optional long-term memory backend | **Evaluate later** behind OmniRoute adapter; do not make canonical |
| `Ar9av/obsidian-wiki` | Wiki/Obsidian workflow reference | **Inspect for conventions**, do not adopt blindly |
| `runkids/skillshare` | Skill sharing/discovery | **Quarantine/evaluate**; only import reviewed skills |
| `zilliztech/memsearch` | Cross-session coding-agent memory | **Test as a narrow session-history retrieval sidecar** |
| Xiaomi MiMo-Code | Coding model/tool candidate | **Benchmark**, not architecture dependency |
| `diegosauzapw/OmniGlyph` | Need exact capability verification | **Research only** until role is clear |
| `headroom-labs-ai/headroom` | Need exact capability verification | **Research only** |
| NevaMind `menU` | Need exact capability verification | **Research only** |
| Upstash Context7 | Documentation/context retrieval | **Useful tool adapter**, not memory authority |
| `huytieu/COG-second-brain` | Git/Markdown/Obsidian second-brain reference | **Borrow verification patterns**, not whole framework |
| `a5c-ai/babysitter` | Supervision/agent guard candidate | **Evaluate as a verifier/guard**, not orchestrator |
| `benmaster82/Kwipu` | Need exact capability verification | **Research only** |
| `netresearch/context7-skill` | Context7 skill wrapper | **Use only if it fits your tool contract** |
| Clean My AI Harness | Harness hygiene/reference | **Inspect for checklist ideas** |
| Perplexity-powered search | External research/retrieval tool | **Adapter only**, separate from private corpus retrieval |
| Android reverse-engineering skill | Specialized scoped capability | **Separate high-risk sandbox skill** |
| Open Interpreter | Local execution capability | **Sandboxed tool only**, permission gated |
| DSH | Primary harness candidate | **Run bake-off now** |
| Hermes | Primary/interactive harness candidate | **Run bake-off now** |
| Qwen Code | Coding worker candidate | **Benchmark** |
| Prime Agent | Local open-weight runtime candidate | **Retain for edge role** |
| OpenShip / Pi / AnythingLLM / LocalAI | Varying server/UI/runtime candidates | **Use only where a precise gap exists** |
| Langflow | Prototype/visual integration | **Defer as production control plane** |
| CrewAI / Orca | Multi-agent orchestration candidates | **Defer until single-agent system works** |
| Fabric | Prompt/transform library | **Adopt as small stateless transformations only** |

MemOS is explicitly positioned as a memory system with a unified store/retrieve/manage API, graph/vector support, multimodal memory, inspectability, and local deployment options; that makes it worth a controlled adapter evaluation, not automatic adoption as your D.U.M.B.A.S.S. backbone.[^6_4][^6_3]

Memsearch is a cleaner, narrower test candidate: it captures coding-agent conversations and offers hybrid search with a local ONNX embedding option. That makes it useful as a **session-history retrieval experiment**, but not as your master corpus or cross-enterprise memory source.[^6_5]

COG is worth reading primarily for its Markdown + Obsidian + Git approach and its verification framing that a worker should not grade its own work. Do not graft its 35 skills/10 agents directly into your stack before your own interface and policy contracts exist.[^6_6][^6_7]

______________________________________________________________________

## Bake-off: how to choose

Create an isolated harness evaluation repo. No access to your full corpus. Give each harness the **same** tools, same constrained data bundle, same models where possible, and same task suite.

```text
harness-lab/
├── contract/
│   ├── session-bootstrap.schema.json
│   ├── agent-result.schema.json
│   ├── tool-call.schema.json
│   └── capability-profile.schema.json
├── adapters/
│   ├── dsh/
│   ├── hermes/
│   ├── prime-agent/
│   ├── claude-code/
│   └── qwen-code/
├── fixtures/
│   ├── small-vault/
│   ├── codebase/
│   └── corrupted-inputs/
├── tasks/
│   ├── retrieval/
│   ├── ingestion/
│   ├── coding/
│   ├── tool-use/
│   ├── recovery/
│   └── policy/
├── evaluators/
│   ├── schema-checks/
│   ├── citation-checks/
│   ├── filesystem-diff/
│   ├── cost-latency/
│   └── human-review/
└── results/
```


### Required tests

| Test | Pass condition |
| :-- | :-- |
| Bootstrap | Reads supplied session contract and returns valid capability acknowledgment |
| Retrieval | Finds expected chunks/decisions across a small vault |
| Bounded context | Does not load all manifests or all docs |
| Tool discipline | Uses allowed tool only; blocks denied action |
| Structured result | Returns valid output envelope every time |
| Failure recovery | Handles one tool failure without fabricating success |
| Staged writing | Writes proposal to staging, not canonical wiki |
| Citation validity | Every source/chunk reference resolves |
| Code task | Produces patch plus tests for a fixed issue |
| Restart/handoff | Another harness can continue from handoff artifact |
| Cost/latency | Logs model/token/provider/tool timings |
| Upgrade stability | Re-run after harness upgrade without data/schema corruption |

Score each:

```text
40% contract compliance
20% task completion
15% evidence/citation accuracy
10% failure recovery
10% operating cost + latency
5% operator usability
```

Reject any harness that fails contract compliance, even if its prose/coding is better.

______________________________________________________________________

## Build sequence

Do this in order. Do not start with a 10,000-file autonomous ingestion run.

### 1. Freeze architecture decisions

Create these documents first:

```text
protocols/
├── omniroute-session-contract-v1.md
├── dumbass-data-plane-v1.md
├── retrieval-contract-v1.md
├── task-observer-contract-v1.md
├── memory-promotion-policy-v1.md
├── agent-output-envelope-v1.md
├── harness-adapter-contract-v1.md
└── device-bundle-contract-v1.md
```

Your proposal already has useful terminology and topology material; integrate it here rather than scattering it across multiple runtime prompts.[^6_1]

### 2. Build the smallest D.U.M.B.A.S.S. slice

Use only:

```text
- One small corpus sample: 50–100 representative files.
- MAP.md.
- File manifest.
- Normalized text.
- Stable chunks.
- SQLite/DuckDB metadata.
- BM25/FTS.
- One embedding model/vector index.
- One OpenWiki/Obsidian view.
- One audit/event log.
```

No MemOS, no graph database, no multi-agent swarm, no full RLVR loop yet.

### 3. Build OmniRoute as adapter-driven

Its first endpoints should be conceptually:

```text
POST /v1/session/start
POST /v1/retrieve
POST /v1/chat/completions
POST /v1/tools/dispatch
POST /v1/events
POST /v1/stage/extraction
POST /v1/handoff
GET  /v1/session/{id}/context
GET  /v1/capabilities
```

Internally, every store is an adapter:

```text
CorpusAdapter
ManifestAdapter
ChunkAdapter
LexicalRetriever
DenseRetriever
GraphRetriever
Reranker
MemoryAdapter
TrajectoryAdapter
ToolAdapter
ModelAdapter
PolicyAdapter
AuditAdapter
```

Do not hardwire `mem0`, Terrestrial Brain, Graphify, or MemOS into core request code. Each should conform to an interface and be swappable.

### 4. Implement Task Observer

Implement it first as a deterministic controller plus a small LLM planning prompt, not an autonomous mega-agent.

Its initial modes:

```text
query
corpus-ingest
wiki-stage
code-build
audit
research
handoff
```


### 5. Run DSH and Hermes against it

Do not choose based on Reddit reports, GitHub stars, or a broken Android app. DSH’s modular plugin architecture is promising but still preview-grade; keep it behind your contract boundary.[^6_2]

### 6. Only then scale corpus ingestion

Run ingestion in batches:

```text
Batch 0: 50–100 mixed files.
Batch 1: 250 files.
Batch 2: 1,000 files.
Batch 3: the remaining corpus by category.
```

After each batch:

- Verify hashes.
- Validate normalizations.
- Check chunk stability.
- Run retrieval evals.
- Review extraction error rate.
- Confirm no sensitive data leaked into external calls.
- Confirm indexes are reproducible from the same commit.


### 7. Add specialist assets one at a time

A tool earns admission only if it improves a benchmark or fills a documented contract gap.

```text
candidate
→ isolated sandbox
→ adapter implementation
→ fixture task suite
→ metric improvement
→ threat/privacy review
→ accepted / rejected / deferred ADR
```


______________________________________________________________________

## Practical prompt style

Do not use long motivational system prompts. Use compact, machine-checkable task packets.

```markdown
# Task

Class: `corpus-ingest`
Task ID: `task:20260925:0007`

## Objective
Normalize the assigned source set and produce staged extraction records.

## Scope
Allowed paths:
- `01_inbox/batch_0007/`
- `02_normalized_sources/staging/batch_0007/`
- `04_registry/staging/`
- `07_episodic_logs/`

Forbidden paths:
- `01_raw_sources/`
- `03_compiled_wiki/`
- `05_retrieval_derivatives/`
- any network destination

## Required procedure
1. Read `MAP.md`.
2. Query the scoped manifest; never load it in full.
3. Preserve originals and hashes.
4. Create normalized derivatives only.
5. Emit source/chunk records according to schema.
6. Stage extraction candidates; do not promote them.
7. Run validator.
8. Return the result envelope.

## Success criteria
- Every source has a stable `source_id`.
- Every chunk has an evidence location.
- All JSON validates.
- No forbidden path changed.
- No uncited factual wiki claim was created.

## Output
Return only a valid `agent-result.schema.json` object.
```

The harness should reject malformed results, rather than hoping the model “remembers” the rules.

______________________________________________________________________

## Bottom line

Your strategic change is correct:

- **OmniRoute** becomes the mandatory gateway and retrieval/orchestration control plane.
- **D.U.M.B.A.S.S.** becomes the logical data plane containing corpus-derived views and scoped memory/audit stores.
- **OpenWiki** becomes the librarian/maintenance interface, not the canonical data authority.
- **Claude Code** becomes a build worker, not the operating system.
- **DSH and Hermes** are the first harnesses worth testing, but neither should control your architecture until it passes your contract suite.
- **MemOS and Memsearch** are evaluate-as-adapters candidates, not replacements for your corpus and evidence model.
- **RLVR comes after** event logs, verifiers, trajectory review, and stable retrieval evaluations—not before.

The first thing to build is not a giant “one skill to rule them all.” It is `omniroute-session-contract-v1`, `agent-output-envelope-v1`, and a tiny 50–100 file pilot that proves the exact ingestion → retrieval → evidence → staged-write loop end to end.

<span style="display:none">[^6_10][^6_11][^6_12][^6_13][^6_14][^6_15][^6_16][^6_8][^6_9]</span>

<div align="center">⁂</div>

[^6_1]: PROPOSAL_V2_CORRECTED_WIKI_TERMINOLOGY_AND_s_tier_ALTERNATIVE.md.txt

[^6_2]: https://github.com/topics/dsh-plugin?l=go

[^6_3]: https://github.com/MemTensor/MemOS

[^6_4]: https://deepwiki.com/MemTensor/MemOS/2.1-installation

[^6_5]: https://zilliztech.github.io/memsearch/

[^6_6]: https://github.com/huytieu/COG-second-brain

[^6_7]: https://github.com/huytieu/COG-second-brain/blob/main/COG-VERSION

[^6_8]: https://github.com/topics/hermes-agent

[^6_9]: https://github.com/toby941/MemTensor-MemOS

[^6_10]: https://github.com/huytieu/COG-second-brain/blob/main/SETUP.md

[^6_11]: https://github.com/topics/harness-engineering

[^6_12]: https://github.com/deepseek-ai/deepseek-harness/discussions/525

[^6_13]: https://github.com/topics/agent-framework?l=html

[^6_14]: https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/guide/ecosystem/agent-harness-landscape.md

[^6_15]: https://www.reddit.com/r/LocalLLaMA/comments/1w8f7bp/which_agent_harness_do_you_use_and_why/

[^6_16]: https://deepwiki.com/MemTensor/MemOS


---

# Okay a couple things corrections I need to make and then I need some more clarification. Correction on one was code review graph is actually a graph vector retrieval arm it is equally as important as a static memory layer or a episodic memory layer it's right up along there with mem0 and terrestrial brain, not to be forgotten about or simply left out. Similarly there's no way in hell I'm going moving without a graph database that's way tighter structure than relying on merely a Wiki and gratifying obsidian are just as important to the dumbass has Wiki is code review graph is just as important to the retrieval layer. Graph database it's not just to ancillary option it's part of the core infrastructure. And I need clarification on exactly how to launch task observer if I'm not going to be using the built-in launch script that it comes with then what the hell am I supposed to be using how does it interact with Omni route how does omni route call on it how do the agents use it? Also if OmniRoute is the routing harness then is that not the main agent itself? Is that going to be the main tui that I use? Or is it a plug-in into a tui like Hermes or deepseek? Also I'm definitely going to build out the corpus I'm not starting with 50 to 100 with the project of over 10,000 plus documents that's ridiculous I'm building the corpus first and foremost so I need some better guidance as to how to get that thing going cuz I'm not stopping until the corpus and the repositories are all complete I'm not just going to start pointing and shooting from the hip before I have the universal dumbass as the control. Also about the training and editing, those are home side sessions based and not something that's going to be interrupting with my daily operations at the end of the day when I finally plug into my home node as a peer-to-peer server my phone's and tablets logs can be collected then and only then will the cross agent auditor interact with my daily workflow that's only for session based cross-agent auditing it's only after a set amount of tasks are collected that the scripts are going to be handed off to a red Asian auditor and then my on-device weights can actually be loaded to a cloud session for training and later extraction that's not something that's going to be a daily issue or even session prompt by prompt inference either. Also those logs and that data is going to be stored and utilized under the auspices of [Success Verification Grade Logs] the models will be trained on success rlvr pathways and that's the way that their data is going to be collected and stored and even reference as. Training off of failures leads to more failures. Oh another correction continual harness and reasoning Bank need to be folded into Omni route and utilized by Omni route we're not going to just leave continual harness out of this and I also need a little further direction on how to exactly get on me right to adopt the successfully. I want another thing honey for Devs SDK is attached to the agents at launch as well, that's the main compression tool and not only that Omni route so Omni route has the socket for running rtk and caveman but honey for Dev's is how much richer token compression layer and I'm hardly ever using rust anyway so rtk is kind of pointless if I'm going to be using honey for Dev's that honey for Dev's is better than Honey I shrunk the AI and caveman and more useful to my work than rtk, so that needs to be implemented as well. Also you never really explained where memos and memsearch would fall into this whole thing and what they would be replacing or what purpose they're actually serving am I just going to flat out replace mem0? Do they fall within the dumbass somewhere else? And some clarification about my own device models, my main on device assistant app that I'm building is utilizing the small executions \& large query model style. The thing is that I'm mostly going to use these to call on my frontier models or API agents that I'm running inference with anyways example I would be on my phone and I would start running a quad code or Gemini something like that perplexity search and I would key in my device agent give it the prompt the query agent would probably reassemble into a metaprompt I would hit send a model like yourself or Claude would reply my TTS would fire off so that I could hear what it was saying in real time it would have VAD as well. Then after retrieving whatever the result was query model could frame that for its basis on how it's going to prompt the execution for implementing the results it could query me for further directions etc. other use cases could be me simply asking a question or giving it a prompt and then the query model itself could decide whether it needed to refer to an API tool or cloud-based tool or run inference with a frontier model first or if it could just handle the task itself on device also I'm going to have terminal access for my APK and a very very small like nanoagent basically it's going to be the npu orchestration layer make sure that these things can fire off on the hexagon properly without overlapping and when I'm at home running everything peer-to-peer then the larger query model can actually become an executor when I'm running running larger inference with a bigger system just to give you an idea of how my workflow is going to work but yeah first and foremost I need to get this dumbass built that's what I need the most help with is building the dumbass and routing the dumbass as far as my runtime and extraction layer goes

You are right on the graph correction: **CodeReviewGraph/Graphify plus a graph database are core D.U.M.B.A.S.S. infrastructure**, not a secondary retrieval add-on. The proper model is a three-arm persistent knowledge layer: static corpus/semantic retrieval, episodic/session memory, and graph-vector/structural retrieval.

Also: OmniRoute is the **control-plane harness and gateway**, but it is not the conversational agent or necessarily your TUI. Your chosen TUI/harness hosts the agent loop; it sends every request through OmniRoute. Task Observer is launched as a controlled service/worker registered with OmniRoute—not by hoping a launch script magically makes it the system brain.

Your uploaded proposal already defines OmniRoute as the interception/extraction layer; Reasoning Bank, mem0, OB1, continual harness, Graphify, and CodeReviewGraph are established first-class architecture components.[^7_1]

## Corrected D.U.M.B.A.S.S. model

Use this as the corrected core:

```text
D.U.M.B.A.S.S.
Database and Universal Memory Bank Across Split Services

Canonical authority
────────────────────────────────────────────────────────────
Git master corpus repository
  ├─ immutable/raw source assets
  ├─ normalized derivatives
  ├─ Markdown compiled wiki
  ├─ schemas, manifests, ADRs, policies
  └─ canonical IDs and provenance

Derived but core operational services
────────────────────────────────────────────────────────────
1. Terrestrial Brain / OB1
   └─ static corpus retrieval, structured SQL records,
      document/entity/claim/decision knowledge graph

2. CodeReviewGraph / Graphify
   └─ code AST graph + vector retrieval + repository dependency graph +
      code-to-doc/tool/skill/runtime relationship graph

3. mem0
   └─ episodic/session memory and selected agent/user context

4. Reasoning Bank inside OmniRoute
   └─ validated execution trajectories, handoffs, recovery records,
      Success Verification Grade Logs

5. Continual Harness inside OmniRoute
   └─ session refinement, state compression, checkpoint/rollback,
      context assembly and task continuity

6. OmniRoute
   └─ mandatory gateway, routing harness, retrieval planner,
      extraction pipeline, policy/budget gate, event/log coordinator

7. Honey for Devs SDK
   └─ launch-time compression and structured context/skill packaging layer

8. OpenWiki TUI
   └─ librarian/operator interface for corpus navigation,
      compilation, maintenance, review, and distribution
```


### Retrieval arms

```text
                         OmniRoute
                             │
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
Terrestrial Brain       CodeReviewGraph            mem0
Static corpus          Graph + AST + vectors       Episodic state
documents, decisions   code, systems, links        current sessions
entities, claims       dependencies, retrieval     user/agent context
    │                        │                        │
    └────────────────────────┼────────────────────────┘
                             │
          Reasoning Bank + Continual Harness
       success logs, verified trajectories, state refinement
```

The graph database is not optional. Use it as a first-class query endpoint behind OmniRoute.

Your original proposal already assigns Graphify to AST and knowledge-graph mapping and identifies CodeReviewGraph as cross-agent graph code checking; it also puts OB1, mem0, Reasoning Bank, and continual harness together in the memory subsystem. The correction is to elevate CodeReviewGraph into the **same core tier**, rather than positioning it as merely a code-specific helper.[^7_1]

______________________________________________________________________

## The graph database

You need **two graph domains**, possibly in the same graph engine but with separate labels, permissions, and ingestion paths.


| Graph | Nodes | Edges | Main questions |
| :-- | :-- | :-- | :-- |
| Knowledge graph | Sources, chunks, claims, decisions, models, tools, skills, runtimes, devices, agents, projects | `supports`, `contradicts`, `uses`, `runs_on`, `depends_on`, `supersedes`, `owned_by`, `implements` | “Why did we choose this?”, “Which runtime supports this model?”, “What changed this decision?” |
| CodeReviewGraph | Repositories, commits, files, symbols, classes, functions, APIs, tests, scripts, packages, build targets | `imports`, `calls`, `defines`, `tests`, `changes`, `generates`, `depends_on`, `implements`, `documents` | “What breaks if this file changes?”, “Which code implements the OmniRoute adapter?”, “Where is this tool contract used?” |
| Cross-graph links | Wiki entities ↔ source chunks ↔ code symbols ↔ configurations ↔ devices | `documented_by`, `implemented_by`, `deployed_to`, `configured_by`, `validated_by` | “Which source supports this system behavior and what code actually implements it?” |

The graph database should be a **derived, rebuildable read model** from the corpus and code repositories, but it is still core runtime infrastructure because OmniRoute depends on it for structural retrieval.

### Graph database contract

```text
GraphDB must support:
- Stable node/edge IDs.
- Source commit/revision on every derived node/edge.
- Evidence links back to source IDs/chunk IDs/code locations.
- Traversal depth limits.
- Namespace/node-level access control.
- Incremental updates from Git diffs.
- Rebuild from a known corpus/repo revision.
- Query logging through OmniRoute.
```

Do not permit Graphify, Obsidian, OpenWiki, or an LLM to be the only writer of graph facts. They can generate **staged graph mutations**. A graph ingestion service validates them against source or code evidence before applying them.

```json
{
  "edge_id": "edge:implements:omniroute:0012",
  "from": "symbol:repo/omniroute/router.py#route_request",
  "type": "implements",
  "to": "protocol:omniroute-routing-contract-v1",
  "evidence": [
    "chunk:src:architecture:000217",
    "code:commit:abc123:path:router.py:lines:51-146"
  ],
  "source_revision": "abc123",
  "status": "verified"
}
```


______________________________________________________________________

## OmniRoute: what it is

**OmniRoute is the main routing harness/control plane. It is not the main interactive agent. It is not automatically the TUI.**

Think of the split like this:


| Component | What it is | What it does not do |
| :-- | :-- | :-- |
| OmniRoute | Always-on local service/control plane | It does not need to be your chat UI |
| Task Observer | Workflow controller/agent service | It does not own model routing or databases |
| Hermes / DSH / Prime Agent / custom APK | Agent-loop host or interactive client | It does not bypass OmniRoute |
| OpenWiki TUI | Vault librarian and operator interface | It does not become the routing harness |
| Phone assistant APK | Daily UI, voice, VAD, TTS, query/executor coordination | It does not own corpus authority |
| Graph database | Core structural retrieval service | It does not replace raw sources or Markdown |
| Claude Code | Bounded build/code worker | It does not govern the whole enterprise |

So your likely daily path is:

```text
You speak/type in your Android assistant APK or TUI
  → VAD/STT converts speech to text
  → local query model classifies/frames request
  → OmniRoute receives request
  → OmniRoute loads session policy + Honey for Devs package
  → OmniRoute queries Terrestrial Brain + CodeReviewGraph + mem0
  → OmniRoute decides:
       local query model only
       local executor model
       terminal/NPU tool
       frontier API/model
       retrieval only
  → response returns
  → TTS speaks it
  → session event + candidate extractions are logged
```

If you use Hermes, DSH, or another harness, the flow is the same:

```text
Hermes/DSH agent loop
  → OmniRoute session/start
  → OmniRoute retrieval/model/tool endpoints
  → Hermes/DSH renders the interaction and executes the permitted loop
```

OmniRoute is the **spine**. The harness/TUI is the **face and loop**.

______________________________________________________________________

## Task Observer: exact role

Task Observer is not launched “instead of” its own launch script. There are two separate questions:

1. **How does the Task Observer process start?**
2. **How does it receive tasks and participate in OmniRoute-controlled sessions?**

If the project comes with a launch script, use it only if it does the correct bounded work—starting the service in your environment. Do not let it become the uninspected architecture owner.

### Correct Task Observer placement

```text
Android assistant / Hermes / DSH / OpenWiki TUI
                    │
                    ▼
          OmniRoute: /v1/session/start
                    │
                    ▼
          OmniRoute: classify task
                    │
             task requires control loop?
                    │ yes
                    ▼
        Task Observer worker/service
                    │
        requests retrieval/tools/model through OmniRoute
                    │
                    ▼
         returns validated result envelope
                    │
                    ▼
          OmniRoute logs/promotes/stages results
```

Task Observer is a **registered OmniRoute worker**. It does not directly own:

- Model-provider keys.
- Raw SQL credentials for every store.
- Direct unrestricted filesystem access.
- Full graph write access.
- Direct production corpus write access.
- Training job submission rights.

It gets short-lived capability grants from OmniRoute.

### How to launch it

Use a supervisor that starts both OmniRoute and Task Observer. On Android/Termux this could initially be `tmux`; on a home node, use `systemd`, Docker Compose, `supervisord`, or another stable process supervisor.

Conceptually:

```text
1. Start GraphDB / SQL services.
2. Start retrieval index services.
3. Start OmniRoute.
4. OmniRoute checks adapters and publishes readiness.
5. Start Task Observer with OmniRoute URL and service credential.
6. Task Observer registers its manifest/capabilities.
7. Start TUI/client(s).
8. Client creates session through OmniRoute.
```

The actual startup order is:

```text
data services
  → OmniRoute
  → Task Observer
  → agent harness/TUI
  → daily assistant clients
```


### Task Observer service registration

At startup it registers:

```json
{
  "worker_id": "task-observer",
  "worker_version": "1.0.0",
  "omniroute_url": "http://127.0.0.1:20128",
  "accepted_task_classes": [
    "query",
    "corpus-ingest",
    "wiki-stage",
    "code-build",
    "skill-extract",
    "tool-extract",
    "audit-stage",
    "handoff"
  ],
  "required_capabilities": [
    "retrieval.query",
    "task.plan",
    "result.stage"
  ],
  "optional_capabilities": [
    "tool.dispatch",
    "wiki.stage_write",
    "graph.stage_write"
  ],
  "result_schema": "agent-result:v1"
}
```

Then OmniRoute treats Task Observer like an internal worker. An agent does not “call” Task Observer by shelling out randomly; it submits a task class to OmniRoute, which dispatches the worker if policy allows it.

### What the launch script should do

If you use the built-in launch script, restrict its role to:

```text
- Start the Task Observer executable.
- Load its pinned configuration.
- Set OmniRoute endpoint.
- Present its worker/service credential.
- Declare capability manifest.
- Health-check registration.
- Write logs to the assigned append-only location.
```

It should **not**:

```text
- Start arbitrary models.
- Modify your vault.
- Replace your policy files.
- Grant itself filesystem/network access.
- Create its own independent database authority.
- Bypass OmniRoute.
```

If the provided launch script does more than the allowed list, replace it with your own wrapper or service definition.

______________________________________________________________________

## Task Observer launch skeleton

This is the logical configuration, not a claim about a specific project’s CLI flags:

```yaml
# config/task-observer.yaml
worker:
  id: task-observer
  version: "1.0.0"

omniroute:
  base_url: "http://127.0.0.1:20128"
  registration_endpoint: "/v1/workers/register"
  task_endpoint: "/v1/tasks/claim"
  result_endpoint: "/v1/tasks/complete"

capabilities:
  requested:
    - retrieval.query
    - task.plan
    - result.stage
    - wiki.stage_write
    - graph.stage_write
  denied:
    - corpus.raw_write
    - corpus.raw_delete
    - training.submit
    - cloud.admin

execution:
  max_parallel_tasks: 1
  max_retrieval_rounds: 3
  max_tool_calls: 20
  write_mode: staging_only

inputs:
  skill_catalog: "bundle://skills/current"
  tool_catalog: "bundle://tools/current"
  honey_context_profile: "honey://profiles/task-observer"
  output_schema: "schema://agent-result-v1"

logging:
  event_sink: "omniroute"
  local_fallback: "07_episodic_logs/task-observer/"
```

The service manager invokes it, conceptually:

```bash
task-observer serve --config config/task-observer.yaml
```

If its real executable uses different syntax, adapt only the wrapper command. The architectural contract remains unchanged.

______________________________________________________________________

## Honey for Devs at launch

Your correction is clear: **Honey for Devs SDK is a first-class session bootstrap/compression layer**, not an optional tool. RTK/Caveman are not your main compression path.

Correct stack position:

```text
User request
  → agent/harness session request
  → OmniRoute session/start
  → Honey for Devs context assembly/compression
  → Task Observer receives selected skills + compressed setup
  → retrieval and model execution
```


### What Honey for Devs should provide

At every agent launch:

- Selected skill bundle.
- Task Observer protocol.
- Relevant runtime/tool contracts.
- Active project and device profile.
- Relevant MAP/MOC references.
- Capability boundary.
- Compressed working context.
- Context provenance and version.
- Prompt budget allocation.
- Required output schema.

Do not load “all skills” because you have 10,000+ files. Honey should return a **context package**, selected by OmniRoute after classification and retrieval.

```json
{
  "bundle_id": "ctx:session:20260925:0001",
  "profile": "query-agent-phone",
  "source_revision": "git:abc123",
  "tokens_before": 42000,
  "tokens_after": 9800,
  "included": [
    "protocol:omniroute-session-contract-v1",
    "skill:task-observer@1.0",
    "skill:frontier-query@1.0",
    "tool:terrestrial-brain-query",
    "tool:codereviewgraph-query",
    "device:alpha-profile"
  ],
  "omitted_by_policy": [
    "training",
    "raw-corpus",
    "red-auditor"
  ],
  "provenance": [
    "MAP.md@abc123",
    "manifest:scope:mobile-query"
  ]
}
```


### Honey, RTK, Caveman

Use them in this order:


| Component | Role in your system |
| :-- | :-- |
| Honey for Devs | Primary session context compression, skill packaging, and agent bootstrap |
| OmniRoute | Session/routing/retrieval/policy coordinator |
| Task Observer | Task lifecycle controller |
| RTK | Optional narrow tool if it supplies a specific feature you verify you need |
| Caveman | Optional narrow utility; not the central context system |
| Continual Harness | OmniRoute-owned state refinement/checkpoint/rollback subsystem |
| Reasoning Bank | OmniRoute-owned validated trajectory and recovery subsystem |

So yes: do **not** build around RTK merely because OmniRoute can socket to it. If Honey for Devs gives you the richer compression workflow you need, RTK is optional and must justify its footprint.

______________________________________________________________________

## Continual Harness and Reasoning Bank

Correction accepted: they are not peer external services that OmniRoute happens to call. They are **internal OmniRoute subsystems**.

```text
OmniRoute
├── Session manager
├── Policy/capability gate
├── Retriever planner
├── Model router
├── Tool dispatcher
├── Honey context assembler
├── Continual Harness
│   ├── checkpoint state
│   ├── summarize/refine state
│   ├── rollback point management
│   ├── context-window refresh
│   └── handoff packet creation
├── Reasoning Bank
│   ├── Success Verification Grade Logs
│   ├── task trajectories
│   ├── verification results
│   ├── recovery records
│   ├── audit-ready exports
│   └── RLVR candidate extraction
└── Event/audit logger
```


### Continual Harness job

It should manage **working state**, not claim durable semantic truth:

- Session checkpoints.
- Compression/refresh of active context.
- State diffs.
- Rollback after a failed tool/action.
- Handoff packets between models or nodes.
- Bounded continuation after context pressure.
- Comparison of predicted vs verified task state.


### Reasoning Bank job

It stores only execution evidence, especially your proposed **Success Verification Grade Logs**:

```text
Successful task trajectory
  + verified tool outputs
  + artifacts/hashes
  + test/lint/citation results
  + approval/audit verdict
  = Success Verification Grade Log
```

Your correction is technically important: do not use arbitrary failure logs as positive RLVR training trajectories. Failures remain valuable as **negative examples**, regression fixtures, and verifier tests—but they should not be promoted as successful policies.

Use three datasets:


| Dataset | Contains | Training/evaluation use |
| :-- | :-- | :-- |
| Success Verification Grade Logs | Verified successful trajectories | Positive RLVR/behavior data |
| Failure/incident logs | Failed actions, broken tools, policy violations | Regression tests, negative preference data, verifier hardening |
| Unverified raw events | Everything else | Not training material; retained for audit/forensics under retention policy |

The proposal already frames Reasoning Bank as a multi-model execution ledger and recovery layer, while the continual harness handles reset-free adaptation and rollback. Folding both into OmniRoute makes the runtime boundary clean.[^7_1]

______________________________________________________________________

## Corpus-first build plan

You are right that a 50–100 file pilot is not your intended end state. I was recommending it as an integration proof, not as the corpus project itself. If you are building the full 10,000+ document corpus now, do it **corpus-first**, but do not let an LLM serially “understand” all 10,000 files before the mechanical pipeline exists.

The right distinction:

```text
Build the entire corpus inventory now.
Compile and semantically enrich it in deterministic batches.
Do not wait to create runtime/retrieval controls until every page is hand-curated.
```


### Full-corpus sequence

```text
Phase 0 — Freeze inputs
  → Identify all repositories, device exports, docs, logs, notes, media,
    conversation exports, references, and archives.
  → Assign source roots and ownership.
  → Snapshot/checksum them.

Phase 1 — Mechanical corpus build
  → Copy/register raw files.
  → Generate hashes.
  → Classify MIME/type/encoding.
  → Extract text/OCR/transcripts.
  → Generate per-file manifest.
  → Generate canonical IDs.
  → Build folder MAPs.
  → No LLM judgment required for this phase.

Phase 2 — Structural corpus build
  → Chunk normalized text.
  → Create lexical index.
  → Create embeddings.
  → Extract code AST/index code repositories.
  → Build graph nodes/edges from deterministic sources.
  → Build Terrestrial Brain SQL/graph read model.
  → Build CodeReviewGraph read model.

Phase 3 — Controlled semantic enrichment
  → Extract entities, tools, skills, models, runtimes, agents, claims,
    decisions, procedures, unresolved questions.
  → Stage rather than auto-promote.
  → Deduplicate and conflict-check.
  → Compile the OpenWiki/Obsidian pages.
  → Generate MOCs and cross-links.

Phase 4 — OmniRoute activation
  → Attach Honey bootstrap.
  → Enable Task Observer.
  → Route all new daily sessions through OmniRoute.
  → Use the corpus from day one as the retrieval substrate.

Phase 5 — Home-node audit/training cycle
  → Periodic P2P collection of mobile/tablet logs.
  → Cross-Agent Auditor runs only on collected session batches.
  → Red Auditor receives selected batch/snapshot in isolation.
  → Verified successful trajectories become Success Verification Grade Logs.
  → Approved training/export job runs separately.
```

This gives you the universal D.U.M.B.A.S.S. control layer without pretending that a model can reliably reason over all 10,000 files in one context window.

### Full corpus ingestion throughput

Parallelize by **deterministic job type**, not by letting ten LLM agents mutate the same vault:

```text
Worker 1: file inventory + hashing
Worker 2: document text extraction/OCR
Worker 3: audio/video transcription
Worker 4: code repository inventory + AST extraction
Worker 5: metadata and manifest generation
Worker 6: Markdown normalization
Worker 7: chunk registry and lexical index
Worker 8: embedding/index build
Worker 9: graph construction
Worker 10: staged semantic extraction
```

All workers must write through durable queues or staging directories. Only a promotion/merge worker writes canonical compiled wiki records and graph updates.

______________________________________________________________________

## Your daily assistant flow

Your actual on-device workflow is coherent. Model it as **small executor + larger query/planner**, with home-node expansion when available.

```text
Voice/text input
  → VAD
  → STT
  → small on-device execution/router model
  → OmniRoute session policy + Honey context package
  → query model decides:
       answer locally
       retrieve D.U.M.B.A.S.S.
       use terminal/NPU tool
       call frontier model/API
       ask user a clarifying question
  → frontier/local response returns
  → query model converts result into:
       answer
       metaprompt
       tool plan
       implementation request
       clarification question
  → small executor carries out allowed local actions
  → TTS returns spoken response
  → OmniRoute emits events and stages verified extractable results
```


### Device roles

| Mode | Small executor | Query/planner | Main job |
| :-- | :-- | :-- | :-- |
| Mobile offline | NPU-bound nano/small model | Local larger model if available | Intent, local tools, retrieval-lite, voice interaction |
| Mobile connected | Small device executor | Frontier/API model through OmniRoute | Query, research, planning, meta-prompting |
| Home P2P | Small model remains safety/router | Larger local/home model becomes executor too | Bigger code/data jobs and peer services |
| Audit/training window | Daily agents do not stop | Home-node batch services | Collect logs, audit, curate success-grade trajectories, prepare training/export |

That matches your stated distinction: the bigger query model can become an executor at home, while the phone keeps a small NPU-resident model responsible for local orchestration and no-overlap scheduling.

______________________________________________________________________

## MemOS and Memsearch

Neither replaces the whole D.U.M.B.A.S.S. They are optional adapters with narrow potential roles.

### MemOS

**Do not replace mem0 with MemOS on day one.**

MemOS is a memory-management system that presents unified store/retrieve/manage operations and supports multiple memory forms, including knowledge bases, tool/skill-related memory, graph/vector mechanisms, and local deployment options.[^7_2][^7_3]

In your architecture, it can occupy one of two roles:


| Option | MemOS role | Recommendation |
| :-- | :-- | :-- |
| A: Replace mem0 adapter only | Episodic/personal/agent memory backend | Best initial evaluation path |
| B: Add as a memory federation adapter | OmniRoute queries MemOS alongside mem0/OB1 during evaluation | Good for comparison, more complexity |
| C: Replace D.U.M.B.A.S.S. | Full corpus/memory authority | No. Do not do this. |

Start with **Option A** only if it can pass your contracts:

```text
- Local/self-hosted operation.
- Export/import of all records.
- Stable record IDs.
- Explicit deletion and retention controls.
- Provenance support.
- Read/write audit trail.
- Can keep unverified model output in staging.
- Does not require it to own your canonical corpus.
- Can be wrapped as an OmniRoute MemoryAdapter.
```

If it fails those, keep mem0 as episodic memory and leave MemOS out.

### Memsearch

Memsearch is even narrower: it captures coding-agent conversations, indexes them with hybrid search, and recalls relevant context, including with a local ONNX embedding option.[^7_4]

In your system it belongs here:

```text
Memsearch = optional developer-session recall sidecar

Agent coding session
  → conversation/tool trace
  → Memsearch index
  → relevant prior coding-session recall
  → returned through OmniRoute as one retrieval source
```

It should **not**:

- Replace Terrestrial Brain.
- Replace CodeReviewGraph.
- Replace the Markdown wiki.
- Replace mem0.
- Write directly into the canonical corpus.
- Become a universal memory source without validation.

So:

```text
mem0/MemOS = episodic agent/session memory candidate
Memsearch = developer conversation recall candidate
Terrestrial Brain = static corpus retrieval
CodeReviewGraph = code/graph/vector retrieval
Reasoning Bank = verified task trajectory and success-log store
```


______________________________________________________________________

## Immediate deliverables

Before coding the whole stack, create these seven documents in the corpus. They are the minimum contract package.

```text
protocols/
├── 01_dumbass-core-architecture.md
├── 02_omniroute-control-plane-contract.md
├── 03_graph-and-vector-retrieval-contract.md
├── 04_task-observer-worker-contract.md
├── 05_honey-launch-context-contract.md
├── 06_success-verification-grade-log-contract.md
└── 07_device-query-executor-routing-contract.md
```


### Specific decisions to write now

1. **Graph is core**: Terrestrial Brain and CodeReviewGraph are mandatory query arms, not optional plugins.
2. **OmniRoute role**: control-plane routing harness and mandatory gateway; not a chat TUI or single agent persona.
3. **Task Observer role**: registered OmniRoute worker; receives ephemeral grants; returns result envelopes.
4. **Honey role**: mandatory launch-time context/skill compression package.
5. **Reasoning Bank + Continual Harness**: internal OmniRoute subsystems.
6. **Corpus strategy**: full mechanical corpus build first; semantic enrichment is staged/batched.
7. **Training strategy**: home-node, batch-based, success-verification-grade trajectories only for positive RLVR promotion.
8. **Memory adapters**: mem0 stays episodic baseline; MemOS is a controlled replacement experiment; Memsearch is a coding-history sidecar.

## Bottom line

Your corrected operating structure is:

```text
OpenWiki / assistant APK / Hermes / DSH
               │
               ▼
         OmniRoute control plane
  ├─ Honey for Devs launch compression
  ├─ Task Observer dispatch
  ├─ Continual Harness
  ├─ Reasoning Bank
  ├─ policy / tools / models / budgets
  └─ retrieval fusion
       ├─ Terrestrial Brain / OB1
       ├─ CodeReviewGraph / Graphify / Graph DB
       ├─ lexical + vector indexes
       └─ mem0 or a tested MemOS adapter
               │
               ▼
Canonical Git corpus + compiled Markdown wiki + code repositories
```

Build the full corpus inventory and derived retrieval infrastructure now. Do not wait for an LLM to comprehend it all. Then use OmniRoute to make every daily query and agent session consume the same graph-backed, corpus-derived D.U.M.B.A.S.S. system.

<div align="center">⁂</div>

[^7_1]: PROPOSAL_V2_CORRECTED_WIKI_TERMINOLOGY_AND_s_tier_ALTERNATIVE.md.txt

[^7_2]: https://github.com/MemTensor/MemOS

[^7_3]: https://deepwiki.com/MemTensor/MemOS

[^7_4]: https://zilliztech.github.io/memsearch/


---

# So I have my main corpus inside of my GitHub repository with my obsidian Vault link to that and what should I be using for the SQL database and is that the same one doesn't mem 0 and Omni route have their own specific services that I have to use or can I plug them into my own do they send use the same one or do they have two different does omni routes one that it builds itself?

Use **PostgreSQL + pgvector as your shared D.U.M.B.A.S.S. data platform** on the home/control node, plus a separate graph database for CodeReviewGraph/Terrestrial Brain relationships. Keep OmniRoute’s own SQLite database separate; do not try to force it to use your Postgres unless OmniRoute officially adds that backend.

Your GitHub repo plus linked Obsidian vault stays the canonical file layer. Databases are derived operational stores built from that repository.[^8_1]

## Short answer

You will have **multiple databases**, not one:


| Component | Database | Same DB instance? | Same tables? |
| :-- | :-- | --: | --: |
| Canonical corpus | Git repo + Markdown/assets | N/A | N/A |
| OmniRoute | Its own SQLite WAL file | **No** | No |
| mem0 | Your Postgres + pgvector is a good choice | **Yes, same Postgres server** | **No, separate database/schema** |
| Terrestrial Brain / OB1 | Your Postgres + pgvector | **Yes** | No |
| CodeReviewGraph | Graph database | No; separate service | No |
| Reasoning Bank | Postgres or SQLite initially; Postgres at home | Yes, same server | No |
| OpenWiki / Obsidian | Files in Git vault | N/A | N/A |

The clean design is:

```text
GitHub repo + local Obsidian vault
            │
            ▼
    Corpus build/index pipeline
            │
 ┌──────────┼───────────────────────┐
 │          │                       │
 ▼          ▼                       ▼
Postgres   Graph DB              OmniRoute SQLite
+pgvector  CodeReviewGraph       own internal state
OB1        Terrestrial Graph     sessions/config/cache
mem0       AST/code graph        routing/audit internals
Reasoning  vector retrieval
Bank
```


## Use PostgreSQL + pgvector

For your main structured/vector platform, use:

```text
PostgreSQL 16+
pgvector extension
```

Why:

- Relational records for source manifests, chunks, claims, decisions, jobs, sync state, success-verification logs, and permissions.
- Native vector similarity search through `pgvector`.
- Proper concurrency and durability for your home-node batch jobs.
- One server can host separate databases or schemas for OB1, mem0, Reasoning Bank, and corpus metadata without merging their ownership models.
- It is a good fit for a peer/home-node service that your phone/tablet can reach only when you intentionally connect.

Mem0’s own self-hosted server stack uses Postgres with pgvector by default; its documentation also supports configuring alternative vector stores, but Postgres/pgvector gives you the least fragmented deployment for your design.[^8_2][^8_3]

### Recommended Postgres layout

Use one Postgres **server**, with separate logical databases:

```text
PostgreSQL server: dumbass-postgres

databases:
├── corpus_meta
│   ├── source records
│   ├── normalized asset metadata
│   ├── chunks
│   ├── claims
│   ├── decisions / ADRs
│   ├── manifests
│   ├── export bundle records
│   └── ingestion job state
│
├── terrestrial_brain
│   ├── static corpus chunks
│   ├── vector embeddings
│   ├── wiki entities
│   ├── relationships mirrored from graph DB
│   ├── semantic retrieval views
│   └── retrieval evaluation data
│
├── mem0_service
│   ├── Mem0-owned tables
│   ├── episodic memories
│   ├── memory history
│   └── Mem0 vector collections
│
├── reasoning_bank
│   ├── Success Verification Grade Logs
│   ├── validated trajectories
│   ├── handoff records
│   ├── verifier outcomes
│   ├── audit batches
│   └── RLVR candidate staging
│
└── ops_audit
    ├── cost events
    ├── sync status
    ├── health checks
    ├── policy decisions
    └── service event summaries
```

Use a separate database role for each service:

```text
corpus_ingestor      → write corpus_meta; read approved corpus views
terrestrial_service  → read corpus_meta; write terrestrial_brain
mem0_service         → full access only to mem0_service
reasoning_service    → write reasoning_bank
omniroute_adapter    → read scoped views; write ops_audit
auditor_readonly     → read approved snapshots only
red_auditor          → isolated export/snapshot, no direct production DB access
```

Do **not** give every service a `postgres` superuser credential.

## Graph database: separate service

Postgres + pgvector is not a substitute for the graph database you said is mandatory.

Use a dedicated graph database for the D.U.M.B.A.S.S. graph arm:

```text
Graph database
├── Knowledge graph
│   ├── sources
│   ├── chunks
│   ├── claims
│   ├── decisions
│   ├── agents
│   ├── tools
│   ├── models
│   ├── runtimes
│   ├── devices
│   └── projects
│
└── CodeReviewGraph
    ├── repos
    ├── commits
    ├── files
    ├── AST symbols
    ├── APIs
    ├── imports
    ├── calls
    ├── tests
    ├── configs
    └── code-to-document links
```

The graph service and Postgres should share stable IDs:

```text
source:...
chunk:...
claim:...
decision:...
repo:...
file:...
symbol:...
agent:...
tool:...
runtime:...
```

But they should not try to be the same database.

```text
Postgres = structured records, vectors, sessions, logs, SQL filtering.
Graph DB = traversals, dependencies, impact analysis, relationship retrieval.
```

Your proposal already treats Graphify as AST/knowledge-graph mapping and CodeReviewGraph as cross-agent graph code checking. Make both core derived services fed from your Git corpus and repository snapshots.[^8_1]

## OmniRoute’s database

Based on OmniRoute’s current database documentation: **it builds and manages its own SQLite database**.

Its primary store is:

```text
~/.omniroute/storage.sqlite
```

It uses SQLite in WAL mode, and it documents encryption for sensitive fields. OmniRoute’s current official storage backend is SQLite; current feature requests/discussions describe Postgres as a requested future external durable-state backend, rather than a generally available standard replacement.[^8_4][^8_5][^8_6]

So the answer is:

- **Yes**, OmniRoute creates/uses its own database.
- **No**, do not point OmniRoute at your Postgres as if it were its native database.
- **Yes**, OmniRoute should query or call adapters that access your Postgres/graph/mem0 services.
- **No**, its SQLite should not become the D.U.M.B.A.S.S. master corpus database.

Correct division:

```text
OmniRoute SQLite:
- Internal routing/configuration state.
- Provider/model configuration.
- API keys/secrets or encrypted settings.
- Its own audit/session/cache data.
- Local service bookkeeping.

Your Postgres:
- Corpus-derived structured state.
- Terrestrial Brain.
- Reasoning Bank.
- Evaluation data.
- Success Verification Grade Logs.
- Long-lived audit summaries.

Graph DB:
- Knowledge graph.
- CodeReviewGraph.
- Graph/vector structural retrieval.
```

Do not directly write to OmniRoute’s SQLite file from other services. Use its API or documented extension path only.

## mem0: can it use your database?

**Yes.** Mem0 can be configured to use infrastructure you run. It is a memory layer on top of a vector backend; it does not require you to use a separate hosted Mem0 database.

For self-hosting, Mem0’s server setup uses a Mem0 API service plus Postgres/pgvector by default. Its open-source configuration supports selectable vector-store backends; without explicit configuration, library defaults can include local Qdrant and a local SQLite history database, while the self-hosted server defaults to Postgres + pgvector.[^8_3][^8_7][^8_2]

For your case:

```text
mem0 API service
   │
   ├── Postgres database: mem0_service
   ├── pgvector extension: semantic memory retrieval
   └── Mem0-owned schema/tables/history
```

That means:

- Same **Postgres server** as your other D.U.M.B.A.S.S. databases: yes.
- Same **database** as Terrestrial Brain: better not.
- Same **tables** as your custom corpus/chunk store: no.
- Same **embeddings/indexes** as your corpus vector store: do not assume so.
- Same **API contract** as OmniRoute: no; OmniRoute calls Mem0 through an adapter/API.


### Why not merge mem0 and Terrestrial Brain?

Their write semantics are different:

```text
mem0:
- episodic/user/agent memory
- selective promotion from conversations
- update/merge/delete memory behavior
- short/medium-lived operational context

Terrestrial Brain:
- static corpus-derived knowledge
- source-controlled and reproducible
- Git revision/provenance tied
- rebuilt from corpus/index jobs
```

If you mix them, a session memory can contaminate the static corpus retrieval layer, and you lose the ability to rebuild Terrestrial Brain exactly from Git.

## Recommended service wiring

```text
                         GitHub repository
                    + local Obsidian vault
                              │
                              │ Git pull / local changes
                              ▼
                  corpus-normalize / ingest jobs
                              │
        ┌─────────────────────┼──────────────────────┐
        │                     │                      │
        ▼                     ▼                      ▼
 corpus_meta Postgres   Terrestrial Brain        Graph database
 sources/chunks/etc.   static SQL + vectors      CodeReviewGraph +
                                                knowledge graph
        │                     │                      │
        └─────────────────────┼──────────────────────┘
                              │
                              ▼
                           OmniRoute
              local SQLite for OmniRoute itself
                              │
          ┌───────────────────┼─────────────────────┐
          │                   │                     │
          ▼                   ▼                     ▼
      mem0 API          Task Observer          Honey for Devs
    episodic memory     worker/controller      context package
          │                   │                     │
          └───────────────────┴─────────────────────┘
                              │
                              ▼
             Hermes / DSH / phone assistant APK /
                  OpenWiki TUI / Claude Code worker
```


## What runs where

### On your daily device

Keep it light:

```text
- Local Git/Obsidian vault working copy.
- OmniRoute local service and its own SQLite file.
- Phone assistant APK.
- Local small executor/NPU coordinator.
- VAD/STT/TTS.
- Retrieval-lite bundle or cached read-only subset.
- Optional local mem0 only if resources permit.
```


### On home node

Run the heavy durable services:

```text
- PostgreSQL + pgvector.
- Graph database.
- Terrestrial Brain/OB1 service.
- CodeReviewGraph/Graphify ingestion and query service.
- Mem0 API service.
- Reasoning Bank database/services.
- Corpus index/build jobs.
- Cross-Agent Auditor batch jobs.
- Red Auditor isolated snapshot/export jobs.
- Training preparation/export jobs.
```

That matches your stated plan: daily device operation stays independent; logs and successful trajectories are collected and audited when you connect peer-to-peer at home, rather than forcing full database/audit work into every prompt.[^8_1]

## Do this first

1. Deploy **one Postgres 16+ server with pgvector** on the home node.
2. Create the five separate databases:

```text
corpus_meta
terrestrial_brain
mem0_service
reasoning_bank
ops_audit
```

3. Deploy the graph database separately.
4. Keep OmniRoute on its default SQLite database.
5. Configure Mem0 to use `mem0_service`, not an uncontrolled default local Qdrant/SQLite deployment.
6. Build Terrestrial Brain and CodeReviewGraph from your Git/Obsidian corpus—not by manually entering knowledge into databases.
7. Give OmniRoute adapters/endpoints for:

```text
terrestrial.query
codereviewgraph.query
mem0.retrieve
reasoningbank.log
```

8. Do not allow any component except controlled ingestion/promotion jobs to write into `corpus_meta`, Terrestrial Brain, or the graph database.

The clean answer: **one Postgres server, multiple isolated databases; one separate graph database; OmniRoute keeps its own SQLite; Mem0 uses its own logical Postgres database on your server; Git/Obsidian remains the canonical corpus.**

<span style="display:none">[^8_10][^8_11][^8_12][^8_13][^8_14][^8_15][^8_16][^8_17][^8_18][^8_19][^8_20][^8_21][^8_22][^8_23][^8_8][^8_9]</span>

<div align="center">⁂</div>

[^8_1]: PROPOSAL_V2_CORRECTED_WIKI_TERMINOLOGY_AND_s_tier_ALTERNATIVE.md.txt

[^8_2]: https://railway.com/deploy/mem0-the-memory-layer-for-personalized-ai--mem0

[^8_3]: https://docs.mem0.ai/open-source/overview

[^8_4]: https://github.com/diegosouzapw/OmniRoute/wiki/Database-Guide

[^8_5]: https://github.com/diegosouzapw/OmniRoute/issues/5409

[^8_6]: https://github.com/diegosouzapw/OmniRoute/issues/8037

[^8_7]: https://docs.mem0.ai/components/vectordbs/overview

[^8_8]: https://github.com/mem0ai/mem0

[^8_9]: https://docs.mem0.ai/components/vectordbs/config

[^8_10]: https://mem0.ai/blog/vector-databases-and-memory-for-ai-agents

[^8_11]: https://docs.mem0.ai/components/vectordbs/dbs/mongodb

[^8_12]: https://github.com/mem0ai/mem0/blob/main/docs/components/vectordbs/overview.mdx

[^8_13]: https://virtuslab.com/blog/ai/git-hub-all-stars-2/

[^8_14]: https://github.com/mem0ai/mem0/discussions/3541

[^8_15]: https://github.com/diegosouzapw/OmniRoute/issues/8620

[^8_16]: https://github.com/diegosouzapw/OmniRoute/issues/8075

[^8_17]: tools.obsidian.integration

[^8_18]: projects.ai.local_deployment.integration_orchestration

[^8_19]: https://www.perplexity.ai/search/474d4143-d735-4392-9b53-0527393e5f0d

[^8_20]: https://www.perplexity.ai/search/e63bde20-723c-47f3-9f38-4be7f3bbbbf6

[^8_21]: https://www.perplexity.ai/search/ba794bb4-88fc-4d39-b93d-23da5fa5ab31

[^8_22]: https://www.perplexity.ai/search/12c0b665-4aec-4757-803f-9a98b1b71845

[^8_23]: https://www.perplexity.ai/search/f83d54de-1cb5-45a0-925b-967f543d645a


---

# So what are you saying here? I make my own Postgres SQL vector, or is that a service that I need to pay for, or what? Is that a different app?How does that work?Because as far as my graph was concerned, I was just going to link my graphify to my Obsidian vault, and yeah, the Obsidian vault with graphify plugged in, notebook LMPY plugged in, and my GitHub repo are absolutely the source of truth. Like, that's where everything's going to live.

You do **not** need to pay for a database service or create a second “master vault.” PostgreSQL is free open-source software you run as a local background service—basically a database app/server. `pgvector` is a free add-on that gives Postgres vector-search capability.[^9_1][^9_2]

Your GitHub repo + local Obsidian vault remain the source of truth exactly as you said. Graphify, Obsidian, NotebookLM-PY, Postgres, and any future graph/vector indexes all derive from that same vault; they do not replace it.[^9_3][^9_4]

## What Postgres actually is

Think of it like this:

```text
GitHub + Obsidian vault
= your actual library and master documents

PostgreSQL
= an indexed catalog/database generated from that library

pgvector
= a search feature inside that catalog for “find similar meaning”
```

It is a program you install and run on a device/node that stays available, likely later your home node—not an external company you must pay.

You have three choices:


| Option | What it is | Cost | Best use |
| :-- | :-- | --: | :-- |
| Self-hosted Postgres | You run Postgres on your own home computer/server/node | Free software | Your intended home-node D.U.M.B.A.S.S. |
| Managed Postgres | A cloud company runs it | Usually paid after free tier | Only if you want external access/maintenance |
| No Postgres yet | Files, Git, Obsidian, Graphify, and local indexes only | Free | Fine while you are still compiling the vault |

For your system, do **not** buy a managed database just because you are setting up the corpus. You can run it locally later when you have the always-on home node. PostgreSQL and pgvector are open source and can be installed via packages, Docker, Homebrew, or compiled; pgvector is explicitly an open-source Postgres extension for vector similarity search.[^9_2][^9_1]

## Your actual source of truth

This is the correct model:

```text
Master GitHub repository
        ↕ Git pull / commit / push
Local Obsidian vault
        ↕ same files
Markor / OpenWiki / file manager
        ↕ same files
Graphify
        → reads/indexes repository and vault material
NotebookLM-PY
        → reads selected vault sources / writes exports back as files
```

That is **one file-based source of truth**.

Your vault should contain:

```text
master-vault/
├── raw-sources/
├── normalized/
├── wiki/
├── projects/
├── protocols/
├── runbooks/
├── decisions/
├── manifests/
├── schemas/
├── tools/
├── skills/
└── exports/
```

Graphify is compatible with this direction: it is designed to turn a codebase and associated docs, SQL schemas, configs, and PDFs into a queryable knowledge graph.[^9_3]

NotebookLM-PY can also operate from your vault root and place generated artifacts such as reports, mind-map JSON, and transcripts back into the Obsidian knowledge graph. Treat those as **generated artifacts to review**, not automatic truth.[^9_4]

## What Postgres would add later

Postgres is not another place for you to write notes manually.

It would hold generated/queryable records like:

```text
Vault Markdown + code + assets
        │
        ▼
corpus compiler/indexer
        │
        ├── file manifest
        ├── extracted text
        ├── stable chunks
        ├── metadata
        ├── embeddings
        ├── entities
        ├── claims
        ├── relationships
        └── graph synchronization records
        │
        ▼
Postgres + pgvector
```

Then OmniRoute can ask it questions programmatically:

```text
“Find chunks about OmniRoute’s session startup contract.”
“Find all files related to Honey for Devs and Task Observer.”
“Find decisions involving Graphify and CodeReviewGraph.”
“Find content semantically close to this query.”
```

But the answer always includes the original vault path, Git revision, source ID, and chunk reference. The underlying Markdown/file remains authoritative.

## You do not need it first

Because you are building the corpus now:

1. Build the vault/repositories and Git/Obsidian structure.
2. Link Graphify to the vault/repositories.
3. Use Graphify’s graph/index output as your first graph retrieval layer.
4. Use NotebookLM-PY only as a research/analysis importer-exporter.
5. Generate `MAP.md` and `manifest.jsonl`.
6. Build chunk records and local lexical search.
7. Add Postgres later when you need:
    - An always-on shared home-node query service.
    - Durable SQL querying across the whole corpus.
    - Vector search shared across agents/devices.
    - Reasoning Bank / success-log batch processing.
    - More controlled graph-to-corpus synchronization.

You are not required to install Postgres right now just because mem0 or OmniRoute exists.

## Graphify and graph database

Your plan is valid:

```text
Obsidian/GitHub vault
       │
       ▼
Graphify
       │
       ▼
Graphify graph/index/query layer
```

That can be your initial graph database/retrieval arm if Graphify provides the persistent graph/index and query APIs you need. Graphify is intended to produce a queryable knowledge graph from code and supporting artifacts.[^9_3]

The reason I mentioned a separate graph database is **not** because you must install Neo4j or another database immediately. It is because the graph needs persistent queryable storage somewhere.

First verify what Graphify itself uses and exposes:

- Where does its graph data live?
- Is it persistent across rebuilds?
- Can OmniRoute query it through CLI, HTTP, MCP, or a library?
- Can it index Markdown and full vault docs, not only code?
- Does it provide vectors as well as graph traversal?
- Can it update incrementally from Git changes?
- Can every node/edge link back to a vault path, source ID, commit, and line/chunk?

If Graphify satisfies those requirements, **use Graphify as your initial graph service**. Do not install another graph database merely for the word “graph.”

Later, if Graphify needs a backing graph engine or does not meet cross-vault/query needs, then you decide whether to add one. Your canonical vault does not change either way.

## Where OmniRoute and mem0 fit

They do not need to share one database.

```text
Your vault
= source truth

Graphify
= graph/index built from vault

OmniRoute
= routing/session/extraction service;
  it has its own internal SQLite storage

mem0
= optional episodic-memory service;
  it can use its own default storage or later be configured
  against a Postgres-backed setup
```


### OmniRoute

OmniRoute currently uses its own local SQLite database with WAL journaling as its primary/internal store. You let it create and manage that database. Do not manually mix your vault data into it.[^9_5]

```text
OmniRoute SQLite
= its internal service state

Vault
= your master source truth

Graphify
= your graph/index derivative
```


### mem0

Mem0 is **not required to have a separate paid service**. It can be self-hosted. It is an episodic memory layer, separate from your static vault and Graphify corpus graph. The self-hosted version can use Postgres + pgvector later, but it does not force you to buy a cloud subscription.[^9_6][^9_7]

For now, conceptually:

```text
mem0
= “remember selected session/user/agent facts”

Graphify
= “how files, code, docs, tools, decisions, and components relate”

Obsidian/GitHub vault
= “the actual documents and knowledge artifacts”
```

Do not replace mem0 with Graphify, and do not replace Graphify with mem0. They solve different problems.

## Clean current setup

Your current architecture can simply be:

```text
GitHub repository
   ↕
Obsidian vault
   ├── Graphify indexes it
   ├── NotebookLM-PY analyzes selected source sets
   ├── OpenWiki maintains/navigates it
   └── Git tracks revisions

OmniRoute
   ├── runs separately
   ├── maintains its own SQLite state
   ├── calls Graphify for graph retrieval
   ├── calls vault/manifest search for file retrieval
   └── calls mem0 for episodic memory

mem0
   └── runs separately as episodic-memory service
```

No paid Postgres. No new cloud database. No second handwritten repository.

## Later home-node upgrade

When you are ready for an always-on home service, add:

```text
Postgres + pgvector
```

Then use it as a **derived index and operations database**, not a replacement vault:

```text
Vault / GitHub / Obsidian
          │
          ▼
compiler/indexer
          │
          ├── Postgres + pgvector
          ├── Graphify graph/index
          ├── mem0 backend
          └── audit/training logs
```

At that point, you can choose to host mem0’s backend on your own Postgres instance, while OmniRoute continues using its own SQLite unless its official configuration adds external Postgres support.[^9_8][^9_5][^9_6]

## Bottom line

- **No**, you do not need to buy a SQL/vector database service.
- **No**, Postgres does not replace your Obsidian vault or GitHub repo.
- **Yes**, Postgres is a separate self-hosted app/service you may add later.
- **Yes**, Graphify linked to your vault can be your initial core graph/index layer.
- **Yes**, GitHub repo + Obsidian vault remain the actual source of truth.
- **OmniRoute** uses its own SQLite for itself.
- **mem0** is an optional separate episodic-memory service; it can later run on your own Postgres/pgvector backend.
- Start the corpus and Graphify integration now; defer Postgres until you are standing up the home-node persistent services.

<span style="display:none">[^9_10][^9_11][^9_12][^9_13][^9_14][^9_15][^9_16][^9_17][^9_18][^9_19][^9_9]</span>

<div align="center">⁂</div>

[^9_1]: https://www.postgresql.org/about/news/pgvector-070-released-2852/

[^9_2]: https://github.com/pgvector/pgvector

[^9_3]: https://github.com/Graphify-Labs/graphify

[^9_4]: https://github.com/teng-lin/notebooklm-py?ref=legaled.ai

[^9_5]: https://github.com/diegosouzapw/OmniRoute/wiki/Database-Guide

[^9_6]: https://railway.com/deploy/mem0-the-memory-layer-for-personalized-ai--mem0

[^9_7]: https://docs.mem0.ai/open-source/overview

[^9_8]: https://github.com/diegosouzapw/OmniRoute/issues/8037

[^9_9]: https://github.com/teng-lin/notebooklm-py/blob/main/docs/installation.md

[^9_10]: https://github.com/topics/google-notebooklm

[^9_11]: https://github.com/marketplace/actions/setup-pgvector

[^9_12]: https://www.datacamp.com/tutorial/pgvector-tutorial

[^9_13]: https://github.com/pgvector

[^9_14]: https://github.com/topics/notebooklm-api

[^9_15]: https://github.com/topics/graphify?l=typescript

[^9_16]: https://www.reddit.com/r/ClaudeCode/comments/1sme1zw/graphify_vs_codereviewgraph_which_is_better_for/

[^9_17]: https://skillsllm.com/skill/notebooklm-py

[^9_18]: https://sourceforge.net/projects/notebooklm-py.mirror/

[^9_19]: https://www.linkedin.com/posts/jonathanlellouche_github-teng-linnotebooklm-py-unofficial-activity-7438592539361869824-Nd9c


---

# So until I get my home node up I'm running all of this off of a VM in my Google cloud as far as Omni route goes so what else do I need to install on that VM cuz right now I have trust real brain Omni route I'm going to be doing mem zero probably and then what else do I need to have running on that

On the Google Cloud VM, run the **runtime services only**. Your GitHub/Obsidian vault remains the source of truth; the VM hosts OmniRoute and the derived retrieval/memory services that agents call.

For your current plan, use Docker Compose and run: **OmniRoute, Terrestrial Brain, Graphify/CodeReviewGraph, Mem0, PostgreSQL+pgvector, Neo4j, and a reverse-proxy/Tailscale access layer.** OmniRoute itself keeps its own SQLite volume.[^10_1][^10_2]

## Required VM services

```text
Google Cloud VM
│
├── OmniRoute
│   └── model/API routing, session gateway, provider keys,
│       its own SQLite state
│
├── Terrestrial Brain / OB1
│   └── static corpus retrieval service
│
├── Graphify / CodeReviewGraph
│   └── code/docs graph extraction and graph-vector retrieval
│
├── PostgreSQL + pgvector
│   └── structured derived corpus records, vectors,
│       Terrestrial Brain data, Reasoning Bank data
│
├── Neo4j
│   └── graph storage for graph-backed memory/retrieval;
│       Mem0’s current self-hosted reference stack uses it
│
├── Mem0 API
│   └── episodic/session-memory service
│
├── OmniRoute adapters or retrieval gateway
│   └── calls Terrestrial Brain, Graphify, Mem0, and later
│       Reasoning Bank through controlled endpoints
│
├── Object/file staging volume
│   └── cloned corpus working copy, normalized outputs,
│       import staging, generated indexes, backups
│
└── Access/security
    ├── Tailscale preferred for private device-to-VM access
    ├── firewall rules
    ├── HTTPS reverse proxy only if you need browser/public access
    └── secret management
```

Do **not** run a separate paid vector service. `pgvector` is the free vector extension inside your self-hosted Postgres container.[^10_3][^10_4]

## Minimum deployment

If you want the smallest stack that still matches your architecture, deploy these first:


| Service | Required now | Why |
| :-- | --: | :-- |
| Docker Engine + Compose | Yes | Runs and manages the services |
| OmniRoute | Yes | Main routing/control gateway |
| OmniRoute persistent volume | Yes | Keeps its own SQLite database/config/state |
| PostgreSQL + pgvector | Yes | Shared derived SQL/vector store |
| Neo4j | Yes, if Mem0 graph mode and graph retrieval are core | Graph persistence for Mem0/knowledge graph workflows |
| Mem0 API | Yes, if you are using Mem0 now | Episodic agent/session memory |
| Terrestrial Brain / OB1 | Yes | Static corpus retrieval |
| Graphify / CodeReviewGraph | Yes | Graph-vector code and corpus retrieval |
| Git working clone | Yes | Read-only or controlled ingest source from your GitHub vault |
| Tailscale or equivalent private access | Yes | Keeps services off the open Internet |
| Backups | Yes | Database/volume recovery |

Mem0’s current documented self-hosted stack is an API container plus PostgreSQL with pgvector and Neo4j.[^10_2]

## Do not install yet

Do **not** add these until the core stack is alive and querying your corpus:

- Multiple alternate vector databases.
- Qdrant, Weaviate, Milvus, Chroma, Pinecone, and similar alternatives.
- A second graph database alongside Neo4j.
- Memsearch.
- MemOS.
- Langflow.
- CrewAI.
- Open Interpreter with host access.
- Full RLVR training infrastructure.
- Cross-Agent Auditor or Red Auditor live daemons.
- A public Nginx/Caddy endpoint unless you actually need browser access from outside your Tailscale/private network.

You already have enough moving pieces. Make the first architecture work before adding replacements for it.

## Service relationship

```text
Phone / tablet / desktop client
          │
          │ Tailscale/private network
          ▼
     OmniRoute :20128
          │
          ├── provider/API routing
          ├── local session policy
          ├── its own SQLite volume
          │
          ├── Terrestrial Brain / OB1 query API
          │       │
          │       └── Postgres + pgvector
          │
          ├── Graphify / CodeReviewGraph query API
          │       │
          │       └── Neo4j or its documented graph backend
          │
          ├── Mem0 API
          │       ├── Postgres + pgvector
          │       └── Neo4j
          │
          └── later: Reasoning Bank
                  └── Postgres database/schema
```

The GitHub/Obsidian vault feeds this system; it does not get replaced by it:

```text
GitHub repo + Obsidian vault
            │
            ▼
VM working clone / import staging
            │
            ├── Graphify indexes code/docs
            ├── Terrestrial Brain indexes compiled corpus
            ├── Postgres stores derived rows/vectors
            └── Neo4j stores derived graph relationships
```


## Storage layout

On the VM, use persistent volumes outside disposable containers:

```text
/opt/dumbass/
├── compose.yml
├── .env                    # chmod 600; never commit
├── corpus/
│   ├── vault-readonly/     # Git clone or controlled checkout
│   ├── inbox/
│   ├── normalized/
│   └── generated/
├── backups/
│   ├── postgres/
│   ├── neo4j/
│   ├── omniroute/
│   └── configs/
└── logs/
```

Docker volumes:

```text
dumbass_postgres_data
dumbass_neo4j_data
dumbass_omniroute_data
dumbass_mem0_data
dumbass_graphify_data
```

OmniRoute’s Docker guidance uses a persistent volume mounted at `/app/data`; its internal SQLite data should remain there and should not be mixed into your corpus folder.[^10_5][^10_1]

## Network rules

Do **not** expose all database ports publicly.


| Port/service | Public Internet | Tailscale/private network | Docker-internal |
| :-- | --: | --: | --: |
| OmniRoute `20128` | No | Yes | Yes |
| Postgres `5432` | No | Usually no | Yes |
| Neo4j Bolt `7687` | No | Usually no | Yes |
| Neo4j browser `7474` | No | Optional/admin only | Yes |
| Mem0 API | No | Through OmniRoute/admin only | Yes |
| Graphify | No | Through OmniRoute/admin only | Yes |
| Terrestrial Brain | No | Through OmniRoute/admin only | Yes |
| SSH `22` | Restrict to your IP/Tailscale | Yes | N/A |

For the initial VM setup, bind OmniRoute to loopback or the private Tailscale interface, not `0.0.0.0` on a public GCP address. OmniRoute’s own Docker documentation shows loopback binding as an option:

```text
127.0.0.1:20128:20128
```

and recommends a persistent data volume.[^10_6]

## OmniRoute install requirements

OmniRoute itself needs:

```text
- Docker container or Node installation
- Persistent data volume
- Strong initial/admin password
- API key protection
- Encryption key if you use encrypted-at-rest storage
- Provider API credentials added through its UI/config
- A stable private URL reachable by your devices
```

Current Docker docs show OmniRoute on port `20128`, with a persistent mounted data directory; its storage defaults to a SQLite database.[^10_7][^10_1][^10_5]

Do not expose provider API keys to every agent. Only OmniRoute should hold those keys. Agents/harnesses call OmniRoute with scoped client credentials.

## Mem0 requirements

If you deploy Mem0 now, it needs:

```text
- Mem0 API container
- Postgres + pgvector
- Neo4j
- Embedding-model/provider configuration
- LLM/provider configuration for memory extraction
- Auth/API key or internal-only Docker networking
- Persistent volumes for Postgres/Neo4j
```

Mem0’s self-host deployment guide specifically uses Mem0 API + Postgres/pgvector + Neo4j, started through Docker Compose.[^10_8][^10_2]

Important: Mem0’s extraction calls can incur API cost and send selected content to the configured LLM/embedding provider. If you want strict local-only operation, choose local-compatible extraction/embedding models only after verifying Mem0 supports your selected configuration. Do not assume “self-hosted Mem0” automatically means no data ever leaves the VM.

## Graphify requirements

Graphify should be deployed as the graph/code retrieval service, reading a **controlled clone** of your vault/repositories.

Graphify’s own materials say it can turn code, documentation, SQL schemas, configs, and PDFs into a queryable knowledge graph. Its on-premise deployment material supports Docker or Kubernetes, and its local MCP server flow uses Python 3.12 and `uv`.[^10_9][^10_10]

For your setup:

```text
Graphify input:
- controlled Git clone of your corpus/vault
- selected code repositories
- normalized docs/PDF text
- generated source manifests

Graphify output:
- graph/vector index
- code/document relationships
- query API or MCP endpoint

OmniRoute:
- calls Graphify only through its approved adapter
```

Do not point Graphify at a live mutable Obsidian folder with unrestricted write access. Mount the Git checkout read-only for indexing; use a separate controlled ingestion/update job when you pull new commits.

## Terrestrial Brain requirements

I cannot verify from public sources exactly which project/version you mean by “Terrestrial Brain,” so I cannot tell you its precise containers, database engine, or required ports.

Treat it as a separate service with this required contract:

```text
Inputs:
- Git revision or read-only vault checkout
- normalized corpus
- stable source/chunk IDs
- manifest metadata

Outputs:
- retrieval endpoint
- source/chunk provenance
- revision/index version
- ranked results
- health endpoint

Storage:
- its own database/schema/index directory
- no direct edits to the master vault
```

If Terrestrial Brain already includes its own SQL/vector backend, do **not** deploy duplicate Postgres/vector infrastructure for the same job until you inspect exactly what it uses. Its storage may replace the `terrestrial_brain` Postgres database described above, while Postgres remains needed for Mem0 and Reasoning Bank.

## First Compose stack

Your first `compose.yml` should conceptually contain:

```text
services:
  omniroute
  postgres
  neo4j
  mem0
  terrestrial-brain
  graphify
  task-observer
```

But start them in this order:

```text
1. postgres
2. neo4j
3. omniroute
4. mem0
5. terrestrial-brain
6. graphify
7. task-observer
```

Then test one endpoint at a time:

```text
Postgres healthy
→ Neo4j healthy
→ OmniRoute dashboard/API reachable privately
→ one provider routes through OmniRoute
→ Mem0 can write/retrieve a disposable test memory
→ Terrestrial Brain returns a source-cited vault result
→ Graphify returns a code/doc graph result
→ Task Observer can request retrieval through OmniRoute
```

Do not start Task Observer until the retrieval endpoints work independently.

## VM sizing

For the services above, do not use a tiny VM.

A reasonable non-model-serving starting target is:

```text
4 vCPU
16 GB RAM
100 GB SSD persistent disk minimum
```

More realistic if you index a 10,000+ document corpus, run Neo4j, Graphify, Postgres vectors, Mem0, and containers concurrently:

```text
8 vCPU
32 GB RAM
200–500 GB SSD persistent disk
```

The exact need depends on corpus size, embeddings, Graphify’s index behavior, Neo4j footprint, and whether Terrestrial Brain runs any local model. I would not claim a precise minimum without the actual storage/index specs.

## What you should do now

1. Install Docker Engine and Docker Compose on the GCP VM.
2. Set up a private Tailscale connection from phone/tablet to the VM.
3. Put your repository in a controlled Git checkout on the VM.
4. Deploy OmniRoute with its own persistent volume.
5. Deploy Postgres + pgvector and Neo4j.
6. Deploy Mem0 only after choosing the extraction/embedding provider.
7. Deploy Graphify against the read-only vault/repo clone.
8. Deploy Terrestrial Brain using its own documented requirements.
9. Wire all retrieval services into OmniRoute through adapters.
10. Add Task Observer last.
11. Add home-node auditing and Success Verification Grade Log processing later, when the home node exists.

The essential VM stack is: **OmniRoute + its SQLite, Postgres/pgvector, Neo4j, Mem0, Terrestrial Brain, Graphify/CodeReviewGraph, Docker volumes/backups, and private networking.**

<span style="display:none">[^10_11][^10_12][^10_13][^10_14][^10_15][^10_16]</span>

<div align="center">⁂</div>

[^10_1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/guides/DOCKER_GUIDE.md

[^10_2]: https://mem0.ai/blog/self-host-mem0-docker

[^10_3]: https://www.postgresql.org/about/news/pgvector-070-released-2852/

[^10_4]: https://hub.docker.com/r/pgvector/pgvector

[^10_5]: https://github.com/diegosouzapw/OmniRoute/wiki/de‐Environment

[^10_6]: https://github.com/diegosouzapw/OmniRoute

[^10_7]: https://github.com/diegosouzapw/OmniRoute/wiki/hi‐VM-Deployment-Guide

[^10_8]: https://docs.mem0.ai/migration/server-pgvector-upgrade

[^10_9]: https://github.com/Graphify-Labs/graphify

[^10_10]: https://graphify.net/

[^10_11]: https://github.com/diegosouzapw/OmniRoute/issues/2830

[^10_12]: https://github.com/topics/omniroute?l=dockerfile

[^10_13]: https://allisterantosik.com/blog/self-hosted-ai-developer-stack/

[^10_14]: https://skillsllm.com/skill/graphify-labs-graphify

[^10_15]: https://github.com/diegosouzapw/OmniRoute/wiki/Database-Guide

[^10_16]: https://github.com/pgvector/pgvector


---

# So why do I need docker engine compose anyway what does that have make anything easier or is that cheap er or is it for free I mean how does that even work I'm never even set up a docker and then what about this tail scale should I use this instead of like sshing my VM to my personal devices or what what's going to be the fastest and best looking graphics

**Docker is not required**, but it is probably the easiest way to run your VM stack cleanly. It is free on a Linux Google Cloud VM. Tailscale is not a graphical remote-desktop system; use it to create a private encrypted network, then use SSH for terminal work and Chrome Remote Desktop for the best practical GUI experience on your GCP VM.[^11_1][^11_2][^11_3]

## Docker in plain English

Docker lets you run each server component in its own isolated package called a **container**.

Without Docker, you manually install and maintain:

```text
Node.js version for OmniRoute
Python version/environment for Graphify
Postgres
pgvector extension
Neo4j
Mem0 API dependencies
system services
ports
startup/restart rules
logs
upgrades
```

With Docker, each service has its own self-contained environment:

```text
Container 1: OmniRoute
Container 2: Postgres + pgvector
Container 3: Neo4j
Container 4: Mem0
Container 5: Graphify
Container 6: Terrestrial Brain
```

They still run on your VM, use its RAM/CPU/disk, and communicate over a private Docker network. Docker does **not** mean cloud hosting, public exposure, or another company handling your data.

```text
Your GCP VM
└── Docker Engine
    ├── OmniRoute container
    ├── Postgres container
    ├── Neo4j container
    ├── Mem0 container
    └── Graphify container
```

Docker Engine is open-source container software. On a Linux VM you install Docker Engine and the Compose plugin directly; you do **not** need Docker Desktop. Docker Engine’s core is Apache-2.0 licensed, while the paid licensing issue people hear about is mainly Docker Desktop use by larger commercial organizations.[^11_4][^11_1]

## What Compose does

Docker Compose is a free tool that controls several Docker containers as **one named stack**.

You write one text config file, usually:

```text
compose.yaml
```

It records:

- Which services exist.
- Which image/version each one uses.
- What storage each service keeps.
- Which services may talk to each other.
- Which ports are available.
- Environment/config values.
- Start order and health checks.

Then you use one command:

```bash
docker compose up -d
```

That starts the full stack in the background.

Other useful commands:

```bash
docker compose ps        # What is running
docker compose logs -f   # Live logs
docker compose down      # Stop the stack
docker compose up -d     # Start again
docker compose pull      # Download updated images
```

Compose is specifically designed to define and run multi-container applications from one YAML file and manage their full lifecycle—start, stop, rebuild, status, logs, and one-off commands.[^11_2][^11_5]

### Why it helps your setup

Your intended VM has multiple services that must stay separated:

```text
OmniRoute
Postgres / pgvector
Neo4j
Mem0
Graphify
Terrestrial Brain
Task Observer
```

With Compose:

- OmniRoute upgrades without overwriting Postgres.
- A broken Graphify update does not break Mem0.
- You can restart only one service.
- Each component has its own persistent storage volume.
- You can back up the database volumes.
- You can rebuild the entire VM setup from Git/config if the VM dies.
- You can later move the stack from GCP to your home node with largely the same config.

The important division:

```text
compose.yaml
= declarative recipe for services

Docker volumes
= persistent service data

Git/Obsidian vault
= your actual source documents and source of truth
```


## Is it cheaper?

Docker itself is free. It does not directly reduce your Google Cloud VM bill.

It can make the VM **cheaper indirectly** because you can:

- Shut down services you are not using.
- Avoid duplicate/abandoned installs.
- Recreate a VM instead of paying to preserve a broken manual setup.
- Move the same stack to a home node later.
- Keep databases and indexes in persistent volumes while replacing only the VM/container layer.

But the actual cost drivers are still:

```text
- GCP VM CPU/RAM hours.
- Persistent SSD storage.
- Network egress.
- Frontier-model/API usage.
- Any external database/model services you choose.
```

For you, Docker’s real benefit is **reproducibility and separation**, not cost savings.

## Do you have to use Docker?

No. You could install every service natively with `apt`, Python virtual environments, Node, `systemd`, and manual configuration.

For a single service, native install is fine:

```text
One Linux VM
└── OmniRoute installed directly
```

For your target stack, native installs are a lot more fragile:

```text
One VM
├── Node environment
├── Python 3.12 / uv environment
├── Python packages
├── Java dependencies for Neo4j
├── Postgres / pgvector versions
├── Mem0 dependencies
├── Graphify dependencies
├── systemd units
├── port rules
└── upgrades that can conflict
```

So the recommendation is:

```text
Use Docker Compose for VM server services.
Use normal Git/Obsidian/Markor files for your vault.
Use SSH/Chrome Remote Desktop/Tailscale for access.
```

You do not need to learn every Docker concept before using it. Initially you need only:

```text
docker compose up -d
docker compose ps
docker compose logs -f <service>
docker compose restart <service>
docker compose down
```


## Tailscale versus SSH

This is not either/or.

```text
Tailscale = private encrypted network between your devices and VM.
SSH = terminal protocol you use over that network.
```

Tailscale uses a WireGuard-based private mesh and can create direct end-to-end encrypted device connections where the network permits, avoiding a public exposure path or bastion host. Tailscale also supports SSH authentication/authorization over the tailnet.[^11_3][^11_6]

### Recommended setup

```text
Phone
Tablet
GCP VM
Future home node
        │
        ▼
All join one private Tailscale tailnet
        │
        ├── SSH/terminal access to VM
        ├── OmniRoute private API access
        ├── Graphify/OB1 admin access if needed
        └── Later peer-to-peer home-node access
```

Then you can use either:

```bash
tailscale ssh your-user@your-vm
```

or conventional SSH through the private Tailscale hostname/IP:

```bash
ssh your-user@your-vm.tailnet.ts.net
```

Tailscale’s own SSH documentation says this can eliminate the need for a bastion host and typically avoids the extra latency that comes with one, while keeping connections private and end-to-end encrypted.[^11_3]

### Why it is useful on GCP

Without Tailscale:

```text
Your device
  → public GCP IP
  → exposed port 22
  → OpenSSH
```

You must manage:

- Public firewall rules.
- SSH keys.
- Public-IP scanning/noise.
- Restricting your IP if it changes.
- Public access for OmniRoute or any dashboard you later need.

With Tailscale:

```text
Your device
  → encrypted Tailscale network
  → VM private Tailscale address
  → SSH / OmniRoute / private services
```

You can keep:

```text
Postgres       private
Neo4j          private
Mem0           private
Graphify        private
Terrestrial Brain private
OmniRoute       private
```

No public database ports. No public OmniRoute endpoint.

## Graphics: SSH is not graphics

SSH is only terminal/text. Tailscale does not render a desktop either.

For graphical remote access to your GCP Linux VM, use **Chrome Remote Desktop** first.

Google has official documentation for running Chrome Remote Desktop on a Debian Compute Engine VM with a full GNOME desktop. It also supports AV1 plus High Quality Color, which improves text clarity and image quality.[^11_7]

Recommended practical split:


| Need | Use |
| :-- | :-- |
| Fast command-line administration | SSH over Tailscale |
| SSH from a terminal app | Tailscale SSH or normal SSH via Tailscale |
| Access to OmniRoute/dashboard in browser | Browser over Tailscale/private endpoint |
| Full Linux GUI desktop | Chrome Remote Desktop |
| Graphical use on phone/tablet | Chrome Remote Desktop app |
| High-end GPU/3D remote workstation later | NICE DCV or equivalent, only if you actually provision a GPU VM |

### “Fastest and best-looking” answer

For your likely GCP VM usage:

```text
Terminal/dev work:
SSH over Tailscale

Desktop/file browser/GUI:
Chrome Remote Desktop

High-end GPU visualization/3D:
NICE DCV, later and only if needed
```

Chrome Remote Desktop is the sensible first choice because it is officially documented for Google Compute Engine Linux VMs and has AV1/high-quality color options for improved visual quality.[^11_7]

NICE DCV is aimed at high-performance remote Linux/Windows desktops and application streaming, including GPU-oriented use cases. It is overkill unless you specifically need GPU-heavy GUI work, 3D, visualization, or a high-frame-rate remote desktop.[^11_8][^11_9]

## Recommended access design

```text
Phone / tablet
    │
    ├── Tailscale
    │     └── encrypted private network
    │
    ├── SSH client
    │     └── VM terminal/dev administration
    │
    ├── Chrome Remote Desktop
    │     └── VM GNOME desktop, browser, graphical tools
    │
    └── Browser
          └── private OmniRoute / admin UIs through Tailscale

GCP VM
    ├── Docker + Compose
    ├── Tailscale
    ├── SSH
    ├── Chrome Remote Desktop + GNOME
    └── D.U.M.B.A.S.S. services
```


## Best first order

1. Keep ordinary SSH enabled so you cannot lock yourself out.
2. Install Tailscale on the VM and your personal devices.
3. Verify you can SSH over Tailscale.
4. Restrict GCP firewall access after the Tailscale path works.
5. Install Docker Engine + Compose.
6. Deploy OmniRoute only first.
7. Add Chrome Remote Desktop if you need a GUI.
8. Add Postgres, graph services, Mem0, Graphify, and Terrestrial Brain gradually through Compose.

Do not set up NICE DCV or a full graphical desktop before you have basic SSH-over-Tailscale and OmniRoute working.

<span style="display:none">[^11_10][^11_11][^11_12][^11_13][^11_14][^11_15]</span>

<div align="center">⁂</div>

[^11_1]: https://docs.docker.com/engine/

[^11_2]: https://docs.docker.com/compose/

[^11_3]: https://tailscale.com/docs/reference/ssh-over-tailscale

[^11_4]: https://docs.docker.com/compose/install/

[^11_5]: https://github.com/docker/compose

[^11_6]: https://tailscale.com/docs/concepts/what-is-tailscale

[^11_7]: https://docs.cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine

[^11_8]: https://aws.amazon.com/hpc/dcv/

[^11_9]: https://www.ni-sp.com/products/nice-dcv/

[^11_10]: https://tailscale.com/docs/features/tailscale-serve

[^11_11]: https://www.docker.com/community/open-source/

[^11_12]: https://www.docker.com/products/docker-desktop/

[^11_13]: https://en.wikipedia.org/wiki/Docker\_(software)

[^11_14]: https://blog.starmorph.com/blog/tailscale-complete-developer-reference-guide

[^11_15]: https://tech.stonecharioteer.com/posts/2026/tailscale-ssh/


---

# Of course I need a graphical desktop dude I need to run my obsidian desktop and my graphify needs to be hooked up to that I need that I need the Omni route UI there's a UI for I believe it's either trust real brain or mem zero any knowledge or I mean code review graph I need to have that wired up so I can operate that I need to know whether where to hook up the SDK for honey for devs and then what about task observer is that run off of a local on my device on my end or the machine or what so yeah I need a good desktop environment can that Chrome remote run like the vs code ? Acode for my local terminal access?

Yes—you need a real Linux desktop on the GCP VM. Chrome Remote Desktop gives you that remote desktop; inside it you can run **Obsidian Desktop, VS Code, a browser for OmniRoute/Terrestrial Brain/Mem0/Graphify UIs, terminals, Git tools, and Graphify’s local tooling** exactly as if you were sitting at the VM.

Chrome Remote Desktop is only the screen/keyboard/mouse connection. It does not replace the VM desktop, VS Code, Acode, Docker, OmniRoute, or Task Observer.[^12_1][^12_2]

## Correct VM desktop layout

```text
Your phone / tablet
        │
        ├── Chrome Remote Desktop app
        │      └── opens and controls the VM's Linux desktop
        │
        └── Tailscale
               └── private network for SSH and service access

GCP VM
├── Ubuntu or Debian
├── GNOME or XFCE desktop
├── Chrome Remote Desktop host
├── Obsidian Desktop
├── VS Code
├── terminal
├── Chrome/Chromium
├── Docker + Compose
│   ├── OmniRoute
│   ├── Terrestrial Brain
│   ├── Mem0
│   ├── Graphify / CodeReviewGraph
│   └── later supporting services
├── Task Observer service
└── Honey for Devs installed into chosen agent harnesses
```

You log into the VM desktop through Chrome Remote Desktop, then open Obsidian, VS Code, browser dashboards, terminals, and desktop tools there.

Google documents Chrome Remote Desktop for Linux Compute Engine VMs, and Chrome Remote Desktop itself is a remote-control service for accessing a computer through a browser/app.[^12_2][^12_3]

## Yes: VS Code works

**Yes.** Install VS Code on the VM. When you remote into the VM desktop, you launch VS Code from its applications menu and use it normally.

```text
Chrome Remote Desktop
   → VM Linux desktop
      → VS Code
      → open the local Git checkout / Obsidian vault
      → edit files, terminals, Git, extensions
```

VS Code runs **on the VM**, not on your phone. Your phone/tablet just displays and controls it.

This is usually better than trying to make Android-local Acode manage the live VM runtime stack.

### Acode

Acode is optional.

Use Acode only when you want to edit files **locally on Android** or make small edits from a mobile workflow. It is not needed to operate the GCP VM.

```text
Acode
= optional Android-side editor

VS Code on VM
= primary full development environment for corpus/runtime/server work
```

Do not try to keep the same project open for editing in Acode, Obsidian, VS Code, and Graphify at the same time through uncontrolled sync. Use Git as the synchronization boundary.

## Obsidian and Graphify

Your source of truth stays:

```text
GitHub repository
        ↕ Git
Local vault checkout on GCP VM
        ↕
Obsidian Desktop
        ↕
Graphify indexes/query graph
        ↕
OmniRoute calls Graphify retrieval
```

On the VM:

```text
~/dumbass/
├── master-vault/          # Git clone, opened by Obsidian
├── services/              # Docker Compose/service config
├── staging/               # Generated extraction and review artifacts
└── backups/
```

Obsidian opens:

```text
~/dumbass/master-vault/
```

Graphify reads/indexes the same repository checkout, preferably read-only from the indexer’s perspective:

```text
~/dumbass/master-vault/
```

Graphify is designed to generate a queryable knowledge graph from code, docs, SQL schemas, configs, and PDFs. Its public material also indicates on-premise deployment via Docker or Kubernetes, and a local setup involving Python 3.12 and `uv`.[^12_4][^12_5]

### Important correction

Graphify linked to your vault does **not** need to be “inside Obsidian” to work.

The relationship is:

```text
same folder / same Git checkout
```

not:

```text
Graphify becomes an Obsidian plugin database
```

Graphify can produce an Obsidian-oriented view or vault output, and public usage material describes a `graphify --obsidian` mode that generates a vault representation. But your preferred architecture should be the reverse: **your existing Git/Obsidian vault remains master; Graphify indexes it as a derived graph.**[^12_6]

## UIs you will use

You will likely have several separate UIs in the VM browser/desktop.


| UI | Where you use it | What it is for |
| :-- | :-- | :-- |
| Obsidian Desktop | Linux desktop app | Read/write/organize master Markdown vault |
| VS Code | Linux desktop app | Code, Docker Compose, scripts, Git, service config |
| OmniRoute UI | Browser on VM | Provider configuration, routing, keys/settings, model routing status |
| Terrestrial Brain UI | Browser or TUI, depending on project | Corpus/static retrieval administration and query |
| Mem0 UI | Browser if you deploy its dashboard | Episodic-memory inspection/admin |
| Graphify UI | Browser/TUI/agent integration, depending on deployment | Graph build, query, code/doc relationship inspection |
| OpenWiki TUI | VM terminal | Vault compilation, navigation, maintenance workflows |
| Task Observer | Usually no primary desktop UI | Worker/service controlled through OmniRoute/task logs |
| Docker logs | VM terminal or VS Code terminal | See whether each service is healthy |
| GitHub | Browser or VS Code Git panel | Push/pull/review commits |

You do not need all of these open all the time. Your everyday operator tools are usually:

```text
Obsidian + VS Code + terminal + browser
```


## Honey for Devs: where it installs

Honey for Devs is **not** a server that you attach to OmniRoute as a Docker container.

It is a cross-tool agent skill/plugin that installs into the **agent harnesses you use**. The upstream project lists installation paths for Claude Code, Codex, Gemini CLI, OpenClaw, Hermes Agent, and others. For Hermes it installs skill files under `~/.hermes/skills/` and is activated through the agent; for Claude Code it is installed as a plugin.[^12_7][^12_8]

So:

```text
Honey for Devs
├── install into Hermes if Hermes is your chosen primary harness
├── install into DSH if/when DSH has a compatible integration path
├── install into Claude Code only for bounded build work
├── install into Codex/Gemini CLI if you use them as workers
└── not installed “inside” OmniRoute as the primary route server
```


### How OmniRoute uses Honey

OmniRoute does not need to run Honey itself.

The correct relationship:

```text
Agent harness starts
   │
   ├── Honey for Devs loads as that harness's compression/skill layer
   │
   ├── Harness starts a session with OmniRoute
   │
   ├── OmniRoute returns allowed retrieval/tool/model endpoints
   │
   └── Harness uses Honey-compressed task context while it calls OmniRoute
```

If you later build a custom OmniRoute adapter that requests compressed context packages from Honey, that is possible as a custom integration—but it is not the base install model.

## Task Observer: where it runs

Task Observer should run **on the VM**, alongside OmniRoute and the corpus services.

```text
GCP VM
├── OmniRoute
├── Terrestrial Brain
├── Graphify
├── Mem0
├── Task Observer
└── Docker/service supervisor
```

Your phone/tablet does not need to run the full Task Observer service.

### Why VM-side

Task Observer needs access to:

- The VM’s controlled Git checkout.
- Graphify and Terrestrial Brain endpoints.
- OmniRoute.
- Docker/service health information.
- Build/staging directories.
- Logs and generated artifacts.
- Home-node-ready service contracts.

Your phone assistant APK can still be a Task Observer **client**:

```text
Phone assistant
  → OmniRoute
  → Task Observer task request on VM
  → retrieval/build result
  → phone receives response
  → TTS speaks it
```


### When Task Observer runs locally

Use an on-device lightweight Task Observer client only for phone-native actions:

```text
- Start local model inference.
- Check local NPU/runtime availability.
- Capture a note/voice transcript.
- Query a synced retrieval-lite bundle.
- Send a task to the VM.
- Execute explicitly approved Android/terminal actions.
```

That is not the same as the main corpus Task Observer service.

## VM startup order

This is the order you want:

```text
1. VM boots.
2. Linux desktop + Chrome Remote Desktop host starts.
3. Docker starts.
4. Docker Compose starts:
   - OmniRoute
   - Terrestrial Brain
   - Graphify
   - Mem0
   - graph/vector stores if needed
5. OmniRoute passes health checks.
6. Task Observer starts and registers with OmniRoute.
7. You open the VM via Chrome Remote Desktop.
8. You open Obsidian, VS Code, browser dashboards, terminal.
9. Your phone/tablet client connects to OmniRoute over Tailscale.
```

Task Observer starts **after** OmniRoute and its retrieval dependencies are healthy. It should not launch first and then blindly fail because Graphify, Mem0, or Terrestrial Brain are unavailable.

## A clean operator workflow

```text
1. Open Chrome Remote Desktop on tablet/phone.
2. Connect to GCP VM desktop.
3. Open Obsidian:
   - inspect and edit the master vault.
4. Open VS Code:
   - edit service config, scripts, agent contracts, Compose files.
5. Open terminal:
   - inspect Docker services/logs.
6. Open browser:
   - OmniRoute UI.
   - Graphify UI.
   - Mem0/Terrestrial Brain UI if deployed.
7. Use phone assistant:
   - send live queries/tasks through OmniRoute.
8. Review staged changes in Obsidian/VS Code.
9. Commit reviewed vault changes to GitHub.
```


## Desktop choice

For a GCP VM, use a standard desktop environment:


| Desktop | Recommendation | Why |
| :-- | :-- | :-- |
| XFCE | Best first choice | Lighter/faster over remote access; enough for Obsidian, VS Code, browser, terminal |
| GNOME | Fine if VM has enough RAM | More polished, heavier |
| KDE Plasma | Fine if you prefer it | More configurable, somewhat heavier |

For a VM running Docker services plus Obsidian/VS Code/browser, I would choose:

```text
Ubuntu/Debian + XFCE + Chrome Remote Desktop
```

Use **8 vCPU / 32 GB RAM** if you intend to operate Graphify, database containers, browser dashboards, Obsidian, and VS Code together on the same VM. Less can work, but expect indexing and UI responsiveness to suffer.

## Direct answers

- **Can Chrome Remote Desktop run VS Code?** Yes. VS Code runs inside the Linux desktop you connect to.
- **Can it run Obsidian Desktop?** Yes.
- **Can it run Graphify and its UI?** Yes, if Graphify is deployed on the VM; use its browser/UI/TUI from that desktop.
- **Can it run OmniRoute UI?** Yes, open the locally hosted dashboard in the VM browser.
- **Does Honey for Devs plug into OmniRoute?** Not directly by default. Install Honey into each selected agent harness; those harnesses then call OmniRoute.
- **Does Task Observer run on your phone?** Main service: VM. Phone: lightweight client/native executor only.
- **Should you use Acode?** Optional for quick Android edits; use VM VS Code as your actual server/corpus development environment.
- **Will your GitHub/Obsidian vault still be source of truth?** Yes. Everything else indexes, queries, logs, or derives from it.

<span style="display:none">[^12_10][^12_11][^12_12][^12_13][^12_14][^12_15][^12_9]</span>

<div align="center">⁂</div>

[^12_1]: https://support.google.com/chrome/answer/1649523?hl=en-VA\&co=GENIE.Platform=Desktop

[^12_2]: https://remotedesktop.google.com/

[^12_3]: https://docs.cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine

[^12_4]: https://github.com/Graphify-Labs/graphify

[^12_5]: https://graphify.net/

[^12_6]: https://chaseai.io/blog/graphify-obsidian-claude-code-second-brain

[^12_7]: https://github.com/green-pt/honey-for-devs

[^12_8]: https://github.com/Green-PT/honey-for-devs/blob/main/INSTALL.md

[^12_9]: https://docs.cloud.google.com/compute/docs/virtual-workstation/linux

[^12_10]: https://skillsllm.com/skill/honey-for-devs

[^12_11]: https://dev.to/mir_mursalin_ankur/graphify-code-review-graph-build-a-self-updating-knowledge-graph-for-claude-code-and-other-ai-j1m

[^12_12]: https://www.developnsolve.com/linux/how-to-install-chrome-remote-desktop-linux

[^12_13]: https://www.linkedin.com/posts/andrei-moroșan-ab171a179_github-graphify-labsgraphify-turn-any-activity-7492617481635672064-Gas1

[^12_14]: https://linuxvox.com/blog/chrome-remote-desktop-ubuntu/

[^12_15]: https://linuxvox.com/blog/chromium-remote-desktop-linux/


---

# Why do you keep calling Graphify and Code Review Graph the same thing? Those are two separately different things. Code Review Graph is part of the three memory extraction tools; Graphify is a graph tool that I hook up to Obsidian.

You’re right. I conflated them. They are separate components with different jobs.

## Correct distinction

| Component | What it is | Where it connects | Main role |
| :-- | :-- | :-- | :-- |
| **Graphify** | Graph-generation/query tool for repositories and documentation | Your GitHub-backed Obsidian vault | Builds/navigates structural relationships across vault files, code, docs, configs, and project artifacts |
| **Code Review Graph** | A core memory-extraction and graph-vector retrieval layer | OmniRoute / D.U.M.B.A.S.S. runtime | Extracts structured code/task knowledge, supports graph-vector retrieval, and participates alongside Terrestrial Brain and mem0 |
| **Terrestrial Brain / OB1** | Static corpus retrieval layer | OmniRoute / D.U.M.B.A.S.S. | Queries the corpus-derived structured static knowledge base |
| **mem0** | Episodic memory layer | OmniRoute / D.U.M.B.A.S.S. | Stores/retrieves selected session, user, and agent context |

So the three core retrieval/memory arms are:

```text
1. Terrestrial Brain / OB1
   = static corpus / structured semantic memory

2. Code Review Graph
   = graph-vector memory extraction and retrieval

3. mem0
   = episodic/session memory
```

Graphify is **not** Code Review Graph, and it is not one of those three memory extraction layers.

## Correct data flow

```text
GitHub repository + Obsidian vault
         │
         ├── Graphify
         │     └── indexes/visualizes/maps the vault and repo graph
         │
         ├── Terrestrial Brain ingestion
         │     └── builds static corpus retrieval data
         │
         └── Code Review Graph extraction
               └── produces graph-vector retrieval data

OmniRoute
   ├── queries Terrestrial Brain for static knowledge
   ├── queries Code Review Graph for graph-vector/code/relationship retrieval
   ├── queries mem0 for episodic session memory
   ├── uses Reasoning Bank + Continual Harness internally
   └── routes the final evidence/context to local or frontier models
```

Graphify may produce useful graph output that Code Review Graph can reference or consume through an adapter, but that is an **integration**, not an identity. Do not merge their databases, prompts, or responsibilities unless you later explicitly decide to build a bridge.

## VM placement

```text
GCP VM
├── Obsidian Desktop
│   └── opens your GitHub-linked master vault
│
├── Graphify
│   └── attached to the vault as its own graph tool
│
├── OmniRoute
│   ├── Terrestrial Brain / OB1
│   ├── Code Review Graph
│   ├── mem0
│   ├── Reasoning Bank
│   └── Continual Harness
│
├── Honey for Devs
│   └── installed in selected agent harnesses at agent launch
│
└── Task Observer
    └── VM-side worker/controller using OmniRoute services
```

I will keep them distinct going forward: **Graphify = Obsidian/vault graph tool. Code Review Graph = D.U.M.B.A.S.S. graph-vector memory/retrieval arm.**

---

# Okay so back to the master configure on the the wiki should I just run open Wiki and which model should I use inside of that would be best I was using a glm and is there any special kind of configuration I need for the open Wiki can I just do when I got in my terminal what direction should I get it first and where should I point it at first

Yes: use OpenWiki as the **wiki compiler/librarian**, pointed first at a clean local Git checkout of your master corpus—not directly at your live mobile vault, not at Docker volumes, and not at OmniRoute’s internal files.

Use your GLM provider only if it is already stable for you, but make OpenWiki’s first pass a **staged, reviewable generation**. Do not let it loose on the full repository with default settings and immediately accept all of its output. OpenWiki runs from the current directory, initializes with `openwiki --init`, and writes a repository wiki under `openwiki/` by default. It supports OpenRouter, Anthropic, Gemini, OpenAI, and OpenAI-compatible endpoints.[^14_1][^14_2]

## Point it here first

On your GCP VM desktop, create this layout:

```text
~/dumbass/
├── master-vault/             # Your GitHub clone; source documents
├── openwiki-worktree/        # Separate Git worktree/clone for OpenWiki output
├── services/                 # Docker/OmniRoute configs; NOT wiki input
├── staging/
└── backups/
```

Do **not** point OpenWiki at:

```text
~/.omniroute/
Docker volumes
Postgres data
Neo4j data
mem0 data
your whole home directory
a live mutable vault while Obsidian is actively mass-editing it
```

Point it at:

```text
~/dumbass/openwiki-worktree/
```

That worktree should be a clone or Git worktree of the same master-vault repository. It protects your primary Obsidian workspace from a bad bulk rewrite.

The workflow is:

```text
GitHub master repo
   ↓ clone/worktree
OpenWiki worktree
   ↓ OpenWiki generates staged wiki documentation
review in Obsidian + VS Code
   ↓
Git commit
   ↓
GitHub
   ↓
your primary Obsidian vault pulls reviewed changes
```


## Which model to use

For initial full-corpus compilation, use a **strong model with reliable long-context instruction following**, not the cheapest fastest model.

### Practical choice

| Work | Recommended model class | Why |
| :-- | :-- | :-- |
| First full wiki architecture / major synthesis | Strong frontier model or best GLM model you have verified | Better hierarchy, cross-linking, conflict detection, less garbage generation |
| Bulk repetitive page drafting | GLM if it gives adequate quality and cost | Lower cost/high throughput |
| Small wiki updates | GLM or a smaller model | Cheap incremental maintenance |
| Architecture decisions, policies, runtime contracts | Stronger model with human review | These are high-impact and should not be mass-autogenerated |
| Code-repo documentation | Strong coding/documentation model | Better symbol/API/system explanation |
| Final review/lint | Separate model or deterministic validator | Avoid one model approving its own work |

If your current GLM model has been producing usable structured Markdown, use it for **controlled batch drafting**. But do not assume it is the best model for the first global vault pass merely because it works. OpenWiki lets you select a provider/model during initialization or configure it through environment variables.[^14_2][^14_3]

### My exact recommendation

Start with:

```text
Provider: OpenRouter or your GLM-compatible endpoint
Model: your proven GLM model
Mode: staged batch generation
```

Then reserve a stronger provider/model for:

```text
- root MAP.md
- ontology/terminology canon
- D.U.M.B.A.S.S. architecture pages
- OmniRoute contract
- retrieval/memory protocols
- harness contracts
- runtime/extraction architecture
- final cross-link and contradiction review
```

If your GLM access is through an OpenAI-compatible API endpoint, OpenWiki’s `openai-compatible` provider is intended for that: configure the provider, base URL, API key, and the exact model ID exposed by your endpoint.[^14_2]

## Do not run this first

Do **not** do this against the full vault on the first command:

```bash
cd ~/dumbass/master-vault
openwiki --init
```

That could create an `openwiki/` folder and bulk-generate output inside your active master clone. OpenWiki’s first-run workflow is meant to initialize docs for the current repository and write its repository wiki to `openwiki/`.[^14_1][^14_2]

Instead, use a dedicated worktree.

## Initial setup

### 1. Prepare the worktree

On the VM, from a terminal:

```bash
mkdir -p ~/dumbass
cd ~/dumbass

git clone <YOUR_PRIVATE_GITHUB_REPO_URL> openwiki-worktree
cd openwiki-worktree
```

If you already have the master repo cloned locally and understand Git worktrees, use a separate branch/worktree instead. The point is isolation:

```text
main vault branch/worktree
= your normal Obsidian source-of-truth files

openwiki branch/worktree
= agent-generated documentation candidate changes
```


### 2. Make the target explicit

Before OpenWiki runs, create a root guidance file. Use `CLAUDE.md`, `AGENTS.md`, or the OpenWiki project’s supported instruction mechanism once you confirm its current name in the installed version.

Put a concise contract in the worktree root:

```markdown
# Wiki Compilation Contract

This repository is the canonical Markdown corpus.
Do not modify raw source files.
Do not rename or delete existing vault folders.
Write generated documentation only under `openwiki/` during the first pass.
Treat all generated claims as drafts unless linked to source paths.
Do not invent runtime status, installed software, device ownership,
model availability, database state, or architecture decisions.
Use `MAP.md` and scoped manifests for discovery.
Preserve source paths and Git revision references in generated pages.
Record conflicts and uncertainty under `openwiki/open-questions/`.
Do not write service secrets, API keys, tokens, database credentials,
or private session logs into wiki pages.
```

This does not make the model perfect, but it creates a clear review boundary.

### 3. Install OpenWiki

OpenWiki is an npm CLI. Its current documentation says it is installed globally with npm and initialized from the repository directory; current package information lists Node.js 22.22+ for the CLI release described there.[^14_3][^14_4]

Conceptually:

```bash
npm install -g openwiki
openwiki --help
```

Then from the isolated worktree:

```bash
cd ~/dumbass/openwiki-worktree
openwiki --init
```

The interactive initializer asks for provider, credentials, and model configuration. OpenWiki stores its local configuration and credentials under `~/.openwiki` by default; the config directory can be relocated with `OPENWIKI_CONFIG_DIR`.[^14_4][^14_2]

## Use a separate OpenWiki config directory

Do not mix its state with anything else. Set:

```bash
export OPENWIKI_CONFIG_DIR="$HOME/.config/dumbass/openwiki"
```

Then initialize:

```bash
cd ~/dumbass/openwiki-worktree
openwiki --init
```

That gives you a clean separation:

```text
~/dumbass/openwiki-worktree/
= repo input and generated `openwiki/` output

~/.config/dumbass/openwiki/
= OpenWiki credentials, local app state, sessions, settings
```

OpenWiki defaults to `~/.openwiki` for local state but supports relocating that state through `OPENWIKI_CONFIG_DIR`.[^14_5][^14_4]

## GLM configuration

The exact endpoint/model name depends on how you access GLM. I do not know your exact provider, base URL, or valid model ID, so I will not invent them.

If your GLM endpoint is OpenAI-compatible, the shape is:

```bash
export OPENWIKI_PROVIDER="openai-compatible"
export OPENAI_COMPATIBLE_BASE_URL="https://YOUR-GLM-ENDPOINT/v1"
export OPENAI_COMPATIBLE_API_KEY="YOUR_KEY"
export OPENWIKI_MODEL_ID="YOUR_EXACT_GLM_MODEL_ID"
```

Then run:

```bash
cd ~/dumbass/openwiki-worktree
openwiki --init
```

OpenWiki documents its OpenAI-compatible provider as requiring a base URL and model ID that correspond to what your endpoint actually exposes.[^14_2]

If you use GLM through OpenRouter instead, configure:

```bash
export OPENWIKI_PROVIDER="openrouter"
export OPENROUTER_API_KEY="YOUR_KEY"
export OPENWIKI_MODEL_ID="YOUR_EXACT_OPENROUTER_GLM_MODEL_ID"
```

Do not put keys in `compose.yaml`, Git-tracked `.env` files, the vault, Obsidian notes, or `CLAUDE.md`.

## First OpenWiki job

Your first job should **not** be “document every file and infer the whole system.”

Start with the core control documents and top-level map:

```text
1. Root MAP.md
2. Architecture overview
3. Terminology glossary
4. Corpus/inventory overview
5. D.U.M.B.A.S.S. component map
6. Open questions and contradictions list
7. Per-domain documentation plan
```

Prompt/task for OpenWiki:

```text
Create a staged architecture and navigation wiki for this repository.

Scope:
- Read top-level structure, MAP.md files, manifests, README files,
  architecture documents, protocol documents, and project indexes first.
- Do not recursively summarize every leaf file in the first pass.
- Write output only under openwiki/.
- Create:
  1. openwiki/overview.md
  2. openwiki/architecture.md
  3. openwiki/terminology.md
  4. openwiki/repository-map.md
  5. openwiki/open-questions.md
  6. openwiki/ingestion-plan.md
- Link every material statement to source paths.
- Flag contradictions rather than resolving them by invention.
- Never modify files outside openwiki/.
```

Then review it in Obsidian and VS Code.

## Full vault compilation order

You are right that the goal is the entire corpus. The correct sequence is **whole corpus inventory first, staged compilation second**:

```text
A. Inventory all 10,000+ files.
B. Generate manifests, hashes, types, paths, and source IDs.
C. Run Graphify against the corpus/repositories.
D. Build OpenWiki top-level architecture and MOCs.
E. Compile one domain at a time.
F. Review/merge each domain.
G. Re-run cross-link/contradiction passes.
H. Publish the reviewed output to the master branch/vault.
```

Use OpenWiki for parts **D through G**. Use deterministic scripts and Graphify for parts **A through C**.

Suggested domain batches:

```text
Batch 1: root governance, architecture, terminology, master MAP
Batch 2: OmniRoute, D.U.M.B.A.S.S., runtime/extraction protocols
Batch 3: Terrestrial Brain, Code Review Graph, mem0, Reasoning Bank
Batch 4: models, runtimes, weights, voice, NPU/SDK material
Batch 5: Android apps, Termux/Æsc, device/operator workflows
Batch 6: projects and repositories
Batch 7: skills, tools, harnesses, agents
Batch 8: external references and vendor documentation
Batch 9: runbooks, decisions, operator corrections
Batch 10: cross-linking, dedupe, contradiction and stale-reference pass
```


## Where OpenWiki output goes

For the first run:

```text
openwiki/
├── overview.md
├── architecture.md
├── repository-map.md
├── terminology.md
├── ingestion-plan.md
├── open-questions.md
├── domains/
├── projects/
├── protocols/
└── sources/
```

After review, either:

```text
Option A:
Keep `openwiki/` as a generated/staged documentation subtree.

Option B:
Merge selected reviewed pages into your canonical vault:
- `02_wiki_md/`
- `architectures/`
- `protocols/`
- `runbooks/`
- `indexes/`
```

Use **Option A first**. Do not allow OpenWiki to write directly into every canonical wiki folder until you trust its output quality and have a validator/promotion script.

## OpenWiki model roles

Your GLM setup can work like this:

```text
GLM
= bulk domain drafting, navigation pages, summaries, cross-links

Stronger frontier model
= architecture contracts, contradiction resolution proposals,
  high-stakes runtime/extraction documentation, final review

Graphify
= structural/code graph evidence

Terrestrial Brain
= static corpus retrieval evidence

Code Review Graph
= graph-vector retrieval evidence

mem0
= episodic session context; not canonical wiki evidence

OpenWiki
= documentation compiler/librarian
```

That is the correct division. OpenWiki does not replace OmniRoute, Graphify, Terrestrial Brain, Code Review Graph, or mem0.

## Bottom line

Run OpenWiki, but point it first at a **separate Git worktree clone** of your master vault. Use GLM for controlled bulk drafting if it has been adequate for you, and use a stronger model for the root architecture/protocol pages. Configure it with an OpenAI-compatible endpoint only if that is how your GLM provider is exposed; otherwise choose the provider you actually use. Start by generating top-level maps and staged architecture pages inside `openwiki/`, review them in Obsidian/VS Code, then promote approved pages into the canonical vault.

<span style="display:none">[^14_10][^14_11][^14_12][^14_13][^14_14][^14_15][^14_6][^14_7][^14_8][^14_9]</span>

<div align="center">⁂</div>

[^14_1]: https://docs.langchain.com/oss/openwiki/overview

[^14_2]: https://github.com/langchain-ai/openwiki

[^14_3]: https://www.langchain.com/blog/introducing-openwiki-an-open-source-agent-for-repo-documentation

[^14_4]: https://github.com/langchain-ai/openwiki/blob/main/openwiki/quickstart.md

[^14_5]: https://github.com/langchain-ai/openwiki/releases

[^14_6]: https://github.com/langchain-ai/openwiki/issues/876

[^14_7]: https://github.com/orapli/git-dashboard-tui/blob/main/openwiki/architecture/overview.md

[^14_8]: https://github.com/langchain-ai/openwiki?aid=recGyKYwdqhoamyVe

[^14_9]: https://regolo.ai/openwiki-setup-a-privacy-first-for-enterprises/

[^14_10]: https://themenonlab.blog/blog/openwiki-langchain-agent-documentation

[^14_11]: https://deepwiki.com/langchain-ai/openwiki

[^14_12]: https://deepwiki.com/vercel-labs/openwiki/6.2-model-configuration-and-scheduling

[^14_13]: https://pub.towardsai.net/running-openwiki-for-real-why-the-model-you-pick-decides-everything-b6cfd1180c38

[^14_14]: https://pub.towardsai.net/openwiki-in-production-a-realistic-setup-review-guide-23edce255b09

[^14_15]: https://daily.dev/posts/openwiki-is-a-cli-that-writes-and-maintains-agent-documentation-for-your-codebase--tpuasnwij


---

# Dude my live local Vault and my master corpus get repo are the same exact things they're synced up together

Got it. Your **live local Obsidian vault is the GitHub master-corpus repository checkout**—the same files, same directory, synced through Git. I should not have described them as separate sources.

```text
Local master corpus folder
= Obsidian vault
= Git working tree
↕
GitHub private repository
= remote mirror/version history
```

Graphify, OpenWiki, NotebookLM-PY, Terrestrial Brain, and Code Review Graph should all read/index **that one vault/repo** or a controlled clone of it. They do not create a second canonical vault.

The only reason to use an OpenWiki worktree is **safety**, not because it is another corpus:

```text
master-vault/             # your live Obsidian + Git repo
openwiki-review-worktree/ # temporary branch/working copy for agent-generated changes
```

After you review the generated pages, merge or copy only the approved changes back into the live master vault.

