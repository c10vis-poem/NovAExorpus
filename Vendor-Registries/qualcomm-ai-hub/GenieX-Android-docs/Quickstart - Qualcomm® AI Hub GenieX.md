<!-- Converted from Quickstart - Qualcomm® AI Hub GenieX.pdf — 7 pages -->

## Page 1

Qualcomm® AI Hub GenieX
Android (Kotlin) Quickstart
Android (Kotlin)
## Quickstart
This page walks through running your first model from a Kotlin app, then swapping in a
different model. For a complete reference app with chat UI, model picker, and VLM support,
see the sample app.
## Prerequisites
The SDK added to your Gradle project — see Install.
A phone running Snapdragon 8 Elite or Snapdragon 8 Elite Gen 5.
INTERNET permission in your AndroidManifest.xml (the SDK pulls weights from
Hugging Face / Qualcomm AI Hub on first use).
## Run your first model
The flow is the same regardless of model: init the SDK → pull weights → load → generate.
Below is a minimal end-to-end example using unsloth/Qwen3-0.6B-GGUF — a small Qwen3
0.6B chat model that runs on any supported chipset.

---

## Page 2

2
3
Init the SDK Qualcomm® AI Hub GenieX
Call once on app startup (idempotent — safe inside Activity.onCreate ):
Pull the model
pullFlow streams progress events. Run inside a coroutine on Dispatchers.IO :
left off.
Load the model
Resolve the on-disk paths and build an LlmWrapper :
Downloads are resumable — killing the app mid-pull and re-running picks up where it

---

## Page 3

Qualcomm® AI Hub GenieX
Generate
flow:
Apply the chat template, then collect tokens from the streaming

---

## Page 4

templated prompt.
## Switching models
Swapping models is mostly a matter of changing the model_name and the runtime_id .
There are two runtimes:
llama_cpp — runs any GGUF model. Supports NPU / GPU / CPU compute units via
compute_unit .
qairt (Qualcomm AI Engine Direct) — runs Qualcomm AI Hub Models. NPU-only,
requires an explicit chipset on Android.
## Another GGUF model (llama.cpp)
Just change the model_name (and precision if you want a different one) — the rest of the
flow is identical:
For VLMs, also pass paths.mmproj_path into VlmCreateInput — see API reference →
VLM.
## A Qualcomm AI Hub Model (NPU via Qualcomm AI Engine Direct)
Qualcomm AI Hub Models are pre-compiled per chipset and only run on the NPU. You must
pass chipset on Android:

---

## Page 5

Qualcomm® AI Hub GenieX
Then switch runtime_id = "qairt" in LlmCreateInput . See the supported Qualcomm AI
Hub repos in the API reference.
## Switching compute unit (NPU / GPU / CPU)
For llama_cpp only — set compute_unit on LlmCreateInput :
| compute _ unit |  | Compute unit |
|---|---|---|
| null or | " npu " | Hexagon NPU (recommended on Snapdragon). |
| " gpu " |  | Adreno GPU via OpenCL. |
| " cpu " |  | Pure CPU. Works on any ARM64 chipset. |
compute_unit Compute unit
 
"gpu" Adreno GPU via OpenCL.
"cpu" Pure CPU. Works on any ARM64 chipset.
Qualcomm AI Engine Direct ignores this — cpu / gpu are coerced to NPU with a warning.
## Using a local model
If the weights are already on the device — side-loaded via adb push , bundled in your app’s
files dir, or produced by another tool — point the model manager at that directory instead of a
hub: set hub = HubSource.LOCALFS and local_path to the on-disk location. pullFlow
imports it into the SDK cache (no network), after which getPaths / LlmWrapper work
exactly as they do for a downloaded model.
The full Android snippets for importing a local GGUF model and a local Qualcomm AI Engine
Direct bundle live on the Models page:

---

## Page 6

Run a local Qualcomm AI Engine Direct bundle → Android Qualcomm® AI Hub GenieX Run a local GGUF model → Android
### Using the sample app
The sample app is a fully wired chat client built on top of the snippets above. A few patterns
worth borrowing when you build your own UI:
Model picker UI — the dropdown is driven by app/src/main/assets/model_list.json .
Each entry pins a model_name , hub , and (for Qualcomm AI Engine Direct) a chipset .
Edit this file to add new models without touching code.
Resumable downloads with progress — the Progress events from pullFlow carry
per-file byte counts; the sample wires them straight into a LinearProgressIndicator .
Runtime-aware compute-unit picker — when the selected model uses Qualcomm AI
Engine Direct, the picker hides GPU/CPU options. See LoadDialog.kt .
VLM image picker — for VLMs, the sample passes the absolute file path into
VlmContent("image", path) . Don’t pass content URIs — the native side reads the file
directly.
Clone qualcomm/ai-hub-apps , open it in Android Studio, and hit Run ▶.
### Next steps
| API reference | Platforms & runtimes |
|---|---|
| Wrapper classes, runtime / compute- | Snapdragon platforms and when to |
| unit selection, and data structures. | pick llama.cpp vs Qualcomm AI Engine |
Platforms & runtimes
Direct.
Was this page helpful? Yes No

---

## Page 7

Android Install API reference Qualcomm® AI Hub GenieX
Powered by