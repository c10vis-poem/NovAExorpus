# Slash commands and tools on this account (2026-10-30)

Everything below was read live from this cloud session on 2026-10-30: the plugin files on disk, the skills the session loaded, and each connector tool's own description. The built-in Claude Code commands come from the official page https://code.claude.com/docs/en/commands (read 2026-10-30; the page goes up to v2.1.288). Descriptions are cut to one line.

Sections:
1. Claude Code built-in slash commands
2. Slash commands from switched-on plugins
3. Skills you can call with /name (plugin skills, account skills, built-in skills)
4. Claude Code core tools (always on)
5. Connector (MCP) tools, grouped by connector
6. Connectors that failed to connect in this session

---

## 1. Claude Code built-in slash commands

Tags: [skill] = runs as a bundled skill. [plan] = depends on your plan, account or platform. Type `/help` inside a session for the exact list your version has.

- `/add-dir <path>`: add a working folder for this session.
- `/advisor [model|off]`: turn the advisor tool on or off.
- `/agents`: reminder to ask Claude to create or manage subagents.
- `/artifact-capabilities` [skill][plan]: load the reference for artifact runtime capabilities.
- `/artifact-diagramming` [skill][plan]: load diagramming guidance for artifacts.
- `/artifacts` [plan]: list, attach, open or copy links to your artifacts.
- `/auto-mode-setup` [plan]: draft and save auto-mode environment entries.
- `/autocompact [auto|<tokens>]`: set the auto-compact window.
- `/autofix-pr [prompt]`: start a cloud session that fixes CI failures and review comments on the current PR.
- `/background [prompt]` (also `/bg`): detach the session to run in the background.
- `/batch <instruction>` [skill]: run large parallel changes across the codebase in worktrees.
- `/branch [name]`: branch the conversation to try another direction.
- `/btw [question]`: ask a side question that stays out of the history.
- `/bug [report]` (also `/share`): report a bug or share the conversation.
- `/cd <path>`: move the session to another folder.
- `/chrome`: Claude in Chrome settings.
- `/claude-api [subcommand]` [skill]: load Claude API and Managed Agents reference.
- `/claude-in-chrome [task]` [skill][plan]: do a browser task through Claude in Chrome.
- `/clear [name]` (also `/reset`, `/new`): start a new conversation with empty context.
- `/code-review [level] [flags] [target]` (also `/review`) [skill]: review the current diff, a PR, branch or path.
- `/color [color|default]`: set the prompt bar color.
- `/compact [instructions]`: summarize the conversation to free context.
- `/config [key=value]` (also `/settings`): open settings or set a value.
- `/context [all]`: show context usage as a grid.
- `/copy [N]`: copy the last (or Nth) reply.
- `/cost`: alias for `/usage`.
- `/dataviz [request]` [skill]: design guidance for charts and dashboards.
- `/debug [description]` [skill]: turn on debug logging and troubleshoot.
- `/deep-research <question>` [workflow]: fan-out web research with a cited report.
- `/design [brief]` [skill][plan]: draft UI mockups as a Claude Design artifact.
- `/design consent`, `/design revoke` [plan]: grant or withdraw Claude Design access.
- `/design-login` [plan]: authorize design-system access for `/design-sync`.
- `/design-sync [hint]` [skill][plan]: upload the repo's React design system to Claude Design.
- `/desktop` (also `/app`) [plan]: continue the session in the desktop app.
- `/diff`: review working-tree changes.
- `/doctor [prompt-audit [path]]` (also `/checkup`) [skill]: setup checkup with proposed fixes.
- `/effort [level|auto|status|ultracode]`: set the effort level.
- `/exit` (also `/quit`): exit the CLI.
- `/export [filename]`: export the conversation as plain text.
- `/fast [on|off]`: toggle fast mode.
- `/feedback [report]`: send product feedback.
- `/fewer-permission-prompts` [skill]: add a read-only allowlist to project settings.
- `/focus`: toggle focus view (fullscreen renderer only).
- `/fork [prompt]`: copy the conversation into a new background session.
- `/goal [condition|clear]`: keep working across turns until a condition is met.
- `/heapdump`: write a heap snapshot (hidden; type it in full).
- `/help`: show help and available commands.
- `/hooks`: view hook configurations.
- `/ide`: manage IDE integrations.
- `/import [codex|gemini|cursor]` [plan]: import configuration from other tools.
- `/init`: create a CLAUDE.md for the project.
- `/insights` [plan]: HTML report on recent sessions.
- `/install-github-app`: install the Claude GitHub App on a repo.
- `/install-slack-app`: install the Claude Slack app.
- `/keybindings`: open the keyboard shortcuts file.
- `/list-agents` (also `/peers`): list subagents and sessions Claude can message.
- `/login`, `/logout`: sign in or out.
- `/loop [interval] [prompt]` (also `/proactive`) [skill]: repeat a prompt on an interval.
- `/mcp [reconnect|enable|disable]`: manage MCP servers and their sign-ins.
- `/memory`: edit CLAUDE.md files and auto memory.
- `/mobile` (also `/ios`, `/android`): QR code for the mobile app.
- `/model [model]`: switch model.
- `/output-style [style]`: list or switch output styles.
- `/passes` [plan]: share a free week of Claude Code.
- `/permissions` (also `/allowed-tools`): manage allow, ask and deny rules.
- `/plan [description]`: enter plan mode.
- `/plugin [subcommand]`: manage plugins.
- `/plugin-authoring` [skill]: reference for writing a mod.
- `/powerup`: interactive lessons on Claude Code features.
- `/privacy-settings` [plan: Pro, Max]: view and update privacy settings.
- `/radio`: open Claude FM lo-fi radio.
- `/rate-limit-options` [plan]: options when a usage limit blocks a request.
- `/recap`: one-line session summary.
- `/release-notes`: changelog with a version picker.
- `/reload-plugins [--force]`: reload plugins without restarting.
- `/reload-skills`: re-scan skill and command folders.
- `/remote-control` (also `/rc`) [plan]: make the session reachable from claude.ai.
- `/remote-env`: choose the default cloud environment.
- `/rename [name]`: rename the session.
- `/restart` (also `/update`) [plan]: restart and resume to apply an update.
- `/resume [session]` (also `/continue`): resume a past conversation.
- `/rewind` (also `/checkpoint`, `/undo`): rewind conversation and/or code.
- `/run` [skill]: launch and drive the project's app to check a change.
- `/run-skill-generator` [skill]: write a per-project skill for `/run` and `/verify`.
- `/sandbox` [plan]: toggle sandbox mode.
- `/schedule [description]` (also `/routines`) [plan]: manage cloud scheduled tasks.
- `/scroll-speed`: mouse wheel speed (fullscreen only).
- `/security-review`: security review of branch changes.
- `/setup-bedrock`, `/setup-vertex`: setup wizards (hidden unless that provider is on).
- `/simplify [target]` [skill]: clean up changed code and apply fixes.
- `/skill-doctor`: each skill's context cost and usage.
- `/skills`: list available skills.
- `/slides [brief]` [skill][plan]: create a Claude Slides artifact.
- `/stats`: alias for `/usage`.
- `/status`: settings on the Status tab.
- `/statusline`: configure the status line.
- `/stickers`: order Claude Code stickers.
- `/stop`: stop the background session you are attached to.
- `/subtask <task>`: spawn a forked background subagent that reports back.
- `/tasks` (also `/bashes`): view and manage background work.
- `/team-onboarding` [plan]: team onboarding guide from 30 days of usage.
- `/teleport` (also `/tp`) [plan]: pull a cloud session into this terminal.
- `/terminal-setup`: install a Shift+Enter newline binding.
- `/theme`: change the color theme.
- `/tui [default|fullscreen]`: set the terminal renderer.
- `/ultrareview [PR or branch]` [plan]: deep multi-agent cloud review.
- `/update-config [request]` [skill]: edit settings.json from a description.
- `/upgrade` [plan]: open the upgrade page.
- `/usage` (also `/cost`, `/stats`): session cost, plan limits and activity.
- `/usage-credits` [plan]: configure usage credits.
- `/verify` [skill]: confirm a change by building, running and observing the app.
- `/voice [hold|tap|off]` [plan]: voice dictation.
- `/web-setup`: connect GitHub for cloud sessions from local gh credentials.
- `/workflow-authoring` [skill]: reference for writing workflow scripts.
- `/workflows`: open the workflow progress view.
- Removed: `/pr-comments`, `/vim`, `/ultraplan`.

