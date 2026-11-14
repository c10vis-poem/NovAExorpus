# The 365 synced plugins: what to keep and why (2026-10-30)

**Recommendation: keep 119 and cut 246.** That's inside your 80 to 120 target. Every one of the 365 is listed below, and each cut has a reason.

**How I judged them.** I read each plugin's own description and its list of parts (skills, commands, agents, hooks and MCP). I didn't open every script; only agent-ingest-audit-optimize has had a full deep read. I judged each plugin on its parts, not on whether it has hooks.

For your goals, I used what's in project memory: the agentic OS, multi-tier memory, memory-as-skill, wiki-admin, web tools, Gemini CLI, reverse engineering, Jetpack Compose APKs on Android, voice (speech-to-text and text-to-speech), your own marketplace, and the standing rules.

**The most common cut reason** is overlap. Where 5 plugins do one job, I kept the strongest one or two and named the winner in each cut reason.

**Changes from what's switched on today:**
- Turn off 1: clawd-pet.
- Turn on 94 plugins that are currently off (all marked "keep" below).
- Leave 2 plugins on but change one hook each:
  - claude-context-optimizer: turn off the `read-cache.js` hook, the only hook that can block a file read.
  - superpowers: turn off the SessionStart injection that says "MUST invoke skills".
- 9 plugins are switched on in settings but have no files here: agent-engineering, agent-protocols, agentkeeper, akc-cycle, context-bar, gas-gauge, hookify, maddog, supabase. They're outside the 365, so they aren't judged here. Check them in your account.

---

## 1. Keep (119), by category

### Memory (13)

- **adaptive-agent**: Skill self-improvement and user profiling. This is the feedback loop memory-as-skill needs.
- **agent-recall**: A SQLite knowledge graph plus MCP tools. It gives you the graph tier of your memory layers.
- **anchor-memory**: A verifiable ledger memory with integrity checks. It answers "the last session didn't know anything".
- **ccfind**: Full-text search across past sessions. It digs up old RESUME and handoff conversations.
- **chat-autoexporter**: Exports each conversation as text before compaction and at session end, so your memory corpus gets fed.
- **claude-patterns**: Turns recurring patterns from sessions into rule and skill captures. It feeds the rulebook with your approval.
- **compounded**: Learns rules from your corrections only with your approval, and skills earn trust step by step.
- **jevmem **(on now)****: Already on. Saves decisions and rules to JEVMEM.md. It needs the jevmem CLI.
- **memory-agent**: Compiles sessions into a Markdown knowledge base you own, with provenance and conflict tracking.
- **memory-toolkit **(on now)****: Already on. Workstreams, handoff and session memory.
- **pmm **(on now)****: Already on. A git-backed flat-file memory.
- **remember**: Compresses conversations into tiered daily logs, the time-based tier of your memory.
- **whydone**: A decision log committed to the repo (what and why) that survives a git clone. It's the decisions tier.

### Handoff (2)

- **context-handoff #1**: Saves context automatically before compaction or a stop, writes handoff manifests and makes them searchable.
- **handoff #1**: Per-branch handoff notes that load into the next session on the same branch.

### Context (4)

- **better-compact**: Steers every compaction to keep the goal, next step, files and decisions. It fights memory loss directly.
- **claude-context-optimizer **(on now)****: Already on. Keep the reports and the task state, but turn off its read-cache hook, which blocks re-reading files.
- **context-window**: A pane listing everything that entered the context, so you can see what hooks inject.
- **headroom**: Outline-first reading of huge logs, docs, JSON and CSV. It keeps corpus work from flooding the context.

### Usage (5)

- **burn-baby-burn**: The signal for the Burn Planner. Within 72h of the weekly reset with 25%+ left, it flags unspent usage so a pre-approved big job can run (see burn-planner-proposal).
- **cache-guard**: Warns before an expensive message after the cache expired, and offers a cheap handoff instead.
- **cache-ttl-timer **(on now)****: Already on. A cache countdown in the footer.
- **claude-code-cost**: Spend in USD per project, branch and day, read from local logs.
- **heavy-usage**: Shows real 5-hour and weekly limits and winds down cleanly (commit, then stop) before the wall.

### Rules (5)

- **bake-claude-md-files**: Turns CLAUDE.md rules into automated checks. It fits your rulebook rewrite.
- **chuck**: Injects only the rules relevant to each prompt and flags contradictions. A candidate router for your new rulebook.
- **claude-md-management **(on now)****: Already on. Official CLAUDE.md audit and upkeep.
- **claude-perfectionist**: Grades the whole harness: CLAUDE.md, rules, hooks, skills, settings and MCP. It's the audit you're doing by hand.
- **instructions-cleanup**: Fixes conflicting CLAUDE.md and AGENTS.md rules with a minimal patch, like the contradiction in Aesop-Xi's MEMORY.md.

### Discipline (4)

- **frontier-simplify**: Cuts made-up process and caps repeated reviews for frontier models. It counters over-engineered workflows.
- **loop-and-gate-build-kit**: Human decision gates for an agent loop. It encodes "no building without my direction".
- **no-cape**: Lean rules for frontier models: escalate, don't thrash; fail loudly; verify before saying done. A slimmer superpowers replacement.
- **superpowers **(on now)****: Already on. Keep the skills, but turn off its SessionStart hook that injects "MUST invoke skills".

### Verification (5)

