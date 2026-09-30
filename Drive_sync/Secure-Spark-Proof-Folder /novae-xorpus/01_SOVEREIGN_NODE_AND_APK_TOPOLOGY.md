01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md
Decoupled 3-APK Architecture, DroidDesk, ADB Loopback & Sovereign Node Mesh
1. Document Scope & Supersession Notice
This specification unifies, standardizes, and consolidates the operational architecture defined across:


* Copy of The 3-APK Native Topology & The Concierge Dataflow..txt
* The Consolidated Master README (/master_build-guide/README.md)
* Branding ligature
* What and Why.txt & Where and When.txt (W5/H Architecture Matrix)


________________


2. The Decoupled 3-APK Native Architecture
To prevent Android's Low Memory Killer (LMK) from terminating background agent execution and to bypass application sandbox restrictions without rooting, the on-device environment is split into three independent native processes communicating over local UNIX domain sockets (AF_UNIX) and WebSockets:


┌────────────────────────────────────────────────────────────────────────┐


│                        HORIZONS UI (APK 1)                             │


│                  Master Visual Shell & Concierge                       │


│  - Chromium WebView (HTML5 / React user interface)                     │


│  - Persistent WebSocket client to background daemons                   │


│  - Chat tiles, terminal visualizer, model picker, and uploader         │


│  - Fallback routing to OmniRoute / OpenRouter API                      │


└───────────────────┬────────────────────────────────┬───────────────────┘


                    │                                │


    UNIX Socket / WebSocket          UNIX Socket / WebSocket


    /dev/socket/aesc_shell.sock      /dev/socket/aeyre_media.sock


                    ▼                                ▼


┌──────────────────────────────────────┐ ┌───────────────────────────────┐


│              ÆSC (APK 2)             │ │          ÆYRE (APK 3)         │


│        Terminal & Shell Daemon       │ │      Media & Sensory Daemon   │


│ - Complete Termux replacement        │ │ - Silero VAD audio stream     │


│ - OS Accessibility & Assistant role  │ │ - Moonshine Small ONNX (STT)  │


│ - Local ADB Loopback (localhost:5555)│ │ - Kokoro-82m / Sherpa (TTS)   │


│ - Runs background CLI agent loops    │ │ - Video Game SDK screen vision│


└──────────────────────────────────────┘ └───────────────────────────────┘
Beginner-Proof Breakdown: Why 3 APKs Instead of One?
If an LLM runs inside the same process that draws buttons and text on the Android screen, the app will freeze whenever the model thinks (Garbage Collection pauses in Java/Kotlin). Furthermore, if the model runs out of memory, the whole app crashes to the home screen. By decoupling into Horizons UI, Æsc, and Æyre:


1. If the shell script or model crashes in Æsc, the user's screen in Horizons UI never flickers.
2. Æyre captures your voice continuously via Silero VAD without stuttering, even if Æsc is compiling code under 100% CPU load.
3. Each daemon runs with its own optimized Linux permissions.


________________


3. The Local ADB Loopback Architecture
The Engineering Mechanism
Android's adbd daemon runs with elevated permissions as UID shell (UID 2000). Standard apps run with isolated UIDs (e.g. u0_a245). By activating Wireless Debugging, Android exposes adbd over a local TCP loopback interface on 127.0.0.1. Æsc connects to itself via this local loopback:


1. Authentication: Æsc generates an onboard RSA key pair (~/.android/adbkey).
2. Local Pairing: User enters the 6-digit code once via adb pair 127.0.0.1:<pairing_port>.
3. Local Connection: On every device boot, Æsc connects via adb connect 127.0.0.1:<port>.
4. Sandbox Evasion: Commands executed through the local ADB shell run outside the Android app sandbox with UID 2000, allowing Æsc to spawn background daemons that survive app restarts.


________________


4. DroidDesk & Salvaging the Horizons Repo
The Transition to DroidDesk
* The Problem with Termux: Termux runs inside standard user app sandbox constraints, struggles with raw audio streams, requires complex wake-lock hacks, and cannot interact smoothly with external displays.
* The Fix: By salvaging the native C++/Java codebase from the original Horizons repository, the terminal shell engine, ADB loopback client, and NPU offload libraries are compiled directly into the standalone Æsc APK.
* DroidDesk Workstation Mode: When docked to external monitors (via Node Gamma / Rubik Pi 3), DroidDesk launches an optimized multi-window desktop interface powered by Node.js and OpenWiki CLI, rendering Termux completely obsolete.


________________


5. Sovereign 3-Node Hardware Mesh
The complete environment operates across three dedicated physical nodes connected over local encrypted Tailscale tunnels:


Node Identifier
	Hardware Platform
	Operating System
	Primary Dedicated Responsibilities
	Node Alpha (The Mobile Engine)
	Motorola RAZR Ultra 2025 (Snapdragon 8 Elite / Hexagon v79)
	Android 15 + Æsc / Æyre Daemons
	Primary on-device controller. Runs local Qwen 3.5 weights on NPU, Horizons UI, voice pipelines, and mobile ADB loopback.
	Node Beta (The Compute Server)
	NVIDIA Jetson Orin Nano Super (8GB / CUDA)
	Ubuntu Server LTS (Headless)
	Central database hub. Hosts PostgreSQL, OB1 vector protocol, heavy background reasoning models, and cross-node audit logs.
	Node Gamma (The Display Station)
	DragonWing Rubik Pi 3 (Qualcomm SoC)
	Embedded Linux / Display Manager
	Workstation visual terminal. Drives dual-monitor setup, physical keyboard/mouse ingress, and terminal monitoring dashboards.