---

## 2. Slash commands from switched-on plugins

Read from each plugin's `commands/` folder. 35 plugins are switched on in `~/.claude/settings.json`; these 8 ship commands.

- `/agent-smith:analyze-agent`: full analysis of a Claude Code configuration.
- `/agent-smith:create-agent`: create a configuration.
- `/claude-md-management:revise-claude-md`: update CLAUDE.md with what this session learned.
- `/code-review:code-review`: review a pull request.
- `/consensus:config`: check and change the providers for consensus (models, add or remove providers).
- `/obsidian-sync:obsidian-sync`: sync project .md and .pdf docs to an Obsidian vault.
- `/plugin-dev:create-plugin`: guided plugin creation with design, build and validation.
- `/searchoclock:searchoclock`: date-aware deep research on the last failed command or a pasted error.

---

## 3. Skills you can call with /name

### 3a. Skills from plugins loaded in this session

- adb-mcp: `build-and-test` (Gradle build, tests, coverage), `crash-triage` (logcat root cause), `driving` (observe, locate, act on an Android screen), `getting-started` (boot an emulator), `pin-and-lock` (PIN pads and lock screen), `rn-expo` (React Native / Expo dev builds).
- adaptive-agent: `build-user-profile` (build the user profile memory), `skill-review` (audit skills for staleness).
- building-with-typesafe-jev: `building-with-typesafe-jev` (when code needs a language judgment: classify, route, score, gate).
- claude-bridge: `browser-bridge` (any web task; picks your signed-in Chrome or a headless browser).
- claude-context-optimizer (22): `cco` (control center), `cco-anatomy` (project map), `cco-budget` (token budget), `cco-claudemd` (CLAUDE.md bloat), `cco-clean` (reset tracking), `cco-coach` (grade your last prompt), `cco-config` (thresholds), `cco-digest` (weekly digest), `cco-doctor` (plugin health), `cco-export` (report export), `cco-git` (git-aware tips), `cco-overhead` (fixed context cost), `cco-pack` (best files for a task), `cco-patterns` (share file patterns), `cco-replay` (recent sessions), `cco-report` (token ROI), `cco-roi` (monthly savings), `cco-shield` (waste protection), `cco-task` (per-task tracking), `cco-templates` (context templates), `cco-tools` (tool token costs), `smart-loader` (suggest files to preload).
- claude-jev: `jev` (typed Choice/Noul/Score decisions through the TypeSafe API).
- claude-md-management: `claude-md-improver` (audit and improve CLAUDE.md files).
- consensus: `ask` (ask GPT-5.5, Gemini and DeepSeek at once through OpenRouter; paid, your keys).
- mcp-server-dev: `build-mcp-server`, `build-mcp-app` (interactive UI widgets), `build-mcpb` (bundled MCP server).
- memory-toolkit (11): `memory`, `memory-setup`, `docs-reflect`, `park`, `reflect`, `session-continue`, `session-end`, `session-insights`, `session-restore`, `session-start`, `task-template`.
- obsidian-notes: `obsidian-notes` (make markdown work as an Obsidian vault; link lint, indexes).
- obsidian-sync: `obsidian-sync`.
- plugin-dev (7): `agent-development`, `command-development`, `hook-development`, `mcp-integration`, `plugin-settings`, `plugin-structure`, `skill-development`.
- pmm, Poor Man's Memory (12): `dump`, `hydrate`, `init`, `init-local-skills`, `onboard`, `query`, `recall`, `save`, `settings`, `status`, `update`, `viz`.
- skill-creator: `skill-creator` (create, improve and measure skills).
- superpowers (15): `brainstorming`, `diagnosing-superpowers`, `dispatching-parallel-agents`, `executing-plans`, `finishing-a-development-branch`, `receiving-code-review`, `requesting-code-review`, `subagent-driven-development`, `systematic-debugging`, `test-driven-development`, `using-git-worktrees`, `using-superpowers`, `verification-before-completion`, `writing-plans`, `writing-skills`.
- build-companion: `build-companion` (board of what is built, in flight, unbuilt).

