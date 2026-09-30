<!-- Converted from c10vis-poem_claude-code-best-practice_ from vibe coding to agentic engineering - practice makes claude perfect.pdf — 15 pages -->

## Page 1

c10vis-poem claude-code-best-practice
Code Pull requests Agents Actions Projects Wiki Security and quality Insights Settings
Watch 0 Fork 0
from vibe coding to agentic engineering - practice makes claude perfect
MIT License
linkedin.com/in/shanraisshan
1 star 0 forks 0 watching 1 branch 0 tags Activity
Public repository · Forked from shanraisshan/claude-code-best-practice
m 1 Branch 0 Tags Go to file T Go to file Add file Code
This branch is 919 commits behind shanraisshan/claude-code-best-practice:main . Contribute Sync fork
shanraisshan and claude chore(readme): refresh Last Updated badge timestamp to 2026-05-11 10:…
4527f4d · 2 months ago
| Claude |  | Replaced |
|---|---|---|
| ! | add video-2.png thumbnail | 2 months ago |
| .claude | record presentation-claude-code Learnings f … | 2 months ago |
| .codex | updated | 3 months ago |
| .github | revert FUNDING.yml to custom checkout lin … | 3 months ago |
| agent-teams | fix: add missing description frontmatter to ti … | 3 months ago |
| best-practice | chore(claude-subagents): bump version bad … | 2 months ago |
| changelog | chore(agent-collections): append 2026-05-1 … | 2 months ago |
| development-workflows | adeed claude-oss banner | 4 months ago |
| implementation | updated weather workflow | 3 months ago |
| orchestration-workflow | updated weather workflow | 3 months ago |
| presentation | insert slide 29 Uncle Bob counterpoint + ren … | 2 months ago |
| reports | Create claude-spinner-verbs-and-tips.md | 3 months ago |
| tips | tips/claude-thariq: fix off-by-one cascade in … | 3 months ago |
| tutorial | add Day 1 onboarding tutorial — prompting, … | 3 months ago |
| videos | karparthy added | 3 months ago |
| .gitignore | fix: add hooks log directory to .gitignore to p … | 3 months ago |
| .mcp.json | fix: pin MCP server package versions to prev … | 3 months ago |
| CLAUDE.md | rename presentation agent | 3 months ago |
| LICENSE | updated docs | 4 months ago |
| README.md | chore(readme): refresh Last Updated badge … | 2 months ago |
! add video-2.png thumbnail 2 months ago
 
.codex updated 3 months ago
 
 
 
 
 
implementation updated weather workflow 3 months ago
 
 
 
 
 
videos karparthy added 3 months ago
 
 
CLAUDE.md rename presentation agent 3 months ago
LICENSE updated docs 4 months ago
 
README License

---

## Page 2

# claude-code-best-practice
# from vibe coding to agentic engineering - practice makes claude perfect
updated with Claude Code v2.1.138 (May 11, 2026 10:36 AM PKT) 6 4 k
Best Practice Implemented Orchestration Workflow Claude Boris Community Click on these badges below to see the actual sources
# = Agents · = Commands · = Skills
GITHUB TRENDING
### #1 Repository Of The Day
# 1
# Boris Cherny on X (tweet 1 · tweet 2 · tweet 3)
# Tip
# Visit the How to Use section to take full advantage of this repo.
# 🧠 CONCEPTS
# Feature Location Description
Subagents .claude/agents/<name>.md Best Practice Implemented
Commands .claude/commands/<name>.md Best Practice Implemented
Best Practice ImplementedOfficial Skills · Skills for
### Skills .claude/skills/<name>/SKILL.md
# Mono-repos
| Workflows | .claude/commands/weather-orchestrator.md | Orchestration Work fl ow |  |
|---|---|---|---|
| Hooks | .claude/hooks/ | Best Practice | Implemented Guide |
| MCP Servers | .claude/settings.json , .mcp.json | Best Practice | Implemented |
| Plugins | distributable packages | Marketplaces · Create Marketplaces |  |
|  |  | Best Practice | Implemented Permissions · Model |
| Settings | .claude/settings.json | Config · Output Styles · Sandboxing · Keybindings · |  |
 
 
  
 
Auto Mode Config

