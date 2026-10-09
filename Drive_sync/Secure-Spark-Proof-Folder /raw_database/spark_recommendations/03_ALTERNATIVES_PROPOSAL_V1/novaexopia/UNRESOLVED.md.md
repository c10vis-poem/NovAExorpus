---
title: "UNRESOLVED.md"
source: "Drive_sync/Secure-Spark-Proof-Folder /raw_database/spark_recommendations/03_ALTERNATIVES_PROPOSAL_V1/novaexopia/UNRESOLVED.md.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

UNRESOLVED.md — novaecopia Engineering
Backlog & Open Tickets
Active Backlog & Optimization Tickets
Ticket ID
Subsystem
Priority
Description &
Technical Target
NX-01
aesc / ADB
HIGH
Zero-Root Local
Pairing Automation:
Implement automated
mDNS pairing
detection inside
WirelessAdbBridg
eService so the
user only enters the
6-digit Android
Wireless Debugging
code once via
Horizons UI dialog
without requiring
manual terminal
bootstrapping.
NX-02
aesc ↔ aeyre
HIGH
Zero-Copy Shared
Memory
(ASharedMemory):
Implement Android
NDK
ASharedMemory_cr
eate + mmap over
abstract UNIX
domain sockets
(\0aesc_ipc) with
SCM_RIGHTS fd
passing. Eliminates
Android 1MB Binder
transaction limits
when passing raw


Ticket ID
Subsystem
Priority
Description &
Technical Target
PCM audio chunks
and screenshot
bitmaps between
daemons.
NX-03
aeyre / Vision
MEDIUM
Dual-Display
Dynamic Crop
Bounds: Benchmark
dynamic switching of
screen_vision_bo
unds.json when
the Motorola Razr
Ultra flips between
internal 22:9
(1080x2640) and
external cover 1:1
(1056x1066)
displays, ensuring
VLM crop
coordinates scale
without restarting the
daemon.
NX-04
mcp_connectors
MEDIUM
Tailscale Mesh
Auto-Reconnection:
Add automatic
exponential backoff
retry in
postgres_mcp.jso
n / client wrappers
when switching
between local Wi-Fi
router switch mode
and cellular Tailscale
tunnels to Node Beta.
NX-05
openwiki-tui-har
ness
LOW
Low-Memory
Profiling for
GLM-5.2: Profile
file_administrat


Ticket ID
Subsystem
Priority
Description &
Technical Target
or.yaml CPU and
memory consumption
in Termux under low
background ionice to
verify that disk tree
sweeps do not cause
frame drops in
Horizons UI
WebView.


Resolved Architectural Debt
​Removed deprecated naming artifacts ("Omni Claw" permanently removed across all
documentation and schemas).
​Formalized decoupled 3-APK IPC contracts over WebSockets and UNIX domain
sockets.
​Standardized universal repository root control files (MAP.md, manifest.jsonl,
AGENTS.md, RESUME.md, UNRESOLVED.md).
