# Environment Audit, 2026-10-25

Read-only audit of the Claude Code cloud container (session `cse_01CaQcHPB1pTuL1vw86EhwTG`). Nothing was changed. Secret values are not shown. Only names appear here.

## Findings summary

### Likely cause of the missing chat (hearthbot) tools
**The CLI was relaunched at 21:29:58Z in coordinator mode. The coordinator tool allowlist does not include any `mcp__hearthbot__*` tool, so the server connects but none of its tools are offered.**

Evidence:
- There were two launches (`/tmp/claude-code.log` lines 3 and 15981). The first, at 20:10:06Z, used `--maintenance --model claude-fable-5-1`. The second, at 21:29:58Z, has no `--maintenance` flag and uses `--model claude-opus-5-5[1m]`. Both pass `--resume=…/sessions/cse_01CaQc…`.
- The env var `CLAUDE_CODE_COORDINATOR_MODE` is set. `CLAUDE_CODE_COORDINATOR_EXTRA_TOOLS` lists only `SuggestConnectors, SearchMcpRegistry, ListConnectors, ClaudeDesign, propose_skills` and 10 `mcp__claude-code-remote__*` tools. It contains **no hearthbot tools**.
- At 21:30:04.225Z: `MCP server "hearthbot": Connection established with capabilities: {"hasTools":true,…}`. The server is up.
- At 21:30:23.868Z: `Unknown tool mcp_tool: toolu_01MHuLfMkALMEiLhohN6grA9`. At 21:30:23.894Z: `[PROMPT CACHE BREAK] tools changed (+0/-9 tools)`. Nine tools were dropped.
- The session transcript (`~/.claude/projects/-home-user/6fe8e63e-….jsonl`) shows the same error at 21:30:23, 21:31:43, 21:32:22, 21:33:28, 21:34:29, 21:36:46 and 21:37:20:
  `Error: No such tool available: mcp__hearthbot__post_message. Its MCP server 'hearthbot' is connected but does not offer this tool here.`
- At 21:35:14 the same transcript shows `No such tool available: Bash. Bash is not available to you as the coordinator`. This confirms that the coordinator filter was active.
- The stop gate then allowed every one of these turns with `ccr_reply_gate_allow path=terminal_tool_unreachable`. As a result, **replies were silently not delivered and nothing blocked them.** Before the relaunch, at 20:10 and 20:13Z, the log shows `path=terminal_tool_found` and successful `post_message` calls.
- A second contributing factor: in `/tmp/mcp-config-cse_….json`, `claude-code-remote` carries an inline pre-declared `tools` list, but `hearthbot` does not. It only has `role: comms, alwaysLoad: true`.

What to escalate: in coordinator mode, the `mcp__hearthbot__*` terminal tools (or the comms-role server) need to be on the coordinator allowlist. Alternatively, the session should not resume into coordinator mode. Users cannot fix this themselves.

### Risks
1. **Silent reply loss.** The reply gate treats "no such tool" as unreachable and allows the turn to stop, so the user sees nothing.
2. **Name mismatch in the gate.** The docstring and `TERMINAL_DEFAULT` in `stop-hook-reply-gate.py` name `mcp__slackbot__*`. The env var `CCR_REPLY_STOP_HOOK_TERMINAL_TOOLS` overrides this with hearthbot names, so the gate works. The leftover is cosmetic, but it is misleading when debugging.
3. **Phone-home hooks.** The `claude-patterns` plugin runs `install-ping.py` on every SessionStart and posts to `https://myceliumai.co/api/install`. MCP servers launched with `npx …@latest` and `uvx browser-use@latest` (desktop-commander, browser-use) pull unpinned code at every start.
4. **Many hosted third-party MCP endpoints.** These include aishorty.com, createstate.ai, cobrain.space, mcpbinder.com, research-desk-checker.fly.dev, agent.tinyfish.ai, userintuition.ai and unstructured.io.
5. **Hooks that block, rewrite or gate edits.** shipwright `approval_gate` (PreToolUse on Edit/Write), fellowship `plan-gate`, maddog guards (Bash, Agent, and all file tools), scaffold PreToolUse on Bash/Write, dev-forge pre-commit on Bash, jevmem `--guard`, and wiki-wonka `protect-raw`. They also include Stop gates from memory-bank, tenet, rutter, pm-toolkit quality-gate, anchor-memory integrity-gate, shipwright checklist, compounded, pmm, handoff, whydone, scaffold and jevmem. In total, about 20 Stop hooks run on every turn (`hookCount: 20`).
6. **Context bloat.** About 110 plugins and about 800 skills are listed at startup. See section 6.
7. **Credentials in the environment** (names only): `GH_TOKEN`, `GITHUB_TOKEN`, `HF_TOKEN`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `QAI_HUB_API_TOKEN`, `CLOUDSDK_AUTH_ACCESS_TOKEN`, `CLAUDE_CODE_MESSAGING_TOKEN`. Every process, plugin hooks included, can read them.
8. **Broken hooks.** Errors at resume: agent-recall (`agent-recall-session-start: not found`, exit 127), workflow-toolkit (`session-start-hook.sh: Permission denied`, exit 126), and ux-superpowers (a prompt-type SessionStart hook, which is unsupported).

### Things the user can fix themselves
- Disable the persona and boot-instruction plugins they don't use: **gangsta, wizard, fellowship, research-superpowers, agent-protocols**, plus the overlapping memory plugins (see section 6).
- Disable **claude-patterns**, because of its install ping.
- Disable plugins that fail or are broken: agent-recall, jevmem and graph-query-mcp (`stdio` executable not found), oak-memory (connection closed), desktop-commander (timeout), `data` (definite endpoint not found), and `engineering` (its github MCP is rejected with 403).
- Authorize, or drop, the plugins whose connectors need OAuth. There are 26 such servers (list in section 5).
- Remove `AWS_*`, `HF_TOKEN` and `QAI_HUB_API_TOKEN` from the cloud environment settings if this project doesn't need them.

---

## 1. Host
- OS: Ubuntu 24.04.5 LTS. Kernel `6.18.44-fc-v153` (a Firecracker VM, hostname `vm`), x86_64.
- 4 vCPU. 15 GiB RAM (about 14 GiB free). No swap.
- Disk: `/` on `/dev/vda` is 252G with 11G used. `/opt/claude-code` (vdc) is 307M and 92% full. `/opt/env-runner` (vdd) is 47M. `/dev/shm` is a 16G tmpfs.
- `/mnt/attach/project-files` is a `fuse.rclone` mount (`rclone-filestore:pjfs_012F46…`, reported as 1.0P) with options rw, allow_other. `/mnt/project-files` shows the same content: `habit-tracker/`, `plugins/`, `uploads/`.
- User: root (uid 0).
- Uptime was 10 minutes at 21:40Z. PID 1 started at Sun Oct 25 21:29:54 2026, so the container (re)started at about 21:29:54Z. Claude Code's first run was at 20:10Z, so the session survived across a container restart.

