---
status: staged
source: wiki-admin sessions 3c1dfa47 (2026-11-11) and a5b45d30 (2026-11-12, contract A)
date: 2026-11-12
---
# Wiki admin report: everything found so far, in one file

This one file is for the owner and for any agent he hands it to. It joins the seven reports from session 3c1dfa47
(2026-11-11). Each section names the file it came from; those files sit next to this one in `01-inbox/`. Nothing in
here has been promoted into the wiki yet. No commands were run to write this report: it repeats what the source files
say. If a fact matters, check it in the source file named.

**Contents:** 1 what was done · 2 the phone today (playbook) · 3 models · 4 routes · 5 where the material is ·
6 research notes · 7 audit of greedy-crane (26 items) · 8 plan for part 2 · 9 questions for the owner · 10 next work order

---

## 1. What was done (session 3c1dfa47, 2026-11-11)
| Contract | What | Result |
|---|---|---|
| A | research, compilation, routes, build, audit | blocked: its steps were written as prose, so none could match; sent back (#redo) |
| A2 | research, audit, route inventory | approved (#ok): `research.md`, `audit.md`, `routes.md` |
| B | survey of the vault, shared storage and the models; vendors; part 2 plan | approved (#ok): `inventory.md`, `vendors-and-models.md`, `part2-plan.md` |
| C | a playbook to play with, plus a handoff | `PLAYBOOK.md`, handoff in NvAEx-Recaps `handoff/2026-11-11/handoff-3c1dfa47-wiki-admin.md` |
| (2026-11-12) A | this report, and all eight files merged to the vault's main branch | this file |

How to write a work order line (learned in contract A): `STEP <Tool>: <exact call>`, `SCOPE <Tool>: <boundary>`,
`REQUIRE <Kind>: <value>`, `TASK <title>`, `END goal|limit <kind>: <value>`. Text after `STEP` that isn't an exact
call never matches.

---

## 2. What you can run on the phone today
(from `compiled/PLAYBOOK.md`. None of these commands has been run yet, so the first run is also the first test.)

### 2.1 Embeddings on the NPU: EmbeddingGemma 2, all three sizes
```sh
cd ~/npu-work/eg2-server
. ~/npu-work/npu-env.sh
~/npu-work/1A/venv18/bin/python eg2_server.py --port 8085
```
In a second Termux tab:
```sh
curl -s localhost:8085/health
curl -s localhost:8085/v1/models
curl -s localhost:8085/v1/embeddings -H 'Content-Type: application/json' \
  -d '{"model":"eg2-text","input":"wiki admin test","dimensions":256,"task":"document"}'
```
| Model id | Bundle | Runs on |
|---|---|---|
| `eg2-text` | text 270M (188 MB) | NPU |
| `eg2-vision` | text + images 440M (447 MB) | NPU |
| `eg2-mm` | text + images + audio 740M (544 MB) | NPU, audio on CPU |

`dimensions` can be 768, 512, 256 or 128. `task` is `query` for searches and `document` for files. An image goes in
as `{"image": "/path.png"}` inside a list. The first call to each model compiles it for the NPU and is slow.

### 2.2 Gemini on your account credits: Antigravity CLI (`agy`, at `~/.local/bin/agy`, logged in)
```sh
agy models                                   # the model slugs your account has
agy -p "Summarize this in 5 bullets: $(cat file.md)" --model gemini-3.8-flash-medium --output-format json
agy -p "..." --model <argon or carbon slug from agy models> --effort high
agy -p "..." --output-format json --json-schema '{"type":"object","properties":{"title":{"type":"string"}}}'
```
- Credits: run `/credits` inside `agy`; quotas: `/usage`.
- In `-p` mode, tools that need approval are refused quietly unless they are allowed in `~/.gemini/antigravity-cli/settings.json`.
- An unknown `--model` exits with an error; it never falls back to another model.
- Parallel workers: `/swarm` inside an interactive `agy` session.

### 2.3 Local LLMs (Qwen 3.5, Gemma 4) on GenieX
- GenieX serves GGUF models over an OpenAI-style API at `http://127.0.0.1:18181/v1` (`geniex serve`). The CLI is in
  `~/tools/geniex-cli-v0.10.0/geniex-cli-linux-arm64-v0.10.0/`. The exact `serve` flags were not read: run it with
  `--help` first.
```sh
curl -s 127.0.0.1:18181/v1/chat/completions -H 'Content-Type: application/json' \
  -d '{"model":"qwen3.5-0.8b","messages":[{"role":"user","content":"Label this file: private, vendor-doc, plan, or code. File: BUILD-ORDER-1.md"}]}'
```

### 2.4 Which model for which job
| Job | Use | File |
|---|---|---|
| Embeddings / search index | `eg2-text` (NPU) | `~/models-npu/embeddinggemma-2/litert/` |
| Image search, screenshots | `eg2-vision` | same |
| Quick labels, triage | Qwen 3.5 0.8B (507 MB) or JEV | `Inventory/_models/gguf/Qwen3.5-0.8B-Q4_0.gguf` (+ mmproj) |
| OCR of scans | Qwen 3.5 2B/4B + mmproj, or Gemini Flash via `agy` | `Inventory/_models/gguf/` |
| Bulk reading and drafting | Gemini 3.8 Flash via `agy` | account credits |
| Hard synthesis | Gemini 4 Argon (Pro) / Carbon (Ultra) via `agy` | account credits |
| Local drafting offline | Qwen 3.5 9B Q4_0 or Gemma 4 12B | `Inventory/_models/gguf/` |
| Voice notes to text | Whisper large-v3-turbo (QAIRT, unpacked) | `Inventory/_models/installed/whisper-large-v3-turbo-8elite/` |
| Frontier second opinion | OpenRouter `anthropic/claude-fable-5.2`, `google/gemini-4-carbon` | OpenRouter key |

Not used: any Qwen3 or Qwen3-VL model (owner rule: Qwen 3.5 only).
`Inventory` = `/storage/emulated/0/Documents/_File-Driven-Agent-Operating-Environment/Inventory/_models` (79 GB).

---

## 3. Models and runtimes
(from `corpus-survey/vendors-and-models.md` and `wiki-admin-refine/routes.md`)

Phone: Razr Ultra 2025, Snapdragon 8 Elite (SM8750), Hexagon HTP v79.

### 3.1 Runtimes on the phone
| Runtime | Loads | Where |
|---|---|---|
| GenieX (`geniex serve`, `127.0.0.1:18181/v1`) | any GGUF (llama_cpp runtime, GGML Hexagon); AI Hub bundles (qairt runtime, NPU only) | `~/tools/geniex-*` v0.7.1-0.10.0, `~/repos/GenieX` |
| LiteRT-LM 0.18.1 (NPU dispatch) | `.litertlm` bundles | `~/npu-work/1A/venv18`, `~/npu-work/eg2-server/eg2_server.py` (port 8085) |
| llama.cpp / llama-server | GGUF on CPU/GPU | `~/bin/llama-server`, `~/llama.cpp`, `~/downloads/llama.cpp` |
| ORT + QNN EP | QAI Hub context binaries (fallback only) | |
| LocalAI v4.10.0 linux-arm64 | various | `Inventory/_models/runtimes/` |
| not built | TFLite, DLC (SNPE), PTE (ExecuTorch) daemons | |

### 3.2 Models on disk
| Model | File(s), size | Runtime | Job it could do |
|---|---|---|---|
| EmbeddingGemma 2: text 270M / text-vision 440M / 740M (SM8750 builds) | `~/models-npu/embeddinggemma-2/litert/` 188 / 447 / 544 MB; generic LiteRT, Q8_0 and UD-Q4_K_XL GGUF too | LiteRT-LM NPU (server written) | embeddings and index |
| EmbeddingGemma 300M int8 | `~/downloads/embeddinggemma-300m-int8.tflite` | TFLite (no daemon) | replaced by EG2 |
| Qwen 3.5 0.8B Q4_0 + mmproj F16 | Inventory gguf 507 MB + 205 MB; copy in the GenieX cache (no mmproj) | GenieX | triage, small OCR |
| Qwen 3.5 2B Q4_0 + mmproj | 1.21 G + 668 M | GenieX | extraction, OCR |
| Qwen 3.5 4B Q4_0 + mmproj | 2.58 G + 672 M | GenieX | multimodal |
| Qwen 3.5 9B Q4_0 | two builds: 5.38 G and 5.74 G (`Qwen_` prefix = the NPU primary) | GenieX | local drafting, W5H |
| Gemma 4 12B it QAT | Inventory q4_0 6.98 G; `~/downloads` UD-Q4_K_XL; mmproj in `~/gemma-12b` | GenieX / llama-server | local drafting |
| Gemma 4 E4B | IQ4_NL 4.84 G, q4_0 5.15 G, q4_k_m 5.34 G, mmproj 992 M | GenieX / llama-server | |
| Gemma 4 E2B | `~/gemma-e2b/` UD-Q4_K_XL | llama-server | light local |
| InternVL 3.5 8B Q4_0 + mmproj | 4.79 G + 678 M | GenieX | vision, OCR |
| InternVL 3.5 2B / 4B QAIRT W4A16 | zips per chip 2.4-3.7 G; unpacked in `installed/` | GenieX qairt (NPU) | vision, OCR on NPU |
| SmolVLM2 2.2B Q8_0 + mmproj | 1.93 G + 593 M | GenieX | vision |
| SmolLM2 1.7B it, QAIRT | 1.0 G per chip | GenieX qairt | |
| Granite 4.0 H Micro Q4_0 | 1.86 G | GenieX | |
| Whisper large-v3-turbo, medium, small; distil-whisper; zipformer; deepspeech2 | `speech/`, `stt/`, `installed/` | QAIRT / ONNX | voice transcripts (STT) |
| MeloTTS en, Piper TTS en | `speech/` 260 M, 69 M | QAIRT | TTS |
| Qwen3 1.7B QAIRT; qwen3_vl_4b bundle | | | not used (Qwen 3.5 only) |

"8 Elite for Galaxy" bundles target the Galaxy version of the same chip. Whether they run on this Razr is a part 2 test.

### 3.3 Vendor docs in the vault (`Vendor-Registries/`, 650 M, 73 files)
| Vendor folder | Files | What it holds |
|---|---|---|
| `google-gemma-litert/` | 17, 614 M | LiteRT / LiteRT-LM / AI Edge pages, Gemma 4 overviews, Gemini fine-tuning page, an unnamed `model.safetensors` 561 M, a gcloud CLI tarball 61 M |
| `qwen/` | 10, 34 M | Qwen 3.5 paper, 0.8B / 2B / unsloth-2B cards, two 9B compile docs |
| `qualcomm-ai-hub/` | 20, 2.0 M | model pages, GenieX Android docs, 8 speech model pages |
| `internvl/` | 1 | InternVL3.5 paper |
| `huggingface-smolvlm/` | 2 | SmolVLM2 cards |
| `agents-gateways/` | 2 | gateway overview; OmniRoute page (OmniRoute is dropped) |
| `opencode/`, `piper/`, `guides/`, `skills-references/` | 1-2 each | READMEs and guides |
| root | 2 READMEs | `README (6).md` (Prime Agent) was FLAGGED by the quarantine hook |

None of these folders yet has the standalone vendor document plus `manifest.jsonl` that the vault rule asks for.
Other vendor-doc stores: `global-documentation-vault/` (74 M), `QAIRT-QNN/` (7.1 G), `HTP/` (5 files),
`_File-Driven-.../_Jev/` (178 files).

---

## 4. Routes (which tool reaches which model)
(from `wiki-admin-refine/routes.md`. No model was called.)

### 4.1 CLIs found
| CLI | Path | Notes |
|---|---|---|
| `agy` (Antigravity CLI) | `~/.local/bin/agy` | logged in (an OAuth token file exists, not opened); one account seen |
| `claude` | `~/.local/bin/claude` | the second Claude Pro account was not checked |
| `pplx` | `~/.local/bin/pplx` | web search; key not checked |
| `hf`, `gh`, `notebooklm`, `rclone` | `$PREFIX/bin/` | |
| `gcloud` | `~/google-cloud-sdk/bin/gcloud` | |
| `llama-server` | `~/bin/llama-server` | |
| `nvaex-secret` | `~/bin/nvaex-secret` | key store; key names not listed |
| not found | `gemini` (Gemini CLI), `antigravity`, `openrouter`, `llama-cli`, `geniex`, `litert_lm_main`, `jev`, `typesafe` | GenieX CLI is a folder, not on PATH |

### 4.2 Routes to test (one round trip each, in part 2)
| Route | Invoke | Cost | Test |
|---|---|---|---|
| Gemini 3.8 Flash via `agy` (bulk) | `agy -p ... --model <slug> --output-format json` | account credits | `agy models`; one short prompt |
| Gemini 4 Argon / Carbon via `agy` | same, argon/carbon slug | Pro = Argon, Ultra = Carbon | which account is logged in |
| `agy /swarm` | interactive | credits | later |
| OpenRouter (frontier) | HTTPS API | OpenRouter credits | owner names the key; one call |
| Second Claude Pro account | second `claude` login | Pro plan | owner says where |
| JEV (TypeSafe) | prompt hook | TypeSafe | the 2026-11-12 hook lines show `local-fallback (no-key)`: key not set in this launch |
| EmbeddingGemma 2 NPU | `eg2_server.py --port 8085` | on device | start, `/health`, one embed |
| Qwen 3.5 0.8B NPU | GenieX | on device | one classify prompt; confirm NPU |
| Gemma 4 12B / E2B | `llama-server -m <gguf>` | on device | one prompt each |
| Web search | `pplx`, Bing via claw_scrape, WebFetch | key / free | DuckDuckGo and Google blocked bots on 2026-11-11 |

---

## 5. Where the material is
(from `corpus-survey/inventory.md`)

### 5.1 The vault NovAExorpus (about 10.7 GB visible)
Largest: `QAIRT-QNN/` 7.1 G (2,258 entries, a flat Qualcomm SDK dump with many numbered copies); `Drive_sync/` 1.8 G
(2,363); `Vendor-Registries/` 650 M; `qairt_/` 86 M; `global-documentation-vault/` 74 M (168); `__RESUME.md/` folder
52 M (867); `raw_database/` 30 M (889); `chunk.jsonl` 7.1 M; `clean_md/` 6.5 M (556); `02_wiki_md/` 6.2 M (550);
`manifest.jsonl` lists 585 converted files. MAP.md is 5 lines and routes nothing yet. About 30 loose files sit in the root.

### 5.2 Shared Documents
| Folder | Size | What it is |
|---|---|---|
| `_File-Driven-Agent-Operating-Environment/` | 84 G | the owner's planning docs and model store |
| `_Merovingians_Keep/` | 20 G | archive: a full older vault copy (14 G), a nested mirror (3.1 G), salvage, research |
| `_personal/` | 11 G | private: sized only, never listed |
| `_Termux-sync/` | 1.6 G | dot-folder backup |
| `NovAExorpus-6d2f7df…/`, `NovAExorpus-v2/` | 332 M, 22 M | older vault snapshots |

Inside `_File-Driven-Agent-Operating-Environment/`:
| Folder | Size / files | What it is |
|---|---|---|
| `Inventory/_models/` | 79 G | `gguf/` 47 G, `qairt/` 17 G, `installed/` 11 G, `speech/` 3.4 G, `stt/` 1.3 G |
| `Inventory/_assets/` | 5.2 G | not yet listed in full |
| `Greedy-crane/` | 1.9 M, 24 files | **the wiki-admin compilation** the owner pointed at: hybrid bridge skill, runtime architecture, harness guide (each twice), `extract_artifacts.py`, two zips, user guide, 7 skills, a 1.2 M HTML, a to-do |
| `_Jev/` | 178 entries | TypeSafe Jev docs, SDKs, cookbooks |
| `_README.txt/` (a folder) | 31 | Cialdini / JEV / Subagent Persuasion, HyperionXi, repo file structure, memory-as-skill brief |
| `plan-docs/` | 16 | Fable master brief, Cloudflare memory stack, architecture planning |
| `Plan-Order-1,2&3/` | 3 | BUILD-ORDER-1/2/3.md (10 Nov 2026) |
| `_Target-planning_objectives/` | 4 | agent engineering, JEV stage-0 ingest, multi-agent state machine, architecture report |
| `More-Argon-Builds/` | 4 | `corpus-ingest.js`, `jev_observation_db.py`, Drive consolidator, a zip |

### 5.3 Download (1.5 G)
Planning docs (blueprints as .md/.html/.mht, `19_Phase1-Dynamic-Workflows_...`), folders `Frankenstein/`,
`Fable-2026-11-03/`, `OR/`, `Copy of Agent os/`, five copies of `litedoc_workspace (1)`, session exports, a Takeout zip,
music folders.

### 5.4 Home model folders
`~/downloads/` 8.5 G, `~/models-npu/` 2.9 G, `~/gemma-e2b/` 2.5 G, `~/npu-work/` 2.1 G, `~/tools/` 1.8 G, `~/gemma-12b/` 168 M.

### 5.5 Duplicates (by name and size; nothing was deleted)
- Whole-vault copies: `_Merovingians_Keep/Zip/` (14 G), `_Merovingians_Keep/NovAExorpus-nested-mirror/` (3.1 G),
  `NovAExorpus-6d2f7df…/`, `NovAExorpus-v2/`.
- `QAIRT-QNN/` 7.1 G twice (vault and the Zip copy).
- Qwen 3.5 0.8B twice; Qwen 3.5 9B in two different builds; Gemma 4 E4B in three quants; InternVL zips plus unpacked copies.
- Doc pairs in `Greedy-crane/`; the Frontier Agent Engineering HTML twice in the vault root; `Vendor-Registries` also inside the Zip copy (536 M).

### 5.6 Flags
- `tablet-age-key.txt` is in shared Documents: it looks like a private key in shared storage (name only; not opened).
- `Vendor-Registries/README (6).md` was flagged by the quarantine hook.

---

## 6. Research notes
(from `wiki-admin-refine/research.md`, pages read 2026-11-11)

- **EmbeddingGemma 2** (`google/embeddinggemma-2`, 744.4M, Apache-2.0, multimodal). Three LiteRT bundles from
  `litert-community`: text 270M (Matryoshka down to 128d), text-vision 440M (one 768-d space), full 740M (text, code,
  images, video, audio; 8,192-token context). Each has a generic build plus chip builds, SM8750 included. Plan: text
  270M for extraction now, vision later.
- **Gemini 4 Argon and Carbon** are models, not accounts. Argon: for most engineering and knowledge work; in
  Antigravity on Pro, Ultra and Enterprise. Carbon: released 10 Nov 2026, the strongest; Ultra and Enterprise only; on
  OpenRouter as `google/gemini-4-carbon` (1.05M context, $2/$10 per million tokens).
- **AGY = Google Antigravity CLI.** `agy -p`, `--output-format text|json|stream-json`, `--json-schema`, `agy models`,
  `--model`, `--effort`, `--agent`, `--conversation`, `--sandbox`. Sign-in uses browser OAuth with a personal Google
  account, and it runs on the subscription's credits. Gemini CLI setups carry over (GEMINI.md and AGENTS.md work;
  `agy plugin import gemini`). `/swarm` is a coordinator + parallel workers + verifiers (preview).
- **Models in Antigravity:** Carbon, Argon, Gemini 3.8 Flash (every plan: the bulk-ingest model), older Flash/Pro on
  Enterprise, Claude Sonnet 5.5 and Opus 5.5 Thinking. Claude 4.6 and GPT-OSS 120B are removed on 18 Nov 2026.
- **Qwen 3.5 0.8B:** vision-language, Apache-2.0; GGUF, ONNX, AWQ and MLX builds exist.
- **JEV (TypeSafe):** a decision model that answers typed questions with calibrated probabilities.
- **OpenRouter, newest:** `anthropic/claude-fable-5.2` (1M, $8/$40), `google/gemini-4-carbon`, `google/gemini-omni-1.2-flash`;
  free long-context: `baidu/ernie-5.5-flash-preview:free`, `thinkingmachines/inkling-2-small:free`.
- Searches that failed: DuckDuckGo (bot challenge), Google ("trouble accessing"). Bing worked.

---

## 7. Audit of the greedy-crane wiki admin setup (26 items, waiting for approval by number)
(from `wiki-admin-refine/audit.md`. Fix codes: K keep, E edit, M merge, D delete.)

| # | Finding | Fix |
|---|---|---|
| 1 | Spec title and role are still the old Housekeeper | E: retitle as wiki admin |
| 2 | Spec ties the agent to the Gemini API; owner wants the CLI on account credits | E: route table, CLI first |
| 3 | Spec points at old homes (`tools/wiki-admin/`, `~/wiki-admin` launcher) | E: plugin `scripts/`, `skills/`, `crane` |
| 4 | Spec's 6-step flow lacks size gate, injection scan, crush, ledger, worker pool, dedup | E: point to the ingest skill |
| 5 | Spec lists 6 skills; agent names 19; plugin has 23 | E |
| 6 | Failure mode never filled; "no key stored" from 2026-10-28 | E from part 2 tests |
| 7 | Agent file names Gemini app / Spark / Cloud with no route | E: name `agy` and `/swarm` |
| 8 | Agent file: Gemini embeddings "through the API" | E: EmbeddingGemma 2 LiteRT first |
| 9 | Agent preloads 8 skills; 11 more named but not preloaded | owner: K or E |
| 10 | `skills/README.md` has old title and indexes 6 of 23 skills | E: index all 23 |
| 11 | `scripts/README.md` has old agent name and indexes 7 of 30 scripts | E |
| 12 | corpus-ingest preloads `honey` / `honey-px`, not found | owner: point or drop |
| 13 | No OCR tool chosen; scanned PDFs come out EMPTY | part 2: pick OCR |
| 14 | TOOLS.md: Gemini lane is `gemini_infer.py` (API) | E: `agy -p` first |
| 15 | cli-tools: web search only via `pplx`; Gemini "needs GEMINI_API_KEY" | E: add `agy`, OpenRouter, local |
| 16 | TOOLS.md points to a session scratch path | E |
| 17 | MANIFEST says no hooks.json; one exists now | E |
| 18 | MANIFEST mentions the removed step-aside switch | E |
| 19 | Root `hooks.json` is the AGY hook set | K, name it in MANIFEST |
| 20 | Same hooks also ship in NovAExopia `nvaex-wiki-admin` | see 21 |
| 21 | `nvaex-wiki-admin` is the older source of greedy-crane | owner: D or keep frozen; diff first |
| 22 | `wa_quarantine.py.bak` beside the `.py` | D after a diff |
| 23 | `__pycache__/` in the public vault | D + `.gitignore`; check if git tracks it |
| 24 | Two manifest builders (`manifest.py`, `wiki_admin.py`) | M or K after reading both |
| 25 | `killswitch.sh` still in scripts | read; D if nothing calls it |
| 26 | Uncommitted kill-switch removal breaks greedy-crane selftest | owner: revert or finish |

Not checked yet: script bodies, the 21 unread skills, `skills.json` freshness, `package/file-administrator/AGENT.md`,
`docs/WIKI-ADMIN-GUIDE.md`, `commands/llmwiki-*`. Under the 2026-11-12 rule, any item that deletes something lists every
file by name for the owner's approval.

---

## 8. Plan for part 2
(from `corpus-survey/part2-plan.md`)

**Phase 1: the owner's planning documents** (about 300 files, 12 batches of 25). Order: A `Greedy-crane/` (24, the
spec he pointed at), then B targets and build orders (~30), C `_README.txt/` (31), F vault-root reports (5), E Download
planning files, D `_Jev/` (178, lowest priority).

**Phase 2: vendor and model docs, one folder per asset.** `Vendor-Registries/<vendor>/` gets a `VENDOR.md`, `clean/`
Markdown, `manifest.jsonl` (path, sha256, size, source, date), `chunk.jsonl` and `MAP.md`. Each model gets a card at
`models/<model>.md` (path, size, sha256, runtime, chip, route). Weights never go into git, only their hash and path.
Each large store gets its own later order: `global-documentation-vault/`, `QAIRT-QNN/` (dedupe first), `Drive_sync/`,
`raw_database/`, `__RESUME.md/`.

**Routes for the reading (CLI first):** bulk via `agy` Gemini 3.8 Flash (fallback: corpus-ingest workers on Sonnet, 4
at a time); hard synthesis via Argon/Carbon (fallback: Claude Opus); injection scan `wa_quarantine.py`; triage via JEV
or Qwen 3.5 0.8B; OCR via Qwen 3.5 2B/4B or Gemini Flash; embeddings via EG2 `eg2-text` on the NPU; index in
`chunk.jsonl` (Supabase pgvector if wanted); independent verification via `verify.py`/`check.py` plus a second model.

---

## 9. Questions only the owner can answer
1. Which account is logged into `agy`: Pro (Argon) or Ultra (Carbon)? Where is the second Gemini account?
2. The second Claude Pro account: on this phone, or on another device?
3. Supabase: which project? Embeddings there, or only in git (`chunk.jsonl`)?
4. What is the OpenRouter key called in `nvaex-secret`?
5. The vault is public: can vendor docs and your planning docs go in as clean Markdown? Anything to keep out?
6. `tablet-age-key.txt` is in shared Documents: move it into the secret store?
7. The duplicate vault copies in `_Merovingians_Keep/` (14 G + 3.1 G) and the 7.1 G QAIRT dump stored twice: keep them, or a cleanup order?
8. Which download folders count as research: `Frankenstein/`, `Fable-2026-11-03/`, `OR/`, `Copy of Agent os/`?

---

## 10. The next work order (owner signs each part)
1. Route tests: one round trip each (`agy` Flash, `agy` Argon/Carbon, EG2 server, Qwen 0.8B on GenieX, OpenRouter, Supabase).
2. Read set A (`Greedy-crane/`, 24 files) in full and compare it with the greedy-crane plugin.
3. Batch ledger for sets B-F (`batch_ledger.py plan`); workers launch only with the owner's okay for each dispatch.
4. Per-asset folders with sha256 manifests for the 10 vendors, in `01-inbox/` first; promotion of each file needs the owner's okay by name.
5. The audit items the owner approves by number.

To spawn workers or call `agy` under a contract, the order needs `SCOPE Agent: corpus-ingest model: sonnet` and a
`SCOPE Bash: agy -p` line.

---

## Source files (all in the vault's `01-inbox/`)
`wiki-admin-refine/research.md` · `wiki-admin-refine/audit.md` · `wiki-admin-refine/routes.md` ·
`corpus-survey/inventory.md` · `corpus-survey/vendors-and-models.md` · `corpus-survey/part2-plan.md` · `compiled/PLAYBOOK.md`
