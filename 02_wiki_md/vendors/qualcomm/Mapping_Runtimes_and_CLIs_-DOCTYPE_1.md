---
source: Mapping Runtimes and CLIs -!DOCTYPE (1).txt
type: html
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

html,body{padding:4px 8px 4px 8px;font-family:'sans-serif-regular';}h1,h2,h3,h4,h5,h6{font-family:'sans-serif-condensed';}a{color: #388E3C;text-decoration:underline;}img{height:auto;max-width:100%;max-height: 90vh;margin:auto;}html,body{color:#ffffff;background-color:#303030;}a:visited{color:#dddddd;}blockquote{color:#cccccc;}video, img { max-width: 100%; } pre { max-width: 100%; overflow: auto; } table, th, td {  border: 1px solid white; border-collapse: collapse; border-spacing: 0; padding: 6px; } .floatl {float: left;} .clear {clear:both;} button:hover,button:active {filter: invert(1);} button { display: inline-block; box-sizing: border-box; border: none; border-radius: 4px; padding: 0 16px; min-width: 64px; height: 36px; font-family: 'Roboto'; font-size: 14px; font-weight: 500;  line-height: 36px; overflow: hidden; outline: none; vertical-align: middle; text-align: center; text-overflow: ellipsis; text-transform: uppercase; box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12); margin: 4px 4px 8px 0px;}    .emojibtn,.fa {font-size:250%; background: transparent; padding: 0px; min-width:0px;}    .sticky {position: sticky; display: inline-block; border: 0px solid white;}
html, body {
/*
font-family: sans-serif-condensed;
font-size: 80%;
*/
}



function onPageLoaded() {
/*
if ('format-plaintext fileext-' == 'MarkdownTextConverter') {
 window.scrollTo(0, document.body.scrollHeight);
}
*/
}
 function onPageLoaded_markor_private() {

onPageLoaded(); }


```
Now that your physical infrastructure—the Moto Razr Ultra, the Jetson
Orin Nano Super, and the Rubik Pi 3—is locked in, matching the right
runtimes and CLIs to each node is what makes this mesh actually
functional.

Because you're splitting workloads across Android (Termux), NVIDIA CUDA,
and Qualcomm NPU hardware, your runtime stack divides cleanly across the
network:

## 1. The Mobile Node (Moto Razr Ultra — Snapdragon 8 Elite)

- **The CLI / Tooling:** **GenieX CLI / Python SDK** (Qualcomm's unified
  > on-device inference runtime).

- **The Runtime:** Dual-path depending on your needs. Use llama_cpp for
  > pulling standard GGUF models from Hugging Face straight into mobile
  > memory, or the qairt (Qualcomm AI Engine Direct) runtime to pin
  > pre-compiled bundles directly onto the Hexagon NPU for maximum
  > thermal and power efficiency.

- **The Job:** Running your local client-side model context, managing
  > terminal sessions via Termux, and handling local ingestion before
  > syncing up with the home tailnet.

## 2. The Heavy Inference Hub (Jetson Orin Nano Super)

- **The CLI / Tooling:** **Ollama / llama.cpp (CUDA compiled)** or
  > **TensorRT-LLM**.

- **The Runtime:** NVIDIA CUDA / TensorRT cores.

- **The Job:** Acting as the heavy muscle of your tailnet. When your
  > mesh needs serious parameter throughput or fast local vector
  > embedding searches, Tailscale routes the request straight to this
  > node's NVMe drive and Ampere architecture.

## 3. The UI & Scripting Hub (Dragonwing Rubik Pi 3)

- **The CLI / Tooling:** **GenieX Local Server** (running an
  > OpenAI-compatible API endpoint locally on the board).

- **The Runtime:** Qualcomm Hexagon 770 NPU via QAIRT.

- **The Job:** Driving your interface and hosting your background
  > scripting model. It continuously ingests agent actions, formats them
  > into your JSONL Almanac, and pushes them to your Red Agent auditor.
[‎Gemini - direct access to Google AI](_res/‎Gemini%20-%20direct%20access%20to%20Google%20AI)
```