## 2. Network
- `HTTPS_PROXY=http://127.0.0.1:45259` is a local agent proxy that tunnels to a policy egress proxy and re-terminates TLS.
- Status endpoint: `enabled: true`, `selective: false`, `bundleCoversEveryHost: true`, `gitConfigInjection: true`, `gitSshRewrite: true`, `governedGitTools: false`, `recentRelayFailures: []`. Preconfigured CLIs: bq, gcloud, gh, gsutil.
- NO_PROXY bypasses the proxy for localhost and private ranges, `api.anthropic.com` (plus its staging and pr-preview hosts), `mcp-proxy.anthropic.com`, npm, jsr, pypi, crates and golang proxy, and `*.svc.cluster.local`.
- Files in `/root/.ccr/`:
  - `ca-bundle.crt` (186 KB, 123 certificates)
  - `agent-proxy-ca.crt`
  - `system-trust.ca.pem`
  - `README.md`, which covers failure classes: TLS, 405, 403/407, resets, tools that ignore the proxy, git, docker, and what is unsupported (gRPC, WebSocket, mTLS, pinned certificates, non-443 ports).
- The CA is wired in through these variables: SSL_CERT_FILE, CURL_CA_BUNDLE, REQUESTS_CA_BUNDLE, NODE_EXTRA_CA_CERTS, GIT_SSL_CAINFO, PIP_CERT, AWS_CA_BUNDLE, DENO_CERT, CARGO_HTTP_CAINFO, HEX_CACERTS_PATH, NIX_SSL_CERT_FILE, CLOUDSDK_CORE_CUSTOM_CA_CERTS_FILE and GRPC_DEFAULT_SSL_ROOTS_FILE_PATH. The Java truststore is `/etc/ssl/certs/java/cacerts`.
- **Injected-credential hosts:** `api.typesafe.ai`, per the `autoMode.allow` text in `~/.claude/launcher-settings.json`. The proxy adds credentials for this host.

## 3. Claude Code
- Version `2.1.310`, at `/opt/claude-code/bin/claude`.
- Launched by the platform with `--settings ~/.claude/launcher-settings.json --setting-sources user --mcp-config /tmp/mcp-config-cse_….json --append-system-prompt-file /tmp/claude-append-system-prompt.txt` (18.9 KB), plus `--tools`, `--allowed-tools` and `--disallowed-tools`. The values of those three are redacted in the log.
- `~/.claude/settings.json` contains only a `statusLine` that runs a synced plugin's `statusline.py`.
- `~/.claude/launcher-settings.json` contains `autoMode` (allow and environment rules), `permissions.allow: ["Skill"]`, and these hooks:
  - Stop → `~/.claude/stop-hook-git-check.sh`
  - Stop → `~/.claude/stop-hook-reply-gate.py`
  - UserPromptSubmit → `~/.claude/user-prompt-submit-reply-reminder.py`
- Layout of `~/.claude`:
  - `.credentials.json` (0600, not read)
  - `agents/`: 10 PGE agents, each with a `.bak` copy
  - `commands/`: 16 `pge-*` commands
  - `hooks/pge-autolaunch.sh`
  - `skills/`: session-start-hook and `synced/`
  - `plugins/synced/<org>_<id>/`: 219 directories
  - `plugins/data/`: one data dir per plugin
  - `projects/-home-user/`
  - `sessions/`, `session-env/`, `shell-snapshots/`, `state/mcp-discover-verdicts.json`, `mcp-needs-auth-cache.json`
  - `environment-manager/codesign-mcp-config.json`
  - Plugin-written directories: `compounded/`, `fellowship/`, `wherewasi/`, `hud/`
- **Platform-generated files.** All are dated 21:29Z, the container start.
  - `stop-hook-reply-gate.py`: *"Generated for this session and rewritten at every container start; do not edit."* Despite the name, it is a sh wrapper around inline Python.
    - Docstring: *"Stop hook that forces the slackbot main-loop agent to communicate to the Slack thread before ending a turn… re-prompts (decision=block) until the model calls one of those tools and the call succeeds… when the result says the server itself was unreachable the hook allows at once."*
    - `TERMINAL_DEFAULT = ["mcp__slackbot__reply","mcp__slackbot__no_reply_needed","mcp__slackbot__post_message","mcp__slackbot__upload_file","mcp__slackbot__update_reply"]`. `RELAY_TOOL = "mcp__slackbot__post_standing_relay"`. `DEFAULT_LOCAL_CAP = 3`.
    - The env var `CCR_REPLY_STOP_HOOK_TERMINAL_TOOLS` overrides the default list with: `mcp__hearthbot__post_message, no_reply_needed, react, edit_message, suggest_project, suggest_tasks, message_thread, start_thread`. The holding tool is `mcp__hearthbot__post_message`.
    - Its fallback block message names hearthbot: *"Your last turn ended without a terminal `mcp__hearthbot__*` tool call…"*
    - **This is the slackbot vs hearthbot mismatch:** the code defaults and docstring say slackbot, while the runtime env and message say hearthbot.
  - `user-prompt-submit-reply-reminder.py`: *"rewritten at every container start; do not edit"*. It is also sh. It injects the following as additionalContext: *"Text you emit directly is not delivered — only `mcp__hearthbot__*` tool calls reach the user. End your turn with `post_message` — or `no_reply_needed`."*
  - `stop-hook-git-check.sh`: a Stop hook that checks for uncommitted or unpushed work in a git repo. It does not carry the "rewritten" banner.
  - `CLAUDE_CODE_TERMINAL_MCP_TOOLS` (a separate CLI-side list): hearthbot `reply, post_message, update_status, no_reply_needed, react, edit_message, suggest_project, suggest_tasks, message_thread, start_thread`.

## 4. MCP servers
- `~/.claude.json` has no `mcpServers` and no per-project MCP config.
- Platform servers are injected through `--mcp-config /tmp/mcp-config-cse_01CaQcHPB1pTuL1vw86EhwTG.json`. Headers `X-MCP-Server-ID` and `X-Session-UUID` are redacted here.
  - `hearthbot`: http `https://api.anthropic.com/v2/ccr-sessions/-/hearthbot/mcp`, `role: comms`, `alwaysLoad: true`. It has no inline tools.
  - `claude-code-remote`: http `…/ccr-sessions/cse_…/mcp?mcp_server_id=…&toolbox_mcp_server_id=…`, with an **inline `tools` list**.
  - `github`: http `…/ccr-sessions/cse_…/github/mcp?native_pr_tools=1`.
  - The log records `mcp_set_servers authority: … host-owned=[hearthbot, claude-code-remote, github]`.