Plugin agents (called through the Agent tool, not /): `claude-bridge:browser-runner`, `claude-context-optimizer:context-analyzer`, `plugin-dev:agent-creator`, `plugin-dev:plugin-validator`, `plugin-dev:skill-reviewer`, `searchoclock:searchoclock-researcher`, `searchoclock:searchoclock-validator`.

### 3b. Your account skills (uploaded on claude.ai, called as `anthropic-skills:<name>`)

- `artifact-emulator`: open an artifact in the real viewer and screenshot it.
- `built-in-browser`: read before using the desktop app's in-app browser.
- `chrome-browser`: read before using Claude in Chrome.
- `computer-use`: read before doing anything in an app on your own computer.
- `deep-research`: multi-source research and comparisons.
- `docs`: editable shared docs (the default for any document).
- `docx`: Word documents.
- `google-workspace`: read before creating or changing a Google Drive, Docs, Sheets or Slides file.
- `import-memory`: import a memory export from another AI assistant.
- `learn`: explain how or why something works.
- `mcp-builder`: build MCP servers.
- `memory-as-skill`: your plain-markdown memory system (snapshot from 2026-07-05).
- `morning`: morning brief as an HTML artifact, or a weekday task.
- `pdf`: anything with PDF files.
- `pptx`: PowerPoint files.
- `skill-creator`: create and improve skills.
- `technical-builder-style`: your Technical Builder writing style.
- `termux-helper`: Termux on Android.
- `web-artifacts-builder`: multi-part React/Tailwind/shadcn artifacts.
- `xlsx`: spreadsheets.

