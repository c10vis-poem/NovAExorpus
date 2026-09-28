# OmniNeural-4B — Official Model Card Reference

Source: "Copy of README (Markor)" (Drive `1ByrC3UGewE13ewPqOGaE1jKJepHBRqZU`) — the Hugging Face model card for `NexaAI/OmniNeural-4B`. Category: **research doc / official documentation**.

**User's take**: this model is the one referenced in AESOP's Edge Model Guide (Razr Ultra only) and in Omni Claw's NPU discussion. Per the user, it's already being superseded by whatever they're running now — "still pretty cool" but not the long-term choice. Some pieces of this README are worth carrying over into their own project's README, which they intend to make "way better and way more in-depth."

## Overview

OmniNeural is described as the **world's first NPU-aware multimodal model** — designed specifically for Neural Processing Units. It natively understands text, images, and audio, and runs across PCs, mobile devices, automobiles, IoT, and robotics.

## Demo

Mobile Phone NPU demo on Samsung S25 Ultra: "the first-ever fully local, multimodal, and conversational AI assistant that hears you and sees what you see, running natively on Snapdragon NPU for long battery life and low latency."

## Key Features

- **Multimodal Intelligence** — processes text, image, and audio in a unified model for richer reasoning and perception.
- **NPU-Optimized Architecture** — uses ReLU ops, sparse tensors, convolutional layers, and static graph execution for maximum throughput — claimed 20% faster than non-NPU-aware models.
- **Hardware-Aware Attention** — attention patterns tuned for NPU, lowering compute and memory demand.
- **Native Static Graph** — supports variable-length multimodal inputs with stable, predictable latency.
- **Performance Gains** — claimed 9x faster audio processing and 3.5x faster image processing on NPUs compared to baseline encoders.
- **Privacy-First Inference** — all computation stays local: private, offline-capable, cost-efficient.

## Performance / Benchmarks

**Human evaluation vs. baselines**:
- Vision: wins/ties in ~75% of prompts against Apple Foundation, Gemma-3n-E4B, Qwen2.5-Omni-3B.
- Audio: clear lead over baselines, claimed much better than Gemma3n and the Apple foundation model.
- Text: matches or outperforms leading multimodal baselines.

**Nexa Attention speedups**:
- 9x faster audio encoding vs. Whisper encoder.
- 3.5x faster image encoding vs. SigLIP encoder.

*(These are the vendor's own benchmark claims, not independently verified here.)*

## Architecture Overview

Design tightly coupled with NPU hardware:
- NPU-friendly ops (ReLU preferred over GELU/SiLU)
- Sparse + small tensor multiplications for efficiency
- Convolutional layers favored over linear for better NPU parallelization
- Hardware-aware attention patterns to cut compute cost
- Static graph execution for predictable latency

## Production Use Cases

- **PC & Mobile** — on-device AI agents combining voice, vision, and text (e.g. summarize slides into an email on PC, extract action items from chat on mobile). Benefits: private, offline, battery-efficient.
- **Automotive** — in-car assistants for voice control, cabin safety, environment awareness (e.g. detecting an unbuckled child, a pet left in the car, loose objects, fog/construction conditions). Benefits: decisions run locally in milliseconds.
- **IoT & Robotics** — multimodal sensing for factories, AR/VR, drones, robots (e.g. defect detection, technician overlays, mid-flight hazard spotting, natural robot interaction). Benefits: works without network connectivity.

## How to Use

Mobile-only (Android) version. Quickstart docs: `docs.nexa.ai/nexa-sdk-android/quickstart`.

## Links

- Hugging Face: `https://huggingface.co/NexaAI/OmniNeural-4B`
- Site: `https://nexa.ai/`
- Discord: `https://discord.com/invite/nexa-ai`
- X/Twitter: `https://x.com/nexa_ai`
- Docs: `https://docs.nexa.ai/nexa-sdk-android/quickstart#run-your-first-model`

## Limitation

Current model is mainly optimized for English; other languages are a future step.

## Citation

```
@misc{
  title={OmniNeural: World's First NPU-aware Multimodal Model},
  author={Nexa AI}, year={2025},
  url={https://huggingface.co/NexaAI/OmniNeural-4B},
}
```

## License

Creative Commons Attribution–NonCommercial 4.0 (CC BY-NC 4.0). Non-commercial use, modification, and redistribution permitted with attribution. Commercial licensing: `dev@nexa.ai`.

## Relevance to this project

Confirms OmniNeural-4B is a real, currently-shipping Nexa AI product (not something AESOP/Omni Claw invented) — the NPU delegation described in both docs is grounded in an actual SDK (`pip install nexaai`, Nexa SDK) and quickstart. Given the user's note that they've since moved to something smarter, this README should be treated as **historical/comparison reference**, not the model the eventual build will necessarily standardize on.