- **claude-code-audit-stack**: A claim auditor plus deploy verifier. It catches fake success and made-up stats in reports.
- **claude-eta**: Detects repair loops (the burning failure loops you named) and calibrates time estimates.
- **colosseum**: Adversarial review grounded in web search, where only verified quotes count. It fights made-up citations.
- **llm-dark-patterns**: Keep it as a parts donor. Its 30 dark-pattern checks (false success, fake recall, fake citations) are exactly your complaints. Turn its blocking Stop hooks off and reuse the checks.
- **spec-drift**: Compares the first requirements with what was built and reports anything missing or changed. It catches "didn't do what I said".

### Harness (8)

- **agent-design**: Decides whether a job needs an agent or a workflow, then writes the spec. A good first step for each agent you design.
- **agent-ingest-audit-optimize**: Already deep-read. Audits outside material and turns verified findings into reversible changes.
- **agent-smith **(on now)****: Already on. Scores your Claude Code setup across 7 areas.
- **claude-code-setup**: Anthropic's official recommender for hooks, skills, MCP servers and subagents per repo.
- **harness**: A team-architecture factory: turns a domain into an agent team and skills, with native workflow modes.
- **harness-architect**: Builds or audits a full harness in 9 phases (CLAUDE.md, settings, rules, agents, hooks, MCP) with a red-team advisor.
- **harness-scope **(on now)****: Already on. Turns skills, rules and tools on or off per repo with profiles. It's the cure for too many skills loading.
- **wizard**: Turns any repeatable task into a reusable workflow ("spell"). It fits your dynamic-workflows goal.

### Orchestration (6)

- **agent-army**: Runs big batches in parallel with checkpoints and checks for fake completion. Made for jobs like reading 2,000 corpus docs.
- **agent-discussion**: Lets Claude, Gemini CLI and other agents debate through a shared file protocol. This is the "hand in hand with Gemini" piece.
- **backlog**: Tasks that survive across sessions and agents, so work isn't lost across your 19-plus sessions.
- **cc**: Parallel sessions can see each other, avoid file conflicts and message each other. It fits running many threads.
- **crewmarshal**: Claude plans and reviews while outside executors such as Gemini implement, behind review gates.
- **noetic-control-room**: One person, one coordinator, many agents: briefs workers, lands ready PRs, starts cloud workers. It matches how you work.

### Skills (4)

- **skill-creator **(on now)****: Already on. Official skill builder with evals.
- **skill-discovery**: Inventories skills and instruction files across Claude, Codex, Cursor and Gemini. It automates this audit.
- **skill-gate**: Puts chosen skills behind confirmation through a per-project list you control. It encodes "no skills without direction".
- **skill-provenance**: Tracks skill provenance and drift across platforms. It fixes the memory-as-skill snapshot that never syncs back.

### Plugins (5)

- **plugin-dev **(on now)****: Already on. Official plugin building kit.
- **plugin-manager**: A visual UI for toggling plugins, for managing a 100-plugin set.
- **plugin-packaging**: Repairs plugins that fail to install or load, which you'll need for your own marketplace.
- **skills-updater**: Audits and updates plugins and skills to their latest versions.
- **turbocharge #2**: The customize-and-sync turbocharge. It keeps your forked plugins customized and in sync with upstream, which is how you work.

### MCP (5)

- **mcp-debugging**: Repairs MCP connection and auth failures, like context7, GitHub and adb failing right now.
- **mcp-server-dev **(on now)****: Already on. Official guide for building MCP servers.
- **mcp-tunnels**: Reaches a private MCP server (for example on your phone) through an Anthropic tunnel. Key for the Android Chrome DevTools MCP.
- **mcp2cli**: Turns MCP servers into token-light CLIs with a SKILL.md generated for each.
- **tool-schemas**: Repairs tool schemas when calls connect but return wrong results. Useful when you build your own tools.

### Web (5)

- **apify**: Apify scrapers and crawlers for bulk web ingestion. It pairs with firecrawl.
- **claude-bridge **(on now)****: Already on. Drives your real Chrome or a headless browser end to end.
- **firecrawl**: Scrape, crawl, map and search the web. The main bulk web-ingestion tool.
- **modern-web-guidance**: Current web practices, including a Chrome-extensions skill for your browser tools.
- **playwright **(on now)****: Already on. Playwright headless browser.

### Research (2)

- **searchoclock **(on now)****: Already on. Date-aware research on fixes after a Bash failure. It matches your "research, don't guess" rule.
- **watch-video**: Watches videos: keyframes plus a Whisper transcript in a report. Good for video sources in the corpus.

### Voice (4)

- **airquote**: Cleans up voice dictation into clear prompts before Claude reads them. You dictate most messages.
- **drunken-master**: Reads garbled speech-to-text the way you meant it and shows its reading before acting.
- **local-whisper**: Local Whisper speech-to-text. It's the STT layer.
- **tts**: Reads answers aloud. It's the TTS layer for your voice workflow.

### Wiki (7)

- **create-smartfolder**: Turns a folder into a tiered knowledge base with per-folder guides. A part for wiki-admin.
- **gdrive-to-markdown**: Imports Google Docs, Sheets and Slides into a Markdown knowledge base through the Drive connector. This is corpus ingestion.
- **llm-wiki**: A Markdown knowledge base with local hybrid search and evidence-linked lessons. It's the core for wiki-admin.
- **obsidian-notes **(on now)****: Already on. Keeps a vault valid for Obsidian, GitHub and VS Code.
- **obsidian-sync **(on now)****: Already on. Syncs docs into the Obsidian vault.
- **rag-evaluation**: Debugs wrong answers from a knowledge base and missed retrieval. It's the test harness for the LLM wiki.
- **wiki-wonka**: An LLM-maintained wiki with ingest, query and lint. A wiki-admin part.