### 3c. Built-in skills in this session

`artifact-design`, `artifact-diagramming`, `artifact-capabilities`, `dataviz`, `update-config`, `keybindings-help`, `code-review`, `simplify`, `fewer-permission-prompts`, `loop`, `claude-api`, `claude-in-chrome`, `run`, `plugin-authoring`, `init`, `security-review`, `session-start-hook`.

---

## 4. Claude Code core tools (always on)

- Bash: run shell commands.
- Read, Write, Edit, NotebookEdit: read and change files and notebooks.
- Glob, Grep: find files and search their contents.
- Agent: start a subagent (fork, general-purpose, Explore, Plan, web-fetch, claude-code-guide, statusline-setup, plus the plugin agents above).
- Skill: run a skill. ToolSearch: load a deferred tool's schema.
- WebSearch: web search (standard or extended). WebFetch: through the web-fetch agent in this session.
- Artifact, ArtifactComments, ArtifactData: publish and manage claude.ai artifacts, their comments and their shared data.
- Monitor: stream events from a long-running script.
- TaskCreate, TaskGet, TaskList, TaskUpdate, TaskStop: background task tracking.
- CronCreate, CronList, CronDelete: local scheduled jobs. ScheduleWakeup: self-paced /loop wake-ups.
- EnterWorktree, ExitWorktree: work in an isolated git worktree.
- ListConnectors, SearchMcpRegistry, SuggestConnectors: see and suggest connectors.
- ListPlugins, SearchPlugins, SuggestPluginInstall, ListSkills, SearchSkills, SuggestSkills, propose_skills: find and propose plugins and skills.
- ListMcpResourcesTool, ReadMcpResourceTool, ReadMcpResourceDirTool: read MCP resources.
- PushNotification: push a notice to your phone. SendMessage, ListAgents: message other agents and sessions.
- DesignSync: Claude Design sync. ReadNotifications, ReportFindings: notifications and code-review findings.
- Project thread tools (hearthbot): post_message, react, request_decision, update_progress_checklist, rename_thread, set_thread_resolved, message_coordinator, message_thread, read_thread, read_project_chat, list_threads, list_devices, connect_device, start_remote_control, suggest_connectors, list_original_project, read_original_project_chat, list_project_artifacts, list_prs, post_widget, switch_model, set_effort_level.

