# Voice engine APK: build brief and feasibility (item 22)

Date: 2026-10-23. Status: brief only, nothing built, installed, or committed.

Operator ask (quoted): "this needs to be built not just for Termux ... it needs to get built as the APK inside the app, and these APKs are Jetpack Compose Kotlin apps ... It needs to be built in modern Material format and actually look like a consumer-grade application."

Plain restatement: a native Android app (Kotlin, Jetpack Compose, Material 3) that runs the voice engine on the phone itself, and also exposes that engine as an API other clients (Chrome, other apps) can call over a local socket.

## Sources read this session

Read: `~/repos/Aesop-Xi/voice-engine/scripts/live_voice_loop.py`, `run_live.sh`; `~/repos/Aesop-Xi/ARCHITECTURE.md` (middle section truncated on display); `~/.claude/skills/aesop-voice-pipeline/SKILL.md`; memories `project_horizons_rebuild_plan.md`, `project_android_local_desktop_next_session.md`; `~/repos/raw-databank/horizons-ui-full/` (`gradle/libs.versions.toml`, `horizons/build.gradle.kts`, `.github/workflows/build-apk.yml` first 80 lines, `ui/theme/HorizonsTheme.kt`, its `CLAUDE.md`, screenshot `Screenshot_20260721-223641_Horizons.png`, file list, sherpa imports); `~/repos/CloviX-AEyre/AGENTS.md`, `RESUME.md`, `docs/VOICE-EXTRACTION-PLAN.md`; `~/repos/NovAExopia/AGENTS.md`. Web: the developer.android.com pages cited below.

Not read: the rest of `horizons-ui-full` UI code (HomeGrid.kt etc.), `ai-hub-apps/geniex_chat_android`, `Novus-WhisperKitAndroid`, `NvAEx-DroidDesk`, Æsc repo, vault NAMING-CANON.md / 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md, sherpa-onnx Kotlin API page (the Android index page did not list classes).

## 1. What exists

**Voice engine today** (`Aesop-Xi/voice-engine/scripts/live_voice_loop.py`): Python, sherpa-onnx, runs inside a Debian proot with PulseAudio bridged from Termux. Silero VAD (512-sample windows, threshold 0.5, min silence 500 ms, max speech 30 s, 16 kHz mono), Moonshine base-en-int8 STT, Kokoro multi-lang v1.0 TTS. The "LLM" is a stub (`response = f"You said: {text}"`). No HTTP/WebSocket server. There is no `VoiceEngine` class: the only class is `LiveVoiceLoop`; the skill's line 77 refers to a "VoiceEngine" that was never written. Only `--demo` was verified; the live mic loop was never verified end to end (skill and Æyre RESUME both say so). Known limit: Moonshine base int8 silently returns empty past about 10 s of audio.

**Prior Compose APK** (`raw-databank/horizons-ui-full`, package `com.horizons`, last commit 94c3abf 2026-09-15): already Compose + `material3`, Compose BOM `2024.12.01`, AGP 8.8.0, Kotlin 2.1.0, minSdk 31, compileSdk 35, arm64-v8a only. It already contains on-device voice parts: sherpa-onnx 1.13.2 AAR (downloaded by CI), `SileroVadDetector`, `MoonshineSttEngine` (`OfflineRecognizer` + `OfflineMoonshineModelConfig`), `KokoroModelManager`/`SherpaOnnxTtsClient` (`OfflineTts` + `OfflineTtsKokoroModelConfig`), `AudioRecorder` (`AudioRecord`, `VOICE_RECOGNITION` source), `HorizonsTtsService`, `HorizonsVoiceInteractionService`. About 1,284 lines across stt/voice/audio. Its own CLAUDE.md: voice classes exist but "not reachable from the app"; voice runs in-process on the sherpa AAR, "NEVER on the NPU". CI (`build-apk.yml`) builds on ubuntu-latest with JDK 17, `android-actions/setup-android@v3`, and publishes a `debug-<branch>` GitHub Release per push.

**Why it looked dated** (from the screenshot and theme file): `HorizonsTheme.kt` is a 26-line object of hardcoded hex colors, with no `ColorScheme`, no `Typography`, no `Shapes`, and no dynamic color. Fonts were 8 to 11 sp app-wide (floor raised to 12 sp only on an unmerged PR). The home screen is a hand-drawn neon tile hub with a leetspeak title, glow orbs, and custom backdrop art (`HomeGrid.kt`, 1,394 lines) instead of standard M3 components. Every panel hardcodes its own sizes. It used M3 as a dependency but not as a design system.

