# NPU install plan: Snapdragon 8 Elite (SM8750, Hexagon v79), on the phone

Date: 2026-10-23. Author: agent-npu-plan (read-only pass, no installs, downloads, model runs or edits outside this file and the progress file).
Builds on `~/.claude/NPU-ON-DEVICE.md` (read in full, 65 lines) and today's audit `~/.claude/session-work/2026-10-23/npu-audit-report.md` (read in full, 256 lines).
Citation style: `file:line`. GenieX paths are relative to `~/repos/GenieX` (fork at `692086f0`, `main`, synced). `docs/...` = `docs/en/...`. llama.cpp paths are `~/llama.cpp` at `origin/master` = `4231b23dc` (fetched today; the local checkout `32eddaf2e` is from June and was not used). QAIRT html pages are cited by the line of their extracted text, because the files are single-line html.
Anything marked **[no on-device doc]** is standard Android/AOSP behaviour that no file on this phone documents; it is given as a command whose output proves or disproves it.

---

## 0. What changed versus what the notes say (read this first)

1. **Newest GenieX release is v0.9.3** (2026-10-19, marked Latest; `gh release list -R qualcomm/GenieX`). Newer **tags without releases** exist: `v0.9.4-alpha.1` (10-20) and `v0.9.4-alpha.2` (10-21) (`git ls-remote --tags`). `gh release view v0.9.4-alpha.2` returned "release not found", so there are no assets for them. Tags containing `-` are drafts (`notes/release.md:9`). Plan targets v0.9.3.
2. **The skel symlink is still needed on v0.9.3.** The fix for the nested `lib/llama_cpp` layout (`550977d0`, 2026-10-19) is *not* an ancestor of `v0.9.3` (`git merge-base --is-ancestor` = no); it is in both v0.9.4 alphas. At v0.9.3, Android sets `ADSP_LIBRARY_PATH` to `GENIEX_PLUGIN_PATH` without `/llama_cpp` (`v0.9.3:sdk/plugins/llama_cpp/src/plugin.cpp:103-120`), while the skels are installed to `lib/llama_cpp` (`v0.9.3:sdk/plugins/llama_cpp/CMakeLists.txt:62-67`).
3. **v0.9.3 bundles a newer llama.cpp that runs K-quant matmuls on the HTP.** v0.9.3 pins llama.cpp `e467e5b5` (2026-10-15); v0.7.1 pinned `94256114` (2026-09-23) (`git ls-tree <tag> third-party/llama.cpp`). `e467e5b5` treats `Q4_K/Q5_K/Q6_K/Q3_K/Q2_K` as HTP repack types and accepts them in MUL_MAT (`e467e5b5:ggml/src/ggml-hexagon/ggml-hexagon.cpp:318-323`, and the `supports_op` switch about line 7036-7046). `94256114` has zero `GGML_TYPE_Q5_K` references in the Hexagon backend. Qwen 3.5's Q5_K `ssm_out` was the CPU fallback (`NovAExorpus/docs/NPU-FINDINGS-2026-10-02.md:10`). Re-measure placement on v0.9.3 before requantizing. GenieX's own docs still say K-quants are "not optimized for Hexagon NPU" (`docs/models/supported.mdx:324`).
4. **v0.9.3 opens two HTP sessions by default.** If neither `GGML_HEXAGON_DEVICES` nor `GGML_HEXAGON_NDEV` is set, the plugin sets `GGML_HEXAGON_DEVICES=2` so a VLM's mmproj can use `HTP1` (`v0.9.3:plugin.cpp:66-75`).
5. **New finding from a live probe: Termux cannot use the two prime cores.** `/proc/self/status` shows `Cpus_allowed_list: 0-5`, cpuset `/foreground` (`/proc/self/cgroup`). Cores 6-7 are policy6, the 4.32 GHz cluster (`policy6/related_cpus` = `6 7`). GenieX pins its offload threadpool to "6 threads ... cores [2, 8)" (`notes/run.md:138`), so under Termux two of the six pins are illegal. That matches the `failed to set affinity mask … Invalid argument (22)` lines the audit found (audit Q3.4). This is a second, independent reason to run as the adb shell user, alongside SELinux.
6. **The CPU is capped while cool.** Live probe today: policy0 `scaling_max_freq` 2,227,200 of `cpuinfo_max_freq` 3,532,800; policy6 1,958,400 of 4,320,000. Governor `walt`, battery 67 % unplugged at 27 °C, CPU zones about 43 °C. The audit saw 1,555,200 / 1,017,600 at 10 % charging and about 61 °C (audit:160). The cap moves with battery state, not temperature alone. Its cause is unidentified.
7. **The vendor docs say `hybrid` is the fast path.** See section 5. This corrects the citation only. The operator's 100 %-NPU target stays; Qualcomm's own QDC bench runs Qwen3.5-2B as `npu` (`sdk/benchmark/qdc/bench-models.json:17`).
8. **Prebuilt GenieX binaries exist only upstream.** `gh release list -R c10vis-poem/GenieX` returns nothing: the fork has no releases. Source and docs come from the fork (synced); the signed Android bench tarball must come from `qualcomm/GenieX` releases. **Operator decision**, because the standing rule says to install from the fork.
9. **Stale paths in NPU-ON-DEVICE.md** (not edited here): `Vendor-Registries/GOOGLE _DEV/` (`:39`) does not exist; the LiteRT pages are in `Vendor-Registries/google-gemma-litert/` and `global-documentation-vault/qairt-docs/#QAIRT/`. `llm-wiki/` (`:52,:55`) now holds only 2 files: `Hexagon_SDK_Linux.zip` is at `_Merovingians_Keep/NovAExorpus-nested-mirror/llm-wiki/`. Models are in `Documents/_models/gguf` and `_models/qairt`, not `Documents/Models/` (`:37`).

---

## 1. GenieX upgrade to v0.9.3

### 1.1 Artifacts (from `gh release view v0.9.3 -R qualcomm/GenieX --json assets`)
- **Needed now:** `geniex-bench-android-arm64-v0.9.3.tar.gz` and `geniex-bench-android-arm64-v0.9.3.tar.gz.sha256`. The archive holds `bin/geniex-bench` plus `lib/` with libgeniex, the llama_cpp plugin and the qairt plugin (`notes/bench.md:220-221`). It is also the full Android C SDK: `npu-serve`'s shim links its `lib/libgeniex.so` (`NPU-ON-DEVICE.md:29`).
- **Later, for the Kotlin/APK path only:** `geniex-android-aar-v0.9.3.aar` and its `.sha256`. Do not use `geniex-android-aar-cpu-v0.9.3.aar`: it has no Hexagon or QAIRT (`docs/resources/troubleshooting.mdx:184`).
- **Not for this phone:** the `linux-arm64`, `windows-arm64` and `pysdist` assets.

### 1.2 URL pattern
- **GitHub release (primary):** `https://github.com/qualcomm/GenieX/releases/download/<tag>/geniex-bench-android-arm64-<tag>.tar.gz`, plus `.sha256`. Every release asset has a per-file `.sha256` sidecar (`notes/release.md:11`).
- **S3 mirror (secondary):** `https://qaihub-public-assets.s3.us-west-2.amazonaws.com/qai-hub-geniex/geniex-bench-android-arm64-<tag>.tar.gz` (`notes/bench.md:204`). Unpinned "latest": `…/geniex-bench-android-arm64.tar.gz` (`notes/bench.md:194`). Caveat: the S3 layout table in `notes/release.md:87-109` does not list bench archives, so treat the S3 URL as unverified until it returns 200.
- **Equivalent with gh:** `gh release download v0.9.3 -R qualcomm/GenieX -p 'geniex-bench-android-arm64-v0.9.3.tar.gz*' -D ~/tools/dl-geniex`.

### 1.3 sha256 verification
- The existing sidecar format already works with coreutils: `cd ~/tools/dl-geniex && sha256sum -c geniex-bench-android-arm64-v0.7.1.tar.gz.sha256` prints `…: OK` (run today).
- For v0.9.3, run `sha256sum -c geniex-bench-android-arm64-v0.9.3.tar.gz.sha256`. Expected output: `geniex-bench-android-arm64-v0.9.3.tar.gz: OK`. Anything else means stop.

