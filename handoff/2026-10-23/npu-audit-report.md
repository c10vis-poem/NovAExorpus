# NPU audit: prior work vs Qualcomm / GenieX vendor docs

Date: 2026-10-23. Scope: read-only audit, with no installs, no model runs and no edits outside this report and the progress file.
Device: Motorola razr ultra 2025, `getprop ro.soc.model` = `SM8750`, Hexagon v79.

## Sources

**Read (in full unless marked):**
- `~/.claude/NPU-ON-DEVICE.md` (1-65)
- GenieX fork `~/repos/GenieX` at `692086f0` (2026-10-23), docs/en, all 20 pages:
  - get-started: platforms, quickstart, what-is-geniex
  - run/android: install, quickstart, api-reference
  - run/cli: install, quickstart, reference. local-server was not read.
  - run/linux: install
  - resources: troubleshooting, faq
  - tutorials: benchmarking
  - models: supported
  - python, audio-input and speculative-decoding pages were not read: they cover no Android or setup steps.
- GenieX `notes/`: README, AI, build, run, bench, release.
- GenieX source excerpts:
  - `sdk/plugins/llama_cpp/src/plugin.cpp:60-130`
  - `sdk/plugins/llama_cpp/src/params.cpp`, grep only
  - `sdk/benchmark/qdc/tests/test_bench.py:1-110`
  - `bench-models.json`
  - git log since 2026-09-28
- llama.cpp `origin/master` (`32dd62ee6`):
  - `docs/backend/snapdragon/README.md` and `developer.md`, in full
  - `linux.md`, grep only
  - `scripts/snapdragon/run.py`: the env and command sections (lines 1-38, 145-520)
  - `ggml-hexagon.cpp` getenv list (8234-8308)
- Vault and Aesop-Xi:
  - `NovAExorpus/HTP/`: all 4 files
  - `~/repos/Aesop-Xi/HTP/`: both files
- QAIRT-QNN vault:
  - `android-qnn-net-run.sh` (in full)
  - `android.html`, `genai.html`, `basic.html`, `no_lora.html` (text)
- Vendor wiki `02_wiki_md/vendors/qualcomm`:
  - `README_master.md` head
  - `GENIE_README.md`
  - grep across all 129 files for ADSP, fastrpc and geniex
- Tools:
  - `~/bin/npu-serve`
  - `~/tools/geniex-serve/` (`shim.c`, `models.json`, `server.py` grep, v0.7.1 header `ModelConfig`)
  - `~/tools/geniex-bench*/` listings
  - `~/tools/geniex-bench-android-arm64-v0.7.1/npu-test.log`, grep
  - `~/.cache/geniex-serve.log`, grep
  - `~/.cache/geniex-apk-build.log`, tail
  - `~/tools/llama-hexagon/server*.log`
- Session logs:
  - `2026-10-01/npu-test{,2..5}.log`, grep
  - `2026-10-01/WRAPUP-NOTES.md`
  - `2026-10-02/SESSION-LOG.md`, NPU lines
  - `2026-10-04/SESSION-LOG.md`, grep
  - `2026-10-08/agent-npu-queue.md`
- Vault docs:
  - `docs/NPU-BENCHMARKS.md`, `NPU-FINDINGS-2026-10-02.md`, `NPU-SERVE-BUILD-LOG.md`, `NPU-SERVE-USER-GUIDE.md`
  - `PENDING.md` and `RESUME.md`, NPU lines only

**Not read:**
- The QAIRT SDK html beyond the pages listed above. The vault dump has 138 html files and no index page was found.
- GenieX `geniex-qairt` plugin source.
- The 2026-10-01 transcript.
- logcat. No saved logcat file was found, so the `0x80000414` lines were never seen first-hand.
- The ai-hub-apps chat app README.

**Live probes, all read-only:**
- `getprop`
- `/sys/.../cpufreq/policy*`
- `ls /vendor/lib64/lib*dsprpc.so` and `ls /vendor/dsp`
- `/proc/self/attr/current`
- `termux-battery-status` and thermal zones
- `pm list packages`
- `gh release list -R qualcomm/GenieX`

---

## Q1. Vendor install and setup steps per route, and what the device did

### Route A: GenieX `llama_cpp` plugin on GGUF

