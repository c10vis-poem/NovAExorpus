---
title: "five-bucket-curation-triage.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/skills-and-capabilities/prompt_skills/five-bucket-curation-triage.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

name: five-bucket-curation-triage description: Enforces the
5-bucket document triage protocol before topical filing. Classifies
ingested assets into Canon, Pending, Vault,
Reverse-Engineering, or Toss.
Five-Bucket Curation Triage Protocol
Mined from: PLUGINS TOOLS AND MEMORY LAYER ARGUMENTS (File 1)
Core Directive: Triage Before Topical Filing
You cannot place a document by subject until you know whether it is true. Documents entering
the corpus must be categorized into one of five distinct disposition buckets:

Bucket
Purpose & Criteria
Action Taken
Canon
Settled, verified truth.
Everything trickles down from
this.
Move to repo root or
canonical spec directories.
Immutable law.
Pending Corpora
Experimental, unproven, or
draft architectures requiring
operator sign-off.
Move to staging / review
holding queue.
Vault
Alternative build approaches,
historical setups, or deep
reference manuals.
Retained in cold storage
(01_raw_sources/) for
future study.
Reverse-Engineering
Decompiled assets,
salvageable code, and
failback mechanisms.
Staged in
reverse_engineering/
for recovery.
Toss
Stale, redundant, or dead
conversational noise.
Marked for operator deletion.
Zero inclusion in manifests.
Workflow Rules
1.​ Never guess canon: If an architecture contradicts the operator's latest directive, flag as
Pending.


2.​ Promotion rule: Promotion from Pending to Canon is an explicit event tracked in
RESUME.md.
