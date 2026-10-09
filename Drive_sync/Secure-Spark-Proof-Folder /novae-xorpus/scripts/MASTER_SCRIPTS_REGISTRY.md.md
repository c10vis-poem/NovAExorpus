---
title: "MASTER_SCRIPTS_REGISTRY.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /novae-xorpus/scripts/MASTER_SCRIPTS_REGISTRY.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

MASTER SCRIPTS REGISTRY — NovÆxorpus
Ecosystem
Authority: Central registry for all executable scripts, daemons, utilities, and runner tools across
all 8 repositories in the NovÆxorpus living canon.


1. Dispersal Architecture & Locality of Reference
Per the Locality of Reference Invariant:

●​ Scripts execute within their respective repository context.
●​ This directory (novae-xorpus/scripts/) maintains the master inventory, execution
signatures, and cross-repo orchestration scripts.


2. Master Scripts Catalog
Script Name
Target
Repository
Subsystem /
Function
Runtime
Execution
Trigger / Port
system_house
keeper.sh
novae-xorpus
/tools/
Zero-trust
hygiene
sweeper
Bash
Periodic /
Scheduled
compile_mani
fest.py
novae-xorpus
/tools/
Manifest
SHA-256 hasher
& cataloger
Python 3
Post-commit /
On-change
generate_jso
nl_markers.p
y
novae-xorpus
/tools/
Pre-tokenized
chunk marker
generator
Python 3
Post-normalizati
on
run_audit.sh
aesop-xi/
Red Agent
background
isolation
daemon
Bash
External
~/.red/ runner


Script Name
Target
Repository
Subsystem /
Function
Runtime
Execution
Trigger / Port
npu_manager.
py
novus-aesc/t
ools/
Hexagon NPU
socket model
switcher
Python 3
UNIX socket
talk.sh /
listen.sh
novus-aeyre/
scripts/
Sherpa-ONNX /
Moonshine /
Kokoro audio
Bash
Sensory ingress
pipeline
bootstrap-st
ack.sh
aesop-xi/scr
ipts/
Multi-node dev
environment
bootstrap
Bash
Session start
check.py
(corpus-veri
fy)
novae-xorpus
/tools/
Hard Rule 5
disjoint extractor
verification
Python 3
Phase 2 RLVR
validation