---

## 5. Connector (MCP) tools

### AppDeploy (build and host apps)
- `get_deploy_instructions`: workflow and starter files before building an app.
- `get_appdeploy_sdk_reference`: SDK reference for one feature (auth, database, AI, cron and more).
- `deploy_app`: publish or update an app at a public URL.
- `get_app_status`: deployment state, errors and logs.
- `get_apps`, `appdeploy_who_am_i`: list apps; account, credits and subscription.
- `get_app_versions`, `apply_app_version`: list stored versions; restore one.
- `src_glob`, `src_grep`, `src_read`: browse, search and read an app's stored source.
- `delete_app`: permanently delete an app (only on request).
- `create_secret_entry`, `get_secret_entry_status`, `get_secret_entry_instructions`, `list_app_secrets`, `set_app_secrets`, `delete_app_secrets`: secure secret entry and binding.
- `upload_resources`, `get_upload_status`, `get_resource_upload_instructions`, `set_app_resources`: binary resource uploads.
- `add_custom_domain`, `verify_custom_domain`, `delete_custom_domain`, `get_custom_domain_instructions`: custom domains.

### Claude Docs
- `batch`: create a doc or apply several edits at once. `create`, `update`, `delete`: one object (tab, contents, comment). `read`: a doc, tab or comment. `query`: comment history. `export`: a tab as pdf, docx, html, text, markdown or Notion. `guide`: usage guides.

### claude-code-remote (cloud sessions)
- `add_repo`, `register_repo_root`, `list_repos`: attach and list GitHub repos.
- `list_sessions`, `get_session`, `list_events`, `get_event`: read sessions and transcripts.
- `archive_session`, `unarchive_session`, `interrupt_session`, `set_session_title`, `set_session_tags`: manage sessions.
- `create_trigger`, `update_trigger`, `delete_trigger`, `fire_trigger`, `get_trigger`, `list_triggers`, `send_later`: scheduled tasks and reminders.
- `subscribe_pr_activity`, `unsubscribe_pr_activity`: watch PR events.
- `watch_url`, `unwatch_url`: inbound webhooks.
- `list_environments`, `confirm_repository_trust`, `read_documentation`: environments, trust prompts, environment docs.

### Claude in Chrome (your signed-in browser)
- `tabs_context_mcp`, `tabs_create_mcp`, `tabs_close_mcp`: tab group and tabs.
- `navigate`, `computer` (click, type, scroll, screenshot, zoom), `browser_batch` (several actions in one call).
- `read_page` (accessibility tree), `get_page_text`, `find` (elements by description), `form_input`.
- `javascript_tool`, `read_console_messages`, `read_network_requests`.
- `gif_creator`, `upload_image`, `resize_window`.
- `list_connected_browsers`, `select_browser`, `shortcuts_list`, `shortcuts_execute`.

### Chrome DevTools (claude-bridge plugin)
- Pages: `list_pages`, `new_page`, `select_page`, `close_page`, `navigate_page`, `resize_page`, `emulate`.
- Input: `click`, `hover`, `drag`, `fill`, `fill_form`, `type_text`, `press_key`, `upload_file`, `handle_dialog`, `wait_for`.
- Inspect: `take_snapshot`, `take_screenshot`, `evaluate_script`, `list_console_messages`, `get_console_message`, `list_network_requests`, `get_network_request`.
- Performance: `performance_start_trace`, `performance_stop_trace`, `performance_analyze_insight`, `lighthouse_audit`, `take_heapsnapshot`.

