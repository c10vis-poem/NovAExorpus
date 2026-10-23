# Voice research, 2026-10-23 (read-only; nothing fetched/installed)
Note: this env's `grep` is a shell function; real binary /data/data/com.termux/files/usr/bin/grep. Open ASR / TTS Arena live tables are JS/private; WER/Elo below are from model cards, Phonon-2 card, Artificial Analysis (AA) page.

## 1. Kokoro: prior claim VERIFIED
| Item | Date | Source |
|---|---|---|
| Kokoro-82M v0.19 | 2024-12-25 | https://huggingface.co/hexgrad/Kokoro-82M (Releases table) |
| Kokoro-82M v1.0 (54 voices, 8 langs) | 2025-01-27 | same |
| Kokoro-82M-v1.1-zh | HF repo updated 2025-03-04 | https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh : "not a strict upgrade ... drops many voices", +100 Chinese speakers +3 EN voices |
| hexgrad HF repos: Kokoro-82M (upd 2025-04-10), v1.1-zh, kLegacy, styletts2 | | hf_fs ls hf://models/hexgrad |
| hexgrad/kokoro GitHub: 0 releases, last push 2025-08-06; misaki last push 2025-08-11 | | gh api users/hexgrad/repos |
| thewh1teagle/kokoro-onnx model-files: 2025-01-03, v1.0 2025-01-28, v1.1 2025-03-01 | | gh api repos/thewh1teagle/kokoro-onnx/releases |
| sherpa-onnx tts-models: kokoro-en-v0_19, kokoro-multi-lang-v1_1 (2025-06-18), kokoro-multi-lang-v1_0 (re-uploaded 2026-09-08) | | gh api repos/k2-fsa/sherpa-onnx/releases/tags/tts-models |
Result: the claim is correct. Not found by those probes: any newer hexgrad model or successor. Only third-party Kokoro derivatives (German, Vietnamese, CoreML, ExecuTorch) turned up on HF search. sherpa "v1_1" = the zh/multi-lang v1.1.
Side note (relevant to the Oct-02 log "tts_speak.py FAILS on v1.0"): sherpa's kokoro-multi-lang-v1_0 package was re-uploaded 2026-09-08.

