---
title: "MASTER_HOOKS_REGISTRY.md (1)"
source: "Drive_sync/Secure-Spark-Proof-Folder /novae-xorpus/hooks/MASTER_HOOKS_REGISTRY.md (1).pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

MASTER HOOKS REGISTRY — NovÆxorpus
Ecosystem
Authority: Authoritative specification and catalog for all Git lifecycle hooks, continual learning
feedback loops, and cross-repository synchronization hooks across the NovÆxorpus
ecosystem.


1. Operational Invariants for Hooks
1.​ Automated Manifest Regeneration: Any write operation to clean_md/, wiki_md/,
skills/, or tools/ fires post-commit manifest generation.
2.​ RLVR Evaluation Hooks: Ingestion passes must trigger verification hooks
(tools/check.py) using disjoint extractors prior to catalog commit.
3.​ Cross-Repo Sync Protocol: Synchronizes #d.u.m.b.a.s.s. authoritative memory
structures across consumer repositories (aesop-xi, novus-aexenti) without
recursive duplication.


2. Master Hooks Catalog
Hook Name
Hook Location
Trigger Event
Action / Script
Bound
post-commit
~/.git/hooks/pos
t-commit
Git Commit in any
repo
Triggers
compile_manifest
.py &
generate_jsonl_m
arkers.py
pre-commit-hygie
ne
~/.git/hooks/pre
-commit
Git Commit
Runs
system_housekeep
er.sh & checks for
.red/ leakage
rlvr-verifier
novae-xorpus/hoo
ks/
Ingestion /
Normalization
Dispatches
corpus-verify


Hook Name
Hook Location
Trigger Event
Action / Script
Bound
check across source
vs clean
continual-rollba
ck
novae-xorpus/hoo
ks/
Skill execution error
Reverts snapshot to
previous verified
checkpoint
dumbass-cross-sy
nc
aesop-xi/.git/ho
oks/
Post-commit in
consumer repo
Synchronizes
memory markers to
novae-xorpus
