# NPU model server — user guide

*Written 2026-10-02. Every command was tested on this phone (Motorola Razr Ultra 2025, Snapdragon 8 Elite) on that date. For background and history, see [LOCAL-AI-GUIDE.md](LOCAL-AI-GUIDE.md) and [NPU-SERVE-BUILD-LOG.md](NPU-SERVE-BUILD-LOG.md).*

**In one line:** `npu-serve` runs one AI model at a time on the phone's NPU and serves it at **`http://127.0.0.1:18181/v1`**. Any app or script that speaks the OpenAI API can use it. To swap models, ask for a different model by name; the server unloads the old one and loads the new one by itself.

---

## 1. Starting from scratch (phone just turned on)

1. **Plug the phone in.** The NPU runs faster on power, and big models drain the battery.
2. Close heavy apps (games, camera). Models need 1–6 GB of RAM.
3. Open **Termux** and type:
   ```
   npu-serve status
   ```
   - `{"status": "ok", "model": "...", ...}` → the server is already running. Go to §3.
   - `not running` → start it:
   ```
   npu-serve smolvlm2-2.2b
   ```
4. Wait for the line ending in `| on NPU: yes`. Loads take 10 seconds to a couple of minutes (InternVL 4B/8B are the slowest). The script waits up to 4 minutes before reporting `failed`.

Any model name from §2 works in place of `smolvlm2-2.2b`.

---

## 2. The models (names to use)

| Name | What it is | Speed today\* | Sees images |
|---|---|---|---|
| `smolvlm2-2.2b` | Small, fast vision model (Hugging Face) | ~23 tok/s | yes |
| `internvl3.5-4b` | Qualcomm's precompiled NPU build of InternVL 4B, **the best match for this chip** | ~16 tok/s | yes |
| `gemma-4-e4b` | Google Gemma 4 E4B (QAT) | ~10 tok/s | yes |
| `internvl3.5-8b` | InternVL 8B, the biggest and smartest here | ~6 tok/s | yes |
| `qwen3.5-0.8b` | Qwen 3.5 0.8B | ~3 tok/s | yes |
| `qwen3.5-2b` | Qwen 3.5 2B | ~3 tok/s | yes |

\* Measured 2026-10-02 while the phone's CPU was speed-capped; real speed may be higher after a reboot. The Qwen files are slow because part of each model runs on the CPU (see the build log).

**tok/s** = words per second, roughly. 10 tok/s is about reading speed.

To see the list live:
```
curl -s http://127.0.0.1:18181/v1/models
```
`"loaded"` in the reply shows which model is in memory right now.

---

## 3. Swapping models (load / unload)

**You never unload by hand.** Every request names a model. If it isn't the one in memory, the server:
1. unloads the current model (frees its RAM and NPU),
2. loads the one you asked for,
3. answers.

The first question after a swap is slow (load time). Later questions to the same model are fast.

| You want to… | Do this |
|---|---|
| Switch model | Send a request with `"model": "<name>"` (§4), or pick it in your chat app's model menu |
| Start on a specific model | `npu-serve <name>` |
| Check what's loaded | `npu-serve status` |
| **Unload everything / free all memory** | `npu-serve stop` |
| Restart clean | `npu-serve stop`, then `npu-serve <name>` |
| Use more of the CPU alongside the NPU | `npu-serve stop`, then `npu-serve <name> hybrid` |

Only **one model is in memory at a time.** That's deliberate: two big models together would run the phone out of RAM.

---

## 4. Asking questions

### From Termux (text)
```
curl -s http://127.0.0.1:18181/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"internvl3.5-4b","messages":[{"role":"user","content":"What is an NPU?"}],"max_tokens":200}'
```

### From Termux (with a photo)
Give the photo's path on the phone:
```
curl -s http://127.0.0.1:18181/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"smolvlm2-2.2b","max_tokens":150,"messages":[{"role":"user","content":[
        {"type":"text","text":"What is in this photo?"},
        {"type":"image_url","image_url":{"url":"/storage/emulated/0/DCIM/Camera/PHOTO.jpg"}}]}]}'
```
The image `url` can be:
- a phone path (`/storage/emulated/0/...`),
- `file:///...`,
- a web link (`https://...jpg`),
- or a `data:image/jpeg;base64,...` string. This is what most chat apps send when you attach a picture.