### Files (1)

- **desktop-commander**: A local MCP for the terminal, processes, PDF, DOCX and Excel, plus Obsidian vault skills. It can read the corpus.

### Reverse eng (2)

- **claude-war-room**: Reverse-engineers any codebase into living docs, plus a multi-agent risk hunt. It's your "reverse engineer anything" piece.
- **code-map**: An interactive HTML map of a codebase, with every node cited to real files.

### Code nav (1)

- **graph-indexer**: A live local code graph: references, impact of a change and post-edit checks, with no network.

### Review (2)

- **code-review **(on now)****: Already on. Official multi-agent PR review.
- **review-council**: Six specialist reviewers: correctness, security, trust boundaries, tests, architecture and interfaces.

### Security (3)

- **claude-security**: Deep vulnerability scan with every finding challenged and every patch verified.
- **llm-secure-patterns**: Secure patterns for agents that take in web content, which matters for an OS that ingests the web.
- **public-repo-readiness**: Audits public repos for secrets, private data and internal references. Your repos are public.

### Android (2)

- **adb-mcp **(on now)****: Drives an emulator or phone over adb to install, tap, build and test your APKs.
- **kotlin-lsp**: Kotlin language server for Jetpack Compose code: diagnostics, definitions and references.

### Google (3)

- **firebase**: Firebase backend for your Android apps (auth, Firestore, hosting). It's part of the Google infrastructure you want.
- **gcp-devkit**: Google Cloud guidance: Cloud Run, Firestore, IAM and Terraform.
- **google-multi-account**: Gmail, Calendar and Drive across several Google accounts. You have two accounts.

### Cloud (1)

- **cloudflare**: You use Cloudflare. Its Workers, D1, R2 and Vectorize skills plus the Cloudflare MCP can host the memory MCP server and its edge storage.

### Data (1)

- **supabase-expert**: You use Supabase. Row-level security, Auth and Storage guidance for the OB1-style pgvector memory mirror. It pairs with the Supabase connector.

### Design (1)

- **design**: Anthropic's official design critique, design system and accessibility reviews, for your Compose app UIs.

### Decisions (3)

- **building-with-typesafe-jev **(on now)****: Already on. A how-to guide for building with Jev. Fold it into one Jev plugin (see ideas).
- **claude-jev **(on now)****: Already on. Jev MCP for typed decisions.
- **jev **(on now)****: Already on. The Jev engine module.

### Thinking (3)

- **claude-deconstruct**: First-principles breakdown of a problem. It earns its place on hard design calls for the OS.
- **consensus **(on now)****: Already on. Asks GPT, Gemini and DeepSeek for second opinions.
- **devil-advocate**: One adversary that tries to kill a decision before you commit. Good for big rewrites.

### Prompting (1)

- **prompt-design**: Designs, evaluates and repairs prompts, agent definitions and rule files for any model, Gemini included.

### Docs (1)

- **context7 **(on now)****: Already on. Version-specific library docs. Its proxy connection currently fails here.

### GitHub (1)

- **github **(on now)****: Already on. GitHub MCP (its proxy connection currently fails here).

### Tracking (2)

- **build-companion**: A board of what's built, in flight, not deployed and never built. It catches sessions that produced no real work.
- **human-in-the-loop**: A pane of tasks only you can do (store keys, pair wireless debugging) so they don't get lost in chat.

### Sessions (1)

- **claudestrophobic**: Lists and deletes stale sessions and orphaned projects, for clearing out the 77 stale ones.

### Backup (1)

- **claudebase**: Backs up and restores ~/.claude to a private GitHub repo, so the phone, cloud and PC stay in sync.

### Repo care (1)

- **cut-weight**: Cleans cluttered repos and archives anything you approve so it can be restored. Good for the stale-branch mess.

### Env (1)

- **env-setup-wizard**: Works out what a project needs and writes a verified setup script, which helps fix cloud environment scripts.

### Notify (1)

- **notify #1**: Sends notifications to Telegram, Slack or webhooks, which reach your phone.

### Style (1)

- **caveman #1**: A concise mode: answer first, no filler, no repeated questions. This matches your profile preferences.

### Feedback (1)

- **claude-code-feedback**: Files proper bug reports against Claude Code, for issues like the sync and hook bugs you've hit.

---

## 2. Overlaps: where several plugins do the same job

