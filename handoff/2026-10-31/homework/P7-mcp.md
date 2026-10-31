# P7 MCP self-host specs (wiki-admin)

Read basis: plugin dirs under `~/.claude/plugins/synced/a5d13a90-190b-42eb-ad1b-69c924919b1b_b410cc73-6e72-411c-a9de-4edf62ec27d7/` (call it `$P`). Short ids: memory-agent=`55175215…`, agent-recall=`80cdebec…`, backlog=`b38c2c6a…`, cc=`ff18ea72…`, watch-video=`b911d56b…`, desktop-commander=`8d52a3a6…`, apify=`d9b3b793…`, google-multi-account=`ba923796…`, cloudflare=`a512755b…`.
Read type: FULL = file read in full or the cited lines; DESC = README/manifest only; NOT READ = not opened. Nothing was run, installed or tested; every "works on Termux/phone" is untested.

## 1. Decision table

| Server | Transport (cite) | Decision | Pipeline |
|---|---|---|---|
| memory-agent | none: README:36 "no vector DB, no daemon, no server"; plugin.json:10 only has commands | not an MCP server. Cut from `.mcp.json` | memory-store |
| agent-recall | stdio py `python -m agent_recall.mcp_server` (README:93-96); plugin `.mcp.json:1` is `{"mcpServers":{}}` | self-host (it is local code), 9 tools | memory-store |
| backlog | stdio node (`plugin.json:12-19`) | replace with `manifest.jsonl` for the ingest ledger; keep backlog only if P3 wants cross-session tasks | wiki-admin (optional) |
| cc | stdio tsx (`plugin.json:11-16`), 3 tools | keep local, trim; tell P3 | wiki-admin (fan-out, optional) |
| watch-video | stdio py wrapper `mcp-server/server.py` (9 tools) | self-host, drop 2 Jira tools | wiki-admin (intake) |
| desktop-commander | stdio via `npx -y …@latest` (`plugin.json:24-29`) | keep vendor, pin version | wiki-admin (convert, overlaps native tools) |
| apify | remote http `https://mcp.apify.com/?client=claude+code+plugin` (`.mcp.json:3-6`) | keep vendor | wiki-admin (intake) |
| google-multi-account | stdio node via `~/.google-multi-mcp/start.sh` (`.mcp.json:3-6`) | self-host (your own OAuth client); Docs/Sheets/Slides stay on the claude.ai connectors | wiki-admin (intake) |
| cloudflare | remote http `https://mcp.cloudflare.com/mcp` (`.mcp.json:3-6`) | keep vendor. The remote server is not limited to Vectorize/D1/R2 (DESC) | memory-store |

## 2. Per server

### memory-agent (noreff/memory-agent, v0.1.0, MIT: `plugin.json:4,7,8`)
- Parts (FULL for plugin.json, README grep only): `/memory-setup` and other commands (`plugin.json:10`), `engine/` (capture, ingest, merge, garden, inject), `adapters/`, `hooks.off-20261028/hooks.json` (already disabled on disk). Compiles sessions into a markdown KB with provenance and conflict tracking (`plugin.json:5`).
- Verdict: cut from wiki-admin. It writes its own `knowledge/` KB from session transcripts, a second wiki that competes with llm-wiki (P4). Hand to the memory-store pipeline. Nothing to self-host.
- Bloat: `tests/`, `docs/`, `install.sh` (sizes not measured).

### agent-recall (mnardit/agent-recall, v0.4.0, MIT: `plugin.json:4`, `pyproject.toml:10`)
- Spec (FULL for mcp_server.py tool defs, README grep):
  - Tools (`agent_recall/mcp_server.py:72-143`): create_entities, create_relations, add_observations, delete_entities, delete_relations, delete_observations, read_graph, search_nodes, open_nodes.
  - Launch: `pip install 'agent-recall[mcp]'` (README:74), entry `python -m agent_recall.mcp_server` (README:96). Deps pyyaml, click; mcp>=1.0,<2.0 (`pyproject.toml:33-39`).
  - Host: local stdio, one process per client. Data `~/.agent-recall/frames.db` SQLite (`config.py:12`).
  - Secrets: none for the MCP server. Briefings use `claude -p` by default, or `ANTHROPIC_API_KEY` if `backend: api` (README:381, 430, 542).
  - Health check: `python3 -m agent_recall.mcp_server` starts without errors (README:534), plus a tools/list round trip showing the 9 names.