### GitHub
- Repos and files: `get_file_contents`, `create_or_update_file`, `push_files`, `delete_file`, `create_branch`, `list_branches`, `fork_repository`, `create_repository`.
- Commits, tags, releases: `get_commit`, `list_commits`, `list_tags`, `get_tag`, `list_releases`, `get_latest_release`, `get_release_by_tag`.
- Issues: `issue_read`, `issue_write`, `list_issues`, `search_issues`, `add_issue_comment`, `update_issue_comment`, `sub_issue_write`, `list_issue_types`, `list_issue_fields`, `get_label`.
- Pull requests: `create_pull_request`, `update_pull_request`, `pull_request_read`, `list_pull_requests`, `search_pull_requests`, `merge_pull_request`, `update_pull_request_branch`, `enable_pr_auto_merge`, `disable_pr_auto_merge`, `request_copilot_review`.
- Reviews: `pull_request_review_write`, `add_comment_to_pending_review`, `add_reply_to_pull_request_comment`, `resolve_review_thread`, `unresolve_review_thread`.
- Actions and CI: `actions_list`, `actions_get`, `actions_run_trigger`, `get_job_logs`, `get_check_run`.
- Search and people: `search_code`, `search_commits`, `search_repositories`, `search_users`, `get_me`, `get_teams`, `get_team_members`, `list_repository_collaborators`.
- Security: `run_secret_scanning`.

### Gmail
- Read: `search_threads`, `get_thread`, `get_message`, `list_drafts`, `get_draft`, `list_labels`.
- Write: `create_draft`, `update_draft`, `delete_draft`, `send_message`, `reply`, `forward`.
- Labels: `create_label`, `update_label`, `delete_label`, `label_message`, `label_thread`, `unlabel_message`, `unlabel_thread`, `update_message_labels`.
- Trash and spam: `trash_message`, `trash_thread`, `untrash_message`, `untrash_thread`, `mark_message_spam`, `mark_thread_spam`, `unmark_message_spam`, `unmark_thread_spam`, `apply_sensitive_message_label`, `apply_sensitive_thread_label`.

### Google Calendar
- `list_calendars`, `list_events`, `search_events`, `get_event`, `create_event`, `update_event`, `delete_event`, `respond_to_event`, `suggest_time` (free slots across calendars).

### Google Drive
- `search_files`, `list_recent_files`, `get_file_metadata`, `get_file_permissions`, `read_file_content`, `download_file_content`, `create_file`, `copy_file`, `update_file` (metadata, move, lock), `share_file`, `trash_file`.

### Google Docs
- `read_doc` (JSON of a doc), `update_doc` (batch edits).

### Google Cloud BigQuery
- `execute_sql_readonly` (SELECT only, preferred), `execute_sql` (any SQL), `get_query_results`, `get_job`, `cancel_job`, `list_dataset_ids`, `get_dataset_info`, `list_table_ids`, `get_table_info`.

### Hugging Face (signed in as Mer0vin8ian)
- `hf_fs`: browse the Hub like a filesystem (trending, search, read files and papers).
- `hub_repo_search`, `hub_repo_details`: search and inspect models, datasets, Spaces.
- `dynamic_space`: run tasks through Spaces (image generation, OCR, text to speech and more).
- `hf_whoami`: current account.

### Indeed
- `search_jobs`, `get_job_details`, `get_company_data` (reviews, salaries, ratings), `get_resume`.

### Perplexity Computer
- `import-claude-dashboard-from-url`, `read_thread`, `list_thread_assets`, `create_asset_download`.