| Job | Keep | Cut as overlap |
|---|---|---|
| Session memory and recall | memory-toolkit, pmm, anchor-memory, agent-recall, memory-agent, remember, whydone, jevmem, compounded, claude-patterns, adaptive-agent, chat-autoexporter, ccfind | agent-memory, anamnese-core, claude-memory, cogmemai, cowork-mem, memex, memories, memory-bank, mind-plus-plus, oak-memory, project-memory, scaffold, workflow-toolkit |
| Handoff between sessions | context-handoff #1, handoff #1 (per branch), cache-guard | claude-handoff, context-handoff #2, handoff #2, handoff-doc, wherewasi, superdevflow |
| Compaction and the cache | better-compact, cache-ttl-timer, cache-guard | cache-caffeine, compact-on-idle, idle-compact, context-compactor, context-keep |
| Usage and cost meters | heavy-usage, claude-code-cost, burn-baby-burn | cc-limit-pacer, ccoverhead, claudemeter, claude-pace, claude-usage-statusline, claude-vitals, claude-pulse, usage-bars, claude-stats, claude-piggy-bank, claude-activity |
| Building a harness or .claude setup | harness, harness-architect, agent-design, claude-code-setup, wizard | agentic-harness, build-harness, harness-bootstrap, harness-init, harness-designing, harnesskit, cc-bootstrapper, claudify, cortex, dev-forge, project-scaffolder |
| Auditing rules and CLAUDE.md | claude-md-management, claude-perfectionist, agent-smith, instructions-cleanup, bake-claude-md-files, chuck | claude-md-composer, claude-md-optimizer, claude-performance, clawness, mcp-workflow-audit, sync-docs |
| Superpowers-style dev discipline | superpowers (hook off), no-cape, frontier-simplify, loop-and-gate-build-kit | agentic-sdlc, claude-damn, gangsta, sixth-sense, sdd-superpowers, skillquiver, shipwright x4, turbocharge #1, senior-developer, sf, spec-driven-dev, feature, claude-forge, god-prompt-mcp, mister-anderson |
| Code review | code-review, review-council, claude-security | audit, claude-review-loop, code-review-harness, code-review-plugin, code-simplifier (built-in /simplify), semgrep, project-review |
| Reverse engineering a codebase | claude-war-room, code-map, graph-indexer | code-graph, code-modernization, codebase-mentor, grill, code-parser, impact-analysis, project-pilot |
| Parallel sessions talking to each other | cc, noetic-control-room | crew, relay |
| Notifications | notify #1 (Telegram and webhooks) | notify #2, cc-notify, cc-terminal-notifier, claude-bell, claude-code-notify, claude-notify, claude-notify-resume, claude-win-notify, notify-sounds |
| Searching past sessions | ccfind | chat-search, chat-namer, claude-sqlite-plugin |
| Wiki and knowledge base | llm-wiki, wiki-wonka, create-smartfolder, gdrive-to-markdown, obsidian-notes, obsidian-sync, rag-evaluation | learn-wiki, md-linker, graph-query-mcp, source-of-truth, docbrain |
| Second opinions and adversaries | consensus, devil-advocate, colosseum, claude-deconstruct | council, theboardroom, mindpowers, fortytwo-mcp, plan-review |
| Prompting | prompt-design, airquote | prompt-brain, prompt-coach, prompt-enhancer, prompt-enhancer-pack, sth |
| Checking skills | skill-creator, plugin-dev, skill-provenance | skill-doctor, skill-reviewer, skill-validator, skillcheck-free, skillers |
| Design | design | consistent-ui, design-dev-bridge, design-skills, design-superpowers, intent, ux-superpowers, ui-color-palette |
| Backing up settings | claudebase | claude-backup, cync |
| Web scraping | firecrawl, apify, claude-bridge, playwright | scout, toolrouter plugin (the connector stays) |

---

## 3. Ideas for combining, streamlining and customizing

These are proposals only. Nothing gets built until you say so.

- **One memory plugin, your own.** Build it from parts in one NovÆxorpus marketplace plugin, sorted into tiers:
  - **Ledger:** anchor-memory's ledger and integrity checks.
  - **Decisions:** whydone's decision log.
  - **Daily logs:** remember's tiered logs.
  - **Graph:** agent-recall's SQLite graph.
  - **Raw feed:** chat-autoexporter's exports.
  - **Recall:** ccfind's session search.
  - **Approved rules:** compounded's approve-before-learning loop.
  Point its start-of-session load at NvAEx-Recaps/memory (the memory-as-skill-design note). Then retire pmm and memory-toolkit's overlapping skills.
- **One Jev plugin.** jev, claude-jev, building-with-typesafe-jev and jevmem are four plugins for one stack. Merge them into one plugin with one settings block. jevmem stays opt-in per project.
- **A non-blocking verification pack.** Combine claude-code-audit-stack (claim auditor), llm-dark-patterns' 30 checks, spec-drift and claude-eta's loop detector into one checker. It warns and logs, and never blocks a stop or a read. A single switch turns it off mid-session.
- **A slimmer discipline layer.** Keep superpowers' skills, but turn off its "MUST invoke" session hook. Pull no-cape's escalate-don't-thrash and fail-loud rules, frontier-simplify's review caps and loop-and-gate's human gates into one short rule file that your rulebook owns.
- **Wiki-admin from parts.** Build wiki-admin from these parts:
  - llm-wiki's hybrid search as the core.
  - wiki-wonka's ingest, query and lint.
  - create-smartfolder's per-folder guides.
  - gdrive-to-markdown and firecrawl or apify for intake.
  - headroom for huge files.
  - rag-evaluation to test answers.
  - obsidian-notes for vault hygiene.
  The corpus run then goes through agent-army in parallel batches instead of 40 slow subagents.
- **A Gemini lane.** Use agent-discussion's shared-file protocol plus crewmarshal's "outside executor under review" pattern, with consensus for quick second opinions. Gemini CLI does the bulk reading, and Claude plans and reviews.
- **A voice layer.** airquote and drunken-master clean up the input, local-whisper does speech-to-text, and tts reads answers aloud. Together they make one voice plugin.
- **An Android lane.** adb-mcp, kotlin-lsp, firebase and gcp-devkit form the APK toolchain. mcp-tunnels connects the phone's Chrome DevTools MCP to cloud sessions.
- **Per-repo profiles instead of 100 plugins everywhere.** harness-scope (already on) can load only the plugins each repo needs. For example, the Android repos get the Android lane and the wiki repo gets the wiki pack. That cuts what every session loads without uninstalling anything.
- **Keep forks in sync.** turbocharge #2 (customize and sync) keeps your customized forks current with upstream. skills-updater flags new versions, and claudebase backs the whole ~/.claude setup up to GitHub.
- **Control over skills.** skill-gate puts any skill you choose behind a confirmation through a per-project list. That makes "no skills without my direction" a setting you can switch off, not a rule I have to remember.