The vendor's documented Android path is not a Termux CLI:
- **App path.** The Kotlin SDK `com.qualcomm.qti:geniex-android` via Gradle (`run/android/install.mdx:28-69`), or the GenieX Chat sample app (`install.mdx:10-18`).
- **CLI and bench path.** `geniex` CLI and `geniex-bench` are documented for Windows ARM64 and Linux ARM64 only (`run/cli/install.mdx:8`, `run/cli/reference.mdx:252`, `tutorials/benchmarking.mdx:10-70`).
- **Raw-binary path on Android.** It exists only in developer notes:
  - `notes/build.md:187-195`: `adb push pkg-geniex /data/local/tmp/geniex`, then in `adb shell`: `LD_LIBRARY_PATH=./lib GENIEX_PLUGIN_PATH=./lib ./bin/...`.
  - Qualcomm's own Android bench harness: `sdk/benchmark/qdc/tests/test_bench.py:49,94`, which runs `cd /data/local/tmp/pkg-geniex && LD_LIBRARY_PATH=…/lib GENIEX_PLUGIN_PATH=…/lib ./bin/geniex-bench … -r 3 -c <ctx> -p <pp> -n <tg> --chipset <chip>` as the **adb shell user**.
- The Android bench tarball URL is in `notes/bench.md:194`.