**Repo already set up for this**: `CloviX-AEyre` (repo name `novus-aeyre`, canon name Æyre) is "the voice and vision daemon layer", one of the 3 APKs, with stub dirs (`voice-ast-stack/`, `stt_models/`, `tts_models/`, `screen-vision/`) and `docs/VOICE-EXTRACTION-PLAN.md`, which already says "This is a rewrite, not a port" and gives a build order. No Kotlin code yet.

## 2. Build tooling on this phone (probed, nothing installed)

| Tool | State |
|---|---|
| `java`/`javac` | present: openjdk 21.0.13 (also openjdk-17 17.0.21 installed) |
| `aapt2` | present: Termux package 16.0.0.4 (aarch64) |
| `android-tools` (adb) | present: 37.0.0p1 |
| `gradle` | MISSING |
| `sdkmanager` / cmdline-tools / platforms / build-tools | MISSING; `ANDROID_HOME` unset |
| `d8`, `kotlinc`, `apksigner` | MISSING |
| `gh` | authenticated as c10vis-poem |

Local builds are possible on aarch64 Termux in principle (Gradle wrapper + a hand-assembled SDK + `android.aapt2FromMavenOverride` pointing at Termux's `aapt2`, because Google's SDK ships x86_64 build-tools only), but that is fragile and slow with Compose/Kotlin compile on a phone. **Recommendation: build in GitHub Actions** (the prior repo already proved this path), sideload the artifact from the Release with `adb install` or the browser. Keep local Termux for `adb`, logcat, and running the APK's API tests (curl/websocat against the phone).

## 3. Which APK hosts voice

The 3-APK plan: Terminal (Æsc, first), Media "daemon" (Æyre: screen vision + voice), UI shell (Horizons-Ui, last). Voice belongs in **Æyre, the Media APK**. Two layers:

- `:voice-core` (Android library module): the engine (audio I/O, VAD, STT, TTS, pipeline) with no UI. Designed so the Terminal and UI-shell APKs can either call Æyre's API or, later, link the module directly.
- `:app` (Æyre application): the Compose UI plus the foreground service that hosts the engine and the local API.

Other APKs talk to Æyre over its local API, not by sharing a process. This matches the stack map in `NovAExopia/AGENTS.md` (Æyre under NovÆxopia) and keeps Horizons-Ui independent of Æyre, as `CloviX-AEyre/AGENTS.md` requires.

## 4. Architecture

**On-device inference in-app, not a call to a local service.** Use the sherpa-onnx Android AAR (prior app used 1.13.2 from the k2-fsa GitHub release; pin the current release when building) for Silero VAD, Moonshine STT, Kokoro TTS. It is the same engine the Python loop uses, so thresholds and model files carry over. ONNX Runtime Mobile directly would mean rewriting the pre/post-processing sherpa already does; no reason to. CPU only: the earlier decision is that voice stays off the NPU because the action and query models share it.

STT choice to settle in M2: Moonshine v2 streaming (`sherpa-onnx-moonshine-tiny-en-quantized-2026-02-27`, named in the skill as the fix for the 10 s ceiling) versus keeping base-en-int8 with VAD segments capped under 9.5 s. Models live in an app-specific folder loaded by absolute path, not downloaded by the APK (existing residency rule); only Silero VAD (~2 MB) ships in assets.

**Pipeline** (Kotlin coroutines + Flow): `AudioRecord` (16 kHz mono float, `VOICE_RECOGNITION`) → VAD → segment queue → STT → `transcript` events → reply hook (stub "You said:" first, then a pluggable LLM client; route through OmniRoute later) → TTS → `AudioTrack`. Barge-in: stop playback when VAD fires during TTS.

**Hosting**: a foreground service of type `microphone` (manifest `android:foregroundServiceType="microphone"`, `FOREGROUND_SERVICE_MICROPHONE` permission, runtime `RECORD_AUDIO`, `startForeground(..., FOREGROUND_SERVICE_TYPE_MICROPHONE)`). Per the Android docs, a microphone FGS cannot be started while the app is in the background or from `BOOT_COMPLETED`, so the user starts listening from the app, a Quick Settings tile, or the notification. The API server can stay up inside the same service while it is running.