---

## Page 3

# Feature Location Description
Status Line .claude/settings.json Best Practice Implemented
CLAUDE.md , .claude/rules/ , ~/.claude/rules/ ,Best Practice ImplementedAuto Memory · Auto
# Memory
### ~/.claude/projects/<project>/memory/
# Memory Deep-dive · Rules
# Checkpointing automatic (git-based)
# CLI Startup
claude [flags] Best PracticeInteractive Mode · Env Vars
# Flags
AI TermsBest Practice
# Best Practices Prompt Engineering · Extend Claude Code
# 🔥 Hot
# Feature Location Description
Ultrareviewbeta /ultrareview , claude ultrareview [target] Tasks tracking
### Devcontainers .devcontainer/
Channelsbeta --channels , plugin-based Reference
Ultraplanbeta /ultraplan
# No Flicker Mode
/tui fullscreen , CLAUDE_CODE_NO_FLICKER=1 Best Practice beta
beta
| Auto Mode | beta | --permission-mode auto , Shift+Tab | Best Practice Blog |  |
|---|---|---|---|---|
| Power-ups |  | /powerup | Best Practice |  |
| Fast Mode | beta | /fast , "fastMode": true |  |  |
| Computer Use | beta | computer-use MCP server | Desktop |  |
| Agent SDK |  | npm / pip package | Quickstart · Examples |  |
| Ralph Wiggum Loop |  | plugin | Best Practice | Implemented |
| Chrome | beta | --chrome , extension | Best Practice |  |
  
Power-ups /powerup Best Practice
Fast Modebeta /fast , "fastMode": true
  
### Agent SDK npm / pip package Quickstart · Examples
Ralph Wiggum Loop pluginBest Practice Implemented
beta
  
# Claude Code Web
### claude.ai/code Routines
beta
### Slack @Claude in Slack
beta Code Review GitHub App (managed)Best PracticeBlog
### GitHub Actions .github/workflows/ GitLab CI/CD
Remote Control /remote-control , /rc Best PracticeHeadless Mode
beta Agent Teams built-in (env var)Best Practice Implemented
Best Practice ImplementedDesktop scheduled tasks ·
### Scheduled Tasks /loop , /schedule , cron tools
# Announcement
Routinesbeta claude.ai/code/routines , /schedule Desktop Tasks
Tasks /tasks , ~/.claude/tasks/ Best PracticeUltrareview tracking
# Voice Dictation
/voice Best Practice
Simplify & Batch /simplify , /batch Best Practice

---

## Page 4

Feature Location Description
built-in, EnterWorktree / ExitWorktree , isolation:
| Git Worktrees | Best Practice |
|---|---|
| "worktree" |  |
### Orchestration Workflow
See orchestration-workflow for implementation details of Command → Agent → Skill pattern.
Claude Code Orchestration Workflow
Agent
Command agents/weather-agent
commands/weather-orchestrator (preloaded skill)
weather-fetcher
Asks user for C°/F°, invokes
Fetches temperature from
agent and SVG creator skill
Open-Meteo API for Dubai
User
commands/weather-orchestrator → agents/weather-agent (preloaded skill) → skills/weather-svg-creator (skill)
How to Use
claude /weather-orchestrator
### DEVELOPMENT WORKFLOWS
All major workflows converge on the same architectural pattern: Research → Plan → Execute → Review → Ship
Name Workflow
→ → → brainstorming using-git-worktrees writing-plans subagent-driven-development→
→ →
Superpowers 184k →
fi
→ → → → → Everythingprp-prd prp-plan prp-implement build-fix code-review quality-gate→prp-commit 176k Claude Code →p r p - p r

---

## Page 5