- Hooks: PostToolUse on `mcp__memory__.*` (README:173-179), SessionStart hook script exists (`pyproject.toml:45`); neither blocks (not read in full; DESC). Plugin ships them in `hooks.off-20261028/`, which is already off.
- Verdict: memory-store pipeline. Not wiki-admin's. wiki-admin hands over `manifest.jsonl` only.

### backlog (backloghq/backlog, v2.4.3, MIT: `plugin.json:4,10`)
- 24 tools (FULL list from `src/tools/*.ts` registerTool names): task_add/done/delete/start/stop/log/duplicate/modify/annotate/denotate/undo/purge/import/list/info/count/projects/tags, task_archive/_list/_load, task_doc_write/read/delete.
- Launch: `scripts/start-server.sh` runs `npm ci --production` into `CLAUDE_PLUGIN_DATA` then `node dist/index.js`; env `TASKDATA_ROOT` (`plugin.json:14-16`, start-server.sh). Docker image exists: `node:25-slim`, `TASKDATA=/tmp/backlog-data` (Dockerfile:1-7).
- Secrets: none.
- Verdict: replace for wiki-admin by the existing `manifest.jsonl` plus each worker's progress file (work-order section 3). Keep only if P3's batch ledger wants cross-agent task claims. If kept: stdio local, data dir `<vault>/.wiki-admin/tasks/`, health = `task_count` returns a number.
- Bloat: `dist/` + `node_modules` after install, `.github/`, `tests/`, `glama.json`.

### cc (anipotts/cc, v0.6.0, MIT: `plugin.json:4,9,12`)
- Tools (`server.ts:277,283,297`): cc_peers, cc_roster, cc_send. Reads `~/.claude/sessions/*.json`; mailbox `~/.claude/cc/mailbox/<id>.json` (`server.ts:9-11`).
- Launch: `npx tsx server.ts` with node_modules symlinked from `CLAUDE_PLUGIN_DATA` (`plugin.json:14`). Needs the `channels` feature (`plugin.json:17-19`); whether this build supports it is not checked.
- Host: local stdio. Secrets: none. Health: `cc_peers` returns the current session.
- Verdict: keep as optional P3 helper (parallel workers see each other and avoid file conflicts). Not self-hosted beyond local stdio. Its `hooks.off-…` stays off until P6 merges hooks.
- Bloat: `node_modules`, `evals/`, `package-lock.json`.

### watch-video (MarcinSufa/claude-watch-video, v1.0.0, MIT: `plugin.json:3,10,11`)
- Tools (`mcp-server/server.py` @mcp.tool at :617,724,831,961,990,1021,1039,1095,1188): watch_video, watch_video_start, watch_video_status, read_transcript, read_report, read_highlights, pick_highlights, post_to_jira, fetch_jira_attachment. Plus resource `workdir://{path}/meta.json` (:1235). Pipeline scripts in `scripts/` (fetch, frames, transcribe, dedup, ocr, report).
- Spec: launch `claude-watch-video-mcp` or `python mcp-server/server.py` (mcp-server/README.md:148); `WATCH_VIDEO_SCRIPTS_DIR`-style env for the scripts dir (README:160, exact variable name not read). Host: local stdio. Prefer the `watch_video_start`/`_status` pair; the sync tool can stall hosts (README:11).
- Secrets by name: GROQ_API_KEY, OPENAI_API_KEY (`scripts/transcribe.py:137-138`), both optional; default is local faster-whisper (`plugin.json:4`). Jira token names not read (only needed by the two Jira tools).
- Health: `watch_video_status` on an unknown id returns a structured error, and `scripts/smoketest.py` exists (not run).
- Verdict: self-host the 7 non-Jira tools; cut `post_to_jira` and `fetch_jira_attachment`. Overlaps P1's local-whisper-mcp for audio; winner for video: this one (frames + transcript). Needs ffmpeg and yt-dlp; Termux support untested.
- Bloat: `docs/`, `.github/`, `ROADMAP.md`, `mcp-server/tests/`.

