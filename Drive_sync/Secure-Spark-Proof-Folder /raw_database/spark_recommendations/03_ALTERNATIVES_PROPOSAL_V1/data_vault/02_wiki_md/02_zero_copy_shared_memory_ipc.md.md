---
title: "02_zero_copy_shared_memory_ipc.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/data_vault/02_wiki_md/02_zero_copy_shared_memory_ipc.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

# Zero-Copy ASharedMemory & UNIX Domain Socket IPC

## 1. Bypassing Android IPC Bottlenecks
Standard Android IPC (Binder) enforces a strict 1MB transaction limit and requires repeated
CPU copying.
- **ASharedMemory Allocation**: Anonymous shared memory regions allocated via
`ASharedMemory_create` and mapped into process spaces via `mmap`.
- **Abstract UNIX Domain Sockets**: Sockets initialized with `sun_path[0] = '\0'` bind directly to
Linux's abstract network namespace, eliminating physical disk I/O and filesystem permission
blocks.
- **File Descriptor Handshake**: File descriptors are passed seamlessly between daemons
using POSIX ancillary messages (`SCM_RIGHTS`).