## 2. Is 24 kHz enough?
Yes for speech; model quality, not sample rate, is the limit. 24 kHz covers to 12 kHz (my reasoning, not a cited fact). Evidence: Kokoro (24 kHz, https://huggingface.co/hexgrad/Kokoro-82M) sits at AA Elo 1065 above 44.1/48k-class models like Chatterbox (1024) and OpenAudio S1 Mini (1044) (https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice/open-weights). Others at 24 kHz: Phonon-31m, KittenTTS 2 (cards). VoxCPM2 outputs 48 kHz via built-in super-resolution (https://huggingface.co/openbmb/VoxCPM2). Fish S2 Pro sample rate: not verified.

## 3. Open TTS vs Fish quality (AA open-weights Elo, same URL as above; AA snapshots vary, recheck live)
| Model | License | Size | Quality evidence | Clone | Phone path | Verdict |
|---|---|---|---|---|---|---|
| Fish Drama 3 (2026-10) | Fish research (non-commercial) | 35B MoE/3B active | AA 1248, #1 | yes | none (needs SGLang/vLLM) | no |
| Breeze-TTS-2 | not read | not read | AA 1225 | ? | not checked | unknown |
| Ming-3.0-tts-0.5B / tiny | not read | 0.5B | AA 1190 | ? | not checked | worth a look |
| Fish S2 Pro (2026-03) | research, non-commercial, gated | 4B slow + 0.4B fast AR | AA 1112 | yes | no ONNX/QNN found; audio.cpp GGUF lists it | too big for phone |
| Voxtral TTS | ? | ? | AA 1091 | ? | ? | not checked |
| Kokoro v1.0 (current) | Apache | 82M | AA 1065 | no | sherpa CPU (in use) | baseline |
| Chatterbox | MIT (not verified) | ~0.5B | AA 1024 | yes | audio.cpp GGUF only | no |
| OpenAudio S1 Mini | Fish | 0.5B | AA 1044 | yes | none found | no |
| Qwen3-TTS 0.6B/1.7B | Apache | 0.6-1.7B | no AA row; 97 ms stream latency claim | custom voice | audio.cpp GGUF | too heavy, test later |
| VoxCPM2 | Apache | 2B, 48 kHz | no AA row | yes | audio.cpp GGUF | too heavy |
| OmniVoice (k2-fsa) | not read | Qwen3-0.6B base | 1.9M dl | ? | not in sherpa assets | check |
| KittenTTS 2 | Stellon community | 1.7B (24 kHz) | none | yes | no (old kitten-nano/mini v0.8 are in sherpa) | no |
| Supertonic-3 (2026-05) | OpenRAIL-M (code MIT) | ~99M, ONNX, 31 langs, tags <laugh> | no AA row; claims fast on CPU, no RTF given | presets; clone via paid Voice Builder | sherpa-onnx-supertonic-3-tts-int8-2026-05-11 | best phone candidate |
| Pocket TTS (Kyutai) / Phonon-31m | Kyutai (check); Phonon-31m Apache | ~31-100M, 24 kHz | no AA row | Pocket yes | sherpa-onnx-pocket-tts-int8-2026-01-26; Phonon GGUF q8 64 MB | second |
Not found by HF + sherpa asset probes: Orpheus, Dia, CosyVoice, Sesame CSM, Higgs v3, VibeVoice, NeuTTS, Spark, IndexTTS, F5 as phone builds (several appear only as audio.cpp GGUF bases: https://huggingface.co/audio-cpp/audio.cpp-gguf ). No Qualcomm AI Hub / QNN TTS build found by these probes (I did not query AI Hub itself).
Honest conclusion: Fish-class (Drama 3 / S2 Pro) is not phone-runnable. Fish itself is a research-license model.
Top 3 for this phone (judgement, no on-device RTF measured): 1 Supertonic-3, 2 Pocket TTS or Phonon-31m, 3 keep Kokoro v1.0.

## 4. STT
| Model | Evidence | Streaming | License | Phone path |
|---|---|---|---|---|
| Granite-speech-4.1-2b / 5.0-2b | AA/Appen: 5.33 mean WER top (https://www.appen.com/blog/hugging-face-open-llm-leaderboard); 5.0 added to leaderboard 21-10-2026 (init.py of hf-audio/open_asr_leaderboard) | no | not read | 2B, too big |
| Cohere transcribe 03-2026 | 5.42 | no | ? | sherpa asset 2026-04-02 |
| Canary-Qwen-2.5B | 5.63 | no | ? | big |
| Parakeet TDT 0.6B v3 | 4.96 avg on 7 sets (Phonon-2 card https://huggingface.co/FermionResearch/Phonon-2); v2 6.05 | offline; unified-en-0.6b streaming 240/560/1120 ms | CC-BY-4.0 | sherpa int8 (v2, v3, unified, streaming) |
| Whisper large-v3-turbo | 6.58 (same card) | no | MIT | whisper.cpp on device; QNN w8a16 8-Elite zip already on device (SESSION-LOG 2026-10-02:30) |
| Canary 180M Flash | 5.69 | no | ? | sherpa int8 |
| Nemotron 3.5 ASR streaming 0.6B | 7.96 | yes (80-1120 ms) | ? | sherpa int8 2026-07 |
| Moonshine v1 base (in use) / v2 streaming | no WER found on leaderboard rows I could read | v2 yes | ? | sherpa; v2 tiny-en quantized 2026-02-27; HF moonshine-ai/moonshine-streaming-{tiny,small,medium} |
| SenseVoice, FireRedASR2, Qwen3-ASR 0.6B, Kyutai STT | assets exist in sherpa (FireRed2 2026-02-26, Qwen3-ASR 2026-04-07); no WER read; Kyutai STT not found in sherpa assets | | | |
"whistle": Cactus-Compute/whistle, Apache-2.0, 16.9 MB single file, CPU, en/de/fr/es/it/nl/pl, released ~2026-10 (https://huggingface.co/Cactus-Compute/whistle). Runs on Cactus's own `needle` engine, not sherpa/ONNX; its card compares to Whisper and Moonshine.
"babbly": not found by HF search (babbly, babble, bubbly, babelfish), GitHub repo search, or web search. Unresolved; ask the operator for spelling/context.

## 5. Moonshine vs Whisper on this device: NO benchmark found
Probes: grep -RIl moonshine across ~/.claude/session-work, ~/repos/Aesop-Xi, vault. Only functional notes: repos/Aesop-Xi/skills/aesop-voice-pipeline/SKILL.md:43-47 (10 s ceiling bisected; v2 streaming has none), repos/Aesop-Xi/docs/LOCAL-AI-GUIDE.md:125,138, ~/.claude/session-work/2026-10-02/SESSION-LOG.md:30,75,110 (Moonshine transcribes a test wav; Whisper v3-turbo QNN unpacked, not tested). ~/tools/whisper-parakeet has bench and whisper-bench binaries; no result files found. No WER or latency numbers exist locally by these probes.

## 6. Recommendation (fetch not done)
- TTS: Supertonic-3 int8 via sherpa-onnx: asset `sherpa-onnx-supertonic-3-tts-int8-2026-05-11.tar.bz2` from https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models . Measure RTF + A/B vs Kokoro. Caveat: no arena Elo, OpenRAIL-M restrictions, cloning needs a paid builder. Runner-up: `sherpa-onnx-pocket-tts-int8-2026-01-26.tar.bz2` (same release).
- STT: `sherpa-onnx-nemo-parakeet-unified-en-0.6b-int8-streaming-560ms.tar.bz2` from https://github.com/k2-fsa/sherpa-onnx/releases/tag/asr-models (streaming, removes the 10 s ceiling, Parakeet-family WER). Fallback: `sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8.tar.bz2`. Cheap control: `sherpa-onnx-moonshine-tiny-en-quantized-2026-02-27`. Run all on the same clips and log WER/RTF to close item 5.