### desktop-commander (wonderwhy-er/DesktopCommanderMCP, v0.2.0, MIT: `plugin.json:4,11,12`)
- Parts (README FULL, server not read): MCP server (terminal, processes, filesystem, PDF/DOCX/Excel/image reading, search, SSH) and 6 skills (terminal, computer-health-check, ai-tools-setup, knowledge-base, obsidian-vault, desktop-commander-overview: README:9-14).
- Launch: `npx -y @wonderwhy-er/desktop-commander@latest` (`plugin.json:27`). Unpinned `@latest` runs new upstream code each start; pin it. Secrets: none. Health: tools/list round trip.
- Verdict: keep vendor, pinned. Use only for structured-doc reads when no converter exists (P1). Cut 5 of 6 skills (keep `knowledge-base` only if P4 wants it). The Bash/Read tools already cover terminal and file ops.

### apify (apify/apify-claude-code-plugin, v1.0.2, Apache-2.0: `plugin.json:4,9`)
- Remote http (`.mcp.json:3-6`). OAuth in browser (README:44); read-only tools (search-actors, fetch-actor-details, search-apify-docs, fetch-apify-docs) need no auth; run-actor and get-dataset-items do. Headless: secret `APIFY_TOKEN` (README:60-63).
- Verdict: keep vendor. No self-hosting; it is a paid marketplace. Cut the 5 actor-development skills and the agent (they build Actors, not ingest). Bloat: `icon.png`, `references/`.
- Conflict: scraping overlaps P1's firecrawl and the TinyFish/Bright Data connectors already in this session; winner chosen by P1.

### google-multi-account (stevegustafson32/google-multi-account, v0.7.0, MIT: `plugin.json:3,8`, LICENSE)
- 21 tools (`servers/index.js` server.tool names): Gmail (search_emails, get_email_thread, send_email, create_email_draft, list_email_labels, label_email, list_attachments, download_attachment, get_attachment), Calendar (list/create/update/delete_calendar_event, find_free_time), Drive (drive_search, drive_list_folder, drive_upload, drive_download, drive_create_folder, drive_file_info, drive_share). No Docs/Sheets/Slides tools.
- Launch: `/bin/bash ~/.google-multi-mcp/start.sh` (`.mcp.json:4-5`); that directory does not exist on this device (`ls` failed). README:26 lists only macOS and Windows. Termux is untested; the server is plain node so it may run.
- Host: local stdio. Config + refresh tokens in `~/.google-multi-mcp/config.json` (`servers/config.js:7,24-25`), you supply your own GCP OAuth client (README:30-33).
- Secrets by name: per-account `refreshToken`, OAuth client id/secret (stored in config.json, gitignored; README:154-155). Never in the vault.
- Health: `search_emails` limit 1 per account label; a stale-token warning is logged at startup (README:248).
- Verdict: self-host. It is the only part that gives multi-account Drive/Gmail reach. Safety: send_email, drive_share, drive_upload write outward; wiki-admin should use read tools only (allowlist in `.mcp.json`). Email content is sanitized (README:20).
- Conflict: Drive read overlaps P1's gdrive-to-markdown and the claude.ai Docs/Sheets/Slides connectors; those win for Docs/Sheets/Slides export, this wins for multi-account search/download.

### cloudflare (v not read, `plugin.json` DESC)
- Remote streamable-http `https://mcp.cloudflare.com/mcp` (`.mcp.json:3-6`, `mcp.json:5-6`); 14 skills (workers, wrangler, durable-objects, …). Wrangler skill covers Workers, KV, R2, D1, Vectorize, Queues (README:76).
- Verdict: keep vendor, memory-store pipeline (hosted vector/DB). wiki-admin does not need it; search starts local (BRIEF). Strip everything but the MCP entry if ever used.

