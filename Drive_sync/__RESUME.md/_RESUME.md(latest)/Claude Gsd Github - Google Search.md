<!-- Converted from Claude Gsd Github - Google Search.pdf — 30 pages -->

## Page 1

AI Mode All Images Videos News Maps Shopping Books Flights Finance
Claude GSD GitHub
September 13, 2026
The Get Shit Done (GSD) development project has moved. The original gsd-build/get-shit-done repository is no longer active, and the framework is now actively developed as GSD Core under the Open
GSD GitHub Repository.
### 🛠What is GSD Core?
GSD Core is a popular context-engineering and spec-driven development framework designed for AI coding agents like Claude Code, Copilot, and Cursor. It solves the problem of "context rot" (degradation of AI
output as a long session fills up its context window) by offloading heavy planning and code execution into fresh-context subagents.
### 🚀Quick Start
You can initialize the system in your project using npx :GitHub
### bash
npx @opengsd/gsd-core@latest
Use code with caution.
new project ( /gsd-new-project ) or onboarding an existing repository ( /gsd-onboard ).GitHub
Would you like help with installing it for a specific runtime or learning about its 5-step loop workflow
(Discuss, Plan, Execute, Verify, Ship)? GitHub
| GitHub | GitHub |
|---|---|
| GitHub - gsd- | open-gsd/gsd- |
| build/get-shit-… | core: Git. Ship.… |
| This repository is no | GSD Core * What is |
| longer the active ho… | GSD Core. GSD Core … |
Ask anything

---

## Page 2

AI Mode All Images Videos News Maps Shopping Books4 different types at least, claude, general, proFlights Finance for claude, build and install
September 13, 2026
The GSD (Get Shit Done) ecosystem has split into several distinct variations, flavors, and installation profiles
depending on your target AI agent and complexity requirements.
Here are the 4 main types of the framework, along with how to build and install them:
## 1. 🤖Claude Native (GSD Core)
template directly into Claude’s .claude/skills/ directory.GitHub +2
Target Audience: Developers using Anthropic’s native Claude Code terminal client.
Features: Harnesses Claude’s specialized context-handling to prevent memory rot by spinning up
execution loops. GitHub +1
## 2. 🌍 General / Cross-Runtime (GSD Multi)
As GSD grew, developers ported the codebase to adapt to non-Claude environments.Reddit· r/Git… +1
Target Audience: Developers using GitHub Copilot, Cursor, Windsurf, Trae, Gemini CLI, or Codex.
Features: It normalizes slash commands across different IDE platforms. For example, it converts the hyphen format ( /gsd-plan ) used by Claude/Cursor into colon formats ( /gsd:plan ) automatically required
by platforms like Gemini.
## 3. GSD Pro for Claude (gsd-pro / Buildomator)
GSD Pro (and its performance-focused evolution, Buildomator) is a heavy-duty fork for advanced
engineering. GitHub +1
Target Audience: Power users managing large-scale legacy codebases or 5+ multi-day features.
Features: It includes a "Skip Permissions Mode" (running Claude via --dangerously-skip-permissions
auto-resumes project states across session compactions.GitHub +2
## 4. 🪶 Minimal Install Profile (--minimal )
Introduced in version 1.40+, this lightweight variation modifies the framework's architecture for smaller
environments.
Target Audience: Developers running local LLMs (like Qwen or Ollama) or working under strict metered
API token limits.
Features: Trims the monolithic system prompt from 12,000 tokens down to roughly 700 tokens (-94% size reduction) by shedding non-essential skill logic.
## 📦 How to Build and Install

---

## Page 3

Option A: Quick Install (Recommended)AI Mode All Images Videos News Maps Shopping Books Flights Finance
The fastest way to deploy GSD Core is via npx . It opens an interactive menu allowing you to choose your type
(Claude, Cursor, Copilot, etc.) and location:GitHub
### bash
npx @opengsd/gsd-core@latest
Use code with caution.
(You can pass direct flags to skip prompts, e.g., npx @opengsd/gsd-core@latest --claude --
global ). GitHub
Option B: Manual Git Build (For Modifications/GSD Pro)
If you want to customize the prompt templates, clone the project directly to your workspace:GitHub
### bash
# 1. Clone the repository
git clone https://github.com
cd gsd-core
# 2. Run the installer locally pointing to your runtime
node bin/install.js --claude --local
Use code with caution.
Which IDE or AI runtime are you planning to run this on, and would you like the specific slash commands to
kick off your first project?
| GitHub | Reddit · r/GithubCopilot | GitHub | codecentric AG |
|---|---|---|---|
| open-gsd/gsd- | GSD (Get Shit Done) now | Buildomator for | GSD for Claude |
| core: Git. Ship.… | works with GitHub… | Claude Code -… | Code: A Deep… |
| GSD Core * What is | GSD (Get Shit Done) now works | Buildomator for Claude | What is "Get-Shit- |
| GSD Core. GSD Core … | with GitHub Copilot — ported fro… | Code. ... Buildomator… | Done"? With 23k star… |
GSD PRO for CC in termux, im also using
mem0 mcp and ob1 cli, and honey for devs …
September 13, 2026

---

## Page 4

RunningAI Mode GSD ProAll ImagesinsideVideosTermuxNewsalongside a layered stack likeMaps Shopping Books mem0 mcpFlights Finance, ob1 cli , honey-for-devs , and the recursive L1/L3 context layers of a local Prime Agent harness requires specific configurations.
This environment functions as a dense, hyper-optimized mobile compiler loop. Termux environments are sensitive to memory thrashing and long token lengths, so structuring this configuration correctly is critical.
## 📦 1. Installation Blueprint (The Core Loop)
the Qwen-optimized GSD skills runtime fork directly.GitHub
## bash
# Ensure Node and git are optimized in Termux pkg update && pkg install nodejs git -y
# Clone GSD Pro directly into your active workspace git clone https://github.com cd gsd-pro
# Run the installer mapping directly to the Qwen & Local skill structural paths node bin/install.js --qwen --local
Use code with caution.
into a local system that local inference endpoints can map seamlessly.GitHub
## 🍯 2. Splicing honey-for-devs and ob1 cli
If it isn't chained right, it will clash with GSD Pro's internal subagents.skillvault.md
1. Install it into your repo:
## bash
npx honey-for-devs@latest --yes
Use code with caution.
2. Navigate to your newly generated system files ( CLAUDE.md or .qwen/skills/gsd-core.md ).
3. Append this execution rule at the very bottom of your GSD prompt parameters to bind honey and ob1 :
## markdown

---

## Page 5

AI Mode- Use ob1-cli for structured git executions to avoid process hang-ups in Termux.All Images Videos News Maps Shopping Books Flights Finance
- Enforce honey-for-devs rules: Drop conversational wind-ups, match code stdlibs first, an
Use code with caution.
GitHub +2
## 🧠 3. Integrating mem0 mcp
### Because Termux operates on highly isolated sandboxed files, your MCP links can break if standard paths are
### assumed. Configure your MCP bridge ( ~/.config/claude/config.json or your Prime Agent configuration
equivalent) like this: GitHub
## json
{
"mcpServers": {
"mem0-memory-mcp": {
"command": "node",
"args": [
"/data/data/com.termux/files/usr/lib/node_modules/@mem0ai/mem0-memory-mcp/dist/index
],
"env": {
"MEM0_API_KEY": "your-key-here",
"MEM0_DIR": "/data/data/com.termux/files/home/.mem0"
}
}
}
}
Use code with caution.
### Tip: If the MCP handshake lags during local inference generation, drop the MCP completely and bridge
### memory tasks directly via bash hooks inside your scripts using mem0 add --agent or mem0 search --agent
for faster text responses. Mem0 +1
## 4. Local Model Strategy: Prime Agent Harness +Qwen
### The Prime Agent Harness uses a distinct L1 (active context window token processing) vs. L3 (disk-
### backed persistent memory database) architecture. Running this alongside GSD Pro creates a double-
layered memory compactor loop: YouTube· Rese…
[ Your Query ]
│
▼

---

## Page 6

