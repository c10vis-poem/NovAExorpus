---
title: "README_VENDOR_CORPORA.md (1)"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/02_MY_ORIGINALS/README_VENDOR_CORPORA.md (1).pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

README — vendor-corpora/
Immutable External Vendor Documentation & Architecture
Registries
W5+H Subsystem Identity
●​ WHO: Managed by the Ingestion Pipeline; queried strictly via OB1 and MCP by Large
Query Models.
●​ WHAT: Millions of tokens of static vendor documentation (Qualcomm QAIRT SDK,
Android OS, Unsloth, Llama Server).
●​ WHEN: Queried on-demand when compiling native C++ daemons, configuring NPU
quantization parameters, or debugging Android OS service permissions.
●​ WHERE: novae-xorpus/vendor-corpora/ (Federated Subsystem Root).
●​ WHY: Isolates heavy external documentation so it does not drown internal conceptual
wiki graphs or pollute active prompt contexts.
●​ HOW: Read-only directory partition indexed by localized manifest.jsonl files and
accessed via targeted MCP tool calls.


Internal Directory Topology
vendor-corpora/

├── README.md                                # This document (Vendor package organization rules)

├── manifest.jsonl                           # Master catalog of vendor packages and version hashes

│

├── qualcomm-qairt-sdk/                      # Qualcomm QAIRT & Hexagon NPU Reference Library

│   ├── manifest.jsonl                       # Localized Qualcomm API index

│   ├── htp-specs/                           # Hexagon v79 HTP hardware limits, INT4/INT8 GEMM
rules

│   ├── headers/                             # libQnnHtp.so headers, FastRPC ioctl definitions



│   └── quantization-guides/                 # Accuracy-aware quantization and graph optimization

│

├── google-android-platform/                 # Android Native Framework Architecture

│   ├── manifest.jsonl                       # Localized Android OS index

│   ├── system-services/                     # Foreground Services, START_STICKY, and LMK
priorities

│   ├── media-gaming-sdk/                    # Low-latency audio frameworks and screen frame
capture

│   └── developer-options/                   # Wireless Debugging, adbd loopback, and key pairing
specs

│

└── unsloth-fine-tuning/                     # Fine-Tuning & Quantization Manuals

    ├── manifest.jsonl                       # Dataset parameters & token formatting rules

    └── gguf-export/                         # Export guidelines for Q4_K_M and GGUF architectures


Beginner-Proof Implementation Rules
1.​ Strictly Read-Only: Never edit files in this tree. They are immutable vendor references.
2.​ Selective MCP Ingestion: Never dump an entire vendor directory into an agent prompt.
Agents query specific structs (e.g. ASharedMemory_create) via MCP to pull only the
matching 15 lines.