---

## 4. Cut (246), with the reason for each

| # | Plugin | Category | Why cut |
|---|---|---|---|
| 1 | agency-mcp | Business | Manages ad, SEO and CRM accounts for a marketing agency, which you don't run. |
| 2 | agent-memory | Memory | Overlaps the memory plugins you keep. Its "60 to 90% savings" claim is marketing and unverified. |
| 3 | agentic-harness | Harness | Overlaps harness and harness-architect, which do team generation and audits more completely. |
| 4 | agentic-sdlc | Dev workflow | Overlaps superpowers and no-cape. The ticket flows assume Jira or Linear, which you don't use. |
| 5 | agentmail | Comms | Email inboxes for agents. Your Gmail connector covers email, and agent inboxes aren't in your plans. |
| 6 | ai-advisors | Business | Measures how AI search engines see a brand, a marketing job. |
| 7 | ai-employees | Business | Hires out business roles (sales, ads, SEO), not your work. |
| 8 | ai-integration-architect | Dev workflow | Enterprise integration scaffolding. mcp-server-dev covers MCP building better. |
| 9 | ai-memory-reader | Viewer | A viewer app for macOS and iOS only. You're on Android. |
| 10 | ai-mentor | Learning | Teaches you Claude Code features. You need the agent to use them, not a tutorial. |
| 11 | ai-native-os | Business | A startup-company handbook despite the "OS" name, not an agent OS. |
| 12 | ai-youtube-os | Business | Korean-language YouTube channel operations. |
| 13 | analytics-skills | Business | Reads website analytics funnels, a marketing job. |
| 14 | anamnese-core | Memory | Syncs memory to a third-party cloud and overlaps the memory stack you keep. |
| 15 | ancestralfire | Hobby | Genealogy. |
| 16 | audit | Review | Overlaps code-review, review-council and claude-security, which cover the same audit with fewer agents. |
| 17 | bigquery-data-analytics | Data | Your BigQuery connector already does this. |
| 18 | build-harness | Harness | An interactive tutorial version of what harness and harness-architect already do. |
| 19 | cache-caffeine | Usage | Pokes the session to keep the cache warm, which spends usage. cache-ttl-timer and better-compact cover the need. |
| 20 | caveman #2 | Style | A joke duplicate of the caveman above. |
| 21 | cc-bootstrapper | Harness | Overlaps harness-architect: another generator for the .claude/ folder. |
| 22 | cc-limit-pacer | Usage | Overlaps heavy-usage and claude-code-cost, and adds 10 commands and 2 hooks for pacing. |
| 23 | cc-notify | Notify | Desktop banners for macOS, Linux and Windows. notify (Telegram and webhooks) reaches your phone. |
| 24 | cc-terminal-notifier | Notify | A macOS notifier that overlaps notify. |
| 25 | ccaf | Learning | Practice tests for the Claude certification exam. |
| 26 | ccgrapher | Orchestration | Small plan-dependency checker. agent-army and superpowers dispatching cover it. |
| 27 | ccoverhead | Usage | A usage band in the terminal. Overlaps cache-ttl-timer and heavy-usage. |
| 28 | changethisfile | Files | A paid hosted converter. Your pdf, docx and xlsx account skills read those files locally. |
| 29 | chat-namer | Sessions | Names local CLI sessions. Overlaps ccfind for finding them. |
| 30 | chat-search | Sessions | Overlaps ccfind. |
| 31 | ci-optimizer | DevOps | CI speed tuning. Not a current goal. |
| 32 | claude-activity | Usage | An activity heatmap that overlaps claude-code-cost. |
| 33 | claude-backup | Backup | Overlaps claudebase, which backs up to GitHub. |
| 34 | claude-bell | Notify | Chime sounds. Overlaps notify. |
| 35 | claude-blog-assistant | Business | Blog publishing, and needs another plugin. |
| 36 | claude-code-notify | Notify | Overlaps notify. |
| 37 | claude-code-toolkit | Dev workflow | A grab bag (Railway preflight and more) that overlaps superpowers and harness. |
| 38 | claude-damn | Dev workflow | 61 modifier skills that overlap superpowers. It also ships the guard that blocks inline multiline scripts. |
| 39 | claude-forge | Dev workflow | Spec-driven evidence workflow that overlaps spec-drift and superpowers. |
| 40 | claude-handoff | Handoff | Overlaps context-handoff, which also saves automatically. |
| 41 | claude-mac-chrome | Web | Chrome automation for macOS only. |
| 42 | claude-md-composer | Rules | Overlaps claude-md-management and instructions-cleanup. |
| 43 | claude-md-optimizer | Rules | Overlaps claude-md-management and bake-claude-md-files. |
| 44 | claude-memory | Memory | A basic categorized memory that the kept memory plugins already cover. |
| 45 | claude-notify | Notify | Overlaps notify. |
| 46 | claude-notify-resume | Notify | Overlaps notify. |
| 47 | claude-opus-4-5-migration | Outdated | Migrates prompts to Opus 4.5, two generations old. |
| 48 | claude-pace | Usage | A statusline that overlaps heavy-usage. |
| 49 | claude-performance | Rules | Writes behavior rules into CLAUDE.md on its own, which breaks your "no rules without my direction" rule. |
| 50 | claude-piggy-bank | Usage | Overlaps claude-code-cost. |
| 51 | claude-pulse | Usage | A statusline badge with 11 hook events. Overlaps the usage tools you keep. |
| 52 | claude-release | DevOps | A release pipeline. superpowers finishing-a-branch covers your needs today. |
| 53 | claude-review-loop | Review | Overlaps review-council. |
| 54 | claude-sqlite-plugin | Sessions | Overlaps ccfind. |
| 55 | claude-stats | Usage | Overlaps claude-code-cost. |
| 56 | claude-tab-fix | Niche | A fix for tab-indented files only. |
| 57 | claude-time | Context | Stamps the time on every prompt. The date is already supplied, and searchoclock is date-aware. |
| 58 | claude-usage-statusline | Usage | Overlaps heavy-usage. |
| 59 | claude-vitals | Usage | Overlaps context-window and heavy-usage. |
| 60 | claude-win-notify | Notify | Windows only. |
| 61 | claudedesktiop | Empty | An unfilled template ("A brief description of what your plugin does"). |
| 62 | claudemeter | Usage | Overlaps heavy-usage. |
| 63 | claudify | Harness | Overlaps harness-architect. |
| 64 | claudinator | Cosmetic | Restyles the terminal UI. |
| 65 | clawback | Scheduling | Webhooks and cron through a hosted server. Native routines already do this. |
| 66 | clawd-pet **(on now)** | Cosmetic | Already on, but it's a pet above the prompt. It adds no work value. |
| 67 | clawness | Rules | Its 222 prewritten rules are the "Clawness rulebook" that was injected into your sessions. You're writing your own. |
| 68 | clean-architecture | Dev workflow | A Clean Architecture course. Not a goal. |
| 69 | cloud-sql-mysql | Data | Cloud SQL for MySQL. Not in your stack. |
| 70 | cloud-sql-postgresql | Data | Cloud SQL for Postgres. Not in your stack. |
| 71 | cloud-sql-sqlserver | Data | Cloud SQL for SQL Server. Not in your stack. |
| 72 | code-graph | Reverse eng | Overlaps code-map, which maps whole systems and flows. |
| 73 | code-modernization | Reverse eng | Aimed at legacy COBOL, Java and .NET. claude-war-room covers reverse-engineering for you. |
| 74 | code-parser | Code nav | Covers Dart, Python and TypeScript, not Kotlin. graph-indexer covers navigation. |
| 75 | code-review-harness | Review | Overlaps code-review and review-council. |
| 76 | code-review-plugin | Review | Overlaps code-review. |
| 77 | code-simplifier | Review | The built-in /simplify does the same job. |
| 78 | codebase-mentor | Reverse eng | Overlaps claude-war-room and code-map. |
| 79 | coding-skills | Dev workflow | Bugs in distributed databases and caches. Not your domain. |
| 80 | cogmemai | Memory | A cloud memory service that overlaps the kept memory stack. |
| 81 | compact-on-idle | Context | Auto-compacts when idle. Overlaps better-compact and cache-guard. |
| 82 | consistent-ui | Design | A UI drift checker. design covers UI review for your apps. |
| 83 | context-compactor | Context | Overlaps better-compact. |
| 84 | context-handoff #2 | Handoff | Overlaps context-handoff. Its handoff-writing skill is worth borrowing to move work into claude.ai chats. |
| 85 | context-keep | Context | Overlaps better-compact. |
| 86 | cortex | Harness | Another "OS for Claude Code" with enforcement hooks. You're building your own. |
| 87 | council | Thinking | Overlaps consensus and devil-advocate. |
| 88 | cowork-mem | Memory | Cowork-only memory that overlaps the kept stack. |
| 89 | cowork-plugin-management | Plugins | You rejected it earlier ("lipstick on a pig"), and plugin-dev covers building plugins. |
| 90 | crayon | Cosmetic | Colored replies. |
| 91 | crew | Orchestration | Overlaps cc. It also spans Codex and OpenCode, which you don't use. |
| 92 | critique | Rules | The "critique mode" that was injected into every prompt and that you flagged as junk. |
| 93 | cync | Backup | Overlaps claudebase. |
| 94 | data | Data | Analyst dashboards and SQL. Not a goal. |
| 95 | design-dev-bridge | Design | A Figma bridge. You don't use Figma. |
| 96 | design-skills | Design | Overlaps design. |
| 97 | design-superpowers | Design | Overlaps design. |
| 98 | dev-env-doctor | Env | Overlaps env-setup-wizard. |
| 99 | dev-forge | Harness | Overlaps loop-and-gate and harness. |
| 100 | dev-mentor | Learning | A teaching companion that withholds answers. |
| 101 | dev-squad | Orchestration | A GitHub-issue dev team that overlaps agent-army and superpowers. |
| 102 | docbrain | Knowledge | Needs an organization DocBrain service. |
| 103 | docker-skills | DevOps | Docker isn't in your stack. |
| 104 | education-agent-skills | Learning | For teachers. |
| 105 | emem | Niche | Earth-observation data memory. |
| 106 | feature | Dev workflow | Overlaps superpowers and spec-drift. |
| 107 | forge | Verification | Overlaps claude-code-audit-stack and superpowers verification. |
| 108 | fortune-cookie | Fun | A fortune cookie. |
| 109 | fortytwo-mcp | Thinking | A paid outside service that is set to trigger itself whenever you doubt an answer. |
| 110 | founderos | Business | A startup-founder toolkit. |
| 111 | gangsta | Dev workflow | A mafia-themed fork of the superpowers idea. |
| 112 | gitbook | Docs | GitBook isn't in your stack. |
| 113 | god-prompt-mcp | Dev workflow | Overlaps superpowers. |
| 114 | google-cloud-storage | Google | No known Cloud Storage buckets. |
| 115 | graph-query-mcp | Wiki | Needs graphify, which you haven't set up. |
| 116 | graphql-guardian | Dev workflow | GraphQL isn't in your stack. |
| 117 | greenfield | Business | Client-engagement delivery methodology. |
| 118 | grill | Reverse eng | Overlaps claude-war-room. |
| 119 | guide | Learning | The built-in claude-code-guide agent covers it. |
| 120 | handoff #2 | Handoff | Overlaps context-handoff. |
| 121 | handoff-doc | Handoff | Overlaps context-handoff. |
| 122 | harness-bootstrap | Harness | A quick-start subset of harness-architect. |
| 123 | harness-designing | Harness | A harness for design teams. |
| 124 | harness-init | Harness | Overlaps harness-architect. |
| 125 | harnesskit | Harness | Aimed at "vibe coders", and overlaps harness. |
| 126 | hzblj-skills | Dev workflow | React and React Native. You build Kotlin and Compose. |
| 127 | idle-compact | Context | Overlaps better-compact. |
| 128 | idle-timing | Context | Idle-gap notes. Minor. |
| 129 | impact-analysis | Code nav | TypeScript only. Overlaps graph-indexer. |
| 130 | intent | Design | Overlaps design. |
| 131 | internet-tools | Network | DNS and email-auth checks. Not a goal. |
| 132 | invaders | Fun | A game. |
| 133 | java-backend-skills | Dev workflow | Java and Spring backends. You build Kotlin Android apps. |
| 134 | jira-attachment-plugin | Business | You don't use Jira. |
| 135 | jsonschemaapp-mcp | Business | SEO structured-data audits. |
| 136 | keep-awake | Desktop | Keeps a laptop awake. |
| 137 | learn-wiki | Wiki | A learning wiki that overlaps llm-wiki. |
| 138 | localstack | Cloud | AWS LocalStack. Not your stack. |
| 139 | mattpocock-skills | Empty | No skill files downloaded. Its ideas overlap superpowers. |
| 140 | mcp-apps | MCP | Overlaps mcp-server-dev (build-mcp-app). |
| 141 | mcp-client-kit | MCP | Python wrappers for MCP servers. Not needed. |
| 142 | mcp-gsc | Business | Search Console SEO. |
| 143 | mcp-image-viewer | Desktop | A desktop image popup. |
| 144 | mcp-workflow-audit | Harness | Overlaps claude-perfectionist. |
| 145 | mcpbackend | Backend | A third-party backend service. |
| 146 | mcpbinder | Tasks | A third-party task service. backlog is local. |
| 147 | md-linker | Wiki | Overlaps obsidian-notes link linting. |
| 148 | md-prompt | Cosmetic | Styles the prompt box. |
| 149 | memex | Memory | Needs Docker and Qdrant, and overlaps the kept memory stack. |
| 150 | memories | Memory | Overlaps the kept memory stack. |
| 151 | memory-bank | Memory | Overlaps pmm and memory-toolkit. |
| 152 | mentor-mode | Learning | A tutor that withholds solutions. |
| 153 | mind-plus-plus | Memory | A meetings-and-stakeholders second brain with dozens of office personas. |
| 154 | mindmap | Viz | Mindmaps. Minor. |
| 155 | mindpowers | Thinking | Overlaps devil-advocate and colosseum. |
| 156 | mister-anderson | Dev workflow | Overlaps superpowers and backlog. |
| 157 | ml-pipeline | ML | ML training discipline. Not a goal. |
| 158 | n8n-knowledge | Niche | n8n. |
| 159 | neocode | Cosmetic | Matrix rain. |
| 160 | (unnamed .staging) | Empty | An unnamed staging folder. |
| 161 | notify #2 | Notify | Overlaps the notify above. |
| 162 | notify-sounds | Notify | Sounds. Overlaps notify. |
| 163 | nvidia-skills | Niche | NVIDIA GPU work. |
| 164 | oak-memory | Memory | Vector memory profiles that overlap the kept stack. |
| 165 | oak-national-academy | Learning | A UK school curriculum. |
| 166 | observability | DevOps | OpenTelemetry. Not a goal. |
| 167 | open-source-launch-skill | DevOps | Launch prep for open source. public-repo-readiness covers the safety part. |
| 168 | opencode | Orchestration | Delegates to OpenCode models. You use Gemini. |
| 169 | opencode-subagent-mcp | Orchestration | Same as above. |
| 170 | paypal | Business | PayPal. |
| 171 | pdf-viewer | Files | Overlaps the pdf account skill. |
| 172 | pge-orchestrator | Orchestration | Autonomous "one prompt to full product" with a "don't care about tokens" mode. That's the opposite of your direction-first rule. |
| 173 | plan-review | Empty | No skill files. Overlaps devil-advocate. |
| 174 | planning-skills | Planning | Overlaps superpowers planning. |
| 175 | platform-skills | DevOps | Kubernetes and platform engineering. |
| 176 | plugin-pilot | Plugins | Installs and removes plugins on its own, which breaks your "no installs without direction" rule. |
| 177 | pm | Tracking | Overlaps build-companion and backlog. |
| 178 | productivity | Tracking | Overlaps backlog and your calendar connector. |
| 179 | project-artifact | Tracking | Overlaps build-companion. |
| 180 | project-boundary | Guard | Its only part is the hook that blocked writes outside /home/claude, $VAR use and mkdir in project files, the blocker you hit. |
| 181 | project-memory | Memory | Overlaps the kept memory stack. |
| 182 | project-pilot | Tracking | Overlaps code-map and claude-war-room. |
| 183 | project-review | Empty | No skill files. Overlaps review-council. |
| 184 | project-scaffolder | Harness | Overlaps harness-architect, and adds destructive-command guards. |
| 185 | project-setup | Env | Overlaps env-setup-wizard. |
| 186 | prompt-brain | Prompting | Overlaps prompt-design. |
| 187 | prompt-coach | Prompting | Overlaps prompt-design. claude-context-optimizer already runs a prompt coach. |
| 188 | prompt-enhancer | Prompting | Overlaps prompt-design. |
| 189 | prompt-enhancer-pack | Prompting | Rewrites your prompts automatically before Claude answers. You want your words read as written. |
| 190 | promptcolor | Cosmetic | Colors your prompt lines. |
| 191 | prove | Verification | Overlaps claude-code-audit-stack. |
| 192 | qdrant | Data | Qdrant isn't in your stack. |
| 193 | relay | Orchestration | Overlaps cc. |
| 194 | repo-hygiene | Repo care | Overlaps cut-weight and superpowers. |
| 195 | resumenext-resume-bullet-points | Business | Resume bullet points. |
| 196 | scaffold | Memory | Obsidian-backed memory that overlaps pmm and obsidian-sync. Its decision enforcement is worth borrowing. |
| 197 | scout | Web | Overlaps firecrawl and your TinyFish and toolrouter connectors. |
| 198 | sdd-superpowers | Dev workflow | A spec-driven fork of superpowers. |
| 199 | second-arrow | Coaching | Coaches healthier human-AI interaction. Not a tooling need. |
| 200 | semgrep | Security | The login-nag hook you flagged, and it needs a Semgrep account. claude-security covers scanning. |
| 201 | senior-developer | Dev workflow | Overlaps superpowers. |
| 202 | senior-engineering-partner | Empty | No skill files. Overlaps superpowers. |
| 203 | sensei | Learning | A teaching dojo. |
| 204 | sf | Dev workflow | Overlaps superpowers. |
| 205 | shipwright #1 | Dev workflow | One of 4 plugins named shipwright. An a-la-carte kit that overlaps the kept memory stack and harness. |
| 206 | shipwright #2 | Dev workflow | One of 4 shipwrights. Overlaps code-review and superpowers. |
| 207 | shipwright #3 | Dev workflow | One of 4 shipwrights. Autonomous deploy pipeline, too heavy. |
| 208 | shipwright #4 | Dev workflow | One of 4 shipwrights. Jira sync with 5 hook events. |
| 209 | sideboard | Tracking | Overlaps build-companion. |
| 210 | siem-lab-coach | Learning | A Splunk lab. |
| 211 | signal-hunter | Research | A trend digest. Not tied to your goals. |
| 212 | sixth-sense | Dev workflow | A superpowers fork. |
| 213 | skill-campfire | Fun | Skill characters around a campfire. |
| 214 | skill-doctor | Skills | The built-in /skill-doctor covers it. |
| 215 | skill-reviewer | Skills | plugin-dev's skill-reviewer agent covers it. |
| 216 | skill-validator | Skills | Overlaps skill-creator evals. |
| 217 | skillcheck-free | Skills | Overlaps skill-creator. |
| 218 | skillers | Skills | Overlaps claude-patterns. |
| 219 | skillkeel-starter | Repo care | Overlaps superpowers and public-repo-readiness. |
| 220 | skillquiver | Dev workflow | A copy of superpowers shared with ChatGPT and Codex. |
| 221 | smart-commits | Git | Commit messages. superpowers and native git cover them. |
| 222 | socratic-mentor | Learning | A Socratic tutor. |
| 223 | source-of-truth | Docs | Overlaps llm-wiki and sync-docs. |
| 224 | sourcegraph | Code nav | Sourcegraph isn't in your stack. |
| 225 | spec-driven-dev | Dev workflow | Overlaps superpowers. |
| 226 | sth | Prompting | A team prompt library you don't use. |
| 227 | supalens | Data | A third-party database chat. |
| 228 | superdevflow | Handoff | Overlaps context-handoff and superpowers. |
| 229 | sync-docs | Docs | Overlaps claude-md-management. |
| 230 | system-design-skills | Learning | System-design study. |
| 231 | theboardroom | Business | A boardroom of executives. |
| 232 | tldr | Style | Overlaps caveman. |
| 233 | tmux-status | Terminal | tmux emoji titles. |
| 234 | toolrouter | Web | Your toolrouter connector is already attached. |
| 235 | turbocharge #1 | Orchestration | A second turbocharge (orchestration) that overlaps superpowers. |
| 236 | ui-color-palette | Design | A color-palette service. |
| 237 | ultrapowers-dev | Dev workflow | 55 generic language guides. Too broad. |
| 238 | ultrasolve | Empty | No skill files. |
| 239 | usage-bars | Usage | Usage bars. Overlaps heavy-usage. |
| 240 | ux-superpowers | Design | Overlaps design. |
| 241 | whats-new | Learning | Injects feature-of-the-day tips through 3 hooks. |
| 242 | wherewasi | Handoff | Overlaps context-handoff. |
| 243 | whodb | Data | Not your stack. |
| 244 | why-is-my-claude-dumb | Plugins | A Korean plugin recommender. |
| 245 | workflow-toolkit | Tasks | Overlaps backlog and ccfind. |
| 246 | worktree-workspace | Git | Overlaps superpowers worktrees. |