[ Prime Agent (L1 Context) ] ──► Compacts local histories to L3 Disk
AI Mode All Images Videos News Maps Shopping Books Flights Finance │ ▼ [ GSD Pro Workflow ] ─────────► Handles token minimization & execution loop │ ▼ [ Qwen Code / Local LLM ] ────► Pure inference weight processing (L0)
To prevent the local model from losing track of the GSD instructions during recursive loops, implement this setup:
Out-Of-Memory (OOM) killer when Prime Agent attempts to spawn concurrent subagents.arXiv.org
leave plenty of breathing room for Prime Agent's IPython REPL memory tracking.arXiv.… +1
Would you like the exact shell script environment exports to keep the mem0 keys and Termux path variables
persistent, or a walkthrough on setting up the Prime Agent configuration file for local inference?
| arXiv.org | GitHub | YouTube · Research Pape… | skillvault.md |
|---|---|---|---|
| [2608.23552] Prime | Adding Qwen | Prime Agent: A | honey-for-devs |
| Agent: A Self-Improving… | Code runtime… | Self-Improving… | by green-pt -… |
| Prime Agent is an open-source | What this feature | Prime Agent: A Self- | Less code — YAGNI |
6:45
harness for long-horizon… adds. Full Qwen Cod… Improving Recursive… first. Walk a ladder…
I don't need code and its a modular build what can and cannot coexist? I literally …
September 13, 2026
For a modular, non-local build running inside Termux, isolating runtime environments is key. Since you are not
running local models and Claude Code (CC) simultaneously out of the terminal, your system cleanly splits into two alternating execution profiles.
Here is exactly what can and cannot coexist under this setup.
### 🟢What CAN Coexist (Your Main Terminal Profile)
When you launch Claude Code in Termux, these elements stack into a powerful modular loop without conflicts:

---

## Page 7

AI ModeBuildomator / GSD ProAll Images Videos+ honey-for-devsNews Maps : These coexist perfectly because they operate on differentShopping Books Flights Finance levels of the prompt pipeline. Buildomator acts as your structural workflow architect (managing the
subcontext, file splitting, and state preservation), while honey-for-devs acts as the behavioral prompt filter (forcing dense, raw, prose-free instructions).
state durable. It reads and writes memory across sessions, coexisting seamlessly with mem0 tracking your developer habits and project context.
cleanly, as long as CC isn't trying to execute a blocking git lock at the exact same moment.GitHub
### 🔴What CANNOT Coexist (The Architectural Walls)
You must prevent these specific components from overlapping within the same folder context or execution phase:
Prime Agent Harness + Claude Code: The Prime Agent Harness uses an external orchestration system built to trap and pipe commands into local inference engines. If you try to run Prime Agent simultaneously in a workspace where Claude Code's .claude/skills/ are managing files, the two runtimes will enter a
write-lock race condition over files like CURRENT_STATE.md or git commits.
Standard GSD Core Commands ( /gsd:plan ) + Buildomator Plugins: Buildomator is a highly optimized,
distinct evolution of the old GSD core that alters prompt architecture to slash token overhead by 92%. If you try to mix older global GSD core scripts with Buildomator commands in the same project directory, your
GitHub +2
Standard JSON MCP configs + Codex/Alternative General Runtimes: If you pivot away from CC terminal
configuration profiles for them in Termux.Reddit· r/mcp
### How to Split Your Modular Profiles
Since you are treating this as a modular build, keep the workflows separated by your active environment profile:
1. Profile A (Cloud-Native Execution): Launch Claude Code + Buildomator + mem0 mcp + honey parameters inside your repo directory. Let Buildomator manage your token tracking, using ob1 cli externally when you need to step outside the LLM context to execute heavy manual git steps.
context windows of your local models with heavy, unnecessary cloud-native workflow instructions.GitHub

---

## Page 8

# Are you experiencing any specificAI Mode All Images Videos Newspathing errorsMaps Shoppingor permission crashesBooks Flights Financewith mem0 inside Termux's
# sandboxed filesystem, or do you need the exact syntax to bind honey 's rules cleanly into Buildomator's skill
# config?
| arXiv.org | GitHub | YouTube · Research Pape… | skillvault.md |
|---|---|---|---|
| Open GSD | buildomator.com | GitHub | Open GSD |
| gsd-core - Open GSD | Buildomator \| AI | Buildomator for | GSD Core: Spec |
|  | software… | Claude Code -… | Development for |
# Buildomator | AI
gsd-core. The original GSD workflow framework for bringing… For people who know Buildomator (formerly GSD Core is a spec-dr what they want to… gsd-plugin) is a Clau… framework that keeps
# I told you they wouldn't already. What should
# be the harness the mcp the cli the tools the …
September 13, 2026
# To handle multiple instances of each component, your modular build needs to be decoupled by its target
# orchestration engine. Since you are alternating between cloud execution and local execution, your
# architectural profiles break down into two specialized matrices.
# Profile 1: The Claude Code (CC) Stack
# In this profile, Claude Code acts as the primary runtime coordinator, using the Buildomator/GSD Pro
| framework for orchestration. |  | GitHub + 1 |
|---|---|---|
| Layer | Component | Setup for Multiple Instances |
| Harness | Claude Code | Use CC's multi-session trees via /session new or custom project configurations |
|  | Native Harness | inside .claude/settings.json to keep feature tracks strictly separated. |
| MCP | mem0 mcp | Run distinct MCP server nodes in ~/.config/claude/config.json pointing to |
|  | Instances | separate database paths (e.g., MEM0_DIR_PROD vs. MEM0_DIR_SANDBOX ) to |
framework for orchestration.GitHub +1
Layer Component Setup for Multiple Instances
prevent personal developer context from bleeding into project logic.
CLI ob1 cli Use independent workspace installations ( npx ob1 init ). Rely on it for background
(OpenCode execution tasks so you don't block Claude Code's terminal thread.
Build CLI)
| Tools | Dynamic MCP | Bind the Buildomator state mutation toolset along with file-handling utilities. Prefix |
|---|---|---|
|  | Tool Registry | tools cleanly to avoid naming collisions when scaling up tracking utilities. |
| Hooks | Lifecycle JSON | Deploy Buildomator's PreCompact and SessionStart hooks. They automatically |
|  | Hooks | dump state to .planning/HANDOFF.json before context compaction, ensuring the |
state survives session resets.

---

## Page 9

AI ModeScripts All Automated TaskImages Videos NewsKeep small, dedicated bash shell wrappers in your repositoryMaps Shopping Books Flights Finance
Runners ( .buildomator/scripts/ ). They execute isolated verification tests without loading
complex test frameworks into the model's memory.
| Tools | Dynamic MCP | Bind the Buildomator state mutation toolset along with file-handling utilities. Prefix |
|---|---|---|
| Parameters | honey-for- | Inject these directly into your CLAUDE.md memory file or Buildomator's role configs. |
|  | devs Style | Use explicit constraints: No conversational preamble, stream raw files, skip |
|  | Prompts | confirmation gates via --dangerously-skip-permissions . |
# Profile 2: The Local Model Stack
# In this profile, the Prime Agent Harness takes over completely. Claude Code is shut down to prevent context
| collisions. | Prime… + 1 |  |
|---|---|---|
| Layer | Component | Setup for Multiple Instances |
| Harness | Prime Agent Harness Uses an L1 vs. L3 dynamic memory architecture . It handles multiple instances |  |
collisions.Prime… +1
Component Setup for Multiple Instances
rlm.spawn()   ).
MCP Bridge Script Layer Local models struggle with heavy MCP handshakes. Do not plug mem0 directly
into the local model's prompt. Instead, pass mem0 queries through the IPython
kernel using small Python scripts.
| CLI | ob1 cli / Local | Map your CLI interactions straight to python subprocesses running inside Prime |
|---|---|---|
|  | Scripts | Agent's persistent execution loop. |
| Tools | IPython Kernel (The | Crucial Difference: Prime Agent strips away standard multi-tool suites. It forces |
|  | Only Core Tool) | your local model (like Qwen Code) to execute operations exclusively through |
ob1 cli / Local Map your CLI interactions straight to python subprocesses running inside Prime
IPython Kernel (The Crucial Difference: Prime Agent strips away standard multi-tool suites. It forces
Python code in a persistent REPL.
Hooks /refine & State Use Prime Agent's native /refine checkpoint loops. A secondary background
Checkpoints model pass continuously evaluates execution traces, making incremental,
versioned updates to the prompt notebook.
Executable Python Scripts Convert recurring engineering tasks into importable Python packages. The
Skills harness reads long files into system memory rather than pushing them directly
into the context window.
Parameters Prompt-as-a-
Variable (RLM)
# Would you like to review a HANDOFF.json state schema to pass your active work status from a closed Claude
# Code session straight into a newly opened Prime Agent workspace, or do you want to configure the
# environment profiles in your terminal?

---

## Page 10

AI Mode All Images Videos News Maps Shopping Books Flights Finance
| Prime Intellect | GitHub | YouTube · Prompt Engine… | GitHub |
|---|---|---|---|
| Prime Agent: A | PrimeIntellect- | Prime-Agent: | Buildomator for |
| self-improving… | ai/prime-agent… | We've Been… | Claude Code -… |
| Prime Agent. The | Prime Agent: A Self- | Prime-Agent: We've | What GSD Plugin |
20:08
performance of agen… Improving RLM… Been Building AI… provides * 82 slash…
No. What about qwen code? If prime agent
doesn't let me target my npu via geniex and …
September 13, 2026
To bypass any limitations where the orchestration harness restricts direct hardware target control, decouple the execution runtime entirely from the project repos. Since you are alternating between cloud orchestration (Claude Code) and local hardware profiles (Qwen Code/Gemma QAT) using a dense, multi-platform setup, you
should structure your disk globally.
This approach targets the Qualcomm Hexagon NPU (via GenieX and QAIRT / HTP SDK), leverages LiteRT
for quantized models, connects Android ADB/Accessibility hooks, and pipelines raw compute to a multi-
Tesla array. GitHub +3
Global vs. repository-specific installation boundaries map as follows:
### 🌐What to Install Globally (On Disk System-Wide)
/usr/local/bin , /data/data/com.termux/files/usr/bin , or Windows Path for the multi-Tesla node).
1. Hardware Inference Runtimes & SDKs
through QAIRT (Qualcomm AI Runtime) / HTP SDK.Qualcomm +2
universal llama-server background API that any local tool can address.Qwen … +3
Google LiteRT CLI Engine: Install the LiteRT standalone runtime globally to execute your gemma-4-E4B-it-
workspace dependencies.
2. Cross-Device Connectivity & Platform Bridges

