# Every skill on your account (2026-10-30)

This is a read-only listing from this cloud container. Each description is the first sentence of that skill's SKILL.md `description:`, cut at 180 characters.

**Totals:**

- **365 plugins** synced to this container. This is likely the "363" you remembered.
- **26** of those plugins are switched on and have files.
- **1568 skills** inside plugins, of which **84** are in plugins that are switched on.
- **20 account skills** you uploaded on claude.ai (section A).
- **Grand total: 1588 skills.**

Another 136 SKILL.md files sit in plugin folders made for other tools, such as `.gemini/skills`, `codex/skills`, `.agents/skills` and `.github/skills`, or in nested sub-skill folders. Claude doesn't load those, so they aren't counted or listed.

Plugins with no `skills/` folder are listed by name only. Their parts are commands, agents, hooks or MCP servers.

## A. Account skills (uploaded on claude.ai): 20

- **artifact-emulator**: See a page, slide deck or design canvas artifact you made, close to how a person will see it: open its files in the real artifact viewer inside this cloud session, then screensh…
- **built-in-browser**: Read this skill before the first step that uses the built-in browser, the browser pane inside the Claude desktop app (also called the in-app browser, the browser pane, Claude's …
- **chrome-browser**: Read this skill before the first step that uses Claude in Chrome, the browser extension whose tools are named mcp__claude-in-chrome__* (also called Chrome, the browser extension…
- **computer-use**: Read this skill before the first step of any request to do something in an app on the person's own computer (Notes, Finder, System Settings, any desktop app), to look at their s…
- **deep-research**: Use this skill when the user's prompt requires (1) researching a topic across multiple sources, comparing options or alternatives, analyzing trends or history, understanding mar…
- **docs**: docs (editable docs people share and comment on; the default for any document, named as a doc or not: a document, report, proposal, resume, cover letter, letter, contract, polic…
- **docx**: Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word templates (.dotx).
- **google-workspace**: Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or changes a Google file.
- **import-memory**: Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data.
- **learn**: Use this skill when the user wants intellectual understanding — learning how or why something works, not getting a task done or soliciting Claude's judgment.
- **mcp-builder**: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.
- **memory-as-skill**: User-controlled persistent memory system using plain Markdown files that the user can directly read, edit, and scope.
- **morning**: Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task.
- **pdf**: Use this skill whenever the user wants to do anything with PDF files.
- **pptx**: Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both.
- **skill-creator**: Create new skills, modify and improve existing skills, and measure skill performance.
- **technical-builder-style**: Custom writing style: Technical Builder.
- **termux-helper**: Termux Environment Skill You are an expert assistant specialized in the Termux environment on Android.
- **web-artifacts-builder**: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui).
- **xlsx**: Use this skill any time a spreadsheet file is the primary input or output.

## B. Plugin skills, with switched-on plugins first


### adb-mcp [ON] (6 skills)

- **build-and-test**: Mapping a multi-module Gradle project before guessing a task name, building a variant, running JVM vs on-device tests, and turning a JaCoCo coverage report into the specific lin…
- **crash-triage**: Using logcat to surface the real "Caused by:" root cause hidden behind a generic UI error, plus app lifecycle tools for reproducing failures.
- **driving**: The core observe→locate→act→re-observe loop for driving an Android UI with adb-mcp — true-pixel coordinates, and gotchas like overlays eating taps, keyboards covering buttons, a…
- **getting-started**: How to list AVDs, boot an emulator, target a device with the serial argument, and run a first interaction with adb-mcp.
- **pin-and-lock**: Entering digits on native (non-IME) PIN pads, and setting/clearing a secure lock screen required by AndroidKeyStore / Keystore-backed crypto flows.
- **rn-expo**: The RN/Expo dev-build recipe for adb-mcp — adb_reverse before launching (or the dev client silently runs its embedded bundle), app_state to confirm it is on Metro, on the RIGHT …

### building-with-typesafe-jev [ON] (1 skills)

- **building-with-typesafe-jev**: Use when code needs a judgment about natural language that rules or regex cannot make (classify, route, triage, moderate, score, rank, match, dedupe, filter, extract, verify, or…

### claude-bridge [ON] (1 skills)

- **browser-bridge**: Use whenever completing the user''s task requires acting in a web browser: logging into an account, changing or checking settings in a web dashboard (ads, hosting, DNS, analytic…

### claude-context-optimizer [ON] (22 skills)

- **cco**: Context Control Center — one screen for budget, $ spent, tokens saved, waste, last prompt grade, the active task, and ready-to-run optimization actions
- **cco-anatomy**: Generate a compact project map so Claude understands the codebase without opening every file
- **cco-budget**: Configure token budget limits, auto-compact settings, and view current budget status (model-aware — Claude 5 lineup, Opus 5.5 default fallback, full 1M context at standard price)
- **cco-claudemd**: Analyze CLAUDE.md files for token bloat and suggest optimizations
- **cco-clean**: Clean up old tracking data and reset statistics
- **cco-coach**: Analyze the user's last prompt for clarity, scope and specificity — give a quality score and concrete suggestions to make the next prompt produce better results
- **cco-config**: View and tune CCO's behavior thresholds — re-read warnings, cache staleness, prompt-coach length bands, and the /cco-pack budget cap
- **cco-digest**: Show weekly/daily efficiency digest with score and trends
- **cco-doctor**: Health check for the context-optimizer plugin install — verifies versions, hooks, data dir, model config, and reports any issues
- **cco-export**: Export context report as Markdown or HTML
- **cco-git**: Show git-aware context suggestions for current working directory
- **cco-overhead**: Audit the fixed context overhead every session starts with — system prompt, MCP tools, agents, CLAUDE.md, memory — measured from real transcript usage
- **cco-pack**: Build an optimal context pack for the user's task — ranked file list with offset/limit suggestions, based on git state, mentioned paths, and historical patterns
- **cco-patterns**: Share learned file patterns across a team — export an anonymized digest of what's usually waste/useful/co-edited, and import a teammate's so a fresh clone benefits day one
- **cco-replay**: Show recent session summaries for quick context recovery
- **cco-report**: Show detailed token ROI report across all tracked sessions
- **cco-roi**: Calculate monthly token savings and ROI by model
- **cco-shield**: Show ContextShield status and waste protection stats; suggest or apply .contextignore rules from historical waste
- **cco-task**: Organize work by task, track tokens/cost per task, and keep a small patchable execution state that is re-injected after /compact (SKILL.state-style) — start a task, patch its st…
- **cco-templates**: Manage context templates for common task types
- **cco-tools**: Show what tools actually cost in tokens — learned per-tool averages from observed results, replacing the hardcoded MCP/Agent guesses
- **smart-loader**: Automatically suggests optimal files to preload based on the user's task description and historical context patterns.

### claude-jev [ON] (1 skills)

- **jev**: Typed Jev decisions (Choice/Noul/Score) via live TypeSafe API — use when a task is a bounded decision (route/classify/score/gate) not open-ended text.

### claude-md-management [ON] (1 skills)

- **claude-md-improver**: Audit and improve CLAUDE.md files in repositories.

### consensus [ON] (1 skills)

- **ask**: When the user wants to cross-check ideas across multiple AI providers — look for phrases like \"consensus\", \"multiple perspectives\", \"what do other AIs think\", \"cross-chec…

### mcp-server-dev [ON] (3 skills)

- **build-mcp-app**: This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", m…
- **build-mcp-server**: This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an M…
- **build-mcpb**: This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb …

### memory-toolkit [ON] (11 skills)

- **docs-reflect**: Collect DOC: notes from session, generalize, and propose repo documentation (.claude/rules/, docs/).
- **memory**: Project memory — search, workstreams, notes, decisions.
- **memory-setup**: Initialize or upgrade project memory for memory-toolkit.
- **park**: Park an idea or task for the next session — save context, don't lose the thought.
- **reflect**: Session reflection — analyzes what happened, proposes backlog items, captures insights.
- **session-continue**: Continue a workstream from where you left off — faster than /session-start, no focus selection.
- **session-end**: Session completion — handoff, reflect, docs-reflect cascade.
- **session-insights**: Extract insights from past .jsonl sessions — problems, decisions, friction points.
- **session-restore**: Context restoration from .jsonl session backups.
- **session-start**: Cold session start — context, status, focus.
- **task-template**: Internal orchestrator — runs YAML pipelines with phases, dependencies, and verification gates.

### obsidian-notes [ON] (1 skills)

- **obsidian-notes**: Makes a folder of markdown work as an Obsidian vault that still renders on GitHub and in VS Code: lints for broken, mis-cased or ambiguous links, orphans, duplicate basenames, m…

### obsidian-sync [ON] (1 skills)

- **obsidian-sync**: Sync project documentation files (.md, .pdf) to an Obsidian vault for unified knowledge management.

### plugin-dev [ON] (7 skills)

- **agent-development**: This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent t…
- **command-development**: This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "orga…
- **hook-development**: This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLU…
- **mcp-integration**: This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external…
- **plugin-settings**: This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YA…
- **plugin-structure**: This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use $…
- **skill-development**: This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs …

### pmm [ON] (12 skills)

- **pmm:dump**: Dump PMM memory state as ASCII art in the terminal.
- **pmm:hydrate**: Populate empty or thin memory files from current session context.
- **pmm:init**: Initialize Poor Man's Memory in your project — runs preference wizard, scaffolds memory/ directory, configures hooks.
- **pmm:init-local-skills**: Install local skill variants for Cowork compatibility.
- **pmm:onboard**: Seed your user identity layer from a prior AI or direct interview.
- **pmm:query**: Query memory — context-first recall with deep traversal across vectors, graph, and taxonomy when needed.
- **pmm:recall**: Context-switching recall — synthesizes a focused briefing on a topic from across all memory files.
- **pmm:save**: Save current session to memory — dispatches maintain agent, updates memory files, commits to git.
- **pmm:settings**: Change Poor Man's Memory configuration.
- **pmm:status**: Quick PMM health dashboard.
- **pmm:update**: Check for and apply updates to Poor Man's Memory system files from upstream.
- **pmm:viz**: Interactive D3.js memory graph visualization with time slider.

### skill-creator [ON] (1 skills)

- **skill-creator**: Create new skills, modify and improve existing skills, and measure skill performance.

### superpowers [ON] (15 skills)

- **brainstorming**: You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior.
- **diagnosing-superpowers**: Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't fire, "it took too…
- **dispatching-parallel-agents**: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
- **executing-plans**: Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is available
- **finishing-a-development-branch**: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work
- **receiving-code-review**: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verific…
- **requesting-code-review**: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
- **subagent-driven-development**: Use when executing implementation plans with independent tasks in the current session
- **systematic-debugging**: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
- **test-driven-development**: Use when implementing any feature or bugfix, before writing implementation code
- **using-git-worktrees**: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or gi…
- **using-superpowers**: Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions
- **verification-before-completion**: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any s…
- **writing-plans**: Use when you have a spec or requirements for a multi-step task, before touching code
- **writing-skills**: Use when creating new skills, editing existing skills, or verifying skills work before deployment

### adaptive-agent [off] (2 skills)

- **build-user-profile**: Build or update the user profile memory by observing workspace context, git history,\nand conversation patterns.
- **skill-review**: Review all skills for staleness, missing gotchas, and improvement opportunities.\nRun periodically or after a series of tasks to keep procedural memory accurate.\nTrigger words:…

### agency-mcp [off] (12 skills)

- **client-audit**: Audits one client through the Agency MCP connector and returns a scorecard of what to fix first — Google Ads (conversion tracking, keywords and search terms spending with no con…
- **client-report**: Produces a clear, jargon-free weekly or monthly client report across every channel the client has linked — organic search, website, Google Ads, Meta ads, CRM leads and won work …
- **connect-accounts**: Connects platforms and logins to an Agency MCP account and groups the accounts into clients without mixing businesses up.
- **crm-followup**: Works a client's HighLevel CRM through the Agency MCP connector — who is waiting on a reply, pipeline and won-work numbers for a period, appointments booked, cancelled or no-sho…
- **google-ads-manager**: Manages a client's Google Ads through the Agency MCP connector — performance reports, search-term hygiene, negative keywords, budgets, bidding strategies, conversion tracking se…
- **keyword-research**: Researches keywords for a client using Google Ads planning data (volumes, competition, bid ranges) joined with what the site already ranks for in Search Console.
- **local-seo-gbp**: Manages a client's Google Business Profile through the Agency MCP connector — locations, reviews and owner replies, posts, and performance (calls, direction requests, website cl…
- **meta-ads-manager**: Reports on and manages a client's Meta (Facebook and Instagram) ads through the Agency MCP connector — spend, reach, clicks and conversions by campaign, pausing or enabling camp…
- **seo-audit**: Audits a client's organic search health using Search Console, Google Analytics and the live WordPress site through the Agency MCP connector.
- **seo-content**: Drafts or optimises a page or blog post on a client's WordPress site through the Agency MCP connector, including the SEO title, meta description and JSON-LD schema.
- **start**: First-run guide for Agency MCP.
- **weekly-review**: Reviews the changes an agency confirmed through the Agency MCP connector and what happened afterwards — each Google Ads or Meta ads change with the seven days before set against…

### agent-army [off] (1 skills)

- **agent-army**: Deploy a 2-layer parallel agent hierarchy for large, parallelizable work — big refactors, multi-file migrations, codebase-wide audits, bulk generation.

### agent-design [off] (3 skills)

- **agent-architecture-decide**: Make an agent vs workflow decision for this process, including single-call and code-only options.
- **agent-build-spec**: Write an agent specification for this AI agent or workflow.
- **agent-process-scope**: Map a business process for AI agent design before choosing what to automate.

### agent-discussion [off] (1 skills)

- **agent-discussion**: Multi-agent discussion coordination skill.

### agent-ingest-audit-optimize [off] (1 skills)

- **agent-ingest-audit-optimize**: Reads or imports external material, audits claims and recommendations against current primary evidence, and turns worthwhile findings into scoped, reversible improvements for AI…

### agent-memory [off] (1 skills)

- **memory-search**: Search past work and observations across sessions

### agentic-harness [off] (5 skills)

- **harness-feedback**: Run a kaizen retrospective on an agentic-harness run and, with the user's consent, file tool-improvement feedback as a GitHub issue on the upstream agentic-harness repo.
- **harness-review**: Assess an existing agentic harness — read-only.
- **harness-setup**: Build, extend, and maintain a project's agentic harness — the agents, skills, and orchestrator under .claude/.
- **spec-advisor**: Detect whether a software project lacks a spec-driven development system and, if so, advise which one fits (GitHub Spec Kit, OpenSpec, BMAD-METHOD, Agent OS, Taskmaster, AWS Kir…
- **tracker-advisor**: Detect whether a software project lacks an issue tracker suited to agentic work and, if so, advise which one fits (Beads, Backlog.md, git-bug, git-issues, Beans, or GitHub Issue…

### agentic-sdlc [off] (11 skills)

- **crafting-commits**: Use when the user wants to clean up commits, rewrite git history, squash messy commits, apply conventional commits, or prepare a branch for PR review.
- **fetching-tickets**: Use when fetching a Jira ticket to disk is needed as a standalone operation.
- **generating-tasks**: Use when a feature/implementation plan exists (e.g.
- **implementing-tasks**: Use when implementing a task specification with test-driven development and you want the right testing skill picked automatically per project type.
- **picking-up-task**: Use when the user wants to start a new task — accepts a Jira ticket URL, Jira key, or local ticket file path.
- **planning-from-spec**: Use when the user has a spec, ticket, or requirement doc (local file or pasted text) and wants an implementation plan.
- **receiving-plan-review**: Use when a reviewing-plan verdict is DO NOT PROCEED or PROCEED WITH CHANGES and findings need to be worked through — before editing the plan.
- **reviewing-code**: Use when the user wants to review and verify implemented code before considering it done or opening a PR.
- **reviewing-plan**: Use when a PLAN+TASKS markdown file exists and the user wants it judged against its ticket BEFORE any code is written.
- **testing-pytest**: Use when writing, reviewing, or improving Python tests with pytest.
- **testing-vitest**: Use when writing, reviewing, or improving tests for React projects using Vitest and TypeScript.

### agentmail [off] (9 skills)

- **agent-email-patterns**: Architecture patterns for AI agents that communicate over email -- why agents need dedicated inboxes rather than human email accounts, infrastructure/provider tradeoffs, one-inb…
- **agentid**: Create accounts for an agent at third-party services with AgentID, using an AgentMail inbox as the agent's identity, and see where each inbox already has an account.
- **agentmail**: Build with the AgentMail TypeScript or Python SDK for inbox, message, thread, draft, attachment, domain, allow/block list, pod, webhook, and WebSocket workflows, including progr…
- **agentmail-cli**: Operate AgentMail from a shell with the official CLI.
- **agentmail-mcp**: Configure or troubleshoot the hosted AgentMail MCP server for Codex, Claude Code, Cursor, Claude.ai, ChatGPT, or another Streamable HTTP MCP client.
- **agentmail-toolkit**: Add AgentMail tools to agent frameworks with the TypeScript or Python AgentMail Toolkit.
- **check-email**: Read, search, summarize, and triage AgentMail inboxes through the connected MCP server.
- **manage-inboxes**: Create, list, inspect, update, or delete AgentMail inboxes through the connected MCP server.
- **send-email**: Draft, send, reply to, or forward email through the connected AgentMail MCP server.

### ai-advisors [off] (4 skills)

- **aeo-audits**: Interpret and act on AI-Advisors AEO (Answer Engine Optimization) audit findings - crawler access, server-side rendering, structured data and entity graphs, content freshness an…
- **ai-advisors-setup**: Set up and verify the AI-Advisors connection - create the API token, configure it, and confirm the tools respond.
- **ai-search-visibility**: Read and interpret AI search visibility data from AI-Advisors - which tracked prompts mention or cite the brand across ChatGPT, Claude, Gemini and Perplexity, who wins the answe…
- **ai-traffic-and-crawlers**: Interpret AI-Advisors traffic data - visits referred from AI assistants, AI crawler activity, paid versus organic AI traffic, and how AI numbers reconcile against Google Search …

### ai-employees [off] (1 skills)

- **hire**: Hire one of the eight open source AI Employees (GTM Engineer, SEO/AEO, Web Dev, Social Media, Ad Manager, Sales, Customer Satisfaction, Chief of Staff) into a local folder, prov…

### ai-integration-architect [off] (1 skills)

- **ai-integration-architect**: Design, plan, and scaffold AI integration into enterprise systems.

### ai-mentor [off] (1 skills)

- **mentor**: Match a developer's question or problem to the best AI workflow, ranked and personalized from a persistent profile of what they already know.

### ai-native-os [off] (25 skills)

- **agentic-build-loop**: Use when a founder says "how do I actually build this", "Claude Code/Codex/Cursor keeps making a mess", "the agent wrote spaghetti", "it passed but I don't trust it", "I'm just …
- **ai-assisted-sales**: Use when a founder is stuck in pilot purgatory, when deals go quiet after a thrilled champion says yes, when they say "the pilot stalled", "they loved the demo but procurement w…
- **apply-ai-native-models**: Use when a founder faces a hard, consequential call and is about to guess - build-or-buy, what to ship, whether to automate something irreversible, whether a slick demo proves a…
- **architect-before-code**: Use when a founder says "let's start building", "what's the architecture", "should I just prototype this", "the codebase is a mess", "the AI keeps building a different thing eac…
- **capture-learning**: Use when a real outcome just landed and the lesson should be banked so the OS stops repeating mistakes - an eval result, a customer reply, a metric move, a failed or won launch,…
- **cognitive-architecture-review**: Use when an AI system already exists or is half-designed and you need to judge whether it is AI-native or a dressed-up wrapper.
- **compliance-readiness**: Use when an AI or agent workload is heading into a security review, an enterprise buyer's questionnaire, or an audit and you do not yet know which frameworks you touch.
- **customer-discovery-that-doesnt-lie**: Use when a founder is running customer interviews and wants the truth, not applause - when they say "everyone loves it", "I talked to fifteen people and they're all interested",…
- **design-a-loop**: Use when a founder wants to automate a recurring agentic task and is moving from prompting to system design - when they say "should I set up a loop", "automate this with agents"…
- **design-the-mva**: Use when a founder is about to build the first version and is piling features instead of proving one loop - \"what's my MVP\", \"what should I build first\", \"scope this down\"…
- **eval-and-safety-harness**: Use when a founder says "is this safe to ship", "it hallucinated to a customer", "it made up a citation", "we need clinical/food-safety/financial guardrails", "how do I evaluate…
- **frame-the-hypothesis**: Use when a founder has a vague AI idea and needs to sharpen it into one falsifiable bet before building - when they say "is this worth building", "how do I validate this", "I ha…
- **gateway-agent-ops**: Use when one agent is trying to do every operational job and it is drifting, getting confused, or running up a bill - when the founder says "my agent does everything", "it route…
- **geo-content**: Use when a founder asks why the AI engines never name them, when traffic holds but the buyer \"already decided\" before the call, when they say \"we rank but ChatGPT cites a com…
- **hypothesis-mining**: Use when a founder has a pile of raw input - interview notes, support logs, search data, papers, competitor reviews - and needs to convert it into testable bets, or has too many…
- **map-the-terrain**: Use when a founder needs the market, competitor, and regulatory terrain mapped before building - when they say "who are my competitors", "what's the regulatory path", "how long …
- **measure-ai-native-pmf**: Use when a founder is mistaking AI novelty for demand and needs the real PMF read - \"do we have PMF\", \"is this working\", \"what metrics matter\", \"users love the demo but\"…
- **moat-strategy**: Use when a founder needs to know what actually defends the company once building is free - when they say "what's my moat", "a competitor could clone this in a weekend", "is my d…
- **pay-down-agentic-debt**: Use when an agent-built codebase has grown faster than anyone understands it and every change feels risky - when they say "the codebase is a mess", "I'm scared to touch this", "…
- **red-team-the-agent**: Use when an agent is about to meet real users or an auditor and you need to attack it first, the way a hostile user or a security reviewer would.
- **secure-the-connectors**: Use when an agent is about to get tools or connectors and you need to bound what it can actually do, the way a security reviewer would before granting access.
- **self-healing-fallbacks**: Use when an AI workflow has to survive a model that fails, stalls, or answers with low confidence instead of shipping a confident wrong answer - when they say "what happens when…
- **share-of-model-audit**: Use when a founder needs to know how often the AI engines name them versus rivals for the questions buyers actually ask, when they say "measure my Share of Model", "do ChatGPT a…
- **start-here**: Use when a founder is unsure where to begin or what to do next on an AI build - when they say "where do I start", "I want to build with AI", "is my idea AI-native or a wrapper",…
- **write-the-claude-md**: Use when an agent keeps relearning the codebase from a blank page every session and getting it confidently wrong.

### ai-youtube-os [off] (1 skills)

- **channel-operations**: 유튜브 채널 폴더(channel.json + OPERATIONS.md)에서 영상 제작·업로드·지표 기록 작업을 할 때 사용한다.

### analytics-skills [off] (13 skills)

- **analytics-diagnostic-method**: The spine of analytics investigation.
- **analytics-profile-setup**: One-time interview that captures the business context (industry, model, primary conversion, traffic range, ICP, data stack) into a local analytics-profile.md file.
- **anomaly-detection-time-series**: Formal time-series methods that augment the hand-coded fingerprint library in traffic-change-diagnosis.
- **bayesian-experiment-reader**: Bayesian counterpart to experiment-result-reader.
- **causal-dag-builder**: Build a refinable causal DAG before answering "did X cause Y" on observational data.
- **causal-evidence-checklist**: Bradford Hill's 9 viewpoints (1965) reframed as a checklist for product analytics.
- **causal-query-classifier**: Pearl's three-rung causal hierarchy as a query classifier.
- **channel-and-funnel-quality**: Judge whether traffic is actually valuable and whether funnel drop-off is real or expected.
- **event-schema-author**: Author and maintain an event-schema.yaml file.
- **experiment-result-reader**: Read the result of a running A/B test honestly.
- **metric-context-and-benchmarks**: Interpret analytics metrics with correct context.
- **sequential-monitoring**: Always-valid sequential inference for honest peeking at running A/B tests.
- **traffic-change-diagnosis**: Diagnose why website traffic changed.

### anamnese-core [off] (1 skills)

- **anamnese**: Load this skill at the start of every conversation.

### ancestralfire [off] (7 skills)

- **ancestralfire**: Use for any question about the person's own family, ancestors, relatives or family tree (AncestralFire, ancestral-fire.com: family history, genealogy, FamilySearch), including h…
- **ancestralfire-change**: Use for any question about the person's own family, ancestors, relatives or family tree (AncestralFire: family history, genealogy, FamilySearch) of this kind: asks to add, fix, …
- **ancestralfire-connect**: Use for any question about the person's own family, ancestors, relatives or family tree (AncestralFire: family history, genealogy, FamilySearch) of this kind: telling us who the…
- **ancestralfire-interesting**: Use for any question about the person's own family, ancestors, relatives or family tree (AncestralFire: family history, genealogy, FamilySearch) of this kind: an open question, …
- **ancestralfire-keep**: Use for any question about the person's own family, ancestors, relatives or family tree (AncestralFire: family history, genealogy, FamilySearch) of this kind: make, save, share …
- **ancestralfire-people**: Use for any question about the person's own family, ancestors, relatives or family tree (AncestralFire: family history, genealogy, FamilySearch) of this kind: a question about s…
- **ancestralfire-world**: Use for any question about the person's own family, ancestors, relatives or family tree (AncestralFire: family history, genealogy, FamilySearch) of this kind: the world beyond t…

### anchor-memory [off] (7 skills)

- **capture-decision**: Use when a load-bearing decision was made or reversed — appends a dated, WHY-first entry to the memory ledger, optionally with a verifiable @meta anchor.
- **handoff**: Use to snapshot where you are so a future session (or you after a rate limit) can resume cleanly — writes memory/HANDOFF.md with goal, what's done, the next step, and open threads.
- **memory-init**: Use to bootstrap Anchor in a project — scaffolds AGENTS.md/CLAUDE.md/GEMINI.md, the memory ledger, anchor.config.json, and wires the integrity hooks.
- **recall**: Use before proposing any new architecture, experiment, or comparison — reads the ledger and runs the integrity linter so you don't re-propose a failed idea or quote stale facts.
- **review-pr**: Use to review a pull request against the project's own rules — license allowlist and architecture invariants read from anchor.config.json.
- **session-wrapup**: Use at the end of a work session to run the memory ritual — capture decisions, update status, mark superseded entries.
- **update-status**: Use to move items between Now/Next/Blocked/Done in the project status ledger.

### apify [off] (5 skills)

- **apify-actor-development**: Develop, debug, and deploy Apify Actors - serverless cloud programs for web scraping, automation, and data processing.
- **apify-actorization**: Convert existing projects into Apify Actors - serverless cloud programs.
- **apify-generate-output-schema**: Generate output schemas (dataset_schema.json, output_schema.json, key_value_store_schema.json) for an Apify Actor by analyzing its source code.
- **apify-sdk-integration**: Integrate Apify into an existing JavaScript/TypeScript or Python application using the apify-client package.
- **apify-ultimate-scraper**: Universal AI-powered web scraper for any platform.

### backlog [off] (7 skills)

- **handoff**: Prepare a session handoff — summarize progress, annotate tasks with current status, and identify what's ready for the next session.
- **implement**: Pick up a task from the backlog and implement it.
- **plan**: Break down a goal into actionable tasks with dependencies, priorities, and optional specs.
- **refine**: Review and improve the backlog — identify vague tasks, missing priorities, broken dependencies, tasks needing specs, and stale items.
- **spec**: Write a detailed spec document for a task before implementation begins.
- **standup**: Daily standup summary — what was completed recently, what's in progress, and what's blocked.
- **tasks**: Show the current task backlog — pending, active, blocked, and overdue tasks.

### bake-claude-md-files [off] (1 skills)

- **bake-claude-md-files**: Converts CLAUDE.md rules into automated checks, removes the automated rules from CLAUDE.md, and verifies everything passes.

### bigquery-data-analytics [off] (1 skills)

- **bigquery-ai-ml**: Skill for BigQuery AI and Machine Learning queries using standard SQL\nand `AI.*` functions (preferred over dedicated tools).\n

### build-harness [off] (1 skills)

- **build-harness**: Guides a person interactively through building their own multi-agent harness for their field in Claude Code, covering Context Engineering, Roles (subagents), Tools/MCP, Multi-Ag…

### cache-guard [off] (1 skills)

- **handoff**: Write a handoff file so a fresh session can continue this work without the conversation: goal, decisions, state, files, what is left, next step.

### caveman [off] (1 skills)

- **caveman**: Use when the user wants short, direct answers without filler, for quick questions or when they only need the code.

### caveman [off] (1 skills)

- **caveman**: Use this skill whenever the user says "caveman mode", "caveman", "talk like caveman", "speak simple", "dumb it down", "ELI5 caveman", or asks to switch to short/simple talk.

### cc-bootstrapper [off] (1 skills)

- **bootstrap**: Генерирует полную .claude/ структуру автоматизации для любого проекта — агенты, пайплайны, скиллы, memory, hooks, settings.

### ccaf [off] (3 skills)

- **ccaf-exam**: Engine for the /ccaf:mock-exam mock exam.
- **ccaf-practice**: Engine for the /ccaf:practice command.
- **ccaf-tutor**: Engine for the /ccaf:prepare conversational tutor.

### ccfind [off] (1 skills)

- **ccfind**: Search the user's own past Claude Code sessions by content and report which conversation discussed a thing, when, in which project, and how to resume it.

### ccgrapher [off] (1 skills)

- **parallel-plan**: Turn a plan, or a messy brain dump of features, fixes and ideas, into the order the work really has, by checking which steps actually depend on each other, running the independe…

### changethisfile [off] (1 skills)

- **file-conversion**: Convert files between formats — PDF to Word, HEIC to JPG, MP4 to MP3, CSV to JSON, EPUB to MOBI, and 1,000+ supported routes across images, video, audio, documents, data, fonts,…

### chat-namer [off] (5 skills)

- **auto-name**: Auto-name all unnamed conversations from their first message
- **list**: List all Claude Code conversations with their names, dates, and message counts
- **rename**: Rename a conversation by its number or UUID prefix
- **resume**: Find and resume a previous conversation by name or keyword instead of UUID
- **search**: Search conversations by name or content keyword

### chuck [off] (1 skills)

- **chuck**: Creates interactive HTML playgrounds for Chuck setup and decision logging.

### ci-optimizer [off] (1 skills)

- **ci-optimizer**: Use when a GitHub Actions or GitLab CI pipeline is slow, expensive, flaky or being written, to find missing caches, wasted runs, unsafe settings and the slowest jobs.

### claude-backup [off] (1 skills)

- **backup**: Manage Claude Code backups — sync config and sessions, list/restore sessions, check status.

### claude-blog-assistant [off] (1 skills)

- **assistant**: Dual-mode blog publishing assistant.

### claude-code-feedback [off] (5 skills)

- **feedback-bug**: File a well-formed bug report against anthropics/claude-code.
- **feedback-docs**: File a documentation issue against anthropics/claude-code — missing docs, outdated docs, incorrect docs, or docs improvements.
- **feedback-feature-request**: File a well-formed feature request against anthropics/claude-code.
- **feedback-model-behavior**: File a report about Claude's model behavior (bad responses, refusals, hallucinations, policy misfires, poor code quality) against anthropics/claude-code.
- **feedback-refresh-templates**: Refresh cached Anthropic claude-code issue-form templates and detect drift or new template types.

### claude-code-setup [off] (1 skills)

- **claude-automation-recommender**: Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers).

### claude-damn [off] (61 skills)

- **add-to-roadmap**: Use when you want to append a new task to a specific phase or section of the\nproject ROADMAP.md.
- **address-pr-feedback**: Address PR Feedback command
- **atlas**: Render a single "where am I, what have I done, what's next" survey HTML page composing anchor cascade + tesseract shelf + git state + CHECKPOINT.md + TaskList.
- **cat**: Subagent-driven development as the explicit combination of /subagent-driven-development (sequential, review-gated execution) and /dispatching-parallel-agents (independent fan-out).
- **check-yourself**: Use when a discrete task boundary is crossed in multi-step work — step completion, subagent dispatch return, Skill-tool invocation return, /proceed gate passed, test-run complet…
- **checkpoint-resume**: Use when resuming paused work, starting a session where a CHECKPOINT.md exists, or when the user says "continue from checkpoint", "resume", or "pick up where we left off
- **checkpoint-save**: Use when pausing work that will be resumed later, when switching contexts, or when the user asks to save a checkpoint.
- **continue**: retry last operation attempted before the user interrupted the process, or otherwise continue last attempted tool use
- **cost-opt**: Compact cost logs, recalibrate the pricing table in ~/.claude/extract_cost.py and statusline-command.sh against platform.claude.com/cost extracts, and surface optimization sugge…
- **cost_**: Extract and log cost data for the current session.
- **draft-cmt-msg-4-below**: draft a commit message for the below changes
- **duper**: Isolated git worktree workflow (alias for /using-git-worktrees)
- **duper-tdd**: TDD workflow using an isolated git worktree
- **duper-tdd-cat**: TDD workflow using an isolated git worktree with subagent-driven-development
- **expert-cat-review**: Expert-level review with each phase dispatched as a parallel subagent
- **expert-duper-tdd-cat-review**: Expert-level review with subagents, then fix using TDD in an isolated git worktree with subagents
- **expert-duper-tdd-review**: Expert-level review, then fix using TDD in an isolated git worktree
- **expert-final-review**: Final pre-merge gate — verify all PR peer feedback is addressed, then run a full /expert-review
- **expert-review**: Expert-level multi-language code review, simplification, debugging, and security audit
- **expert-super-cat-review**: Expert-level review with subagents, then brainstorm and fix with subagents
- **expert-super-duper-cat-review**: Expert-level review with subagents, then brainstorm and fix in an isolated git worktree with subagents
- **expert-super-duper-review**: Expert-level review, then brainstorm and fix in an isolated git worktree
- **expert-super-duper-tdd-cat-review**: Expert-level review with subagents, then brainstorm and fix using TDD in an isolated git worktree with subagents
- **expert-super-duper-tdd-review**: Expert-level review, then brainstorm and fix using TDD in an isolated git worktree
- **expert-super-review**: Expert-level review, then brainstorm and fix
- **expert-super-tdd-cat-review**: Expert-level review with subagents, then brainstorm and fix using TDD with subagents
- **expert-super-tdd-review**: Expert-level review, then brainstorm and fix using TDD
- **expert-tdd-cat-review**: Expert-level review with subagents, then fix using TDD with subagents
- **expert-tdd-review**: Expert-level review, then fix using TDD
- **fast-pr-feedback-to-me**: Process code review feedback received on current PR
- **fast-pr-feedback-to-others**: Give code review feedback on current PR
- **fast-pr-final-self-review**: Self-review to verify all PR peer feedback has been addressed on current branch
- **fixer**: Systematic debugging (alias for /superpowers:systematic-debugging)
- **jcvd**: Open the best Jean-Claude Van Damme movie in your browser.
- **learn**: Use when you want to review the current session for skills that misfired (skipped, invoked-but-ignored, or triggered user corrections) and update them — scans the active transcr…
- **legal-visual-aid**: Use when the user gives a contract (text, file, or paste) and wants both an analysis AND an at-a-glance visual — "review this contract and make me a one-pager", "summarize this …
- **lets-make-a-skill**: Use when creating or improving a skill that must both perform well on real prompts AND hold under rationalization pressure (discipline rules, process guardrails, workflows agent…
- **listen**: Execute instructions while listening for and invoking every skill referenced within them
- **pause**: Use when wrapping up a session, parking work at a clean stop, or reaching a natural boundary where you want to close out current progress without starting new work
- **proceed**: Signal alignment and authorize Claude to pass the current approval gate only — single-use approval for the pending checkpoint (design review, plan approval, risky-action confirm…
- **review**: Review command
- **sme-test**: TDD coach: guides users through Given/When/Then test design using a Subject Matter Expert approach.
- **super**: Brainstorming (alias for /brainstorming)
- **super-cat**: Brainstorming with subagent-driven-development
- **super-duper**: Brainstorming workflow using an isolated git worktree
- **super-duper-cat**: Brainstorming workflow using an isolated git worktree with subagent-driven-development
- **super-duper-fixer**: Expert review to debug, then fix using brainstorming workflow in an isolated git worktree
- **super-duper-fixer-cat**: Expert review to debug, then fix using brainstorming workflow in an isolated git worktree with subagent-driven-development
- **super-duper-fixer-tdd-cat**: Expert review to debug, then fix using brainstorm+TDD workflow in an isolated git worktree with subagent-driven-development
- **super-duper-tdd**: Brainstorm+TDD workflow using an isolated git worktree
- **super-duper-tdd-cat**: Brainstorm+TDD workflow using an isolated git worktree with subagent-driven-development
- **super-fixer**: Expert review to debug, then fix using brainstorming workflow
- **super-fixer-cat**: Expert review to debug, then fix using brainstorming workflow with subagent-driven-development
- **super-tdd**: Brainstorm first, then implement using TDD
- **super-tdd-cat**: Brainstorm first, then implement using TDD with subagent-driven-development
- **sync**: Sync files between two local directories, repos, or git worktrees.
- **task-list**: TaskCreate / TaskUpdate / render the current TaskList in response to `/task-list` (with or without flags).
- **tdd**: Invoke test-driven development as an explicit one-at-a-time micro-cycle — one test, one piece of functionality, refactor, then repeat for the next behavior
- **tdd-cat**: TDD workflow with subagent-driven-development — /tdd composed with /cat, plus the A/B TDD execution-mode axis (split-phase vs micro-cycle) asked as a third question in /cat's co…
- **tesseract**: Use when you've been poking at the same file, concept, or problem across many sessions and want to step outside time to see its whole arc — or when you want to leave a note for …
- **visual-aid**: Use when the user asks for a quick visual aid, visual explainer, concept card, one-pager, poster, cheat sheet, infographic, visual summary, summary card, or mini explainer page …

### claude-deconstruct [off] (1 skills)

- **deconstruct**: First-principles analyst.

### claude-forge [off] (6 skills)

- **bootstrap**: Run the deterministic platform health check, summarize readiness, and recommend the next step for this repository.
- **gap-note**: Record a structured note when the approved spec and repository reality diverge during implementation.
- **milestone-report**: Produce a standardized milestone completion report with evidence, changed files, verification results, residual risks, and the next todo.
- **review**: Orchestrate a multi-review pass from requirements through consensus.
- **session-handoff**: Generate a precise handoff packet for the next Claude Code session.
- **test**: Run structured verification, capture actual command outcomes, and summarize what is verified versus unverified.

### claude-handoff [off] (1 skills)

- **handoff**: Generate a handoff prompt summarizing current work and launch a fresh Claude Code session.

### claude-mac-chrome [off] (2 skills)

- **check-emails-all-profiles**: Check unread email count across all Chrome profiles on macOS (Gmail, ProtonMail, Fastmail, Outlook).
- **chrome-multi-profile**: Reliably automate Chrome on macOS across multiple profiles (Personal / Work / School / etc.) using Chrome's own authoritative profile catalog (Local State file) combined with st…

### claude-md-composer [off] (1 skills)

- **claude-md-composer**: Audit, compose, and refactor CLAUDE.md files so they stay under the token budget.

### claude-memory [off] (1 skills)

- **structured-memory**: This skill should be used when the user asks to \"set up memory\", \"configure memory\", \"add memory to my project\", \"remember things across sessions\", or mentions wanting C…

### claude-opus-4-5-migration [off] (1 skills)

- **claude-opus-4-5-migration**: Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5.

### claude-patterns [off] (1 skills)

- **patterns**: Instinct Engine — scans recent sessions, journals, and decisions for recurring patterns and turns them into concrete captures (CLAUDE.md rules, concept notes, writing seeds, ski…

### claude-perfectionist [off] (1 skills)

- **claude-perfectionist**: Activate when the user wants to edit, trim, audit, reorganize, or debug CLAUDE.md or any Claude Code config file.

### claude-performance [off] (1 skills)

- **performance**: Use this skill when the user says /performance, /digest, asks for a weekly Claude performance report, or wants to review how their Claude Code sessions have been going.

### claude-piggy-bank [off] (1 skills)

- **cpb**: Open the Claude Piggy Bank report — where this project's context and token spend went

### claude-release [off] (1 skills)

- **release**: Use this skill when the user invokes `/claude-release:release` or asks to ship, cut, tag, or publish a release of the current project.

### claude-review-loop [off] (1 skills)

- **review-loop**: Automated code review and swarm remediation — reviews changes, presents findings for human annotation, then dispatches a fixer team to remediate.

### claude-security [off] (1 skills)

- **claude-security**: The Claude Security menu — pick a job: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or one commit), or …

### claude-stats [off] (1 skills)

- **claude-stats**: Show Claude Code token usage and estimated API cost broken down by project and timeline.

### claude-win-notify [off] (1 skills)

- **plugin-dev**: Use when the user asks about this plugin's architecture, wants to add a new hook event, edit notify.mjs, modify hooks.json, run plugin tests, or debug notification issues.

### claudebase [off] (6 skills)

- **sync-config**: Use when the user wants to view or change claudebase settings like global sync, agent skills sync, auto-push, or machine ID.
- **sync-profiles**: Use when the user wants to list, create, switch, delete, compare, or inspect config sync profiles.
- **sync-pull**: Use when the user wants to restore, download, or pull their Claude Code config from GitHub onto this machine.
- **sync-push**: Use when the user wants to back up, save, or push their current Claude Code config to GitHub.
- **sync-setup**: Use when the user wants to set up config sync for the first time, connect to GitHub, or re-initialize the backup repo.
- **sync-status**: Use when the user wants to check what config has changed, see sync status, or compare local vs remote config.

### claudestrophobic [off] (2 skills)

- **projects**: List every Claude Code project; delete the orphaned ones
- **sessions**: List and manage sessions in the current project

### claudify [off] (2 skills)

- **init**: Bootstrap a clean .claude/ folder structure for any existing repo following official Claude Code best practices
- **update**: Keep CLAUDE.md files in sync with the current codebase using claude-md-management

### clawback [off] (1 skills)

- **configure**: Set up the Clawback channel — save the connection token and check status.

### clawness [off] (14 skills)

- **add**: Create a new Clawness rule from a natural language description.
- **audit-rules**: Review one domain of the Clawness rule corpus for correctness against current official documentation, then record what was established as a version stamp (applies_to / verified …
- **bootstrap**: Author a starter set of Clawness rules for a project whose stack Clawness ships no corpus for (Ruby, PHP, Elixir, Haskell, C#, Swift, Dart, Scala, Clojure, ...).
- **claude-md**: Shrink an oversized CLAUDE.md.
- **eval-set**: Build and run a project-specific retrieval eval so changes to your rules or base prompt are scored, not eyeballed.
- **messaging**: Write or rewrite the product's customer-facing copy — landing page, hero section, CTAs, onboarding, empty states, pricing, app-store and marketing pages — with the customer as t…
- **openclaw-audit**: Trim an OpenClaw workspace's base system prompt.
- **perf**: Run a performance audit on the project or a specific module.
- **refresh**: Bring this project's Clawness rules up to date with the framework version it actually runs.
- **review**: Run an adversarial code review on staged changes or a specific file.
- **security-audit**: Run a stateful red team / blue team security audit on the current project or a specific module.
- **status**: Show the current Clawness configuration: which rules are loaded, which agents are available, and how the hook is configured.
- **test**: Generate comprehensive tests for a file or module.
- **user-docs**: Write user documentation for a project by scanning its codebase — its UI screens and its public API/CLI — inferring what someone can actually do with it, and drafting brief, tas…

### clean-architecture [off] (15 skills)

- **boundary**: (no description)
- **check**: (no description)
- **components**: (no description)
- **controller**: (no description)
- **diagram**: (no description)
- **entity**: (no description)
- **gateway**: (no description)
- **init**: (no description)
- **main**: (no description)
- **migrate**: (no description)
- **presenter**: (no description)
- **review**: (no description)
- **solid**: (no description)
- **test**: (no description)
- **usecase**: (no description)

### cloudflare [off] (14 skills)

- **agents-sdk**: Build, debug, or review Cloudflare Agents SDK applications using the agents package.
- **cloudflare**: Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security.
- **cloudflare-email-service**: Implement or troubleshoot Cloudflare Email Sending and Email Routing integrations and their delivery configuration.
- **cloudflare-one**: Design, configure, troubleshoot, or review Cloudflare One Zero Trust and SASE deployments.
- **cloudflare-one-migrations**: Assess and plan migrations from existing VPN, SWG, or SASE platforms to Cloudflare One, including policy mapping, parity gaps, and rollout.
- **durable-objects**: Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination.
- **nextjs-on-cloudflare**: Build, migrate, and deploy Next.js apps on Cloudflare Workers with vinext.
- **sandbox-migrate-to-next**: Migrate Cloudflare Sandbox apps from stable @cloudflare/sandbox to @cloudflare/sandbox@next (SDK 1.0 preview).
- **sandbox-next**: Build or maintain Cloudflare Sandbox apps on @cloudflare/sandbox@next (SDK 1.0 preview).
- **sandbox-stable**: Build or maintain Cloudflare Sandbox apps on the stable @cloudflare/sandbox package.
- **turnstile-spin**: Set up, repair, or migrate to Cloudflare Turnstile bot verification in an existing frontend and backend, including server-side Siteverify.
- **web-perf**: Audit, diagnose, or optimize website loading and interaction performance, Core Web Vitals, and Lighthouse performance scores.
- **workers-best-practices**: Cloudflare Workers best practices for production applications.
- **wrangler**: Run or troubleshoot Wrangler CLI commands and configure Worker projects for local development, deployment, and Cloudflare resource management.

### code-graph [off] (1 skills)

- **code-graph**: Use when someone needs to understand a complex subsystem they didn't write - "how does X work", "what breaks if I change Y", onboarding to unfamiliar code, or mapping a subsyste…

### code-map [off] (1 skills)

- **code-map**: Generate an interactive, self-contained HTML map of a codebase — a pan/zoom node graph with a detail panel, search, layer filters, flow walkthroughs, and matrices, with every no…

### code-parser [off] (1 skills)

- **code-parser**: Use this skill whenever you need to read, understand, navigate, edit, refactor, or reason about a codebase written in Dart, Python, or TypeScript — especially before reading any…

### code-review-harness [off] (2 skills)

- **harness-review**: Independent Evaluator for code review harness.
- **harness-review-ja**: コードレビューハーネスの独立したEvaluator（日本語版）。 コードを読むだけでなく実際に動かして確認することで、静的解析では見逃すバグを発見する。 TRIGGER when: ユーザーがハーネスレビューまたは独立したコードレビューを依頼した場合。 IMPORTANT: このコードベースで以前作業したセッションとは別の、新規セッションで実行すること…

### code-review-plugin [off] (1 skills)

- **code-review**: 代码审查 / code review / 检查 bug / 安全审计 / security audit / lint / 代码质量。审查 git diff、最近 commit、指定文件或粘贴的代码片段，输出按严重度与优先级分级的 Markdown 报告与修复片段。支持 TypeScript / JavaScript / Python / Go / Ru…

### codebase-mentor [off] (2 skills)

- **codebase-mentor**: Explain unfamiliar code, trace execution paths, plan changes, and check onboarding docs against current source.
- **onboard**: Generate a draft ONBOARDING.md by reading current source and asking the developer for missing rationale, gotchas, and ownership.

### coding-skills [off] (30 skills)

- **algorithmic-complexity-attacks**: This skill should be used when the user asks "is this regex safe", "what is ReDoS", "why does CPU spike on one request", "how do I safely accept uploads or XML", "is this parser…
- **cache-stampede**: This skill should be used when the user asks "how do I stop a thundering herd", "why does load spike when a cache key expires", "how should I set cache TTLs", "how do I handle c…
- **clocks-and-time**: This skill should be used when the user asks "how do I measure elapsed time correctly", "why do timestamps disagree across servers", "how do I order events across machines", "sh…
- **code-hotspots**: This skill should be used when the user asks "where should we start refactoring", "which files are riskiest", "what is our tech debt priority", "which files always change togeth…
- **connascence**: This skill should be used when the user asks "why is this so tightly coupled", "how do I decouple these", "is this coupling acceptable across a module boundary", or when reviewi…
- **connection-pooling**: This skill should be used when the user asks "how many database connections should I use", "why is the database out of connections", "should I use PgBouncer", "what is transacti…
- **consistent-hashing**: This skill should be used when the user asks "how do I shard this data", "how do I add a node without rehashing everything", "what is consistent hashing", "should I use rendezvo…
- **coordinated-omission**: This skill should be used when the user asks "why is production latency worse than our load test", "is this benchmark trustworthy", "how do I aggregate p99 across servers", "whi…
- **cyclomatic-complexity**: This skill should be used when the user asks "how complex is this function", "count the branches", "find overly complex functions", "set a complexity threshold", "reduce cycloma…
- **database-queues**: This skill should be used when the user asks "how do I build a job queue in Postgres", "what is SELECT FOR UPDATE SKIP LOCKED", "why are jobs processed twice", "how do I publish…
- **dependency-confusion**: This skill should be used when the user asks "how do I secure our package supply chain", "what is dependency confusion", "how do I stop typosquatting", "is this package safe to …
- **expand-contract**: This skill should be used when the user asks to "rename a column without downtime", "drop a column safely", "add NOT NULL to a live table", "add an index in production", "change…
- **floating-point**: This skill should be used when the user asks "why is 0.1 + 0.2 not 0.3", "how do I compare floats", "what type should I use for money", "why is my total off by a cent", "why do …
- **hyrums-law**: This skill should be used when the user asks "is this a breaking change", "can I change this undocumented behavior", "why did an internal change break a consumer", "how do I sto…
- **index-design**: This skill should be used when the user asks "why is my index not being used", "which columns should I index", "what order should the composite index columns be in", "should thi…
- **isolation-anomalies**: This skill should be used when the user asks "which isolation level do I need", "why did concurrent requests break this invariant", "should I use SELECT FOR UPDATE", "what is wr…
- **keyset-pagination**: This skill should be used when the user asks "why is deep pagination slow", "how do I replace OFFSET", "how do I build a cursor-based API", "why do users see duplicate or skippe…
- **metamorphic-testing**: This skill should be used when the user asks "how do I test this when I do not know the expected output", "how do I test a search ranking or ML model", "what is the oracle probl…
- **module-depth**: This skill should be used when the user asks "should I split this class", "is this abstraction worth it", "why does this change ripple through so many layers", "is this wrapper …
- **mutation-testing**: This skill should be used when the user asks "are our tests actually good", "is 100% coverage meaningful", "what is mutation testing", "how do I measure test quality", "which te…
- **mvcc-and-bloat**: This skill should be used when the user asks "why is the table growing despite deletes", "why did queries get slower over time", "why is autovacuum not keeping up", "what is tra…
- **parse-dont-validate**: This skill should be used when the user asks "where should validation live", "how do I stop re-checking this everywhere", "how do I make illegal states unrepresentable", or when…
- **query-plans**: This skill should be used when the user asks "why is this query slow", "read this EXPLAIN output", "why is the planner not using my index", "why is it fast in staging but slow i…
- **queueing-and-utilization**: This skill should be used when the user asks "how big should this thread pool be", "what CPU target is safe", "why did latency spike without more traffic", "do we have headroom …
- **retry-amplification**: This skill should be used when the user asks "how should I configure retries", "why is the service still down after we fixed the cause", "where should retries live in the call c…
- **start-here**: This skill should be used when the user asks a broad engineering question that could match several areas, asks "which skill covers this", "what skills are available", "where do …
- **tail-latency**: This skill should be used when the user asks "why is p99 bad when p50 is fine", "how do I reduce tail latency", "should I use hedged requests", "how do I set timeouts for a fan-…
- **unicode-pitfalls**: This skill should be used when the user asks "why is this string length wrong", "how do I truncate text safely", "why do these identical strings not match", "how do I compare te…
- **universal-scalability-law**: This skill should be used when the user asks "why does adding servers not help", "why did throughput drop when we scaled out", "how far can this scale", "why is a bigger thread …
- **write-amplification**: This skill should be used when the user asks "should I use an LSM or a B-tree", "why is disk usage far bigger than my data", "why do writes slow down as data grows", "how do I t…

### cogmemai [off] (2 skills)

- **cogmemai-guard-review**: Guard before, review after.
- **cogmemai-memory**: Persistent memory management for Ai coding assistants using CogmemAi.

### colosseum [off] (1 skills)

- **colosseum**: Runs a web-search-grounded adversarial review of a contested question.

### compounded [off] (5 skills)

- **compounded-author**: Use this skill when you have just completed a non-trivial task (more than 3 tool calls, novel approach, recovery from a dead end) and are considering whether to save the procedu…
- **compounded-trust-tracker**: Use this skill when working with skills already at .verified, .trusted, or .autonomous trust levels — particularly when deciding whether to invoke a verified skill on a task, wh…
- **compounded-typo-fixer**: Use this skill when the user reports a typo in their codebase or documentation and asks for it to be fixed across the project, or when reviewing code and noticing a misspelled i…
- **compounded-verifier**: Use this skill ONLY when invoked as the skill-verifier subagent by compounded's Stop hook.
- **using-compounded**: Use this skill at the start of any session where compounded is installed, or whenever the user mentions earning trust, verifying skills, the trust ladder, compounded, the trust …

### consistent-ui [off] (1 skills)

- **consistent-ui**: Enforce UI consistency across an entire codebase, regardless of language, framework, or styling approach.

### context-compactor [off] (1 skills)

- **context-compactor**: Use when a long Claude Code session slows down or nears the context limit, or before a large task, to keep only the context that is still needed.

### context-handoff [off] (3 skills)

- **handoff-resume**: Restore previous session context from handoff file.
- **handoff-save**: Save current session context to handoff file.
- **handoff-search**: Search past session handoffs by topic or keyword.

### context-handoff [off] (1 skills)

- **handoff-writing**: Use when generating a session handoff summary (triggered by the /context-handoff:handoff command or the SessionEnd hook) to bring Claude Code project context into a separate Cla…

### cortex [off] (10 skills)

- **brief**: Quick daily status overview (~20 lines) — focus, priorities, blockers, key numbers.
- **close**: Session close ritual.
- **daily-wrap**: End-of-day consolidation.
- **memory**: How this workspace keeps long-term memory.
- **plan**: Break a task into phases with verification criteria before building.
- **review**: Code review checklist — security, simplicity, edge cases.
- **setup**: First-time guided workspace setup.
- **soul**: Core identity, working style, and hard limits for this workspace's agent.
- **start**: Session start ritual.
- **weekly**: Weekly retrospective from closing reports — what shipped, decisions, patterns, next-week priorities.

### council [off] (2 skills)

- **council**: Runs a question, idea, or decision through a configurable council of AI advisors who analyze it independently, peer-review each other anonymously, and have a chairman synthesize…
- **council-setup**: Configures the council used by the council skill — lists and activates presets, shows the active council, customizes a preset, or builds a new council from scratch.

### cowork-mem [off] (7 skills)

- **cowork-mem**: Persistent memory across Cowork sessions.
- **do**: Execute a task using memory for context — the memory-aware task runner.
- **knowledge-agent**: Answer questions using accumulated project memory as a knowledge base.
- **make-plan**: Create a work plan using memory context from past sessions.
- **mem-search**: Search persistent memory using keyword or semantic (TF-IDF) search.
- **smart-explore**: Explore a project or codebase using memory as a guide.
- **timeline-report**: Generate a chronological report of what happened across sessions.

### cowork-plugin-management [off] (2 skills)

- **cowork-plugin-customizer**: Customize a Claude Code plugin for a specific organization's tools and workflows.
- **create-cowork-plugin**: Guide users through creating a new plugin from scratch in a cowork session.

### create-smartfolder [off] (1 skills)

- **create-smartfolder**: Turn a folder hierarchy into a SmartFolder — a tiered navigation-and-knowledge layer over the real files, so people and future Claude sessions can operate in it with full contex…

### crewmarshal [off] (12 skills)

- **adversarial-review-to-go**: Use when a spec, a plan, or an implemented diff needs an external adversarial reviewer — locks the reviewer to the altitude of what is being reviewed, converges diff findings to…
- **checkpoint-verification**: Use when accepting an executor's task or about to claim work done — refuses green tests as proof and requires inspecting the call-site and driving the real runtime path to catch…
- **concept-briefing**: Use as the first step on any new request, before design begins — locks a user-confirmed system profile (scale today and expected, users, trade-off priorities) and tiers the requ…
- **convention-commit-gate**: Use at every checkpoint review before committing — enforces centralized enums, no magic string/number literals, constant-based collection/model names, and the project's commit-m…
- **executor-context**: Use when dispatching work to executors or subagents and the same project conventions keep getting retyped into every prompt — maintains one fixed context file the coordinator wr…
- **lessons-ledger**: Use before starting work in an area to retrieve only the lessons that apply to it, and right after a wrong diagnosis, a defect the tests missed, or an environment trap to record…
- **multi-lane-coordination**: Use when the working agreement sets coordination mode to multi-lane, or when design finds two or more services or large independent areas that could each carry their own coordin…
- **orchestrating-executors**: Use when a plan is ready and implementation will be delegated to external coding agents or subagents — covers knowing your workforce and what each has proven, choosing between a…
- **planning-for-delegation**: Use after a plan is drafted and before any task is handed to an executor — settles how detailed this project's plans are (asking once and recording it in the working agreement),…
- **pointer-handoff**: Use at the start of any session on an ongoing project to recover where the work stands, and at the end of a session (or on any significant discovery) to record it — maintains a …
- **project-working-agreement**: Use before executing or dispatching work on a project, and whenever the user changes how the work should run — keeps one project file of working rules (stop after each task or c…
- **using-crewmarshal**: Use when starting delegated multi-agent delivery on a project — maps the full workflow arc and points to the right crewmarshal skill and superpowers skill at each stage.

### critique [off] (4 skills)

- **badge**: Install, remove, or check the [CRITIQUE] statusline badge.
- **critique**: Permanent critical mindset — balanced co-pilot for the session.
- **rigorous**: Deep analysis mode — critical thinking before and during coding, reviewing, or planning.
- **scan**: One-shot critical scan — surfaces only critical blockers in what was just shown.

### cut-weight [off] (1 skills)

- **cut-weight**: Sanitize repositories and project folders by removing development residue: superseded plans, completed audits, duplicate docs, plugin output, scratch files, and disposable artif…

### data [off] (10 skills)

- **analyze**: Answer data questions -- from quick lookups to full analyses.
- **build-dashboard**: Build an interactive HTML dashboard with charts, filters, and tables.
- **create-viz**: Create publication-quality visualizations with Python.
- **data-context-extractor**: Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts.\nBOOTSTRAP MODE - Triggers: \"Create a data context skill\", \"Set up da…
- **data-visualization**: Create effective data visualizations with Python (matplotlib, seaborn, plotly).
- **explore-data**: Profile and explore a dataset to understand its shape, quality, and patterns.
- **sql-queries**: Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.).
- **statistical-analysis**: Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing.
- **validate-data**: QA an analysis before sharing -- methodology, accuracy, and bias checks.
- **write-query**: Write optimized SQL for your dialect with best practices.

### design [off] (7 skills)

- **accessibility-review**: Run a WCAG 2.1 AA accessibility audit on a design or page.
- **design-critique**: Get structured design feedback on usability, hierarchy, and consistency.
- **design-handoff**: Generate developer handoff specs from a design.
- **design-system**: Audit, document, or extend your design system.
- **research-synthesis**: Synthesize user research into themes, insights, and recommendations.
- **user-research**: Plan, conduct, and synthesize user research.
- **ux-copy**: Write or review UX copy — microcopy, error messages, empty states, CTAs.

### design-dev-bridge [off] (4 skills)

- **code-to-figma**: Turn existing code — a component, page, or screen — into a Figma design, or sync code changes back into Figma.
- **figma-to-code**: Implement a Figma design as front-end code — design-to-code (the reverse of code-to-figma).
- **handoff-to-code**: Implement a Claude Design HANDOFF BUNDLE (README + component code + CSS + prototype + assets) into an existing codebase — reconciling the handoff's self-contained implementation…
- **write-design-system-doc**: Extract a project's design system from its implementation into a single normative DESIGN.md — the on-brand reference for AI-generated UI — and audit whether the implementation c…

### design-skills [off] (10 skills)

- **accessibility-audit**: Conduct accessibility audits against WCAG 2.2 guidelines.
- **design-critique**: Evaluate UI designs against usability heuristics, UX laws, interaction patterns, interaction design principles, information architecture, and content quality.
- **design-elevation**: Comprehensive design elevation system that automatically transforms functional visual outputs into polished, professional designs.
- **design-ops**: Run design sprints, manage handoff, establish team rituals, documentation standards, and design QA processes.
- **design-systems**: Build, document, and maintain design systems with design tokens, component specifications, pattern libraries, naming conventions, and governance processes.
- **interaction-design**: Design meaningful interactions, microinteractions, animations, state machines, gesture patterns, error prevention, and product behavior.
- **journey-mapping**: Create customer journey maps, service blueprints, experience maps, empathy maps, and other alignment diagrams.
- **ux-research**: Plan, conduct, and analyze UX research using proven methodologies.
- **ux-strategy**: Connect design decisions to business outcomes through competitive analysis, opportunity mapping, Jobs to Be Done, outcome-driven discovery, value proposition design, and UX metr…
- **ux-writing**: Create user-centered, accessible interface copy (microcopy) for digital products including buttons, labels, error messages, notifications, forms, onboarding, empty states, succe…

### design-superpowers [off] (9 skills)

- **creative**: Use when exploring visual direction, generating moodboards, proposing color palettes, typography systems, layout strategies, imagery/art direction, refreshing an existing design…
- **design**: Use when designing product features, flows, pages, or screens using an existing design system or design language.
- **design-review**: Use to evaluate existing designs against UX heuristics, accessibility standards, DS compliance, visual quality, or motion principles.
- **ds-consumer**: Use when designing product features using an enterprise DS, evaluating existing UI, selecting DS components, reviewing information architecture, or requesting new components.
- **ds-make**: Use when creating, updating, versioning, or deprecating design system tokens, components, or patterns.
- **ds-manage**: Use for DS operations — publishing cascades, adoption analytics, documentation generation, health and drift monitoring.
- **ds-producer**: Use when creating, updating, auditing, documenting, versioning, or publishing DS components, foundations, icons, or patterns.
- **figma-setup**: Install or verify PluginOS for Figma work in design-superpowers.
- **map-design**: Use to extract design language from an existing artifact (screenshot, URL, Figma file, or codebase) and generate a DESIGN.md.

### desktop-commander [off] (6 skills)

- **ai-tools-setup**: Set up, connect, validate, and repair Claude Desktop and MCP servers using Desktop Commander — inspecting and fixing mcp.json / claude_desktop_config.json, getting MCP servers t…
- **computer-health-check**: Run a comprehensive, read-only health check on the user''s computer and return a scored chat summary with prioritized, plain-English recommendations and safe cleanup suggestions.
- **desktop-commander-overview**: Use for Desktop Commander MCP capabilities — persistent shells and REPLs, long-running processes, filesystem beyond the workspace, structured files (.xlsx, .docx, .pdf, images) …
- **knowledge-base**: Create and maintain a Markdown knowledge base that any AI agent can read, search, and update.
- **obsidian-vault**: Organize Obsidian vaults with MOCs, wikilinks, frontmatter/properties, dashboards, orphan-note checks, and cleanup workflows.
- **terminal**: Use Desktop Commander for terminal and command-line work, especially anything that needs a shell whose state persists across turns: Python/Node REPLs, database shells, dev serve…

### dev-mentor [off] (3 skills)

- **mentor**: Always-on teaching companion.
- **pr-guardian**: Standalone PR/MR checklist enforcer.
- **wdyt**: Command — not a mode.

### devil-advocate [off] (1 skills)

- **devil-advocate**: Use when about to commit to a decision, plan, conclusion, or recommendation and it needs to be attacked before anyone acts on it — especially when everyone already agrees, money…

### docbrain [off] (1 skills)

- **docbrain-capture**: Capture what this conversation worked out into DocBrain, so the whole organization can find it later and DocBrain can tell when it stops being true.

### docker-skills [off] (11 skills)

- **docker-agent-config**: Use this skill when creating or editing an agent.yaml (or .yml/.hcl) configuration file for Docker Agent (cagent), including defining agents, models/providers, built-in or MCP t…
- **docker-agent-deploy**: Use this skill when exposing a Docker Agent as a server (MCP, HTTP API, A2A, ACP, or OpenAI-compatible chat), distributing an agent via an OCI registry with `docker agent share`…
- **docker-agent-run**: Use this skill when running a Docker Agent with `docker agent run`, choosing a safety/approval mode, using the `--sandbox` isolation flag, setting up aliases, or troubleshooting…
- **docker-build-strategies**: Use this skill when writing, reviewing, or optimizing Dockerfiles, even if the user just says their image is too large, their build is slow, or they need to harden a container f…
- **docker-compose-patterns**: Use this skill when creating, modifying, or debugging Docker Compose configurations, even if the user just says they need to wire services together, add a database to their stac…
- **docker-destructive-guardrails**: Use this skill before running, or recommending, any Docker command that deletes, wipes, resets, or otherwise irreversibly changes state — even if the user just says to "clean up…
- **docker-project-foundations**: Use this skill when setting up, initializing, or Dockerizing a project, even if the user doesn't explicitly mention Docker but describes a need for containerized local developme…
- **docker-sandboxes-env**: Use this skill when authoring, planning, or running a declarative `sbxenv.yaml` file for Docker Sandboxes (`sbx env create/run/plan/exec/rm`), even if the user just says they wa…
- **docker-sandboxes-kits**: Use this skill when authoring, validating, packaging, signing, or composing a Docker Sandboxes kit `spec.yaml` (`sbx kit add/inspect/pack/pull/push/sign/validate/verify`), even …
- **docker-sandboxes-lifecycle**: Use this skill when creating, running, reattaching to, listing, stopping, or removing Docker Sandboxes (the standalone `sbx` CLI that runs AI coding agents in isolated microVMs)…
- **docker-sandboxes-network-credentials**: Use this skill when configuring what a Docker Sandboxes (`sbx`) sandbox can reach on the network or which credentials it authenticates with, even if the user just says they want…

### drunken-master [off] (1 skills)

- **drunken-master**: Recover what the user actually meant when their message arrived garbled from any input path — speech-to-text, T9/autocorrect, swipe typing, hurried typing, OCR, copy-paste.

### education-agent-skills [off] (165 skills)

- **academic-language-sentence-frame-generator**: Generate tiered sentence frames for academic tasks that scaffold language production across proficiency levels.
- **adaptive-hint-sequence-designer**: Generate a cascading hint sequence for a problem type, revealing progressively without giving answers.
- **agency-circles-for-systems-action**: Map control, influence, and concern after systems analysis.
- **agency-scaffold-generator**: Generate scaffolds that gradually increase student choice, voice, and ownership within a learning task.
- **ai-claim-checker**: After any AI-generated explanation, require the learner to identify one place it could be wrong, one thing to check, and one source to consult.
- **ai-expertise-interrogation-designer**: Design a Funhouse Mirror activity where students use their own domain expertise to detect AI distortions, omissions, and overconfidence.
- **ai-facilitated-collaborative-learning-designer**: Design AI-supported collaborative tasks that structure group interaction and address participation problems.
- **ai-feedback-design-principles**: Audit and redesign AI-generated feedback for pedagogical quality, timing, and learning impact.
- **ai-hallucination-fact-check-protocol**: Design a fact-checking protocol for AI-generated text, extending SIFT with AI-specific adaptations for hallucination detection.
- **ai-learning-boundary-mapper**: Map which elements of an assignment benefit from AI assistance vs.
- **ai-output-critical-audit-designer**: Design a structured protocol for auditing AI-generated text against Ennis's six CT standards.
- **ai-socratic-dialogue-designer**: Design a multi-round questioning sequence for interrogating AI chatbot answers, tracking how responses shift and distinguishing genuine updates from sycophantic capitulation.
- **argument-structure-scaffold-generator**: Generate argument structure scaffolds using Toulmin, PEEL, or CER frameworks for a specific claim or question.
- **aspirational-systems-iceberg**: Design the deeper patterns, structures, artefacts, and mental models needed to grow a desired event.
- **assessment-design-orchestrator**: Routes between five assessment pathways — formative, rubric/criteria, authentic/performance, peer/self, and diagnostic — with validity and equity checks.
- **assessment-validity-checker**: Audit a proposed assessment for construct validity, reliability, and alignment to learning objectives.
- **awe-wonder-experience-designer**: Design a moment of awe or wonder that hooks curiosity and deepens emotional engagement with content.
- **backwards-design-unit-planner**: Plan a unit using backwards design from desired outcomes through assessment evidence to learning activities.
- **belonging-classroom-culture-designer**: Design targeted interventions that strengthen belonging and inclusion for specific classroom dynamics.
- **biophilic-learning-environment-designer**: Redesign a learning space using biophilic design principles to improve focus, calm, and wellbeing.
- **central-historical-question-evaluator**: Evaluate a teacher-drafted central historical question for its capacity to drive genuine historical inquiry.
- **checking-for-understanding-protocol-designer**: Design a checking-for-understanding protocol with specific techniques for each lesson stage.
- **close-reading-skill-builder**: Build students' capacity to read historical documents closely — attending to word choice, tone, and rhetoric as evidence of perspective.
- **cognitive-load-analyser**: Analyse a learning task for cognitive load problems and recommend specific design improvements.
- **cognitive-tutoring-architecture-designer**: Map knowledge components and skill hierarchies for a cognitive tutoring system or adaptive learning platform.
- **coherent-rubric-logic-builder**: Build a five-level rubric with coherent logic for a learning target within a developmental band.
- **compassionate-systems-awareness-orchestrator**: Orchestrate compassionate systems tools from issue or aspiration to wise action.
- **competency-framework-translator**: Translate an external competency framework like DigComp, GreenComp, or ISTE into classroom-ready activities.
- **competency-unpacker**: Unpack a broad standard or competency descriptor into specific, assessable success criteria and sub-skills.
- **confidence-calibration-check**: Capture confidence ratings before and after a learning attempt to identify overconfidence and underconfidence patterns.
- **contextualisation-skill-builder**: Build students' capacity to place historical documents in their temporal and social context.
- **corroboration-skill-builder**: Build students' capacity to compare accounts across multiple historical sources — identifying agreements, contradictions, and gaps.
- **coverage-audit**: Takes a curriculum framework and a statutory or accreditation requirement list; produces a coverage table, gap summary, and CSV showing which framework content covers each requi…
- **cpa-sequence-designer**: Design a Concrete-Pictorial-Abstract learning sequence for a mathematical concept using manipulatives.
- **criterion-referenced-rubric-generator**: Generate a criterion-referenced rubric with descriptive performance levels for a task or objective.
- **critical-thinking-task-designer**: Design a critical thinking task targeting specific skills like evaluating evidence, identifying bias, or analysing arguments.
- **cross-cultural-task-validity-checker**: Check an educational practice or task for cultural bias, WEIRD assumptions, and cross-cultural validity.
- **culturally-responsive-teaching-designer**: Redesign a lesson to centre students' cultural backgrounds, community knowledge, and lived experience.
- **curriculum-crosswalk**: (no description)
- **curriculum-knowledge-architecture-designer**: Map the epistemic structure of a subject to determine knowledge types and inform curriculum sequencing.
- **developmental-band-system-designer**: Design a developmental band system mapping student growth from early childhood through upper secondary.
- **developmental-band-translator**: Tags harness-decomposed curriculum items (KUDs, LTs, criteria) with a school's developmental band metadata while preserving source voice and labels.
- **developmental-progression-synthesis**: Synthesise completed KUD charts into a developmental progression matrix and per-competency narrative sections.
- **dialogic-teaching-move-generator**: Generate follow-up teaching moves that extend student thinking after a specific classroom response.
- **differentiation-adapter**: Adapt a classroom task for specific learner needs while preserving the core learning objective intact.
- **digital-worked-example-sequence**: Create an interactive digital worked example sequence with fading for online or blended delivery.
- **dilemma-navigation-for-education-design**: Identify and navigate genuine dilemmas in curriculum, school, or community contexts — tensions between competing goods that cannot be solved, only navigated.
- **disciplinary-ai-literacy-sequence-designer**: Design a sequence where students compare AI's handling of the same question across disciplines, developing a mental model of where AI is reliable vs.
- **disciplinary-writing-scaffold**: Create a writing scaffold teaching the genre conventions specific to an academic discipline.
- **discipline-specific-critical-thinking-task-designer**: Design discipline-specific critical thinking tasks grounded in knowledge-contingent reasoning rather than generic skills.
- **discussion-protocol-selector**: Select and configure a structured discussion protocol matched to the purpose, topic, and group readiness.
- **dispositional-knowledge-assessment-designer**: Design multi-informant assessment approaches for dispositional competencies like curiosity or resilience.
- **document-based-lesson-designer**: Design a complete document-based history lesson using the Reading Like a Historian four-part structure.
- **dual-coding-designer**: Design a visual complement to verbal content using dual coding principles for stronger encoding.
- **ecological-inquiry-anchor-designer**: Design an inquiry sequence anchored in a local ecosystem that embeds science or geography curriculum content.
- **elaborative-interrogation-generator**: Generate elaborative interrogation prompts that deepen encoding through targeted why and how questions.
- **emergent-project-design-scaffold**: Scaffold an emergent project from observed children's interests using Reggio-inspired approaches.
- **erroneous-example-designer**: Design deliberately flawed examples that develop error-detection skills and deepen understanding.
- **error-analysis-protocol**: Design an error analysis protocol to diagnose the root cause of student mistakes and misconceptions.
- **experiential-learning-cycle-designer**: Structure a direct experience into a full learning cycle with concrete experience, reflection, and conceptual transfer.
- **explain-first-interrogator**: Require the learner to explain a concept in their own words before the AI evaluates or extends it.
- **explicit-instruction-sequence-builder**: Build a complete explicit instruction sequence from teacher modelling through guided practice to independent work.
- **fading-manager**: Track performance across sessions and reduce scaffolding as competence grows.
- **feedback-quality-analyser**: Analyse existing written feedback for quality, specificity, actionability, and impact on student learning.
- **flow-state-condition-designer**: Optimise a learning activity for flow by balancing challenge level, skill, clear goals, and immediate feedback.
- **formative-assessment-loop-designer**: Design an adaptive assessment loop where each student response triggers the next instructional move.
- **formative-assessment-technique-selector**: Select the right formative assessment technique for a specific learning moment, purpose, and age group.
- **gap-analysis-from-student-work**: Analyse student work against criteria to identify specific gaps between current performance and learning objectives.
- **goal-setting-protocol-designer**: Design a structured goal-setting protocol using SMART or implementation-intention frameworks for students.
- **hexagon-complexity-mapper**: Map a complex topic by placing factors on hexagonal tiles where adjacency signals a claimed relationship.
- **hinge-question-designer**: Design a diagnostic hinge question that reveals whether students understand enough to move on.
- **historical-document-set-curator**: Design a document set for a document-based lesson — selecting and sequencing sources for analytical tension around a central question.
- **historical-source-adapter**: Adapt a historical primary source for classroom use — modifying complexity and length while preserving features for sourcing, close reading, and corroboration.
- **historical-thinking-assessment-designer**: Design formative assessments that make students' historical thinking visible — revealing whether they source, close-read, contextualise, and corroborate.
- **historical-thinking-strategy-modelling-guide**: Design a teacher think-aloud that models historical thinking strategies with a specific document.
- **implementation-intention-designer**: Create if-then implementation intentions and WOOP plans for specific student behaviour change goals.
- **inclusive-design-orchestrator**: Coordinates UDL and differentiation tools through a universal-first hierarchy: barrier removal before targeted differentiation before individualised accommodation.
- **individual-spacing-algorithm-explainer**: Explain and configure individual spacing algorithms using student performance data and forgetting curves.
- **instructional-coaching-conversation-guide**: Generate a coaching conversation guide with questions, protocols, and follow-up actions for a teaching focus.
- **intelligent-tutoring-dialogue-designer**: Script a multi-turn tutoring dialogue with branching responses for anticipated student difficulties.
- **interdisciplinary-real-world-connection-mapper**: Map curriculum connections across multiple subjects for a real-world problem or authentic context.
- **interleaving-unit-planner**: Redesign a blocked topic sequence into an interleaved plan with mixed practice across related topics.
- **kud-chart-author**: (no description)
- **kud-knowledge-type-mapper**: Classify curriculum content into Know, Understand, and Do categories to align teaching and assessment approaches.
- **ladder-of-inference-reflection**: Slow down interpretation from observation to action.
- **language-demand-analyser**: Analyse the language demands of a classroom task to identify barriers for EAL and multilingual learners.
- **learning-analytics-interpretation-guide**: Interpret learning analytics data and translate dashboard findings into actionable teaching decisions.
- **learning-progression-builder**: Build a learning progression showing prerequisite-to-mastery steps for a target skill or understanding.
- **learning-target-authoring-guide**: Author learning targets for a competency across developmental bands with precise, observable progression language.
- **lesson-observation-protocol-designer**: Design a focused lesson observation protocol with specific look-fors and evidence collection methods.
- **lesson-opening-designer**: Design a lesson opening that activates prior knowledge and connects previous learning to today's content.
- **lesson-study-cycle-designer**: Design a complete lesson study cycle from research question through collaborative planning to research lesson.
- **leverage-and-response-design**: Design a wise systems intervention from an existing analysis.
- **media-literacy-deconstruction-protocol**: Design a media deconstruction protocol analysing persuasion, bias, or representation in media texts.
- **mental-model-mapper**: Surface beliefs, assumptions, stories, and values shaping a system.
- **metacognitive-monitoring-ai-contexts**: Design metacognitive checkpoints that prevent AI-assisted learning from bypassing genuine understanding.
- **metacognitive-prompt-library**: Build a library of metacognitive prompts targeting planning, monitoring, or evaluation for a specific task.
- **mixed-age-learning-task-designer**: Design a learning task where mixed-age students work together with mutual benefit for all age groups.
- **motivation-diagnostic-task-redesign**: Diagnose motivation problems in a task using self-determination theory and redesign for autonomy, competence, and relatedness.
- **multi-perspective-decision-wheel**: Structure a decision or design challenge through multiple perspectives before committing to action.
- **outdoor-learning-sequence-designer**: Design a structured outdoor learning sequence embedding curriculum objectives in an available outdoor space.
- **panel-review**: Seven-role depersonalised panel review of framework artefacts (KUD, criterion bank, LT definition, crosswalk, scope-and-sequence) in sequential-isolation mode.
- **pedagogical-content-knowledge-developer**: Develop pedagogical content knowledge for a topic by surfacing common misconceptions and effective representations.
- **perma-based-lesson-designer**: Design a lesson that embeds PERMA wellbeing elements alongside academic learning objectives.
- **perspective-taking-designer**: Design structured perspective-taking activities with anti-projection guardrails.
- **phenomenon-based-unit-anchor**: Anchor a multidisciplinary unit in a real-world phenomenon that requires multiple subject lenses to understand.
- **place-based-curriculum-orchestrator**: Present pathway options and orchestrate place-based curriculum design from a local place, curriculum requirement, or community issue.
- **place-based-inquiry-anchor**: Anchor curriculum learning in a specific local place with connections to community, culture, and identity.
- **practice-problem-sequence-designer**: Generate a scaffolded sequence of practice problems with graduated difficulty and strategic variability.
- **prepared-environment-designer**: Redesign a classroom as a prepared environment optimised for independent learning, calm transitions, and material access.
- **productive-failure-desirable-difficulty-designer**: Redesign a direct instruction sequence to include productive struggle before the explanation phase.
- **productive-failure-protocol**: Stage exploration before instruction on complex problems.
- **professional-development-session-designer**: Design a professional development session using adult learning principles with active teacher engagement.
- **progressive-hint-ladder**: Provide graduated assistance from abstract conceptual nudge to concrete procedural step, with reflection required before each escalation.
- **project-brief-designer**: Design a project-based learning brief with a driving question, milestones, and assessment criteria.
- **prompt-literacy-sequence-designer**: Design a learning sequence teaching prompt quality — comparing vague vs.
- **reading-comprehension-strategy-selector**: Select and sequence reading comprehension strategies matched to a specific text's challenges and demands.
- **reflective-practice-prompt-generator**: Generate structured reflection prompts for a specific teaching experience or professional learning challenge.
- **regenerative-project-design-orchestrator**: Present project-design pathway options and orchestrate regenerative projects using backwards design, PBL, SEEDS, compassionate systems action, or civic/service pathways.
- **reggio-documentation-protocol**: Design a pedagogical documentation protocol for making children's learning processes visible and shareable.
- **restorative-practice-protocol-designer**: Design a restorative practice protocol for addressing harm, rebuilding trust, and restoring relationships.
- **retrieval-practice-generator**: Generate retrieval practice questions at varied difficulty levels for a topic or concept.
- **retrieve-first-gate**: Before any explanation or answer, require the learner to produce a free-recall attempt and confidence rating.
- **ruler-emotional-literacy-sequence**: Design a RULER emotional literacy sequence for recognising, understanding, labelling, expressing, and regulating emotions.
- **scaffolded-task-modifier**: Modify a classroom task with language scaffolds that preserve cognitive demand for EAL learners.
- **scope-and-sequence-designer**: (no description)
- **scoping-for-transformative-learning-inquiry**: Define the scope and purpose of a complex inquiry before mapping or futures work begins.
- **seeds-regenerative-inquiry-cycle**: Design a SEEDS regenerative inquiry cycle connecting place-based learning to ecological awareness for young learners.
- **self-determined-project-design-protocol**: Structure a student's self-determined project with mentoring checkpoints, competency alignment, and reflection.
- **self-efficacy-builder-sequence**: Design a mastery experience sequence that systematically builds student confidence in a skill they avoid.
- **self-explanation-prompt-designer**: Create self-explanation prompts that deepen understanding of worked examples, texts, or diagrams.
- **self-regulation-scaffold-generator**: Generate scaffolds supporting student self-regulation across planning, monitoring, and evaluation phases.
- **service-learning-project-designer**: Design a service-learning project connecting genuine community need with embedded curriculum learning.
- **sheltered-instruction-lesson-modifier**: Modify a lesson plan using SIOP sheltered instruction principles to support language learners across all four skills.
- **single-point-rubric-designer**: Design a single-point rubric with one criterion and open columns for evidence.
- **socratic-questioning-sequence-generator**: Generate a Socratic questioning sequence that develops conceptual understanding through guided inquiry.
- **source-credibility-evaluation-protocol**: Design a source evaluation protocol using lateral reading and credibility checks for digital information.
- **sourcing-skill-builder**: Build students' capacity to interrogate a historical source before reading — asking who authored it, when, why, and what this means for reliability.
- **spaced-practice-scheduler**: Design a spaced retrieval schedule for any topic list and timeline.
- **srl-session-wrapper**: Wrap a learning session in a plan → monitor → reflect cycle.
- **stuck-and-error-diagnosis-coach**: When a learner gets something wrong or feels stuck, require them to diagnose the problem before receiving help.
- **study-strategy-selector**: Select evidence-based study strategies matched to material type, learning goal, and student habits.
- **systems-awareness-iceberg**: Map a current event below the surface into patterns, structures, and mental models.
- **systems-wellbeing-impact-mapper**: Map systemic forces shaping a wellbeing concern without individualising the problem.
- **teach-back-evaluator**: The learner teaches the concept to the AI, which plays a curious novice peer and identifies gaps through authentic questions.
- **teacher-inquiry-cycle-designer**: Design a practitioner inquiry cycle from research question through data collection to evidence-informed action.
- **technological-pedagogical-content-knowledge-developer**: Develop TPACK for integrating a specific technology or AI tool into subject teaching with pedagogical alignment.
- **text-complexity-analyser**: Analyse text complexity across quantitative, qualitative, and reader-task dimensions with scaffolding recommendations.
- **think-aloud-script-generator**: Script a teacher think-aloud demonstrating expert reasoning processes for a specific task.
- **three-horizons-learning-transition-mapper**: Map a scoped topic across three coexisting horizons — current system under strain (H1), preferred future (H3), and transition innovations sorted as H2+ or H2- — to understand ch…
- **three-part-lesson-designer**: Design a Montessori three-period lesson for introducing concepts through concrete materials and naming.
- **transfer-bridge**: After the learner demonstrates understanding of a concept, present near-transfer and far-transfer challenges.
- **trauma-informed-practice-designer**: Design trauma-informed classroom practices that prioritise safety, predictability, connection, and regulation.
- **ubuntu-collective-knowledge-task-designer**: Design learning tasks built on Ubuntu philosophy emphasising collective knowledge-building and mutual responsibility.
- **udl-barrier-anticipator**: Predicts access barriers in a learning task before delivery, given a learner variability profile.
- **udl-lesson-auditor**: Audits an existing lesson against UDL's three principles — engagement, representation, and action/expression.
- **udl-options-designer**: Generates multiple means of engagement, representation, and action/expression for a given learning goal.
- **unassisted-evidence-checkpoint**: After scaffolded practice, run an unassisted check with no AI help.
- **uninterrupted-work-cycle-designer**: Design an uninterrupted work cycle with choice-based activities structured within a realistic time block.
- **variation-theory-task-designer**: Design a variation theory task using contrast, separation, and fusion to teach critical features of a concept.
- **vocabulary-tiering-tool**: Tier vocabulary from a text or topic into everyday, academic, and technical categories with teaching priorities.
- **weekly-agency-review**: Review the week using accumulated session evidence — retrieval rates, hint depths, calibration accuracy, transfer and unassisted results.
- **wellbeing-learning-connection-mapper**: Map evidence-based connections between a wellbeing initiative and specific academic learning outcomes.
- **worked-example-fading-designer**: Design a worked example fading sequence from fully worked examples through to independent practice.
- **worked-example-to-problem-solving-transition-designer**: Design the transition from worked examples to independent problem-solving using expertise-reversal principles.

### emem [off] (19 skills)

- **emem-device-traces**: Inspects and verifies the execution evidence emem holds for devices such as robots, drones, satellites and sensor hosts.
- **emem-document-evidence**: Turns a scanned document into signed, checkable evidence with emem.
- **emem-eudr-due-diligence**: Produces a signed, Annex II shaped Due Diligence Statement under the EU Deforestation Regulation (EU 2023/1115) for one or more production plots with emem, and explains what it …
- **emem-field-signals**: Answers agronomy questions about one farm field with signed evidence from emem.
- **emem-field-tokens**: Fetches a native-resolution raster field over an area from emem, or the same field over several dates, as a signed and re-derivable artifact rather than a set of per-cell scalars.
- **emem-find-similar**: Returns the top-K places most similar to a seed place by cosine over a stored 128-D surface-texture embedding (Sentinel-1 plus Sentinel-2, annual).
- **emem-locate-and-recall**: Resolves a place name to an emem cell64 address and recalls signed Earth-observation facts there (weather, vegetation indices, elevation, soil, land cover, surface water, forest…
- **emem-long-horizon-memory**: Keeps an agent's working state in signed emem notes that outlive its context window, so a later session, or the same agent after a reset, picks up from bytes it can verify rathe…
- **emem-multi-agent-handoff**: Hands work between agents so it arrives as checkable evidence rather than prose someone has to trust, and checks what other agents hand back.
- **emem-recall-polygon**: Recalls signed Earth-observation facts at sampled cells inside an area (a named region, a bounding box, or a GeoJSON boundary) in one call.
- **emem-referential-drift**: Stops two agents, or one agent across two sessions, from reporting different numbers for the same reading.
- **emem-research-grade-citation**: Prepares emem facts for use in research, where a reviewer needs to know exactly what a number is, how it was read, and how to reproduce it.
- **emem-shared-identity**: Makes two agents refer to the same object.
- **emem-sign-and-attest**: Writes to emem with the agent's own Ed25519 key, either a signed note in its namespace that other agents can verify it wrote, or a derivation over signed facts that the responde…
- **emem-tokenise-files**: Turns a file into signed, resolvable tokens with emem.
- **emem-transparency-log**: Audits emem's append-only RFC 6962 transparency log offline.
- **emem-urban**: Answers urban-analysis questions with signed emem facts and says what each number measures.
- **emem-verify-before-publish**: Checks a draft before it is sent.
- **emem-verify-receipt**: Verifies an emem receipt's Ed25519 signature offline by rebuilding its canonical BLAKE3 preimage (v1 or v2) and checking it against the responder's published key.

### env-setup-wizard [off] (1 skills)

- **env-setup-wizard**: Use when a project will not start, a new developer is onboarding, or a setup script or README setup section is needed, to find what is missing and write a verified setup.

### firecrawl [off] (12 skills)

- **firecrawl**: Any live-web task via the Firecrawl CLI — including ordinary web research: searching the web, reading or extracting pages, gathering sources, discovering site URLs, bulk extract…
- **firecrawl-agent**: Autonomous multi-page extraction into structured JSON.
- **firecrawl-crawl**: Bulk-extract many pages from one site or section.
- **firecrawl-developer-index**: Search issues, merged pull requests, READMEs, and documentation.
- **firecrawl-download**: Save a site or section as local files (markdown, screenshots).
- **firecrawl-interact**: Drive a live browser on a scraped page: click, fill forms, log in, paginate, infinite-scroll.
- **firecrawl-map**: Discover and list a site's URLs, with search filtering.
- **firecrawl-monitor**: Alert by webhook/email on web changes — use for \"monitor/watch/track/alert me when\": recurring checks on known URLs (prefer over repeated one-off scrapes) or web-wide watches …
- **firecrawl-parse**: Convert a local file (PDF, DOCX, XLSX, HTML, …) to markdown, or answer questions about its content.
- **firecrawl-research-index**: Find the papers that answer a research query in Firecrawl's research paper index — a corpus of paper abstracts whose largest share is biomedical and life-science literature (Pub…
- **firecrawl-scrape**: Extract a URL's content as clean markdown, including JS-rendered pages.
- **firecrawl-search**: Web search with full page content.

### forge [off] (2 skills)

- **forge-evidence-gate**: Use when about to assert that a build passed, tests passed, types are clean, or linting succeeded — before writing that claim.
- **forge-risk-classify**: Use when about to edit, create, or delete files as part of an implementation task — before writing any code.

### fortytwo-mcp [off] (1 skills)

- **fortytwo-mcp**: Fortytwo Prime: collective multi-agent inference for high-stakes questions.

### founderos [off] (23 skills)

- **apply-mental-models**: Use when a founder faces a hard, ambiguous, or high-stakes decision and wants to think it through with proven lenses rather than gut alone - "help me think about this", "what am…
- **brand-and-naming**: Use when a founder needs to name the company or product and set a simple brand voice - when they say "what should I call it", "help me name my startup", "is this name any good",…
- **capture-learning**: Use after a Founder OS skill, flow, or decision produced a real outcome worth remembering - when something worked, something failed, advice turned out wrong, or the founder says…
- **cofounder-and-equity**: Use when a founder is choosing a co-founder or splitting equity - when they ask "do I need a co-founder", "how do I find a co-founder", "how do I split equity", "is 50/50 fair",…
- **consumer-product-testing**: Use when a founder has a real or prototype consumer/physical product (food, beverage, cosmetic, personal-care, household, hardware, or a packaged good) and needs to test whether…
- **customer-interviews**: Use when a founder needs to talk to potential customers and wants real signal, not flattery - when they say "I'm going to interview some users", "how do I do customer discovery"…
- **find-first-customers**: Use when a founder needs their first paying customers and there's no inbound, no audience, and no growth engine yet - when they say "how do I get my first customers", "nobody's …
- **first-hire**: Use when a founder is making early hires - when they ask "should I hire someone", "what's my first hire", "who do I hire first", "how do I write a job description", "how do I in…
- **founderos-prompt-scaffold**: Use when writing, refining, or porting any Founder OS prompt or skill, or when a founder asks "how do I write a good prompt for this" - provides the shared 3-tier (Low/Medium/Hi…
- **investor-pipeline**: Use when a founder is starting or running a fundraise and needs to manage it like a sales process - when they say "how do I find investors", "I'm raising and don't know where to…
- **landing-page-copy**: Use when a founder needs words for a landing page that converts - when they say "write my landing page", "what should my headline be", "my page isn't converting", "people don't …
- **launch-plan**: Use when a founder is approaching a launch and needs a sequenced plan instead of a single chaotic "go live" day - when they say "I'm launching next week", "how do I launch", "wh…
- **legal-and-incorporation**: Use when a founder is forming the company or worried they've skipped legal basics - when they ask "should I incorporate", "when do I form a company", "LLC or C-corp or what", "d…
- **north-star-metrics**: Use when a founder needs to decide what to measure - when they say "what metric should I track", "what's my north star", "I'm drowning in dashboards", "is this a vanity metric",…
- **pitch-deck**: Use when a founder needs to build or fix an investor pitch deck - when they say "help me make a pitch deck", "my deck isn't landing", "what slides do I need", "investors keep gh…
- **pivot-decision**: Use when a founder has run real experiments and must decide whether to keep going, change direction, or stop - the moment validation results, retention, pipeline, or runway are …
- **positioning-and-gtm**: Use when a founder is ready to take a product to market and needs to say what it is, who it's for, and why it wins - when they say "how do I describe this", "what's my positioni…
- **pricing-strategy**: Use when a founder needs to set or fix a price - when they say "how should I price this", "what should I charge", "am I too cheap", "should I do subscription or one-time", "how …
- **runway-and-unit-economics**: Use when a founder needs to understand the money - when they ask "how long until we run out of cash", "what's my burn rate", "how much runway do I have", "are my unit economics …
- **scope-mvp**: Use when a founder is about to start building and needs to decide what to build first - when they say "what should my MVP be", "what's the minimum I can ship", "I'm scoping the …
- **sensory-testing**: Use when a founder is testing a product people taste, smell, touch, or apply to the body - food, beverage, supplements, cosmetics, personal care, household - and needs to know i…
- **start-here**: Use when a founder is overwhelmed, unsure what to do next, just arrived at Founder OS, or asks "where do I start", "what should I work on", "I have an idea now what", or "help m…
- **validate-idea**: Use when a founder has a startup idea and needs to test whether it's real before building - when they say "I have an idea", "is this worth building", "how do I validate", "shoul…

### frontier-simplify [off] (3 skills)

- **frontier-simplify**: Stops an agent from manufacturing process around its own work — invented gates, approval flows, traceability matrices, verification machinery, and governance documents nobody as…
- **frontier-simplify-audit**: Diagnoses a repository that has accumulated agent-built bureaucracy.
- **frontier-simplify-review**: Review a change for concrete defects, then check repairs and their regressions against the preserved review.

### gangsta [off] (19 skills)

- **audit-review**: Use when completing tasks, implementing major features, or before merging — dispatches the-inspector to audit the books before the job is closed
- **drill-tdd**: Use when implementing any feature or bugfix — enforces the Red-Green-Refactor drill with no production code allowed without a failing test first
- **exit-strategy**: Use when implementation is complete and all tests pass — guides the clean exit from a development branch with structured options for merge, PR, or cleanup
- **interrogation-debugging**: Use when encountering any bug, test failure, or unexpected behavior — finds the rat in the code through systematic root-cause interrogation before any fix attempts
- **laundering**: Use when all territories report completion after the hit — handles integration, verification, consigliere final review, cleanup, and ledger updates to produce clean production-r…
- **omerta**: Use when enforcing governance guardrails during any gangsta operation — referenced as cross-cutting concern by all skills for anti-hallucination, authorization, state durability…
- **receiving-orders**: Use when receiving code review feedback — processes orders with technical rigor, not blind obedience or performative agreement
- **reconnaissance**: Use when beginning a new heist — deploys associates to survey the target codebase, existing tests, dependencies, documentation, and the ledger to produce a reconnaissance dossie…
- **resource-development**: Use when the contract is signed and work packages need to be created — decomposes the contract into bite-sized tasks, sets up git isolation, allocates territories and token budg…
- **safehouse-worktrees**: Use when starting feature work that needs isolation from the current workspace — sets up a secure safehouse with git worktrees for clean operational bases
- **sweep-verification**: Use when about to claim work is complete, fixed, or passing — sweeps for evidence before any assertions, because unverified claims are invalid
- **the-capo**: Use when orchestrating workers within a specific domain territory — managing work package dispatch, reviewing reports against the contract, and reporting status to the underboss
- **the-consigliere**: Use when needing impartial architectural advice, security audit, spec integrity review, or a second opinion — operates outside the chain of command with standing authority to in…
- **the-grilling**: Use when adversarial brainstorming is needed after reconnaissance — the Proposer, Devils-Advocate, and Synthesizer each run ONE pass (no rounds); the Don is grilled on the IDEA …
- **the-hit**: Use when the execution plan is approved and it is time for parallel execution — dispatches workers through crew leads to implement work packages with TDD enforcement, report col…
- **the-ledger**: Use when reading or writing institutional memory — insights from successful solutions, fails from historical mistakes, and the Project Constitution that accumulates commandments…
- **the-sit-down**: Use when the grilling consensus is approved and it is time to draft the formal contract specification — strictly prohibits code generation, produces the binding spec document th…
- **the-underboss**: Use when decomposing tasks into work packages, allocating territories to crew leads, managing heist phase progression, or serving as the operational buffer between the Don and t…
- **using-gangsta**: Use when starting any conversation — establishes how to find and use Gangsta skills, enforces the 1% invocation rule, maps platform tools, and routes the Don's intent through th…

### gcp-devkit [off] (6 skills)

- **cloud-run-deploy**: Scaffold everything needed to deploy a service to Cloud Run.
- **firestore-rules**: Generate or audit Firestore security rules.
- **gcloud-debug**: Diagnose common GCP failures on Cloud Run, GKE, and Cloud Functions.
- **gke-manifest**: Generate GKE-tailored Kubernetes manifests that use Workload Identity, BackendConfig, and Ingress with Google-managed certificates.
- **iam-audit**: Audit IAM bindings on a GCP project for overly broad roles and stale service account keys.
- **terraform-gcp**: Generate idiomatic Terraform for common GCP resources.

### gitbook [off] (6 skills)

- **build-integration**: Build, develop, and publish GitBook integrations — apps that run inside GitBook to add custom blocks, react to events, connect external services via OAuth, and extend the editor.
- **configure-site**: Create and maintain GitBook documentation sites end-to-end — design structure from source content, scaffold a Git monorepo, set up the GitHub/GitLab remote, drive the GitBook AP…
- **cr-create**: Drive an end-to-end GitBook docs review flow from Claude Code by calling the GitBook REST API directly with curl (no CLI) — create a change request, push content (update an exis…
- **cr-review**: Review GitBook change requests from Claude Code by calling the GitBook REST API directly with curl (no CLI) — the reviewer-side companion to cr-create (the authoring side over t…
- **write-docs**: Write, author, edit, and format GitBook documentation pages in Git-synced repos, IDEs, or any text editor.
- **write-openapi**: Author, configure, structure, and troubleshoot OpenAPI/Swagger API reference documentation in GitBook.

### god-prompt-mcp [off] (1 skills)

- **god-prompt**: Production workflow skill for coding, debugging, architecture, design, deployment,\nautomation, SEO, content, and other substantial build or review work.

### google-cloud-storage [off] (5 skills)

- **gcs-security-assessment**: Assesses the security posture of Google Cloud Storage (GCS) buckets and projects.
- **google-cloud-storage-basics**: Stores, retrieves, and manages data as objects in Cloud Storage (Google Cloud Storage, or GCS) buckets.
- **google-cloud-storage-bucket-architect**: Creates Cloud Storage (Google Cloud Storage, or GCS) buckets.
- **google-cloud-storage-diagnostic**: Troubleshoots and diagnoses Google Cloud Storage (GCS) errors, permission denials, and access control issues.
- **google-cloud-storage-fuse**: Mounts Cloud Storage buckets as a POSIX file system with Cloud Storage FUSE (gcsfuse).

### google-multi-account [off] (1 skills)

- **google-setup**: This skill provides guidance for setting up the Google Multi-Account MCP plugin.

### graphql-guardian [off] (1 skills)

- **graphql-guardian**: Use when changing a GraphQL schema or resolvers, reviewing a GraphQL pull request, or investigating slow GraphQL queries, N+1 database calls or breaking schema changes.

### greenfield [off] (13 skills)

- **architecture-design**: Use when producing the engagement design document, choosing architecture or stack for a client project, or generating the client repository's CLAUDE.md and AGENTS.md.
- **build-loop**: Use when actually building - working a task from pick-up to merge with an agent, verifying the result, reviewing agent-written code and tests, and handling what to do when the b…
- **build-standards**: Use when writing code, tests, or reviews on a client engagement, or when deciding whether work meets the engagement's definition of done.
- **business-test-cases**: Use when turning approved requirements into business test cases a person can execute - writing them, reviewing them, tracking their results, and taking them into handoff accepta…
- **discovery**: Use when scoping a new client engagement before requirements - running a discovery conversation, writing a problem statement, or producing an estimate range.
- **greenfield-delivery**: Use when working on a client greenfield engagement - starting one, moving through a delivery gate, writing requirements or design documents, syncing work to a tracker, or handin…
- **handoff**: Use when closing out a client engagement - assembling the delivery package, writing the runbook, or producing the engagement record for acceptance.
- **progress-reporting**: Use when writing or updating a client-facing engagement status page for business stakeholders - in Confluence, ADO Wiki, or repository markdown.
- **qe**: Use when automating test cases that already exist - generating Gherkin feature files from test-cases.md, deciding what should and should not be automated, wiring step definition…
- **requirements-gate**: Use when writing or reviewing engagement requirements and acceptance criteria, or preparing the client sign-off that establishes the scope baseline.
- **tracker-azure-devops**: Use when the engagement tracker is Azure DevOps and you need the ADO-specific mechanics - creating epics, features, or product backlog items, updating states, or writing ADO Wik…
- **tracker-conventions**: Use when deciding what belongs in a work item, ticket, story, or backlog item on a client engagement, and whether one is well-specified enough to assign to an agent.
- **tracker-jira**: Use when the engagement tracker is Jira and you need the Jira-specific mechanics - creating epics, stories, or issues, updating status, writing Confluence status pages, or assig…

### grill [off] (1 skills)

- **grill-core**: Conventions for grill agents: output format, severity ratings, evidence standards

### guide [off] (7 skills)

- **ask**: Ask any question about Claude Code features — setup, best practices, automation, models, plugins, MCP, configuration, and more.
- **game-mode**: Track your Claude Code feature usage, earn levels, and see your stats.
- **introspect**: Introspect your project — audit lifecycle coverage, find gaps, and improve your development environment.
- **level-up**: See your feature roadmap and get a personalized hint on what to try next.
- **migrate-to-claude**: Migrate your AI coding assistant config (Cursor, Windsurf, Copilot, Continue, Aider, Cody, Codex) to Claude Code.
- **onboard**: Interactive getting-started walkthrough for new Claude Code users.
- **visualize-setup**: Generate an HTML dashboard visualizing all installed Claude Code skills, plugins, and MCP servers with usage statistics and martial arts belt levels.

### handoff [off] (1 skills)

- **handoff**: Write or refresh the current git branch's handoff note — the non-code knowledge (goal, decisions and their rationale, gotchas found while implementing, what's done, what's still…

### handoff [off] (4 skills)

- **check**: Read-only inspector for saved handoffs.
- **discard**: Use when the user explicitly wants to discard a saved handoff without acting on it (the work is no longer relevant).
- **pickup**: Use when a saved handoff is surfaced at SessionStart, or when the user runs /handoff:pickup, to resume prior work — presents the saved directive and dispatches on the user's cho…
- **save**: Use when the user signals end-of-session — "save handoff", "pick this up later", "continue in a new session", "I'll come back to this".

### harness [off] (2 skills)

- **evolve**: 하네스 진화 스킬.
- **harness**: 프로젝트에 맞는 하네스를 설계하고, 전문 에이전트와 각 에이전트가 사용할 스킬을 만든다.

### harness-bootstrap [off] (1 skills)

- **init**: Bootstraps a complete, project-specific Claude Code harness — a lean CLAUDE.md plus the full .claude/ tree (hooks, agents, commands, skills) — from a one-paragraph description o…

### harness-designing [off] (4 skills)

- **hd:learn**: Answers questions about the five-layer design harness framework.
- **hd:maintain**: Captures design lessons and proposes rule adoptions from narrative to rule.
- **hd:review**: Reviews harness health (full) or targets one layer/file (targeted).
- **hd:setup**: Walks the five-layer design harness layer by layer.

### harness-init [off] (1 skills)

- **harness-init**: Use when initializing a new project, making a repo agent-ready, or adding architectural layer boundaries — produces AGENTS.md, docs/ system of record, boundary tests, linter rul…

### harnesskit [off] (12 skills)

- **apply**: Review and apply improvement proposals from /harnesskit:insights — presents diffs for approval
- **architect**: Design agent teams for your domain using 6 orchestration patterns — analyzes project, selects pattern, generates agent definitions and orchestrator
- **dev**: Start the development server for the detected framework — auto-configured based on project detection
- **init**: Generate harness infrastructure and toolkit files based on detection results and preset selection
- **insights**: Analyze session logs, failures, and usage patterns to propose harness and toolkit improvements as concrete diffs
- **lint**: Run linter and formatter for the project with auto-fix — integrates with HarnessKit error tracking
- **prd**: Decompose a PRD document into GitHub issues and feature_list.json entries
- **setup**: Detect project tech stack, choose experience preset, and initialize HarnessKit harness + toolkit
- **status**: Show current HarnessKit harness status — preset, feature progress, active failures, installed toolkit
- **test**: Run project tests with HarnessKit integration — logs failures to failures.json automatically
- **typecheck**: Run TypeScript type checker and summarize errors — only available for TypeScript projects
- **worktree**: Create a harness-aware git worktree for isolated feature work using Claude Code's built-in worktree

### headroom [off] (1 skills)

- **headroom**: Use when the user wants Claude to work with a document, log or data file too large to read whole, such as long specs, big logs or large JSON or CSV files.

### heavy-usage [off] (1 skills)

- **sweep**: Run a usage-budgeted, resumable sweep of the codebase that grinds until your heavy-usage wind-down threshold, then commits findings and (optionally) resumes after reset.

### hzblj-skills [off] (8 skills)

- **hooks**: Rules for custom hooks — naming, logic extraction, and separation of view and logic.
- **how**: Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\"…
- **orchestration**: Tiered multi-agent orchestration — an expensive model plans and synthesizes while specialized subagents do the work in their own isolated contexts.
- **project**: Monorepo project structure — Turborepo layout with packages/core-*, packages/platform-*, packages/feature-*, and deployable apps (mobile, web, backend, e2e), dependency directio…
- **teach**: Explain a body of work plainly so a person actually understands it.
- **type-safety**: Strict TypeScript typing — type over interface, no any, no as casts, narrow literal unions, discriminated unions, constructive modeling, exhaustive switch with never, satisfies,…
- **unslop**: Cut AI tells from writing and put a real voice back in.
- **why**: Investigate why code is the way it is — design rationale, rejected alternatives, the incident or customer that forced a threshold.

### instructions-cleanup [off] (2 skills)

- **rule-file-repair**: Fix conflicting CLAUDE.md and AGENTS.md instructions and stale commands while preserving approvals and exceptions.
- **rule-scope-audit**: Find which CLAUDE.md and AGENTS.md instructions apply and why ignored rules or conflicting instructions appear.

### intent [off] (17 skills)

- **articulate**: Design the words in a product — labels, instructions, errors, confirmations, empty states, onboarding copy, tooltips, voice and tone frameworks, and content models.
- **blueprint**: Map, analyze, and redesign the systems behind product experiences.
- **evaluate**: Structured UX evaluation that produces quantitative assessments, identifies specific issues, and routes to the right Intent skill for resolution.
- **fortify**: Harden designs for real-world use by systematically identifying and designing for every condition outside the happy path.
- **include**: Design for everyone by treating accessibility as a first-class design discipline, not a compliance checklist.
- **intent**: The entry point for Intent, a UX and design strategy system.
- **investigate**: Guide and conduct user research — from planning through synthesis.
- **journey**: Design any user-facing experience end-to-end: task flows, multi-step workflows, navigation structures, onboarding, settings, search, content creation, collaboration, signup, che…
- **localize**: Adapts experiences across cultures and languages — not just translation, but cultural reconception.
- **measure**: Defines and tracks UX success through metrics, measurement frameworks, and experimentation.
- **organize**: Structure information so people can find what they need, understand where they are, and navigate confidently.
- **philosopher**: A cross-cutting cognitive mode for sitting with design problems before rushing to solve them.
- **specify**: Bridges design and engineering by producing detailed specs, organized handoff packages, asset inventories, and cross-functional documentation.
- **storytelling**: Discipline for giving design work narrative structure that makes people care.
- **strategize**: Frames product design problems before solutions exist.
- **transpose**: Rethinks experiences for different platforms and contexts — not just resizing, but reconceiving.
- **wireframe**: Design the structural anatomy of screens at wireframe fidelity — what goes where and why, before anyone argues about how it looks.

### java-backend-skills [off] (15 skills)

- **java-build**: Resolution.
- **java-concurrency**: Lifetime.
- **java-debugging**: Causality.
- **java-design**: Cohesion.
- **java-idiomatic**: Contracts.
- **java-implement**: Execution.
- **java-performance**: Evidence.
- **java-unit-testing**: Behavior.
- **spring-boot**: Composition.
- **spring-data**: Atomicity.
- **spring-integrations**: Delivery semantics.
- **spring-observability**: Operability.
- **spring-security**: Authorization.
- **spring-testing**: Mechanism.
- **spring-web**: Translation.

### jira-attachment-plugin [off] (1 skills)

- **jira-issue-attachments**: Downloads and reads attachments from Jira Cloud user stories and issues using the official Atlassian MCP V2.

### jsonschemaapp-mcp [off] (7 skills)

- **add-schema-with-templates**: Use when the user asks how to add structured data / schema to their site or a URL, which schema type they should add, how to get a page into rich results, or how to fix a "missi…
- **ai-crawler-access**: Use when the user wants to fix or allow AI-crawler access in robots.txt, e.g.
- **ai-search-optimization**: Use when the user asks about AI search visibility, GEO, llms.txt / llms-full.txt, or whether AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) can access their site.
- **audit-report-format**: Reference for the standard shape of every JSON Schema App audit answer: a one-line verdict, findings grouped by P1/P2/P3 priority, each citing the tool that produced it.
- **draft-llms-txt**: Use when the user wants to create, write, or draft an llms.txt or llms-full.txt file for their site, e.g.
- **schema-rich-results**: Reference for how Schema.org / JSON-LD types map to Google rich results and AI readability.
- **structured-data-audit**: Use when the user wants to audit, check, or improve the JSON-LD / Schema.org structured data on their website or a single page, e.g.

### kotlin-lsp [off] (1 skills)

- **kotlin-lsp**: Real-time Kotlin code intelligence via kotlin-language-server.

### learn-wiki [off] (5 skills)

- **concept**: Resolve a concept named in learner evidence to a wiki concept entry, creating, naming, and placing it if it doesn't exist yet.
- **learn**: Turn on learning-first development in this project.
- **lint**: Health check for the learner wiki.
- **wiki-onboarding**: First-time onboarding for the learner wiki.
- **wiki-process**: Merge a learner evidence file into the learner wiki — resolve concepts, add evidence, update levels, prune, and regenerate INDEX.md and domain summaries.

### llm-secure-patterns [off] (6 skills)

- **agent-action-surface**: Use when designing or wiring up tool_use, function_calling, MCP servers, multi-agent chains, or calling multiple LLM providers (e.g., Gemini for vision plus Claude for reasoning…
- **llm-endpoint-hardening**: Use when designing or building a web route (FastAPI, Flask, Express, or similar) that accepts user input and forwards it to any LLM API (Claude, OpenAI, Gemini, or similar) — fi…
- **output-validation**: Use when designing or implementing code where LLM responses are rendered as HTML or markup in a frontend, written to a database, passed to another service, or used to generate e…
- **report**: Review or audit an existing codebase's security posture against the OWASP LLM Top 10.
- **secure-external-ingestion**: Use when designing or implementing code that fetches URLs, scrapes pages, calls external APIs, parses PDFs/HTML from untrusted sources, builds RAG retrieval pipelines, or proces…
- **system-prompt-design**: Use when designing, writing, editing, or reviewing system prompts for any LLM application — fire this skill during architecture/planning discussions (before prompts are drafted)…

### llm-wiki [off] (1 skills)

- **llm-wiki**: Build and maintain an LLM-curated knowledge base from papers, articles, transcripts, notes and project findings.

### local-whisper [off] (1 skills)

- **local-whisper**: Transcribes audio and video to text with Local Whisper, on the user's own computer, so the recording stays on their machine.

### localstack [off] (6 skills)

- **localstack**: Manage the LocalStack emulator lifecycle with the lstk CLI.
- **localstack-deploy**: Deploy infrastructure to LocalStack using IaC tools.
- **localstack-extensions**: Manage LocalStack Extensions.
- **localstack-iam**: Analyze and enforce IAM policies in LocalStack.
- **localstack-logs**: Analyze LocalStack logs and debug issues with lstk.
- **localstack-state**: Manage LocalStack state and snapshots with lstk.

### loop-and-gate-build-kit [off] (1 skills)

- **loop-and-gate**: Run a change through the Loop & Gate human-decision gates.

### mattpocock-skills [off] (38 skills)

- **ask-matt**: Ask which skill or flow fits your situation.
- **claude-handoff**: Hand the current conversation off to a fresh background agent that picks up the work immediately.
- **code-review**: Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (d…
- **codebase-design**: Shared vocabulary for designing deep modules.
- **diagnosing-bugs**: Diagnosis loop for hard bugs and performance regressions.
- **domain-modeling**: Build and sharpen a project's domain model.
- **git-guardrails-claude-code**: Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute.
- **grill-me**: A relentless interview to sharpen a plan or design.
- **grill-with-docs**: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
- **grilling**: Grill the user relentlessly about a plan, decision, or idea.
- **handoff**: Compact the current conversation into a handoff document for another agent to pick up.
- **implement**: Implement a piece of work based on a spec or set of tickets.
- **implement-spec**: Implement a specification in code.
- **improve-codebase-architecture**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **loop-me**: Grill me about specs for the workflows I want to build, within this workspace.
- **migrate-to-shoehorn**: Migrate test files from `as` type assertions to @total-typescript/shoehorn.
- **pr**: Use when writing a PR body.
- **prototype**: Build a throwaway prototype to answer a design question.
- **research**: Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo.
- **resolving-merge-conflicts**: Use when you need to resolve an in-progress git merge/rebase conflict.
- **retro**: Conduct a retrospective on a coding session.
- **scaffold-exercises**: Create exercise directory structures with sections, problems, solutions, and explainers that pass linting.
- **setup-matt-pocock-skills**: Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout.
- **setup-pre-commit**: Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo.
- **setup-ts-deep-modules**: Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point files.
- **tdd**: Test-driven development.
- **teach**: Teach the user a new skill or concept, within this workspace.
- **to-questionnaire**: Turn a decision you can't fully answer into a questionnaire for someone else to fill in.
- **to-spec**: Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed.
- **to-tickets**: Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in one…
- **triage**: Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs.
- **wait-what**: Stop.
- **wayfinder**: Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the d…
- **wizard**: Generate an interactive bash wizard that walks a human through steps only they can perform.
- **writing-beats**: Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it.
- **writing-for-agents**: Writing documents for agents.
- **writing-fragments**: Writing, explore: mine raw fragments, no structure yet.
- **writing-shape**: Writing, exploit: shape raw material into an article, paragraph by paragraph.

### mcp-apps [off] (4 skills)

- **add-app-to-server**: This skill should be used when the user asks to "add an app to my MCP server", "add UI to my MCP server", "add a view to my MCP tool", "enrich MCP tools with UI", "add interacti…
- **convert-web-app**: This skill should be used when the user asks to "add MCP App support to my web app", "turn my web app into a hybrid MCP App", "make my web page work as an MCP App too", "wrap my…
- **create-mcp-app**: This skill should be used when the user asks to "create an MCP App", "add a UI to an MCP tool", "build an interactive MCP View", "scaffold an MCP App", or needs guidance on MCP …
- **migrate-oai-app**: This skill should be used when the user asks to "migrate from OpenAI Apps SDK", "convert OpenAI App to MCP", "port from window.openai", "migrate from skybridge", "convert openai…

### mcp-client-kit [off] (2 skills)

- **generate-mcp-runner**: Use when generating a runnable, shape-aware smoke-test `run.py` for an MCP server's generated wrappers.
- **generate-mcp-wrappers**: Use when generating typed Python wrappers for an MCP server.

### mcp-debugging [off] (2 skills)

- **mcp-connect**: Fix my MCP connection error or MCP authentication failure in the client I actually use.
- **mcp-tool-check**: Find why my MCP tools are missing or failing after the server connects.

### mcp-gsc [off] (3 skills)

- **gsc-indexing-triage**: Diagnose Search Console indexing and sitemap questions with URL Inspection evidence while avoiding unsupported indexing claims or general-purpose Indexing API use.
- **gsc-search-opportunities**: Find evidence-backed Search Console optimization opportunities from query and page data without treating partial Search Analytics rows as exhaustive or causal proof.
- **gsc-weekly-review**: Review a Search Console property week over week using mcp-gsc while preserving Search Analytics data-completeness and causality boundaries.

### mcp-workflow-audit [off] (1 skills)

- **auditing-mcp-workflows**: Use when a Claude Code, MCP, or AI-agent workflow is fragile, has unclear write permissions, risks duplicate side effects, lacks failure recovery or verification, or needs an op…

### mcp2cli [off] (3 skills)

- **mcp-analyze**: Analyze MCP server source code to classify its pattern and assess CLI conversion feasibility.
- **mcp-codegen**: Generate TypeScript CLI tool code from an MCP server analysis.
- **skill-author**: Generate a SKILL.md file for a CLI tool so Claude Code can use it effectively.

### mcpbackend [off] (1 skills)

- **mcpbackend**: Use MCPBackend to manage schemas and APIs.

### mcpbinder [off] (6 skills)

- **get-started**: Introduce MCPBinder when someone first uses it or asks what it can do, which workspace and projects it can reach, or what it's allowed to change.
- **log-decision**: Record a decision, outcome or update as a permanent, attributed comment on an MCPBinder project or task.
- **plan-tasks**: Turn a goal, brief, meeting notes or pasted list into tasks in an MCPBinder project.
- **project-update**: Write a status update for an MCPBinder project, such as a weekly update or a summary of recent progress, from the project's goals, tasks and activity.
- **task-focus**: Help someone decide what to work on next in MCPBinder.
- **work-assigned-task**: Work on MCPBinder tasks assigned to this agent, when a task.assigned event arrives or someone asks you to pick up or check your assigned tasks.

### memories [off] (1 skills)

- **memories**: Session journaling — save, list, open, search, and delete session memories.

### memory-bank [off] (1 skills)

- **memory-bank**: Initialize, read, and maintain a structured Memory Bank — a set of markdown files in a memory-bank/ directory that preserve project context across sessions.

### mentor-mode [off] (1 skills)

- **mentor**: Activates mentor mode for the entire session.

### mind-plus-plus [off] (13 skills)

- **capture-idea**: Captures a quick idea, note, or thought with minimum friction — auto-classifies the context (client, product, personal, operational) and saves it to the right place, or routes t…
- **daily-brief**: Generates the morning situational briefing — today's agenda, urgent tasks, overdue follow-ups, and contexts without recent contact.
- **knowledge-search**: Searches the vault by topic or question and returns a synthesized answer with wikilinks to the source notes.
- **meeting-prep**: Prepares a briefing for an upcoming meeting by pulling recent meetings, open tasks, pending decisions, and unresolved follow-ups for the relevant client, product, or person.
- **new-decision**: Records an architecture or business decision as a structured ADR (Architecture Decision Record) with context, decision, consequences, and rejected alternatives.
- **new-meeting**: Processes a meeting and updates the vault.
- **process-inbox**: Triages the inbox/ folder — sorts files with no defined destination.
- **process-meeting-emails**: Automatic pipeline that ingests meeting transcription emails and creates structured notes in the vault.
- **setup-mind-plus-plus**: Sets up the Mind++ second brain from scratch — creates vault folder structure, captures the user profile, and generates configuration files.
- **specialist**: Routes a request to the right domain specialists and produces a vault-grounded deliverable.
- **stakeholder-update**: Generates a status update for a client, product, or project from vault content — recent meetings, decisions, open tasks, risks, and next steps.
- **user-profile**: Captures, updates, and consults the user profile — who they are, their professional context, projects, personal goals, and work preferences.
- **weekly-review**: Weekly review that consolidates tasks, unlogged meetings, at-risk contexts, and a preview of next week.

### mindmap [off] (2 skills)

- **mindmap**: Generate an interactive Markmap mindmap from a file, a URL, pasted text, or a topic.
- **mindmap-zh**: 从文件、URL、粘贴的文本或一个主题生成可交互的 Markmap 思维导图（中文版）。

### mindpowers [off] (6 skills)

- **calibrating**: Use after a knowledge-work deliverable ships or gets human edits.
- **drafting**: Use when a mindpowers spec exists and the user wants the actual deliverable written, such as "draft it", "write the memo from the spec", or right after mindstorming locks a spec.
- **fact-checking**: Use before a finished document ships, when the user asks "fact-check this", "is this ready to send", "check the numbers", or after drafting/review hand off a doc that carries ch…
- **mindstorming**: Use before drafting any non-code knowledge-work deliverable, including strategic memos, business reviews, OKR defences, PRDs, decision docs, briefing docs, exec talking points, …
- **reviewing-docs**: Use when the user has a finished or near-finished document (memo, business review, PRD, decision doc, briefing, comms, framework, talking points, post-mortem) and wants it press…
- **validating-problems**: Use when a user wants to test, sharpen, frame, or gather evidence for a customer or business problem before pitching a direction, prioritising work, or writing a PRD.

### mister-anderson [off] (20 skills)

- **add-supervisor**: Create a new implementation supervisor for a specific technology.
- **architecture**: Create high-level product architecture — system design, tech stack, structural decisions.
- **core-loop**: Enforces staged execution discipline on large tasks: a written stage plan, parallel delegation where the runtime supports it, a failable verification check at each stage, and a …
- **do**: Dispatch the implementation supervisor for a bead task.
- **implementation**: Stage 3 orchestrator — guides Implementation for a phase: shows task progress, routes through investigate → do → review → quality per task.
- **investigate**: Dispatch codebase investigation for a bead task.
- **manifesto**: Guide the creation of a product manifesto — vision, principles, and governing laws that shape all downstream decisions.
- **plan**: Create a phase/feature plan that scopes work, defines high-level tasks, and identifies dependencies.
- **product**: Stage 1 orchestrator — guides Product Discovery: manifesto → requirements → architecture.
- **quality**: QA finalization gate — validates spec conformity, runs tests/build/lint, produces a structured QA report.
- **requirements**: Transform a raw idea into a structured PRD (Product Requirements Document).
- **research**: Validate technical assumptions from the plan against real APIs, libraries, and codebase before spec creation.
- **review**: Code review gate — dispatches the code-reviewer agent to analyze an implementation branch, tracks findings, and auto-dispatches the supervisor for rework when verdict is NEEDS-R…
- **setup**: Bootstrap project orchestration with beads task tracking.
- **spec**: Create a detailed technical spec grounded in validated research.
- **specification**: Stage 2 orchestrator — guides Specification for a phase: plan → research → spec → tasks.
- **subagents-discipline**: Core engineering principles for implementation tasks
- **tasks**: Create beads from a spec (full decomposition) or from user input (ad-hoc issues).
- **update**: Update mister-anderson plugin and clean up legacy local copies that are now provided by the plugin system.
- **workflow**: Meta-orchestrator — shows project state across all 3 stages, suggests next step, and routes to stage orchestrators or individual skills.

### ml-pipeline [off] (1 skills)

- **ml-pipeline**: MANDATORY whenever a task involves training, fine-tuning, tuning, or evaluating a machine-learning model on data (tabular, time series, text, images — any modality).

### modern-web-guidance [off] (2 skills)

- **chrome-extensions**: Build and publish Chrome Extensions using Manifest V3 best practices.
- **modern-web-guidance**: Search tool for modern web development best practices.

### n8n-knowledge [off] (1 skills)

- **n8n-knowledge**: Deep search of the n8n knowledge base — community solutions, GitHub issues, workarounds, and node specs.

### no-cape [off] (14 skills)

- **clarifying-requirements**: Use when starting a new feature, component, or project whose requirements are underspecified or ambiguous — before designing or writing code
- **durable-plans**: Use when planned work will outlive the current session — persisting a plan to disk, resuming work from an on-disk plan, or landing changes a plan file describes
- **escalate-dont-thrash**: Use when repeated attempts at the same problem keep failing without producing new evidence — before trying another variation of the last fix
- **exploring-approaches**: Use when starting a new project or significant feature from a vague idea — before clarifying details or planning, especially when the user already has a preferred approach
- **fail-loud**: Use when writing error handling — try/catch blocks, fallback values, default parameters, retries, or any code path that handles failure
- **measure-before-optimizing**: Use when asked to improve performance, or when about to optimize code believed to be slow
- **receiving-feedback**: Use when receiving code review comments, reviewer suggestions, or technical corrections — before implementing any of them
- **root-cause-debugging**: Use when encountering a bug, test failure, regression, flaky test, or unexpected behavior — before proposing or applying any fix
- **safe-refactoring**: Use when restructuring, renaming, moving, or extracting code that already works — before making the first edit
- **schema-migration-safety**: Use when writing database schema migrations or changing tables, columns, indexes, or constraints on a system with real data
- **surgical-changes**: Use when editing existing code — bug fixes, small features, or any change inside a codebase you didn't just write
- **verify-before-done**: Use when about to claim work is complete, fixed, or passing — before committing, opening a PR, marking a task done, or relaying a subagent's success report
- **writing-meaningful-tests**: Use when writing or modifying tests, adding mocks, or tempted to add test-only methods to production code
- **writing-solid-plans**: Use when designing or planning a multi-step feature, refactor, or spec before implementation begins

### noetic-control-room [off] (4 skills)

- **brief-worker**: Write and send the brief that assigns one epic to one AI coding worker in the fixed EPIC shape (branch, scope, grants, model and effort, acceptance that can fail) and deliver it…
- **land-ready**: Check a worker's pull request that ends with "EPIC <id> READY <sha> <url>" and land it on the integration branch by a fixed checklist (READY sha, scope, security read, merge --n…
- **run-desk**: Keep one decision desk of what only the person can decide or do (a choice between options, creating an environment, granting access, answering a client) as GitHub issues labelle…
- **start-cloud-worker**: Start a new AI coding worker as a Claude Code cloud session (claude.ai/code) for one profile of a repository - the cloud environment, its setup script, the worker section of CLA…

### notify [off] (4 skills)

- **check**: Health check for notify — verifies terminal-notifier/notify-send installed, notify.sh script exists, hook entries in settings.json, and notify-config.json.
- **setup**: Use only when the user explicitly invokes /notify:setup — one-time setup of cross-platform desktop notifications (installs the notifier, wires the Stop/Notification/SubagentStop…
- **uninstall**: Use only when the user explicitly invokes /notify:uninstall — removes notify's hooks and config while leaving other settings intact.
- **wizard**: Interactive Q&A for customizing notification preferences (sounds, durations, matcher regex, per-event toggles).

### nvidia-skills [off] (1 skills)

- **nvidia-skill-finder**: Use for NVIDIA-related requests where an NVIDIA skill might help, even if the user did not ask for a skill.

### oak-national-academy [off] (3 skills)

- **oak-accessibility**: Make ANY artefact meet WCAG 2.2 AA — the accessibility floor for everything, Oak-branded or not — and audit existing artefacts against it.
- **oak-curriculum-principles**: Apply Oak National Academy's six curriculum principles — knowledge and vocabulary rich, sequenced and coherent, evidence-informed, flexible, diverse, and accessible — when desig…
- **oak-curriculum-principles-mcp-enabled**: Ground Oak National Academy's six curriculum principles in Oak's *live* curriculum data using the Oak Curriculum MCP server.

### observability [off] (1 skills)

- **setup-otel-propagation**: Configure OpenTelemetry context propagation (OTEL_PROPAGATORS) for services running in Kubernetes, especially when using mirrord to intercept or steal traffic.

### open-source-launch-skill [off] (1 skills)

- **open-source-launch**: Prepare any open-source repository for a clear, trusted public launch.

### opencode [off] (3 skills)

- **gpt-5-4-prompting**: Internal guidance for composing provider-neutral OpenCode prompts for coding, review, diagnosis, and research tasks inside the OpenCode Claude Code plugin
- **opencode-cli-runtime**: Internal helper contract for calling the opencode-companion runtime from Claude Code
- **opencode-result-handling**: Internal guidance for presenting OpenCode helper output back to the user

### opencode-subagent-mcp [off] (1 skills)

- **delegate-to-opencode**: Decide when to delegate work to the opencode subagent tools (agent, send_message, wait, stop, list) instead of a native Claude subagent, and how to brief and review them.

### paypal [off] (2 skills)

- **paypal-best-practices**: PayPal integration guidance, code examples, and best practices.
- **paypal-routing**: PayPal payments, subscriptions, checkout, invoices, disputes, webhooks, BNPL, Venmo, SDK, v5, v6, Fastlane, Braintree Fastlane, braintree-web, accelerated guest checkout.

### pdf-viewer [off] (1 skills)

- **view-pdf**: Interactive PDF viewer.

### pge-orchestrator [off] (16 skills)

- **pge**: PGE Orchestrator — autonomously runs Planner → Generator → Evaluator pipeline for multi-sprint product builds.
- **pge-autolaunch**: (no description)
- **pge-clean**: (no description)
- **pge-eval-backend**: Select the evaluator backend for PGE pipeline — claude (default), codex, or gemini.
- **pge-god**: PGE God Mode — absolute maximum quality pipeline.
- **pge-idontcaretokenanymore**: PGE idontcaretokenanymore — premium unlimited-token pipeline.
- **pge-indicator**: (no description)
- **pge-limit**: Set or clear a usage-based auto-pause threshold for PGE pipelines.
- **pge-notify**: (no description)
- **pge-preflight**: (no description)
- **pge-quality**: PGE Quality Orchestrator — runs the full Planner→Generator→Evaluator pipeline with the quality evaluator.
- **pge-statusline**: (no description)
- **pge-strict**: PGE Strict Orchestrator — runs the full Planner→Generator→Evaluator pipeline with the strict (FAIL-biased) evaluator.
- **pge-summary**: (no description)
- **pge-ultra**: PGE Ultra Orchestrator — runs the full PGE pipeline with multi-evaluator evaluation per sprint.
- **pge-update**: (no description)

### planning-skills [off] (14 skills)

- **breadboard-reflection**: Compare accepted intent with implementation reality, assess realized conformance and effect separately, diagnose failures backward, and prepare explicit correction decisions.
- **breadboarding**: Map current behavior, candidate shapes, or a selected design into places, affordances, stores, consequences, and wiring when concrete behavior needs clarification.
- **dumplink**: Turn a selected, bounded project into sequenced vertical task groups with dependencies, risks, appetite-based cuts, acceptance checks, and a bounded handoff.
- **executable-breadboards**: Turn a selected slice into fixtures, example runs, expected outputs, edge cases, and acceptance tests when it is ready for a buildable behavioral handoff.
- **feed-planning-context**: Prepare a compact context packet when an implementation agent needs the authoritative planning subset, execution contract, non-goals, and verification target for one active task…
- **framing-doc**: Create a frame from research, notes, requests, or transcripts when the current problem, desired outcome, boundaries, and evidence need to become explicit.
- **interface-contracts**: Define plain-language inputs, outputs, branches, errors, and open decisions when a selected slice crosses a meaningful data, service, or system boundary.
- **kickoff-doc**: Create a builder-facing kickoff document from accepted planning artifacts when a team needs a durable reference organized by shaped product territory.
- **lead-user-research**: Inspect future-facing markets with Eric von Hippel's Lead User Method when teams need evidence-traceable trend, lead-user, and opportunity research.
- **planning-router**: Inspect product-planning context and choose the smallest next move when no specific move is selected, while preserving fluid entry points and explicit commitment gates.
- **shaping**: Shape ambiguous product work before implementation by iterating among requirements, solution shapes, fit checks, spikes, and candidate evidence while keeping commitment gates ex…
- **sketch-reconciliation**: Reconcile a screenshot, wireframe, mockup, whiteboard, or sketch with existing planning artifacts when visual evidence may change the frame, criteria, scope, or shape.
- **statechart**: Derive states and transitions from an accepted breadboard when retries, timeouts, approvals, lifecycle stages, or multiple valid actions make behavior difficult to review.
- **wayfinding**: Coordinate planning across multiple agent sessions as a shared map of dependent decision, evidence, prototype, and prerequisite tickets when one bounded route cannot fit in a si…

### platform-skills [off] (1 skills)

- **platform-skills**: Use when troubleshooting, implementing, reviewing, or auditing platform infrastructure as a system — where Kubernetes, GitOps, CI/CD, and security concerns intersect.

### plugin-manager [off] (1 skills)

- **open**: Open the Plugin Manager UI in the browser.

### plugin-packaging [off] (3 skills)

- **plugin-install-check**: Check whether my skills-only Claude plugin actually loads, invokes its skills and reads its bundled resources in the target host.
- **plugin-package-audit**: Find why a skills-only Claude plugin works locally but fails to install, load skills or find its resources for colleagues.
- **plugin-package-repair**: Fix the manifest, paths and broken references in my existing skills-only Claude plugin so colleagues can use the same files.

### plugin-pilot [off] (1 skills)

- **Plugin Pilot**: This skill should be used proactively at the START of every new task or conversation when the working directory contains a project (has package.json, Cargo.toml, pyproject.toml,…

### pm [off] (10 skills)

- **build-guidance**: Analyzes the next package spec and provides specific guidance on what to do next, what to tell Builder, and what to prepare.
- **decision-support**: Structures decisions with options, trade-offs, and recommendations.
- **package-generation**: Breaks an approved product spec into build packages with correct dependencies, matching the dev plugin's exact format.
- **product-interview**: Runs a structured product interview with 6 core questions and conditional follow-ups to capture everything needed for a product spec.
- **progress-tracking**: Reads STATUS.md, package files, DECISIONS.md, PARKED.md, and git log to present comprehensive project status.
- **project-state**: Detects the current project state (empty, planned, mid-build, complete) by reading .dev/ directory, STATUS.md, and package files.
- **quality-assurance**: Runs pre-flight checks including plugin validation, package completion, tests, dependency satisfaction, decision resolution, and standards compliance.
- **scaffold-creation**: Creates the .dev/ project structure, writes all project files, initializes git, and optionally creates a GitHub repo.
- **spec-writing**: Generates a full product spec from interview answers using the product-spec template, with revision and approval flow.
- **troubleshooting**: Diagnoses build failures and problems by reading project context, matching common failure patterns, and prescribing exact fixes.

### productivity [off] (4 skills)

- **memory-management**: Two-tier memory system that makes Claude a true workplace collaborator.
- **start**: Initialize the productivity system and open the dashboard.
- **task-management**: Simple task management using a shared TASKS.md file.
- **update**: Sync tasks and refresh memory from your current activity.

### project-artifact [off] (1 skills)

- **project-artifact**: Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, n…

### project-memory [off] (1 skills)

- **project-memory**: Use when the user asks Claude to remember, recall or forget a project fact, decision or convention across sessions, or at the start of work on a project that has stored memories.

### project-pilot [off] (13 skills)

- **adr-generator**: Generate Architecture Decision Records.
- **breaking-change-detection**: Detect breaking changes between versions.
- **bus-factor**: Analyze knowledge concentration and bus factor risks.
- **code-history**: Explain why code was written a certain way using git history and blame.
- **dependency-analysis**: Analyze project dependencies.
- **impact-analysis**: Analyze blast radius of code changes.
- **onboarding-guide**: Generate onboarding guide for new team members.
- **project-analyze**: Analyze project tech stack, folder structure, architecture, and business logic.
- **project-context**: Provides ambient project awareness.
- **project-dashboard**: Show project health dashboard with combined metrics.
- **release-notes**: Generate release notes from git history.
- **sprint-health**: Analyze sprint health and development velocity.
- **tech-debt**: Scan for technical debt: complex code, stale TODOs, outdated dependencies.

### project-scaffolder [off] (7 skills)

- **context-manager**: Use at the end of every task in a scaffolded project and whenever the session context grows heavy.
- **cortex**: Use when a task needs to be executed through the full development pipeline — classification, delegation, QA, user testing, and learning propagation.
- **design-first**: Use before executing the first operational task of a phase and any Complex task.
- **persona-lab**: Use after QA passes to simulate end-user testing with diverse profiles.
- **pipeline-logger**: Use to log every operation in the synaptic pipeline.
- **project-scaffolder**: Use when starting ANY new project from a user brief.
- **synapse**: Use after a task completes to propagate learning across connected skills.

### project-setup [off] (6 skills)

- **detect-directories**: Discover additional source directories outside the project root that should be accessible.
- **detect-environment**: Detect language runtimes, virtual environments, and toolchains (Python, Node, Rust, Go).
- **detect-ide-settings**: Read IDE/editor configuration files (VSCode, PyCharm, Vim/Neovim, Emacs) to discover project settings.
- **detect-linters**: Detect linters and formatters configured in the project across Python, JS/TS, Rust, and Go.
- **detect-runtime-context**: Detect whether the project is running locally or in a remote/container environment (GitHub Codespaces, VS Code Dev Containers, Gitpod, SSH, etc.).
- **detect-test-runners**: Detect test runners and testing configuration across Python, JS/TS, Rust, and Go.

### prompt-brain [off] (2 skills)

- **migrate-prompt**: Migrates a prompt that was tuned for one model so it is optimized for another, using per-model guides.
- **optimize-prompt**: Analyzes and optimizes any Claude Code prompt — identifies weaknesses, applies best practices, reconstructs the prompt, and generates a changelog.

### prompt-coach [off] (1 skills)

- **coach**: Send a rough request to the prompt-coach agent and get back suggestions and an improved prompt

### prompt-design [off] (1 skills)

- **prompt-design**: Use when designing, revising, evaluating, or debugging any prompt artifact — a one-shot request, system or project instruction, rule file, agent or skill definition, tool/functi…

### prompt-enhancer [off] (1 skills)

- **enhance**: Use this when the user asks to improve, rewrite, sharpen, polish, tighten, "enhance" or "make better" a prompt, task, spec or instruction they are going to give to an AI or a co…

### prompt-enhancer-pack [off] (4 skills)

- **enhance**: Enhance a vague or rough prompt into a well-structured, comprehensive prompt before responding.
- **enhance-code**: Enhance a vague coding prompt into a detailed, developer-focused prompt.
- **enhance-for**: Enhance a prompt optimized for a specific AI platform (ChatGPT, Gemini, Cursor, Copilot, Claude).
- **enhance-writing**: Enhance a vague writing prompt into a detailed creative brief with audience, tone, structure, and quality constraints.

### prove [off] (2 skills)

- **empirical-method**: Measure a change before you ship it.
- **scaffold-benchmark**: Measure a proposed change for the developer — author and run the experiment, don't hand them a blank template.

### public-repo-readiness [off] (1 skills)

- **public-repo-readiness**: Use when the user asks to "make this repo public ready", "publicize the repo", "genericize the repo", "public-ready check", or any similar request to audit a codebase before ope…

### qdrant [off] (22 skills)

- **qdrant-clients-sdk**: Qdrant provides client SDKs for various programming languages, allowing easy integration with Qdrant deployments.
- **qdrant-deployment-options**: Guides Qdrant deployment selection.
- **qdrant-edge**: Guides building on Qdrant Edge, the embedded in-process shard.
- **qdrant-indexing-performance-optimization**: Diagnoses and fixes slow Qdrant indexing and data ingestion.
- **qdrant-memory-usage-optimization**: Diagnoses and reduces Qdrant memory usage.
- **qdrant-minimize-latency**: Guides Qdrant query latency optimization.
- **qdrant-model-migration**: Guides embedding model migration in Qdrant without downtime.
- **qdrant-monitoring**: Guides Qdrant monitoring and observability setup.
- **qdrant-monitoring-debugging**: Diagnoses Qdrant production issues using metrics and observability tools.
- **qdrant-monitoring-setup**: Guides Qdrant monitoring setup including Prometheus scraping, health probes, Hybrid Cloud metrics, alerting, and log centralization.
- **qdrant-multitenancy**: Guides tenant isolation architecture in Qdrant for multi-tenant or multi-user applications.
- **qdrant-performance-optimization**: Navigation hub linking sub-skills for proactive Qdrant tuning: search speed, indexing performance, and memory usage optimization.
- **qdrant-scaling**: Guides Qdrant scaling decisions.
- **qdrant-scaling-data-volume**: Guides Qdrant data volume scaling decisions.
- **qdrant-scaling-qps**: Guides Qdrant query throughput (QPS) scaling.
- **qdrant-scaling-query-volume**: Guides Qdrant query volume scaling.
- **qdrant-search-quality**: Diagnoses and improves Qdrant search relevance.
- **qdrant-search-quality-diagnosis**: Diagnoses Qdrant search quality issues.
- **qdrant-search-speed-optimization**: Diagnoses and fixes slow Qdrant search.
- **qdrant-search-strategies**: Guides Qdrant search strategy selection.
- **qdrant-sizing**: Sizes a Qdrant deployment before it is provisioned.
- **qdrant-version-upgrade**: Covers upgrading Qdrant server and SDKs without interrupting availability or losing data integrity.

### rag-evaluation [off] (3 skills)

- **rag-answer-check**: Check whether a RAG answer and its citations are supported by the retrieved passages and the right source documents.
- **rag-incident-repair**: Prepare a pipeline correction for a diagnosed RAG failure and check the resulting retrieval and answer evidence.
- **rag-retrieval-check**: Debug wrong RAG answers by checking retrieval quality, missing documents and the evidence needed for grounded citations.

### remember [off] (1 skills)

- **remember**: Save session state for clean continuation next session.

### repo-hygiene [off] (9 skills)

- **cleaning-existing-codebase**: Use when the user asks to "clean up", "apply repo-hygiene to", or "fix the hygiene of" an existing codebase — orchestrates the other hygiene skills in a phased, reviewable order…
- **gating-commits**: Use when about to commit, merge, or push — runs verification (tests, typecheck, lint), confirms focus, and checks sibling hygiene (docs, tests, docstrings) BEFORE the commit lan…
- **keeping-docs-fresh**: Use when changing a public API surface — renamed export, changed signature/return type, new or removed flag/route/env var, schema migration, deprecation — before committing, so …
- **keeping-files-small**: Use when about to add lines to an existing source file, when a single file passes ~400 lines, or when proposing where to put new code — prevents files from sprawling into multi-…
- **orienting-to-repo**: Use when starting substantive work in an unfamiliar repo, before diving into task-specific grep or edits — especially when the task touches business logic, public API, build, or…
- **testing-new-code**: Use when adding or modifying business logic, branching code, public API, or fixing a bug in a repo using repo-hygiene — tests for the new code paths must exist before the change…
- **using-repo-hygiene**: Use when starting any conversation in a repo — establishes the repo-hygiene skill set and the moments each sub-skill applies
- **writing-commit-messages**: Use when drafting any commit message — sets format (imperative subject under 72 chars, explanatory body when the why isn't obvious from the diff) and prevents the "Fix X" one-li…
- **writing-docstrings**: Use when writing or modifying any function, method, class, or source file in a repo using repo-hygiene — public API, internal helpers, and new files all require docstrings; only…

### review-council [off] (1 skills)

- **review-council**: Use when the user asks for a thorough, multi-angle code review of a working tree, git diff, or GitHub pull request before merging — dispatches six independent read-only speciali…

### scout [off] (3 skills)

- **fetch**: Fetch web page content from URLs.
- **search**: Web search and content fetching.
- **setup**: Guided interactive setup for scout's search engines and fetching tools.

### sdd-superpowers [off] (21 skills)

- **dispatching-parallel-agents**: Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies
- **finishing-a-development-branch**: Use when implementation is complete, all tests pass, and a decision is needed on how to integrate the work
- **receiving-code-review**: Use when receiving code review feedback, before implementing review suggestions
- **requesting-code-review**: Use when the user asks for a code review directly, before merging to main, or after completing a major feature
- **sdd-brainstorm**: Use when an idea is fuzzy, exploratory, has competing approaches, or needs a technology/architecture decision investigated before specification
- **sdd-execute**: Use when a plan is approved and implementation should begin
- **sdd-init**: Use when starting a new project that has no CLAUDE.md and no docs/specs/ directory
- **sdd-integrations**: Use when a user wants to connect their own custom Claude Code skill (e.g.
- **sdd-plan**: Use when a feature spec exists and needs to become a technical implementation plan
- **sdd-review**: Use when a spec needs a completeness check before planning, or when implementation claims to be complete and needs spec-alignment validation
- **sdd-spec-update**: Use when a user describes a change, addition, or correction to an approved spec — during or before implementation
- **sdd-specify**: Use when a user describes a new feature, idea, or problem without an existing spec — before any planning, research, or code
- **sdd-tasks**: Retired — do not use.
- **sdd-workflow**: Use when starting any conversation in an SDD project
- **session-wrap**: Use when ending a session to capture memory candidates and narrative lessons before context is lost
- **subagent-driven-development**: Use when executing implementation plans with independent tasks in the current session
- **systematic-debugging**: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
- **test-driven-development**: Use when implementing any feature or bugfix, before writing implementation code
- **using-git**: Use when any git operation is needed in an SDD project — branch creation, commits, merge commit validation, showing the convention, or setting up an isolated git worktree for pa…
- **verification-before-completion**: Use when about to claim work is complete, fixed, or passing
- **writing-skills**: Use when creating new skills, editing existing skills, or verifying skills work before deployment

### second-arrow [off] (1 skills)

- **second-arrow**: Invoke on EVERY user prompt to scan tone before responding.

### semgrep [off] (3 skills)

- **add-and-validate-guardian-developer-semgrep-rule**: write a custom semgrep rule with the user, add it to guardian in either user or repo scope, and prove it fires by writing a file that should trip it.
- **install-mfw**: Install the mfw (Semgrep Malware Firewall) CLI via the curl|sh installer and walk the user through setup — trust store, PATH shims, shell integration, and the background daemon …
- **remove-guardian-developer-semgrep-rule**: Remove a custom Semgrep rule from Guardian — list what is installed, work out which file holds the rule, and delete or edit it out of the user or repo rules directory.

### senior-developer [off] (1 skills)

- **work-on-issue**: MUST use when the message contains a GitHub issue reference — URL (github.com/.../issues/N) or number (#N) — regardless of other content in the message.

### sensei [off] (14 skills)

- **challenge-me**: Generate a project-relevant exercise with acceptance criteria
- **commands**: Show available commands and their triggers
- **dojo-open**: Open a teaching session with briefing and skill pulse
- **notecards**: Quiz the student using spaced repetition from the Concept Index
- **pizza-time**: Close the session and update progress tracking files
- **progress-report**: Visual summary of mastery levels and learning progress
- **reset**: Re-establish Sensei teaching mode if character voice or Socratic discipline has drifted
- **sensei-check**: Validate Sensei setup — confirms CONFIG.md, character, safeword, ROADMAP.md, and PROGRESS.md are present
- **set-mode**: Change learning mode mid-project
- **setup**: Initialize sensei in the current project
- **show-me**: Prediction-driven annotated code demo with reflection
- **spar**: Attempt-compare-gap loop for deliberate practice
- **teach-back**: Explain a concept back to your sensei to test your mental model
- **why**: Deep-dive into the reasoning behind a pattern or concept

### sf [off] (3 skills)

- **document**: Generate minimal documentation through parallel agents
- **implement**: Implement through pattern learning
- **spec**: Create specifications from requirements

### shipwright [off] (1 skills)

- **setup**: Set up Shipwright — a la carte toolkit for best practices, memory, and planning

### shipwright [off] (12 skills)

- **audit-full**: Branch-aware audit.
- **frontend-design**: Create distinctive, production-grade frontend interfaces.
- **merge-pr**: Merge current PR after CI passes.
- **parallel-builder**: Build multiple files/pages in parallel using subagents.
- **push**: Smart commit + push + auto-create PR.
- **review-code-fix**: Code review → fix → re-review loop until score ≥ 9.5.
- **review-docs**: Verify Phase D doc updates are accurate.
- **review-full**: Smart review entry point.
- **review-ux-fix**: UX review → fix → re-review loop targeting 10/10.
- **ship**: One-command pipeline from "done coding" to "PR ready for review".
- **skill-creator**: Meta-skill that teaches how to create effective Claude Code skills.
- **update-docs**: Sync documentation with code changes.

### shipwright [off] (26 skills)

- **agent-admin**: Query and manage Shipwright agents via the admin API — cron jobs, env vars, tool permissions, API tokens, and plugins.
- **canary-execution**: Cross-cutting contract for the test-readiness pipeline.
- **consolidation-fix**: Read consolidation-report.md and queue ready_to_propose duplication patterns as task-store tasks, one task per pattern, each carrying a strangler-fig (build -> coexist -> elimin…
- **consolidation-scan**: Discover emerging duplicate/similar code patterns via judgment-driven comparison, track them across runs in a ledger, and report only patterns that have stabilized.
- **entropy-fix**: Read entropy-report.md and queue PR-worthy violations as task-store tasks, one task per rule, with per-finding HITL classification.
- **entropy-scan**: Scan codebase for principle deviations.
- **error-fix**: Read error-report.md, fetch each New/Regressed issue's Sentry detail and stack trace, classify hitl per issue, and queue task-store tasks (plus companion observability-fix tasks…
- **error-resolve**: Read the error-patrol ledger, check each linked task's current status via the task store, and resolve the corresponding Sentry issue once its gating task has reached deployed/done.
- **error-scan**: Scan Sentry for new/regressed unresolved issues, dynamically map them to repos.
- **investigate-cron**: Diagnose why a cron run behaved unexpectedly — looks up the exact run via the admin cron-runs API (by name+time or by PR/task id), finds the matching Claude Code session transcr…
- **learning-capture**: Capture a durable learning by editing context directly.
- **pull-requests**: Query PR records from the task store — filter by repo, PR number, state, reviewState, or staged flag, and display results as a readable table.\n
- **repo-config**: Cross-cutting contract for the test-readiness pipeline.
- **review-staged**: Walk through staged PR reviews from the task store conversationally — APPROVEs first, then COMMENTs, smallest diff to largest within each.
- **security-fix**: Read security-report.md and queue PR-worthy findings as task-store tasks, one task per rule, routing any finding that requires credential rotation/revocation through /shipwright…
- **security-scan**: Scan a repo for secrets, dependency CVEs, container CVEs/SBOM, GitHub Actions issues, authn/authz anti-patterns, and posture gaps across three tiers.
- **slack-say**: Post a one-line progress update into the Slack thread or channel a run started from.
- **speed-budgets**: Cross-cutting contract for the test-readiness pipeline.
- **task-store**: Query and update the Shipwright task store — pick the next ready task, mark status transitions, and append new tasks.
- **test-debt**: Post-execution skill for the test-readiness pipeline.
- **test-design**: Phase 2 of the test-readiness pipeline.
- **test-fix**: Read docs/test-readiness/test-readiness-plan.md and queue its flat T-NNN task list as task-store tasks, one task per row, with dependency edges (predecessor/fan-out) and per-tas…
- **test-inventory**: Phase 1 of the test-readiness pipeline.
- **test-migration**: Phase 3 of the test-readiness pipeline.
- **test-readiness**: Orchestrates the full test-readiness pipeline (phases 1–5), once per qualifying repo under repos/, each in its own worktree + branch.
- **test-roadmap**: Phase 4 of the test-readiness pipeline.

### shipwright [off] (12 skills)

- **breakdown**: Decompose a hardened SDD into at most 8 atomic, dependency-ordered tasks, create them as Claude Code tasks and (optionally) Jira subtasks, and write task_state.json.
- **checkpoint**: Show, write, or clear shipwright's resume checkpoint, or clear the current plan.
- **dashboard**: Open the read-only shipwright pipeline dashboard (risks, tasks, amendments, budget, patterns, inbox) and call out anything that needs action.
- **design**: Generate a System Design Document (SDD) from a requirement or Jira ticket, then harden it with fresh-context adversarial review across 10 failure classes until it converges.
- **doctor**: Diagnose a shipwright installation — Python version, framework.json, whether the configured test/lint/typecheck/build commands actually run, Jira config, statusline wiring, and …
- **init**: Set up shipwright in the current project in one step — detects the stack, writes .claude/framework.json and state files, wires the budget statusline, seeds CLAUDE.md, optionally…
- **remember**: Save a durable project learning — a decision, a correction, an anti-pattern, or a convention — as a memory that shipwright re-injects at session start and design time.
- **resume**: Continue interrupted shipwright work from .claude/checkpoint.json — reports where it stopped, checks the budget window has reset, and picks up the literal next action.
- **retro**: Structured feature retrospective once implementation finishes — diffs plan vs.
- **review**: Guide a staff/lead engineer through a hardened SDD section by section instead of dumping the whole document — orientation, then Risk Register by severity, adversary pass history…
- **sdd-implementer**: Implement an approved shipwright plan task by task from its SDD, staying in the implement-bug-fix loop without process interruptions while silently staging design amendments and…
- **ship**: Gated deploy pipeline — documentation, tests, type check, independent code review, build — then Jira transitions and Slack notification.

### sideboard [off] (1 skills)

- **sideboard**: Maintain and display a live project roadmap/kanban board backed by GitHub Issues.

### siem-lab-coach [off] (1 skills)

- **coach**: Operate the Splunk lab, grade answers, and teach the curriculum

### signal-hunter [off] (7 skills)

- **add-source**: Add a new content source to the daily knowledge builder.
- **deploy**: Deploy Signal Hunter for automated daily digests — local macOS setup with launchd
- **digest**: Run the full daily knowledge digest pipeline — collect from all sources, synthesize trends with scoring and velocity tracking, write Obsidian notes
- **list-sources**: Show all configured sources in the daily knowledge builder grouped by category
- **setup**: Set up the Daily Knowledge Builder — install dependencies, configure sources, and create Obsidian vault structure
- **test-source**: Test a specific source or category to validate scraping works and output is meaningful
- **weekly**: Generate a weekly trend report from the last 7 days of daily digests and cache data

### sixth-sense [off] (13 skills)

- **configuring-sixth-sense**: One-time interactive setup — configures model preferences and effort levels for Sixth Sense subagents.
- **crossroad-stack**: Use before applying test-driven-development, diagnosing-bugs, or requesting-code-review to detect whether the task targets Java/Spring Boot backend, Angular, React, Next.js, Pyt…
- **diagnosing-bugs**: Use when encountering bugs, test failures, or unexpected behavior — replaces random fixes with a disciplined, hypothesis-driven diagnosis loop.
- **dispatching-parallel-agents**: Use when facing multiple independent tasks that can be worked on without shared state or sequential dependencies — dispatches specialized subagents with Effort Routing, batching…
- **domain-modeling**: Build and sharpen a project's domain model — pin down terminology, record architectural decisions, maintain CONTEXT.md and ADRs.
- **dylan-dog**: The nightmare investigator — hunts edge cases and runs premortems on failure modes.
- **managing-development-branches**: Covers the full lifecycle of a development branch — creating an isolated git worktree with systematic safety checks, resolving an in-progress merge/rebase conflict by intent, an…
- **requesting-code-review**: Use when completing tasks, implementing features, or before merging — dispatches Dylan Dog (edge-case hunting) and processes feedback with technical rigor, not performative agre…
- **roundtable**: Put the user's plan or design through a relentless round of questioning until a shared understanding is reached.
- **specifying-and-implementing**: Turn the current conversation into a structured spec document, then implement it — orchestrates TDD, typechecking, code review, and commit.
- **test-driven-development**: Use when implementing a feature or fixing a bug.
- **using-sixth-sense**: Use when starting any conversation — establishes how to find and use skills, and platform adaptation.
- **verification-before-completion**: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs — requires running verification commands and confirming output before making any s…

### skill-campfire [off] (1 skills)

- **campfire**: The Campfire — a social hangout where all of the user's installed skills come alive as distinct characters with personalities, voices, and relationships.

### skill-discovery [off] (1 skills)

- **inventory**: Inventory the AI-agent skills and standing instruction files installed on this machine.

### skill-doctor [off] (3 skills)

- **rollback**: Restore skills from the last skill-doctor backup.
- **skill-doctor**: Audit and improve your Claude Code skills and agents.
- **treat**: Apply skill-doctor diagnosis by building upgraded skills in a staging directory for testing.

### skill-gate [off] (1 skills)

- **focus-guard**: Use when the user wants to gate, block, restrict, guard, or require confirmation before specific skills run, or to manage which skills are gated.

### skill-provenance [off] (5 skills)

- **bootstrap**: Add version tracking to an existing unversioned skill bundle.
- **close**: Update version tracking when finishing work on a skill bundle.
- **handoff**: Generate a handoff note summarizing skill project state for a future session or collaborator.
- **open**: Verify a skill bundle's integrity when opening a project.
- **validate**: Run a focused validation check for a skill bundle.

### skill-reviewer [off] (1 skills)

- **skill-reviewer**: Use when reviewing a Claude Code skill, auditing skill quality before publish, or asking \"is this skill any good?\".

### skillcheck-free [off] (1 skills)

- **skill-check**: Validate Claude Code skills against Anthropic guidelines.

### skillers [off] (2 skills)

- **recommend**: Use when turning skillers knowledge into automation suggestions, choosing between a hook, a skill and an agent for a recurring pattern, or writing a scaffold spec for one.
- **skillers-compact**: Use when compacting AI coding session transcripts into skillers knowledge, or when writing skillers observations.

### skillkeel-starter [off] (8 skills)

- **changelog**: Use when the user asks to update or generate CHANGELOG.md, prepare release notes, or cut a version.
- **claude-md-init**: Use when a repo has no CLAUDE.md, or the user asks to create/refresh CLAUDE.md or project instructions for Claude Code.
- **commit-message**: Use when the user asks to commit, write a commit message, or stage-and-commit changes.
- **dependency-audit**: Use when the user asks to check dependencies for vulnerabilities, outdated packages, or before a release.
- **pr-description**: Use when the user asks to open a pull request, write a PR description, or summarise a branch for review.
- **readme-refresh**: Use when the user asks to update, fix, or audit README.md, or when README commands look stale.
- **secret-audit**: Use when the user asks whether secrets were committed, before open-sourcing a repo, or after a leak scare.
- **test-gap-finder**: Use when the user asks what to test next, where coverage is weak, or before a refactor of untested code.

### skillquiver [off] (24 skills)

- **automate-ui**: Automates web and desktop UIs while capturing evidence that separates navigation from verified behavior.
- **brainstorming**: Explores user intent, requirements, and design before implementation.
- **communicate-clearly**: Controls report length while preserving evidence and explains external sources without overstating them.
- **design-ui**: Builds accessible interfaces and verifies renders.
- **diagnose-systematically**: Finds root causes through reproduction and falsifiable experiments.
- **dispatching-parallel-agents**: Dispatches one subagent per independent problem.
- **engineer-prompts**: Builds or audits testable prompt contracts with explicit outcomes, permissions, tools, evidence, and stop conditions.
- **execute-durably**: Runs long or interruption-prone work from a durable state file with falsifiable criteria and evidence.
- **executing-plans**: Executes a written implementation plan inline, task by task, stopping only on blockers.
- **finishing-a-development-branch**: Guides integration of a finished branch: verify tests, present merge/PR/keep/discard options to the user, and clean up worktrees.
- **handle-host-boundaries**: Handles unavailable named capabilities and destructive filesystem roots.
- **improve-agent-instructions**: Audits and safely updates scoped AGENTS.md and CLAUDE.md guidance for Claude Code and Codex.
- **receiving-code-review**: Verifies code review feedback before implementation and pushes back with evidence when a claim is wrong.
- **refactor-safely**: Refactors working or legacy code without changing observable behavior, using characterization tests when needed.
- **requesting-code-review**: Dispatches a bounded reviewer and preserves verified findings.
- **research-systematically**: Runs source-bound research and version-matched documentation lookup.
- **skillquiver-doctor**: Audits the current ChatGPT, Claude Code, or Codex host for conflicting skills, plugins, and persistent hooks, then offers reversible per-item repairs.
- **solve-efficiently**: Routes multi-module work with progressive discovery, matched effort, and context economy.
- **subagent-driven-development**: Executes an implementation plan by dispatching one subagent per task with per-task review gates, keeping the orchestrator's context small.
- **test-driven-development**: Runs a recorded red-green-refactor cycle.
- **using-git-worktrees**: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or gi…
- **verification-before-completion**: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs; requires running verification commands and confirming output before making any su…
- **verify-work**: Independently audits finished work — verifies a delivery or completion claim against real evidence.
- **writing-plans**: Creates implementation plans with interfaces, tests, and open decisions.

### skills-updater [off] (1 skills)

- **skills-updater**: Use when the user wants to check for plugin/skill updates, audit installed versions, or update Claude Code plugins to their latest versions.

### smart-commits [off] (1 skills)

- **smart-commits**: Use when committing changes, to write a clear conventional commit message from the staged diff.

### socratic-mentor [off] (1 skills)

- **socratic-mentor**: Turns Claude into a Socratic tutor for the rest of the session — it never gives the answer directly or makes changes for the user; it explains why and where, guides with hints a…

### source-of-truth [off] (1 skills)

- **source-of-truth**: Use in a project that has a docs/overview.md spec catalog, or when the user asks to set one up: before writing, modifying, or deleting production code in that project (refactors…

### sourcegraph [off] (1 skills)

- **searching-sourcegraph**: Use when the user needs to search or navigate code with Sourcegraph MCP tools.

### spec-drift [off] (2 skills)

- **drift-detection**: Compares the requirements recorded in SPEC_CHECKLIST.md against the actual files in the working directory and reports requirement drift.
- **requirement-extraction**: Extracts an explicit requirement checklist from a user's task request and writes it to SPEC_CHECKLIST.md so it can be verified later.

### spec-driven-dev [off] (3 skills)

- **implement-plan**: Execute a reviewed implementation plan step by step with verification and standards review
- **small-change**: Make a small change in the main session, then review it through isolated fact, standards and final passes
- **write-plan**: Discuss a feature, draft an implementation plan, and review it through isolated passes

### sth [off] (2 skills)

- **sth-library**: Use when the user asks for a prompt, agent, skill, rule, command or workflow the team may already have — "do we have a prompt for X", "find our cold email prompt", "reuse the co…
- **sth-transfer**: Use when moving or converting an agent, command, instruction, rule, skill or workflow between AI coding tools — "port this skill to Codex", "does this rule work in Cursor", "mak…

### supabase-expert [off] (1 skills)

- **supabase**: This skill should be used when the user is working with Supabase, mentions PostgreSQL with Supabase, Row Level Security (RLS), Supabase Auth, Supabase Storage, supabase CLI, dat…

### superdevflow [off] (5 skills)

- **clone**: Clone the current conversation so the user can branch off and try a different approach.
- **gha**: Analyze GitHub Actions failures and identify root causes
- **half-clone**: Clone the later half of the current conversation, discarding earlier context to reduce token usage while preserving recent work.
- **handoff**: Write or update a handoff document so the next agent with fresh context can continue this work.
- **review-claudemd**: Review recent conversations to find improvements for CLAUDE.md files.

### sync-docs [off] (1 skills)

- **sync-docs**: Use when the user asks to update docs, sync documentation, fix stale docs or update the changelog, or after code changes that may affect docs.

### system-design-skills [off] (22 skills)

- **api-design**: This skill should be used when the user needs to "design the API", do "endpoint design", pin down a "request/response shape", choose a "pagination" strategy (cursor vs offset), …
- **architecture-diagram**: This skill should be used when a system design needs a diagram — "draw the architecture", "diagram this system", "show the components", "make an architecture/infrastructure/topo…
- **back-of-the-envelope**: This skill should be used when the user needs to "estimate QPS", "back-of-the-envelope" (BOTEC) numbers, "how much storage / bandwidth", "how many servers", "peak load", "capaci…
- **blob-store**: This skill should be used when the user wants a "blob store" or "object storage", names "S3" or an S3-compatible store, needs to "store images / video / files", asks about "mult…
- **caching**: This skill should be used when the user asks about a "caching strategy", "cache invalidation", "what to cache", "read-through vs write-through vs write-back", "cache eviction" (…
- **consistency-coordination**: This skill should be used when the user asks about the "CAP theorem", "PACELC", a "consistency model", "eventual vs strong consistency", "read-your-writes", "causal consistency"…
- **content-delivery**: This skill should be used when the user asks about a "CDN", "edge caching", "static asset delivery", "media / video delivery", "geo distribution of content" or "edge POP selecti…
- **data-storage**: This skill should be used when the user asks "SQL or NoSQL", "which database", how to design a "data model" or "schema design", picks an "indexing" strategy, needs "sharding" or…
- **distributed-logging**: This skill should be used when the user designs "distributed logging", "log aggregation", "centralized logs", an "ELK" or "EFK" stack, "log shipping", "structured logging", a "c…
- **distributed-search**: This skill should be used when the user designs a "search system", needs "full-text search", asks about an "inverted index", "Elasticsearch / OpenSearch", "relevance ranking" (T…
- **dns**: This skill should be used when the user asks about "DNS", "domain resolution", "GeoDNS / geo routing", "latency-based routing", "weighted / failover routing", "Route 53 / Cloud …
- **load-balancing**: This skill should be used when the user adds a "load balancer", asks about "L4 vs L7" (transport vs application layer), picks a balancing algorithm ("round robin", "least connec…
- **messaging-streaming**: This skill should be used when the user designs a "message queue", reaches for "Kafka", "RabbitMQ", "SQS", "Kinesis", "pub/sub", or "event-driven" architecture, asks about "asyn…
- **observability**: This skill should be used when the user asks about "observability" or "monitoring", what "metrics, logs, and traces" to collect, "health checks" (liveness/readiness), "alerting"…
- **requirements-scoping**: This skill should be used when the user needs to "clarify requirements", separate "functional vs non-functional requirements", "scope the problem", figure out "what questions sh…
- **resilience-failure**: This skill should be used when the user asks about "fault tolerance", "resilience", a "circuit breaker", "graceful degradation", "retry storm" or "thundering herd on recovery", …
- **scaling-evolution**: This skill should be used when the user asks "how does this scale", "scale to millions", "scaling roadmap", "where is the bottleneck", "what breaks first", "10x growth", "vertic…
- **sequencer**: This skill should be used when the user needs a "unique ID generator", "distributed IDs", a "Snowflake ID", asks "UUID vs auto-increment", wants a "time-sortable ID", a "monoton…
- **service-decomposition**: This skill should be used when the user asks "monolith vs microservices", how to "split into services", set "service boundaries", find the right "service granularity", design an…
- **sharded-counters**: This skill should be used when the user needs a "sharded counter", "distributed counter", to "count likes / views at scale", handles a "high-write counter" or "hot counter conte…
- **system-design**: This skill should be used when the user asks to "design a system", "design <a product>" (e.g.
- **task-scheduling**: This skill should be used when the user designs a "task scheduler", "job scheduler", "job queue", "cron at scale", "distributed cron", "delayed / scheduled / recurring tasks", a…

### theboardroom [off] (1 skills)

- **theboardroom**: Convene an AI executive board of directors (CEO, CFO, COO, CLO, CISO sub-agent personas) to vet a business idea, product concept, new service offering, M&A target, or operationa…

### tldr [off] (2 skills)

- **tldr**: Compress output without losing it: lead with a three-line TL;DR, keep the full detail directly underneath, and compress agent-to-agent reports to a parseable block.
- **tldr-write**: Write messages people actually read: the ask first, the padding gone.

### tmux-status [off] (1 skills)

- **tmux-icons**: Switch tmux status icon themes or customize individual icons for the claude-tmux-status plugin.

### tool-schemas [off] (4 skills)

- **tool-contract-audit**: Find why a connected AI agent tool picks the wrong action, gets wrong arguments or gives misleading results.
- **tool-contract-check**: Check an existing AI agent tool contract against real calls so wrong arguments and misleading results are visible.
- **tool-interface-repair**: Repair an existing AI agent tool schema and description for wrong tool choices and invalid arguments.
- **tool-result-repair**: Fix structured tool output and tool error handling so an AI agent can tell success, no match and failure apart.

### tts [off] (1 skills)

- **tts**: Control shared agent text-to-speech (on/off/mode/stop/skip/pause/resume/status/voices)

### turbocharge [off] (10 skills)

- **atlas**: Generate or update a semantic domain map (ATLAS.md) for the project.
- **brainstorm**: Use when starting creative work - creating features, building components, adding functionality, or modifying behavior.
- **build**: Use when you have an implementation plan ready to execute.
- **debug**: Use when encountering any bug, test failure, or unexpected behavior.
- **plan**: Use when you have stories or clear requirements that need to become an implementation plan with bite-sized tasks, exact file paths, complete code, and verification commands.
- **review**: Use before merging to verify completed work meets requirements and quality standards.
- **setup**: Run once after installing turbocharge.
- **ship**: Use when implementation and review are complete and you need to integrate the work.
- **story**: Use when you have requirements, PRDs, or feature descriptions that need to become implementable work.
- **wrap**: Use when ending a session, taking a break, or context is getting full.

### turbocharge [off] (3 skills)

- **customize-plugin**: Use when you want to implement a customization in your target repo — describe the desired change and have it applied with the intent recorded.
- **setup-plugin-customization**: Use when setting up or reconfiguring a plugin customization workspace — cloning an upstream plugin source, linking a target repo, and writing .turbocharge/settings.json to the t…
- **sync-plugin-customizations**: Use when running a scheduled check for upstream plugin release updates — fetches the latest tagged release, merges into the target repo, uses agent-assisted conflict resolution …

### ui-color-palette [off] (53 skills)

- **gh-cli**: GitHub CLI (gh) comprehensive reference for repositories, issues, pull requests, Actions, projects, releases, gists, codespaces, organizations, extensions, and all GitHub operat…
- **gitlab-cli-skills**: Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations via terminal.
- **glab-alias**: Create, list, and delete GitLab CLI command aliases and shortcuts.
- **glab-api**: Make direct GitLab REST API calls for advanced queries and operations not covered by other glab commands.
- **glab-attestation**: Work with GitLab attestations for software supply chain security including artifact verification and provenance.
- **glab-auth**: Manage GitLab CLI authentication including login/logout, check auth status, switch accounts, and configure Docker registry access.
- **glab-changelog**: Generate changelogs from GitLab releases, tags, and commits.
- **glab-check-update**: Check for glab CLI updates and view latest version information.
- **glab-ci**: Work with GitLab CI/CD pipelines, jobs, and artifacts.
- **glab-cluster**: Manage GitLab Kubernetes clusters and agent integrations.
- **glab-completion**: Generate shell completion scripts for bash, zsh, fish, or PowerShell.
- **glab-config**: Manage glab CLI configuration settings including defaults, preferences, and per-host settings.
- **glab-deploy-key**: Manage SSH deploy keys for GitLab projects including add, list, and delete operations.
- **glab-duo**: Interact with GitLab Duo AI assistant for code suggestions and chat.
- **glab-gpg-key**: Manage GPG keys for commit signing including add, list, and delete operations.
- **glab-help**: Display help information for glab commands and subcommands.
- **glab-incident**: Manage GitLab incidents for issue tracking and incident management.
- **glab-issue**: Create, view, update, and manage GitLab issues.
- **glab-iteration**: Manage GitLab iterations for project planning and sprint management.
- **glab-job**: Work with individual CI/CD jobs including view, retry, cancel, trace logs, and download artifacts.
- **glab-label**: Manage GitLab labels including create, list, update, and delete operations at project and group level.
- **glab-mcp**: Work with Model Context Protocol (MCP) server for AI assistant integration.
- **glab-milestone**: Manage project milestones including create, list, update, view, and close operations.
- **glab-mr**: Create, view, manage, approve, and merge GitLab merge requests.
- **glab-opentofu**: Work with OpenTofu state management in GitLab.
- **glab-quick-actions**: Use GitLab quick actions — text-based slash commands in comments, descriptions, and MR/issue bodies — via glab CLI.
- **glab-release**: Manage GitLab releases including create, list, view, delete, download, and upload release assets.
- **glab-repo**: Work with GitLab repositories and projects including clone, create, fork, archive, view, update, delete, search, transfer, and member management.
- **glab-runner**: Manage GitLab CI/CD runners — list, assign, unassign, inspect recent jobs and managers, pause/unpause via update, and delete runners at project, group, or instance level.
- **glab-runner-controller**: Manage GitLab runner controllers and authentication tokens.
- **glab-schedule**: Manage CI/CD pipeline schedules including create, list, update, delete, and run scheduled pipelines.
- **glab-securefile**: Manage secure files for CI/CD including upload, download, list, and delete operations.
- **glab-snippet**: Create, view, update, and manage GitLab code snippets (gists).
- **glab-ssh-key**: Manage SSH keys for GitLab account including add, list, and delete operations.
- **glab-stack**: Manage stacked merge requests for complex multi-part changes.
- **glab-todo**: Manage your GitLab to-do list from the CLI, including listing pending or completed items and marking items done.
- **glab-token**: Manage GitLab personal access tokens and project access tokens.
- **glab-user**: View and manage GitLab user information including profile, events, and SSH keys.
- **glab-variable**: Manage CI/CD variables at project and group level including create, update, list, and delete operations.
- **glab-version**: Display glab CLI version information and build details.
- **glab-workitems**: List and manage GitLab work items (tasks, OKRs, key results, epics).
- **ui-color-palette-audit-palette**: Audit color pairs for contrast compliance against WCAG 2.1 and APCA standards.
- **ui-color-palette-build-color-system**: Define a semantic color system taxonomy and resolve bindings against a palette using get_color_system.
- **ui-color-palette-figma**: Entry point for UI Color Palette workflows targeting Figma.
- **ui-color-palette-framer**: Entry point for UI Color Palette workflows targeting Framer.
- **ui-color-palette-generate-code**: Export palette configuration as code or design tokens via the generate_code MCP tool using base and themes.
- **ui-color-palette-generate-semantic-code**: Generate semantic code files alongside primitives by passing a color system configuration to generate_code.
- **ui-color-palette-generate-source-colors**: Generate source colors to seed a palette.
- **ui-color-palette-help**: Display a quick-start guide and list all available commands.
- **ui-color-palette-manage-palettes**: Browse, publish, share, update, and delete palettes on the UI Color Palette platform.
- **ui-color-palette-penpot**: Entry point for UI Color Palette workflows targeting Penpot.
- **ui-color-palette-scale-palette**: Build a full color palette from source colors.
- **ui-color-palette-sketch**: Entry point for UI Color Palette workflows targeting Sketch.

### ultrapowers-dev [off] (55 skills)

- **API Design**: Use when designing REST APIs, choosing URL structures, handling errors in responses, implementing pagination, or planning API versioning.\n
- **Agent Loop**: Use when a task requires autonomous multi-step reasoning with tool calls, where the number of steps is not known in advance.
- **Angular Patterns**: Use when building frontend applications with Angular — covers components, services, dependency injection, signals, standalone components, and testing.
- **Architecture**: Use when making system-level architecture decisions, choosing between monolith and microservices, selecting architectural patterns, or designing system boundaries.\n
- **Auth & Security**: Use when implementing authentication, authorization, or security controls — covering identity, access, and defense against common vulnerabilities.
- **Background Jobs**: Use when designing task queues, async workers, or event-driven processing that runs outside the request-response cycle.
- **C# Best Practices**: Use when writing or reviewing C# code.
- **C/C++ Best Practices**: Use when writing or reviewing C/C++ code.
- **CI/CD**: Use when designing continuous integration and deployment pipelines — covering stages, deployment strategies, rollback, and pipeline performance.
- **Caching**: Use when adding caching to a system, choosing cache strategies, designing invalidation logic, or diagnosing cache-related bugs.\n
- **DAG Workflows**: Use when a multi-step process has dependencies between steps, some of which can run in parallel, with shared state and conditional routing.
- **Dart Best Practices**: Use when writing or reviewing Dart code.
- **Database Design**: Use when designing schemas, writing migrations, optimizing queries, choosing indexes, or deciding between normalization and denormalization.\n
- **Design Patterns**: Use when making structural design decisions, applying SOLID principles, choosing between inheritance and composition, or deciding when to introduce an abstraction.\n
- **Django Patterns**: Use when building Python web applications with Django — covers models, views, ORM, migrations, admin, Django REST Framework, and testing.
- **Error Handling**: Use when designing error handling strategies, choosing between exceptions and result types, validating inputs, or building resilient systems in any language.\n
- **Express Patterns**: Use when building Node.js web servers with Express — covers middleware chains, routing, error handling, security, and testing.
- **FastAPI Patterns**: Use when building Python APIs with FastAPI — covers async endpoints, dependency injection, Pydantic models, middleware, and testing.
- **Flask Patterns**: Use when building Python web applications with Flask — covers blueprints, extensions, application factory, context management, and testing.
- **Go Best Practices**: Use when writing or reviewing Go code.
- **Java Best Practices**: Use when writing or reviewing Java code.
- **JavaScript Best Practices**: Modern JavaScript patterns for non-TypeScript projects covering ES2024+ idioms, tooling, and common pitfalls
- **Kotlin Best Practices**: Use when writing or reviewing Kotlin code.
- **Laravel Patterns**: Use when building PHP web applications with Laravel — covers Eloquent ORM, middleware, queues, Blade templates, Livewire, and testing.
- **Multi-Agent Debate**: Use when a decision benefits from adversarial perspectives, where a single LLM call might be biased or miss edge cases.
- **Multi-Agent Handoffs**: Use when a conversation spans multiple domains and should be routed between specialized agents based on context.
- **NestJS Patterns**: Use when building Node.js backends with NestJS — covers modules, controllers, providers, pipes, guards, interceptors, and testing.
- **Next.js Patterns**: Use when building or reviewing Next.js applications.
- **Observability**: Use when instrumenting systems with structured logging, metrics, and distributed tracing to achieve production visibility.
- **Orchestrator-Workers**: Use when a complex task can be decomposed into subtasks that benefit from specialized prompts or models.
- **PHP Best Practices**: Use when writing or reviewing PHP code.
- **Parallelization**: Use when the same input needs multiple independent analyses, or the same task should be run multiple times for voting or redundancy.
- **Plugin Development**: Use when creating, structuring, validating, or publishing Claude Code plugins and self-hosted marketplaces — covers plugin.json manifests, skill authoring, marketplace setup, ve…
- **Python Best Practices**: Use when writing or reviewing Python code.
- **RAG & AI Retrieval**: Use when building retrieval-augmented generation pipelines — covering chunking, embeddings, vector search, and reranking for grounded LLM responses.
- **Rails Patterns**: Use when building Ruby on Rails applications — covers convention over configuration, ActiveRecord, concerns, jobs, and testing.
- **Ratatui Patterns**: Use when building terminal user interfaces with ratatui — covers app architecture (Elm/TEA), async event loops with crossterm EventStream, PTY rendering with tui-term, terminal …
- **React Patterns**: Canonical patterns for React applications covering component design, hooks, state management, and data fetching
- **Resilience**: Use when building systems that must survive transient failures, network partitions, and downstream service degradation.
- **Ruby Best Practices**: Use when writing or reviewing Ruby code.
- **Rust Best Practices**: Use when writing or reviewing Rust code.
- **SQL Best Practices**: Use when writing or reviewing SQL queries.
- **Spring Boot Patterns**: Use when building or reviewing Spring Boot applications.
- **Supabase Patterns**: Use when building with Supabase.
- **Swift Best Practices**: Use when writing or reviewing Swift code.
- **Tailwind Patterns**: Use when building UIs with Tailwind CSS.
- **Testing & TDD**: Use when writing tests, practicing test-driven development, designing test suites, or deciding what and how to test in any language or framework.\n
- **Tool Calling**: Use when an LLM needs to interact with external systems, APIs, or data sources through structured function calls.
- **Type Safety**: Use when leveraging type systems to prevent bugs at compile time — covering generics, contracts, narrowing, and using types as documentation.
- **TypeScript Best Practices**: Use when writing or reviewing TypeScript code.
- **browser-automation**: Use when an AI agent needs to interact with websites — navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, or automating any browser task
- **e2e-testing**: Use when writing end-to-end UI tests, setting up Playwright or Cypress, or debugging flaky tests — covers test structure, selectors, waiting strategies, and CI integration
- **frontend-design**: Use when building web components, pages, or applications — guides creation of distinctive, production-grade frontend interfaces that avoid generic AI aesthetics
- **react-best-practices**: Use when writing, reviewing, or refactoring React/Next.js code — 62 performance optimization rules across 8 categories, prioritized by impact
- **web-design-guidelines**: Use when asked to review UI code, check accessibility, audit design, review UX, or check a site against best practices

### ux-superpowers [off] (8 skills)

- **insight-synthesizer**: Trigger whenever the user says \"compile the discovery doc\", \"synthesize everything into one document\", \"write the UX discovery document\", \"produce the final discovery art…
- **jobs-to-be-done**: Trigger this skill whenever the user asks \"what are users actually trying to do\", \"what jobs are users hiring this for\", \"what's the underlying user motivation\", \"let's d…
- **persona-builder**: Build me a persona for the primary user of this system, who are the users of this product, define the user types, let's flesh out the persona for the admin role, create a primar…
- **research-intake**: Whenever the user hands you raw user-research artifacts — interview transcripts, survey results, NPS verbatims, support tickets, app store reviews, usability test notes, forum/c…
- **telemetry-designer**: Use when the user asks how to measure product or feature success, define success metrics, pick a north star metric, track KPIs, design analytics events, build an instrumentation…
- **user-journey**: Use when mapping the end-to-end user experience for any software product, including CLI tools, APIs, SDKs, infrastructure, and other non-visual interfaces that most journey-mapp…
- **ux-discover**: Use BEFORE writing any code, planning, or brainstorming.
- **ux-validate**: Trigger whenever reviewing a PR, code change, or feature for shipping readiness and a UX Discovery Document exists at docs/ux-discovery/ — always invoke on phrases like \"review…

### whats-new [off] (5 skills)

- **configure**: Set how aggressively whats-new suggests features.
- **discover**: Find Claude Code features relevant to what you're working on.
- **learn-more**: Get a detailed walkthrough of the feature of the day or any specific feature by name.
- **list**: Browse and filter all Claude Code features by category, tag, or status.
- **surprise-me**: Get a random Claude Code feature explained in a fun, conversational way.

### whodb [off] (3 skills)

- **query-builder**: Convert natural language questions into SQL queries.
- **schema-designer**: Help design database schemas, create tables, and plan data models.
- **whodb**: Database operations including querying, schema exploration, and data analysis.

### wiki-wonka [off] (3 skills)

- **ingest**: Add new sources to the wiki, creating and updating pages as needed.
- **lint**: Scan the wiki for structural, factual, and navigational problems — and fix what you can, flag what you cannot.
- **query**: Answer questions by reading and synthesizing information from the wiki.

### wizard [off] (12 skills)

- **building-a-discipline-spell**: Use when the meta-builder routes to kind=discipline.
- **building-a-spell**: Use when the user wants to capture a repeatable task as a reusable spell, or asks "how do I build a workflow / skill / framework for X
- **building-a-subagent-spell**: Use when the meta-builder routes to kind=subagent.
- **building-a-workflow-spell**: Use when the meta-builder routes to kind=workflow.
- **chaining-spells**: Use when composing multiple spells into a chain that runs end-to-end (e.g.
- **discovering-spells**: Use when browsing what spells are available - bundled seeds, your personal library, or both.
- **inferring-a-spell-from-examples**: Use when the user invokes /capture-this-chat or /build-spell --from-transcript.
- **intuitive-interviewing**: Use when conducting any interview-style flow with a user (building a spell, refining one, gathering requirements).
- **pressure-testing-a-spell**: Use during try-it for kind=discipline spells.
- **refining-a-spell**: Use when an existing spell needs improvement based on usage.
- **sharing-a-spell**: Use when exporting a spell for someone else to use.
- **using-wizard**: Use when starting any conversation - establishes how to find and use Wizard skills and spells, including the 1% rule

### workflow-toolkit [off] (21 skills)

- **contribution-check**: Pre-flight checklist for open source contributions.
- **create-agent**: Creates a new Claude Code custom subagent configuration.
- **create-skill**: Creates a new Claude Code custom skill (slash command).
- **db-viewer**: Open the journal SQLite database in a GUI viewer (DB Browser for SQLite, or similar).
- **distill-concept**: Distills a codebase concept into a structured knowledge base entry.
- **help**: Show usage information for any workflow-toolkit skill.
- **issues-list**: List and filter tracked GitHub issues from the local SQLite database.
- **issues-sync**: Sync GitHub issues from the repo into the local SQLite database for tracking.
- **issues-triage**: Update the local tracking metadata for a GitHub issue.
- **issues-view**: View detailed information about a specific GitHub issue.
- **journal-read**: Read and query journal entries.
- **journal-write**: Write a journal entry documenting what was done in this session.
- **pr-prepare**: Prepares a pull request description.
- **skill-and-agent-factory**: Creates skills, agents, or both together.
- **task-create**: Create a new task with a title and optional description, priority, tags, and linked GitHub issue.
- **task-done**: Mark a task as done.
- **task-list**: List and filter local tasks from SQLite.
- **task-start**: Mark a task as in-progress.
- **task-update**: Update a task's field (status, priority, tags, notes, description).
- **task-view**: View full details of a specific task by ID or slug, including its TASK.md contents.
- **workflow-db-setup**: Initialize and verify the workflow-toolkit environment.

### worktree-workspace [off] (4 skills)

- **worktree-add**: Create a complete git worktree workspace with nested repos and gitignored config files.
- **worktree-help**: Display usage information and examples for all worktree-workspace commands.
- **worktree-list**: List all workspaces created by worktree-add for the current repo, showing branch names and nested repos.
- **worktree-remove**: Remove a workspace created by worktree-add, cleaning up all nested worktrees.

## C. Plugins with no skills: 105

agent-smith (ON), cache-ttl-timer (ON), clawd-pet (ON), code-review (ON), context7 (ON), github (ON), harness-scope (ON), jev (ON), jevmem (ON), playwright (ON), searchoclock (ON), (unnamed .staging) (off), agent-recall (off), ai-memory-reader (off), airquote (off), audit (off), better-compact (off), build-companion (off), burn-baby-burn (off), cache-caffeine (off), cc (off), cc-limit-pacer (off), cc-notify (off), cc-terminal-notifier (off), ccoverhead (off), chat-autoexporter (off), chat-search (off), claude-activity (off), claude-bell (off), claude-code-audit-stack (off), claude-code-cost (off), claude-code-notify (off), claude-code-toolkit (off), claude-eta (off), claude-md-optimizer (off), claude-notify (off), claude-notify-resume (off), claude-pace (off), claude-pulse (off), claude-sqlite-plugin (off), claude-tab-fix (off), claude-time (off), claude-usage-statusline (off), claude-vitals (off), claude-war-room (off), claudedesktiop (off), claudemeter (off), claudinator (off), cloud-sql-mysql (off), cloud-sql-postgresql (off), cloud-sql-sqlserver (off), code-modernization (off), code-simplifier (off), compact-on-idle (off), context-keep (off), context-window (off), crayon (off), crew (off), cync (off), dev-env-doctor (off), dev-forge (off), dev-squad (off), feature (off), firebase (off), fortune-cookie (off), gdrive-to-markdown (off), graph-indexer (off), graph-query-mcp (off), handoff-doc (off), harness-architect (off), human-in-the-loop (off), idle-compact (off), idle-timing (off), impact-analysis (off), internet-tools (off), invaders (off), keep-awake (off), llm-dark-patterns (off), mcp-image-viewer (off), mcp-tunnels (off), md-linker (off), md-prompt (off), memex (off), memory-agent (off), neocode (off), notify (off), notify-sounds (off), oak-memory (off), plan-review (off), project-boundary (off), project-review (off), promptcolor (off), relay (off), resumenext-resume-bullet-points (off), scaffold (off), senior-engineering-partner (off), skill-validator (off), supalens (off), toolrouter (off), ultrasolve (off), usage-bars (off), watch-video (off), wherewasi (off), why-is-my-claude-dumb (off), whydone (off)
