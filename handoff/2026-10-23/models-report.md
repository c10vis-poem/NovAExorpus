# Models report 2026-10-23 (read-only; find -size +50M, GGUF headers read, Drive via MCP)
Main local set: /storage/emulated/0/Documents/_models/ (= ~/storage/shared/Documents/_models). Not inside an Obsidian vault.
## Local: Documents/_models/gguf (all Q4_0 unless noted)
Qwen3.5-9B-Q4_0.gguf 5379417312 (qwen35 9B) | Qwen_Qwen3.5-9B-Q4_0.gguf 5741391904 (same family, different build, NOT dup) | Qwen3.5-2B-Q4_0 1214873856 | Qwen3.5-0.8B-Q4_0 507154688
gemma-4-12b-it-qat-q4_0 6975877728 | gemma-4-e4b-it-q4_k_m 5335273760 | gemma-4-E4B_q4_0-it 5154941280 | gemma-4-E4B-it-IQ4_NL 4835837088
granite-4.0-h-micro-Q4_0 1860759584 | OpenGVLab_InternVL3_5-8B-Q4_0 4787329216 | SmolVLM2-2.2B-Instruct-Q8_0 1927933984
mmproj: InternVL3_5-8B-f16 678065568, Qwen3.5-2B-F16 668227264, Qwen3.5-0.8B-F16 204987232, SmolVLM2 592523200, gemma-4-E4B 991552256
## Local: other Documents/_models
qairt/{8-elite-galaxy,x-elite,x2-elite}: intern3_5_vl_4b (3.7GB zips, 8elite+xelite), intern3_5_vl_2b (2.4GB, all 3 chips), qwen3_1_7b (x-elite 1.5GB), smollm2_1_7b (x2, 8elite ~1GB)
installed/: intern3_5_vl_4b-8elite (5 parts+vision+embedding), intern3_5_vl_2b-8elite, intern3_5_vl_2b-xelite, whisper-large-v3-turbo-8elite
speech/: whisper_medium, whisper_large_v3_turbo, distil_whisper (onnx/qnn_dlc/tflite), deepspeech2, zipformer x3, melotts x2, pipertts
runtimes/local-ai-v4.10.0-linux-arm64 (150MB binary)
## Local: ~ (Termux home)
downloads/gemma-4-12B-it-qat-UD-Q4_K_XL.gguf 4267937792 (gemma4 12B) | gemma-e2b/gemma-4-E2B-it-qat-UD-Q4_K_XL.gguf 2620368960 (gemma4, 4.6B label) | gemma-12b/mmproj-gemma-4-12b-it-qat-q4_0.gguf 175115264
models-npu/qwen3_vl_4b_instruct-geniex_qairt-w4a16-qualcomm_snapdragon_8_elite/part3_of_4.bin 457768960 (ONLY part 3 of 4 present; incomplete)
downloads/weights-1-8.nexa 770293308 and "(2)" 767131196 (.nexa, identity not read; near-dup by size)
model.onnx 177870108 (unidentified) | downloads/WhisperInput/.../ggml-tiny.en.bin 77704715
## Local: vault/keep copies (non-GGUF)
Documents/NovAExorpus/Vendor-Registries/google-gemma-litert/model.safetensors 560571228 (dup in _Merovingians_Keep/Zip/Vendor-Registries/)
Documents/NovAExorpus/Drive_sync/Secure-Spark-Proof-Folder /novae-xorpus/01_raw_sources (1)/Agent models and assets/hybrid_llama_qnn.pte 930694676 (dup in _Merovingians_Keep/Zip/Drive_sync/...)
No .gguf found in any vault. Large archives (QAIRT-QNN SDK, Hexagon_SDK zip, vault-archive zips) are SDKs/backups, not models.
## Proot (Debian, containers/debian/rootfs/root/models)
kokoro-multi-lang-v1.0/model.onnx 325630829 | parakeet/ggml-parakeet-tdt-0.6b-v3-q8_0.bin 668757119 | sherpa-onnx-moonshine-base-en-int8 (2 onnx ~100/122MB) | sherpa-onnx-streaming-zipformer-en-2023-06-26 encoder int8 71083163
Ubuntu rootfs: no model files >50MB (only bun binary).
## Google Drive: folder "_models" id <drive-id> (parent folder is "_agents.md", id <drive-id>)
(name | bytes | id) all modified 2026-09-18 unless noted; no subfolders seen
gemma-4-E2B_q4_0-it.gguf 3349516256 | <drive-id>
gemma-4-e4b-it-q4_k_m.gguf 5335273760 (2026-10-13) | <drive-id>-
gemma-4-E4B-it-IQ4_NL.gguf 4835837088 (2026-10-13) | <drive-id>
gemma-4-E4B_q4_0-it.gguf 5154941280 | <drive-id>
gemma-4-12B-it-qat-UD-Q4_K_XL.gguf 6716356800 | <drive-id>
gemma-4-12b-it-qat-q4_0.gguf 6975877728 | <drive-id>
mtp-gemma-4-E2B-it-BF16.gguf 170211200 | <drive-id>
granite-4.0-h-micro-Q4_0.gguf 1860759584 | <drive-id>
Qwen3.5-9B-Q4_0.gguf 5379417312 | <drive-id> ; "Qwen3.5-9B-Q4_0 (1).gguf" 5379417312 | <drive-id>- (dup of each other)
Qwen_Qwen3.5-9B-Q4_0.gguf 5741391904 | <drive-id>
Qwen3.5-2B-Q4_0.gguf 1214873856 | <drive-id> ; "(1)" copy | <drive-id>
qwen3_vl_4b_instruct-geniex_qairt-w4a16-qualcomm_snapdragon_8_elite (2).zip 3035113774 | <drive-id>
non-model: Granite-4.0-Micro AI Hub .mht, Qwen3-4B-Thinking search .jsonl
Other Drive hits for "models" folders (many auto-copied llm-wiki / On-device_Model-Guide / "models" folders from 2026-10-15) were doc dumps, not opened. Only this one holds model files found by title search (.gguf / Qwen3.5 / gemma-4 / granite / InternVL; page 1 only of the gguf title search, plus full _models listing).
## Direct answers
- Qwen3.5-9B: local gguf/Qwen3.5-9B-Q4_0 + Qwen_Qwen3.5-9B-Q4_0; both in Drive.
- Qwen3.5-2B: local + Drive. Qwen3.5-0.8B: LOCAL ONLY (Drive probe: _models listing, no 0.8B).
- Gemma 4 12B QAT: q4_0 local (gguf/) + Drive, same size 6975877728. UD-Q4_K_XL: local ~/downloads is 4267937792 but Drive copy is 6716356800: DIFFERENT files despite same name; check before treating as dup.
- Gemma E4B: all 3 variants local + Drive, same sizes.
- Gemma E2B: local ~/gemma-e2b UD-Q4_K_XL (2.6GB, local only). Drive has a different file, E2B_q4_0-it (3.3GB) + mtp E2B BF16: DRIVE ONLY.
- Granite micro: local + Drive.
- InternVL: local gguf 8B Q4_0 + mmproj, QAIRT zips (4B, 2B), installed 4B/2B 8elite. Drive: not in _models (only a "InternVL 3.5 8B" Google Doc elsewhere).
- Drive only: gemma-4-E2B_q4_0-it, mtp-gemma-4-E2B BF16, complete qwen3_vl_4b qairt zip (local has only part3_of_4). NOT USED: operator 2026-10-23 "we're not using qwen 3vl"; Qwen family = Qwen 3.5 only, multimodal 4B = Qwen/Qwen3.5-4B (not on phone by these probes).
## Probes / gaps
- Permission denied: /storage (cannot list; SD card check done via ~/storage/external-0 and media-0, both empty), Android/data, proot rootfs sdcard/data dirs. Android/media and Download searched: no model files.
- find -size +50M only; a second find for model extensions under 50MB (gguf/litertlm/task/pte/safetensors/tflite) returned nothing. .part/.crdownload stub find returned nothing in ~ and shared. .litertlm/.task: none found.
- Debian proot searched root/opt/home only.
- Disclosure: to find the Drive folder I called get_file_metadata on the "_agents.md" folder (metadata only, parent of _models); I did not list or search inside it except the _models child you asked about.
- Header names: gemma-4-12b q4_0 general.name "12B_qat_it_dequant_safetensors"; E4B_q4_0 name "Hf". file_type absent in text-model headers read (first keys only).
- 2026-10-23 added (operator 57 yes): gguf/Qwen3.5-4B-Q4_0.gguf 2583221408 sha256 298fcb5f…72b8bb + gguf/mmproj-Qwen3.5-4B-F16.gguf 672423616 sha256 cd88edcf…91f864, from unsloth/Qwen3.5-4B-GGUF; both match HF LFS oids.
