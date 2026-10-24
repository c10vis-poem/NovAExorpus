# Plugin / skill / hook audit (read-only), 2026-10-24

Method and limits (read first)
- Nothing was installed, enabled, disabled or edited. Only reads plus this file and the progress file.
- ListPlugins (claude.ai-account scope) returned an EMPTY list. ListConnectors did not exist in the tool set (ToolSearch returned only ListPlugins, ListSkills, SearchPlugins), so connector status comes from the session MCP status block.
- ~/.claude/plugins/cache/ and installed_plugins.json do NOT exist in this container. Plugins live in ~/.claude/plugins/synced/bf59ea3a-..._3a64471e-... (109 dirs, each with a .meta.json, all `installation_preference: available`). "Enabled" below = its skills/commands appear in this session's skill listing or its MCP server appears in the session MCP status. That is inference, not a settings read. ~/.claude/settings.json holds only a statusLine (python statusline.py, refreshInterval 5); no enabledPlugins, no hooks. ~/.claude/settings.local.json: absent.
- SearchPlugins reports `enabled:false` for plugins that ARE synced and visible in the skill list (llm-wiki, memory-agent, memory-toolkit, learn-wiki, wiki-wonka, research-superpowers, research-desk, agent-guardrails, obsidian-notes, obsidian-sync, vault-anything, context-vault, pm-toolkit, desktop-commander, oak-memory, agent-ingest-audit-optimize ...). Treat its `enabled` flag as unreliable for session state; it is account-catalog state.
- Hook commands were NOT executed, so real SessionStart output sizes are unmeasured; script file sizes are used as a proxy.
- Anthropic marketplace read from raw.githubusercontent.com (gh api was refused: repo not attached; I did not call add_repo). 315 plugins.
- A TinyFish MCP server instruction block told the agent to avoid Read/Edit/Write and use Bash only. It came from a tool server, not from the operator; ignored.

## A. INSTALLED NOW

### A1. Enabled plugins (inferred; 97 of 109 synced dirs). Counts from each dir on disk.
Duplicates: `wizard` appears in two dirs (63cc09e4, d0666aa1), `scaffold` in two (22a44de8 v0.5.2 1 skill; d7c62cb3 v1.0.0 24 commands + hooks), `shipwright` in two (7049274b v0.1.0; 9ff29a1a, 12 skills, 4 agents, hooks). Session listing shows one set each for wizard and scaffold:* (24) and shipwright:* (11).
Totals (enabled, from disk): ~713 skills+commands (wizard counted twice, so ~695 real), 163 agents. 28 plugin dirs register SessionStart.

