---
title: "Linxr _ Part 1 — The Idea and Architecture - DEV Community"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ/--• 🦁 NovusÆxenti🌳NovÆcopia🕸️• ~ /CLIS-AND-AGENTS/Linxr and pockr/Linxr _ Part 1 — The Idea and Architecture - DEV Community.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Ai2th
Posted on Mar 9 • Edited on Aug 5
1
Linxr | Part 1 — The Idea and Architecture
#android
#linux
#qemu
#architecture
Linxr — Alpine Linux on Android (12 Part Series)
1
Linxr — Alpine Linux on Android (No Root)
2
Linxr | Part 1 — The Idea and Architecture
...
8 more parts...
11
Linxr | Part 10 — Automated End-to-End Testing for Mobile Virtual…
12
Linxr | Part 11 — The v3.0.0 Milestone & Official Release
The Idea and Architecture
Part 1 of 4 — building Linxr, a single APK that runs Alpine Linux on non-rooted
Android.
The Constraint
Android is a locked-down Linux system. For regular (non-root) apps:
execve() from app storage is blocked by SELinux W^X policy
Native Linux tools are unavailable without Termux


The kernel disables CONFIG_USER_NS — Docker rootless mode is impossible
No way to load kernel modules or create network namespaces
A QEMU virtual machine sidesteps all of this. The VM runs its own kernel with its own
namespace — completely isolated from Android's restrictions.
Why Alpine?
Alpine Linux is the right guest OS for a mobile VM:
Property
Alpine
Debian/Ubuntu
Compressed disk image
~35 MB
~300 MB+
Boot time
~5 s
~30+ s
RAM at idle
~30 MB
~100 MB+
Package manager
apk
apt
Init system
OpenRC
systemd
Small footprint, fast boot, full POSIX shell — ideal for embedding in an APK.
Architecture
Android OS (non-rooted)
└── APK (Flutter + Kotlin)
   ├── VmManager — asset extraction, QEMU lifecycle
   ├── VmService — ForegroundService (keeps QEMU alive)
   └── Flutter UI — Home, Terminal, About tabs
         └── TerminalScreen (dartssh2 + xterm)
QEMU process (libqemu.so)
└── Alpine Linux 3.19 VM
   └── OpenRC init → sshd on :22
         ↑


Disk Layout
Linxr uses QCOW2 copy-on-write layering:
base.qcow2 ships compressed in the APK assets. Extracted once on first install.
user.qcow2 is created fresh on first install. Persists across VM restarts — installed
packages and files survive.
The overlay is only recreated when base.qcow2 changes (asset version marker bumps
on app update).
SLIRP Networking
QEMU SLIRP requires no root and no kernel modules:
Inside the VM:
The VM has full outbound internet access. apk add , curl , git all work normally.
         SLIRP hostfwd tcp::2222-:22
         ↑
   SSH on 127.0.0.1:2222 (from Android app)
base.qcow2 (read-only — Alpine rootfs, openssh baked in)
 └── user.qcow2 (writable overlay — your data lives here)
Android app
 └── TCP to 127.0.0.1:2222
       └── QEMU hostfwd: tcp::2222-:22
             └── Alpine VM eth0 (10.0.2.15):22
                   └── sshd
eth0:    10.0.2.15/24
gateway: 10.0.2.2
DNS:     10.0.2.3  (SLIRP built-in resolver)


Token-Free Design
Pockr uses a UUID token injected via QEMU kernel cmdline to authenticate its HTTP
API. Linxr doesn't need that — SSH handles authentication natively:
Username: root
Password: alpine (baked into the base image)
No tokens, no custom API — standard SSH.
Next: Part 2 — Shipping QEMU in an APK
GitHub: github.com/AI2TH/Linxr
Linxr Series — Alpine Linux on Android
Linxr = Linux + r. A single Android APK that runs a full Alpine Linux shell on any
Android phone — no root, no Termux, no PC required.
#
Post
Topic
📖
Intro
What is Linxr? Start here
1
Part 1
The Idea and Architecture
2
Part 2
Shipping QEMU in an APK
3
Part 3
SSH Terminal in Flutter
4
Part 4
Test Results
GitHub: github.com/AI2TH/Linxr
Website: ai2th.github.io


Linxr — Alpine Linux on Android (12 Part Series)
1
Linxr — Alpine Linux on Android (No Root)
2
Linxr | Part 1 — The Idea and Architecture
...
8 more parts...
11
Linxr | Part 10 — Automated End-to-End Testing for Mobile Virtual…
12
Linxr | Part 11 — The v3.0.0 Milestone & Official Release
React Native logs that actually help you debug
production issues
Improve your mobile debugging workflow with structured logs in React Native that
provide actual context for production crashes.
Sentry
PROMOTED
Read blog


See why 4M developers consider Sentry, “not bad.”
Code of Conduct
Report abuse
Top comments (0)
•
Sentry
PROMOTED


Fixing code doesn’t have to be the worst part of your day. Learn how Sentry can
help.
Ai2th
JOINED
Mar 5, 2026
More from Ai2th
Linxr | Part 11 — The v3.0.0 Milestone & Official Release
android
linux
docker
opensource
Linxr | Part 10 — Automated End-to-End Testing for Mobile Virtual Machines
testing
android
linux
ci
Linxr | Part 9 — Dynamic Storage Expansion & Automatic resize2fs on Boot
android
linux
storage
sysadmin
Learn more
#
#
#
#
#
#
#
#
#
#
#
#
Sentry
PROMOTED


React Native logs that actually help you debug production issues
Improve your mobile debugging workflow with structured logs in React Native that provide actual
context for production crashes.
Read blog