- `/tmp/codesign-mcp-config.json` is used for commit signing (`gpg.ssh.program=/tmp/code-sign`).
- Logs: `/tmp/claude-code.log` (4.5 MB, 28k lines), `/tmp/claude-code-*.diag.log`, and `/tmp/claude-command`. `~/.claude/debug` does not exist.
- Why hearthbot shows as connected but has no tools after the resume: see the Findings summary. Connection succeeds at 21:30:04Z. Coordinator-mode filtering then removes its tools: `-9 tools` at 21:30:23Z, followed by repeated "No such tool available" errors.

## 5. Plugins
All plugins are synced from claude.ai (marketplace `synced`, under `~/.claude/plugins/synced/bf59ea3a…_3a64471e…/`). They are enabled by the platform sync (`CLAUDE_CODE_SYNC_PLUGINS`). No `enabledPlugins` override exists in settings.json. The audit found about 110 plugin manifests and 106 hook registrations.

### Hooks (event | matcher | command, with root = `${CLAUDE_PLUGIN_ROOT}`)
Flags: **[BLOCK]** can block or deny, **[INJ]** injects context, **[NET]** makes outbound calls.
- memory-bank | Stop | `(all)` | `"${CLAUDE_PLUGIN_ROOT}"/scripts/memory-bank-hook.sh` [BLOCK?]
- dev-forge | SessionStart | `(all)` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/session-start.sh"` [INJ]
- dev-forge | PreToolUse | `Bash` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/pre-commit.sh"` [BLOCK?]
- memory-toolkit | UserPromptSubmit | `(all)` | `node ${CLAUDE_PLUGIN_ROOT}/scripts/pipeline-hint.js` [INJ]
- memory-toolkit | PreCompact | `(all)` | `node ${CLAUDE_PLUGIN_ROOT}/scripts/session-save.js` 
- memory-toolkit | PostToolUse | `Bash(git commit*)` | `bash -c 'node ${CLAUDE_PLUGIN_ROOT}/scripts/memory.js note "COMMIT: $(git log --oneline -1 2>/dev/null)"'` 
- memory-toolkit | PostToolUse | `(all)` | `node ${CLAUDE_PLUGIN_ROOT}/scripts/session-watcher.js` 
- memory-toolkit | SubagentStop | `(all)` | `node ${CLAUDE_PLUGIN_ROOT}/scripts/session-watcher.js` 
- memory-toolkit | SessionStart | `(all)` | `node ${CLAUDE_PLUGIN_ROOT}/scripts/session-log.js` [INJ]
- tenet | SessionStart | `startup` | `command` [INJ]
- tenet | SessionStart | `compact` | `python3 "${CLAUDE_PLUGIN_ROOT}/tenet/cli.py" hook session-start --compact` [INJ]
- tenet | Stop | `(all)` | `python3 "${CLAUDE_PLUGIN_ROOT}/tenet/cli.py" hook stop` [BLOCK?]
- learn-wiki | SessionStart | `startup` | `clear` [INJ]
- oak-memory | UserPromptSubmit | `(all)` | `node "${CLAUDE_PLUGIN_ROOT}/dist/hook.mjs"` [INJ]
- claude-patterns | SessionStart | `(all)` | `python3 ${CLAUDE_PLUGIN_ROOT}/hooks/install-ping.py` [INJ][NET]
- rutter | Stop | `(all)` | `"${CLAUDE_PLUGIN_ROOT}"/hooks/librarian-stop.sh` [BLOCK?]
- career-brand | Notification | `(all)` | `bash -c 'title="Claude Code" msg="Career Brand needs your attention"; case "$(uname -s)" in Darwin) osascript -e "display notification \"$ms` 
- workflow-toolkit | SessionStart | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/session-start-hook.sh` [INJ]
- workflow-toolkit | Stop | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/journal-hook.sh` [BLOCK?]
- workflow-toolkit | PreCompact | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/pre-compact-hook.sh` 
- workflow-toolkit | PostToolUse | `Write` | `Bash` 
- workflow-toolkit | SubagentStop | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/subagent-stop-hook.sh` 
- workflow-toolkit | TaskCompleted | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/task-completed-hook.sh` 
- workflow-toolkit | SessionEnd | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/session-end-hook.sh` 
- maddog | PreToolUse | `Bash` | `${CLAUDE_PLUGIN_ROOT}/scripts/hooks/executor-guard.sh` [BLOCK?]
- maddog | PreToolUse | `Agent` | `${CLAUDE_PLUGIN_ROOT}/scripts/hooks/judge-dispatch-guard.sh` [BLOCK?]
- maddog | PreToolUse | `Read` | `Glob` [BLOCK?]
- pm-toolkit | SessionStart | `compact` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/context-reinject.sh"` [INJ]
- pm-toolkit | Stop | `(all)` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/quality-gate.sh"` [BLOCK?]
- pm-toolkit | PostToolUse | `Skill` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/usage-logger.sh"` 
- pm-toolkit | PostToolUse | `Skill` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/workflow-tracker.sh"` 
- pm-toolkit | PostToolUseFailure | `Skill` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/usage-logger.sh"` 
- memory-agent | SessionStart | `startup` | `clear` [INJ]
- memory-agent | SessionEnd | `(all)` | `MEMORY_AGENT_DATA="${CLAUDE_PLUGIN_DATA}" python3 "${CLAUDE_PLUGIN_ROOT}/adapters/agent/claude_code/hooks/session_end.py"` 
- memory-agent | PreCompact | `(all)` | `MEMORY_AGENT_DATA="${CLAUDE_PLUGIN_DATA}" python3 "${CLAUDE_PLUGIN_ROOT}/adapters/agent/claude_code/hooks/pre_compact.py"` 
- gangsta | SessionStart | `startup` | `compact` [INJ]
- wherewasi | SessionStart | `(all)` | `python3 ${CLAUDE_PLUGIN_ROOT}/tools/wherewasi.py on-session-start` [INJ]
- wherewasi | PreCompact | `(all)` | `python3 ${CLAUDE_PLUGIN_ROOT}/tools/wherewasi.py on-precompact` 
- wherewasi | UserPromptSubmit | `(all)` | `python3 ${CLAUDE_PLUGIN_ROOT}/tools/wherewasi.py on-user-prompt` [INJ]
- wherewasi | SessionEnd | `(all)` | `python3 ${CLAUDE_PLUGIN_ROOT}/tools/wherewasi.py on-session-end` 
- anchor-memory | SessionStart | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/session-context.sh` [INJ]
- anchor-memory | SessionStart | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/memory-integrity-scan.sh` [INJ]
- anchor-memory | Stop | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/memory-integrity-gate.sh` [BLOCK?]
- anchor-memory | Stop | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/session-checkpoint.sh` [BLOCK?]
- anchor-memory | PreCompact | `(all)` | `${CLAUDE_PLUGIN_ROOT}/hooks/session-checkpoint.sh` 
- wizard | SessionStart | `startup` | `compact` [INJ]
- sdlc-kit | PostToolUse | `Write` | `NotebookEdit` 
- claude-cognis | SessionStart | `(all)` | `node "${CLAUDE_PLUGIN_ROOT}/scripts/context-hook.cjs"` [INJ]
- claude-cognis | Stop | `(all)` | `node "${CLAUDE_PLUGIN_ROOT}/scripts/summary-hook.cjs"` [BLOCK?]
- claude-cognis | UserPromptSubmit | `(all)` | `node "${CLAUDE_PLUGIN_ROOT}/scripts/prompt-hook.cjs"` [INJ]
- memanto | SessionStart | `startup` | `command` [INJ]
- memanto | SessionStart | `startup` | `command` [INJ]
- memanto | PreCompact | `(all)` | `memanto` 
- memanto | PostToolUse | `Bash` | `python "${CLAUDE_PLUGIN_ROOT}/hooks/notify.py"` 
- memanto | PostToolUse | `Bash` | `python3 "${CLAUDE_PLUGIN_ROOT}/hooks/notify.py"` 
- jevmem | UserPromptSubmit | `(all)` | `"${CLAUDE_PLUGIN_ROOT}/hooks/jevmem-hook.sh" hook --plugin` [INJ]
- jevmem | Stop | `(all)` | `"${CLAUDE_PLUGIN_ROOT}/hooks/jevmem-hook.sh" --detach hook --plugin` [BLOCK?]
- jevmem | SessionStart | `(all)` | `"${CLAUDE_PLUGIN_ROOT}/hooks/jevmem-hook.sh" --start hook --plugin` [INJ]
- jevmem | PreToolUse | `Bash` | `Write` [BLOCK?]
- agent-recall | SessionStart | `(all)` | `agent-recall-session-start` [INJ]
- agent-recall | PostToolUse | `mcp__memory__.*` | `agent-recall-post-tool-use` 
- loop-and-gate-foundation | SessionStart | `(all)` | `${CLAUDE_PLUGIN_ROOT}/scripts/inject-operating-rules.sh` [INJ]
- loop-and-gate-foundation | SessionStart | `(all)` | `${CLAUDE_PLUGIN_ROOT}/scripts/session-start-hook.sh` [INJ]
- ux-superpowers | SessionStart | `(all)` | `Check if UX Superpowers plugin is installed. If it is, remember: before writing ` [INJ]
- shipwright | SessionStart | `(all)` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/run.sh" "${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py"` [INJ]
- shipwright | UserPromptSubmit | `(all)` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/run.sh" "${CLAUDE_PLUGIN_ROOT}/hooks/prompt_submit.py"` [INJ]
- shipwright | PreToolUse | `Edit` | `MultiEdit` [BLOCK?]
- shipwright | PostToolUse | `Edit` | `MultiEdit` 
- shipwright | Stop | `(all)` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/run.sh" "${CLAUDE_PLUGIN_ROOT}/hooks/stop_checklist.py"` [BLOCK?]
- whydone | Stop | `(all)` | `node "${CLAUDE_PLUGIN_ROOT}/cli/whydone.mjs" hook stop` [BLOCK?]
- agent-protocols | SessionStart | `(all)` | `bash ${CLAUDE_PLUGIN_ROOT}/hooks/session-start.sh` [INJ]
- compounded | SessionStart | `startup` | `clear` [INJ]
- compounded | Stop | `(all)` | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/skill_verify.py --check-pending` [BLOCK?]
- compounded | Stop | `(all)` | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/auto_propose.py` [BLOCK?]
- compounded | SessionEnd | `(all)` | `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/trust_ladder.py --process-session` 
- claude-memory | SessionStart | `(all)` | `bash ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/memory-context.sh` [INJ]
- pmm | SessionStart | `startup,resume,clear,compact` | `bash ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/session-start.sh` [INJ]
- pmm | Stop | `(all)` | `bash ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/should-save.sh` [BLOCK?]
- research-superpowers | SessionStart | `startup` | `compact` [INJ]
- research-superpowers | SessionStart | `startup` | `"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd" drift-check` [INJ]
- wiki-wonka | PreToolUse | `Write` | `command` [BLOCK?]
- wiki-wonka | PostToolUse | `Write` | `command` 
- wiki-wonka | FileChanged | `raw/` | `jq -r '"New file in raw/: " + .file_path + ". Say \"ingest\" to process it."'` 
- wiki-wonka | SessionStart | `compact` | `"$CLAUDE_PROJECT_DIR"/hooks/restore-context.sh` [INJ]
- wiki-wonka | Stop | `(all)` | `"$CLAUDE_PROJECT_DIR"/hooks/suggest-lint.sh` [BLOCK?]
- wiki-wonka | Stop | `(all)` | `osascript -e 'display notification "wiki-wonka done" with title "wiki-wonka"' 2>/dev/null ` [BLOCK?]
- wizard | SessionStart | `startup` | `compact` [INJ]
- handoff | SessionStart | `(all)` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/branch-handoff-load.sh"` [INJ]
- handoff | Stop | `(all)` | `bash "${CLAUDE_PLUGIN_ROOT}/hooks/branch-handoff-nudge.sh"` [BLOCK?]
- scaffold | Stop | `(all)` | `echo ''; echo '=== SESSION END ==='; echo 'Before you close:'; echo '  1. Run /context-save to persist state'; echo '  2. Update status file` [BLOCK?]
- scaffold | PostToolUse | `Bash` | `echo "$CLAUDE_TOOL_INPUT" ` 
- scaffold | PostToolUse | `Agent` | `echo "$CLAUDE_TOOL_INPUT" ` 
- scaffold | PreToolUse | `Bash` | `echo "$CLAUDE_TOOL_INPUT" ` [BLOCK?]
- scaffold | PreToolUse | `Write` | `echo "$CLAUDE_TOOL_INPUT" ` [BLOCK?]
- coach | SessionStart | `*` | `node "${CLAUDE_PLUGIN_ROOT}/hooks/session-start.mjs"` [INJ]
- fellowship | SessionStart | `startup` | `compact` [INJ]
- fellowship | SessionStart | `startup` | `compact` [INJ]
- fellowship | SessionStart | `startup` | `compact` [INJ]
- fellowship | SessionStart | `startup` | `compact` [INJ]
- fellowship | SessionStart | `resume` | `"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd" session-start --resume` [INJ]
- fellowship | SessionStart | `resume` | `"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd" fellowship-voice-session-start` [INJ]
- fellowship | SessionStart | `resume` | `"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd" fellowship-opener-session-start` [INJ]
- fellowship | SessionStart | `resume` | `"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd" fellowship-drift-check-session-start` [INJ]
- fellowship | PreToolUse | `Edit` | `MultiEdit` [BLOCK?]
- fellowship | PostToolUse | `(all)` | `"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd" fellowship-context-monitor` 
- fellowship | SessionEnd | `(all)` | `"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd" fellowship-session-end` 

### Plugin MCP servers (plugin | server | transport | target)
- shorty | shorty | http | `https://aishorty.com/api/mcp`
- enterprise-search | slack | http | `https://mcp.slack.com/mcp`
- enterprise-search | notion | http | `https://mcp.notion.com/mcp`
- enterprise-search | guru | http | `https://mcp.api.getguru.com/mcp`
- enterprise-search | atlassian | http | `https://mcp.atlassian.com/v1/mcp`
- enterprise-search | asana | http | `https://mcp.asana.com/v2/mcp`
- enterprise-search | google calendar | http | ` `
- enterprise-search | gmail | http | ` `
- pge-orchestrator | pge-orchestrator | stdio | `node ${CLAUDE_PLUGIN_ROOT}/bridge/mcp-server.cjs`
- graph-query-mcp | graph-query | stdio | `fastmcp run ${CLAUDE_PLUGIN_ROOT}/server.py`
- create-state | create-state | http | `https://createstate.ai/claude`
- legal | slack | http | `https://mcp.slack.com/mcp`
- legal | box | http | `https://mcp.box.com`
- legal | egnyte | http | `https://mcp-server.egnyte.com/mcp`
- legal | atlassian | http | `https://mcp.atlassian.com/v1/mcp`
- legal | docusign | http | `https://mcp.docusign.com/mcp`
- legal | google calendar | http | ` `
- legal | gmail | http | ` `
- oak-memory | oak-memory | stdio | `node ${CLAUDE_PLUGIN_ROOT}/dist/index.mjs`
- rutter | rutter | stdio | `node ${CLAUDE_PLUGIN_ROOT}/dist/stdio.js`
- tinyfish | tinyfish | http | `https://agent.tinyfish.ai/mcp`
- user-intuition-research | user-intuition | http | `https://mcp.userintuition.ai/mcp`
- research-desk | reference-lookup | stdio | `python3 ${CLAUDE_PLUGIN_ROOT}/servers/reference_lookup/server.py`
- research-desk | reference-lookup-hosted | http | `https://research-desk-checker.fly.dev/mcp`
- foundation | foundation | http | `https://mcp.foundation.unstructured.io/mcp`
- claude-cognis | cognis | stdio | `node ${CLAUDE_PLUGIN_ROOT}/scripts/mcp-server.cjs`
- jevmem | jevmem | stdio | `jevmem mcp`
- cobrain | cobrain | http | `https://cobrain.space/mcp`
- browser-use | browser-use | stdio | `uvx --python 3.12 browser-use@latest --cli-mcp`
- desktop-commander | desktop-commander | stdio | `npx -y @wonderwhy-er/desktop-commander@latest`
- mcpbinder | mcpbinder | http | `https://www.mcpbinder.com/api/mcp`
- career-compass | career-compass | stdio | `node ${CLAUDE_PLUGIN_ROOT}/server/build/src/index.js`
- data | snowflake | http | ` `
- data | databricks | http | ` `
- data | bigquery | http | `https://bigquery.googleapis.com/mcp`
- data | hex | http | `https://app.hex.tech/mcp`
- data | amplitude | http | `https://mcp.amplitude.com/mcp`
- data | amplitude-eu | http | `https://mcp.eu.amplitude.com/mcp`
- data | atlassian | http | `https://mcp.atlassian.com/v1/mcp`
- data | definite | http | `https://api.definite.app/v3/mcp/http`
- design | slack | http | `https://mcp.slack.com/mcp`
- design | figma | http | `https://mcp.figma.com/mcp`
- design | linear | http | `https://mcp.linear.app/mcp`
- design | asana | http | `https://mcp.asana.com/v2/mcp`
- design | atlassian | http | `https://mcp.atlassian.com/v1/mcp`
- design | notion | http | `https://mcp.notion.com/mcp`
- design | intercom | http | `https://mcp.intercom.com/mcp`
- design | google calendar | http | ` `
- design | gmail | http | ` `
- engineering | slack | http | `https://mcp.slack.com/mcp`
- engineering | linear | http | `https://mcp.linear.app/mcp`
- engineering | asana | http | `https://mcp.asana.com/v2/mcp`
- engineering | atlassian | http | `https://mcp.atlassian.com/v1/mcp`
- engineering | notion | http | `https://mcp.notion.com/mcp`
- engineering | github | http | `https://api.githubcopilot.com/mcp/`
- engineering | pagerduty | http | `https://mcp.pagerduty.com/mcp`
- engineering | datadog | http | `https://mcp.datadoghq.com/api/unstable/mcp-server/mcp`
- engineering | google calendar | http | ` `
- engineering | gmail | http | ` `
- productivity | slack | http | `https://mcp.slack.com/mcp`
- productivity | notion | http | `https://mcp.notion.com/mcp`
- productivity | asana | http | `https://mcp.asana.com/v2/mcp`
- productivity | linear | http | `https://mcp.linear.app/mcp`
- productivity | atlassian | http | `https://mcp.atlassian.com/v1/mcp`
- productivity | monday | http | `https://mcp.monday.com/mcp`
- productivity | clickup | http | `https://mcp.clickup.com/mcp`
- productivity | google calendar | http | ` `
- productivity | gmail | http | ` `

**Failed to connect:**
- data:definite: endpoint not found
- desktop-commander: 30s timeout
- engineering:github: Dynamic Client Registration 403
- graph-query-mcp and jevmem: `stdio` executable not found
- oak-memory: connection closed

**Needs OAuth (26 servers):** cobrain, create-state, data: amplitude, amplitude-eu, bigquery, hex; design: figma, intercom, linear; engineering: datadog, pagerduty; enterprise-search: asana, guru, notion; foundation; legal: atlassian, box, docusign, egnyte, slack; mcpbinder; productivity: clickup, monday; shorty; tinyfish; user-intuition.

**Outbound URLs found in hook scripts:**
- claude-patterns: `myceliumai.co/api/install`. This is an active install ping.
- graph-query-mcp: myceliumai.co
- jev (test scripts only): ai-gateway.vercel.sh, api.cloudflare.com, api.typesafe.ai, openrouter.ai
- jevmem and wizard: github.com

## 6. Skills, agents, commands and startup context
Per-plugin counts (name | version | skills | agents | commands | hooks | size KB):
-  :  skills,  agents,  cmds,  hooks,  KB
- shorty 1.1.0: 4 skills, 0 agents, 0 cmds, 0 hooks, 176 KB
- agent-architecture-designer 0.41.0: 0 skills, 60 agents, 62 cmds, 0 hooks, 45444 KB
- memory-bank 0.1.0: 1 skills, 0 agents, 0 cmds, 1 hooks, 33 KB
- enterprise-search 1.3.0: 5 skills, 0 agents, 0 cmds, 0 hooks, 51 KB
- pge-orchestrator 2.7.0: 16 skills, 10 agents, 0 cmds, 0 hooks, 396 KB
- build-companion 2.0.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 71 KB
- dev-forge 3.0.3: 0 skills, 0 agents, 4 cmds, 2 hooks, 68 KB
- graph-query-mcp 0.1.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 81 KB
- memory-toolkit 1.9.13: 11 skills, 0 agents, 0 cmds, 6 hooks, 338 KB
- create-state 1.1.0: 6 skills, 0 agents, 0 cmds, 0 hooks, 26 KB
- tenet 3.3.0: 3 skills, 0 agents, 0 cmds, 3 hooks, 336 KB
- context-window 0.5.4: 0 skills, 0 agents, 0 cmds, 0 hooks, 126 KB
- legal 1.3.0: 9 skills, 0 agents, 0 cmds, 0 hooks, 120 KB
- learn-wiki 0.1.1: 5 skills, 0 agents, 0 cmds, 1 hooks, 193 KB
- second-arrow 1.1.0: 1 skills, 0 agents, 1 cmds, 0 hooks, 2881 KB
- adaptive-agent : 2 skills, 0 agents, 0 cmds, 0 hooks, 17 KB
- oak-memory 0.2.0: 0 skills, 0 agents, 9 cmds, 1 hooks, 2749 KB
- scaffold 0.5.2: 1 skills, 0 agents, 0 cmds, 0 hooks, 356 KB
- agent-smith 2.5.1: 0 skills, 0 agents, 2 cmds, 0 hooks, 1260 KB
- claude-patterns 1.0.0: 1 skills, 0 agents, 0 cmds, 1 hooks, 51 KB
- memories 1.0.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 14 KB
- rutter 0.3.3: 0 skills, 0 agents, 0 cmds, 1 hooks, 1151 KB
- career-brand 0.3.0: 2 skills, 1 agents, 2 cmds, 1 hooks, 1583 KB
- prompt-coach 1.2.0: 1 skills, 1 agents, 0 cmds, 0 hooks, 8 KB
- workflow-toolkit 1.0.0: 21 skills, 2 agents, 0 cmds, 7 hooks, 112 KB
- maddog 4.3.3: 6 skills, 11 agents, 0 cmds, 3 hooks, 1223 KB
- claude-md-composer 1.0.2: 1 skills, 0 agents, 0 cmds, 0 hooks, 19 KB
- obsidian-notes 0.2.1: 1 skills, 0 agents, 0 cmds, 0 hooks, 526 KB
- pm-toolkit 1.9.1: 54 skills, 5 agents, 0 cmds, 5 hooks, 810 KB
- the-life-edit 6.0.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 316 KB
- tinyfish 1.4.0: 6 skills, 0 agents, 0 cmds, 0 hooks, 32 KB
- promptcolor 0.1.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 10 KB
- agent-guardrails 0.1.0: 3 skills, 0 agents, 0 cmds, 0 hooks, 52 KB
- snoozing-pet 0.3.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 912 KB
- user-intuition-research 1.3.3: 10 skills, 0 agents, 0 cmds, 0 hooks, 27 KB
- memory-agent 0.1.0: 0 skills, 0 agents, 0 cmds, 3 hooks, 2093 KB
- local-whisper 1.0.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 91 KB
- gangsta 1.11.6: 19 skills, 6 agents, 0 cmds, 1 hooks, 571 KB
- signal-hunter 2.1.0: 7 skills, 0 agents, 0 cmds, 0 hooks, 2557 KB
- wherewasi 0.1.0: 0 skills, 0 agents, 1 cmds, 4 hooks, 90 KB
- anchor-memory 0.1.0: 7 skills, 0 agents, 0 cmds, 5 hooks, 317 KB
- wizard 1.0.0: 12 skills, 1 agents, 6 cmds, 1 hooks, 2396 KB
- research-desk 0.4.1: 7 skills, 0 agents, 0 cmds, 0 hooks, 221 KB
- sdlc-kit 0.8.0: 11 skills, 0 agents, 0 cmds, 1 hooks, 622 KB
- product-discovery-flow 1.0.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 329 KB
- foundation 0.1.1: 5 skills, 0 agents, 0 cmds, 0 hooks, 25 KB
- shipwright 0.1.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 197 KB
- claude-cognis 1.1.0: 2 skills, 0 agents, 5 cmds, 3 hooks, 1204 KB
- memanto 0.2.0: 2 skills, 1 agents, 12 cmds, 5 hooks, 146 KB
- decision-council 1.18.0: 9 skills, 8 agents, 0 cmds, 0 hooks, 100 KB
- sensei 1.0.0: 14 skills, 0 agents, 0 cmds, 0 hooks, 136 KB
- glance 0.1.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 68 KB
- jevmem 0.7.6: 0 skills, 0 agents, 0 cmds, 4 hooks, 42 KB
- cobrain 1.0.7: 1 skills, 0 agents, 0 cmds, 0 hooks, 33 KB
- compact-on-idle 0.1.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 859 KB
- agent-ingest-audit-optimize 0.6.0: 1 skills, 0 agents, 1 cmds, 0 hooks, 2293 KB
- agent-recall 0.4.0: 0 skills, 0 agents, 0 cmds, 2 hooks, 471 KB
- browser-use : 0 skills, 0 agents, 0 cmds, 0 hooks, 2 KB
- obsidian-sync 0.1.0: 1 skills, 0 agents, 1 cmds, 0 hooks, 27 KB
- docbrain 1.0.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 38 KB
- loop-and-gate-foundation 0.5.0: 10 skills, 0 agents, 0 cmds, 2 hooks, 168 KB
- claude-md-management 1.0.0: 1 skills, 0 agents, 1 cmds, 0 hooks, 1078 KB
- desktop-commander 0.2.0: 6 skills, 0 agents, 0 cmds, 0 hooks, 78 KB
- ux-superpowers 1.0.0: 8 skills, 0 agents, 0 cmds, 1 hooks, 63 KB
- shipwright : 12 skills, 4 agents, 0 cmds, 5 hooks, 251 KB
- token-saver 0.2.0: 1 skills, 0 agents, 5 cmds, 0 hooks, 36 KB
- llm-wiki 3.2.0: 1 skills, 0 agents, 9 cmds, 0 hooks, 4757 KB
- whydone 1.4.1: 0 skills, 0 agents, 0 cmds, 1 hooks, 1033 KB
- agent-protocols 1.0.0: 25 skills, 8 agents, 0 cmds, 1 hooks, 381 KB
- reef 1.1.4: 13 skills, 1 agents, 0 cmds, 0 hooks, 430 KB
- compounded : 5 skills, 1 agents, 9 cmds, 4 hooks, 617 KB
- usage-line 0.3.1: 0 skills, 0 agents, 0 cmds, 0 hooks, 50 KB
- vault-anything 0.1.0: 2 skills, 2 agents, 0 cmds, 0 hooks, 235 KB
- claude-memory 1.0.0: 1 skills, 0 agents, 0 cmds, 1 hooks, 22 KB
- pmm 2.7.0: 12 skills, 0 agents, 0 cmds, 2 hooks, 356 KB
- 16-minds 0.3.0: 4 skills, 16 agents, 4 cmds, 0 hooks, 131 KB
- mindpowers 0.12.0: 6 skills, 0 agents, 0 cmds, 0 hooks, 590 KB
- bigquery 1.0.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 28 KB
- brightdata-plugin 1.9.0: 21 skills, 0 agents, 0 cmds, 0 hooks, 676 KB
- token-inspector 1.2.0: 8 skills, 0 agents, 0 cmds, 0 hooks, 39 KB
- research-superpowers 0.41.1: 17 skills, 7 agents, 0 cmds, 2 hooks, 2745 KB
- wiki-wonka 1.0.2: 3 skills, 1 agents, 0 cmds, 6 hooks, 3657 KB
- mcpbinder 1.2.0: 6 skills, 0 agents, 0 cmds, 0 hooks, 89 KB
- career-compass 2.15.1: 11 skills, 0 agents, 0 cmds, 0 hooks, 2479 KB
- wizard 1.0.0: 12 skills, 1 agents, 6 cmds, 2 hooks, 2396 KB
- project-memory 1.4.0: 1 skills, 0 agents, 2 cmds, 0 hooks, 86 KB
- handoff 1.0.0: 1 skills, 0 agents, 0 cmds, 2 hooks, 29 KB
- scaffold 1.0.0: 0 skills, 0 agents, 24 cmds, 5 hooks, 10296 KB
- jev 0.3.3: 0 skills, 0 agents, 0 cmds, 0 hooks, 59 KB
- data 1.1.0: 10 skills, 0 agents, 0 cmds, 0 hooks, 143 KB
- sarathi 0.8.0: 3 skills, 0 agents, 0 cmds, 0 hooks, 388 KB
- design 1.2.0: 7 skills, 0 agents, 0 cmds, 0 hooks, 32 KB
- coach 1.0.0: 8 skills, 8 agents, 0 cmds, 1 hooks, 22605 KB
- fellowship 1.2.0: 12 skills, 9 agents, 18 cmds, 11 hooks, 1707 KB
- create-smartfolder 6.6.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 283 KB
- analytics-office 0.28.0: 19 skills, 0 agents, 0 cmds, 0 hooks, 941 KB
- engineering 1.2.0: 10 skills, 0 agents, 0 cmds, 0 hooks, 34 KB
- cowork-plugin-management 0.2.2: 2 skills, 0 agents, 0 cmds, 0 hooks, 70 KB
- prompt-enhancer 1.0.5: 1 skills, 0 agents, 0 cmds, 0 hooks, 38 KB
- agent-design 0.1.0: 3 skills, 0 agents, 0 cmds, 0 hooks, 43 KB
- thinking-partner 1.0.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 79 KB
- agent-army 1.0.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 858 KB
- crayon 0.2.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 1445 KB
- mindmap 0.3.0: 2 skills, 0 agents, 0 cmds, 0 hooks, 135 KB
- context-vault 2.0.0: 2 skills, 0 agents, 0 cmds, 0 hooks, 213 KB
- obsidian-wiki : 0 skills, 0 agents, 0 cmds, 0 hooks, 14063 KB
- productivity 1.3.1: 4 skills, 0 agents, 0 cmds, 0 hooks, 133 KB
- snowflake 1.0.0: 1 skills, 0 agents, 0 cmds, 0 hooks, 32 KB
- task-observer 3.7.0: 0 skills, 0 agents, 0 cmds, 0 hooks, 716 KB

**Competing personas and boot instructions.** These are SessionStart hooks that inject a "using-X" meta-skill:

| Plugin | Injected skill (bytes on disk) | Observed additionalContext at first start |
|---|---|---|
| fellowship (Gandalf/LOTR team) | using-fellowship (28.8 KB) | 393 chars on resume ("FELLOWSHIP_DORMANT"), plus voice, opener and drift hooks |
| gangsta (mafia persona) | using-gangsta (10.9 KB) | about 10.5 KB (largest observed) |
| research-superpowers | using-research-powers (10.5 KB) | about 3.0 KB, plus drift-check |
| wizard (spells) | using-wizard (2.7 KB) | about 2.4 KB |
| agent-protocols | using-agent-skills (9.2 KB) | full SKILL.md, reported as an error-wrapped stdout "IMPORTANT" |
| loop-and-gate-foundation | inject-operating-rules | operating rules |
| memory-agent, compounded, claude-memory, claude-cognis, wherewasi, pmm, anchor-memory, memanto, tenet, learn-wiki, coach, shipwright, handoff | memory and status injects | about 0.1 to 1 KB each |

Each of these claims to be "the" entry point for tasks: gangsta's the-capo, fellowship's start, wizard's cast-spell, research-superpowers, agent-protocols, scaffold:start, dev-forge, sdlc-kit, shipwright and pge.

**Overlaps:**
- There are about 15 or more memory systems: memory-agent, memory-toolkit, memory-bank, claude-memory, claude-cognis, oak-memory, anchor-memory, compounded, pmm, memanto, jevmem, agent-recall, project-memory, wherewasi, whydone and handoff.
- There are 4 wiki systems: llm-wiki, obsidian-wiki, wiki-wonka and learn-wiki.
- These names are duplicated across plugins: plan, review, verify, session-start, session-end and reflect.
- Slack, Notion, Asana, Atlassian and Linear MCPs are each declared by 3 to 5 plugins.

**Startup context estimate:**
- Auto-mode classifier logs show `sys=141495` chars for the system prompt. That is about 140 KB, or about 35k tokens, and it includes the about 800-entry skill listing.
- The append-system-prompt file adds 18.9 KB.
- First-start SessionStart additionalContext adds about 16 to 20 KB.
- MCP tool definitions are deferred through ToolSearch. MCP server instructions add about 8 KB (browser-use is truncated to 4 KB, plus career-compass and github).
- **Total: about 180 KB, or about 45k tokens, before the first user message.** The tokenizer counts are redacted in the logs, so this is an estimate. Disabling the persona plugins and the extra memory and wiki plugins would cut a large share of it.

## 7. Repos and git
- No repos are cloned in `/home/user` (it is empty apart from this report). The only `.git` directories are toolchains: `/opt/rbenv` and `/opt/nvm`.
- Global git config:
  - `user.name=Claude`, `user.email=noreply@anthropic.com`
  - SSH commit signing: `gpg.ssh.program=/tmp/code-sign`, `commit.gpgsign=true`
  - `http.proxyauthmethod=basic`
  - git-lfs filters
- No `credential.helper` is set. Authentication goes through `GIT_ASKPASS` and the proxy's git config injection (`GIT_CONFIG_COUNT=3`, `GIT_CONFIG_KEY_0..2`; values not shown). `GH_TOKEN` and `GITHUB_TOKEN` are present (values redacted).

## 8. Environment variables (names only)
- **Credentials (redacted):** AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, GH_TOKEN, GITHUB_TOKEN, HF_TOKEN, QAI_HUB_API_TOKEN, CLOUDSDK_AUTH_ACCESS_TOKEN, CLAUDE_CODE_MESSAGING_TOKEN, CLAUDE_SESSION_INGRESS_TOKEN_FILE (a path).
- **Proxy and CA:** HTTPS_PROXY, https_proxy, NO_PROXY, no_proxy, GLOBAL_AGENT_*, DOCKER_HTTPS_PROXY, YARN_HTTPS_PROXY, npm_config_https_proxy, npm_config_noproxy, CLOUDSDK_PROXY_*, ELECTRON_GET_USE_PROXY, SSL_CERT_FILE, CURL_CA_BUNDLE, REQUESTS_CA_BUNDLE, NODE_EXTRA_CA_CERTS, GIT_SSL_CAINFO, PIP_CERT, AWS_CA_BUNDLE, DENO_CERT, DENO_TLS_CA_STORE, CARGO_HTTP_CAINFO, HEX_CACERTS_PATH, NIX_SSL_CERT_FILE, HTTPLIB2_CA_CERTS, GRPC_DEFAULT_SSL_ROOTS_FILE_PATH, CLOUDSDK_CORE_CUSTOM_CA_CERTS_FILE, BUN_TLS_EXTRA_DISTRUSTED_KEYS, UV_NATIVE_TLS, JAVA_TOOL_OPTIONS.
- **CCR platform:** CCR_AGENT_PROXY_*, CCR_ASYNC_REGISTER_WORKER, CCR_AUTO_MODE_*, CCR_DIAG_FLUSH_INTERVAL_S, CCR_EGRESS_GATEWAY_ENABLED, CCR_ENABLE_TRACING, CCR_OPUS_REMINDER_HOOK_BODY, CCR_OTLP_METRICS_INTERVAL_S, CCR_PRELOAD_CLAUDE, CCR_REPLY_STOP_HOOK_* (HOLDING_TOOL, LOCAL_CAP, REASON, TERMINAL_TOOLS), CCR_SESSION_PROFILE, CCR_SPAWN_TIMESTAMP_MS, CCR_UPSTREAM_PROXY_ENABLED, SESSION_INGRESS_URL, SBX_TELEMETRY_SOCKET, TRACEPARENT, IS_SANDBOX, ENVRUNNER_SKIP_ACK, ENV_MANAGER_ENABLE_DIAG_LOGS.
- **Claude Code:** CLAUDECODE, CLAUDE_CODE_* (about 70, including COORDINATOR_MODE, COORDINATOR_EXTRA_TOOLS, TERMINAL_MCP_TOOLS, MCP_ALWAYS_LOAD_JOIN_BEFORE_INPUT, SYNC_PLUGINS, SYNC_SKILLS, REMOTE_*, ARTIFACT_*, SESSION_ID, ACCOUNT_UUID, ORGANIZATION_UUID, USER_EMAIL), CLAUDE_* (EFFORT, MEMORY_STORES, PID, AUTOCOMPACT_PCT_OVERRIDE and others), ANTHROPIC_BASE_URL, API_TIMEOUT_MS, MAX_THINKING_TOKENS, MCP_CONNECTION_NONBLOCKING, MCP_TOOL_TIMEOUT, USE_SHTTP_MCP, DOCUMENTS_MCP_SCRATCH_ROOT, DISABLE_AUTOUPDATER, SKIP_PLUGIN_MARKETPLACE, AI_AGENT, AUTOPATCH_ENABLE_ASIMOV.
- **Git:** GIT_ASKPASS, GIT_CONFIG_COUNT, GIT_CONFIG_KEY_0..2, GIT_CONFIG_VALUE_0..2 (values redacted), GIT_EDITOR, GIT_TERMINAL_PROMPT, GCM_INTERACTIVE, GH_NO_UPDATE_NOTIFIER.
- **Toolchains and shell:** PATH, HOME, SHELL, PWD, OLDPWD, SHLVL, TERM, JAVA_HOME, NODE_OPTIONS, NODE_PATH, NPM_CONFIG_USERCONFIG, COREPACK_ENABLE_AUTO_PIN, BUN_*, RBENV_ROOT, RUSTUP_HOME, RUST_BACKTRACE, PIP_CONFIG_FILE, PYTHONUNBUFFERED, MATPLOTLIBRC, PLAYWRIGHT_*, FSSPEC_GCS, NIX_PROFILES, XDG_DATA_DIRS, DEBIAN_FRONTEND, YARN_NETWORK_CONCURRENCY, USE_BUILTIN_RIPGREP, COACH_PLUGIN_ROOT (set by a plugin).

## 9. Memory stores
- `/tmp/claude/memory/team/silo/` holds the team memory: `MEMORY.md`, `claw-toolkit-project.md`, `feedback-auto-merge-after-ci.md`, `feedback-mods-only-on-request.md`, `habit-tracker-cadence-build.md`, `plugins-panel-mod.md`, `user-environment.md`, `vault-dispatch-github-app.md`, plus `.memory-sync` and `.memory-sync-basis`. Most were synced at 21:10Z.
- `~/.claude/plugins/data/` has one directory per plugin, 39 in total. Nearly all are empty (4 KB). The non-empty ones are memory-agent-synced (20 KB) and shipwright-synced (8 KB).
- Plugin-written dirs: `~/.claude/compounded/`, `~/.claude/fellowship/`, `~/.claude/wherewasi/`.
- Project memory: `~/.claude/projects/-home-user/` holds only the session transcript and subagent transcripts. It has no MEMORY.md.
- The persistent project files in `/mnt/project-files/` are `habit-tracker/`, `plugins/` and `uploads/`.