**Local API** (for Chrome and other clients):
- Bind `127.0.0.1` only, fixed port (e.g. 8766; 8765 is taken by aesopd per termux-helper).
- Auth: random bearer token generated on first run, stored with Android Keystore-backed encryption, shown and copyable in Settings, rotatable. Required on every HTTP request (`Authorization: Bearer`) and on WebSocket connect (header, or `Sec-WebSocket-Protocol` / first message since browsers cannot set WS headers). Check `Origin` against an allowlist (DNS-rebinding defence, same idea as code-review-graph's `http_origin_guard.py`).
- Endpoints: `GET /v1/health`; `POST /v1/tts` (text, voice, speed → WAV/PCM); `POST /v1/stt` (audio → text); `WS /v1/stream` (client sends PCM frames, server sends `vad_start`/`vad_end`/`partial`/`final` JSON events and optional TTS audio); `POST /v1/listen` start/stop the device mic loop.
- Server library: Ktor server (CIO engine, websockets plugin) is pure Kotlin and runs on Android; NanoHTTPD + a WS add-on is the lighter fallback. Pick in M3 after a size check.
- Chrome on the same phone can reach `http://127.0.0.1:<port>` (loopback counts as a secure context). Off-device clients (tablet, DroidDesk) are out of scope until there is an explicit opt-in to bind on the Tailscale interface.

## 5. Look and feel: Material 3, consumer grade

Rules, so it does not repeat the last round:
- Theme from M3, not a color object: `MaterialTheme(colorScheme, typography, shapes)`. Dynamic color (Material You) via `dynamicDarkColorScheme(LocalContext.current)` / `dynamicLightColorScheme(...)` on API 31+ (minSdk 31, so always available), with a Theme Builder-generated fallback scheme. Light and dark both supported.
- Use the full M3 type scale (`displayLarge` … `labelSmall`, 15 styles) through `MaterialTheme.typography`; no hardcoded `sp` in screens. Shapes via `MaterialTheme.shapes`.
- Standard components only: `Scaffold`, `TopAppBar`/`LargeFlexibleTopAppBar`, `NavigationSuiteScaffold` (bar on phone, rail on unfolded/tablet; artifact `material3-adaptive-navigation-suite`), `ListItem`, `Card`, `FilledTonalButton`, `ButtonGroup`, `FloatingToolbar`, `ModalBottomSheet`, `Slider`, `SegmentedButton`, `Switch`, `SnackbarHost`. Tonal elevation, not glow. Edge-to-edge with proper insets.
- M3 Expressive: material3 1.4.0 is the latest stable; 1.5.0-beta02 (2026-10-21) has Expressive components (`ButtonGroup`, `SplitButton`, `FloatingToolbar`, flexible app bars) graduated from experimental. Plan: build on the BOM (`2026.09.00` is the latest shown on the BOM page) and adopt 1.5.0 when it goes stable, or use the beta behind a version catalog entry if the operator wants Expressive now.
- Screens (small set): **Talk** (big mic FAB with an animated level/state indicator, live transcript as chat bubbles, reply audio controls), **Voices** (Kokoro voice picker with preview, speed slider), **Models** (installed STT/TTS/VAD with size, path, status chips, import from folder), **API** (on/off, port, token copy/rotate, connected clients, curl examples), **Settings**. Quick Settings tile and a proper media-style ongoing notification.
- Proper launcher icon (adaptive + themed monochrome), splash via SplashScreen API, Compose previews for each screen in light/dark/dynamic, screenshot tests in CI so the look is reviewed from images, not prose.

Design references:
- Material 3 guidelines: https://m3.material.io/
- M3 Expressive: https://m3.material.io/blog/building-with-m3-expressive
- Color / dynamic color: https://m3.material.io/styles/color/overview
- Typography: https://m3.material.io/styles/typography/overview
- Components index: https://m3.material.io/components
- Material Theme Builder: https://material-foundation.github.io/material-theme-builder/
- Compose M3 (read): https://developer.android.com/develop/ui/compose/designsystems/material3
- Adaptive navigation (read): https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation
- material3 releases (read): https://developer.android.com/jetpack/androidx/releases/compose-material3
- Compose BOM (read): https://developer.android.com/develop/ui/compose/bom
- FGS types (read): https://developer.android.com/develop/background-work/services/fgs/service-types
- Reference app for quality bar: Now in Android, https://github.com/android/nowinandroid

Only the developer.android.com pages marked "(read)" were fetched this session; the m3.material.io links are listed as design targets, not as sources for claims here.

## 6. Module layout

```
aeyre-android/              (new top-level dir in the chosen repo)
  settings.gradle.kts
  gradle/libs.versions.toml (Compose BOM, material3, Ktor, coroutines, sherpa AAR)
  app/                      Compose UI, MainActivity, theme/, ui/talk|voices|models|api|settings
                            VoiceService (FGS microphone), QS tile, notification
  voice-core/               audio/ (AudioRecord, AudioTrack), vad/, stt/, tts/,
                            pipeline/ (Flow-based loop, barge-in), models/ (registry, paths)
  voice-api/                Ktor server, routes, auth token store, origin check, JSON schema
  .github/workflows/android.yml
```

Port parameters and decisions from the Python loop and `horizons-ui-full`'s stt/voice/audio classes; do not copy their UI or theme.

## 7. CI (GitHub Actions)

`android.yml` on PR and push: checkout, `actions/setup-java` (temurin 17), `android-actions/setup-android`, Gradle wrapper (committed, not generated in CI), Gradle cache, fetch sherpa AAR + Silero VAD with pinned SHA-256, `./gradlew lint testDebugUnitTest assembleDebug`, Compose screenshot tests, upload APK as an artifact and to a `debug-<branch>` Release. Secret scan (gitleaks) job. Release signing key as an Actions secret later; debug key for now. Then the standing pipeline: branch, PR, CI green, `gh pr merge --auto --squash`.

## 8. Milestones

- **M0 Skeleton**: Gradle project, M3 theme with dynamic color, NavigationSuiteScaffold with empty screens, CI producing an installable APK. Exit: installed on the Razr, screenshots reviewed by operator.
- **M1 Audio round-trip**: record + play natively. Exit: TTS → speaker → STT text match on device (native equivalent of `--demo`).
- **M2 VAD + STT**: Silero gating, Moonshine with the 10 s rule built in (or v2 streaming). Exit: spoken sentence transcribed correctly on device.
- **M3 TTS + live loop**: Kokoro, barge-in, FGS. Exit: live mic loop verified with a real spoken utterance (never verified before).
- **M4 Local API**: HTTP + WS, token, origin check. Exit: curl from Termux and a test page in Chrome both get a transcript and TTS audio; requests without a token get 401.
- **M5 Polish**: voices/models/API screens, QS tile, notification, icon, light/dark, accessibility pass. Exit: operator design sign-off.
- **M6 LLM hook**: reply provider interface, wired to OmniRoute or a local runtime.

## 9. What Claude Code on this phone can and cannot do

Can: write all Kotlin/Gradle/CI code; port the VAD/STT/TTS logic (prior Kotlin classes exist to crib from); push through PR + CI; pull the built APK; drive `adb`/logcat; test the API with curl. Compose UI built strictly from M3 components with dynamic color will look like a current Google app, because the components carry the design.

Cannot (or weak): see the UI live while writing it. Claude gets feedback only from screenshots (operator's, or CI screenshot tests rendered to PNG and read back). Visual taste on custom elements is the weak spot, which is why this brief bans custom-drawn chrome and keeps the screen count small. No local Gradle build without installing an SDK on Termux (not recommended).

Where a hosted builder helps: Google AI Studio's app builder (operator's API) is useful for fast visual mockups of the 5 screens to pick a look before M5; its output is web-first, so treat it as a design reference, not the codebase. Replit/OpenShip add little for a native Compose + NDK-library app: the build and device test still have to happen in Gradle CI and on the phone. Recommendation: Claude builds it; use AI Studio only for the M0/M5 visual direction if the operator wants options to choose from.

## 10. Which repo

Recommend **`c10vis-poem/CloviX-AEyre` (novus-aeyre, Æyre)**. Reasons: it is already the designated voice/vision daemon and Media APK repo, sits under NovÆxopia in the stack map ("capabilities" layer), and already holds the extraction plan. Not NovusAExenti (agent logic, the voice engine is not an agent) and not Aesop-Xi (orchestration/protocol; the Python `voice-engine/` there is marked temporary and to be removed once Æyre's native version round-trips). NovAExopia should get only a pointer/contract doc in `daemons/` (the API spec) so other APKs code against it.

Open questions for the operator:
1. Media APK as its own app now (this brief), or voice-core inside the Terminal APK first? Memory says this was undecided.
2. Material 3 Expressive beta now, or stable 1.4.0 and upgrade later?
3. API reachable only on the phone (127.0.0.1), or also from the tablet over Tailscale with the token?
