# Active rules, hooks and plugins (this session, 2026-10-30)

This is a read-only snapshot of the cloud container this thread runs in, which started at 00:04 UTC. Nothing was changed, disabled or run.
`<synced>` stands for `/root/.claude/plugins/synced/a5d13a90-190b-42eb-ad1b-69c924919b1b_b410cc73-6e72-411c-a9de-4edf62ec27d7/`.

---

## 1. Hooks registered in the harness settings

**Source:** `/root/.claude/settings.json`. The platform generates this file at container start, and its `permissions.deny` list blocks edits to it.

| Event | Matcher | Command | What it does |
|---|---|---|---|
| PostToolUse | (all) | `~/.claude/posttooluse-hearth-status-nudge.py` | After a stretch of tool calls with nothing shown to the user, it injects a reminder to refresh the checklist. It never blocks. |
| SessionStart | (all) | `~/.claude/session-start-setup-script-failure.sh` | If the environment's setup script failed, it tells the model to fix it. It stays silent otherwise. |
| Stop | (all) | `~/.claude/stop-hook-git-check.sh` | Checks for uncommitted or unpushed git work. It exits early when there's no repo. |
| Stop | (all) | `~/.claude/stop-hook-reply-gate.py` | **Blocks** the end of a turn until a reply tool has been called. It re-prompts a limited number of times, then lets the turn end. |
| UserPromptSubmit | (all) | `~/.claude/user-prompt-submit-reply-reminder.py` | Injects: "Text you emit directly is not delivered… End your turn with post_message or no_reply_needed." |

The same file also sets:
- `permissions.allow`: `Skill`.
- `permissions.deny`: reading `~/.claude/remote` and `/run/ccr`, and editing `launcher-settings.json`, `stop-hook-git-check.sh` and `user-prompt-submit-reply-reminder.py`.
- `autoMode.environment`: a credential-handling rule for the env vars `HF_TOKEN` and `QAI_HUB_API_TOKEN`.
- `switchModelsOnFlag: true`.

Other files checked:
- `/root/.claude/launcher-settings.json` sets no hooks of its own and mirrors the file above.
- `/root/.claude/settings.json` (user level) holds only `enabledPlugins`, with no hooks, rules or permissions.
- Not present: `/etc/claude-code` (managed settings), `~/.claude/CLAUDE.md`, `~/.claude/rules/`, and any CLAUDE.md or `.claude/` in `/home/user`.

---

## 2. Plugins enabled in `/root/.claude/settings.json`

The settings list 483 synced plugins. **35 are enabled**, 26 of those have files on disk, and 9 are enabled but have no files downloaded.

### 2a. Enabled plugins with hooks (9)

**claude-context-optimizer v4.12.1** (`<synced>43b5eda8…/hooks/hooks.json`)
- PreToolUse, matcher `Read`, runs `src/read-cache.js`. **Can block a Read** of a file already read this session (`decision: block`, lines 304, 351 and 408). It allows the re-read once enough other context has loaded.
- PreToolUse, matcher `Read`, runs `src/context-shield.js`. Warns about files that were "wasted" in earlier sessions.
- UserPromptSubmit, all prompts, runs `src/prompt-coach.js`. Injects the "[prompt-coach] Prompt quality: D…" grade.
- PostToolUse, matcher `Edit|Write`, runs `src/read-cache.js`.
- PostToolUse, matcher `Bash|Read|Edit|Write|Glob|Grep|Agent|mcp__.*`, runs `tracker.js` and `budget.js`.
- PreCompact runs `read-cache.js` and `tracker.js`.
- SessionStart runs `tracker.js` and `tasks.js`.
- SessionEnd runs `tracker.js` and `dashboard.js`.

**consensus v1.7.3** (`<synced>a1fc638c…/hooks/hooks.json`)
- SessionStart runs `scripts/check-setup.sh`. Checks for `uv` and API keys. It's informational and never blocks.

