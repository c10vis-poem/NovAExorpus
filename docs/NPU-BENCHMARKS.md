# NPU benchmarks — Razr Ultra 2025 (SM8750, HTP v79)

One table per run. Raw data: `benchmarks/results/`. Harness: `~/tools/npu-bench/bench.py`. Tiers: T1 small/Oracle help desk, T2 routing/tools/planning, T3 vision+language. Final output: role map.

## Streaming on a small screen (2026-10-02, GenieX Chat, Gemma 4 E4B)
- The limit is NOT reading speed (the operator reads faster than 10 tok/s). Above ~10 tok/s the auto-scrolling text jumps and flutters on the phone screen, which breaks reading.
- ~9 tok/s streamed smoothly; ~13 tok/s jittered.
- So this is a **UI problem, not a model-speed target**: smooth or line-buffered scrolling, or no auto-scroll while reading. Faster models are still better.
