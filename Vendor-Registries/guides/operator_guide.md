# Claude Code Engineering Harness: User & Installation Guide

## 1. Executive Summary & Intended Outcomes
This guide outlines the custom operations required to run long, multi-session programming epics within a Termux-sandboxed environment using Claude Code. The primary operational goals achieved are:
* **Context Preservation:** Ensuring progress logged up to intermediate stages (e.g., Agent 7D) is safe on disk.
* **Context Token Control:** Restricting memory blowouts, lag, or "auto-compaction thrashing loops."
* **Workspace Guarding:** Preventing automated tools from over-writing local custom utilities (like Termux automation operators or cleanup scripts) while enabling expert engineering workflows.

---

## 2. Topic Breakdowns & Troubleshooting

### Topic A: Compaction Techniques (Native vs. Scripted Hooks)
* **The Concept:** Compaction collapses long text logs into clear historical notes to keep token usage within efficient margins. 
* **The Problem:** Repeated background read/write updates can create an auto-compaction loop ("thrashing") that kills performance.
* **The Fix:** Run a manual, parameter-guided native command to strip raw conversational baggage while locking finalized schema definitions and current code states into memory.

### Topic B: Environment Namespace Mismatch (Hollowness)
* **The Problem:** Software agents may mistakenly report that directories or files are missing or incomplete. 
* **The Cause:** Global system sweeps ignore deep plugin caches. Managed plugins isolate files within private directories, preventing raw file system commands like `find` or `ls` from seeing them.
* **The Fix:** Query active tools through the application's internal manifest interface rather than utilizing native operating system paths.

---

## 3. Operator Installation Workflow

### Step 1: Environment Integrity Validation
Confirm whether the required engineering package is registered inside the active user scope by querying the plugin manager:
```bash
claude plugins list
```

### Step 2: System Namespace Discovery
Examine internal capabilities directly to verify namespaced tools:
```bash
/plugin list
```
*Note: To inspect loose, unmanaged scripts sitting within the system's global directory, execute:*
```bash
find ~/.claude/skills/ -name "SKILL.md" 2>/dev/null
```

### Step 3: Phase Initialization
Run the initialization tool to verify repository configuration constraints:
```bash
/mattpocock-skills:setup-matt-pocock-skills
```

---

## 4. Multi-Session Phase Path Matrix
For long projects, execute tasks in a linear sequence to prevent memory saturation.

| Step | Command Name | Phase Target | Memory Action |
| :--- | :--- | :--- | :--- |
| **1** | `/mattpocock-skills:ask-matt` | Master Routing | Initial check of repository state |
| **2** | `/mattpocock-skills:grill-with-docs` | Discovery Loop | Exhaustive architectural interview |
| **3** | `/mattpocock-skills:to-spec` | Blueprint Commit | Writes a stable specification file to disk |
| **4** | `/mattpocock-skills:to-tickets` | Task Breakdown | Generates atomic issue logs |
| **5** | `/compact <context prompt>` | Session Clear | **Manual Action:** Purge conversation logs |
| **6** | `/mattpocock-skills:implement` | Execution Phase | Start a clean window; execute code on a specific ticket |
| **7** | `/mattpocock-skills:tdd` | Verification | Run red-green-refactor quality gates |
