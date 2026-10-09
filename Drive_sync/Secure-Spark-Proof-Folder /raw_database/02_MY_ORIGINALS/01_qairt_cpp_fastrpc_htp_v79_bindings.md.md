---
title: "01_qairt_cpp_fastrpc_htp_v79_bindings.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/02_MY_ORIGINALS/01_qairt_cpp_fastrpc_htp_v79_bindings.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Qualcomm AI Engine Direct (QAIRT) C++ API &
Hexagon HTP v79 FastRPC Bindings
1. System Overview & Hardware Target
This specification details the native C/C++ interface to the Qualcomm AI Engine Direct (QAIRT /
QNN SDK) targeting the Hexagon Tensor Processor (HTP v79 on Snapdragon 8 Elite SM8750).
2. Low-Level FastRPC Communication
The Hexagon NPU is interfaced via Qualcomm's Compute DSP Remote Procedure Call
(cdsprpc) over Domain 3:

-​
Device Node: /dev/fastrpc-cdsp
-​
Userspace Driver: libcdsprpc.so / libadsprpc.so
-​
Execution Domain: User Process Domain (PD) on Domain 3 with attribute 0x8
-​
Skel Library: libQnnHtpV79Skel.so loaded into DSP memory space
-​
Stub Library: libQnnHtpV79Stub.so linked into native Android C++ process
3. High-Speed Zero-Copy Shared Memory (ASharedMemory)
To bypass Android Binder 1MB transaction limits and eliminate CPU copying taxes:

-​
Allocate native anonymous shared memory: ASharedMemory_create(name, size)
-​
Map into local daemon address space: mmap(NULL, size, PROT_READ |
PROT_WRITE, MAP_SHARED, fd, 0)
-​
Protect region across child processes: ASharedMemory_setProt(fd, PROT_READ)
-​
Transmit anonymous file descriptor over abstract UNIX domain socket (sun_path[0]
= '\0') using POSIX ancillary payloads (SCM_RIGHTS).
4. Multi-Device Virtualization & Process Domain Management
Qualcomm's mobile firmware enforces an allocation ceiling of ~3.5GB per single Hexagon
Process Domain (PD). To execute models exceeding 3.5GB (such as Qwen 3.5 9B Q4_0
requiring ~5.5GB–6.0GB VRAM with KV cache):

-​
Allocate an array of QNN context handles: Qnn_ContextHandle_t ctx[2]
-​
Virtual Device 1 (HTP0): Maps Layers 0 to 24 (capped at ~2.8GB)
-​
Virtual Device 2 (HTP1): Maps Layers 25 to 48 (capped at ~2.7GB)


-​
Intermediate tensor transitions between Layer 24 and Layer 25 occur over on-chip
FastRPC ioctl calls without host memory round-trips.
