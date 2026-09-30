# Part 1: The Consolidated Master README (/master_build-guide/README.md)
Save this complete document as the primary specification file at your workspace root. It unifies
your hardware topologies, the corrected role of OB1 and the Reasoning Bank, and sets the final
operational parameters for the system.
# 🌌 AESOP XI: Master System Orchestration Matrix## Canonical Edge Architecture &
Multi-Node Core Specifications### Operating Infrastructure: [NovA-Claw / Novus-Agenti] Engine
---## 🚨 0. Operational Core Law: The Horizons UI DependencyThe **Horizons UI** native
Kotlin/Java APK is the absolute framework foundation of this computing mesh. No local model
can load onto the Snapdragon 8 Elite NPU, no bare-metal voice pipeline can process audio, and
no screen-vision tool can execute frame context if Horizons UI is inactive. All configuration
parameters, memory layers, and routing architectures serve strictly to support operations
initiated via Horizons UI.
---## ⚙️ 1. Hardware Node Topology & Mesh Integration
The system leverages an ad-hoc Peer-to-Peer network connected over wired data interfaces
and **Tailscale** tunnels across your local network environment:
* **Node Alpha (The Mobile Engine) [Moto RAZR Ultra 2025]:** Primary on-device controller.
Runs the Snapdragon 8 Elite (Gen 4) SoC with a Hexagon NPU (v.79) pushing 40+ INT8 TOPs.
Operates with 16GB total RAM, dynamically carving out an open sandbox of **8.0 to 11.5 GB
exclusively for running local model weights**. Houses the native Horizons UI APK, Moonshine
Small ONNX (STT), and Kokoro-82m/Sherpa ONNX (TTS) voice engines.
* **Node Beta (The High-Compute Core) [Nvidia Jetson Orin Nano Super]:** Headless Ubuntu
server operating with an 8GB hardware configuration, high-speed 500+GB NVMe data storage
drives, and dedicated CUDA core tensor pipelines pushing 60-70 TOPs. Hosts your global
vector storage engines, heavy background reasoning models, and the local **OB1 Postgres
backend server**.
* **Node Gamma (The Display Station) [Rubik Pi 3 Dragonwing]:** Thundercomm/Qualcomm
SoC configuration pushing 14+ TOPs, connected via high-speed hardware data ribbons to a
dual-monitor setup to act as your core visual terminal workstation workspace.
---## 🧠 2. The Asymmetric Dual-Model Context & Memory Stack
All user interactions, device inputs, and tools execution paths are processed using a
**Dual-Model Asymmetric Workflow** running bare-metal on Node Alpha:
┌────────────────────────────────────────┐
│ HORIZONS UI INGRESS CONDUIT │
└───────────────────┬────────────────────┘
│
▼
┌────────────────────────────────────────┐
│ OMNI ROUTE CONTEXT DISPATCHER │
└───────────────────┬────────────────────┘ │
┌───────────────