Name Workflow
→ → → → /speckit.constitution /speckit.specify /speckit.plan /speckit.tasks /speckit.implement→ Spec Kit 94k /speckit.checklist→/speckit.taskstoissues
→ → → /office-hours /plan-ceo-review /plan-eng-review /plan-design-review→/plan-devex-review gstack 92k → → → → → /autoplan /review /qa /ship /land-and-deploy→/canary
→
| Auto Mode | beta | --permission-mode auto , Shift+Tab | Best Practice Blog |  |
|---|---|---|---|---|
| Matt Pocock |  | /grill-with-docs → /to-prd → /tdd → /diagnose → /zoom-out → /improve-codebase-architecture |  |  |
|  | 6 7k |  | 0 0 | 13 |
| Skills |  | → /to-issues → /triage |  |  |
Matt Pocock/grill-with-docs /to-prd /tdd /diagnose /zoom-out→/improve-codebase-architecture 67k 0 0 13 Skills → /to-issues→/triage
→ → → /gsd-map-codebase /gsd-new-project /gsd-discuss-phase /gsd-plan-phase→
→ → → Get Shit Done 61k → /gsd-execute-phase /gsd-verify-work /gsd-ship /gsd-complete-milestone33 66 0
/gsd-new-milestone
→ → → bmad-agent-analyst bmad-prfaq bmad-agent-pm bmad-create-prd→
→ → bmad-agent-ux-designer bmad-agent-architect bmad-create-architecture→ BMAD-METHOD 47k 6 0 40 → → → bmad-create-epics-and-stories bmad-agent-dev bmad-dev-story bmad-code-review→
bmad-retrospective
→ → → →
| OpenSpec 47k | → |
|---|---|
| /opsx:explore |   /opsx:sync   /opsx:archive |
oh-my-→ → → → → →
| 33k | → |
|---|---|
| /omc-setup |   /ultraqa   /release |
claudecode
→ → → →
| agent-skills 27k | → |
|---|---|
| /spec /plan |     /review   /ship |
→ → → → → Compound/ce-strategy /ce-ideate /ce-brainstorm /ce-plan /ce-work /ce-debug→ 16k 49 4 38 Engineering → → /ce-code-review /ce-doc-review /ce-compound→/ce-product-pulse
→ → → → /research_codebase /create_plan /validate_plan /iterate_plan /implement_plan→ HumanLayer 11k 6 27 0 → → /local_review /describe_pr /commit→/create_handoff
Note: yellow tags are sub-loops — steps that repeat inside a parent step (e.g. per task, per story, or until a verify condition passes).
### Others
| Cross-Model (Claude Code + Codex) Workflow |  | Implemented |
|---|---|---|
| RPI Implemented |  |  |
| Ralph Wiggum Loop | Implemented |  |
Cross-Model (Claude Code + Codex) WorkflowImplemented
RPIImplemented
Ralph Wiggum LoopImplemented
Andrej Karpathy (Founding Member, OpenAI) Workflow
Peter Steinberger (Creator of OpenClaw) Workflow
Boris Cherny (Creator of Claude Code) Workflow — 13 Tips · 10 Tips · 12 Tips · 2 Tips · 15 Tips · 6 TipsBoris
Thariq (Anthropic) Workflow — Skills · Session ManagementThariq
### 🧰 SKILL COLLECTIONS
Repos primarily known as curated libraries of SKILL.md files (distinct from full workflow methodologies above). Sorted by stars descending.
Name
| anthropics/skills | 131k | 17 |
|---|---|---|
| mattpocock/skills | 68 k | 19 |
| agent-skills | 37k | 22 |
| wshobson/agents | 35k | 153 |
anthropics/skills 131k 17
mattpocock/skills 68k 19
agent-skills 37k 22
wshobson/agents 35k 153

---

## Page 6

