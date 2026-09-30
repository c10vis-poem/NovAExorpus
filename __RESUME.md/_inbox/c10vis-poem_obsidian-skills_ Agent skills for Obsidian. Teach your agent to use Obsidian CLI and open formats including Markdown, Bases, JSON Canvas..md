<!-- Converted from c10vis-poem_obsidian-skills_ Agent skills for Obsidian. Teach your agent to use Obsidian CLI and open formats including Markdown, Bases, JSON Canvas..pdf — 2 pages -->

## Page 1

c10vis-poem obsidian-skills
Code Pull requests 1 Agents Actions Projects Wiki Security and quality Insights Settings
Watch 0 Fork 0
# Agent skills for Obsidian. Teach your agent to use Obsidian CLI and open formats including Markdown, Bases, JSON Canvas.
MIT License
0 stars 0 forks 0 watching 2 branches 0 tags Activity
Public repository · Forked from kepano/obsidian-skills
m… 2 Branches 0 Tags Go to file T Go to file Add file Code
This branch is 2 commits ahead of kepano/obsidian-skills:main . Contribute Sync fork
| Detail |  | Selection | Default cap |
|---|---|---|---|
| c10vis-poem Merge branch 'kepano:main' into main |  |  | 47cf064 · now |
| .claude-plugin | chore: update plugin version so it can be up … | 7 months ago |  |
| .github/workflows | ci: add CI workflow with gitleaks secret scan | 3 weeks ago |  |
| skills | Merge pull request kepano#143 from vladim … | 2 weeks ago |  |
| LICENSE | license | 8 months ago |  |
| README.md | Add Knap skill | 2 weeks ago |  |
 
 
 
 
LICENSE license 8 months ago
README.md Add Knap skill 2 weeks ago
README License
# Agent Skills for use with Obsidian.
# These skills follow the Agent Skills specification so they can be used by any skills-compatible agent, including Claude Code, Codex, and Open
# Code.
# Installation
# Marketplace
/plugin marketplace add kepano/obsidian-skills /plugin install obsidian@obsidian-skills
# npx skills
npx skills add git@github.com:kepano/obsidian-skills.git
# Instead of ssh, if you prefer to use https:
npx skills add https://github.com/kepano/obsidian-skills
# Manually
# Claude Code

---

## Page 2

Add the contents of this repo to a /.claude folder in the root of your Obsidian vault (or whichever folder you're using with Claude Code). See
# more in the official Claude Skills documentation.
# Codex
skills/ Copy the directory into your Codex skills path (typically ~/.codex/skills ). See the Agent Skills specification for the standard skill
# format.
# OpenCode
Clone the entire repo into the OpenCode skills directory ( ~/.opencode/skills/ ):
git clone https://github.com/kepano/obsidian-skills.git ~/.opencode/skills/obsidian-skills
skills/ Do not copy only the inner folder — clone the full repo so the directory structure is ~/.opencode/skills/obsidian-
skills/skills/<skill-name>/SKILL.md .
SKILL.md ~/.opencode/skills/ OpenCode auto-discovers all files under . No changes to opencode.json or any config file are needed.
# Skills become available after restarting OpenCode.
# Skills
# Skill Description
obsidian- Create and edit Obsidian Flavored Markdown ( .md ) with wikilinks, embeds, callouts, properties, and other Obsidian-
# markdown
# specific syntax
obsidian-bases Create and edit Obsidian Bases ( .base ) with views, filters, formulas, and summaries
json-canvas Create and edit JSON Canvas files ( .canvas ) with nodes, edges, groups, and connections
# obsidian-cli Interact with Obsidian vaults via the Obsidian CLI including plugin and theme development
# defuddle Extract clean markdown from web pages using Defuddle, removing clutter to save tokens
# knap Render Markdown templates from JSON or CSV data using Knap, including batch file generation
# Releases
No releases published Create a new release
# Packages
No packages published Publish your first package
# Contributors
No contributors