**jevmem v0.7.6** (`<synced>7d57870a…/hooks/hooks.json`)
- UserPromptSubmit runs `hooks/jevmem-hook.sh hook --plugin`.
- Stop runs `jevmem-hook.sh --detach hook --plugin`.
- SessionStart runs `jevmem-hook.sh --start hook --plugin`.
- PreToolUse, matcher `Bash|Edit|Write`, runs `jevmem-hook.sh --guard hook --plugin`.
- All of these are opt-in: they do nothing unless a project has a `jevmem.config.json`. The jevmem CLI isn't installed here, and its MCP server failed to connect.

**memory-toolkit v1.9.13** (`<synced>07e6b314…/hooks/hooks.json`)
- UserPromptSubmit runs `scripts/pipeline-hint.js`. It reacts only to `/skill` prompts, and only when debug mode is on.
- PreCompact runs `scripts/session-save.js`.
- PostToolUse, matcher `Bash(git commit*)`, saves a memory note "COMMIT: …".
- PostToolUse, all tools, runs `scripts/session-watcher.js`. **It sends transcript excerpts to Haiku** and saves its findings to memory. It throttles itself.
- SubagentStop runs `scripts/session-watcher.js`.
- SessionStart runs `scripts/session-log.js`.

**pmm v2.7.0** (`<synced>b907fbde…/hooks/hooks.json`)
- SessionStart, matcher `startup,resume,clear,compact`, runs `hooks/scripts/session-start.sh`. It printed `<!-- pmm:not-initialized -->` this session.
- Stop runs `hooks/scripts/should-save.sh`. **Can block a stop** ("PMM save threshold reached, run pmm:save") when `./memory/config.md` sets an every-N cadence. It's inactive here because no config exists.

**searchoclock v0.3.0** (`<synced>ed67ab32…/hooks/hooks.json`)
- PostToolUseFailure, matcher `Bash`, runs `bash searchoclock.sh`. Injects research context after a Bash failure. It never blocks.
- PostToolUse, matcher `Bash`, runs `bash searchoclock.sh`. This is a backup for the trigger above.
- PreToolUse, matcher `Bash`, runs `bash searchoclock.sh preflight`. It's off unless "proactive" mode is set. When on, it can return `ask` or `deny` for destructive commands (lines 651 to 654).

**superpowers v6.4.2** (`<synced>6ba53849…/hooks/hooks.json`)
- SessionStart, matcher `startup|clear|compact`, runs `hooks/run-hook.cmd session-start`. Injects the full `using-superpowers` skill, which includes: "If you think there is even a 1% chance a skill might apply… you ABSOLUTELY MUST invoke the skill", "Invoke relevant or requested skills BEFORE any response or action", and a "Red Flags" table. This conflicts with your standing rules.

**Mod-style plugins.** These use the newer `modules` hooks format, not classic events:
- **cache-ttl-timer v1.0.0** registers `session.start` (`hooks/register.js`). It draws a prompt-cache countdown in the footer.
- **clawd-pet v1.0.6** registers `session.start` (`hooks/register.tsx`). It draws a pet above the prompt.
- **harness-scope v0.1.3** (`hooks/register.ts`) can hide skills, rules, agents and tools per repo through profiles. It does nothing without a repo's `.claude/harness-scope.json`, and none exists here.
- **jev v0.3.3** registers `engine.create` (`hooks/register.ts`). It adds `$.jev` typed-decision calls for other plugins.

### 2b. Enabled plugins without hooks: skills, commands, agents and MCP servers

- **adb-mcp v0.23.0**
  - Skills: build-and-test, crash-triage, driving, getting-started, pin-and-lock, rn-expo.
  - MCP: `adb`, which failed to connect because the executable wasn't found.
- **agent-smith v2.5.1**
  - Commands: analyze-agent, create-agent.
  - Has a `CLAUDE.md` and a `.claude/settings.json` inside the plugin folder. These are the plugin's own repo files and aren't loaded into sessions.
