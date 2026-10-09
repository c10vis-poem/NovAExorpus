# NPU work — findings so far (2026-10-02), before restarting one model at a time

All NPU testing was stopped on 2026-10-02 at the operator's call. This file records what is actually known, what is suspect and what was never verified, so the restart begins from facts. Raw numbers: `benchmarks/results/`, `docs/NPU-SERVE-BUILD-LOG.md`, `~/.claude/NPU-ON-DEVICE.md`.

## 1. Verified (with evidence)
- **Device:** Motorola Razr Ultra 2025, `ro.soc.model=SM8750`, Hexagon **v79** (same chip family as the Galaxy S25's "8 Elite for Galaxy", AI Hub chipset `qualcomm-snapdragon-8-elite-for-galaxy`, soc_model 69).
- **GenieX v0.7.1** files on the phone match Qualcomm's release checksum (sha256 `857879f8…83bf01`).
- **Our server runs inside GenieX's libraries.** `/proc/<pid>/maps` showed only GenieX v0.7.1 libs plus `/vendor/lib64/libcdsprpc.so` and OpenCL. No llama-server or other stack was involved.
- **An NPU session opens:** the log shows `Hexagon Arch version v79`, `HTP0 new session … domain-id 3`, and layers assigned to HTP0.
- **Qwen 3.5 files (Unsloth, = AI Hub's official asset) are not fully on the NPU:** 18 `ssm_out` (Q5_K) plus `token_embd` (Q6_K) run on the CPU, giving 38 CPU↔NPU handoffs per token. Same for 0.8B and 2B. Gemma 4 E2B (clean Q4_0) had 2 handoffs.
- **AI Hub's own numbers (Galaxy S25, same chip):**
  - Qwen 3.5 2B, GenieX llama.cpp: NPU decode 22.6–24.8, CPU 30–40 tok/s.
  - Qwen3-0.6B: QAIRT w4a16 decode 57.6 vs llama.cpp q4_0 30.8 (QAIRT ≈2×).
- **Model files fingerprinted:** Qwen 3.5 0.8B, 2B, 9B (Unsloth official) and the other 9B (= bartowski's public build, not a compile job).

## 2. Suspect / not trustworthy
- **Every speed number from today.**
  - Qwen 3.5 2B on NPU: 12.7–17 tok/s (vs Qualcomm's 22.6–24.8). Qwen 3.5 0.8B on NPU: 2.5–3 tok/s.
  - During the runs the **CPU clocks were capped and moving**: prime cores 1,401→1,958 MHz of 4,320; performance cores 1,996→2,227 MHz of 3,532.
  - The phone was at 27% battery, unplugged; chip temperature 50–54 °C. The cause of the caps was **not identified**. Battery saver was not confirmed and the operator says it is off.
- **"It runs on the NPU" ≠ "it runs correctly."** Only session-open and layer-assignment were shown. Throughput is about half of Qualcomm's reference or worse.
- **`0x80000414`** (dspqueue / HMX max-clock vote refused, llama.cpp #22352 / PR #22334) is logged on every load. Its effect is unknown.
- **The install route is not Qualcomm's documented Android route.** We run the `geniex-bench-android-arm64` tarball's libraries through our own C shim (`~/tools/geniex-serve`) from Termux. The documented Android path is the GenieX SDK (`com.qualcomm.qti:geniex-android`, AAR) inside an app, or the GenieX Chat sample app. The documented CLI (`geniex serve` / `geniex infer`) ships for Windows ARM64 and Linux ARM64 (Dragonwing), not Android. Termux, SELinux and FastRPC access may differ from an app context.
- An earlier v0.7.1 run gave 2.7 tok/s; a later one gave 15.9. Never explained.

## 3. Never done / never verified
- The Qualcomm reference run on this phone: their GenieX Chat app (official Android path), to get a baseline from Qualcomm's own route.
- The ADB shell-user test (RESUME item since 2026-10-01): same binary, outside Termux's sandbox.
- Any QAIRT bundle run (InternVL 2B/4B, SmolLM2 1.7B for 8 Elite). These are AI Hub's precompiled, chip-specific route, and our server doesn't support it yet.
- Any speech model run (Whisper, Zipformer, MeloTTS, Piper, DeepSpeech, Distil-Whisper).
- Vision input (`mmproj`) for any VL model.
- Vendor docs: about 12 of 49 read fully before today's tests. Rule now: read all docs for a model before loading it.
- Model cards saved but not yet read: SmolVLM2-2.2B (+ GGUF card), Qwen3.5-0.8B, Qwen3.5-2B, unsloth Qwen3.5-2B-GGUF.

## 4. Restart plan: one model at a time, with the operator
For each model, in order:
1. **Read** all its vendor docs (Vendor-Registries + model card). List what was read.
2. **Identify the vendor's documented install/run path** for this exact model and chip (AI Hub page, `qai-hub-models info`, GenieX Quickstart). Use that path first, before any custom shim.
3. **Check the phone state**: plugged in, CPU caps = hardware max (`/sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq`), temperature, nothing else running.
4. **Run the vendor's own tool** (geniex-bench / their app / their CLI) and compare with AI Hub's published number for this chip.
5. Only when the vendor path matches the published number, wire the model into our server and benchmark.

## 5. Tools in place (keep)
- `npu-serve` / `~/tools/geniex-serve` (shim + server), `~/tools/npu-bench/bench.py` (records runtime, placement, provenance), `models`.
- `qai-hub-models` CLI in Debian proot (`/root/venvs/qai-hub`).
- Models organized under `Documents/Models/{gguf,qairt/<chip>,speech,runtimes}`. Docs organized under `Vendor-Registries/<vendor>/`.