Each message takes one image (extra images in the same message are ignored).

### From an app (Open WebUI, OmniRoute, any "OpenAI-compatible" client)
- **Base URL:** `http://127.0.0.1:18181/v1`
- **API key:** anything (it's ignored)
- **Model:** any name from §2

Streaming (`"stream": true`) works; the last chunk carries the speed (`timings.decode_tps`).

### Useful request options
| Option | Meaning | Default |
|---|---|---|
| `max_tokens` | Longest answer allowed | 512 |
| `temperature` | 0 = steady and repeatable, 1 = more creative | 0.7 |
| `top_p` | Sampling cutoff | 0.95 |
| `enable_thinking` | `true` lets Qwen models "think" first (slower) | off |

**Each request stands alone.** The server doesn't remember earlier questions. For a conversation, send the whole history in `messages` (chat apps do this for you).

---

## 5. Adding a new model

The list lives in **`~/tools/geniex-serve/models.json`**. Each entry:

```json
"my-model-name": {
  "path": "/storage/emulated/0/Documents/Models/gguf/MODEL.gguf",
  "plugin": "llama_cpp",
  "mmproj": "/storage/emulated/0/Documents/Models/gguf/mmproj-MODEL.gguf"
}
```
- **`path`**: the model file.
- **`plugin`**: `llama_cpp` for `.gguf` files; `qairt` for Qualcomm AI Hub precompiled bundles.
- **`mmproj`**: the vision add-on file. **Leave it out for text-only models.** Without it, the model can't see images.
- **Qualcomm bundles (`qairt`):** `path` must point at the **`genie_config.json` inside the bundle folder**, not the folder itself, and add `"vlm": true` if it's a vision bundle. This is the gotcha that blocked InternVL 4B until 2026-10-02.

Then `npu-serve stop` and `npu-serve my-model-name`.

Where models live:
- `Documents/Models/gguf/`: GGUF models and their `mmproj` files
- `Documents/Models/installed/`: unpacked Qualcomm bundles
- `Documents/Models/qairt/<chip>/`: bundle zips

Run `models` to list everything.

---

## 6. Troubleshooting

| Symptom | Fix |
|---|---|
| `npu-serve` says `failed` | `tail -30 ~/.cache/geniex-serve.log` to read the real error |
| `already running: ...` | It's up. Use it, or `npu-serve stop` first to change mode |
| Reply is `{"error": "load failed (-100004) ..."}` | Bad model path. For a `qairt` bundle, the path must end in `/genie_config.json` (§5) |
| `... was loaded without vision` | That model has no `mmproj` in `models.json` (§5) |
| Very slow first answer | Normal after a swap (loading). Ask again |
| Everything is slow | Plug in, close apps, reboot. The CPU speed cap seen on 2026-10-02 clears on reboot (to be confirmed) |
| Phone gets hot / app killed | Use a smaller model (`smolvlm2-2.2b`), `npu-serve stop` when done |
| Server dead after a crash | `npu-serve stop; npu-serve <name>` |

**Logs:** `~/.cache/geniex-serve.log`. `loaded <name> (..., vlm)` = loaded with vision. `stream done: N tok, ... decode X tok/s` = speed per answer.

---

## 7. Where the pieces are (if something needs rebuilding)

| Piece | Location |
|---|---|
| Start/stop script | `~/bin/npu-serve` |
| Server + model list | `~/tools/geniex-serve/` (`server.py`, `models.json`, `shim.c`, `libgeniex_shim-v0.7.1.so`) |
| Qualcomm GenieX runtime (v0.7.1) | `~/tools/geniex-bench-android-arm64-v0.7.1/` |
| Backed-up copy of the source | `aesop-xi` repo, `deploy/phone/geniex-serve/` |

Rebuild the shim (only needed if `shim.c` changes or the `.so` is lost):
```
cd ~/tools/geniex-serve
G=~/tools/geniex-bench-android-arm64-v0.7.1/lib
clang -O2 -shared -fPIC -DGX071 -o libgeniex_shim-v0.7.1.so shim.c -I. -L$G -lgeniex -Wl,-rpath,$G
```