Name
awesome-agent-skills 21k 938 (curated list)
scientific-agent-skills 20k 137
### 🤖 AGENT COLLECTIONS
Repos primarily known as curated libraries of subagent definitions ( .claude/agents/*.md ). Sorted by stars descending.
Name
msitarzewski/agency-agents 96k 185
VoltAgent/awesome-claude-code-subagents 20k 145
### 💡 TIPS AND TRICKS (83)
🚫👶 = do not babysit
Prompting · Planning · Context · Session · CLAUDE.md + .claude/rules · Agents · Commands · Skills · Hooks · Workflows · Advanced · Git / PR · Debugging · Utilities · Daily
Community
■ Prompting (3)
Tip Source
Claude diff between main and your branch 🚫👶
after a mediocre fix — "knowing everything you know now, scrap this and implement the elegant solution" 🚫👶Boris
Claude fixes most bugs by itself — paste the bug, say "fix", don't micromanage how 🚫👶Boris
■ Planning/Specs (7)
Tip Source
always start with plan modeBoris
to execute the spec
Video
Programmer 🚫👶
spin up a second Claude to review your plan as a staff engineer, or use cross-model for reviewBoris
write detailed specs and reduce ambiguity before handing work off — the more specific you are, the better the outputBoris
Video

---

## Page 7

■ Context (5)
Tip Source
context rot kicks in around ~300-400k tokens on the 1M context model — don't let sessions drift past that for intelligence-sensitive work
60% only on simple tasks. Manual /compact or /clear to reset when switching tasks
leaving failed attempts + corrections polluting context 🚫👶
model is at its least intelligent point when auto-compacting due to context rot
reads + 12 greps + 3 dead ends stay in the child's context, only the final report returns 🚫👶
■ Session Management (6)
Tip Source
based on how much existing context you need to carry forward
new tasks deserve a fresh session
Claude from its future self
control exactly what carries forward (high-stakes next step)
minutes or hours. Disable with recaps in /config
Claudes simultaneously
■ CLAUDE.md + .claude/rules (8)
Tip Source
Dex
when Claude touches files matching the glob
| wrap domain-specific CLAUDE.md rules in <important if="..."> tags to stop Claude from ignoring them as files grow longer | Dex |
|---|---|
| use multiple CLAUDE.md for monorepos — ancestor + descendant loading | Boris |
| use .claude/rules/ to split large instructions | Claude |
 
  
use .claude/rules/ to split large instructionsClaude
CLAUDE.md is missing essential setup/build/test commands
keep codebases clean and finish migrations — partially migrated frameworks confuse models that might pick the wrongBoris
pattern Video
in CLAUDE.md when attribution.commit: "" is deterministic
Agents (4)

---

## Page 8

|  | Tip | Source |
|---|---|---|
| have feature specific sub-agents (extra context) with skills (progressive disclosure) instead of general qa, backend engineer |  | Boris |
| say "use subagents" to throw more compute at a problem — offload tasks to keep your main context clean and focused 🚫 👶 |  | Boris |
| agent teams with tmux and git worktrees for parallel development |  | Boris |
# Tip Source
have feature specific sub-agents (extra context) with skills (progressive disclosure) instead of general qa, backend engineerBoris
  
agent teams with tmux and git worktrees for parallel developmentBoris
# use test time compute — separate context windows make results better; one agent can cause bugs and another (same model)
# can find them
# Commands (3)
# Tip Source
use commands for your workflows instead of sub-agentsBoris
# use slash commands for every "inner loop" workflow you do many times a day — saves repeated prompting, commands live in
Boris
# .claude/commands/ and are checked into git
# if you do something more than once a day, turn it into a skill or command — build /techdebt, context-dump, or analytics
Boris
# commands
# Skills (9)
# Tip Source
# use context: fork to run a skill in an isolated subagent — main context only sees the final result, not intermediate tool calls. The
Lydia
# agent field lets you set the subagent type
use skills in subfolders for monoreposClaude
skills are folders, not files — use references/, scripts/, examples/ subdirectories for progressive disclosureThariq
build a Gotchas section in every skill — highest-signal content, add Claude's failure points over timeThariq
skill description field is a trigger, not a summary — write it for the model ("when should I fire?")Thariq
don't state the obvious in skills — focus on what pushes Claude out of its default behavior 🚫👶Thariq
don't railroad Claude in skills — give goals and constraints, not prescriptive step-by-step instructions 🚫👶Thariq
include scripts and libraries in skills so Claude composes rather than reconstructs boilerplateThariq
# embed !command in SKILL.md to inject dynamic shell output into the prompt — Claude runs it on invocation and the model
Lydia
# only sees the result
# ■ Hooks (5)
|  | Tip | Source |
|---|---|---|
| use on-demand hooks in skills — /careful blocks destructive commands, /freeze blocks edits outside a directory |  | Thariq |
| measure skill usage with a PreToolUse hook to find popular or undertriggering skills |  | Thariq |
# Tip Source
 
measure skill usage with a PreToolUse hook to find popular or undertriggering skillsThariq
# use a PostToolUse hook to auto-format code — Claude generates well-formatted code, the hook handles the last 10% to avoid
Boris
# CI failures
route permission requests to Opus via a hook — let it scan for attacks and auto-approve safe ones 🚫👶Boris
use a Stop hook to nudge Claude to keep going or verify its work at the end of a turnBoris
# ■ Workflows (5)
# Tip Source
# use /model to select model and reasoning, /context to see context usage, /usage to check plan limits, /extra-usage to
Cat
# configure overflow billing, /config to configure settings — use Opus for plan mode and Sonnet for code to get the best of both

---

## Page 9

Tip Source
always use thinking mode true (to see reasoning) and Output Style Explanatory (to see detailed output with Insight boxes) in /config for better understanding of Claude's decisions
use ultrathink keyword in prompts for high effort reasoningClaude
/focus mode hides all intermediate work and shows only the final result — trust the model to run the right commands and just look at the outcome (toggle with /focus)
medium · high · xhigh · max)
■ Workflows Advanced (9)
Tip Source
use ASCII diagrams a lot to understand your architectureBoris
your machine is off
use Ralph Wiggum plugin for long-running autonomous tasksBoris
/permissions with wildcard syntax (Bash(npm run *), Edit(/docs/**)) instead of dangerously-skip-permissionsBoris
Cat
invest in product verification skills (signup-flow-driver, checkout-verifier) — worth spending a week to perfectThariq
auto-approves, pauses and asks if risky. Shift+Tab to cycle Ask → Plan → Auto modes 🚫👶
a recommended allowlist to paste into settings
come back, you know the code works 🚫👶
■ Git / PR (5)
Tip Source
review and revert
always squash merge PRs — clean linear history, one commit per feature, easy git revert and git bisectBoris
commit often — try to commit at least once per hour, as soon as task is completed, commitShayan
tag @claude on a coworker's PR to auto-generate lint rules for recurring review feedback — automate yourself out ofBoris
code review 🚫👶 Video
use /code-review for multi-agent PR analysis — catches bugs, security vulnerabilities, and regressions before mergeBoris
■ Debugging (6)
Tip Source
|  | Tip | Source |
|---|---|---|
| make it a habit to take screenshots and share with Claude whenever you are stuck with any issue |  | Shayan |
| use mcp (Claude in Chrome, Playwright, Chrome DevTools) to let claude see chrome console logs on its own |  | Claude |
| always ask claude to run the terminal (you want to see logs of) as a background task for better debugging |  | Shayan |
| /doctor to diagnose installation, authentication, and configuration issues |  | Shayan |
make it a habit to take screenshots and share with Claude whenever you are stuck with any issueShayan
use mcp (Claude in Chrome, Playwright, Chrome DevTools) to let claude see chrome console logs on its ownClaude
always ask claude to run the terminal (you want to see logs of) as a background task for better debuggingShayan
/doctor to diagnose installation, authentication, and configuration issuesShayan

---

## Page 10

Tip Source
|  | Tip | Source |
|---|---|---|
| use a cross-model for QA — e.g. Codex for plan and implementation review |  | Shayan |
| agentic search (glob + grep) beats RAG — Claude Code tried and discarded vector databases because code drifts out of |  | Boris |
| sync and permissions are complex |  | Video |
 
agentic search (glob + grep) beats RAG — Claude Code tried and discarded vector databases because code drifts out ofBoris
■ Utilities (5)
|  | Tip | Source |  |
|---|---|---|---|
| iTerm/ Ghostty/tmux terminals instead of IDE (VS Code/Cursor) |  | Boris |  |
| /voice or Wispr Flow for voice prompting (10x productivity) |  | Boris |  |
| claude-code-hooks for claude feedback |  | Shayan |  |
| status line for context awareness and fast compacting |  | Boris | Shayan |
| explore settings.json features like Plans Directory, Spinner Verbs for a personalized experience |  | Boris |  |
Tip Source
iTerm/Ghostty/tmux terminals instead of IDE (VS Code/Cursor)Boris
 
claude-code-hooks for claude feedbackShayan
status line for context awareness and fast compactingBoris Shayan
   
■ Daily (2)
|  | Tip | Source |
|---|---|---|
| update Claude Code daily |  | Shayan |
| start your day by reading the changelog |  | Shayan |
Tip Source
update Claude Code dailyShayan
 
Claude
|  | Article / Tweet | Source |
|---|---|---|
| 6 Tips for Getting More Out of Opus 4.7 (Boris) \| 1 6 /Apr/2 6 |  | Tweet |
| Session Management & 1M Context (Thariq) \| 1 6 /Apr/2 6 |  | Tweet |
| 15 Hidden & Under-Utilized Features in Claude Code (Boris) \| 30/Mar/2 6 |  | Tweet |
| Squash Merging & PR Size Distribution (Boris) \| 25/Mar/2 6 |  | Tweet |
| Lessons from Building Claude Code: How We Use Skills (Thariq) \| 17/Mar/2 6 |  | Article |
| Code Review & Test Time Compute (Boris) \| 10/Mar/2 6 |  | Tweet |
| /loop — schedule recurring tasks for up to 3 days (Boris) \| 07 Mar 202 6 |  | Tweet |
| AskUserQuestion + ASCII Markdowns (Thariq) \| 2 8 Feb 202 6 |  | Tweet |
| Seeing like an Agent - lessons from building Claude Code (Thariq) \| 2 8 Feb 202 6 |  | Article |
| Git Worktrees - 5 ways how boris is using \| 21 Feb 202 6 |  | Tweet |
| Lessons from Building Claude Code: Prompt Caching Is Everything (Thariq) \| 20 Feb 202 6 |  | Article |
| 12 ways how people are customizing their claudes (Boris) \| 12/Feb/2 6 |  | Tweet |
| 10 tips for using Claude Code from the team (Boris) \| 01/Feb/2 6 |  | Tweet |
| How I use Claude Code — 13 tips from my surprisingly vanilla setup (Boris) \| 03/Jan/2 6 |  | Tweet |
| Ask Claude to interview you using AskUserQuestion tool (Thariq) \| 2 8 /Dec/25 |  | Tweet |
| Always use plan mode, give Claude a way to verify, use /code-review (Boris) \| 27/Dec/25 |  | Tweet |
Article / Tweet Source
 
Session Management & 1M Context (Thariq) | 16/Apr/26 Tweet
15 Hidden & Under-Utilized Features in Claude Code (Boris) | 30/Mar/26 Tweet
Squash Merging & PR Size Distribution (Boris) | 25/Mar/26 Tweet
Lessons from Building Claude Code: How We Use Skills (Thariq) | 17/Mar/26 Article
Code Review & Test Time Compute (Boris) | 10/Mar/26 Tweet
 
 
 
Git Worktrees - 5 ways how boris is using | 21 Feb 2026 Tweet
Lessons from Building Claude Code: Prompt Caching Is Everything (Thariq) | 20 Feb 2026 Article
12 ways how people are customizing their claudes (Boris) | 12/Feb/26 Tweet
10 tips for using Claude Code from the team (Boris) | 01/Feb/26 Tweet
 
Ask Claude to interview you using AskUserQuestion tool (Thariq) | 28/Dec/25 Tweet
Always use plan mode, give Claude a way to verify, use /code-review (Boris) | 27/Dec/25 Tweet
Tips from Claude code CLI binary
Spinner Verbs & Tips (extracted from CLI binary v2.1.121)

---

## Page 11

# 🎬 VIDEOS / PODCASTS
|  | Video / Podcast | Source | YouTube |
|---|---|---|---|
| From Vibe Coding to Agentic Engineering (Andrej) \| 02 May 202 6 \| AI Engineer |  | Karpathy | YouTube |
| Full Walkthrough: Workflow for AI Coding (Matt) \| 24 Apr 202 6 \| Matt Pocock |  | Matt | YouTube |
| Everything We Got Wrong About Research-Plan-Implement (Dex) \| 24 Mar 202 6 \| MLOps Community |  | Dex | YouTube |
| Building Claude Code with Boris Cherny (Boris) \| 04 Mar 202 6 \| The Pragmatic Engineer |  | Boris | YouTube |
| Head of Claude Code: What happens after coding is solved (Boris) \| 19 Feb 202 6 \| Lenny's Podcast |  | Boris | YouTube |
| Inside Claude Code With Its Creator Boris Cherny (Boris) \| 17 Feb 202 6 \| Y Combinator |  | Boris | YouTube |
| Boris Cherny (Creator of Claude Code) On What Grew His Career (Boris) \| 15 Dec 2025 \| Ryan Peterman |  | Boris | YouTube |
| The Secrets of Claude Code From the Engineers Who Built It (Cat) \| 29 Oct 2025 \| Every |  | Boris | YouTube |
# Video / Podcast Source YouTube
 
 
 
 
 
 
Boris Cherny (Creator of Claude Code) On What Grew His Career (Boris) | 15 Dec 2025 | Ryan PetermanBorisYouTube
The Secrets of Claude Code From the Engineers Who Built It (Cat) | 29 Oct 2025 | EveryBorisYouTube
# 🔔 SUBSCRIBE
| Source |  | Name | Badge |
|---|---|---|---|
|  | r/ClaudeAI, r/ClaudeCode, r/Anthropic |  | Claude |
|  | Claude, Claude Devs, Anthropic, Boris, Thariq, Cat, Lydia, Noah, Anthony, Alex, Kenneth |  | Claude |
# Source Name Badge
r/ClaudeAI, r/ClaudeCode, r/AnthropicClaude
  
# Jesse Kriss (Superpowers), Affaan Mustafa (ECC), Garry Tan (gstack), Dex Horthy (HumanLayer), Kieran Klaassen
# (Compound Eng), Tabish Gilani (OpenSpec), Brian McAdams (BMAD), Lex Christopherson (GSD), Matt Pocock
Community
# (Skills), Dani Avila (CC Templates), Dan Shipper (Every), Andrej Karpathy (AutoResearch), Peter Steinberger
# (OpenClaw), Sigrid Jin (claw-code), Yeachan Heo (oh-my-claudecode)
AnthropicClaude
Lenny's Podcast, Y Combinator, The Pragmatic Engineer, Ryan Peterman, Every, MLOps CommunityCommunity
# STARTUPS / BUSINESSES
| Claude |  | Replaced |
|---|---|---|
| Code Review | Greptile, CodeRabbit, Devin Review, OpenDiff, Cursor BugBot |  |
| Voice Dictation | Wispr Flow, SuperWhisper |  |
| Remote Control | OpenClaw |  |
| Claude in Chrome | Playwright MCP, Chrome DevTools MCP |  |
| Computer Use | OpenAI CUA |  |
| Cowork | ChatGPT Agent, Perplexity Computer, Manus |  |
| Tasks | Beads |  |
| Plan Mode | Agent OS |  |
# Claude Replaced
  
 
# Remote Control OpenClaw
# Claude in Chrome Playwright MCP, Chrome DevTools MCP
# Computer Use OpenAI CUA
# Cowork ChatGPT Agent, Perplexity Computer, Manus
# Tasks Beads
# Plan Mode Agent OS

---

## Page 12

Claude Replaced
| Claude |  | Replaced |
|---|---|---|
| Design | Figma, Framer, Sketch, v0 |  |
| Agent SDK | LangChain, LangGraph, CrewAI, AutoGen, OpenAI Assistants API |  |
| Skills / Plugins | YC AI wrapper startups (reddit) |  |
Design Figma, Framer, Sketch, v0
Agent SDK LangChain, LangGraph, CrewAI, AutoGen, OpenAI Assistants API
Skills / Plugins YC AI wrapper startups (reddit)
### Billion-Dollar Questions
If you have answers, do let me know at shanraisshan@gmail.com
Memory & Instructions (4)
1. What exactly should you put inside your CLAUDE.md — and what should you leave out?
2. If you already have a CLAUDE.md, is a separate constitution.md or rules.md actually needed?
3. How often should you update your CLAUDE.md, and how do you know when it's become stale?
4. Why does Claude still ignore CLAUDE.md instructions — even when they say MUST in all caps? (reddit)
Agents, Skills & Workflows (6)
1. When should you use a command vs an agent vs a skill — and when is vanilla Claude Code just better?
2. How often should you update your agents, commands, and workflows as models improve?
3. Should you have a generalist subagent or a feature-specific/role-specific agent? Does giving your subagent a detailed persona improve quality, and what does a "perfect persona prompt" for research/vision look like?
4. Should you rely on Claude Code's built-in plan mode — or build your own planning command/agent that enforces your team's workflow?
5. If you have a personal skill (e.g., /implement with your coding style), how do you incorporate community skills (e.g., /simplify) without conflicts — and who wins when they disagree?
6. Are we there yet? Can we convert an existing codebase into specs, delete the code, and have AI regenerate the exact same code from those specs alone?
Specs & Documentation (3)
1. Should every feature in your repo have a spec as a markdown file?
2. How often do you need to update specs so they don't become obsolete when a new feature is implemented?
3. When implementing a new feature, how do you handle the ripple effect on specs for other features?
### 🤔 Does code matter?
### REPORTS
A G E N T S D K V S C L I B R O W S E R A U T O M A T I O N M C P G L O B A L V S P R O J E C T S E T T I N G S S K I L L S I N M O N O R E P O S
A G E N T M E M O R Y A D V A N C E D T O O L U S E U S A G E & R A T E L I M I T S A G E N T S V S C O M M A N D S V S S K I L L S
L L M D E G R A D A T I O N W H Y H A R N E S S I S I M P O R T A N T S P I N N E R V E R B S & T I P S
How to Use
Get the maximum out of this repo by following these steps:

---

## Page 13

1. Read this repo as a course, not as a workflow or skill. It's reference material first; you'll run things later.
2. Don't use Claude as a chatbot. Learn the primitives — agents, commands, skills, hooks — and assemble them into your own workflow.
3. Run /weather-orchestrator to see a complete command agent skill flow. Use it as a template for any dev workflow, from planning
to shipping.
like Agent Teams ship inside this repo's implementation/ directory.
5. Learn the advanced topics and their implementations from the 🔥 Hot sub-table — for example, the Ralph Wiggum self-evolving loop is a full working repo you can clone to see one of these patterns end-to-end.
CLAUDE.md . Every tip is sourced from the Claude team or the community.
7. Subscribe to the Reddit and YouTube channels in the Subscribe section to keep up with the community.
🎬 Videos
📊 Presentations
Trending on Github in March 2026
### Star History
Star History Chart
6 4 k stars and counting

---

## Page 14

### Other Repos
Claude Code
Codex CLI Codex CLI Gemini CLI Gemini CLI
Best Practice Hooks Best Practice Hooks
### Developed by
This project is 100% autopilot and developed by Claude Code
# Workflow Description
Update the DEVELOPMENT WORKFLOWS table and cross-workflow analysis report 1 /workflows:development-workflows by researching all 10 workflow repos in parallel
Update the SKILL COLLECTIONS table by researching all 5 skill-collection repos in 2 /workflows:skill-collections parallel
Update the AGENT COLLECTIONS table by researching all agent-collection repos 3 /workflows:agent-collections in parallel
/workflows:best-practice:workflow-Update the README CONCEPTS section with the latest Claude Code features and 4 concepts concepts
/workflows:best-practice:workflow-5 Track Claude Code settings report changes and find what needs updating claude-settings
/workflows:best-practice:workflow-6 Track Claude Code subagents report changes and find what needs updating claude-subagents
/workflows:best-practice:workflow-7 Track Claude Code commands report changes and find what needs updating claude-commands
/workflows:best-practice:workflow-f
Releases
No releases published Create a new release
Packages
No packages published Publish your first package
Contributors
No contributors
Languages
HTML 95.5% Python 4.5%
Suggested workflows
Based on your tech stack
Jekyll using Docker image Configure Package a Jekyll site using the jekyll/builder Docker image. By GitHub Actions
SLSA Generic generator Configure

---

## Page 15

Generate SLSA3 provenance for your existing release workflows
By Open Source Security Foundation (OpenSSF)
Pylint Configure Lint a Python application with pylint.
By GitHub Actions
More workflows