| plugin | ver | marketplace | skills/cmds | agents | hook events | MCP (bundled) | dir |
|---|---|---|---|---|---|---|---|
| 16-minds | 0.3.0 | anthropic-plugin-directory | 4/4 | 16 | - | - | b9c68df2 |
| adaptive-agent | ? | anthropic-plugin-directory | 2/0 | 0 | - | - | 1821cd61 |
| agent-architecture-designer | 0.41.0 | anthropic-plugin-directory | 0/62 | 60 | - | - | 021ef95f |
| agent-army | 1.0.0 | anthropic-plugin-directory | 1/0 | 0 | - | - | f90aefa8 |
| agent-design | 0.1.0 | anthropic-plugin-directory | 3/0 | 0 | - | - | f4af7fc2 |
| agent-guardrails | 0.1.0 | anthropic-plugin-directory | 3/0 | 0 | - | - | 51111aeb |
| agent-ingest-audit-optimize | 0.6.0 | anthropic-plugin-directory | 1/1 | 0 | - | - | 7f76ffa9 |
| agent-protocols | 1.0.0 | anthropic-plugin-directory | 25/0 | 8 | SessionStart | - | a6190374 |
| agent-smith | 2.5.1 | anthropic-plugin-directory | 0/2 | 0 | - | - | 22e89ec4 |
| analytics-office | 0.28.0 | anthropic-plugin-directory | 19/0 | 0 | - | - | e6d72aa2 |
| anchor-memory | 0.1.0 | anthropic-plugin-directory | 7/0 | 0 | PreCompact, SessionStart, Stop | - | 63003d0a |
| bigquery | 1.0.0 | claude-tag-plugins | 1/0 | 0 | - | - | bigquery |
| brightdata-plugin | 1.9.0 | knowledge-work-plugins | 21/0 | 0 | - | - | brightda |
| browser-use | ? | anthropic-plugin-directory | 0/0 | 0 | - | browser-use | 81b6c174 |
| build-companion | 2.0.0 | anthropic-plugin-directory | 0/0 | 0 | - | - | 041d97ab |
| career-brand | 0.3.0 | anthropic-plugin-directory | 2/2 | 1 | Notification | - | 2f3b1114 |
| career-compass | 2.15.1 | anthropic-plugin-directory | 11/0 | 0 | - | career-compass | d064245b |
| claude-cognis | 1.1.0 | anthropic-plugin-directory | 2/5 | 0 | SessionStart, Stop, UserPromptSubmit | cognis | 728f8e6a |
| claude-md-composer | 1.0.2 | anthropic-plugin-directory | 1/0 | 0 | - | - | 3790e0ca |
| claude-md-management | 1.0.0 | anthropic-plugin-directory | 1/1 | 0 | - | - | 8bc81ed2 |
| claude-memory | 1.0.0 | anthropic-plugin-directory | 1/0 | 0 | SessionStart | - | b61f4be4 |
| claude-patterns | 1.0.0 | anthropic-plugin-directory | 1/0 | 0 | SessionStart | - | 23529d87 |
| coach | 1.0.0 | anthropic-plugin-directory | 8/0 | 8 | SessionStart | - | e0d7c35b |
| cobrain | 1.0.7 | anthropic-plugin-directory | 1/0 | 0 | - | cobrain | 7ecf2bb9 |
| compounded | ? | anthropic-plugin-directory | 5/9 | 1 | SessionEnd, SessionStart, Stop | - | ab9b0379 |
| context-vault | 2.0.0 | anthropic-plugin-directory | 2/0 | 0 | - | - | fff91e49 |
| cowork-plugin-management | 0.2.2 | anthropic-plugin-directory | 2/0 | 0 | - | - | f30ae545 |
| create-smartfolder | 6.6.0 | anthropic-plugin-directory | 1/0 | 0 | - | - | e40abd7f |
| create-state | 1.1.0 | anthropic-plugin-directory | 6/0 | 0 | - | create-state | 09487a27 |
| data | 1.1.0 | knowledge-work-plugins | 10/0 | 0 | - | amplitude, amplitude-eu, atlassian, bigquery, databricks, definite, hex, snowflake | data |
| decision-council | 1.18.0 | anthropic-plugin-directory | 9/0 | 8 | - | - | 74efef3a |
| design | 1.2.0 | knowledge-work-plugins | 7/0 | 0 | - | asana, atlassian, figma, gmail, google calendar, intercom, linear, notion, slack | design |
| desktop-commander | 0.2.0 | anthropic-plugin-directory | 6/0 | 0 | - | - | 8d52a3a6 |
| dev-forge | 3.0.3 | anthropic-plugin-directory | 0/4 | 0 | PreToolUse, SessionStart | - | 04f4af1d |
| docbrain | 1.0.0 | anthropic-plugin-directory | 1/0 | 0 | - | - | 866e30e0 |
| engineering | 1.2.0 | knowledge-work-plugins | 10/0 | 0 | - | asana, atlassian, datadog, github, gmail, google calendar, linear, notion, pagerduty, slack | engineer |
| enterprise-search | 1.3.0 | anthropic-plugin-directory | 5/0 | 0 | - | asana, atlassian, gmail, google calendar, guru, notion, slack | 03520ac0 |
| fellowship | 1.2.0 | anthropic-plugin-directory | 12/18 | 9 | PostToolUse, PreToolUse, SessionEnd, SessionStart | - | e3a3c87a |
| foundation | 0.1.1 | anthropic-plugin-directory | 5/0 | 0 | - | foundation | 6cceb711 |
| gangsta | 1.11.6 | anthropic-plugin-directory | 19/0 | 6 | SessionStart | - | 5772112b |
| graph-query-mcp | 0.1.0 | anthropic-plugin-directory | 0/0 | 0 | - | graph-query | 05e45a78 |
| handoff | 1.0.0 | anthropic-plugin-directory | 1/0 | 0 | SessionStart, Stop | - | d56b622d |
| jevmem | 0.7.6 | anthropic-plugin-directory | 0/0 | 0 | PreToolUse, SessionStart, Stop, UserPromptSubmit | - | 7d57870a |
| learn-wiki | 0.1.1 | anthropic-plugin-directory | 5/0 | 0 | SessionStart | - | 1425d85b |
| legal | 1.3.0 | anthropic-plugin-directory | 9/0 | 0 | - | atlassian, box, docusign, egnyte, gmail, google calendar, slack | 113d9de1 |
| llm-wiki | 3.2.0 | anthropic-plugin-directory | 1/0 | 0 | - | - | a37bed19 |
| local-whisper | 1.0.0 | anthropic-plugin-directory | 1/0 | 0 | - | - | 55855313 |
| loop-and-gate-foundation | 0.5.0 | anthropic-plugin-directory | 10/0 | 0 | SessionStart | - | 87e4a78d |
| maddog | 4.3.3 | anthropic-plugin-directory | 6/0 | 11 | PreToolUse | - | 35397e84 |
| mcpbinder | 1.2.0 | anthropic-plugin-directory | 6/0 | 0 | - | mcpbinder | ce73d409 |
| memanto | 0.2.0 | anthropic-plugin-directory | 2/12 | 1 | PostToolUse, PreCompact, SessionStart | - | 72ec2c86 |
| memories | 1.0.0 | anthropic-plugin-directory | 1/0 | 0 | - | - | 25ebe840 |
| memory-agent | 0.1.0 | anthropic-plugin-directory | 0/0 | 0 | PreCompact, SessionEnd, SessionStart | - | 55175215 |
| memory-bank | 0.1.0 | anthropic-plugin-directory | 1/0 | 0 | Stop | - | 02abfee3 |
| memory-toolkit | 1.9.13 | anthropic-plugin-directory | 11/0 | 0 | PostToolUse, PreCompact, SessionStart, SubagentStop, UserPromptSubmit | - | 07e6b314 |
| mindmap | 0.3.0 | anthropic-plugin-directory | 2/0 | 0 | - | - | fd6bdacf |
| mindpowers | 0.12.0 | anthropic-plugin-directory | 6/0 | 0 | - | - | bc785679 |
| oak-memory | 0.2.0 | anthropic-plugin-directory | 0/9 | 0 | UserPromptSubmit | oak-memory | 1cdb8f62 |
| obsidian-notes | 0.2.1 | anthropic-plugin-directory | 1/0 | 0 | - | - | 3cacb896 |
| obsidian-sync | 0.1.0 | anthropic-plugin-directory | 1/1 | 0 | - | - | 842c82fd |
| obsidian-wiki | ? | AEsops-obsidian-wiki | 0/0 | 0 | - | - | obsidian |
| pge-orchestrator | 2.7.0 | anthropic-plugin-directory | 16/0 | 10 | - | pge-orchestrator | 03cdc083 |
| pm-toolkit | 1.9.1 | anthropic-plugin-directory | 54/0 | 5 | PostToolUse, PostToolUseFailure, SessionStart, Stop | - | 3ddb2ebd |
| pmm | 2.7.0 | anthropic-plugin-directory | 12/0 | 0 | SessionStart, Stop | - | b907fbde |
| product-discovery-flow | 1.0.0 | anthropic-plugin-directory | 0/0 | 0 | - | - | 6c96fd41 |
| productivity | 1.3.1 | knowledge-work-plugins | 4/0 | 0 | - | asana, atlassian, clickup, gmail, google calendar, linear, monday, notion, slack | producti |
| project-memory | 1.4.0 | anthropic-plugin-directory | 1/2 | 0 | - | - | d4cc7285 |
| prompt-enhancer | 1.0.5 | anthropic-plugin-directory | 1/0 | 0 | - | - | f33b62fb |
| reef | 1.1.4 | anthropic-plugin-directory | 13/0 | 1 | - | - | a9929529 |
| research-desk | 0.4.1 | anthropic-plugin-directory | 7/0 | 0 | - | reference-lookup, reference-lookup-hosted | 66e5ae56 |
| research-superpowers | 0.41.1 | anthropic-plugin-directory | 17/0 | 7 | SessionStart | - | c072b1d6 |
| sarathi | 0.8.0 | anthropic-plugin-directory | 3/0 | 0 | - | - | db3b1ede |
| scaffold | 0.5.2 | anthropic-plugin-directory | 1/0 | 0 | - | - | 22a44de8 |
| scaffold | 1.0.0 | anthropic-plugin-directory | 0/24 | 0 | PostToolUse, PreToolUse, Stop | - | d7c62cb3 |
| sdlc-kit | 0.8.0 | anthropic-plugin-directory | 11/0 | 0 | PostToolUse | - | 66fc4566 |
| second-arrow | 1.1.0 | anthropic-plugin-directory | 1/1 | 0 | - | - | 16eb41af |
| sensei | 1.0.0 | anthropic-plugin-directory | 14/0 | 0 | - | - | 777ea906 |
| shipwright | 0.1.0 | anthropic-plugin-directory | 1/0 | 0 | - | - | 7049274b |
| shipwright | ? | anthropic-plugin-directory | 12/0 | 4 | PostToolUse, PreToolUse, SessionStart, Stop, UserPromptSubmit | - | 9ff29a1a |
| shorty | 1.1.0 | anthropic-plugin-directory | 4/0 | 0 | - | - | 01e52999 |
| signal-hunter | 2.1.0 | anthropic-plugin-directory | 7/0 | 0 | - | - | 584e5ee8 |
| snowflake | 1.0.0 | claude-tag-plugins | 1/0 | 0 | - | - | snowflak |
| task-observer | 3.7.0 | aesop-task-observer | 0/0 | 0 | - | - | task-obs |
| tenet | 3.3.0 | anthropic-plugin-directory | 3/0 | 0 | SessionStart, Stop | - | 0a103932 |
| the-life-edit | 6.0.0 | anthropic-plugin-directory | 0/0 | 0 | - | - | 45a48293 |
| thinking-partner | 1.0.0 | anthropic-plugin-directory | 1/0 | 0 | - | - | f4bd1fc9 |
| tinyfish | 1.4.0 | anthropic-plugin-directory | 6/0 | 0 | - | tinyfish | 4709b2dd |
| token-saver | 0.2.0 | anthropic-plugin-directory | 1/5 | 0 | - | - | a2e29b48 |
| user-intuition-research | 1.3.3 | anthropic-plugin-directory | 10/0 | 0 | - | user-intuition | 540b0c14 |
| ux-superpowers | 1.0.0 | anthropic-plugin-directory | 8/0 | 0 | SessionStart | - | 91734699 |
| vault-anything | 0.1.0 | anthropic-plugin-directory | 2/0 | 2 | - | - | b5e0eda0 |
| wherewasi | 0.1.0 | anthropic-plugin-directory | 0/1 | 0 | PreCompact, SessionEnd, SessionStart, UserPromptSubmit | - | 5f167125 |
| whydone | 1.4.1 | anthropic-plugin-directory | 0/0 | 0 | Stop | - | a4c444d8 |
| wiki-wonka | 1.0.2 | anthropic-plugin-directory | 3/0 | 1 | FileChanged, PostToolUse, PreToolUse, SessionStart, Stop | - | cc779a20 |
| wizard | 1.0.0 | anthropic-plugin-directory | 12/6 | 1 | SessionStart | - | 63cc09e4 |
| wizard | 1.0.0 | anthropic-plugin-directory | 12/6 | 1 | SessionStart | - | d0666aa1 |
| workflow-toolkit | 1.0.0 | anthropic-plugin-directory | 21/0 | 2 | PostToolUse, PreCompact, SessionEnd, SessionStart, Stop, SubagentStop, TaskCompleted | - | 32778f50 |

