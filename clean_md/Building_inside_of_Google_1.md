---
source: Building inside of Google (1).txt
type: condensed
condensed_from: NovA-Corpus/condensed/native-apk-vs-cloud-orchestration (2026-08-20)
original_moved_to: Merovingian's_keep/_salvage/NovA-Corpus/originals/
---

# Antigravity CLI + Gemini Spark orchestration for a native app build

The combination of Antigravity CLI and Gemini Spark orchestrates an asynchronous "Captain's Chair" agent stack to build an app. Because they share the same underlying core Antigravity agent harness, they hand off tasks to one another across the network.

## How Antigravity and Gemini Spark Work Together

Antigravity runs locally on the node cluster to write code; Gemini Spark runs 24/7 in the cloud to manage long-running background tasks (deployment, monitoring data stores).

```
[Antigravity CLI (Local Node)] ──► Code App / Create MCP Artifacts
                                          │
                                          ▼ (Syncs Project Context)
[Gemini Spark (Cloud VM)]       ──► Triggers Background Build & 24/7 Monitor
                                          │
                                          ▼
[Your Custom Operations App]    ◄── Placed onto Cloud Run (Credit Pool)
```

1. **Local Scaffolding with Antigravity CLI (`agy`)** — the Go-based Antigravity CLI lays out MCP server files and the core structure of the app. Uses Asynchronous Subagents to code features and build files in parallel without freezing the shell.
2. **Handoff to Gemini Spark** — Spark lives on persistent Google Cloud VMs, keeps processing code, building containers, testing database routing loops 24/7 even after the terminal/phone is closed.
3. **The Deployment App Hub** — Spark automates pushing finalized container files to Cloud Run, creating a permanently active custom server app drawing from the credit pool.

## Will Speech and Vision Break the Rules?

No. The Antigravity engine natively supports multi-modal image inputs; the Gemini Enterprise Agent Platform supports full multi-modal grounding. Vision and speech both fall under Google Cloud's standard enterprise billing tracks:

- **Vision**: linking a Vertex AI Data Store to a Cloud Storage bucket of image-heavy manuals/PDFs/diagrams routes through the standard Agent Builder track.
- **Speech**: the Vertex AI Voice/ADK (Agent Development Kit) pipeline keeps billing inside the cloud project's enterprise boundary.

## Step 1: Initialize the Tool-Building Agent Workspace

```bash
# Ensure the latest Go-based Antigravity client
agy /config --trust-workspace true

# Open the multi-agent management matrix
/agents
```

## Step 2: The Core Prompt for the Tool-Builder

Paste into the Antigravity CLI or Gemini Spark thread to kick off the "Captain's Chair" workflow:

```
Initialize a new application build project named "Neuromesh_Command_Hub".

You are an expert infrastructure architect tasked with building a developer
help desk and operational guide server app.

Generate the following core code artifacts:
1. An implementation plan tracking file formats for model weights, software
   manuals, and custom Model Context Protocol (MCP) server endpoints.
2. A containerized Python backend that maps local database snapshots and
   tool logs into an automated, multi-modal ingestion schema (supporting
   inline Base64 images for Vision and real-time text logs).
3. A deployment script targeting Google Cloud Run to host the operational
   manuals on enterprise credits.

Utilize background subagents to code the files in parallel and test the UI
components inside the sandboxed web browser before compiling. Avoid all
conversational filler — return only clean schemas and production code.
```

Firing this prompt spins up subagents via the Antigravity harness while Gemini Spark keeps the project running in the background until the full local-to-cloud server infrastructure is built, tested, and deployed to Cloud Run.