- **building-with-typesafe-jev v0.3.0**
  - Skill: building-with-typesafe-jev.
- **claude-bridge v0.1.0**
  - Skill: browser-bridge.
  - Agent: browser-runner.
  - MCP: `chrome-devtools`, which connected.
- **claude-jev v0.1.1**
  - Skill: jev.
  - MCP: `jev`.
- **claude-md-management v1.0.0**
  - Skill: claude-md-improver.
  - Command: revise-claude-md.
- **code-review v1.0.1**
  - Command: code-review.
- **consensus**
  - Skill: ask.
  - Command: config.
  - Has a `CLAUDE.md` in the plugin folder, which isn't loaded.
- **context7**
  - MCP: `context7`, which failed because the proxy refused the tunnel.
- **github**
  - MCP: `github`, which failed with a 403 from the proxy. The connector version of GitHub is separate (section 4).
- **mcp-server-dev**
  - Skills: build-mcp-app, build-mcp-server, build-mcpb.
- **obsidian-notes v0.2.1**
  - Skill: obsidian-notes.
  - Has `CLAUDE.md` and `AGENTS.md` in the plugin folder, which aren't loaded.
- **obsidian-sync v0.1.0**
  - Skill and command: obsidian-sync.
- **playwright**
  - MCP: `playwright`, which connected.
- **plugin-dev**
  - Skills: agent-development, command-development, hook-development, mcp-integration, plugin-settings, plugin-structure, skill-development.
  - Command: create-plugin.
  - Agents: agent-creator, plugin-validator, skill-reviewer.
- **skill-creator**
  - Skill: skill-creator.
- **Skills of plugins listed in 2a:**
  - claude-context-optimizer: cco, cco-anatomy, cco-budget, cco-claudemd, cco-clean, cco-coach, cco-config, cco-digest, cco-doctor, cco-export, cco-git, cco-overhead, cco-pack, cco-patterns, cco-replay, cco-report, cco-roi, cco-shield, cco-task, cco-templates, cco-tools and smart-loader, plus the context-analyzer agent.
  - memory-toolkit: docs-reflect, memory, memory-setup, park, reflect, session-continue, session-end, session-insights, session-restore, session-start, task-template.
  - pmm: dump, hydrate, init, init-local-skills, onboard, query, recall, save, settings, status, update, viz.
  - searchoclock: the searchoclock command, plus the searchoclock-researcher and searchoclock-validator agents.
  - superpowers: brainstorming, diagnosing-superpowers, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills.

None of these skills or agents declare `hooks:` in their frontmatter.

### 2c. Enabled but no files on disk (9)

agent-engineering, agent-protocols, agentkeeper, akc-cycle, context-bar, gas-gauge, hookify, maddog, supabase. These load nothing in this session. Supabase still runs here as a claude.ai connector.

---

## 3. Account skills synced from claude.ai

**Source:** `/root/.claude/skills/synced/a5d13a90…/`

artifact-emulator, built-in-browser, chrome-browser, computer-use, deep-research, docs, docx, google-workspace, import-memory, learn, mcp-builder, memory-as-skill, morning, pdf, pptx, skill-creator, technical-builder-style, termux-helper, web-artifacts-builder, xlsx.

The platform also adds the skill `/root/.claude/skills/session-start-hook/SKILL.md` (startup-hook-skill). None of these declare hooks.

Platform built-in skills also appear in the listing: dataviz, artifact-design, artifact-diagramming, artifact-capabilities, update-config, keybindings-help, code-review, simplify, fewer-permission-prompts, loop, claude-api, claude-in-chrome, run, plugin-authoring, init, security-review.

---

## 4. Connectors (MCP) loaded from claude.ai

AppDeploy, Claude Docs, Gmail, Google Calendar, Google Cloud BigQuery, Google Docs, Google Drive, Hugging Face, Indeed, Perplexity Computer, Replit, Supabase, TinyFish, toolrouter, claude-in-chrome, GitHub (connector) and claude-code-remote. They carry server instructions but no hooks.