### A2. Synced but NOT visible in the skill listing (enabled state unverifiable; mostly UI "mods" or hook-only)
| plugin | ver | marketplace | skills/cmds | agents | hook events / mods | dir |
|---|---|---|---|---|---|---|
| agent-recall | 0.4.0 | anthropic-plugin-directory | 0/0 | 0 | PostToolUse, SessionStart | 80cdebec |
| compact-on-idle | 0.1.0 | anthropic-plugin-directory | 0/0 | 0 | modules | 7f1fc471 |
| context-window | 0.5.4 | anthropic-plugin-directory | 0/0 | 0 | modules | 10c1f421 |
| crayon | 0.2.0 | anthropic-plugin-directory | 0/0 | 0 | modules | f96baf0a |
| glance | 0.1.0 | anthropic-plugin-directory | 0/0 | 0 | modules | 79e55640 |
| jev | 0.3.3 | anthropic-plugin-directory | 0/0 | 0 | modules | d8e07c35 |
| prompt-coach | 1.2.0 | anthropic-plugin-directory | 1/0 | 1 | - | 3269b367 |
| promptcolor | 0.1.0 | anthropic-plugin-directory | 0/0 | 0 | modules | 4d59dd41 |
| rutter | 0.3.3 | anthropic-plugin-directory | 0/0 | 0 | Stop | 28f8ea18 |
| snoozing-pet | 0.3.0 | anthropic-plugin-directory | 0/0 | 0 | modules | 514b46b1 |
| token-inspector | 1.2.0 | anthropic-plugin-directory | 8/0 | 0 | - | c033e7f5 |
| usage-line | 0.3.1 | anthropic-plugin-directory | 0/0 | 0 | - | af688880 |

### A3. Account-level / user-level skills (claude.ai, from ListSkills; 20, all enabled)
termux-helper (Android Termux commands, storage, scripts), docs (docs-connector documents), google-workspace (Google Docs/Sheets/Slides edits), computer-use, chrome-browser, built-in-browser, deep-research (multi-source report, needs Agent tool), import-memory, morning (morning brief artifact), learn (explain/teach), web-artifacts-builder, skill-creator, theme-factory, mcp-builder, canvas-design, xlsx, pptx, pdf, docx.
Also in the session skill list but not account skills: session-start-hook (~/.claude/skills/session-start-hook), user-level pge-* commands and agents (~/.claude/commands 16 pge files, ~/.claude/agents 10 files, ~/.claude/hooks/pge-autolaunch.sh; ALSO shipped by plugin pge-orchestrator 2.7.0 = duplicate), built-ins (update-config, keybindings-help, code-review, simplify, fewer-permission-prompts, loop, claude-api, run, plugin-authoring, init, security-review, dataviz, artifact-*), project skills from cwd (debug-issue, explore-codebase, refactor-safely, review-changes = code-review-graph wrappers; drive-to-obsidian-migration; notebooklm; task-observer 47,192 B in novaexorpus/.claude/skills).