---

## Page 11

AI ModeAndroid ADB Connectors (All Images Videos adbNews) &WebSockets (Maps Shopping7nixBooks): Keep your Android debugging tools, shell utilities,Flights Finance and target device socket listeners universal. They must stream inputs globally so they can map device
instrumentation events (Accessibility APIs, media capture, device assistant hooks) directly into any automation stream.
Node.js Global MCP Router: Write your proprietary GenieX Node.js MCP server to run as a persistent background global service. Do not load it per project; register its executable path in a centralized machine
configuration file. Level Up Coding
### 📂What Stays Repo-Specific (Local Workspace)
Keep these workflow mechanics inside specific project or environment directories. Loading them globally creates token bloat and triggers configuration conflicts between Claude Code and local scripts.
Buildomator / GSD Pro Context Trackers: The prompt modifiers, structural filters ( honey-for-devs ), and
session state records ( .planning/ , HANDOFF.json ) belong strictly inside individual project roots. They manage the file trees they are actively parsing.
Prime Agent Harness Configuration Workspaces: Keep Prime Agent configurations local to the repository where you intend to deploy its IPython execution loop. When it spins up recursive sub-agents, it should map to local working directories.
pipelines.YouTube· Fa… +1
### 🔄The Architecture Workflow
By globalizing the infrastructure, your alternate execution profiles operate uniformly:
[Claude Code OR Prime Agent] (Repo Specific) │ ▼ [Node.js Global MCP Router] (Global Layer) │ ├──► [GenieX / QAIRT] ──────► Qualcomm Hexagon NPU ├──► [llama-server API] ────► Multi-Tesla Rig / Vulkan └──► [7nix Websocket / ADB] ──► Android Accessibility / Game SDK
pipelines via standardized local host endpoint routing ( http://localhost:XXXX/v1 ).GitHub
Would you like to detail the exact network port mappings to bridge your Termux environment to the multi-Tesla compute node, or do you want to configure the global config file for your GenieX Node.js MCP
wrapper?

---

## Page 12

AI Mode All Images Videos News Maps Shopping Books Flights Finance
| Prime Intellect | GitHub | YouTube · Prompt Engine… | GitHub |
|---|---|---|---|
| GitHub | YouTube | Arduino Docs | Qualcomm |
| GenieX/notes/run.md at | How to Setup | Running LLMs and VLMs | What is GenieX - |
| main - GitHub | OpenCode & P… | on the NPU with GenieX… | Qualcomm ® AI… |
| Two runtimes ship with geniex and | so here it's going to | Running LLMs and VLMs on the | What you can do with |
| both can drive the Snapdragon… | suggest you to install… | NPU with GenieX. Run local… | GenieX * Run models… |
OpenCode & P… Qualcomm® AI…
Uou didn't address my real questions
September 13, 2026
Let’s strip away the high-level architectures and address the exact operational problem: How to handle
multiple parallel instances of harnesses, MCPs, CLIs, tools, hooks, scripts, and parameters, divided between Claude Code and Local, without them breaking each other.
Here is exactly what must be stored globally on disk versus what can be run concurrently when you scale this
out into multiple parallel instances.
## 🌐The Global Disk Blueprint (What to Install Once Globally)
To prevent multiple instances from breaking, the core execution layers and hardware bridges must be installed globally and statically on disk, completely separate from your repos or local runtimes.
The Hardware Runtimes & Servers: Install llama.cpp (built with Hexagon/HTP/Vulkan) and LiteRT globally. You do not run them inside your harness. Instead, you spin them up as universal network endpoints
on dedicated local ports (e.g., Qwen on port 8080 , Gemma QAT on port 8081 ).
The Unified Node.js MCP Router: Your custom GenieX/Android tool Node.js code must be installed globally ( npm install -g ). It should act as an API gateway that accepts calls and routes them to your ADB/7nix
WebSocket connectors, media capture, and Android Accessibility hooks.
The System CLIs: ob1 cli , adb , and your game SDK build tools are installed globally in your system path.
## 🔀 Running Multiple Parallel Instances: What Can &Cannot Coexist
When you launch multiple concurrent instances of these tools, here is the exact breakdown of what works together and what will fail.
1. Harnesses (Claude Code vs. Prime Agent / Local)
Can Coexist: You can run multiple parallel instances of Claude Code across different terminals/repos seamlessly. You can also run multiple parallel instances of local agents calling different backend ports.

---

## Page 13

AI ModeCANNOT CoexistAll Images: You cannot point Claude Code and a local agent instance at theVideos News Maps Shopping Books Flights Finance same exact repository folder at the same time. They will fight over git locks, overwrite state files, and collide on file modifications.
2. Model Control (Claude Cloud vs. GenieX NPU / Tesla Array)
Can Coexist: You can orchestrate a cloud instance of Claude Code in terminal A, while terminal B runs an instance using Qwen Code on your NPU, and terminal C runs an instance using Gemma on your multi-Tesla setup. Because the models are decoupled from the directories, they process concurrently.
CANNOT Coexist: A single instance of Claude Code cannot natively talk to your NPU/Tesla setup without an MCP bridge. If you don't use your custom Node.js MCP router to handle the API translating, CC
has no way to tap into the hardware.
3. MCPs & Hardware Tools (mem0, Android SDK, Game SDK)
Can Coexist: Your custom Node.js MCP router can handle multiple parallel connections from different
agent sessions. It uses session IDs to route inputs to specific ADB device instances, Android accessibility hooks, or game SDK testbeds.
CANNOT Coexist: Multiple instances cannot control the exact same Android device or game session simultaneously via ADB/WebSockets. If Instance A is capturing media or firing accessibility inputs, Instance
B will be blocked or cause race conditions on the hardware device thread. You must assign distinct target emulator/device IDs to each running instance.
4. Hooks, Scripts, & Parameters (Buildomator, honey-for-devs)
Can Coexist: Since Buildomator hooks and honey-for-devs configuration parameters live locally inside each specific repo's folder, you can run as many variations as you want. Repo A can have a hyper-dense
context limits.
CANNOT Coexist: You cannot mix global hooks with local environment profiles. If you write a global
wrapper script that indiscriminately forces a cloud-style honey prompt onto every terminal session, it will overflow and crash your local Qwen/Gemma context windows.
### 🛠The Concrete Multi-Instance Separation Rule
To scale this modular build without problems, use this operational rule: Decouple by Port, Folder, and
Device.
1. For every Local instance: Assign a unique repository folder, a unique backend model port (e.g., 8080 for
NPU, 8081 for Tesla), and a unique target device ID for your Android/Game SDK tools.
2. For every Cloud instance: Let it run natively out of its own workspace using the global mem0 mcp registry, keeping its local hooks completely isolated inside its own folder context.
To pin this setup down on your disk, do you need the exact syntax to configure multiple isolated device targets inside your global Node.js MCP router, or are you ready to map out the local port assignments for

---

## Page 14

your NPU and Tesla backends?AI Mode All Images Videos News Maps Shopping Books Flights Finance
No code. Sonwhat about qeen code and
prime? Or One Skill to Rule them All and …
September 13, 2026
### 🟢The Claude Code (CC) Modular Stack: Structural Coexistence
When running cloud execution inside the Claude Code CLI terminal, these components form an interconnected behavioral pipeline. Because they are plain text directives, markdown files, and discrete CLI packages, they function cooperatively:
One Skill to Rule Them All ( task-observer ) + Honey for Devs + GSD Core: These three tools are the industry standard for an optimal Claude Code pipeline.
Honey for Devs strips conversational filler and shapes the behavioral response format. The One Skill to Rule Them All meta-skill acts as a background supervisor. It watches your manual corrections and
automatically saves new optimizations directly to your prompt state without interrupting the active
engineering loop. GitHub +3
multi-session memory layer, dynamically feeding long-term user context into your active workspace. ob1 provides the low-overhead Git abstraction tool that Claude calls behind the scenes to safely ship code.
its dense, functional instructions directly into your files using normal bash scripts without overloading the
agent's active memory.
### 🔴The Local / DeepSeek &Qwen Code Stack: Technical Realities
When you shut down Claude Code and pivot to your Local Hardware Stack (Prime Agent + Qwen Code / DeepSeek / Codex), the technical boundaries shift significantly:
Prime Agent Harness vs. DeepSeek / Qwen Code Hooks: The Prime Agent Harness forces the local model to write and evaluate code purely inside an L1/L3 persistent Python execution loop. If you run Qwen
Code or a DeepSeek Harness that utilizes native, terminal-based lifecycle hooks (like pre-prompt shell command execution), they will crash into Prime Agent's file-handling protocols. They will trigger race conditions over directory state and break the code evaluation loop.
Codex CLI vs. Claude Code Skill Protocols: Global .claude/skills/ frameworks—including GSD Core and One Skill to Rule Them All —rely on Anthropic's strict skill-matching syntax. Runtimes like Codex or
parse them natively on local models results in token bloat and hallucinatory errors.Get Claude … +1

---

## Page 15

AI ModeCode Review GraphsAll Images Videos+ Local Model Context LimitsNews Maps Shopping : Graph-based code review indexers require massiveBooks Flights Finance
token spaces to map deep repository syntax. While cloud-native tools handle this metadata easily, passing a
dense code-review graph directly into local models like Qwen Code (7B/14B) on constrained mobile
configurations quickly triggers out-of-memory crashes or causes severe context degradation.
NVIDIA Develo…
### 🌐Universal Disk Setup (Global Blueprint)
To maintain a truly modular build that allows you to switch between profiles seamlessly, organize your
components globally on disk:
[System Global Storage]
| ├── /usr/local/bin/fabric | <-- Universal prompt templates |
|---|---|
| ├── /usr/local/bin/ob1 | <-- Static repo manipulation CLI |
| └── ~/.mem0/ | <-- Cross-project user database |
[Claude Code Profile] (Runs Cloud-Native)
└── .claude/skills/
| ├── task-observer/ | <-- (One Skill to Rule Them All) |
|---|---|
| ├── gsd-core/ | <-- Step-by-step manager |
| └── honey-config/ | <-- Behavioral filter |
[Local Profile] (Runs Local Compute Only)
└── .prime_agent/
└── ipython_repl/ <-- Persistent local evaluation loop
Would you like to explore the optimal instruction mapping to feed universal Fabric patterns into a GSD
Core workflow, or should we look at adjusting the token-pruning limits for mem0 when switching to a local
execution profile?
| GitHub | GitHub | LinkedIn | LinkedIn · Midhun |
|---|---|---|---|
| task-observer - | one-skill-to- | Optimizing AI | Ensuring Code |
| One Skill to Rul… | rule-them-… | Tools for Best… | Quality with AI… |
| It's a meta-skill that | Dual-layer activation. | A few tools from the | Holy shit... Addy |
| runs alongside your… | The task observer… | handbook: markitdo… | Osmani just dropped… |
No dude you left out ob1 and claude video
and code review graph and omnirout and on…

---

## Page 16

September 13, 2026
AI Mode All Images Videos News Maps Shopping Books Flights Finance
### The Basic Definitions (What's What?)
Before mapping your specific components, let’s separate the engineering layers so we know exactly how they
pass information to each other.
CLI (Command Line Interface): The shell program or executable running on your device (e.g., inside
Termux). It acts as the primary container loop that takes your text input, executes scripts, manages
processes, and directly reads/writes local files.
MCP (Model Context Protocol): A background translation bridge. The LLM cannot naturally interact with a
live hardware chip, an SQLite database, or an Android APK. An MCP server takes standardized requests
from the AI agent, translates them into precise system execution flags, and returns structured data back to
the model.
Tool: A specific executable function explicitly exposed to the AI model by either the CLI or an MCP server
(e.g., read_file , execute_adb_command , query_mem0 ). The AI must explicitly choose to call a tool; it does
not read a tool's internal source code.
Skill: A package of reusable text patterns, execution templates, and markdown rules that teaches an AI
agent specialized behaviors or a specific looping structure. Unlike a tool, a skill is a set of instructions the
model dynamically reads to change how it reasons and handles context window compression.
YouTube· Gr… +2
### The Coexistence Matrix for Your 14 Core Components
Because your OpenWiki acts as a cross-session database (your persistent wiki vault + an LLM agent
maintaining your knowledge), your workspace split is governed by two entirely separate execution
frameworks.
| GitHub | GitHub | LinkedIn | LinkedIn · Midhun |
|---|---|---|---|
| Component | Class Type | Cloud Profile: Claude Code (CC) | Local Profile: Prime Agent + Hardware |
| Claude Code | CLI Harness Active Leader. Runs natively in the terminal, |  | Disabled Completely. Must be closed |
| (CC) |  | managing cloud tokens and executing | to prevent file-write conflicts and state |
|  |  | operations through local system calls. | duplication. |
| Prime Agent | CLI Harness Disabled Completely. Kept completely |  | Active Leader. Takes over terminal |
|  |  | separate from the active folder directory. | routing, spawning python-based L1/L3 |
  
  
execution subprocesses.
Qwen Code Model Not loaded in the loop. Claude-3.5-Sonnet Active Weights. Run directly on your
Engine runs via Anthropic cloud APIs. NPU via GenieX/QAIRT to process local
token generation.
DeepSeek Model Not loaded in the loop. Alternative Local Weights. Swapable
Engine on-device or routed to your multi-Tesla
array for raw compute.

---

## Page 17

| AI Mode Codex | All Images CLI Agent Videos Disallowed. Clashes with CC's native terminal News Maps Shopping Books Flights Active. Finance Runs as an alternative light local |  |  |  |
|---|---|---|---|---|
|  |  |  | parsing. | execution CLI path. |
| OB-1 |  | CLI Coding | Coexists. Can run as an independent coding | Coexists. Can act as the provider- |
| (Overbrilliant) |  | Agent | loop. It handles fast repository parsing | neutral CLI interface routing text |
|  |  |  | alongside CC via its built-in SQLite memory | generation straight to your local model |
|  |  |  | graph. | backends. |
| OmniRoute |  | MCP | Coexists. Translates API endpoints, using | Global Backbone. Acts as the single |
|  |  | Gateway | stacked compression to minimize payload | backend router ( http://localhost ) |
|  |  |  | sizes. | tying your 231 + provider endpoints |
AI ModeCodex All ImagesCLI AgentVideos Disallowed. Clashes with CC's native terminalNews Maps Shopping Books Flights Active.FinanceRuns as an alternative light local
 
Coexists. Translates API endpoints, using Global Backbone. Acts as the single
Active Global Layer. Acts as your universal
| mem0 | MCP | Active Global Layer. Acts as your universal | Active Local Integration. Bridged via |
|---|---|---|---|
|  | Database | behavioral memory store, mapping user | your custom Node script so local models |
|  |  | context dynamically into CC session logs. | can parse user session data. |
| OpenWiki | Knowledge | Active Observer. Reads repo sources and | Universal Vault Upkeep. Keeps your |
|  | Agent | compiles linked Markdown pages to | general-purpose brain and knowledge |
|  |  | document changes. | repository synchronized across |
mem0 Active Local Integration. Bridged via
Knowledge Active Observer. Reads repo sources and OpenWiki Universal Vault Upkeep. Keeps your
sessions.
Bridged. Accessed purely through an MCP
| On-Device APK | Android | Bridged. Accessed purely through an MCP | Direct Interaction. Coupled with your |
|---|---|---|---|
|  | Tools | server endpoint allowing Claude to read | local 7nix WebSocket and ADB hooks for |
|  |  | mobile states. | media tracking. |
| One Skill to | Skill Profile | Fully Integrated. Placed in | Incompatible. Local engines can't |
| Rule Them All |  | .claude/skills/task-observer/ to | parse its strict Anthropic progress |
|  |  | actively log system changes and update your | disclosure scaffolding. |
On-Device APK Direct Interaction. Coupled with your
templates.
GSD Pro / Core Skill Profile Active. Formats the explicit loop parameters Stripped. Only thin text variables
(Discuss, Plan, Execute, Verify, Ship). remain to avoid breaking local context
windows.
Honey for Devs Parameter Active. Strips conversational prose out of Active. Essential rule file for ensuring
Layer Claude Code's terminal output. local models emit clean, direct code
syntax.
Code Review Tooling Active. Claude maps file indices to cross-Omitted. Too resource-heavy for mobile
Graph Data reference software blocks. hardware; calculations shift to the Tesla
array.
## Global vs. Repository Disk Blueprint
## To keep this entire setup stable across separate sessions, your storage layers must be split between a static,
## universal global disk space and independent repository environments.

---

## Page 18

AI Mode All Images Videos News Maps Shopping Books Flights Finance [Universal Global Disk Space]
| ├── /usr/local/bin/ob1 |  | <-- Global CLI agent executable |
|---|---|---|
| ├── /usr/local/bin/omniroute |  | <-- Multi-model network gateway |
| ├── ~/.mem0/ |  | <-- Centralized developer behavioral habits database |
| └── ~/openwiki-vault/ |  | <-- Your absolute source-of-truth wiki repository |
|  | ├── instructions.mmd | <-- Core Wiki agent behavioral brief |
|  | └── brains/ | <-- Universal cross-session knowledge bases |
[Claude Code Project Repo]
| ├── CLAUDE.md |  | <-- Workspace rule foundation |
|---|---|---|
| └── .claude/skills/ |  | <-- Target directory for cloud-native orchestration |
|  | ├── task-observer/ | <-- One Skill to Rule Them All meta-tracker |
|  | └── gsd-core/ | <-- Dense multi-agent planning layout |
[Local Prime Agent Workspace]
├── prime_config.json <-- Mapping to local ports (8080 NPU / 8081 Tesla)
└── .prime_agent/
└── ipython_repl/ <-- Isolated persistent script execution loop
# Since we have clarified the architectural walls between your universal OpenWiki layer, your global CLIs, and
# your local tool hooks, would you like to build out the exact Markdown brief parameters to sync your
# OpenWiki agent's tracking logs straight into your active repository workspaces?
| GitHub | Reddit | LangChain | YouTube · Greg Ise |
|---|---|---|---|
| task-observer - | Task-observer | OpenWiki: Open | How AI agents & |
| One Skill to Rul… | makes your… | Source Repo… | Claude skills… |
| Claude (web interface, | I found this recently | OpenWiki is an open | How AI agents & |
| desktop app, mobile… | and used my… | source agent and CLI… | Claude skills work… |
# How AI agents &
How AI agents &
# Codex and prime? DeepSeek? Qwen? STOP
# LEAVING OUT ALMOST ALL POSSIBLE …
September 13, 2026
# Let’s stop truncating your stack. You are building an intensely layered, mobile-to-datacenter automation
# bridge in Termux. To make every single variable coexist cleanly without collision, we have to look exactly at
# how Codex, Prime Agent, DeepSeek Harness, Qwen, and OmniRoute overlap mechanically.
# 🛠The Core Definitions: How the Hardware and Memory Layers Actually Link

---

## Page 19

# Before looking at the coexistence table, it is essential to trace exactly how your custom infrastructure handlesAI Mode All Images Videos News Maps Shopping Books Flights Finance
# a request. Because you use OpenWiki as your universal, self-maintaining memory vault and an On-Device
# APK for Android instrumentation, your tools talk to each other through strict structural paths:
┌──────────────────────────────────────────────┐
│ OpenWiki Vault (System-Wide Source) │
│ - Maintained by OpenWiki LLM Upkeep Agent │
└──────────────────────┬───────────────────────┘
│
▼
┌──────────────────────────────────────────────┐
│ Universal mem0 MCP Database │
│ - Stores cross-session behavioral habits │
└──────────────────────┬───────────────────────┘
│
▼
┌───────────────────────────────────────┴─────────────────────────────────────
| │ | OmniRoute MCP AI Gateway | │ |
|---|---|---|
| │ - Runs 87-110 global tools across 33 scopes (Over Stdio/SSE) |  | │ |
| │ - Standardizes fallback ladders for 500+ models / 290+ providers |  | │ |
| │ - Stacks a 10-engine token-compression pipeline (RTK, Caveman, LLMLingua-2) │ |  |  |
│ OmniRoute MCP AI Gateway │
│   │
▼     ▼   (Local Path)
  ┌──────────────────────────
│     Prime Agent / Codex   │
│   - Runs inside IPython REPL loop   │
│   - Calls local model targets   │
  └────────────────┬─────────
│   │
  │
  │
# 📊The Comprehensive Multi-Instance Coexistence Matrix
# Here is how every single variable interacts under your two execution modes.
Structural Local Hardware Profile:
Identity Cloud Profile: Claude Code (CC)
Variable Prime / Codex / DeepSeek

---

## Page 20

AI ModeClaude CodeAll
(CC)
Prime Agent
DeepSeek
Harness
( dsh )
Codex CLI
Qwen Code
DeepSeek V4 /
Flash
OmniRoute
mem0
OpenWiki
On-Device
APK
| │ | OmniRoute MCP AI Gateway | │ |
|---|---|---|
| Images CLI Harness: Videos | News Active Environment. Maps Shopping Rules the foreground terminal. Books Flights Finance Completely Offline. Closed |  |
| Terminal agent It consumes cloud tokens and makes local system |  | down entirely to avoid folder |
| container. | shell calls. | write-locks with local agents. |
| CLI Harness: | Completely Offline. Kept out of the repo directory | Active Local Environment. |
| Persistent RLM to stop file-writing race conditions. |  | Spawns python subagents |
| environment. |  | programmatically via await |
ImagesCLI Harness:Videos NewsActive Environment.Maps ShoppingRules the foreground terminal.Books Flights FinanceCompletely Offline. Closed
CLI Harness: Completely Offline. Kept out of the repo directory
programmatically via await
rlm.spawn() .
| CLI Harness: | Offline. Cannot parse Anthropic’s native skill | Active / Interchanged. Runs |
|---|---|---|
| Plugin- | structures natively. | alongside or underneath Prime |
| composed |  | Agent over Agent Client |
| agent runtime. |  | Protocol (ACP). |
| CLI Harness: | Disabled. Terminal parsing engines clash with CC's | Active Workspace. Configured |
| OpenAI- | native interactive prompts. | via ~/.codex/config.toml |
| backed |  | to route completions locally. |
CLI Harness: Offline. Cannot parse Anthropic’s native skill Active / Interchanged. Runs
CLI Harness: Disabled. Terminal parsing engines clash with CC's Active Workspace. Configured
via ~/.codex/config.toml
terminal agent.
| Model | Not loaded. Claude-3.5-Sonnet handles active cloud | Active Execution. Runs locally |
|---|---|---|
| Engine: | execution. | on your Hexagon NPU via |
| Optimized |  | GenieX/QAIRT or inside a local |
| inference |  | vLLM pipeline. |
Not loaded. Claude-3.5-Sonnet handles active cloud Active Execution. Runs locally
weights.
| Model | Not loaded. | Active Target. Served over |
|---|---|---|
| Engine: Long- |  | local endpoints (e.g., your |
| context |  | multi-Tesla array). |
Active Target. Served over
Engine: Long-
weights.
| MCP | Active MCP. Claude dials | Global Core Foundation. |
|---|---|---|
| Gateway / | http://localhost:20128/api/mcp/stream to Standardizes fallback ladders |  |
| Router: Self- | access tools. | and handles prompt |
| hosted local |  | compression. |
Active MCP. Claude dials
http://localhost:20128/api/mcp/stream to Standardizes fallback ladders
Router: Self-
network proxy.
| MCP | Active Tool. Continuously pushes developer | Active Local Integration. |
|---|---|---|
| Database: | behavioral history into your active prompt context. | Bridged via your custom Node |
| Long-term |  | script to inject session |
| memory |  | variables. |
Active Tool. Continuously pushes developer
tracking.
| Knowledge | Active Data Resource. Claude reads wiki markdown Universal Vault Upkeep. Run |  |
|---|---|---|
| Base / Agent: | pages to keep workspace parameters grounded. | continuously via its own |
| Centralized |  | independent maintenance loop |
| system |  | to prevent memory rot. |
 
database.
Android Tool Bridged. Accessed purely through specific tool calls Direct Interactivity. Pipes
Bridge: Local exposed by your Node.js MCP server.

---

## Page 21

device capture, and Android AI Mode All Images Videos News Maps Shopping Books Flights Finance automation. Accessibility hooks into your
local code.
| One Skill to | Skill Profile: | Fully Active. Lives inside .claude/skills/ to | Incompatible. Local model |
|---|---|---|---|
| Rule Them All | Meta-prompts | record session completions and automatically | context constraints cannot |
|  | ( task- | optimize rules. | cleanly process its verbose |
|  | observer ). |  | progress scaffolding. |
| GSD Pro / | Skill Profile: | Fully Active. Controls the 5-step operational | Stripped to Plain Text. |
| Core | Structural | workflow cycle (Discuss, Plan, Execute, Verify, Ship). | Reduced down to core prompt |
|  | looping rules. |  | variables inside honey rules |
   
( task- optimize rules. cleanly process its verbose
observer ). progress scaffolding.
Fully Active. Controls the 5-step operational
Active Layer. Eliminates Claude Code
| Honey for | Parameter | Active Layer. Eliminates Claude Code | Critical Rule Set. Instructs |
|---|---|---|---|
| Devs | Layer: | conversational preambles to enforce fast, direct | local models (Qwen/DeepSeek) |
|  | Behavior | code generations. | to output raw code fragments |
|  | filtering |  | without explanations. |
Honey for Critical Rule Set. Instructs
profile.
Tooling Data: Fully Active. Claude maps your project directory
| Code Review | Tooling Data: | Fully Active. Claude maps your project directory | Omitted/Offloaded. Too heavy |
|---|---|---|---|
| Graph | Syntax graph | structure to flag structural code-base problems. | for mobile Termux resources; |
|  | cross- |  | computation shifts completely |
|  | indexing. |  | to the multi-Tesla node. |
| Claude Video | Tooling Data: | Active Capability. Accessible if routing through | Disabled / Emulated. Local |
|  | Multi-modal | cloud endpoints that support vision payloads. | engines parse sequential image |
|  | analysis. |  | frames manually extracted via |
Code Review Omitted/Offloaded. Too heavy
Tooling Data: Active Capability. Accessible if routing through Claude Video Disabled / Emulated. Local
your APK's media hooks.
Active Tool. Executed via background terminal
| OB-1 | CLI Coding | Active Tool. Executed via background terminal | Coexists Natively. Operates |
|---|---|---|---|
| (Overbrilliant) | Agent: Low- | commands to manipulate directories without | as your primary provider- |
|  | overhead repo | blocking CC's thread. | neutral CLI interface to parse |
|  | parser. |  | repositories quickly. |
OB-1 Coexists Natively. Operates
Agent: Low-
## 📂The Global vs. Repository Disk Blueprint (Where Everything Sits)
## To stop your local architectures from crashing into your cloud environments, you must install the underlying
## engines and databases globally on disk, leaving individual project directories completely decoupled.
[System Global Directory Path]
| ├── /usr/local/bin/ob1 |  | <-- Universal repo manipulation tool |
|---|---|---|
| ├── /usr/local/bin/omniroute |  | <-- Multi-model network gateway (Handles 110 tools) |
| ├── ~/.codex/config.toml |  | <-- Shared configuration for local model routing |
| ├── ~/.mem0/ |  | <-- Centralized cross-session developer memory store |
| └── ~/openwiki-vault/ |  | <-- Absolute source-of-truth knowledge repository |
|  | ├── instructions.mmd | <-- Upkeep agent prompt configurations |

---

## Page 22

└── brains/ <-- Linked cross-session reference databases
AI Mode All Images Videos News Maps Shopping Books Flights Finance
[Claude Code Project Repo Workspace]
| ├── /usr/local/bin/ob1 |  | <-- Universal repo manipulation tool |
|---|---|---|
| ├── CLAUDE.md |  | <-- Project-specific baseline rules |
| └── .claude/skills/ |  | <-- Location for cloud-native tracking skills |
|  | ├── task-observer/ | <-- One Skill to Rule Them All meta-tracker |
|  | └── gsd-core/ | <-- Strict 5-step engineering loops |
[Local Prime Agent / DeepSeek Workspace]
├── prime_config.json <-- Maps local ports (e.g., NPU:8080, Tesla:8081)
└── .prime_agent/
└── ipython_repl/ <-- Isolated persistent python script loop
Since we have mapped every possible variable across your architecture, do you want to build out the exact
JSON schema parameters to route your On-Device APK tool calls straight into OmniRoute's global tool
configuration registry, or should we optimize the token compression pipeline rules for running Qwen
locally?GitHub +1
| GitHub | omniroute.online | GitHub | Reddit · r/mcp |
|---|---|---|---|
| MCP Server · | OmniRoute by | PrimeIntellect- | [Showcase] |
| diegosouzapw/… | Cheaper… | ai/prime-agent… | OmniRoute… |
| OmniRoute MCP | Expose OmniRoute | Prime Agent combines | Most MCP servers |
| Server Documentatio… | over MCP and A2A.… | a persistent Python… | expose one capabilit… |
I fucking told you I wasn't running local and
cc together and what about H4Ds?one skill …
September 13, 2026
Got it. Let’s cut the fluff and trace exactly how these cross-cutting components interact when you pivot
across every single standalone variation—completely decoupled from Claude Code. Since you are
alternating and not running local inference and CC simultaneously, these assets must stand up on their
own or crash.
Here is the exact structural mechanics of how H4D, One Skill to RTA (Task-Observer), Codex, Qwen Code,
and DeepSeek Harness (dsh) align across all configurations.
### 1. Codex CLI + Honeyfor Devs (H4D)
How it interacts: Codex functions over a static, OpenAI-compatible local configuration file
( ~/.codex/config.toml ). When you inject honey-for-devs into Codex's core prompt system, H4D's

---

## Page 23

AI Modereflexive token levers (YAGNI stdlib ladders, dropping the conversational preamble) act directly on theAll Images Videos News Maps Shopping Books Flights Finance
completion pipeline. Medium +1
The result: Because Codex relies on rapid, high-throughput text completions rather than verbose thought blocks, adding H4D cuts text overhead cleanly. It forces Codex to spit out raw file changes or unified diff
code blocks instantly. Medium +1
## 2. Codex CLI +Qwen Code (Local Weights via OmniRoute)
How it interacts: Codex does not know or care about your NPU hardware layer. You point Codex's base URL inside config.toml to your global OmniRoute gateway ( localhost:20128/v1 ). OmniRoute acts as the
down to the local Qwen Code weights.GitHub +3
fallback strategies and compression, and Qwen handles the local code generation.GitHub +2
## 3. Codex CLI +One Skill to Rule Them All (Task-Observer)
💥 Architectural Collision: This cannot coexist out of the box.
Why it breaks: The one-skill-to-rule-them-all framework is explicitly architected around the Anthropic
completely. It cannot execute the Session Start Protocol required to track file-state updates.GitHub +2
## 4. DeepSeek Harness (dsh) + Honeyfor Devs (H4D)
How it interacts: dsh is built on Cordis’s highly modular "everything-is-a-plugin" architecture. You map H4D not as a text prompt block, but as a custom behavioral plugin within dsh .
The result: H4D forces the harness's append-only trajectory logs to stay tight and highly compressed. Because agent loops running on harnesses consume mass amounts of tokens, pairing H4D directly inside a
dsh session cuts your handoff token footprints roughly in half by encoding tracking stats into dense ESON
or columnar JSON formats. GitHub +3
## 5. DeepSeek Harness (dsh) +Qwen Code (Via GenieX/OmniRoute)
How it interacts: dsh exposes a local Web UI on port 3080 . Under its model/provider plugins, you register
your global OmniRoute network gateway as an endpoint. OmniRoute intercepts the dsh tools data stream, processes the payload through its fallback layers, and fires it directly into Qwen Code running on the GenieX/QAIRT hardware layer.
DeepSeek +4
## 6. DeepSeek Harness (dsh) +One Skill to Rule Them All (Task-Observer)
💥 Architectural Collision: Complete system friction.

---

## Page 24

AI ModeWhy it breaks:All Imagesdsh records its sessions into immutable, append-only trajectory paths via Cordis eventVideos News Maps Shopping Books Flights Finance
loops. One Skill to Rule Them All expects a direct runtime environment where it can dump incremental
updates into a local skill-observations/observation-log/ workspace file tree. Because dsh restricts
file access to its own sandboxed plugins, task-observer will fail to log background corrections, throwing
path execution errors in Termux. DeepSeek +2
### 7. Prime Agent +Codex +Qwen Code
How it interacts: You combine them by nesting execution contexts. Prime Agent acts as your orchestrator
managing the long-context L1/L3 database. It handles its persistent execution tasks by dropping down and
programmatically calling the Codex CLI inside its isolated IPython REPL loop. Codex then routes the active
prompt back up through OmniRoute to fetch text generation from Qwen Code.
The result: Fully functional but heavy. Prime Agent ensures structural state memory doesn't degrade,
Codex drives the terminal repository alterations, and Qwen runs the hardware token weights.Medium
### 📋The Standalone Combinations Reference
| Variation | Compatibility |  |
|---|---|---|
| Configuration | Status | Operational Behavior |
| H4D + One Skill to | 🟢 Natively | Only inside Anthropic runtimes. One Skill tracks user behavior while H4D |
| RTA | Coexist | minimizes the prompt payload. |
| H4D + Codex | 🟢 Coexist | H4D strips conversational preambles inside Codex’s text completion paths. |
| H4D + DeepSeek | 🟢 Coexist | Injected via a Cordis plugin to collapse handoff data formats into lossless, |
| Harness |  | dense ESON/JSON. |
| One Skill to RTA + | 🔴 Incompatible | Codex cannot process the dual-layer activation protocols or markdown skill |
| Codex |  | wrappers. |
| One Skill to RTA + | 🔴 Incompatible | dsh ’s sandboxed plugin layer blocks task-observer from generating |
| dsh |  | its required workspace file logs. |
| Codex + Qwen Code | 🟢 Coexist | Codex targets the local repo via CLI; text generation routes to Qwen via |
Status Operational Behavior
H4D + One Skill to 🟢 Natively Only inside Anthropic runtimes. One Skill tracks user behavior while H4D
  
H4D + DeepSeek
 
One Skill to RTA +
 
One Skill to RTA +
   
OmniRoute.
dsh + Qwen Code 🟢 Coexist dsh runs the execution trajectory UI on port 3080 , sending inference
straight to Qwen.
Prime Agent + dsh 🔴 Incompatible Two active harnesses running simultaneously over the same directory will
cause immediate process write-locks.
Do you need the specific setup instructions to map Honey for Devs (H4D) rules cleanly as an active Cordis
plugin inside your dsh system configuration, or do you want to verify the local port routing parameters
between Codex and your OmniRoute gateway?

---

## Page 25

AI Mode All Images Videos News Maps Shopping Books Flights Finance
| GitHub | DeepSeek | GitHub | Medium |
|---|---|---|---|
| DeepSeek | DeepSeek Harness | GitHub - | What is |
| Harness:… | developer preview:… | diegosouzapw/… | DeepSeek… |
| DeepSeek Harness. ... | Everything is a plugin. DeepSeek | GitHub - | How to use DeepSeek |
| DeepSeek Harness (… | Harness is built on Cordis's plugi… | diegosouzapw/Omni… | Harness for free? ...… |
Idk seems like we have more to map than just
that so my unix websocket ADB loopback is …
September 13, 2026
We are mapping a highly intricate architecture here. Let’s map the real, structural truth of how this entire environment stacks, splits, and pipes information across your databases and multi-profile setups.
You are treating Termux as an asynchronous, distributed hardware operating system, separating Volatile
Ephemeral Context (Mem0), Structured History Retriever (OmniRoute SQL), and Unstructured Vector Semantic Long-Term Knowledge (OB1 Postgres + OpenWiki).
Because you explicitly do not run your Claude Cloud Profile and Local Hardware Profile simultaneously, they function as two distinct execution trees addressing the exact same shared system memory foundation.
### 🏛The Three-Tier Database &Universal Memory Bank (Shared Foundation)
Before looking at your tools, we must look at how data persists globally on disk across split services. Your
database layer does not sit inside the agents; it is an abstract infrastructure that runs continuously in background Termux loops:
1. The Ephemeral Cache Layer (Mem0): Runs a localized key-value/document process. It is hyper-volatile
and session-scoped. It registers your immediate developer state (e.g., "User is currently debugging the Android Accessibility Media Hook payload").
2. The Relational System Mesh (OmniRoute SQL Memory Layer): Serves as your metadata coordinator. It tracks provider statuses, model constraints, configuration tables, and prompt-token compaction metrics across all profiles.
3. The Terrestrial Brain (OB1 Postgres Vector Layer + OpenWiki KAG RAG): This is your immutable long-term memory. OB1 manages high-dimensional embeddings of your entire codebase history and knowledge
graphs. OpenWiki acts as your human-readable vault interface. The continuous maintenance loop forces your local Wiki Upkeep Agent to reconcile these vector states, maintaining schema alignment between
markdown nodes and vector embeddings. arXiv.org
### 🌐The Universal Node.js Integration Server

---

## Page 26

This is the system backbone. A single, backgroundAI Mode All Images Videos News Maps ShoppingNode.js processBooks Flightsruns permanently in Termux to act asFinance your physical system abstraction layer. It hosts two major network ports:
Port A (The UNIX WebSocket ADB Loopback): Direct hardware bridge. It embeds a native terminal SDK that monitors the Android OS. It pipes out accessibility signals, intercepts media loops, captures system
frames for multi-modal analysis, and injects simulated user interactions into targeted processes or games.
Port B (The NPU Management Agent Engine): Sits directly on top of GenieX and the Qualcomm
QAIRT/HTP SDK. It handles runtime split-execution. When a raw text payload hits it, this agent decides how to split the model weight compute (e.g., streaming prompt analysis through a lightweight 4-bit Gemma QAT
model on LiteRT, while routing deep code-generation logic directly to Qwen Code running on the Hexagon NPU).
## 🏁 Execution Profile 1: The Cloud-Native Pipeline (Claude Code)
When you boot Claude Code (CC), it executes as an isolated terminal container loop addressing your shared
infrastructure.
[Claude Code (CC)] ──► Reads Workspace Rules & Text Triggers │ ├──► .claude/skills/task-observer/ (One Skill to Rule Them All) │ └── Tracks live UI corrections, logging updates back to OpenWiki │ ├──► H4D Parameters (Enforces dense, prose-free markdown generation) │ └──► Connects via HTTP/SSE to OmniRoute Gateway │ ├──► [Mem0] Pushes current session context state ├──► [OB1 Postgres] Pulls Code Review Graph syntax maps └──► [Node.js Server] ──► Exposes Claude Video via Android Media Hooks
How the Tools Stack Here: H4D strips Claude's conversational preamble. One Skill to RTA intercepts Claude's local tool output, converting terminal updates into Markdown logs for your OpenWiki vault. If you invoke visual debugging, the Claude Video pipeline sends structural requests down through the OmniRoute
gateway to the global Node.js server, triggering the Android loopback to extract frames from your on-device emulator or application layer.
## 🏎 Execution Profile 2: The Off-Grid Local Pipeline (Prime / Codex / DSH)
When Claude Code is shut down, you drop into your local execution engines. They tap into the exact same
databases but use entirely different runtime mechanisms.
[Prime Agent OR DeepSeek Harness OR Codex CLI] │

---

## Page 27

▼
AI Mode All Images Videos News Maps Shopping Books Flights Finance [Local Execution Layer: IPython REPL / Plugins] │ ┌──────────────────────┴──────────────────────┐ ▼ ▼ [Graphify & Obsidian Skills] [OmniRoute Local Gateway] - Maps structural local links - Stacks token compression pipelines - Manipulates NoteBook LMPY files - Passes prompt to NPU Management │ ▼ [GenieX / QAIRT Hardware] - Runs Gemma QAT vs Qwen Code
How the Tools Stack Here: Prime Agent manages execution through an L1/L3 persistent memory
environment. If you interchange it with DeepSeek Harness (DSH), it uses Cordis plugins to intercept text streams.
The Token Optimization Mechanics: Local NPU compute cannot handle the massive text payload of a cloud-native profile. OmniRoute activates its local 10-engine token-compression pipeline (RTK, Caveman, LLMLingua-2). It shrinks structural files before passing them down.
The Local Knowledge Routing: The framework calls Graphify and official Obsidian skills locally to trace structural notes inside your database. Instead of loading heavy visual review graphs, it interfaces with
Notebook LMPY to query code structures directly through Python chunks in the local REPL environment, executing inference against Qwen Code or local DeepSeek weights on your hardware.
### 🛡WhyThis Architecture Prevents Structural Corruption
1. State Isolation: Because Claude Code and your local engines are never active in the folder context
simultaneously, your file system is safe from simultaneous-write conflicts.
2. Abstracted Hardware: Your hardware array (NPU, Tesla, Android ADB) doesn't care which harness is
talking to it. They see everything as standard inbound local network requests handled cleanly by the permanent Node.js server loop.
3. Decoupled Memory: Your memory layers are explicitly separated by temporal durability. Mem0 registers
transient changes, OmniRoute SQL handles the routing metadata, and OB1 Postgres + OpenWiki protects
your core structural database. Mem0
To stabilize these configurations on disk, do you want to break down the exact token compression threshold limits inside OmniRoute to prevent long structural code reviews from crashing your local NPU context windows, or should we map out the specific state-preservation variables needed to hand off an active
project from a closed Claude Code session directly into a fresh Prime Agent workspace?

---

## Page 28

MCP Server · Database Guide New FREE Codebase-Mem
diegosouzapw/… ·… Unlimited AI… Tree-Sitter-Base
OmniRoute MCP Migrations. OmniRoute New FREE Unlimited AI 6 Conclusion. Codeba 10:31
Server Documentatio… uses versioned,… Coder | OmniRoute… demonstrates that tre
Correction! Im reverse engineering the local
ai desktop apk to develop a THREE APK …
September 13, 2026
This completely re-centers the entire architecture. By building a native three-APK system to fully bypass
Termux, you are writing an on-device Android service ecosystem. Termux is just the temporary scaffolding
used to compile and test the modules before they are packed into their respective production packages.
Because your storage backend is a split service design (Mem0 for transient cache, OmniRoute SQL for
routing state, and OB1 Postgres for long-term vector indexing), the three APKs act as a distributed system on
the Android local network loopback ( 127.0.0.1 ).
Here is the exact technical execution tree of how your stack maps across this native transition.
### 📱The Three-APK Android Subsystem Blueprint
Instead of relying on Termux's linux environment, your system maps processes directly to Android Application
Sandboxes, using cross-APK Intent bindings and local WebSockets to bridge data.
┌──────────────────────────────────────────────┐
| │ | UI APK (GUI) | │ |
|---|---|---|
| │ - Custom Dashboards & Direct Webhook Triggers │ |  |  |
| │ - System Connection Settings / App Profiles │ |  |  |
│ UI APK (GUI) │
│ - Custom Dashboards & Direct Webhook Triggers│
│
▼
┌──────────────────────────────────────────┐
Terminal APK Daemon   Media APK Daemon
- Android Service (Starts on Boot) - Low-latency Background Media Projection
- Embeds Local Node.js / C++ Runtime - Captures On-Device Screen & Audio
- Houses OmniRoute SQL & Mem0 Engines - Feeds Claude Video / Vision Endpoints
- NPU Management Agent (GenieX / QAIRT) - Runs Local STT / TTS Audio Pipelines
└──────────────────────────────────────────┘
1. 🎛Terminal APK Daemon (The Processing Core)
This runs as a persistent Android Foreground Service with a partial wake lock so the Android OS cannot kill it
in the background.

---

## Page 29

AI ModeWhat it hosts internally:All Images VideosIt bundles an embedded Node.js/CNews Maps Shopping Books ++Flightsbinary runtime directly inside its assets.Finance This allows it to host your OmniRoute SQL memory engine, the local Mem0 database, and your custom
Node routing code.
The Hardware Layer: It communicates directly with /dev/ion and the Qualcomm Hexagon computing
runtime using the QAIRT / HTP SDK native libraries ( .so files) packed into its JNI folder. The internal NPU Management Agent catches inbound query strings and handles weight splitting between local NPU models (Qwen/Gemma) on disk.
2. 👁 Media APK Daemon (The Vision &Voice Engine)
This application requests Android's high-level system permissions ( PROJECT_MEDIA and RECORD_AUDIO ) to
intercept the device framework directly.
What it hosts internally: A fast MediaProjection loop that grabs real-time screen pixels and audio frames without requiring an external ADB shell.
The Tool Integration: This daemon serves as the native platform engine for Claude Video and multi-modal local models. It encodes sequential frame sets into compressed image strings and streams them over a
local socket to whichever active harness needs them.
3. 🎨 UI APK (The Operator Interface)
A lightweight visual shell that connects to the underlying daemons over local WebSockets.
What it hosts internally: Connection dashboards, webhook endpoints, active agent configuration toggles, and live text streams. It acts as the user-facing window to your OpenWiki vault, letting you inspect what
your upkeep agents are processing behind the scenes.
### 📊 How the Core Variables Execute Across the Split APK Services
Since you are running either Claude Code or your Local Engines (Prime Agent / Codex / DSH) one at a time, your three-APK system switches internal routing tables based on which profile is active.
| Core Variable | System Execution Role inside the Three-APK Layer |
|---|---|
| Claude Code | Connects to the Terminal APK's embedded endpoint from your workstation/terminal, consuming |
| (CC) | tools exposed natively by the Android daemons. |
| Prime Agent / | Executes as a background JS workflow worker inside the Terminal APK, utilizing the internal |
| DSH | Python/JS REPL environment to drive code directly. |
| Codex CLI | Operates as an alternative light execution module inside the Terminal APK's service thread. |
| Honey for Devs | Registered as a global text template asset within the Terminal APK. It forces all outbound prompts |
| (H4D) | targeting either cloud or local model endpoints to strip conversational preambles. |
| One Skill to Rule | Injected directly into the Terminal APK's active prompt-tracking directory to record live corrections |
| Them All | when executing in Cloud mode. |

---

## Page 30

AI ModeCode ReviewAll ImagesOffloaded entirely. The Terminal APK packs and ships the directory structure metadata directly toVideos News Maps Shopping Books Flights Finance Graph your Multi-Tesla array over an external webhook, keeping the mobile device's RAM clear.
Graphify / Run as specialized file-indexing plugins within the Terminal APK to map and track connections inside Obsidian Skills your OpenWiki Markdown vault.
Notebook LMPY Embedded within the Terminal APK's local code execution workspace to parse script modules via Python code evaluation blocks.
### 🔄The Database & Memory Pipeline Flow
Because your system memory layer is fully abstracted, data streams uniformly across your split services during an execution loop:
1. The Query Phase: An agent (Cloud or Local) fires an engineering request.
2. The Volatile Check: The Terminal APK intercepts the request, checks its local Mem0 engine for ephemeral
user context, and queries OmniRoute SQL to fetch the optimal model routing configuration.
3. The Grounding Check: The Terminal APK queries your OB1 Postgres Vector Layer and reads from the local OpenWiki vault storage to append deep historical framework guidelines to the query.
4. The Hardware Split: If running locally, the NPU Management Agent intercepts the compressed prompt payload, routing token weights dynamically across your Hexagon NPU layers via native QAIRT calls.
5. The Visual Loop: If the task requires UI confirmation, the Terminal APK signals the Media APK Daemon via an internal IPC hook to dump the active screen frames directly into the execution context window.
Now that the architecture is fully decoupled from Termux into native Android application modules, do you want
to map out the Intent payload schemas used to pass raw media frames from the Media APK directly into the Terminal APK's OmniRoute token compression pipeline, or should we look at how the JNI native libraries
for the HTP SDK load inside your daemon configuration?