---

## 5. Rule text that reaches the model

**a. Your claude.ai profile preferences**, injected into every session's system prompt. In summary:
- "STOP GUESSING". If code fails, research a fix and/or create or use a skill.
- Don't conserve tokens by skipping connectors, web searches or skills.
- Never guess what's in a shared file. If given a link, read everything.
- Do a web search first before answering a question.
- Be concise, with no repetition. Give one step at a time, think first, and don't gaslight.
- Read the chat thread's consolidation, audit and failure logs first if it's not a new chat.
- "Create a skills if you don't already have them". This conflicts with the project-memory rule "no skills without explicit direction".

**b. Project memory**, at `/tmp/claude/memory/team/silo/`:
- `MEMORY.md` holds your standing rules from 2026-10-29:
  - No rules, scripts, hooks, skills or tools without your explicit direction, and show the content first.
  - No building unless directed.
  - No subagents until you've gone over how they'll be deployed.
  - No failure loops while waiting on you.
  - No subscriptions to PRs or APIs without direction.
  - A half-answered question isn't answered.
  - Never offer only yes/no or A/B/C options.
  - Every script or hook must be disableable mid-session, and nothing may block reading files or following your direction.
  - Disable all hooks and list every rule.
- `novaexorpus-corpus-handoff.md`:
  - Read every doc end to end, and never invent rules.
  - Stay inside NovÆxorpus repos.
  - Vendor docs go in `raw/`.
  - mem0 needs a matching user_id.
  - Answer questions before acting. A deny counts as an unanswered question.
- `feedback-plugins-are-parts.md`: judge plugins part by part, never by their hooks, and deep-read before recommending.
- `memory-as-skill-design.md`: show the exact SKILL.md, script and hook text before writing anything.
- `plugin-sync-across-accounts.md` and `rules-hooks-inventory.md`: reference notes only, with no rules.

**c. Project instructions:** none are set for this project. The session context carries only the PR-attribution rule.

**d. Platform system prompt** for project threads. It has many rules. The ones that affect behavior most are:
- Reply only through `mcp__hearthbot__*` tools.
- Keep a progress checklist.
- Don't spawn subagents unless asked.
- Confirm irreversible steps.
- Auto-watch PRs you create. This conflicts with your "no subscriptions without direction" rule.

**e. Hook-injected text this session:**
- superpowers: the "MUST invoke skills" block in 2a.
- prompt-coach: the prompt grade and suggestions.
- pmm: `pmm:not-initialized`.
- The reply reminder from section 1.

---

## 6. Hooks that can block, in one place

1. `stop-hook-reply-gate.py` (harness) blocks the end of a turn without a reply tool call. It's capped and fails open.
2. claude-context-optimizer `read-cache.js` **blocks repeated Reads**. This is the only one here that can stop a file read.
3. pmm `should-save.sh` blocks a stop at the save cadence. It's inactive here because there's no `memory/config.md`.
4. searchoclock preflight can ask or deny destructive Bash commands, but only if proactive mode is configured. It's off by default.
5. jevmem `--guard` (PreToolUse on Bash, Edit and Write) is opt-in per project. It's inactive here.

The hooks named in the earlier thread (project-boundary, construction-gate from claude-meta-skills) are **not enabled** in this container's settings.

## Not read

- The other 448 synced plugins that are turned off: 406 are downloaded but off and 42 aren't downloaded. The earlier catalog covers them: https://claude.ai/artifact/R3Xc8Mk95RCD7998h3KvUD
- Repo-level rules (Aesop-Xi `.claude/settings.json` with 35 hooks, Hyperion-XI `rules/`). No repo is attached to this session. The earlier inventory covers them: https://claude.ai/artifact/7VegGyMfpKpr9MUWRsQp1h
- Your second account, your devices and the phone's `~/.claude`, which can't be reached from this container.
