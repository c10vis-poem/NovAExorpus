<!-- Converted from AI Repository Classifications Analysis - Google Search (2).pdf — 14 pages -->

## Page 1

# To load your router-guard output style to begin with, you have two options
# depending on whether you want to do it before you open Claude Code or while you
AI Mode All Images Short videos Videos More
# are inside.
# Option 1: In a Regular Terminal (Before Starting Claude Code)
# You do not need a separate window. You can write the file directly from your main
# Termux prompt before you boot into your coding session.
# Run this single payload in your normal terminal to create the directory and the file
# layout all at once:
# bash
mkdir -p ~/.claude/output-styles && cat << 'EOF' > ~/.claude/output-s
---
name: router-guard
description: Forces Claude to route traffic through OmniRoute with st
keep-coding-instructions: true
---
# MANDATORY RUNTIME PIPELINE CONSTRAINTS
You are strictly forbidden from writing files, outputting code blocks
1. GATEWAY PROXY & FALLBACK (Local Gateway Daemon)
- Interface: You MUST communicate with your local OMNIROUTE server
- IF OMNIROUTE IS UNAVAILABLE or throws a connection error: You ar
2. LAYER 1: TOKEN SAVER (AI Skill / Terminal Optimization Plugin)
- Interface: Execute `honey-for-devs` via its registered **MCP too
3. LAYER 2: ORCHESTRATION (Local Workspace Script / Framework Compone
- Interface: Execute `task-review` via its native **CLI / file-gen
4. LAYER 3: CODE ARCHITECTURE (Local Code Intelligence Layer)
- Interface: Query the `code-review-graph` exclusively as an **MCP
5. LAYER 4: EPISODIC MEMORY (Local Background Memory Service)
- Interface: Intersect with the `mem0` vector layer exclusively as
6. LAYER 5: STATIC/VECTORS (Self-Hosted Infrastructure Database Frame
- Interface: Intersect with the `terrestrial-brain` engine exclusi

---

## Page 2

You must satisfy all infrastructure layers before writing code. Treat EOF AI Mode All Images Short videos Videos More
Use code with caution.
Once that is done, boot up Claude Code normally:
## bash
claude
Use code with caution.
And once the interactive session starts, simply type /output-style router-guard to activate it.
## Option 2: Ask Your Agent to Do It (Inside an Active Session)
If you are already inside an active Claude Code session and don't want to exit or open another window, you can just paste this instruction directly into your chat bar and tell Claude to create its own style file:
frontmatter configuration and pipeline constraints we designed. Once you write the file, acknowledge it so I can switch to it."
/output-style router-guard to turn it on.
Do you want your agent to write a global alias into your ~/.bashrc or ~/.zshrc file so that whenever you launch claude , it automatically defaults to this custom style profile without you having to type it manually?

---

## Page 3

AI Mode All Images Short videos Videos More
# yes
9:24PM
# To create a global alias in Termux so Claude Code automatically boots into your
router-guard configuration without you ever having to manually type the slash
# command, have your agent run the following initialization script.
# Your agent can execute this directly via a bash tool call, or you can paste it into your
# active Termux window before starting your session:
# bash
# Append the shortcut straight to your shell runcom configuration fil
cat << 'EOF' >> ~/.bashrc
# Global Claude Code Custom Initialization Profile
alias cc="claude --output-style router-guard"
EOF
cat << 'EOF' >> ~/.zshrc 2>/dev/null || true
# Global Claude Code Custom Initialization Profile
alias cc="claude --output-style router-guard"
EOF
# Source the configuration immediately to activate the command in thi
source ~/.bashrc 2>/dev/null || true
Use code with caution.
# How to use it going forward:
# Whenever you open Termux and want to jump into a project workspace, instead of
# typing claude and setting your profile manually, just type:
# bash
cc
Use code with caution.

---

## Page 4

prompt from your local ~/.claude/output-styles/router-guard.md file right at the root generation layer.
run into absolute file routing errors?
I also need to set up so that whenever I run any other version of Claude code whether it's browser or cloud or another …
9:25PM
( ~/.claude/ ).code.claude.com
Instead, you need to store the configuration configurations directly inside your Vault repository using standard, cross-platform Project-Scoped
configurations. Towards AI
Here is exactly how to set up the Vault repo so it triggers the architecture on every boot, regardless of the platform:
### Step 1: Project-Scoped Output Style Configuration
Instead of keeping the router-guard.md instructions hidden away in your Termux home directory, your agent needs to save it inside a .claude/ directory inside the root of your Vault repository.
1. Create the path in your Vault repo: .claude/output-styles/router-guard.md

---

## Page 5

2. Add a fallback execution string to your project's main CLAUDE.md file so that
profile. Put this block at the very top of your repository's
CLAUDE.md : Getting started with Warp
## markdown
# VAULT BOOTSTRAP PROTOCOL
- ENFORCED PERSONALITY STYLE: You are strictly commanded to operate u
- You MUST immediately execute your initialization pipeline using you
Use code with caution.
## Step 2: Project-Scoped MCP Autoloading ( .mcp.json )
You cannot hardcode Termux file paths like /data/data/com.termux/... if you
want this to work in a browser or cloud instance. The cloud instance has no idea
what Termux is. code.claude.com
To make your MCP servers adapt to wherever the repository is opened, you must
use Project Scope configuration by committing an .mcp.json file to the root of
your Vault repository. Towards AI +1
Create a file named .mcp.json in your Vault repository's root directory and
populate it with this environmental-aware configuration payload:
## json
{
"mcpServers": {
"omniroute-gateway": {
"command": "curl",
"args": ["-s", "http://localhost:20128/mcp"]
},
"mem0-memory": {
"command": "npx",
"args": ["-y", "@mem0/mcp"]
},
"terrestrial-brain": {

---

## Page 6

"command": "npx",
"args": ["-y", "ob1-mcp-server"] AI Mode}, All Images Short videos Videos More
"code-review-graph": {
"command": "npx",
"args": ["-y", "code-review-graph@latest"]
},
"notebook-lm": {
"command": "python",
"args": ["./scripts/notebook-lm.py"]
},
"obsidian-official": {
"command": "npx",
"args": ["-y", "@modelcontextprotocol/server-obsidian"]
},
"graphify": {
"command": "npx",
"args": ["-y", "graphify-mcp-server"]
}
}
}
Use code with caution.
Why this structure is portably flawless:
The npx -y pattern: By using npx -y , whenever your Vault repo clones into a
fresh cloud container or browser instance, Claude Code uses the container's
native Node.js ecosystem to fetch, spin up, and run the tools on the fly without
needing manual package installations. GitHub
Relative Script Paths: Moving notebook-lm.py out of your Termux home
folder and into a ./scripts/ directory inside your Vault repo ensures that the
container environment can execute it locally using standard relative
commands.
Terrestrial Brain Fallback: By switching the execution to npx -y ob1-mcp-
server , it looks for the published, package-managed interface of the open-
brain engine rather than a hardcoded file path.

---

## Page 7

### Step 3: Handling Remote Connections vs. Local Backends
When you open this Vault in a browser or cloud session, there is one technicalAI Mode All Images Short videos Videos More
hurdle: A cloud session cannot reach a local database sitting on your phone's Termux app ( localhost ).
This is exactly why your router-guard configuration profile requires Rule #1: The Gateway Proxy Fallback.
When you open the repo on your mobile device (Local): localhost:20128 is live. OmniRoute catches the completions, coordinates your local tools, and manages your billing profiles seamlessly.
localized Terrestrial Brain PostgreSQL server, the connection will
drop. code.claude.com +1
The Result: Thanks to your explicit instruction, Claude will print: "Warning: OmniRoute Proxy/Terrestrial Brain backend is offline. Falling back to direct model execution environment." It will safely bypass the broken proxy port but still keep your honey-for-devs , task-review , and repository-relative scripts fully functional in the cloud workspace.
Would you like your agent to write a GitHub Actions workflow file or a Docker initialization script into the repo root so that if you ever deploy this Vault to a remote development container, it boots a persistent PostgreSQL instance for your memory data automatically?
code.claude.com
Run Claude Code in the cloud from your browser or phone. Connect a GitHub repository, submit a task, and review the PR without loc...
Towards AI
CLAUDE.md and SKILL.md are both just markdown files someone wrote. MCP isn't a file you write once, it's a live connection between...

---

## Page 8

Pristren
Keep Reading. LLM Token Optimization in 2026 — model routing, caching, MCP audit; Claude Code Complete Setup Guide — install, CLAU...
Show all
yes
9:26PM
To make your Vault repository completely portable so it automatically provisions its own local data stack wherever it is spun up, we will use a Docker Compose engine combined with an automatic workspace bootstrap script.
This setup handles the infrastructure requirements automatically. When you clone your Vault into a cloud runtime, GitHub Codespace, or a clean terminal environment, a single file boots up your PostgreSQL vector database layer, provisions your local memory storage, and exposes everything directly to your model tools.
Here is the exact multi-container orchestration system to place into the root of your Vault repository.
### Step 1: The Portability Engine ( docker-compose.yml )
Create a file named docker-compose.yml right in the root of your Vault repository. This file declares your self-hosted backend stack so it can run isolated on any computer or cloud instance without you needing to install tools manually:
### yaml
version: '3.8'
services: # The Static/Vector Layer (Terrestrial Brain Backend) terrestrial-db: image: pgvector/pgvector:pg16

---

## Page 9

container_name: terrestrial_postgres
restart: always AI Modeenvironment:All Images Short videos Videos More
POSTGRES_DB: terrestrial_brain
POSTGRES_USER: vault_admin
POSTGRES_PASSWORD: safe_local_password_123
ports:
- "5432:5432"
volumes:
- terrestrial_data:/var/lib/postgresql/data
# The Unified Traffic Proxy (OmniRoute Gateway Daemon)
omniroute-gateway:
image: node:20-alpine
container_name: omniroute_proxy
restart: always
ports:
- "20128:20128"
working_dir: /app
volumes:
- ./:/app
environment:
- PORT=20128
- DATABASE_URL=postgresql://vault_admin:safe_local_password_123
command: >
sh -c "npm install -g omniroute && omniroute start --mcp --port
depends_on:
- terrestrial-db
volumes:
terrestrial_data:
driver: local
Use code with caution.
## Step 2: The Automatic Workspace Bootstrapper ( bootstrap.sh )
### To stitch your local tools together when you load the repository, create a
### lightweight bash file named bootstrap.sh in your Vault repository root:

---

## Page 10

AI Mode All Images Short videos Videos More
#!/bin/bash
set -e
echo "🚀 [Vault Lifecycle] Starting Unified Memory Storage Stack..."
# 1. Check for Docker engine infrastructure
if command -v docker-compose &> /dev/null || docker compose version &
echo "📦 Spin up PostgreSQL (Terrestrial Brain Data-Layer) & Omni
docker compose up -d
else
echo " Docker engine not detected. Skipping background containe
echo " Runtime will lean on local fallbacks defined in .mcp.jso
fi
# 2. Verify local project-scoped layout requirements
mkdir -p .claude/output-styles
mkdir -p ./scripts
# 3. Inform the developer of the connection layout status
echo " [Complete] Environment ready for AI client interaction."
echo "👉 Execute client app using: 'claude --output-style router-guar
Use code with caution.
### Make this file executable inside your repository by running:
## bash
chmod +x bootstrap.sh
Use code with caution.
## Step 3: Aligning Your Portable .mcp.json Connections
### Now that your Docker ecosystem handles running the backend containers on the
### network, update your Vault's root .mcp.json file so it matches this cloud-portable

---

## Page 11

environment exactly:
AI Mode All Images Short videos Videos More
### json
{
"mcpServers": {
"omniroute-gateway": {
"command": "curl",
"args": ["-s", "http://localhost:20128/mcp"]
},
"mem0-memory": {
"command": "npx",
"args": ["-y", "@mem0/mcp"]
},
"terrestrial-brain": {
"command": "npx",
"args": ["-y", "ob1-mcp-server"],
"env": {
"DATABASE_URL": "postgresql://vault_admin:safe_local_password
}
},
"code-review-graph": {
"command": "npx",
"args": ["-y", "code-review-graph@latest"]
},
"notebook-lm": {
"command": "python",
"args": ["./scripts/notebook-lm.py"]
},
"obsidian-official": {
"command": "npx",
"args": ["-y", "@modelcontextprotocol/server-obsidian"]
},
"graphify": {
"command": "npx",
"args": ["-y", "graphify-mcp-server"]
}
}
}
Use code with caution.

---

## Page 12

## The New Workspace Launch BlueprintAI Mode All Images Short videos Videos More
Going forward, whenever you clone this repository down onto a new device, a cloud server, or a browser container environment, your launch workflow drops to just two simple commands:
## bash
# Step 1: Boot all infrastructure pools instantly ./bootstrap.sh
# Step 2: Fire up your coding terminal locked to your exact 6-layer m claude --output-style router-guard
Use code with caution.
repo, an automated pipeline verifies your custom code maps and database schema integrity automatically?
yes that also that workflow needs to include the get sync with the master Branch so that every repo stays current with the …
9:28PM
To fully automate your workflow across your main Vault and all downstream forks, you need a configuration that handles Upstream Git Syncing, Token Integrity Auditing, Automated Pull Request Generation, and Continuous Integration Auto-Merging.
ci.yml .GitHub

---

## Page 13

### Step 1: The Master CI File ( .github/workflows/vault-ci.yml )
Create this file in the root of your repository. It leverages deep Git manipulation,AI Mode All Images Short videos Videos More
leakage check, and fires the auto-merge engine natively.GitHub +2
The complete GitHub Actions workflow YAML configuration file, which includes jobs for upstream fork synchronization, runtime verification and exposed token checks using secret-scanning tools, automatic pull request creation upon session push, and auto-merging upon successful CI status, can be found in the referenced web
document. GitHub
Step 2: Critical Settings to Enable in GitHub
inside your repository settings panel on GitHub:GitHub
for "Allow GitHub Actions to create and approve pull requests."
2. Auto-Merge Toggle: Scroll to the bottom of your Settings -> General page. Under the Pull Requests section, check the box that says "Allow auto-
merge". DEV Community
How this executes during your workflow:
The Master Sync Loop: Every 3 hours, the background sync-fork action wakes up. It fetches the newest edits from your authority Main branch, forces your fork repositories to lock to it via fast-forwarding, and updates the local
origin. GitHub +1
branch cleanly into the main code pool.GitHub

---

## Page 14

Would you like me to give your agent the pre-commit Git hooks file setup for your
before the code even gets uploaded to GitHub's network?
GitHub
Code-review-graph is a tool that builds a structural map of your code and tracks changes incrementally. It uses Tree-sitter to par...
GitHub
ESON — Efficient Structured Object Notation. Honey includes ESON, a zero-dependency, schema-first format for agent handoffs. Repea...
GitHub
Automatically merges main into pull request branches. Detects if a merge conflict is true or false. Auto-resolves false conflicts ...
Show all
is it possible to run clod from the terminal incognito if I have it
hooked up to a browser and then also have it clones in the …
9:34PM
Yes, it is entirely possible to run an isolated, completely separate instance of Claude
Code in your terminal that is fully insulated from your usual browser session, your
default agent, or your standard machine state.
If you are worried that your main day-to-day agent will notice this setup and try to
modify, override, or delete your files, you can build a secure sandbox. This isolates
the environment so that your default agent cannot see what the terminal instance is
doing.