### 1.4 Install layout: side by side, old versions kept
```
~/tools/dl-geniex/                                   # tarballs + .sha256 (v0.7.1 already here)
~/tools/geniex-bench/                                # v0.3.14 (existing, has lib/libggml-htp-v79.so symlink)
~/tools/geniex-bench-android-arm64-v0.7.1/           # v0.7.1 (existing)
~/tools/geniex-bench-android-arm64-v0.9.3/{bin,lib}  # NEW: tar -xzf … -C ~/tools/
```
- The top-level directory name follows the v0.7.1 pattern and `notes/bench.md:212` (`./geniex-bench-linux-arm64-*/bin/geniex-bench`).
- Expected contents, by analogy with v0.7.1 (listed today): `lib/libgeniex.so`, `lib/llama_cpp/{libggml-hexagon.so, libggml-htp-v73/75/79/81.so, libggml-cpu.so, libggml-opencl.so, libllama.so, libgeniex_plugin.so, …}`, `lib/qairt/{libgeniex_plugin.so, libgeniex_vlm.so, …, htp-files/libQnnHtp.so, libQnnHtpV79Stub.so, libQnnHtpV79Skel.so, libQnnHtpPrepare.so, libQnnSystem.so}`.
- The old versions stay until v0.9.3 passes steps 6-9 of the checklist. **The operator then decides on removal.** Nothing is deleted by this plan.

### 1.5 Skel symlink (still required at v0.9.3; see §0.2)
```
ln -sf llama_cpp/libggml-htp-v79.so ~/tools/geniex-bench-android-arm64-v0.9.3/lib/libggml-htp-v79.so
```
- Make the same link in the `/data/local/tmp` copy (§3).
- Why: FastRPC searches only `ADSP_LIBRARY_PATH`. If the skel is missing, logcat shows `apps_std_fopen … lib/./libggml-htp-v79.so` and the session fails with `0x80000406` (`NPU-ON-DEVICE.md:13-16,24`).
- Drop the link once a release containing `550977d0` (v0.9.4 or later) is installed.

