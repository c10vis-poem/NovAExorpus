# Copy of Horizons App: Comprehensive Architectural Blueprint and UI Specification - Reading Mode

Horizons App: Comprehensive Architectural Blueprint
and UI Specification
Horizons App: Comprehensive Architectural Blueprint and UI Specification
1. The "User-is-the-Loader" Philosophy
The Horizons architecture represents a fundamental shift in mobile systems design, moving away
from "auto-detect" background service models toward a manual "Workbench/OS" paradigm. In this
model, the Kotlin UI functions as the primary
Operating System
, serving as a lightweight command center. Conversely, resource-heavy components—including the
Chromium browser, Terminal environments, and Inference Engines—are treated as
Guest Ports
.
To eliminate the system-wide instability and memory crashes associated with background auto-
detection, we utilize
CliffordService
. This is a strictly decoupled background daemon manager. By default, the application boots into an
empty, stable state. Heavy model weights and daemons are only initialized when the user explicitly
"plates" a configuration and flips the manual switch, ensuring that Guest Ports only consume
resources when summoned.
2. The Seven-Room Functional Topology
The UI is organized into seven functional "rooms" mapped across a clock-face geometry. Each room
serves a distinct metaphor and operational responsibility:
12:00 — Monitor/Console (The Library/Checkpoint): The primary dashboard for asset
verification and "green-light" status checks. It houses the main browser for "window shopping"
and configuration testing.
02:00 — Chat (The Agentic Interface): An independent agentic entity. This is the primary
interactive port for natural language engagement.


04:30 — Settings/Platform Armory (The Pantry/Deposits Box): The secure vault and repository.
This room stores raw "ingredients"—API keys, tokens, SDKs, and raw model files imported via
"Open with -> Horizons."
06:00 — Terminal (The Mod Garage): A technical workspace for modification. It contains
precompiled commands, custom bash scripts, and runtime definitions.
07:30 — Archives (The Artifacts Vault): A real-path file manager for long-term storage of
harnesses, system logs, and saved environments.
10:00 — Horizons Panel (About/Legal/Credits): The metadata hub containing legal
documentation and project credits.
Center Hub — Router (The Fuse Box): The central information highway. This is where
configurations are "plated" and switched live using the system’s 10-amp fuse logic.
3. The Green-Light Data Pipeline
Configurations follow a strict "Land → Acknowledge → Green-Light → Fuse-Box" workflow to ensure
system integrity.
3.1 Workflow Stages
1. Land: Assets (e.g., .gguf files) are imported into the Armory or detected in local storage.
2. Acknowledge: The Monitor detects the asset and displays it in the Library as "Landed."
3. Green-Light: The user selects a Runtime Definition. The Monitor performs static checks
(AssetChecks).
4. Plugged In: The user flips the "Plug In" switch in the Monitor, making the configuration
persistent.
5. Fuse-Box (Switch On): The configuration is handed to the Router.
Expert Bypass: Advanced users may bypass the standard bake flow by selecting models
directly from the Library and dumping them into the Router if assets are already pre-
configured.
The Re-Check: At the exact moment the user flips the "Switch On" in the Router, the
system re-runs all Green-Light checks to ensure assets haven't been moved or deleted
since the initial acknowledgment.
3.2 AssetCheck Criteria
The Router refuses to close the fuse unless the following criteria are met:
Binary Presence: Engine binary must be located in application-accessible directories.
Execution Permissions: Binaries must have valid chmod +x permissions.


Asset Availability: All secondary SDKs and plugins must be resolved.
Model Path Resolution: A valid, readable model weight file must be "Plugged In."
4. UI/UX Visual Specification
4.1 Central Artifacts
Central Crystal: A symmetrical quartz crystal with a 30° bevel cap. Rendered from a 45° off-
center perspective, it features inner violet/purple glows and sharp specular streaks.
Conduits: Visualized as "Plasma Tubes" using layered glows. These lines must include beads
or nodes moving along the connection paths to indicate data flow.
4.2 Themed Backgrounds
Panel
Visual Metaphor
Aesthetic Description
Home
Grid
Obsidian Volcanic
Glass
Deep black base with angular glass facets and thin pale glint
lines.
Terminal
Matrix Waterfall
Falling green katakana and ASCII characters.
Monitor
Oscilloscope
Scrolling signal lines over a graticule grid.
Settings
Vault Door
Dark steel texture with concentric rings, bolt circles, and a spoke
handle.
Archives
Film Grain
Dark noise with scanlines, sepia flecks, and sprocket holes.
Router
Circuit Board
Faint gold and teal PCB traces with solder pads.
Horizons
Deep Space
Purple, blue, and gold butterfly nebula with slow star drift.
Chat
Rain-Splashed Slate
Blue-gray stone texture with cracks and water highlights.
4.3 Iconography
Horizons: Amber Sun with eight rays, a blue horizon line, and a pale pinkish-purple arch.
Monitor: Chat bubble icon containing two horizontal lines and a tail.
Chat: Hub-and-spoke node network featuring five outer nodes.
4.4 System Status Bar
The bottom of the UI features a status bar with five glowing dots representing
ASR, LLM, TTS, MLLM, and VAG
. Each dot utilizes radial glow layers and specular highlights to indicate active/inactive states.
4.5 Branding & Banner Typography
A header banner utilizes a "heredoc shell aesthetic" with the following specific typography:
cat << 'EOF' (Dim label)
MØ[)u14R_ 11( (36sp, Black weight display sans)


Pioneer_Tech (20sp, typewriter mono, wide spacing)
(Next-Gen Certified) (17sp, bold sans)
EOF (Bottom-left dim)
5. Systems Operations & Component Architecture
The architecture is supported by three primary storage managers:
1. ArchiveStore: A real-path file system manager. It manages a directory tree under
filesDir/archive, supporting nested folders and physical file persistence for .sh files
and harnesses.
2. RuntimeDefStore: Manages parameters for engines, including binary paths, ports, and
handshake/health-check endpoints.
3. RouterConfigStore: A persistent state manager for plated configurations (Running, Sleeping, or
Archived).
6. Interactive Standards and Accessibility
Global Copy/Paste: Every pane is wrapped in a SelectionContainer. This is a non-
negotiable requirement for all text surfaces, including chat bubbles and terminal logs.
Terminal Action Menus: Long-pressing command history triggers a menu with: Copy
Command, Copy Output, Export to Router, Save to Commands, and Archive.
Archive Navigation: Includes a breadcrumb navigation bar for jumping through the directory
tree and inline viewers for quick inspection.
7. System Sentinels and Easter Eggs
The Goat: Triggered by runtime or backend failures. Displays a full-screen dark overlay with a
🐐 icon and // GOAT_SAYS_NO. It is accompanied by a synthesized bleat: a sawtooth wave
with vibrato, tremolo, and a distinct "meh-eh-eh" warble.
The 404 Cat: Triggered by browser connection drops. Displays an ASCII art cat face styled in
Matrix-green, with the message CONNECTION_NOT_FOUND.
Screensaver: Activates after 5 minutes of idle time. Attempts to load classic_cat.jpg (the
"chonky orange cat") from local storage. If missing, it falls back to a drifting starfield with a
monospace clock.
8. Next Development Targets
Time-to-Live (TTL): Implementing TTL parameters for protocol packets and living tokens
within the Armory.
App Compilation: Finalizing strategies for asset bundling and app-wide binary compilation.


Strict Manual Mode: Evaluation of a purely manual loading model where no default models are
active without user-initiated "plug-ins."