| Vendor step | Source | Device status (evidence) |
|---|---|---|
| Get the Android bench/SDK package for the current release | `notes/bench.md:194`, `release.md:11` | DONE for v0.3.14 (`~/tools/geniex-bench`, files dated Jul 1) and v0.7.1 (`~/tools/geniex-bench-android-arm64-v0.7.1`; sha in `dl-geniex/*.sha256` = `857879f8…`). **Stale:** latest upstream is **v0.9.3 (2026-10-19)**, from `gh release list`. |
| Run from `/data/local/tmp/<pkg>` as the adb shell user | `build.md:190-195`, `test_bench.py:94` | **NOT DONE.** Everything ran from Termux, SELinux context `u:r:untrusted_app_27` (`/proc/self/attr/current`). The adb shell-user test has been an open item since 2026-10-01 (`NPU-FINDINGS-2026-10-02.md:28`, `NPU-SERVE-BUILD-LOG.md` §7 item 1). |
| `LD_LIBRARY_PATH=./lib`, `GENIEX_PLUGIN_PATH=./lib` | `test_bench.py:49` | DEVIATED: `npu-serve:19` uses `lib:lib/llama_cpp:lib/qairt:/vendor/lib64`. `/vendor/lib64` was needed because Termux's linker namespace could not find `libOpenCL.so` (`2026-10-01/npu-test.log:6`). |
| Skel reachable by FastRPC | GenieX sets `ADSP_LIBRARY_PATH` itself (`plugin.cpp` at HEAD lines ~110-118) | WORKAROUND. v0.7.1 sets `ADSP_LIBRARY_PATH` to `lib` (`npu-test.log:14`) while the skel lives in `lib/llama_cpp`, which caused `0x80000406` (`2026-10-01/npu-test2.log:24`). The device fix is the symlink `lib/libggml-htp-v79.so` (`ls -la ~/tools/geniex-bench*/lib`; `NPU-ON-DEVICE.md:13-16`). Upstream fixed this in commit `550977d0` ("support flattened llama plugin layout", 2026-10-19), after v0.7.1. |
| `libcdsprpc.so` resolvable | `troubleshooting.mdx:102-109` | DONE: `/vendor/lib64/libcdsprpc.so` exists and is world-readable (`ls -la`). |
| Q4_0 weights | `supported.mdx:319-326`, `run.md:142` | PARTIAL: Qwen 3.5 2B (Unsloth, AI Hub's asset) has Q5_K `ssm_out` and Q6_K `token_embd`, which run on the CPU (`NPU-FINDINGS:10`). Qualcomm's own QDC bench uses the same file (`bench-models.json:17`). |
| Power mode burst (default) | `run.md:79-83`, `cli/reference.mdx:234` | DONE: `geniex-serve.log:26-34` shows "power mode set to burst" and "HTP0 power mode: burst". `shim.c:38,119` sets BURST. |
| Confirm the NPU is engaged | `troubleshooting.mdx:113` | DONE: `Hexagon Arch version v79` and `HTP0 new session` appear (`npu-test.log:22,31`). Note: the env var used, `GGML_HEX_VERBOSE` (`npu-serve:19`, `NPU-ON-DEVICE.md:20`), is **not read by llama.cpp**. Only `GGML_HEXAGON_VERBOSE` is (`ggml-hexagon.cpp:8234`). The vendor doc has the same typo (`troubleshooting.mdx:113`). The proof lines come from GenieX DEBUG logging anyway. |
| Bench protocol: 512 random pp, 128 tg, 1 warmup + 5 runs, median (CLI doc); QDC: `-r 3`, ctx 512/1024/4096 | `benchmarking.mdx:108,181-188`; `notes/bench.md:67-72` | DEVIATED. Recorded numbers come from a 256-token real prompt with the phone loaded (`NPU-ON-DEVICE.md:57`), a 220-token request (`:28`) and server streaming. See Q3 for the v0.7.1 run. |
| Official Android baseline (GenieX Chat app) | `install.mdx:10-18` | PARTIAL: built in CI (`~/.cache/geniex-apk-build.log:113-127`) and used once (`2026-10-02/SESSION-LOG.md:72,78`: Gemma 4 E4B 9.5–13.2 tok/s, "same slowness in Qualcomm's own app"). It is **not installed now**: `pm list packages \| grep -c geniex` returned 0, and the app id is `com.geniex.demo` (`ai-hub-apps/geniex_chat_android/build.gradle:18`). No Qwen 3.5 2B run in the vendor app was found. |
| Model paths valid | – | BROKEN NOW: `npu-serve:15` defaults to, and `models.json:3-28` points at, `/storage/emulated/0/Documents/Models/…`, which is "No such file or directory". The models are now in `Documents/_models/`. |

### Route B: GenieX `qairt` plugin on AI Hub precompiled bundles

Vendor steps:
1. Pull with an explicit chipset (`"SM8750"`). This is required on Android (`platforms.mdx:40`, `android/api-reference.mdx:90,125`).
2. Or import a local bundle (metadata.json + .bin, or the AI Hub .zip) with `HubSource.LOCALFS` or `geniex pull --local-path`. The import generates `geniex.json` (`supported.mdx:197-229`; `run.md:152` "QAIRT models need a `geniex.json`").
3. Load with `runtime_id="qairt"`, `nCtx=0`, `nGpuLayers=0` (`platforms.mdx:117-119`).
4. Use the bundled QAIRT runtime, or override it with `GENIEX_QAIRT_LIB` / `geniex_set_qairt_runtime_path`. An SDK-root override points `ADSP_LIBRARY_PATH` at `lib/hexagon-v*/unsigned` (`run.md:154-193`).
5. The raw QAIRT Android recipe for v79 puts `libQnnHtp.so`, `libQnnHtpPrepare.so`, `libQnnHtpV79Stub.so` and `hexagon-v79/unsigned/libQnnHtpV79Skel.so` in one directory, with `ADSP_LIBRARY_PATH=<dir>` and `LD_LIBRARY_PATH=<dir>`, run from adb shell (`QAIRT-QNN/android-qnn-net-run.sh:166-173,213`; Genie tutorial `no_lora.html`: `genie-t2t-run` from `/data/local/tmp`, `LD_LIBRARY_PATH=/data/local/tmp/`).

| Vendor step | Device status |
|---|---|
| Bundle for this chip (SoC `SM8750` maps to AI Hub `qualcomm-snapdragon-8-elite`) | **Not found.** On disk (`ls _models/qairt`): `8-elite-galaxy/` (InternVL 2B and 4B, SmolLM2 1.7B), `x-elite/`, `x2-elite/`. "Galaxy" is the separate `SM8750-AC` alias (`platforms.mdx:30`). `getprop ro.soc.model` returns plain `SM8750`. No base-8-Elite bundle and no text-LLM bundle (other than the SmolLM2 galaxy zip, not unpacked) were found by `ls _models/qairt/* _models/installed`. |
| qairt plugin libs load | v0.7.1 bench run: **FAILED**. `npu-test.log:6`: `libgeniex_vlm.so not found` because `lib/qairt` was not on `LD_LIBRARY_PATH`. The same failure appears in every 2026-10-01 test (`npu-test{,2..5}.log:9-10`). Under `npu-serve` it is fixed: `geniex-serve.log:4-7` shows "Registered plugin: qairt". |
| QAIRT runtime files | Present in the v0.3.14 package: `lib/qairt/htp-files/` has `libQnnHtp.so`, `libQnnHtpV79Stub.so`, `libQnnHtpV79Skel.so`, `libQnnSystem.so`, `libQnnHtpPrepare.so` (`ls -la`). The v0.7.1 `htp-files` directory exists but was not listed in this audit. |
| Import via LOCALFS / `pull --local-path` (generates `geniex.json`) | **NOT DONE.** The bundle was fed straight to `geniex_vlm_create` through the custom shim, pointing at `genie_config.json` as a workaround for error `-100004` (`SESSION-LOG 10-02:90,97`; `NPU-SERVE-USER-GUIDE.md:132`). |
| `nCtx=0`, `nGpuLayers=0` | DONE (`shim.c:35,117-118`). |
| `ADSP_LIBRARY_PATH` covering the QAIRT skel | UNVERIFIED. In the serve process the llama_cpp plugin overwrote `ADSP_LIBRARY_PATH` to `…/v0.7.1/lib` (`geniex-serve.log:16`), and the variable is process-wide (`run.md:229-234`). How the v0.7.1 qairt plugin locates `libQnnHtpV79Skel.so` was not read. |
| `geniex-bench --plugin qairt` run | Not found in any log probed. |

### Route C: llama.cpp `llama-server` with Hexagon

Vendor steps (llama.cpp `docs/backend/snapdragon/README.md`):
1. Build with the Docker toolchain `ghcr.io/snapdragon-toolchain/arm64-android:v0.7` via `scripts/snapdragon/build.py` (`:5-13,27-30`).
2. `adb push pkg-android/llama.cpp /data/local/tmp/` (`:102-110`).
3. Run through `run.py --target adb`, which executes `cd /data/local/tmp/llama.cpp && LD_LIBRARY_PATH=./lib ADSP_LIBRARY_PATH=./lib … <tool> --device HTP0 -ngl 99 -fa on --ubatch-size 1024 -t 6` with `GGML_HEXAGON_OPPOLL=1` as the adb shell user (`run.py:163,404-420,427-443`).

| Vendor step | Device status |
|---|---|
| Built with the vendor toolchain at a known commit | NOT DONE. `~/tools/llama-hexagon` is a prebuilt of unknown provenance from vault `llm-wiki/` (Jul 4) (`NPU-ON-DEVICE.md:52`). `~/llama.cpp/build` is CPU-only: no `libggml-h*` was found by `find -maxdepth 3`. |
| Binaries and libs consistent | FAILED: `server2.log:1` shows `CANNOT LINK … common_models_handler_init`, a lib/binary mismatch. |
| `ADSP_LIBRARY_PATH=./lib`, adb shell user | Not found in any launch script or log. Only `ai-web` launches `llama-server`, CPU only (`~/bin/ai-web:6,15`). |
| `-fa on -ub 1024 -t 6` | Unknown for the hexagon runs. `server.log:3-11` shows HTP0 listed but decode 2.66 tok/s, which is consistent with `NPU-ON-DEVICE.md:52` "falls back to CPU". |

---

## Q2. Was the qairt route properly attempted?

It was **partly attempted, but not by the vendor route.** Evidence:
- `2026-10-02/SESSION-LOG.md:99`: InternVL 4B qairt (8-Elite-for-Galaxy bundle), decode 15.4–17.1 tok/s. This matches AI Hub's 16.0–16.4, while prefill was about a third of AI Hub's.
- `SESSION-LOG.md:104`: X Elite InternVL 2B bundle, decode 27.5 tok/s, with `Context create from binary failed … err 5005` logged.
- `NPU-FINDINGS-2026-10-02.md:29` ("never done") is **stale** and contradicts these runs.

What is missing:
1. **The bundle for this exact chipset.** The device reports `SM8750`, and AI Hub's id for it is `qualcomm-snapdragon-8-elite` (`platforms.mdx:22,30`). Only galaxy and X-series bundles are on disk. Cross-chip variants should still be tested (operator rule), but the exact-match bundle has never been fetched. The pull needs `chipset="SM8750"` (`api-reference.mdx:90`).
2. **A text-LLM qairt bundle.** No text LLM has ever been run on qairt. Qwen 3.5 2B is a GGUF-only AI Hub asset per `NPU-ON-DEVICE.md:64`. GenieX's Android list of qairt LLMs is `ai-hub-models/Qwen3-4B-Instruct-2507` (`api-reference.mdx:346-349`). QDC also benches `qualcomm/qwen3_4b` and `qwen3_4b_instruct_2507` (`bench-models.json:26-27`). Neither was found on disk by `ls _models/qairt`.
3. **The vendor import path.** LOCALFS / `pull --local-path` generates `geniex.json` (`run.md:152`, `supported.mdx:229`). The shim's `genie_config.json` path hack skips it.
4. **A vendor measurement.** No `geniex-bench --plugin qairt` run was found. The QDC protocol is `test_bench.py:94-97`.
5. **The skel search path.** It is unverified for qairt in a process where llama_cpp has already rewritten `ADSP_LIBRARY_PATH`. Vendor practice is `ADSP_LIBRARY_PATH` set to the skel directory (`android-qnn-net-run.sh:171`; `run.md:190-191`).
6. **The bench's `LD_LIBRARY_PATH`.** It lacked `lib/qairt`, so the qairt plugin never loaded in any `geniex-bench` run (`npu-test.log:6`).

---

## Q3. Deviations that plausibly explain the speed gap and `0x80000414`

Ranked by evidence strength:

1. **The phone is clock-capped, today and on every recorded test day.**
   - Live probe: policy0 `scaling_max_freq` 1,555,200 of 3,532,800; policy6 1,017,600 of 4,320,000. Battery 10%, charging; CPU zones about 61 °C.
   - Same pattern on 10-02 (`NPU-FINDINGS:19-20`) and 10-08 (`agent-npu-queue.md` Blocked).
   - Why it matters: Qwen 3.5 makes 38 CPU↔HTP handoffs per token (`NPU-FINDINGS:10`), and in `npu` mode the host thread busy-waits on the HTP (`run.md:111`). Decode is therefore CPU-clock-bound.
   - The vendor app showed the same slowness (`SESSION-LOG 10-02:72`).
   - Qualcomm's QDC numbers come from uncapped devices. That is an inference, not read in a file.

2. **The v0.7.1 "2.7 tok/s DSP-queue" number is a measurement artifact.**
   - `npu-test.log:1273-1297`: `generated_tokens: 7, stop_reason: eos`, giving `[ok] … decode=2.8tps gen=7 tok`. v0.7.1's bench stopped at EOS on random-token prompts.
   - Upstream fixed this in `e36f6ab0` ("run geniex-bench timing runs to n_gen tokens, ignoring EOS", 2026-10-14).
   - The v0.3.14 run generated the full 128 tokens (`2026-10-01/npu-test5.log:845,888`, decode 16.5).
   - So `NPU-ON-DEVICE.md:62` and `WRAPUP-NOTES.md:7` misattribute the number to `0x80000414`. The log shows no `0x8000*` lines (grep on `npu-test.log`).

3. **The process runs in the wrong security context.**
   - Every vendor Android recipe runs as the adb shell user from `/data/local/tmp`: GenieX `build.md:190-195` and `test_bench.py:94`; llama.cpp `run.py:427-443`; QAIRT `android-qnn-net-run.sh:213` and `no_lora.html`.
   - The device runs in `untrusted_app_27`. `ls /vendor/dsp` returns Permission denied.
   - `geniex-serve.log:22` shows `FASTRPC_GET_DOMAINS query failed (0x6c), using static CDSP domains`.
   - The HMX max-clock vote refusal (`0x80000414`, `NPU-ON-DEVICE.md:28`) is consistent with a non-privileged context, but it is **untested**. The adb-shell A/B run has been pending since 2026-10-01.

4. **CPU thread pinning fails, and the thread layout differs from the vendor's.**
   - `failed to set affinity mask … Invalid argument (22)` appears at `geniex-serve.log:2462,2465` and `npu-test.log:1265,1272`.
   - The threadpool reports `n_threads=8 … pinned_cores=[0,1,2,3,4,5,6,7]` (`geniex-serve.log:2464`).
   - The vendor uses 6 threads on cores [2,8) (`run.md:138`; llama.cpp `run.py:419-420` `-t 6`).
   - With pinning failing and 8 threads on capped cores, the polling host thread competes with the workers.

5. **The GenieX binaries are 4 releases behind.**
   - The device has v0.3.14 and v0.7.1; upstream is at v0.9.3 (`gh release list`).
   - Post-v0.7.1 fixes on the fork's `main` that matter here (`git log --since=2026-09-28`):
     - `999fd1d1` warm up at load so HTP mapping stays out of TTFT
     - `3133c664` llama.cpp bump
     - `e36f6ab0` bench to n_gen
     - `550977d0` `ADSP_LIBRARY_PATH` nested layout (removes the symlink hack)
     - `4457e88d` and `2910f700` `MBUF` caps

   The fork is synced (`692086f0`), but the runtime was never updated.

6. **The compute-unit guidance is misquoted.**
   - `NPU-ON-DEVICE.md:8` cites `platforms.mdx:95` for "hybrid is not the fast path".
   - The vendor docs say the opposite: `platforms.mdx:81,98` ("`hybrid` … **The fast path on Snapdragon**"), `benchmarking.mdx:156` ("Default recommendation"), `faq.mdx:40`, and `notes/run.md:108-115` (npu-pinned is "slower on LLMs", CPU pegged).
   - The device's own best result was hybrid, 20.5 tok/s (`NPU-ON-DEVICE.md:61`).
   - This is a citation correction, not a change of the operator's 100%-NPU goal. Qualcomm's QDC bench for Qwen3.5-2B runs `npu`, not hybrid (`bench-models.json:17`).

7. **The benchmark protocol is not the vendor's.**
   - Device runs used real 220- or 256-token prompts on a loaded phone.
   - The vendor uses 512 random tokens, 128 generated, 1 warmup + 5 runs, median (`benchmarking.mdx:108`), or QDC `-r 3` over ctx 512/1024/4096 (`notes/bench.md:67-72`).
   - So the numbers are not directly comparable to 22.6–24.8.

8. **Minor issues:**
   - `GGML_HEX_VERBOSE` is a no-op name. The real variable is `GGML_HEXAGON_VERBOSE` (`ggml-hexagon.cpp:8234`).
   - `GGML_HEXAGON_OPPOLL=1`, a `run.py:163` default, is not set by `npu-serve:19`. Whether GenieX sets it internally was not checked.
   - The operator's HTP notes use `D=HTP0,HTP1` (`NovAExorpus/HTP/HTP-Memory-Architecture…md:29,45`). That is not a vendor variable: the vendor uses `GGML_HEXAGON_DEVICES` or `--device` (llama.cpp README `:309-322`).
   - Matches the vendor: flash-attn on and `n_ubatch=1024` (`geniex-serve.log:1286`), burst power (`:26-34`).

**`0x80000414` specifically:** no saved logcat containing it was found. It is not in the GenieX logs grepped (`npu-test.log`, `geniex-serve.log`). The root cause given in `NPU-ON-DEVICE.md:28` (llama.cpp #22352 / PR #22334) was not re-verified here. The adb shell-user run is the test that would separate "Termux context" from "firmware refuses HMX vote".

---

## Q4. Corrected setup checklists (vendor-exact; done / missing on this device)

### Route A: GenieX llama_cpp, GGUF

0. [ ] `gh repo sync c10vis-poem/GenieX` (done at `692086f0`). Download `geniex-bench-android-arm64-v0.9.3.tar.gz` and its `.sha256`, `sha256sum -c` (`notes/bench.md:204`). **MISSING** (on v0.7.1).
1. [ ] Put the device in a vendor-like state: plugged in, battery not low, cpufreq `scaling_max_freq == cpuinfo_max_freq` on both policies, nothing else running. **MISSING** (capped right now).
2. [ ] Stage as the vendor does: copy the package to `/data/local/tmp/geniex` and the model to `/data/local/tmp/geniex/modelfiles/llama_cpp/` (`build.md:190-191`). Run from an adb shell over loopback wireless debugging, with no PC (`NPU-ON-DEVICE.md:65`). **MISSING.**
3. [ ] Env exactly `LD_LIBRARY_PATH=./lib GENIEX_PLUGIN_PATH=./lib` (`test_bench.py:49`). No `/vendor/lib64` (needed only under Termux), and no symlink on v0.9.3 (`550977d0`). Status: DONE under Termux with the two workarounds.
4. [ ] Run `./bin/geniex-bench --plugin llama_cpp --device npu -m <Qwen3.5-2B-Q4_0.gguf>` at the defaults (512/128/1+5), then `--device cpu` and `--device hybrid` (`benchmarking.mdx:110-150`). Optionally run the QDC form `-r 3 -c 512|1024|4096 --chipset SM8750` (`test_bench.py:94-97`). **MISSING** for v0.9.3 and adb shell.
5. [ ] Verify `Hexagon Arch version v79`, `HTP0 new session`, `offloaded N/N`, and **gen=128** in the output (`troubleshooting.mdx:113`). Use `GGML_HEXAGON_VERBOSE=1`. DONE except the correct env name.
6. [ ] Repeat steps 3–5 under Termux with the same package for the A/B comparison. Only then port to `npu-serve`, rebuilding the shim against v0.9.3's header (`NPU-SERVE-BUILD-LOG.md` §6). **MISSING.**
7. [ ] Repair `npu-serve:15` and `models.json` paths to `Documents/_models/…`. **MISSING.**

### Route B: GenieX qairt, AI Hub bundles

1. [ ] Fetch the bundle for **`qualcomm-snapdragon-8-elite` (SoC SM8750)**, at minimum one text LLM GenieX lists (`Qwen3-4B-Instruct-2507`, `api-reference.mdx:348`), plus the existing galaxy and X-series variants as cross-chip candidates. **MISSING** (exact-chip bundle).
2. [ ] Import as the vendor does: metadata.json + `.bin` or the AI Hub `.zip` through LOCALFS / `pull --local-path`, which generates `geniex.json` (`supported.mdx:197-229`; `run.md:152`). **MISSING** (the shim's `genie_config.json` hack).
3. [ ] Use the bundled QAIRT runtime, or `GENIEX_QAIRT_LIB=<QAIRT root>` so `ADSP_LIBRARY_PATH` covers `lib/hexagon-v79/unsigned` (`run.md:154-193`). Confirm with `--log info` showing "host libs:". **UNVERIFIED.**
4. [ ] `LD_LIBRARY_PATH` must include `lib/qairt` or the plugin fails to load (`npu-test.log:6`). DONE in `npu-serve`, **MISSING** in bench runs.
5. [ ] `nCtx=0`, `nGpuLayers=0`, power burst (`platforms.mdx:119`). DONE (`shim.c`).
6. [ ] Measure with `geniex-bench --plugin qairt --device npu -m <bundle dir>` (`cli/reference.mdx:258-260`). Remember that prefill is reported over 128-token padding (`benchmarking.mdx:175`). Do it as the adb shell user and under Termux. **MISSING.**
7. [ ] Raw QAIRT cross-check (optional): put the `libQnnHtp*` files, the `V79Stub` and the `hexagon-v79/unsigned` skel in one directory with `ADSP_LIBRARY_PATH` and `LD_LIBRARY_PATH` set to it, then run `genie-t2t-run -c <genie_config.json>` (`android-qnn-net-run.sh:166-173`; `no_lora.html`). **MISSING.**

### Route C: llama-server with Hexagon

1. [ ] Build at a known `origin/master` commit with `scripts/snapdragon/build.py --target adb`, which uses the `arm64-android:v0.7` toolchain (README `:9,27-30`). The Docker toolchain needs a host or CI; the GenieX APK was already built in CI (`geniex-apk-build.log`), so the same approach works. **MISSING** (only an unknown-provenance prebuilt exists, and it fails to link: `server2.log:1`).
2. [ ] Install to `/data/local/tmp/llama.cpp` (README `:102-110`). **MISSING.**
3. [ ] Run as the adb shell user: `LD_LIBRARY_PATH=./lib ADSP_LIBRARY_PATH=./lib GGML_HEXAGON_OPPOLL=1 ./bin/llama-server -m … --device HTP0 -ngl 99 -fa on --ubatch-size 1024 -t 6` (`run.py:404-443`). **MISSING.**
4. [ ] Verify with `test-backend-ops -b HTP0 -o MUL_MAT` (README `:188-199`) and `llama-bench -p 128 -n 64` against README `:210-213`. **MISSING.**

---

## Corrections owed to existing docs (not edited: read-only audit)

- `NPU-ON-DEVICE.md`:
  - `:8`: hybrid citation is wrong. Vendor says hybrid is the fast path (`platforms.mdx:98`).
  - `:62` and `:31`: the v0.7.1 2.7 tok/s figure was a 7-token EOS run (`npu-test.log:1273-1297`).
  - `:20` and others: `GGML_HEX_VERBOSE` should be `GGML_HEXAGON_VERBOSE`.
- `NPU-FINDINGS-2026-10-02.md:29`: the qairt runs did happen (`SESSION-LOG 10-02:99,104`).
- `NPU-SERVE-BUILD-LOG.md:77`: the "hybrid is the fast path" claim it calls wrong is what the vendor docs say.
- `npu-serve:15` and `models.json`: stale `Documents/Models` paths.