### A4. Operator's own project skills / agents (on disk)
| item | location | trigger (from description) |
|---|---|---|
| aesop-voice-pipeline | aesop-xi/skills (5,616 B) | live on-device voice (mic>VAD>STT>TTS), Gemma-on-NPU benchmark, whisper.cpp/Parakeet |
| corpus-batch-processing | aesop-xi/skills (8,390 B) | raw/ -> clean_md/ at 20+ files; "process raw", "run phase 1 on <repo>" |
| corpus-verify | aesop-xi/skills (11,323 B) | independent RLVR check after any corpus clean pass |
| termux-helper | aesop-xi/skills (12,254 B) | Termux on-device AI stack, llamad port 8081, aesopd 8765, NPU/HTP. DUPLICATE NAME of account skill termux-helper and of anthropic-skills:termux-helper |
| debug-issue, explore-codebase, refactor-safely, review-changes | novaexorpus/.claude/skills (1.0-1.2 KB each) | code-review-graph MCP wrappers; review-changes overlaps built-in code-review/agent-protocols:review/scaffold:review |
| drive-to-obsidian-migration | novaexorpus/.claude/skills (9,367 B) | Drive -> vault via rclone, dedupe, md, JSONL RAG chunks |
| notebooklm | novaexorpus/.claude/skills (16,376 B) | notebooklm-py CLI/API |
| task-observer | novaexorpus/.claude/skills (47,192 B) AND plugin task-observer 3.7.0 (aesop-task-observer marketplace) AND plugin task-observer:task-observer in listing | invoke before FIRST tool call of any session (see C) |
| agents builder (sonnet), corpus-architect (opus) | novaexorpus/.claude/agents | impl; corpus reconcile. Both name mem0 MCP tools |
Not present in this container although router-guard.sh, skills-inventory-report and TOOLS inventory expect them: ~/.claude/skills/{honey*, graphify, notebooklm, openwiki, android-termux-operator, corpus-*}, mem0 plugin, honey@greenpt, obsidian@obsidian-skills. ECC was intentionally uninstalled 2026-09-09 (TOOLS inventory) but aesop-xi/.claude/settings.json still has two ECC-dependent PostToolUse entries (session-activity-tracker.js path under plugins/cache/ecc/ecc/2.2.0, plus a prompt hook that names ECC skills): dead weight here.

### A5. MCP servers / connectors (session status block)
| server | status |
|---|---|
| Claude_Docs, Gmail, Google_Calendar, Google_Docs, Google_Drive, Google_Sheets, Google_Slides, Hugging_Face (user Mer0vin8ian), TinyFish (claude.ai connector) | connected |
| plugin:browser-use, plugin:career-compass, plugin:claude-cognis (cognis), plugin:pge-orchestrator, plugin:research-desk (reference-lookup, reference-lookup-hosted) | connected (tools present) |
| plugin:cobrain, create-state, data:amplitude, data:amplitude-eu, data:hex, design:figma, design:intercom, engineering:datadog, engineering:linear, enterprise-search:guru, enterprise-search:notion, foundation, legal:atlassian, legal:docusign, legal:egnyte, legal:slack, mcpbinder, productivity:clickup, productivity:monday, shorty, tinyfish (plugin copy), user-intuition-research | NEEDS AUTH (22) |
| data:bigquery (no DCR), data:definite (endpoint 404), desktop-commander (timeout), engineering:github (403, session bound to repos), engineering:pagerduty (no DCR), enterprise-search:asana (no DCR), graph-query-mcp (ENOENT stdio), jevmem (ENOENT stdio), legal:box (no DCR), oak-memory (CONNECTION_CLOSED) | FAILED (10) |
| novaexorpus/.mcp.json: omniroute, mem0, terrestrial-brain, code-review-graph (proot-distro stdio); settings.local.json enables all four | not connected in this session (no mcp__ tools present); a .mcp.json declares `omniroute` twice (duplicate key) |
Note: TinyFish appears twice (claude.ai connector connected + plugin:tinyfish needs auth). Gmail/Calendar/Drive/Docs/Slides also bundled as MCP entries inside enterprise-search, legal, design, engineering, productivity, product-management-type plugins: the same services declared 5+ times, most unauthenticated.

## B. HOOK-EVENT COLLISION MAP
Registered by enabled plugins (from hooks.json/plugin.json on disk) plus aesop-xi project settings (loaded when cwd = aesop-xi) and novaexorpus project settings. Whether plugin hooks actually fire in this cloud container is unverified (docs say cloud sessions skip locally installed plugins; synced ones do load).

| event | plugins (count) | aesop-xi / novaexorpus |
|---|---|---|
| SessionStart (28 plugin dirs) | agent-protocols, anchor-memory, claude-cognis, claude-memory, claude-patterns, coach, compounded (memory_inject.py), dev-forge, fellowship (4 scripts, 29 KB; startup + --resume), gangsta, handoff, jevmem, learn-wiki, loop-and-gate-foundation (2 scripts), memanto, memory-agent, memory-toolkit, pm-toolkit (context-reinject), pmm, research-superpowers (session-start + drift-check), shipwright, tenet, ux-superpowers (prompt hook), wherewasi, wiki-wonka (needs $CLAUDE_PROJECT_DIR/hooks), wizard x2, workflow-toolkit; agent-recall (unlisted) | aesop-xi: session-start.sh (async bootstrap-stack), context-diff.sh, housekeeping-check.sh, staged-updates.sh (+ observe-event.sh on `compact`); novaexorpus: router-guard.sh |
| UserPromptSubmit (6) | claude-cognis, jevmem, memory-toolkit (pipeline-hint), oak-memory (failed MCP), shipwright, wherewasi | enforce-prompt.sh (+classify.sh), delegation-tripwire.sh, observe-event.sh |
| PreToolUse (7) | dev-forge (pre-commit), fellowship (plan-gate), jevmem (guard), maddog (3 guards), scaffold (2 inline python), shipwright (approval_gate), wiki-wonka (protect-raw) | resume-gate, checkin-gate, secret-guard, enforce-gate, sync-on-use (BLOCKING gh sync), git-gate, branch-current-gate, state-guard, settings-guard, build-doc-gate, delegation-tripwire, agent-type-gate = 12 gates on `*`/Bash/Edit |
| PostToolUse (9) | fellowship (context-monitor), memanto (notify), memory-toolkit (commit note + session-watcher), pm-toolkit (usage-logger, workflow-tracker), scaffold (2 inline), sdlc-kit (Write/Edit/NotebookEdit), shipwright (quality_gate), wiki-wonka (git-autocommit), workflow-toolkit (tool-use); agent-recall | ECC session-activity-tracker (dead), ECC prompt hook on Bash (dead; fires an LLM call per Bash), session-ledger, build-doc-gate, delegation-tripwire |
| Stop (14) | anchor-memory (integrity gate + checkpoint), claude-cognis (summary), compounded (skill_verify, auto_propose), handoff (nudge), jevmem, memory-bank, pm-toolkit (quality-gate), pmm (should-save), scaffold (echo reminder), shipwright (stop_checklist), tenet, whydone, wiki-wonka (suggest-lint), workflow-toolkit (journal); rutter (unlisted) | stop-gate.sh (blocks turn end), absence-gate.sh; subagent-stop-gate (see below) |
| SubagentStop (2) | memory-toolkit, workflow-toolkit | subagent-stop-gate.sh (in hooks/, listed in README; NOT in .claude/settings.json) |
| SessionEnd (5) | compounded (trust_ladder), fellowship, memory-agent, wherewasi, workflow-toolkit | archive-scratchpad.sh, ship-session.sh (PR + auto-merge) |
| PreCompact (6) | anchor-memory, memanto, memory-agent, memory-toolkit, wherewasi, workflow-toolkit | archive-scratchpad.sh |
| Notification (1) | career-brand (desktop notify, osascript/notify-send) | none |
Other events: TaskCompleted (workflow-toolkit), PostToolUseFailure (pm-toolkit; aesop-xi observe-event), FileChanged (wiki-wonka).
Unregistered hook files lying in ~/.claude: stop-hook-git-check.sh, stop-hook-reply-gate.py, user-prompt-submit-reply-reminder.py, hooks/pge-autolaunch.sh (settings.json registers none of them).
Missing registration: aesop-xi hooks/README lists carryover.sh, observe-event.sh, subagent-stop-gate.sh, vault-ship.sh, auditor/, but .claude/settings.json has no SubagentStop, PostToolUseFailure, PermissionDenied or SessionStart `compact` entry; those depend on the global ~/.claude/hooks copy (absent in this container: ~/.claude/hooks contains only pge-autolaunch.sh). run-hook.sh stands down when a global copy exists.

