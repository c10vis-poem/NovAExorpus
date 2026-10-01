<!-- Converted from c10vis-poem_NvAEx-openwiki-skills_ OpenWiki ported to agent skills — generate and maintain a codebase wiki with Claude Code, Codex, or Gemini CLI. No API token needed..pdf — 2 pages -->

## Page 1

NvAEx-openwiki-skills
Code Pull requests Agents Actions Projects Wiki Security and quality Insights
Settings
Watch 0 Fork 0
# OpenWiki ported to agent skills — generate and maintain a codebase wiki with Claude Code, Codex, or Gemini CLI. No
# API token needed.
MIT License
0 stars 0 forks 0 watching 1 branch 0 tags Activity
Public repository · Forked from kinensake/openwiki-skills
1 Branch 0 Tags Go to file T Go to file Add file Code
This branch is up to date with kinensake/openwiki-skills:main . Contribute Sync fork
| kinensake Rename skills to openwiki-init and openwiki-update |  |  | 1c44826 · 2 months ago |
|---|---|---|---|
| skills | Rename skills to openwiki-init and o … | 2 months ago |  |
| .gitignore | Port OpenWiki prompts to self-cont … | 2 months ago |  |
| LICENSE | Initial commit | 2 months ago |  |
| README.md | Rename skills to openwiki-init and o … | 2 months ago |  |
 
 
 
LICENSE Initial commit 2 months ago
 
README License
# OpenWiki Skills
OpenWiki ported to agent skills — generate and maintain a codebase wiki ( openwiki/ ) with the coding
# agent you already use, no API token or separate CLI required.
# The original OpenWiki is a standalone CLI agent (deepagents/LangGraph) that needs a provider config and
# API key. This repo extracts its prompts and repackages them as two self-contained skills following the
# Claude Code skill format (also supported by Codex and Gemini CLI), with the content neutralized to run on all
# three.

---

## Page 2

### Install
npx skills add kinensake/openwiki-skills --all
### Usage
In the repository you want to document:
— generate the wiki into : /openwiki-init openwiki/ quickstart.md as the entrypoint plus up to ~8 focused section pages, add a wiki reference section to / AGENTS.md CLAUDE.md , and record run metadata in openwiki/.last-update.json .
/openwiki-update — run periodically after code changes: performs a no-op check first (clean worktree + unchanged git head → stops immediately), diffs against the previous run, and surgically edits only the affected pages.
Both accept extra instructions, e.g. /openwiki-update focus on the new auth module .
### Credits
Releases
No releases published Create a new release
Packages
No packages published Publish your first package
Contributors
No contributors