## 3. Comparison repos (what they are, what wiki-admin gets)

| Repo | What it is | Relevance |
|---|---|---|
| `~/repos/NvAEx-mcp` (Apache-2.0) | README list of Google's MCP servers: remote managed (BigQuery, Cloud Storage, Cloud Run, Resource Manager, Firestore, Developer Knowledge, …) and open-source (Workspace Gemini CLI extension, Firebase, MCP Toolbox) (README:7-35). Only README/LICENSE/examples. | Source of the Google Cloud reach. Vendor-hosted, nothing to self-host. |
| `~/repos/NvAEx-mcp-toolbox` (Apache-2.0) | Go MCP server for databases; `internal/sources/` has bigquery, cloudstorage, firestore, postgres, serverlessspark (Dataproc), … (ls). | Needed only for memory-store databases, or BigQuery/GCS reads. Not wiki-admin core. |
| `~/repos/github-mcp-server` (MIT) | Remote `https://api.githubcopilot.com/mcp/` (README:58-59) or local with `GITHUB_PERSONAL_ACCESS_TOKEN` (`server.json:35`). | Intake source `repo`. Keep vendor remote; `gh` CLI is the fallback. |
| `~/repos/NvAEx-render-mcp-server` | Render's MCP, stdio and streamable HTTP (README:11-14); `render.yaml` runs `./app --transport http`. | A hosting option for HTTP MCP servers, not a wiki-admin tool. Cut. |
| `gemini_infer.py serve` (`~/repos/.wt/vault-session/plugins/greedy-crane/scripts/gemini_infer.py:182-240`) | Stdlib stdio JSON-RPC, server `wiki-admin-gemini`, tools gemini_draft, gemini_w5h, gemini_ask (:184-198); key `GEMINI_API_KEY`/`GOOGLE_API_KEY` env only (:11,100); dry-run when no key (:106). | Reuse as the template for any new wiki-admin server. It is the only self-hosted wiki-admin MCP needed today. |

## 4. Reach the wiki admin needs

| Reach | Covered by | Gap |
|---|---|---|
| Web tools | apify (vendor), plus connectors already present this session (TinyFish, Bright Data skills, Firecrawl via P1) | none MCP-wise |
| Google Cloud projects | Google remote MCPs listed in NvAEx-mcp README:7-35 (Cloud Storage, BigQuery, Resource Manager); mcp-toolbox for self-run | Setup per project: enable the API, auth by gcloud ADC or OAuth (not tested) |
| Google Drive/Gmail multi-account | google-multi-account (self-host) | Termux run untested |
| Frontier apps | claude.ai connectors; `gemini_infer.py serve` for Gemini API | No MCP found by probes for ChatGPT or other chat apps |
| Gemini app / Spark agents | **none**. `handoff/2026-10-24/extracts/ondisk-extract.md:10-11,45` says Spark agents cannot read cloud Gemini chat sessions out of the box; only an idea of a headless-browser aggregator (:35). TOOLS.md:14 lists "Gemini app and Spark agents" as fan-out lanes. | Not decided: manual export, or a browser-driven MCP. Operator choice; I did not invent one. |

Probes for the gap: TOOLS.md, `handoff/2026-10-24/extracts/ondisk-extract.md`, the repos above. Not probed: the rest of the vault, memory repo. Report as "not found by those probes".

## 5. New self-hosted servers needed

None. One reuse: `gemini_infer.py serve`. If the operator wants a Spark/Gemini-app lane, spec later; no existing script in `extraction-index.txt` was checked for it (file not opened this run).

## 6. Hooks in this packet
All hook files are already renamed `hooks.off-20261028/` (memory-agent, agent-recall, backlog, cc), so none load. Event lists were not read in full; P6 owns the merge. None of them may be kept if they could block a read.

## 7. Open points
- Pin versions: desktop-commander `@latest`, cc `tsx` via npx.
- Confirm `WATCH_VIDEO` scripts-dir variable name and Jira secret names (not read).
- google-multi-account on Termux and watch-video's ffmpeg/yt-dlp: untested.