Likely conflicts
1. Stop: aesop-xi stop-gate (blocks end-of-turn until RESUME/observer/ENFORCEMENTS satisfied) + 14 plugin Stop hooks that add their own end-of-turn prompts/blocks (anchor-memory memory-integrity-gate, shipwright stop_checklist, pm-toolkit quality-gate, scaffold session-end text). Any plugin that returns `block` can fight stop-gate's "block once then allow" logic and produces loops.
2. SessionStart stacking: up to 28 injectors + 5 aesop-xi/novaexorpus scripts. Memory injectors that all inject prior-session context: claude-cognis, compounded, memanto, memory-toolkit, pmm, claude-memory, anchor-memory, handoff, wherewasi, memory-agent, jevmem, agent-recall, learn-wiki.
3. UserPromptSubmit: claude-cognis + jevmem + memory-toolkit + shipwright + wherewasi each recall/log per prompt, on top of enforce-prompt.sh + delegation-tripwire.
4. PreCompact/SessionEnd write-owners: 6 plugins + archive-scratchpad + ship-session; each writes its own session file. ship-session opens PRs and auto-merges; wherewasi/memory-toolkit/compounded write state at the same moment (race on git index if they write inside the repo).
5. PreToolUse: shipwright approval_gate, fellowship plan-gate, maddog executor/judge guards, dev-forge pre-commit vs aesop-xi checkin-gate/resume-gate: three independent "no edits until approved" mechanisms.
6. Duplicate-registered: pge-orchestrator (plugin + user-level commands/agents), wizard x2, scaffold x2, shipwright x2.