### 1.6 Environment variables
| Variable | Value | Why / source |
|---|---|---|
| `LD_LIBRARY_PATH` | `lib:lib/llama_cpp:lib/qairt` (Qualcomm's own Android bench) | `v0.9.3:sdk/benchmark/qdc/tests/test_bench.py:50-53`. Under **Termux only**, append `:/vendor/lib64` for `libOpenCL.so` (`NPU-ON-DEVICE.md:17-21`). Without `lib/qairt` the qairt plugin does not load (`libgeniex_vlm.so not found`, audit:115). |
| `GENIEX_PLUGIN_PATH` | `lib` | `test_bench.py:53`; `notes/build.md:194` |
| `ADSP_LIBRARY_PATH` | `lib` (Qualcomm sets it; GenieX overwrites it with `GENIEX_PLUGIN_PATH` anyway) | `test_bench.py:52`; overwrite `setenv(...,1)` at `v0.9.3:plugin.cpp:115-120` |
| `GGML_HEXAGON_VERBOSE=1` | proof runs only. Logs every op (`llama.cpp docs/backend/snapdragon/README.md:358-368`), so leave it off for timed runs | read at `e467e5b5:ggml-hexagon.cpp:9975` |
| ~~`GGML_HEX_VERBOSE`~~ | **typo, no effect.** No getenv for it exists in `origin/master` or `e467e5b5`. The typo comes from `docs/resources/troubleshooting.mdx:113` and is copied in `NPU-ON-DEVICE.md:20` and `~/bin/npu-serve:19` (audit:98) | |
| `GGML_HEXAGON_OPPOLL=1` | A/B parameter. The backend default is `0` (`e467e5b5:ggml-hexagon.cpp:166`); Qualcomm's llama.cpp runner defaults to `1` (`scripts/snapdragon/run.py:223`). GenieX does not set it (`git grep` in `v0.9.3:sdk/plugins/llama_cpp/src`). | |
| `GGML_HEXAGON_DEVICES` | leave unset (GenieX sets `2`), or `1`/`3` for large-model splits (§4.3). `GGML_HEXAGON_NDEV` is deprecated | `README.md:309-322`; `plugin.cpp:69-75` |
| `GGML_HEXAGON_GDN_SELECT` | Qwen 3.5 recurrent layers: `2`=HMX, `1`=HVX, `0`=disable. A/B only | `run.py:232`; read at `e467e5b5:ggml-hexagon.cpp:9988` |
| Power | `--power-mode burst` is the default, the highest corner with DCVS disabled | `notes/run.md:77-83`; `docs/run/cli/reference.mdx:234,267`. Env equivalent `GGML_HEXAGON_POWER_MODE` (`README.md:333-350`) |

### 1.7 `~/tools/geniex-serve` shim ABI
- The C structs changed between v0.7.1 and v0.9.3 (`git diff v0.7.1 v0.9.3 -- sdk/include/geniex.h`: +81/-6 lines):
  - `geniex_SamplerConfig` gains `bool ignore_eos` (v0.9.3 `geniex.h:470-471`).
  - `geniex_LlmGenerateInput` gains `input_embd`, `input_embd_count` and `input_embd_dim` (`geniex.h:649-673`).
  - New decide APIs are added.
- The shim fills `in.config.power_mode` and sampler/generate structs (`~/tools/geniex-serve/shim.c:38,119`).
- **Rebuild against the v0.9.3 header.** Never load v0.9.3's `libgeniex.so` with the v0.7.1 shim; the ABI warning is at `NPU-ON-DEVICE.md:32`.
- Steps:
  1. Save `git -C ~/repos/GenieX show v0.9.3:sdk/include/geniex.h > ~/tools/geniex-serve/geniex-v0.9.3.h`. That follows the existing `geniex-v0.7.1.h` / `libgeniex_shim-v0.7.1.so` naming in that folder.
  2. Rebuild with the same command as the v0.7.1 shim (`NovAExorpus/docs/NPU-SERVE-BUILD-LOG.md` §6) into `libgeniex_shim-v0.9.3.so`.
  3. Leave the v0.7.1 files in place.
  4. Fix the stale model paths in `npu-serve:15` and `models.json` (`Documents/Models` → `Documents/_models/gguf`) at the same time (audit:101).

---

## 2. Device state before any benchmark

### 2.1 What Termux can read (probed today)
| Item | Command (Termux) | Result today |
|---|---|---|
| CPU cap | `for p in /sys/devices/system/cpu/cpufreq/policy*; do echo ${p##*/} $(cat $p/scaling_max_freq) $(cat $p/cpuinfo_max_freq) $(cat $p/scaling_cur_freq) $(cat $p/scaling_governor); done` | readable: policy0 2227200/3532800, policy6 1958400/4320000, `walt` |
| Usable cores | `grep Cpus_allowed_list /proc/self/status; cat /proc/self/cgroup` | `0-5`, cpuset `/foreground`. Prime cores 6-7 excluded |
| Temperatures | `for z in /sys/class/thermal/thermal_zone*; do echo $(cat $z/type) $(cat $z/temp); done` | readable (cpu-* ≈ 43 °C) |
| Battery | `termux-battery-status` | readable (67 %, UNPLUGGED, 27 °C) |
| Battery saver / thermal status | `settings get global low_power`, `dumpsys thermalservice` | **not readable**: `SecurityException … INTERACT_ACROSS_USERS`; `dumpsys: command not found` |
| devfreq (DDR, NPU bus) | `ls /sys/class/devfreq` | `Permission denied` |
| SELinux context | `cat /proc/self/attr/current` | `u:r:untrusted_app_27` |
| FastRPC device node | `ls /dev/adsprpc-smd` | not present / not visible |

### 2.2 What the adb shell user adds (after §3) **[no on-device doc; verify by output]**
- `adb shell dumpsys thermalservice`: thermal status and throttling state.
- `adb shell dumpsys power | grep -i -E 'mLowPowerMode|BatterySaver'` and `adb shell settings get global low_power`: whether battery saver is on.
- `adb shell dumpsys battery`: charge state.
- `adb shell grep Cpus_allowed_list /proc/self/status`: the shell user's cpuset. **This is the key check.** If it says `0-7`, the [2,8) pinning becomes legal.
- `adb shell ls -l /sys/devices/system/cpu/cpufreq/policy6/scaling_max_freq`: shows whether the shell user could write the cap. Normally it is root/system-owned, and nothing here assumes root.

### 2.3 Clearing the cap (no root; remove the cause, then confirm)
1. Plug the charger in and charge to ≥ 80 %. The audit day was capped harder at 10 %.
2. Turn battery saver off. Check it reads `0` via `adb shell settings get global low_power` **[no on-device doc]**.
3. Close other apps and let the CPU zones fall below 45 °C. NPU-FINDINGS:39 gives the same protocol.
4. Keep Termux visible. Background apps move to a smaller cpuset; `/foreground` is what the probe showed.
5. Success criterion: `scaling_max_freq == cpuinfo_max_freq` on **both** policies just before each run.
6. If the cap does not clear, record both values and the `dumpsys thermalservice` output with every result. A capped number is labelled capped, never compared to Qualcomm's QDC numbers (audit Q3.1, Q3.7).

---

## 3. adb shell over loopback wireless debugging (on the phone, no PC)

Why:
- Every vendor Android recipe runs from `/data/local/tmp` as the adb shell user:
  - GenieX `notes/build.md:187-196`
  - QDC `test_bench.py:114-118` with `BUNDLE_PATH=/data/local/tmp/pkg-geniex` (`v0.9.3:sdk/benchmark/qdc/tests/utils.py:21`)
  - llama.cpp `run.py:504-513` (Android target: no `adb root`; root is only used for `linux:adb`, `run.py:501-502`) and `README.md:102-110`
  - QAIRT `android-qnn-net-run.sh:166-173,213-214` and `no_lora.html` text 22-40
  - LiteRT-LM (`Run LLMs using LiteRT-LM.mht`, extracted text 437-450)
- Termux runs as `untrusted_app_27`, cannot list `/vendor/dsp` (audit:174), and gets `FASTRPC_GET_DOMAINS query failed (0x6c), using static CDSP domains` (audit:175). It is also limited to cores 0-5 (§0.5).
- The shell user is UID 2000, outside the app sandbox (operator note `NovAExorpus/01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md:95-98`).
- `adb` is already installed in Termux: `/data/data/com.termux/files/usr/bin/adb`, `Android Debug Bridge version 1.0.41 / 37.0.0p1-android-tools`.

Steps. The pairing flow follows `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md:95-97`; the Settings menu names are **[no on-device doc]**.
1. Turn on Settings → System → Developer options → **Wireless debugging**. Wi-Fi must be connected; traffic stays on 127.0.0.1.
2. Tap **Pair device with pairing code**. Note the pairing port and 6-digit code. Tip: put Termux and Settings in split screen so the dialog stays open.
3. In Termux, run `adb pair 127.0.0.1:<pairing_port> <code>`. Expected: `Successfully paired to 127.0.0.1:<pairing_port>`.
4. Read the **connect** port from the main Wireless debugging screen. It is a different port from the pairing port and is not 5555. Run `adb connect 127.0.0.1:<connect_port>`. Expected: `connected to 127.0.0.1:<connect_port>`.
5. Run `adb devices`. Expected: `127.0.0.1:<connect_port>	device`.
6. Verify the context:
   - `adb shell id` should show `uid=2000(shell)`.
   - `adb shell cat /proc/self/attr/current` should show `u:r:shell:s0`.
   - `adb shell ls /vendor/dsp` should list files where Termux got Permission denied.
   - `adb shell grep Cpus_allowed_list /proc/self/status` shows the cpuset (§2.2).
7. Stage the package like Qualcomm does (`notes/build.md:190-191`; QDC dir name `pkg-geniex`, `utils.py:21`). `/data/local/tmp` is `drwxrwx--x shell:shell` (probed today). The shell user cannot read Termux's private home, so files go over `adb push`, which reads them as the Termux user. Commands:
   ```
   adb push ~/tools/geniex-bench-android-arm64-v0.9.3 /data/local/tmp/pkg-geniex
   adb shell ln -sf llama_cpp/libggml-htp-v79.so /data/local/tmp/pkg-geniex/lib/libggml-htp-v79.so
   adb shell mkdir -p /data/local/tmp/pkg-geniex/modelfiles/llama_cpp /data/local/tmp/geniex-cache
   adb push ~/storage/shared/Documents/_models/gguf/Qwen3.5-2B-Q4_0.gguf /data/local/tmp/pkg-geniex/modelfiles/llama_cpp/
   ```
   Space: `/data` has 115 G free (`df -h`, today).
8. Run with Qualcomm's environment (`test_bench.py:50-53`):
   ```
   adb shell "cd /data/local/tmp/pkg-geniex && LD_LIBRARY_PATH=lib:lib/llama_cpp:lib/qairt ADSP_LIBRARY_PATH=lib GENIEX_PLUGIN_PATH=lib ./bin/geniex-bench --plugin llama_cpp --device npu -m modelfiles/llama_cpp/Qwen3.5-2B-Q4_0.gguf"
   ```
   There is no `/vendor/lib64` workaround here: Termux needed it only because of its linker namespace (audit:93).
9. For logcat on failures, run `adb logcat -d | grep -i -E 'adsprpc|fastrpc|cdsp'`. Termux's `logcat` saw only its own process; the shell user sees all. Error meanings: `0x80000406` = skel not found; `0x80000414` = dspqueue / HMX vote (`NPU-ON-DEVICE.md:24,28`).

What the A/B separates: the same binary and model run once as `untrusted_app` on cores 0-5 and once as `shell` on the shell cpuset. This is the pending test from `NPU-FINDINGS-2026-10-02.md:28` and `NPU-ON-DEVICE.md:65`. On `0x80000414`: QAIRT's HTP doc says an HMX vote is refused with `INVALID_INPUT` unless a DCVS_V3 vote is active on the same power-config id (`global-documentation-vault/qairt-docs/#QAIRT/HTP - Qualcomm AI Runtime (QAIRT) SDK.md:679-690`). That is a client-side vote-order rule, so do not assume SELinux causes it. The A/B is the test.

---

## 4. Per-model routing, as Qualcomm documents it

### 4.1 Decision rule
- **The model exists on Qualcomm AI Hub as a `geniex_qairt` bundle for this chip:** use the **qairt** route. It is "the fastest NPU path when your model is on Qualcomm AI Hub" (`docs/get-started/platforms.mdx:59,70,106`), NPU only, with precision and context fixed in the bundle (`platforms.mdx:117-119`).
- **Anything else (GGUF):** use **llama_cpp**. Q4_0 is the native Hexagon format (`docs/models/supported.mdx:321,326`). Q4_K_M and other K-quants are "not optimized" per GenieX docs (`supported.mdx:324`; `notes/run.md:142`), but see §0.3: v0.9.3's llama.cpp now has K-quant HTP kernels.
- **AI Hub's own GGUF assets are not fetched with `qai-hub-models fetch`.** The CLI raises `AssetNotFoundError` for `geniex_llamacpp` and points to the README/HF (`qai_hub_models_cli/fetch.py:170-187` in the Debian venv). The card's `fetch … --runtime geniex_llamacpp` line (`Vendor-Registries/qualcomm-ai-hub/Qwen3.5-2B.md:25`) therefore resolves to the HF file (`unsloth/Qwen3.5-2B-GGUF` q4_0, `NPU-ON-DEVICE.md:64`).

### 4.2 qairt route (AI Hub precompiled bundle → HTP)
- **What files:** a bundle is `metadata.json` plus one or more `.bin` context-binary shards, or the AI Hub `.zip` (`docs/models/supported.mdx:197,229`). Weight-sharing bundles hold the prefill (AR128) and decode (AR1) graphs in shared context binaries, e.g. `weight_sharing_model_ar128_ar1_…serialized.bin` (`QAIRT-QNN/gemma4-e2b-htp.json:69-76`; `gemma3-4b-htp.json:89-93`). Weight sharing is v73+, a single PD, and offline-prepared (`HTP - Qualcomm AI Runtime (QAIRT) SDK.md:227-236`).
- **Chip match:**
  - This phone reports `SM8750`; AI Hub id `qualcomm-snapdragon-8-elite` (`platforms.mdx:22`).
  - "Galaxy" bundles are the `SM8750-AC` alias (`platforms.mdx:30`): same v79 HTP.
  - X Elite (v73) and X2 Elite (v81) bundles are another HTP arch. QAIRT warns that loading such a context binary "may give indeterminate result" (`HTP - … SDK.md:96`). Per the operator rule they are still test candidates; record err `5005` and similar loader errors (audit:142).
- **Getting the exact-chip bundle (phone only):**
  - (a) **Qualcomm's own path:** `geniex-bench` resolves model-manager ids and downloads with `--chipset` and `--mm-data-dir` (`test_bench.py:114-118`), e.g. `-m qualcomm/qwen3_4b_instruct_2507 --chipset SM8750 --mm-data-dir /data/local/tmp/geniex-cache`. QDC benches exactly `qualcomm/qwen3_4b` and `qualcomm/qwen3_4b_instruct_2507` (`bench-models.json:26-27`). Android needs an explicit chipset (`platforms.mdx:40`; `troubleshooting.mdx:169-171`).
  - (b) **The CLI in the Debian proot:** `proot-distro login debian -- /root/venvs/qai-hub/bin/qai-hub-models fetch Qwen3-1.7B --runtime geniex_qairt --precision w4a16 --chipset qualcomm-snapdragon-8-elite`. The filter is at `args.py:103-108` and the file is named `{model}-{runtime}-{precision}-{chipset}.zip` (`fetch.py:47-49`). Card commands: `Vendor-Registries/qualcomm-ai-hub/Qwen3-1.7B.md:25`, `SmolLM2-1.7B-Instruct.md:25`, `Intern3.5-VL-4B.md:25`. Note: the venv holds only `qai_hub_models_cli 0.63.0`, not the full `qai-hub-models`, so **export** (`ai-hub-apps/tutorials/geniex/export.md:74`, `--chipset qualcomm-snapdragon-8-elite --target-runtime geniex_qairt`) is not available there.
- **Runtime:**
  - GenieX's bundled QAIRT in `lib/qairt/htp-files` (`libQnnHtp.so`, `libQnnHtpV79Stub.so`, `libQnnHtpV79Skel.so`, `libQnnHtpPrepare.so`, `libQnnSystem.so`; listed today for v0.7.1).
  - Override with `--qairt-lib DIR` (`v0.9.3:sdk/benchmark/options.c:60-62`) or `GENIEX_QAIRT_LIB`. The override accepts an SDK root or a flat folder (`notes/run.md:156-193`).
  - The vault has a flat QAIRT **2.48.0** (`QAIRT-QNN/sdk.yaml:23`) with V79 Stub and Skel. The plugin's floor is QNN API 2.27, and provider queries were checked against 2.48.40 (`notes/run.md:209-213`).
  - Confirm with `--log info`: expect `Overriding the bundled QAIRT runtime from <source>: … (host libs: <dir>)` (`notes/run.md:196-205`).
  - Only one QNN runtime can be used per process (`notes/run.md:229-234`).
- **Config:**
  - GenieX generates `geniex.json` on import; you do not author it (`supported.mdx:229`). "QAIRT models need a `geniex.json`" (`notes/run.md:152`).
  - Load parameters: `runtime_id="qairt"`, `nCtx=0`, `nGpuLayers=0`; anything else is rejected with `PARAM_NOT_SUPPORTED` (`platforms.mdx:119`; `docs/run/android/api-reference.mdx:384`).
  - Multicore follows the bundle's `htp_backend_ext_config.json` `devices[].cores`. Most mobile SoCs expose one NSP core (`notes/run.md:240-261`).
  - The power mode overrides the bundle json (`notes/run.md:91-96`).
- **Command (adb shell, pkg staged as in §3):** `./bin/geniex-bench --plugin qairt --device npu -m <bundle dir | model id> --chipset SM8750 --mm-data-dir /data/local/tmp/geniex-cache`. Prefill tokens are reported padded to multiples of 128 (`docs/tutorials/benchmarking.mdx:175`).
- **Raw QAIRT cross-check (optional, deprecated stack).** AI Hub cards say "Genie support will be deprecated soon" (`Vendor-Registries/qualcomm-ai-hub/SmolLM2-1.7B-Instruct-github-v0.63.0.md:34`; `Llama-3.2-3B-Instruct-SSD.md:36`).
  - Push `genie-t2t-run`, `libGenie.so`, `libQnnHtp.so`, `libQnnSystem.so`, `libQnnHtpPrepare.so`, `libQnnHtpNetRunExtensions.so`, `libQnnHtpV79Stub.so` and `libQnnHtpV79Skel.so` from vault `QAIRT-QNN/` (all present, QAIRT 2.48), plus the bundle's `genie_config.json`, `htp_backend_ext_config.json`, tokenizer and `.bin`s, to one directory under `/data/local/tmp`.
  - Run: `LD_LIBRARY_PATH=<dir> ADSP_LIBRARY_PATH=<dir> ./genie-t2t-run -c genie_config.json -p "<templated prompt>"` (`no_lora.html` text 22-40; `android-qnn-net-run.sh:166-173`; `ai-hub-apps/tutorials/llm_on_genie/README.md:221-234`).
  - **Do not copy** `README.md:82-83` of that tutorial ("v73 for 8 Elite", `hexagon-v73`). This phone is v79 (`android-qnn-net-run.sh:96,166-173`; `NPU-ON-DEVICE.md:3`).
  - Genie engine defaults from Qualcomm's HTP configs: `n-threads 3`, `poll true`, `cpu-mask 0xe0`, `use-mmap true` (`QAIRT-QNN/gemma4-e2b-htp.json:28-45`; `llama2-7b-htp.json:39-54`). `cpu-mask 0xe0` means cores 5-7, which Termux cannot use (§0.5), so again run as the shell user.

### 4.3 llama_cpp route (GGUF → GenieX llama_cpp → ggml-hexagon → HTP)
- **Modes:**
  - `npu` pins `HTP0` with all layers (`platforms.mdx:95`; `notes/run.md:38,111`; `api-reference.mdx:166-173`).
  - `hybrid` leaves `device_id` empty, which is llama.cpp's per-tensor HTP+CPU scheduler. Qualcomm calls it **"The fast path on Snapdragon"** (`platforms.mdx:81,98`), "Default recommendation" (`benchmarking.mdx:156`) and the rule of thumb for throughput (`notes/run.md:109-115`).
  - `npu` is "deterministic, slower on LLMs" because the host busy-waits (`notes/run.md:38,111`).
  - Run **both** for every model, plus `cpu` as the baseline (`benchmarking.mdx:110-150,195`). The operator target is `npu`; the speed reference is whichever wins.
- **Layer and tensor split:**
  - `-ngl -1` / `ngl=999` means all layers (`notes/run.md:41-43`; bench `-ngl`, `options.c:58-59`).
  - Fallback tensors go to the CPU automatically in `hybrid` (`notes/run.md:109`).
  - Embeddings: llama.cpp's runner offers `--no-embd-offload` = `-ot "^(token_embd|output)\.weight$=CPU"` (`run.py:211,487-489`). Even Qualcomm's README example keeps a CPU model buffer: `CPU model buffer size = 225.49 MiB` next to `HTP0 … 504.26 MiB` (`README.md:172-173`). A CPU-resident `token_embd` is normal; the per-token CPU↔HTP hops in the middle layers (Qwen 3.5 `ssm_out`) are the problem.
  - On v0.9.3, check whether `ssm_out` (Q5_K) still lands on the CPU (§0.3). Use `GGML_SCHED_DEBUG=2` (env passed by `run.py:51`; suggested at `NPU-SERVE-BUILD-LOG.md:79`) or the load log's per-buffer sizes.
  - Only if it still falls back: requant `llama-quantize --pure` to Q4_0 (`NPU-ON-DEVICE.md:42`).
- **Threads:** the SDK pins 6 threads to cores [2,8) on every offloaded path (`notes/run.md:138`), mirroring llama.cpp's `-t 6` (`run.py:484-486`). Override with bench `-t N` (`options.c:57,420`). Under Termux, compare `-t 4` (cores 2-5, all allowed) against the default.
- **Large models (> ~3.5 GB per session).** A session has about a 3.5 GB virtual window (`developer.md:33-37`; `README.md:225`). Two documented options:
  1. **Single session with dynamic buffer mapping.** This is the default: the backend maps and unmaps weight buffers automatically (`README.md:221-232`; `developer.md:39-45`). No flags.
  2. **Layer split across virtual sessions on the one NPU.** Set `GGML_HEXAGON_DEVICES=N`, giving sessions `HTP0..HTP<N-1>` (`README.md:311`), or the explicit `HTP0:0,HTP0:1` (`README.md:313`). In GenieX, pass the device list: `--compute HTP0,HTP1` (`docs/run/cli/reference.mdx:76-79`; `notes/run.md:50-54`), or `--device-id HTP0,HTP1` in `geniex-bench` (`options.c:161,349`). Each session keeps its weights inside its own window, with no remapping (`README.md:234-240`). Qualcomm's example runs GPT-OSS-20B over 4 sessions with `--load-mode none -ctk q8_0 -ctv q8_0 -fa on` (`README.md:242-249`).
  - Tensor split across *physical* NPUs (`HTP0:0,HTP1:0`, `--split-mode tensor`) and row-split groups (`HTP0[0-1]`) need multiple NSP cores (`README.md:278-305`). Most mobile SoCs expose one NSP (`notes/run.md:259-261`), so check before using.
  - The operator's `D=HTP0,HTP1` (`NovAExorpus/HTP/HTP-Memory-Architecture-and-runtime-splitting.md:29`) is not the vendor variable; use the above.
- **VLMs:** the mmproj goes to its own session: `GGML_HEXAGON_DEVICES=2 … --compute HTP0 --vit-compute HTP1` (`troubleshooting.mdx:92-99`). v0.9.3 does this by default (`plugin.cpp:66-75`).

### 4.4 Routing table for what is on the phone (`ls Documents/_models`, today)
| File / bundle | Size | Route | Mode to bench | Split | Notes |
|---|---|---|---|---|---|
| `gguf/Qwen3.5-2B-Q4_0.gguf` | 1.21 G | llama_cpp | npu, hybrid, cpu | none | AI Hub asset (`NPU-ON-DEVICE.md:64`); QDC uses npu (`bench-models.json:17`); target 22.6-24.8 decode, 593-644 prefill (`NPU-ON-DEVICE.md:63`); re-check `ssm_out` placement (§0.3); try `GGML_HEXAGON_GDN_SELECT` |
| `gguf/Qwen3.5-4B-Q4_0.gguf` + `mmproj-Qwen3.5-4B-F16.gguf` (added 2026-10-23, operator's multimodal pick) | 2.58 G + 0.67 G | llama_cpp | npu, hybrid, cpu | none for weights (fits HTP0); mmproj on HTP1 (v0.9.3 default) | QDC benches it on cpu and npu (`bench-models.json:18`); no AI Hub page; same `ssm_out` / GDN checks as the 2B |
| `gguf/Qwen3.5-0.8B-Q4_0.gguf` | 0.51 G | llama_cpp | npu, hybrid, cpu | none | QDC model (`bench-models.json:11`) |
| `gguf/Qwen3.5-9B-Q4_0.gguf`, `gguf/Qwen_Qwen3.5-9B-Q4_0.gguf` | 5.38 G, 5.74 G | llama_cpp | npu, hybrid | dynamic mapping first, then `GGML_HEXAGON_DEVICES=2` + `HTP0,HTP1` | two different 9B files on disk; same-identity check not done here |
| `gguf/gemma-4-12b-it-qat-q4_0.gguf` | 6.98 G | llama_cpp | npu, hybrid | dynamic, then 2 sessions, then 3 (`HTP0,HTP1,HTP2`) once KV is added | 6.98 G ≈ 2 × 3.5 G before KV |
| `gguf/gemma-4-E4B_q4_0-it.gguf` + `mmproj-gemma-4-E4B-it.gguf` | 5.15 G + 0.99 G | llama_cpp | npu, hybrid | dynamic or 2 sessions; mmproj on HTP1 | AI Hub page, GenieX llama.cpp q4_0 on 8 Elite NPU: prefill 427, decode 12.4 tok/s (`global-documentation-vault/google-dev-docs/GEMMA 4/Gemma-4-E4B-it - Qualcomm AI Hub.md:39-48`) |
| `gguf/gemma-4-e4b-it-q4_k_m.gguf`, `gguf/gemma-4-E4B-it-IQ4_NL.gguf` | 5.34 G, 4.84 G | llama_cpp | npu, hybrid | as above | K-quant and IQ4_NL are in v0.9.3's HTP repack list (`e467e5b5:ggml-hexagon.cpp:318-323`); GenieX docs still prefer Q4_0 (`supported.mdx:321-326`) |
| `gguf/granite-4.0-h-micro-Q4_0.gguf` | 1.86 G | llama_cpp | npu, hybrid, cpu | none | QDC benches `granite-4.0-micro` Q4_0 on npu (`bench-models.json:21`); `h-micro` is a different file from that one |
| `gguf/OpenGVLab_InternVL3_5-8B-Q4_0.gguf` + mmproj f16 | 4.79 G + 0.68 G | llama_cpp | npu, hybrid | dynamic or 2 sessions, mmproj HTP1 | |
| `gguf/SmolVLM2-2.2B-Instruct-Q8_0.gguf` + mmproj | 1.93 G | llama_cpp | npu | none | QDC benches SmolVLM2 Q8_0 on npu (`bench-models.json:25`) |
| `qairt/8-elite-galaxy/{smollm2_1_7b_it, intern3_5_vl_2b, intern3_5_vl_4b}…zip` | 1.0 / 2.4 / 3.7 G | qairt | npu | baked in | v79, same arch; import via `-m` (unpacked dir) |
| `qairt/x-elite/*`, `qairt/x2-elite/*` | | qairt | npu | baked in | other HTP arch: test-load only, results "indeterminate" (`HTP - … SDK.md:96`) |
| **Missing:** exact `qualcomm-snapdragon-8-elite` text LLM, e.g. `qwen3_4b_instruct_2507` (`api-reference.mdx:348`) or Qwen3-1.7B w4a16 | | qairt | npu | baked in | fetch per §4.2 (needs operator approval: download) |

### 4.5 LiteRT / LiteRT-LM with the Qualcomm accelerator (optional fourth route)
- LiteRT supports QNN through the CompiledModel API, both AOT and on-device (JIT), on SM8750 (`global-documentation-vault/qairt-docs/#QAIRT/Qualcomm NPU (AI Engine Direct) with LiteRT … .md:9-10,34-36`).
- **LLMs (LiteRT-LM):**
  - Model: a `.litertlm` per SoC (Gemma3-1B SM8750, 4-bit, ctx 1280).
  - Build `litert_lm_main` and `@litert//litert/vendors/qualcomm/dispatch:dispatch_api_so` with Bazel and the NDK.
  - Push the QAIRT `libQnnHtp*Stub`, `libQnnHtp`, `libQnnSystem`, `libQnnHtpPrepare` and `hexagon-*/unsigned/libQnnHtp*Skel` to `/data/local/tmp`.
  - Run `LD_LIBRARY_PATH=$DEVICE_FOLDER ADSP_LIBRARY_PATH=$DEVICE_FOLDER litert_lm_main --backend=npu --model_path=…` (`Vendor-Registries/google-gemma-litert/Run LLMs using LiteRT-LM … .mht`, extracted text 332-450).
- The binaries need a Bazel/NDK build, which runs in CI like the GenieX APK did (audit:241). The vault's QAIRT 2.48 libs cover the push step.

### 4.6 llama-server with Hexagon (deferred)
- Qualcomm's build is `scripts/snapdragon/build.py --target adb` in `ghcr.io/snapdragon-toolchain/arm64-android:v0.8` (`README.md:9,27-30`; now v0.8, the audit saw v0.7). Do it in the fork's GitHub Actions and download the artifact to the phone.
- Run it as in §3, with `-ngl 99 -fa on -ub 1024 -t 6` and `GGML_HEXAGON_OPPOLL=1` (`run.py:223,469-486`).
- Lower priority: `npu-serve` over GenieX v0.9.3 already ships llama.cpp `e467e5b5`.

---

## 5. NPU-ON-DEVICE.md line 8: exact replacement (proposed, not applied)

**Current line 8** (`~/.claude/NPU-ON-DEVICE.md:8`):
> - `npu` is GenieX's default and the target here: 100% on the HTP. `hybrid` (HTP+CPU per-tensor split) is not the default; don't present it as the fast path. (`platforms.mdx:95`)

**New line 8:**
> - `npu` is GenieX's default (`platforms.mdx:78,95`) and is the operator's target here: all layers pinned to `HTP0`. Qualcomm's own docs call `hybrid` (llama.cpp's per-tensor HTP+CPU scheduler) "the fast path on Snapdragon" and the default throughput recommendation (`platforms.mdx:81,98`; `tutorials/benchmarking.mdx:156`; `resources/faq.mdx:40`; `notes/run.md:109-115`), and call `npu` "slower on LLMs" because the host thread busy-waits on the HTP (`notes/run.md:38,111`). Bench `npu`, `hybrid` and `cpu` on every model and report all three; this phone's best decode so far is `hybrid` (20.5 tok/s, table below). Qualcomm's QDC bench runs Qwen3.5-2B as `npu` (`sdk/benchmark/qdc/bench-models.json:17`).

**Other corrections owed in the same file** (listed only; the operator approves each one separately):
- `:20`: `GGML_HEX_VERBOSE` → `GGML_HEXAGON_VERBOSE` (`llama.cpp README.md:358`; `e467e5b5:ggml-hexagon.cpp:9975`).
- `:31` and `:62`: the v0.7.1 "2.7 tok/s" was a 7-token EOS run, not `0x80000414` (audit:166-170). Fixed upstream by `e36f6ab0`, which is in v0.9.3.
- `:37`: `Documents/Models/` → `Documents/_models/gguf/`.
- `:39`: `Vendor-Registries/GOOGLE _DEV/` → `Vendor-Registries/google-gemma-litert/` and `global-documentation-vault/qairt-docs/#QAIRT/`.
- `:52,55`: the `llm-wiki/` contents moved to `_Merovingians_Keep/NovAExorpus-nested-mirror/llm-wiki/`.
- `:64`: `qai-hub-models fetch` does not serve `geniex_llamacpp` assets (`fetch.py:170-187`).
- `:15` (skel symlink): still required on v0.9.3; drop it from v0.9.4 on (§1.5).

---

## 6. Ordered checklist (each step: command → expected result)

Steps marked **(approval)** change state (download, install, settings) and need the operator's explicit go-ahead per the standing rules.

1. **Fork synced and release confirmed.**
   - `gh repo sync c10vis-poem/GenieX && git -C ~/repos/GenieX pull`
   - `gh release list -R qualcomm/GenieX -L 3`. Expected: `v0.9.3  Latest  … 2026-10-19`. If a newer non-draft release appears, re-plan with that tag, re-checking `550977d0` ancestry and the `third-party/llama.cpp` pin.
   - Operator decides the upstream-binary question (§0.8).
2. **Download (approval).**
   - `gh release download v0.9.3 -R qualcomm/GenieX -p 'geniex-bench-android-arm64-v0.9.3.tar.gz*' -D ~/tools/dl-geniex`
   - Verify: `cd ~/tools/dl-geniex && sha256sum -c geniex-bench-android-arm64-v0.9.3.tar.gz.sha256`. Expected: `…: OK`.
3. **Extract side by side (approval).**
   - `tar -xzf ~/tools/dl-geniex/geniex-bench-android-arm64-v0.9.3.tar.gz -C ~/tools/`
   - Verify: `ls ~/tools/geniex-bench-android-arm64-v0.9.3/lib/llama_cpp/libggml-htp-v79.so ~/tools/geniex-bench-android-arm64-v0.9.3/lib/qairt/htp-files/libQnnHtpV79Skel.so`. Both should exist; `~/tools/geniex-bench` and `…-v0.7.1` are untouched.
4. **Skel symlink.**
   - `ln -sf llama_cpp/libggml-htp-v79.so ~/tools/geniex-bench-android-arm64-v0.9.3/lib/libggml-htp-v79.so`
   - Verify: `ls -l …/lib/libggml-htp-v79.so` shows `-> llama_cpp/libggml-htp-v79.so`.
5. **Help runs.**
   - `cd ~/tools/geniex-bench-android-arm64-v0.9.3 && LD_LIBRARY_PATH=lib:lib/llama_cpp:lib/qairt:/vendor/lib64 GENIEX_PLUGIN_PATH=lib bin/geniex-bench --help`
   - Expected: the usage text, including `--device-id ID` and `--qairt-lib DIR` (`options.c:60-62,161`).
6. **Device state recorded** (§2.1 commands).
   - Expected for a valid run: `scaling_max_freq == cpuinfo_max_freq` on policy0 and policy6, plugged in, zones below 45 °C.
   - If it is not met, record the values and label every result "capped".
7. **Termux NPU proof run** (short, verbose): same env as step 5 plus `GGML_HEXAGON_VERBOSE=1`, then `bin/geniex-bench --plugin llama_cpp --device npu -m ~/storage/shared/Documents/_models/gguf/Qwen3.5-2B-Q4_0.gguf -r 1 --warmup 0 -n 16 --log debug`. Expected lines:
   - `ggml-hex: … allocating new registry : ndev 2`: two sessions by v0.9.3 default (`plugin.cpp:69-75`; line format `README.md:147`).
   - `ggml-hex: Hexagon Arch version v79` (`README.md:148`).
   - `ggml-hex: new session: HTP0 : session-id 0 domain-id 3 uri file:///libggml-htp-v79.so?…` (`README.md:168`).
   - `ggml-hex: HTP0 power mode: burst` (`e467e5b5:ggml-hexagon.cpp:5000`).
   - `load_tensors: offloaded 25/25 layers` and an `HTP0 model buffer size` line (`README.md:172-173`; 25/25 seen before, `NPU-ON-DEVICE.md:23`).
   - Per-op `ggml-hex: HTP0 matmul : …` lines (`README.md:362-367`). Check for `ssm_out` matmuls now on `HTP0` (§0.3).
   - Expected under Termux: an affinity failure, because cores 6-7 are not allowed (§0.5).
   - If `Hexagon Arch` is missing, the run fell back to the CPU (`troubleshooting.mdx:112-113`).
   - If you see `0x80000406`, read `logcat -d | grep -i adsprpc` (`NPU-ON-DEVICE.md:24`).
8. **Termux timed A/B baseline (vendor protocol).** `bin/geniex-bench --plugin llama_cpp --device {npu|hybrid|cpu} -m <2B>` at the defaults: 512 random tokens, 128 generated, 1 warmup + 5 runs, median (`benchmarking.mdx:108`).
   - Expected per line: `[ok  ] cell  plugin=llama_cpp  device=npu  ngl=999  ttft=…  prefill=…tps  decode=…tps  gen=128 tok` (`benchmarking.mdx:90`).
   - `gen=128` is required. Runs never stop at EOS on v0.9.3 (`benchmarking.mdx:108`; `e36f6ab0` is in v0.9.3).
   - Repeat `npu` with `GGML_HEXAGON_OPPOLL=1` and with `-t 4`.
9. **Wireless debugging paired (approval: settings change).** Follow §3 steps 1-6. Expected: `adb devices` lists `127.0.0.1:<port>	device`, `id` shows `uid=2000(shell)`, context `u:r:shell:s0`. Record `Cpus_allowed_list`.
10. **Stage in `/data/local/tmp/pkg-geniex`** (§3.7). Verify with `adb shell ls -l /data/local/tmp/pkg-geniex/lib/libggml-htp-v79.so /data/local/tmp/pkg-geniex/modelfiles/llama_cpp/`.
11. **Shell-user A/B (same binary, same model, same protocol as step 8).** Use the §3.8 command for `--device npu`, then `hybrid` and `cpu`. Optionally add the QDC form `-r 3 -c 512|1024|4096 --chipset SM8750` (`test_bench.py:114-118`).
    - Expected: the same `[ok ]` lines with `gen=128 tok`.
    - Look for `threadpool tuned for offload: 6 threads pinned to cores [2, 8), strict, poll=1000` with **no** affinity error (`notes/run.md:138`), and no `FASTRPC_GET_DOMAINS query failed`.
    - `adb logcat -d | grep -i -E 'adsprpc|0x8000041'` shows whether `0x80000414` persists as the shell user.
    - Compare against Qualcomm's numbers for this file: decode 22.6-24.8, prefill 593-644 (`NPU-ON-DEVICE.md:63`). Compare only if step 6 showed no cap.
12. **K-quant placement check on v0.9.3.** Run as in step 11 with `GGML_SCHED_DEBUG=2` (or `GGML_HEXAGON_VERBOSE=1`, short). Expected if §0.3 holds: the `ssm_out` matmuls run on `HTP0` and the CPU model buffer shrinks from 398 MiB (`NPU-SERVE-BUILD-LOG.md:16`) toward the embeddings-only size. Then A/B `GGML_HEXAGON_GDN_SELECT=2|1`.
13. **qairt route.**
    - First, the on-disk galaxy bundle (unpacked) via `./bin/geniex-bench --plugin qairt --device npu -m <dir>`.
    - Then **(approval: download)** the exact-chip text LLM, `-m qualcomm/qwen3_4b_instruct_2507 --chipset SM8750 --mm-data-dir /data/local/tmp/geniex-cache` (§4.2).
    - Expected: `[ok ] cell plugin=qairt device=npu …`, with prefill over padded tokens (`benchmarking.mdx:175`).
    - With `--qairt-lib`, also expect `--log info` to show `Overriding the bundled QAIRT runtime … (host libs: …)` (`notes/run.md:200`).
    - Then test-load the X-series variants and record errors.
14. **Large model split.**
    - Qwen3.5-9B Q4_0: (a) default (dynamic mapping, `--device npu`); (b) `GGML_HEXAGON_DEVICES=2 … --device npu --device-id HTP0,HTP1`.
    - Expected: (b) shows two `HTP0`/`HTP1` model buffer lines, each below about 3.5 GB (`README.md:260-265` format), and offloaded N/N.
    - Then gemma-4-12B with 2, then 3 sessions.
15. **Port to `npu-serve`** after steps 11-14 pick the winner: rebuild the shim against `geniex-v0.9.3.h` (§1.7) and fix the model paths.
    - Verify: `npu-serve` starts and a `curl 127.0.0.1:18181/v1/chat/completions` round-trip returns text.
    - The log shows the step-7 proof lines and `power mode: burst`.
    - Decide with the operator whether the server runs under Termux or is launched as the shell user via `adb shell` (cpuset, SELinux).
16. **Docs.** The operator approves §5 and each listed correction. Afterwards the operator decides on removing v0.3.14 and v0.7.1.

---

## docs_read

Read in full unless marked.
- `~/.claude/NPU-ON-DEVICE.md` (1-65): baseline facts, line 8 under review, stale paths.
- `~/.claude/session-work/2026-10-23/npu-audit-report.md` (1-256): audit findings this plan builds on.
- **GenieX fork `~/repos/GenieX` @ `692086f0`:**
  - `docs/en/get-started/platforms.mdx` (1-123): chip ids, runtime choice, defaults, npu/hybrid table, qairt constraints.
  - `docs/en/resources/troubleshooting.mdx` (1-201): VLM HTP1, libcdsprpc, silent fallback and the VERBOSE typo, Android chipset, CPU-only AAR.
  - `docs/en/run/cli/reference.mdx` (40-285): `--compute HTP0..` with `GGML_HEXAGON_NDEV`, power mode, bench flags.
  - `docs/en/tutorials/benchmarking.mdx` (1-258): protocol, output format, hybrid recommendation, qairt padding.
  - `docs/en/resources/faq.mdx` (grep): hybrid line 40, QDC.
  - `docs/en/models/supported.mdx` (180-240, 300-343): Android LOCALFS import, `geniex.json` generation, quant table.
  - `docs/en/run/android/install.mdx` (8-75): app/Maven path, sample app.
  - `docs/en/run/android/api-reference.mdx` (grep): chipset, `nGpuLayers`, qairt constraints, Qwen3-4B.
  - `notes/run.md` (1-393): compute aliases, power mode, npu vs hybrid paths, threadpool, QAIRT override, multicore.
  - `notes/bench.md` (1-261): S3 URLs, QDC protocol.
  - `notes/build.md` (150-257): Android deploy via `/data/local/tmp`.
  - `notes/release.md` (1-20, 83-110, grep): asset names, sha256 sidecars, S3 table.
  - `sdk/benchmark/qdc/bench-models.json` (1-29): QDC model and compute list.
  - `v0.9.3:sdk/plugins/llama_cpp/src/plugin.cpp` (60-130): DEVICES=2 default, MBUF, Android ADSP path.
  - `v0.9.3:sdk/plugins/llama_cpp/CMakeLists.txt` (60-70): skels in `lib/llama_cpp`.
  - `v0.9.3:sdk/benchmark/options.c` (40-70, 150-166, 340-360, grep): bench flags.
  - `v0.9.3:sdk/benchmark/benchmark.c` (80-100): device resolve.
  - `v0.9.3:sdk/benchmark/qdc/tests/test_bench.py` (20-60, 88-122) and `tests/utils.py` (grep): Qualcomm's Android env and command.
  - `.github/workflows/_build-sdk.yml` (grep): Android build matrix.
  - commit `550977d0` (full diff).
  - `git diff v0.7.1 v0.9.3 -- sdk/include/geniex.h` (filtered): ABI changes.
  - `gh release list` / `view` and `git ls-remote --tags`: release state.
- **llama.cpp `~/llama.cpp` `origin/master` @ `4231b23dc`:**
  - `docs/backend/snapdragon/README.md` (1-393): build, install, run, log lines, multi-device modes, env vars.
  - `docs/backend/snapdragon/developer.md` (1-58, 171-201, 337-341; headings of the rest): libs, 3.5 GB window, dynamic mapping, K-quant tiles.
  - `scripts/snapdragon/run.py` (1-70, 100-135, 205-245, 336-385, 440-520): adb env, defaults, flags.
  - `e467e5b5:ggml/src/ggml-hexagon/ggml-hexagon.cpp` (315-340, 7030-7060, getenv block 9975-9998, 10077, grep 104-166, 5000): pinned-version capabilities and defaults.
  - `94256114` (grep): no K-quants.
- **Vault `NovAExorpus/QAIRT-QNN/`** (flat; 2,257 files inventoried):
  - `android.html`, `basic.html`, `no_lora.html`, `lora.html`, `lade.html`, `spd.html`, `ssd-q1.html`, `genai.html`, `preparation (1).html` (text extracted, full): Genie Android recipe.
  - `android-qnn-net-run.sh` (92-101, 107-236): v79 lib set, ADSP/LD paths.
  - `gemma4-e2b-htp.json` (1-90): Genie HTP engine, weight-sharing ctx bins.
  - `llama2-7b-htp.json`, `llama2-7b-htp-multistream.json`, `llama3-8b-htp.json`, `gemma3-4b-htp.json`, `llama3-3b-htp-long-context.json` (grep of engine fields).
  - `executor-config.json`, `config (1).json`, `config (2).json` (heads): backend file sets.
  - `htp.json`, `htp_v2.json`, `HtpConfigFile.json`, `qwen3-4b-instruct-2507.json` (heads): judged op tables and composer config.
  - `program_listing_file_include_QNN_HTP_QnnHtpContext.h.html`, `…QnnHtpDevice.h.html` (grep): weight sharing and multi-context options, perf infra.
  - `sdk.yaml` (1-33): QAIRT 2.48.0.
  - `README.md`, `README (1).md`, `README (7).txt` (heads): simulator, Python API, SNPE samples; not relevant.
  - `file` on `genie-t2t-run`, `libQnnHtpV79Skel.so`, `libQnnHtpV79Stub.so`.
- **Vault `02_wiki_md/vendors/qualcomm/`** (129 files; term-hit ranking over all):
  - `GENIE_README.md` (1-24): Genie scope.
  - `backend.md` (grep and sample): QAIRT nav plus QairtBackend C++ API, no setup.
  - `README_master.md` (head): operator planning.
  - `android.md` (head): a CI yaml.
  - grep across all for wireless-debugging terms.
- **Vault `HTP/`:**
  - `NPU-RUNTIME-PATHS.md` (1-60): operator routing notes.
  - `snapdragon-npu-partitioner.md (1).txt` (1-38): `D=` heuristics.
  - `HTP-Memory-Architecture-and-runtime-splitting.md` (grep): the `D=HTP0,HTP1` non-vendor var.
  - `runtime_pipeline_server.py.txt` (head): daemon code, not relevant.
- **Vault `Vendor-Registries/`** (inventory of all subfolders):
  - `qualcomm-ai-hub/Qwen3.5-2B.md` (1-66): GGUF route.
  - `GenieX-Chat-App/README (5).md` (1-60): app path.
  - grep of all model cards: runtimes per model and the Genie deprecation.
  - `Llama-3.2-3B-Instruct-SSD.md` (30-60) and `SmolLM2-…v0.63.0.md` (28-40): deprecation, export needs.
  - `google-gemma-litert/Run LLMs using LiteRT-LM….mht` (text 236-470): LiteRT-LM QNN recipe.
  - `LiteRT for Android….mht`, `Installing LiteRT CLI….mht`, `litert-samples…npu_android….mht` (grep): nav only beyond the CompiledModel snippet.
- **Vault `global-documentation-vault/`:**
  - `qairt-docs/#QAIRT/HTP - Qualcomm AI Runtime (QAIRT) SDK.md` (headings; 86-96, 214-236, 472-486, 676-692; grep): arch-matched context binaries, weight sharing limits, perf infra, HMX vote rule.
  - `qairt-docs/#QAIRT/Qualcomm NPU (AI Engine Direct) with LiteRT….md` (1-56): SM8750 support, AOT and JIT.
  - `qairt-docs/#QAIRT/NPU acceleration with LiteRT….md` (grep): AOT and JIT.
  - `qairt-docs/Research.NPU/Snapdragon NPU LLM.md` (grep, 64-78): community ExecuTorch route, cdsprpc domain 3; not vendor.
  - `google-dev-docs/GEMMA 4/Gemma-4-E4B-it - Qualcomm AI Hub.md` (15-85): Qualcomm's 8 Elite NPU numbers for E4B Q4_0.
- **Vault docs:**
  - `docs/NPU-FINDINGS-2026-10-02.md`, `docs/NPU-SERVE-BUILD-LOG.md`, `docs/NPU-BENCHMARKS.md` (grep): prior state, protocol, open items.
  - `LAPTOP-TRICK.md` (1-80): operator's loopback-adb background.
  - `01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md` (94-98): pair, connect, UID 2000.
- **`~/repos/Aesop-Xi/`:** `HTP/` (2 files: the partitioner note, compared by `diff -q` to the vault copy, which differs; the memory-architecture txt is the same topic as the vault md); `docs/NPU-ON-DEVICE.md` and `NPU-SERVE-BUILD-LOG.md` (listed, same names as the files read).
- **`~/repos/ai-hub-apps` @ `7fbeb9b`:**
  - `tutorials/llm_on_genie/README.md` (1-20, 66-122, 218-250, grep): Genie Android run; the v73 typo.
  - `tutorials/geniex/README.md` (20-70): `pull --local-path`.
  - `tutorials/geniex/export.md` (grep): export chipsets.
  - `geniex_chat_android/README.md` (via the vault copy `Vendor-Registries/qualcomm-ai-hub/GenieX-Chat-App/README (5).md`).
- **Debian proot venv `$PREFIX/var/lib/proot-distro/containers/debian/rootfs/root/venvs/qai-hub`:**
  - site-packages listing: only `qai_hub_models_cli 0.63.0`.
  - `qai_hub_models_cli/args.py` (84-120): `--chipset`, `--runtime`.
  - `fetch.py` (20-100, 168-192): asset naming; `geniex_llamacpp` not fetchable.
- **Live read-only probes:** cpufreq (all policy attrs), `/proc/self/{status,cgroup,attr/current}`, thermal zones, `termux-battery-status`, `settings` and `dumpsys` (failed as shown), `/dev` rpc nodes, `/data/local/tmp` perms, `df -h`, `adb version`, `ls ~/tools/*`, `sha256sum -c` on the v0.7.1 sidecar, `ls Documents/_models`.

## Inventoried, judged not relevant (and why)
- `QAIRT-QNN/`: 505 `.so`, 126 `.dll`, 68 `.pyd`, 47 `.lib` and 151 `.js` (SDK binaries and html assets); 129 of the 138 html are API reference pages (SNPE Java classes, `QnnHtpProfile`/`QnnOpDef` defines, `GenieDialog`/`GenieAccuracy` function pages, SNPE `DlSystem` headers) with no setup steps; `.trashed-*` images; `linux.html`, `windows.html`, `gpu (1).html` (other targets); `*-qnn-net-run.sh` for linux, oe-linux and ubuntu.
- `02_wiki_md/vendors/qualcomm/`: about 125 of 129 files are operator planning docs, grill sessions, OmniRoute `ENVIRONMENT.md` and AESOP specs, filed under "qualcomm" but holding no vendor setup text.
- `Vendor-Registries/`: `agents-gateways`, `huggingface-smolvlm`, `internvl`, `opencode`, `piper`, `skills-references`, `guides`; `qualcomm-ai-hub/speech/*` (STT/TTS, outside LLM scope); `google-gemma-litert` Gemma overviews, SFT guide, RAG notebook, `model.safetensors`, gcloud tarball; `qwen/*` (model cards and blog, no runtime setup).
- `global-documentation-vault/`: `llama-docs` (GitHub page captures of llama.cpp repos, superseded by `~/llama.cpp origin/master`); `unsloth-docs`, `qwen-models`, `fragmented-qat`, `reference`, `research`, `reverse-engneering`, `readme-notes` (listed, titles not NPU setup); `google-dev-docs` Antigravity, Gemini Enterprise and GitHub-Actions Android build (could serve CI builds, not NPU).
- `llm-wiki/`: now 2 non-NPU files.
- `_personal/le_Grand_archive/` (13,324 files): `_duplicate-docs/` mirrors `_Merovingians_Keep/Zip`, and its NPU documents are copies of the vault `global-documentation-vault/qairt-docs` files read above (same names and paths); `_reciepts`, `_vault-unreviewed-2026-10-09` (audit, clean_md) not opened.
- `GenieX docs/cn/*` (Chinese duplicates of `docs/en`), `docs/en/run/python/*`, `run/linux/install.mdx`, `run/cli/install.mdx`, `run/cli/local-server.mdx`, `tutorials/audio-input.mdx` and `speculative-decoding-mtp.mdx`: Windows, Linux and Python paths; not read this pass.
- `llama.cpp docs/backend/snapdragon/linux.md`, `windows.md`, `CMakeUserPresets.json`: other targets and build presets.

## Not read / open
- `0x80000414` root cause (llama.cpp #22352 / PR #22334) was not re-verified; no saved logcat contains it (audit:212).
- How `geniex-bench -m <unpacked qairt dir>` behaves without a `geniex.json` on Android was not checked in source. Step 13 tests it.
- The contents of the v0.9.3 Android tarball are inferred from the v0.7.1 layout and v0.9.3 CMake. Step 3 verifies them.
- Android Settings wording for Wireless debugging, `dumpsys`/`settings` behaviour as the shell user, and the shell user's cpuset: no on-device doc. §2.2, §3 and step 9 verify them.
