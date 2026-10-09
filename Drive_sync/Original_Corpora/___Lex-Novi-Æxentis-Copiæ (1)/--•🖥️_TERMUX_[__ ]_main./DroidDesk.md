---
title: "DroidDesk"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--•🖥️_TERMUX_[__ ]_main./DroidDesk.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

orailnoor / DroidDesk
Public
About
DroidDesk turns your Android phone into a real Linux desktop using Termux, Termux X11, TUR, and Proot. Run VS Code, Firefox,
LibreOffice, Blender, and more with X11 or VNC support for monitor setup.
Readme
GPL-3.0 license
Activity
3.2k stars
34 watching
288 forks
Report repository
Releases 1
DroidDesk v1.0.0
Latest
last month
Contributors 1
orailnoor Noor
Languages
Kotlin 35.6%
Java 27.8%
Dart 23.5%
Shell 8.7%
C 3.9%
C++ 0.3%
Other 0.2%
3 Branches
1 Tag
Go to file
Go to file
Code
orailnoor Merge pull request #32 from orailnoor/dev
e23f197 · last month
LICENSES
stuff
last month
app
stuff
last month
.gitignore
stuff
last month
APP_TROUBLESHOOTING.md
working on H/A
last month
COMPLIANCE.md
stuff
last month
LICENSE
stuff
last month
NOTICE.md
stuff
last month
README.md
docs: add attribution notice
last month
THIRD_PARTY_NOTICES.md
stuff
last month
fetch_deps.sh
VNC worked
last month
pi-launch_phone.sh
Initial
4 months ago
about to introduce isolates
last month
Code
Issues
45
main


termux-linux-setup sh
Run a full Linux desktop on any Android phone. Not a terminal. Not an emulator. A complete desktop environment with
direct kernel access -- VS Code, Blender, Metasploit, local AI, all of it.
Connect your phone to a monitor and it becomes a Linux PC. Unplug it and your entire setup comes with you.
Important
DroidDesk is an independent GPL-3.0 open-source project that incorporates modified Termux:X11 components. It is not
affiliated with or endorsed by Termux, Termux:X11, TUR, Canonical, or Ubuntu.
Source and licenses: https://github.com/orailnoor/DroidDesk
Termux:X11 upstream: https://github.com/termux/termux-x11
Everything below has been tested and confirmed working:
LibreOffice -- Word processing, spreadsheets, presentations. Fully functional.
VS Code -- Full version. Python, PIP, extensions, everything.
Claude Code -- AI coding agent running directly in terminal.
Blender -- Installs and opens. Laggy on mobile hardware, but it runs.
DroidDesk
Video
What This Actually Runs
README
GPL-3.0 license


Wireshark -- Full network analysis, every packet and protocol.
Metasploit -- Pentesting framework, runs fine.
Local AI -- Offline LLM inference, 5+ tokens/second, no API needed.
If it runs on Ubuntu, it runs here.
The Linux environment runs through Termux with direct access to the phone's kernel. No emulation, no translation -- native
performance.
The setup script installs a full desktop (XFCE4/LXQt/MATE/KDE) inside Termux using the Termux User Repository (TUR) for
GUI apps. For tools not available in TUR (Wireshark, Metasploit, etc.), a Proot container provides a standard
Ubuntu/Debian/Kali environment where you install anything with apt .
The automatic menu sync scans what you install inside Proot and adds it directly to your desktop app menu. No need to
enter the container every time.
DroidDesk is also available as a standalone Android application that completely automates this process without requiring a
separate Termux installation. It renders through an embedded Termux:X11 server running in its own Android process; the
app does not use VNC.
Rooted phones: Run the Ubuntu filesystem through chroot .
Non-rooted phones: Run an app-private native Termux userspace and install desktop packages from the X11 and TUR
repositories. PRoot is not used.
Rendering: Both modes connect directly to the embedded X11 server on DISPLAY=:0 . Adreno devices use Turnip/Zink
hardware acceleration when available; other GPUs fall back to Mesa software rendering.
Automated setup: The app extracts the bundled ARM64 Termux bootstrap, configures its private package prefix, and
installs the selected desktop automatically.
Download the latest release APK from the Releases tab and sideload it to begin.
Any Android phone (ARM64)
Termux (install from F-Droid, not Play Store)
Termux-X11 (for on-phone display)
Option A: USB-C Display Output If your phone supports display output over USB-C, just use a USB-C to HDMI adapter. Done.
Option B: Raspberry Pi Bridge For phones without display output (most mid-range phones with USB 2.0), use a Raspberry Pi
Zero 2W as a bridge:
Raspberry Pi Zero 2W with Raspberry Pi OS
Micro USB to USB-C cable
USB-C hub
Micro HDMI to HDMI adapter
SD card with Pi firmware
Wireless keyboard and mouse
How It Works
DroidDesk App (Standalone)
Requirements
For Monitor Output ( Optional )


