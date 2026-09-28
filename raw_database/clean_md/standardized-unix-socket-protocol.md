---
source: "raw/Standardized UNIX socket protocol,.md"
cleaned: 2026-09-09
converter: Read tool (source was itself a pre-converted PDF-to-markdown pass, 2 pages)
---

Decoupling the architecture into standalone daemons and independent processes unlocks the highest tier of engineering performance possible on Android. Here is why this separation ensures the system runs flawlessly under heavy load:

## 1. Zero Impact on Game Frame Rates (FPS)

If Qwen 3.5 were loaded directly inside the UI app or hooked natively into a game thread, the Garbage Collector (GC) pauses from Java/Kotlin would cause noticeable micro-stutters in the game.

Because AI inference is locked inside isolated native background processes (`:qairt_engine` and `:llamacpp_engine`), its memory management is completely invisible to the operating system's main rendering loop. The active video game keeps 100% of its high-priority CPU and GPU execution lanes untouched.

## 2. Complete Fault Isolation (No App Crashes)

Large language models are inherently volatile on mobile hardware. If Qwen 3.5 exhausts its token allocation window or hits a weird tensor parsing bug, a monolithic application would instantly crash straight to the Android home screen, ruining the user's gaming session.

With this daemon structure, if the AI engine panics or hits an out-of-memory wall, only that specific engine daemon dies. The Master Orchestrator Service instantly detects the process drop, clears the shared memory file descriptor, and re-initializes the backend in milliseconds — without your UI frontend or the active video game ever realizing a crash occurred.

## 3. Ultimate Memory Efficiency via Zero-Copy

Traditional Android apps pass data across processes using Binders or local network sockets, which forces the CPU to constantly copy data back and forth in RAM.

By using Linux `memfd_create` or `ASharedMemory`, the system daemon writes game tracking information into a shared RAM sector once. The Qualcomm NPU reads it directly from that exact same physical address space. You achieve desktop-class throughput because you have completely eliminated the CPU data-copying tax.

## 4. Pluggable, Upgradable Scale

Because frontends and AI backends communicate purely over a standardized UNIX socket protocol, the system becomes infinitely scalable. If you want to replace Qwen 3.5 with a completely new model next month, or add a native Rust-based translation system, you don't have to rewrite the UI. You simply compile the new native daemon binary via your GitHub CI pipeline, drop it into place, and let the orchestrator route the socket traffic to it.

This is built exactly the way Google handles its system-level AI pipelines — with the complete C++ cross-process socket listener loop to handle the token streaming, and the GitHub Actions YAML configuration to automate the building of these separate daemon binaries.