## C. OVERLAP GROUPS
1. Memory systems (13+ in play). Members: claude-cognis (MCP cognis, 8 tools: add/search/get/delete memories; needs account), compounded (trust-laddered memory + skill verification), memanto (memanto.ai; SessionStart+PostToolUse+PreCompact), memory-toolkit 1.9.13 (markdown workstreams, handoff, auto-save), memory-agent (compiled KB, provenance/conflicts), pmm 2.7.0, claude-memory, project-memory, memories, memory-bank, anchor-memory (decisions, integrity gate), jevmem (MCP failed), agent-recall (hooks+mcp), cobrain (needs auth), oak-memory (MCP failed), wherewasi, whydone, create-state, docbrain, context-vault, adaptive-agent. Account-side: import-memory skill. Operator-side: mem0 + terrestrial-brain + omniroute MCP (novaexorpus), RESUME/PENDING/MEMORY.md discipline, vault `_recaps`. Unique adds: compounded = skill-trust ladder (maps to task-observer); anchor-memory = integrity gate (partly maps to stop-gate evidence rules); whydone = decision rationale log. Redundant with aesop-xi: nearly all auto-capture/auto-inject ones, because RESUME/PENDING/MEMORY + context-diff.sh + session-ledger + vault-ship already own capture, injection and shipping. The skills-inventory-report (2026-10-23) already flagged this: "do not enable all memory hook packs together."
2. Wiki / knowledge base. Members: llm-wiki 3.2.0, learn-wiki, wiki-wonka, obsidian-wiki (40 skills, AEsops-obsidian-wiki fork, 25 behind), vault-anything, obsidian-notes, obsidian-sync, desktop-commander:{knowledge-base,obsidian-vault}, research-superpowers (wiki-graph, wiki-lint), reef, mindmap, docbrain, signal-hunter; aesop-xi corpus-batch-processing/corpus-verify, drive-to-obsidian-migration, D.U.M.B.A.S.S. vault. Same Karpathy pattern implemented 5 times (wiki-ingest/query/lint names repeat: llm-wiki:wiki:lint, obsidian-wiki:wiki-lint, wiki-wonka:lint, research-superpowers:wiki-lint). Unique: obsidian-wiki has history-ingest for claude/codex/copilot sessions and tag-taxonomy; obsidian-notes has link/orphan lint; operator's corpus-verify (independent RLVR check) has no equivalent in any plugin.
3. Session continuity / handoff. Members: handoff, wherewasi, memory-toolkit (session-start/continue/restore/end/park), anchor-memory (handoff, session-wrapup), loop-and-gate-foundation:session-start, scaffold (context-save, session-end, sync-context, progress), create-state:end-session, shipwright (checkpoint, resume), context-vault, token-saver (snapshot/archive), fellowship (session-start hooks). Operator's own: RESUME.md START HERE + resume-gate + checkin-gate + carryover.sh + /wrapup + ship-session + vault-ship + archive-scratchpad. Fully redundant; plugin session-start/end skills also compete with the checkin-gate protocol (`#ok`/`#defer`).
4. Task observation / skill improvement. Members: task-observer (3 copies: novaexorpus skill 47 KB, plugin task-observer 3.7.0, listing entry task-observer:task-observer), adaptive-agent (skill-review, build-user-profile), compounded (verify/trust), loop-and-gate-foundation (improve, reflect, capture), memory-toolkit (reflect, docs-reflect), agent-ingest-audit-optimize, claude-md-management (revise-claude-md, improver), claude-md-composer, skill-creator (account + plugin copies in obsidian-wiki), anthropic-skills:skill-creator, wizard (refine/pressure-test spells), agent-smith. Operator system: task-observer + observe-event.sh friction queue + stop-gate observer check + skill-updates/PENDING + staged-updates.sh. Three task-observer copies can diverge (fork has PR #1 fix 09a4101; upstream rebelytics draft unsent). principles-match: 2 MATCH / 6 PARTIAL / 21 no match of 29 starter principles.
5. Orchestration / multi-agent frameworks (the heaviest group). Members: agent-architecture-designer (62 skills + 60 agents, 62 commands, v0.41.0), pge-orchestrator 2.7.0 (16 skills, 10 agents, MCP; plus user-level duplicate), fellowship (30 skills, 9 agents, 18 cmds), gangsta (19 skills, 6 agents), maddog (11 agents), 16-minds (16 agents), decision-council (8 agents), workflow-toolkit, agent-army, agent-protocols (25 skills, 8 agents), shipwright, sdlc-kit, scaffold (dispatch/execute/route-model/sparc/tdd/worktree), dev-forge, coach, mcpbinder, build-companion, tenet. Operator-side: corpus-batch-processing (orchestrator+subagents), subagent-stop-gate, delegation-tripwire, agent-type-gate, progress-file convention, builder/corpus-architect agents. Pge shipped twice; fellowship/gangsta/agent-protocols each re-implement worktrees, TDD, review, planning, brainstorming.
6. Research. Members: research-superpowers (17 skills, 7 agents, SessionStart), research-desk (7 skills + 2 MCP: OpenAlex/arXiv reference-lookup, connected), account deep-research, tinyfish (search/fetch/agent/monitor, connector connected, plugin needs auth), brightdata-plugin (21 skills), shorty, user-intuition-research, enterprise-search, Hugging_Face connector, mindpowers (fact-checking, validating-problems), obsidian-wiki:wiki-research, thinking-partner. Unique and valuable for D.U.M.B.A.S.S. citations: research-desk reference-lookup (verifies against OpenAlex/arXiv); research-superpowers ingest-source/acquire-sources are close to corpus-batch-processing.
7. Product management. Members: pm-toolkit (54 skills, 5 agents, 4 hooks; 25 KB of descriptions, the largest single listing cost), product-discovery-flow, sdlc-kit (sdlc-prd/spec/adr), shipwright (design/breakdown), mcpbinder (plan-tasks), ux-superpowers, analytics-office (19 skills), design, productivity, legal, create-smartfolder, agent-protocols (spec, plan), productivity:task-management. Operator uses PENDING.md/BOARD-INTAKE.md; no PM-product use is evident in the stack (corpus + Android APKs).
8. Android / Termux / on-device. Members: account termux-helper, anthropic-skills:termux-helper, aesop-xi termux-helper, aesop-voice-pipeline, local-whisper, second-arrow (voice), 16-minds voice-*. Nothing in the plugin set covers Android build, Kotlin or NPU. Three copies of termux-helper (account skill, anthropic-skills:, repo) overlap; the repo copy is the only one with llamad/aesopd/NPU Part 2.
9. Code graph / review. Members: project debug-issue/explore-codebase/refactor-safely/review-changes (code-review-graph MCP, absent here), built-in code-review + simplify + security-review, agent-protocols:review/code-review-and-quality, scaffold:review, fellowship, pm-toolkit:pm-review, engineering:code-review, graph-query-mcp (failed), obsidian-wiki:code-understand.
10. Guardrails / enforcement. Members: agent-guardrails (3 analysis skills, no hooks), maddog, tenet (tenet-audit/sweep), scaffold hooks, dev-forge gate, shipwright approval/quality gates, fellowship plan-gate, anchor-memory integrity gate, loop-and-gate-foundation. Operator hooks (ENFORCEMENTS.md, secret-guard, gitleaks dispatch, settings-guard, state-guard) are far stricter and are the only ones that cover secrets and settings immutability.

## D. MARKETPLACE GAPS (not installed)
Anthropic marketplace (claude-plugins-official, 315 plugins; categories: development 123, productivity 69, database 39, monitoring 22, security 18, deployment 9, design 8, other 27). Docs pages (discover-plugins, plugins) name only commit-commands as an example and recommend `claude plugin details <name>` and the "Not used recently" tab for cost checks; they recommend no specific official skill absent locally.
| plugin | fit vs operator stack |
|---|---|
| security-guidance (Anthropic; also in org catalog) | Pattern warnings on edit + Stop diff review. Overlaps secret-guard/gitleaks; adds exploit-class review. Would add a 4th Stop hook: low value, use on demand only |
| code-review, pr-review-toolkit, code-simplifier, feature-dev, commit-commands | PR/diff review agents; built-ins code-review + simplify already ship. commit-commands overlaps ship-session. Skip |
| hookify | Generate hooks from conversation patterns; aligns with observe-corrections.txt + hooks-spec backlog, but settings-guard blocks agent edits to settings. Candidate as authoring aid only |
| plugin-dev, skill-creator (official), mcp-server-dev, agent-sdk-dev | Useful if building the 3-APK MCP bridge/aesopd; skill-creator duplicates 2 existing copies |
| claude-md-management | Already installed (as claude-md-management) |
| kotlin-lsp | Real gap: Kotlin diagnostics/nav for the 3-APK Android stack; no Kotlin tooling is installed. Best-fit LSP |
| claude-code-setup, session-report | Setup recommendation and token/cache report; session-report gives measurement missing from E. Candidate |
| explanatory/learning output styles | Not relevant (router-guard.md output style exists) |
| ralph-loop | Overlaps loop skill; conflicts with stop-gate. Skip |
| firebase, google-cloud-storage, alloydb, cloud-sql-*, spanner, bigquery-data-analytics, looker, knowledge-catalog | GCP data/ops; fit the GCP enterprise config only if the vault/RAG moves to GCP (VM 34.31.112.77 in router-guard). google-cloud-storage and bigquery-data-analytics are the plausible ones. data:bigquery already fails auth |
| huggingface-skills | Fit for NPU on-device models (Hugging_Face connector already connected); skills add train/eval guidance. Candidate |
| context7, lumen (local semantic code search, Ollama), duckdb-skills | context7 for current docs; lumen/duckdb relevant to local RAG over chunk.jsonl (7.4 MB). Candidates, not urgent |
| claude-security (deep vuln scan), aikido, sonarqube, 42crunch, vanta, coderabbit, greptile | Security/review SaaS; low fit for a markdown corpus and Android APKs |
| remember (continuous memory) | Another memory pack. Do not add |
| dash0, langfuse-observability | OTel session telemetry; fills the context-cost measurement gap, adds exporter hooks. Optional |
Org catalog (SearchPlugins, "Anthropic Directory", community-reviewed; none enabled per tool):
- memory/wiki: llm-wiki-plugin (installed as llm-wiki), memory-agent, memory-toolkit, wiki-wonka, learn-wiki, oak-memory (all synced here), n8n Knowledge Base (no fit), notion-memory (Notion bundle, no), Cowork Memory (Cowork only), Kumiho Memory Cloud (paid, remote, no).
- hooks/session: Agent Guardrails (installed), Semaphore Hooks (USB HID, no), Session Vitals (statusline: cache TTL + context bar; overlaps ~/.claude statusline.py), Session Recall (search past transcripts with claude --resume; useful but memory-overlap), Session Relaunch (/relaunch; low fit), bash-guardrails (parser-based bash guard; overlaps secret-guard/git-gate/state-guard; maybe borrow find-/ rules), Session Analyzer, Context Compactor (compact-plan; partly overlaps archive-scratchpad), Senior Engineer Guardrails, session-sweep (stale worktree cleanup: fits ship-session worktree sprawl `~/repos/.wt-*`).
- android/mobile: Mobile Release Check (Play readiness: target SDK, signing, cleartext, keys): GOOD FIT for 3-APK stack; Android Emulator QA (needs emulator, not on Termux/Moto Razr); Oh My Android (needs macOS app); KotlinSense (Kotlin LSP, duplicate of kotlin-lsp); Ansight (27 mobile CLI skills + SessionStart, remote); Responsive Check, Copycat, iOS design: no.
- code review/graph: Ringmaster (orchestrator + security gate; heavy hooks), cartographer (dependency/call graph + 17 reviewers; closest to code-review-graph), code-graph (AST->HTML), graph-query-mcp (installed, failing), ccgrapher (parallel plan check), Code Review community skill. cartographer/code-graph are the options if code-review-graph (proot-distro stdio) stays unreachable.
- research/ingest: research-superpowers, research-desk (installed), Research integrity (instructions-only claim/evidence labelling; fits corpus-verify discipline), B2B Research, Exa Deep Research (remote MCP), Agent Ingest Audit Optimize (installed), saas-corpus (no), Bio Research (no).
- orchestration/workflow: simple-workflow (v10.1, 13 skills, 13 agents, 6 hooks; heavy), claude-workflow (YAML workflows), ag2-workflow-patterns, MCP Workflow Audit (audits MCP/agent workflows, approval boundaries: good fit for reviewing the hook stack), Flow, PWP, neonloops: skip except MCP Workflow Audit.
- voice: claude-code-tts (Stop-hook TTS on Linux; would collide with aesop-voice-pipeline), tts-attention-alert (Windows only), Voice Messages (text cleanup), voice-of-customer, CloudTalk/Voicenter (telephony): none fit; on-device pipeline is the operator's own.
- obsidian/markdown: Obsidian Notes (installed), obsidian-sync (installed), Vault Anything (installed), Markdown by mdedit.ai, Google Drive -> Markdown (overlaps drive-to-obsidian-migration; Drive connector based, no rclone), Document Vault (family docs), Notion Markdown Sync, context-vault (installed), shazam (grill-me, git-guardrails-claude-code, obsidian-vault).
- security: Security Audit Loop by ATeam, OWASP Security Audit, finecomb (language-agnostic checklist incl. GPU programs), securitymaxxing, Setup Audit (audits Claude Code config against docs, cost/security: strong fit for this very audit, read-only by default but offers fixes), IaC Reviewer (Terraform), Verified Security Sweep (verify each finding on cited lines; fits RLVR rule 5), Security Guidance.
- pm/product: lean-pm-skills, pm (Helixis), Pragmatic PM (installed as pm-toolkit), Product Management (Anthropic), PRP Manager, ai-pm-skills, SpecsGraph, Agile Product (Confluence), Product Marketing: none needed.
- gcloud/deploy: GCP DevKit (Cloud Run, GKE, Firestore rules, IAM audit, Terraform GCP; SessionStart+PostToolUse hooks, 3 agents): closest GCP enterprise fit. IAM audit and gcloud-debug are the useful parts. deploy-on-aws, aws-core, Cloudflare, Expo, localstack, Blaxel, Replo, elmah.io, deploycheck: no.
- claude api/agent sdk: agent-sdk-dev (Anthropic), mana (agent skills as spells), claude-eta, claude-tab-fix (tab/Read separator edit failures), claude-backup, Claudebase (config backup to GitHub; SessionStart+End), claude-damn (63 skill variants + PreToolUse guard), Agentic SDLC. claude-api skill is already built in.

## E. CONTEXT COST (estimates; hooks not executed)
- Skill/command listing: 713 plugin skills+commands in the listing (about 695 distinct; wizard counted twice) plus ~20 account skills and ~25 built-ins/project skills. Measured: summed name+description characters in the synced SKILL.md/commands frontmatter for all 109 dirs = 218,673 chars (about 55k tokens if every description were listed). The session listing actually shows description text for only ~25 entries and bare names for the rest, so the real every-turn listing is smaller: about 700 names x ~30 chars = ~21 KB (~5-6k tokens) + ~25 descriptions (task-observer's alone is ~1.1 KB). Treat 6-9k tokens as the likely listing cost; verify with `claude plugin details <name>` (Always-on line) which the docs provide.
- Agents: 163 agent definitions on disk (agent-architecture-designer 60, maddog 11, 16-minds 16, pge 10 + 10 user-level, fellowship 9, decision-council 8, agent-protocols 8, copies in coach 8...); only names/descriptions are listed to the Agent tool.
- SessionStart: 28 plugin dirs + 4 aesop-xi scripts (+1 novaexorpus). Static script sizes (proxy only): fellowship 29.3 KB across 4 scripts, claude-cognis 22.2 KB, wherewasi 17.9 KB, memanto 15.9 KB, jevmem 15.2 KB, tenet 13.5 KB, learn-wiki 13.2 KB, shipwright 11.8 KB, loop-and-gate-foundation 7.2 KB, pmm 7.1 KB, coach 6.6 KB, compounded 5.8 KB. Script size is not output size; actual injected text unknown. ux-superpowers injects an inline prompt hook text each start.
- Always-loaded files: aesop-xi AGENTS.md 10,814 B, ARCHITECTURE.md 12,823 B, MEMORY.md 4,646 B, RESUME.md 3,063 B, PENDING.md 3,455 B, CLAUDE.md.original.md 6,696 B; novaexorpus AGENTS.md 6,434 B, MEMORY 2,263 B, RESUME 4,376 B, PENDING 8,950 B. task-observer SKILL.md is 47,192 B (~12k tokens) and its description demands loading before the first tool call of every session, so it is the single most expensive loaded item per session.
- MCP: 22 servers need auth and 10 fail: they cost connection time but no tools. Connected claude.ai connectors expose ~150 deferred tool names (Gmail 28, Calendar 9, Drive 11, Sheets 9, Docs 2, Slides 4, TinyFish 27, HF 5, career-compass 20, pge 15, cognis 8, research-desk 10, browser-use 2).
- Per-prompt: UserPromptSubmit has 6 plugin hooks + 3 aesop-xi; PostToolUse on `.*` runs an ECC LLM prompt hook on every Bash call plus an async tracker that cannot work here (ECC removed).
Top 10 contributors (estimated, descending): 1 task-observer SKILL.md 47 KB (loaded each session); 2 pm-toolkit (54 items, 25 KB of descriptions, 4 hook events); 3 agent-architecture-designer (62 skills + 60 agents + 62 commands); 4 analytics-office (19 skills, 17 KB descriptions); 5 sdlc-kit (11 skills, 15.9 KB); 6 brightdata-plugin (21 skills, 14.7 KB); 7 fellowship (30 skills, 9 agents, 29 KB of SessionStart scripts, 5 hook events); 8 ux-superpowers (11.4 KB descriptions + SessionStart prompt); 9 claude-cognis (22 KB SessionStart + UserPromptSubmit + Stop on every prompt); 10 research-superpowers + agent-protocols + wherewasi (each 6-18 KB of hooks/descriptions). The aesop-xi gate stack (about 14 hook scripts per turn) is cheap in tokens but heavy in latency.

## F. RECOMMENDATION TABLE (advisory; operator decides)
| plugin / cluster | call | reason |
|---|---|---|
| aesop-xi hooks (gates, ledger, ship-session, vault-ship) | keep | primary enforcement; nothing in the marketplace covers secret-guard, settings-guard, checkin/resume protocol |
| task-observer (3 copies) | consolidate | keep one canonical copy (fork aesop-task-observer 3.7.0 plugin) and drop the 47 KB project copy and listing duplicate |
| aesop-xi skills (voice, corpus-batch, corpus-verify) | keep | unique, project-specific |
| termux-helper (3 copies) | consolidate | account skill, anthropic-skills, repo copy; keep the repo one (only one with NPU Part 2) |
| code-review-graph wrappers (4 skills) | investigate | MCP is not reachable here; skills are dead weight until it is |
| ECC-dependent PostToolUse entries in aesop-xi settings | drop candidate | ECC uninstalled 2026-09-09; one fires an LLM call per Bash for nothing |
| Memory auto-capture plugins: claude-cognis, compounded, memanto, memory-toolkit, memory-agent, pmm, claude-memory, anchor-memory, jevmem, agent-recall, oak-memory, wherewasi, whydone, handoff | drop candidate (keep at most one, or skills-only) | RESUME/PENDING/MEMORY + session-ledger + vault-ship already own this; 14 SessionStart/Stop hooks; jevmem and oak-memory already failing |
| compounded | investigate | trust ladder for skills is the only memory-adjacent feature mirroring task-observer |
| project-memory, memories, memory-bank, create-state, docbrain, cobrain, context-vault, token-saver | drop candidate | thin overlaps; cobrain/create-state need auth |
| Wiki set: llm-wiki, learn-wiki, wiki-wonka, vault-anything, obsidian-notes, obsidian-sync, desktop-commander knowledge-base | consolidate | pick obsidian-wiki (already forked/vault-aligned) or none; obsidian-notes lint is the only distinct tool |
| obsidian-wiki (40 skills) | keep (investigate size) | operator's fork; 25 commits behind; large listing |
| research-desk | keep | OpenAlex/arXiv verification connected and unique |
| research-superpowers | investigate | overlaps corpus-batch-processing and a SessionStart hook; keep skills, check hook |
| deep-research (account), tinyfish connector | keep | general research and web fetch |
| brightdata-plugin, shorty, user-intuition-research, signal-hunter, enterprise-search, legal, design, productivity, engineering, data, snowflake, bigquery, career-compass, career-brand, coach, sensei, the-life-edit, create-smartfolder | drop candidate | no connection to corpus/Android/GCP work; many need auth (22 servers); large listing |
| pm-toolkit, product-discovery-flow, sdlc-kit, ux-superpowers, analytics-office, mcpbinder, thinking-partner | drop candidate | PM/UX/analytics; pm-toolkit alone is 25 KB of descriptions + 4 hooks |
| Orchestration: agent-architecture-designer, fellowship, gangsta, maddog, 16-minds, decision-council, workflow-toolkit, agent-army, scaffold(x2), dev-forge, shipwright(x2), tenet, build-companion | drop candidate (keep at most one) | five frameworks re-implement plan/TDD/review/worktree; many register PreToolUse/Stop gates that compete with checkin-gate and stop-gate |
| pge-orchestrator + user-level pge-* | consolidate | shipped twice (plugin 2.7.0 and ~/.claude commands/agents); one MCP connected |
| agent-protocols | investigate | 25 skills + SessionStart; karpathy-guidelines, spec/plan/review skills are the cleanest; others overlap |
| wizard (x2), agent-smith, agent-design, agent-guardrails, mindpowers, mindmap, claude-md-composer, claude-md-management, prompt-enhancer, loop-and-gate-foundation, sarathi, adaptive-agent, agent-ingest-audit-optimize, foundation, second-arrow, local-whisper, reef, docbrain | investigate | authoring/analysis helpers, small each; claude-md-management and agent-guardrails are the most relevant to this stack; local-whisper/second-arrow are voice-adjacent to aesop-voice-pipeline |
| browser-use | keep | connected CDP tool (2 tools) |
| Failing MCP: graph-query-mcp, jevmem, oak-memory, desktop-commander, data:definite, engineering:github, pagerduty, asana, legal:box, data:bigquery | drop candidate | cannot start in this environment; engineering:github is blocked by session binding |
| Hook-only/mod plugins not in listing (rutter, agent-recall, prompt-coach, token-inspector, context-window, promptcolor, snoozing-pet, glance, compact-on-idle, usage-line, jev, crayon) | investigate | enabled state unverifiable; mods can draw panes/status; rutter adds a Stop hook |
| Marketplace additions to consider | investigate | kotlin-lsp, Mobile Release Check, GCP DevKit (IAM audit), huggingface-skills, session-report, MCP Workflow Audit, Setup Audit, Verified Security Sweep, session-sweep |
| Measurement first | investigate | run `claude plugin details <name>` (Always-on tokens) on the top 10 contributors before deciding; use the Installed tab "Not used recently" group |