The Pi connects to the phone via USB tethering, detects the phone's IP automatically, and opens a VNC viewer to display the
phone's desktop on the monitor.
Download and install Termux from F-Droid: https://f-droid.org/en/packages/com.termux/
Do NOT use the Play Store version. It is outdated and will not work.
Download the latest APK from: https://github.com/termux/termux-x11/releases/tag/nightly
Install it on your phone. This is the display server that renders the desktop.
Open Termux and run:
The script will:
1. Update Termux packages
2. Add X11 and TUR repositories
3. Install your chosen desktop environment (XFCE4/LXQt/MATE/KDE)
4. Set up GPU acceleration (Turnip for Adreno, Zink fallback for others)
5. Install Firefox, Git, Python, and core tools
6. Set up a Proot Linux container (Ubuntu/Debian/Kali)
7. Create the App Bridge for automatic menu syncing
8. Apply a modern dark theme
9. Optionally set up VNC for remote access
After installation completes:
Then open the Termux-X11 app on your phone. Your desktop is ready.
To install tools that are not in TUR:
Installation
Step 1: Install Termux
Step 2: Install Termux-X11
Step 3: Run the Setup Script
curl -sL https://raw.githubusercontent.com/orailnoor/DroidDesk/main/termux-linux-setup.sh -o setup.sh
bash setup.sh
Step 4: Start the Desktop
bash ~/start-x11.sh
Step 5: Install Apps Inside Proot
bash ~/start-proot.sh
apt install wireshark    # or any other package
exit
bash ~/proot-menu-sync.sh


The app will appear in your desktop menu automatically.
If you are using a Raspberry Pi Zero 2W to output to a monitor:
Flash standard Raspberry Pi OS to an SD card and boot the Pi.
Copy pi-launch_phone.sh to your Pi:
1. Connect the phone to the Pi via USB cable
2. Enable USB Tethering on the phone
3. Start VNC on the phone: bash ~/start-vnc.sh (in Termux)
4. Run the bridge script on the Pi:
The script auto-detects the phone's IP and opens a fullscreen VNC session on the monitor.
To make the Pi automatically connect when powered on, add to crontab:
Add this line:
Command
What It Does
bash ~/start-x11.sh
Start desktop via Termux-X11
bash ~/start-vnc.sh
Start desktop via VNC (if installed)
bash ~/start-proot.sh
Open Proot Linux shell
Raspberry Pi Monitor Bridge Setup
Step 1: Flash Raspberry Pi OS
Step 2: Install VNC Viewer on the Pi
sudo apt update
sudo apt install realvnc-vnc-viewer
Step 3: Copy the Launcher Script
curl -sL https://raw.githubusercontent.com/orailnoor/DroidDesk/main/pi-launch_phone.sh -o ~/pi-launch_
chmod +x ~/pi-launch_phone.sh
Step 4: Connect and Launch
bash ~/pi-launch_phone.sh
Optional: Auto-Launch on Boot
crontab -e
@reboot sleep 15 && /home/pi/pi-launch_phone.sh
Commands Reference


Command
What It Does
bash ~/proot-menu-sync.sh
Sync Proot apps to desktop menu
bash ~/stop-linux.sh
Stop all sessions
Warning
Disable Child Process in Developer Options On some Android versions (MIUI, One UI, stock Android 13+), the system
may kill Termux background processes and drop your desktop session. To prevent this:
1. Go to Settings → Developer Options
2. Find "Child process" (may be labeled differently depending on your ROM)
3. Disable child process restrictions for Termux
Without this, long-running sessions (VNC, Termux-X11) may be killed by the OS without warning.
Termux-X11 directly on the phone is faster than VNC. Use VNC only when you need monitor output through the Pi bridge
or remote access from another device.
For standalone phone use without a monitor, Termux-X11 is the recommended option.
The Proot container shares the display with the native Termux desktop. Apps installed in Proot render on the same
screen.
GPU acceleration works best on Adreno GPUs (Qualcomm Snapdragon phones). Other GPUs fall back to software
rendering.
Created by orailnoor
DroidDesk is independent software licensed under GNU GPL version 3 only. It is not affiliated with or endorsed by Termux,
Termux:X11, TUR, Canonical, Ubuntu, or other upstream projects.
The Android application incorporates GPL-licensed Termux:X11 components and bundles other third-party software under
their respective licenses. See:
Notices and attribution
Third-party software inventory
Release compliance status
Notes
Credits
License and third-party software