### Replit
- `create_app_from_prompt`, `update_app_using_prompt`, `ask_question` (about an app without changing it).
- `search_apps`, `list_apps`, `resolve_app_by_name`, `list_app_files`, `read_app_file`.
- `publish_app`, `get_publish_status`, `import-claude-design-from-url`, `get-design-import-job-status`.

### Supabase
- Projects and orgs: `list_projects`, `get_project`, `create_project`, `pause_project`, `restore_project`, `list_organizations`, `get_organization`, `get_project_url`, `get_publishable_keys`.
- Database: `list_tables`, `list_extensions`, `list_migrations`, `apply_migration`, `execute_sql`, `generate_typescript_types`.
- Edge functions: `list_edge_functions`, `get_edge_function`, `deploy_edge_function`, `create_edge_function_secret`.
- Branches: `create_branch`, `list_branches`, `merge_branch`, `rebase_branch`, `reset_branch`, `delete_branch`.
- Health and docs: `get_advisors`, `query_logs`, `search_docs`.

### TinyFish (web search, fetch, automation)
- Search and fetch: `search`, `fetch_content`, `get_search_usage`, `list_fetch_usage`.
- Browser automation: `run_web_automation`, `run_web_automation_async`, `wait_for_run`, `get_run`, `list_runs`, `cancel_run`, `batch_status`, `batch_cancel`.
- Browser sessions: `create_browser_session`, `list_browser_sessions`, `close_browser_session`.
- Deep research: `start_deep_research`, `get_deep_research`, `list_deep_research`, `cancel_deep_research`.
- Datasets: `plan_dataset`, `create_dataset`, `populate_dataset`, `get_dataset`, `get_dataset_rows`, `list_datasets`, `cancel_dataset_run`, `delete_dataset`.
- Monitors: `create_monitor`, `list_monitors`, `get_monitor`, `run_monitor`, `pause_monitor`, `resume_monitor`, `cancel_monitor`.
- Wallet: `get_wallet`, `top_up_wallet`, `guide_next_step`.

### ToolRouter
- Run tools: `discover` (search the catalogue), `route` (run from a plain-language intent), `use_tool` (run one skill with explicit inputs).
- Account and billing: `account_setup`, `account_list`, `account_switch`, `account_preferences`, `credits_balance`, `credits_usage`, `invoice_list`.
- Brain (knowledge store): `brain_add`, `brain_query`, `brain_update`, `brain_delete`, `brain_expand`, `brain_status`, `brain_wings`, `brain_lint`, `brain_settings`, `brain_admin`.
- Connectors and keys: `connector_add`, `connector_list`, `connector_remove`, `connector_permissions`, `credential_save`, `credential_list`, `credential_delete`, `credential_default`, `credential_guide`, `key_create`, `key_list`, `key_delete`.
- Files and jobs: `file_write`, `file_read`, `file_list`, `file_delete`, `job_get`, `job_list`, `job_cancel`.
- Media libraries: `persona_list`, `outfit_list`, `product_list`, `scene_list`.
- Feedback: `feedback_debug`, `feedback_request_tool`, `feedback_review`.

### Playwright (playwright plugin)
- `browser_navigate`, `browser_navigate_back`, `browser_tabs`, `browser_close`, `browser_resize`.
- `browser_click`, `browser_hover`, `browser_drag`, `browser_drop`, `browser_type`, `browser_press_key`, `browser_select_option`, `browser_fill_form`, `browser_file_upload`, `browser_handle_dialog`, `browser_wait_for`.
- `browser_snapshot`, `browser_take_screenshot`, `browser_find`, `browser_evaluate`, `browser_run_code_unsafe`, `browser_console_messages`, `browser_network_requests`, `browser_network_request`, `browser_emulate_media`.

---

## 6. Connectors that failed to connect in this session

These are configured but did not start, so their tools were not available:
- `adb-mcp` (adb): the command was not found in this container.
- `context7`: the network proxy refused it.
- `github` plugin server: the network proxy refused it (the separate GitHub connector above works).
- `jevmem`: the command was not found in this container.
