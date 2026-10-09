---
title: "namhokaist_appgen-qwen3-model-e-simplepath-sparse-s10warm-v42-h200x8-s100-20260731memfix-step60 · Hugging Face"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ/--• 🦁 NovusÆxenti🌳NovÆcopia🕸️• ~ /Enterprise documentation and agent assets/namhokaist_appgen-qwen3-model-e-simplepath-sparse-s10warm-v42-h200x8-s100-20260731memfix-step60 · Hugging Face.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Search models, datasets, users...
namhokaist/
appgen-qwen3-model-e-simplepath-sparse-s10warm-v42-
h200x8-s100-20260731memfix-step60
0
Image-Text-to-Text
Transformers
Safetensors
qwen3_vl
qwen3-vl
android
gui-agent
sft
appgen
conversational
Model card
Files
Community
like
luca0621/appgen-sft-ngc-v1
Yuxiang007/AMEX
License: apache-2.0
xet
Copy to bucket
Deploy
NEW
Use this model
Downloads last month
-
Image-Text-to-Text
This model isn't deployed by any Inference Provider.
🙋Ask for provider support
Model tree for namhokaist/appgen-qwen3-model-e-simplepath-sparse-s10warm-…
Base model
Qwen/Qwen3-VL-8B-Instruct
Finetuned (447)
this model
Datasets used to train namhokaist/appgen-qwen3-model-e-simplepath-sparse-s1…
Yuxiang007/AMEX
Inference Providers
NEW
Safetensors
Model size
9B params
Tensor type
BF16
Chat template
Files info


Updated Sep 27, 2024 •
1.28k •
30
luca0621/appgen-sft-ngc-v1
Viewer • Updated 11 days ago •
7.18k •
67
Edit model card
This is arm ngc_anchor_lr2p5e7 from a preregistered four-arm follow-up to the best
NGC configuration A. The language model was fully fine-tuned while the complete
Qwen3-VL visual tower, merger, and deep-stack mergers remained frozen. Publication
verifies every model.visual tensor byte-for-byte against the pinned base and verifies
that language-model weights changed.
Base: Qwen/Qwen3-VL-8B-Instruct at commit
0c351dd01ed87e9c1b53cbc748cba10e6187ff3b
Sources: luca0621/appgen-sft-ngc-v1 at
769ea99dbc4ff190048ae0db37eb6310dba595e0 and Yuxiang007/AMEX at
17196b29c88dd48a7fb90ef9131bc5c7bf39f26e
Dataset variant: ngc_anchor
Dataset SHA-256:
8890e2fe596e4d78714ce4309f2a59ed9632dd5d656f758c8dc4608d46a9c6bc
Exposures: 3,588; unique semantic examples: 3,168
Direct-grounding exposures: 400
Completion-retention replay exposures: 420
Image provenance: synthetic AppGen HTML-to-PNG
Coordinates: normalized 0–1000
AppGen Qwen3-VL frozen SFT — A-variant arm E
Training contract


Prompt: proven A prompt; SHA-256
67ff8adb0e78a617f3d0edcf196d4e4cc3239967a8c30619fc5afc14484ee8c0
Optimizer: full-language AdamW, learning rate 2.5e-07, cosine schedule, 5%
warmup
Batch: microbatch 4 × two GPUs × gradient accumulation 4 = global batch 32
Epochs: 1; optimizer updates: 113
Loss scale: Swift default
Frozen: visual encoder and aligner; trainable: language model and LM head
Only the final checkpoint (checkpoint-113) is published. The exact system prompt is
appgen_system_prompt.txt; run_manifest.json records exact hashes, the dataset
receipt, overlap audit, and weight verification. Intermediate 25-step checkpoints
remain local.
The training/evaluation overlap gate compares EXIF-transposed decoded RGBA pixels
plus image dimensions against the seven pinned AW7 test suites. It also compares
normalized instruction hashes. The exact pinned receipt must report zero train/eval
pixel and instruction overlaps for every data variant and suite before publication. Static
grounding benchmarks are not a substitute for interactive AndroidWorld task success,
and no score is claimed in this card.
This model is for Android visual-agent research, not safety-critical autonomous
deployment.
Evaluation and limitations
Company
System theme


TOS
Privacy
About
Careers
Website
Models
Datasets
Spaces
Pricing
Docs
