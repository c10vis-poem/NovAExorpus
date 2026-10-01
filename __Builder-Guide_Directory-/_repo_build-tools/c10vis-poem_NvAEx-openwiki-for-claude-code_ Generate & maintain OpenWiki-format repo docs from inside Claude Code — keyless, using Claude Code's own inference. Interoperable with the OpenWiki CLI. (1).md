<!-- Converted from c10vis-poem_NvAEx-openwiki-for-claude-code_ Generate & maintain OpenWiki-format repo docs from inside Claude Code — keyless, using Claude Code's own inference. Interoperable with the OpenWiki CLI. (1).pdf — 3 pages -->

## Page 1

NvAEx-openwiki-for-claude-code
Code Pull requests Agents Actions Projects Wiki Security and quality Insights
Settings
Watch 0 Fork 0
# Generate & maintain OpenWiki-format repo docs from inside Claude Code — keyless, using Claude Code's own
# inference. Interoperable with the OpenWiki CLI.
MIT License
0 stars 0 forks 0 watching 1 branch 0 tags Activity
Public repository · Forked from jatinmayekar/openwiki-for-claude-code
1 Branch 0 Tags Go to file T Go to file Add file Code
This branch is up to date with jatinmayekar/openwiki-for-claude-code:master . Contribute Sync fork
| jatinmayekar and claude feat: OpenWiki for Claude Code — keyless native plugin |  |  | 33e9d93 · 2 months ago |
|---|---|---|---|
| .claude-plugin | feat: OpenWiki for Claude Code — k … | 2 months ago |  |
| plugins/openwiki | feat: OpenWiki for Claude Code — k … | 2 months ago |  |
| .gitignore | feat: OpenWiki for Claude Code — k … | 2 months ago |  |
| LICENSE | feat: OpenWiki for Claude Code — k … | 2 months ago |  |
| README.md | feat: OpenWiki for Claude Code — k … | 2 months ago |  |
    
 
 
 
 
 
README License
# OpenWiki for Claude Code
# A Claude Code plugin marketplace that brings OpenWiki into Claude Code — generating and maintaining
# agent-facing repo documentation using Claude Code's own inference, with no separate API key.
# OpenWiki is LangChain's tool for writing and maintaining docs "built specifically for agents." Its CLI
# needs its own paid inference key. Claude Code users already pay for inference — so this plugin makes
# the Claude Code agent itself the engine, producing the exact same on-disk format so the two are
# interoperable.

---

## Page 2

## Install
/plugin marketplace add jatinmayekar/openwiki-for-claude-code /plugin install openwiki@openwiki-for-claude-code
### Then:
| /openwiki:generate | # build the wiki |
|---|---|
| /openwiki:update | # refresh it from recent commits |
| /openwiki:ask <question> | # ask the wiki |
| /openwiki:schedule | # keep it fresh automatically (keyless) |
/openwiki:generate # build the wiki /openwiki:update # refresh it from recent commits /openwiki:ask <question> # ask the wiki /openwiki:schedule # keep it fresh automatically (keyless)
## What you get
openwiki/quickstart.md + focused section pages (architecture, workflows, domain, operations,
### testing, …) — evidence-grounded, with inline source references.
openwiki/.last-update.json run metadata and an AGENTS.md / CLAUDE.md reference section, in the
### exact shape the OpenWiki CLI uses.
### Surgical, git-diff-driven updates and a no-op when nothing relevant changed.
plugins/openwiki/README.md See for details and plugins/openwiki/reference/openwiki-format.md for
### the format spec.
## Two audiences
### Claude Code users get OpenWiki-style docs natively and keyless.
### Existing OpenWiki users can drive/refresh their wikis from Claude Code workflows; because the format
### matches, the CLI and this plugin can maintain the same wiki interchangeably.
## Repository layout
.claude-plugin/marketplace.json # marketplace catalog plugins/openwiki/ # the plugin .claude-plugin/plugin.json skills/{generate,update,ask,schedule}/SKILL.md reference/openwiki-format.md # shared format spec (distilled from upstream) README.md
## Relationship to upstream OpenWiki
### This project reimplements OpenWiki's methodology and on-disk format (from
### langchain-ai/openwiki ,
### MIT) so a host coding agent can be the inference engine. It ships standalone; it is also intended as a
### proposal to upstream as an "OpenWiki Claude Code mode." Not affiliated with or endorsed by LangChain.

---

## Page 3

## License
### Releases
No releases published Create a new release
### Packages
No packages published Publish your first package
### Contributors
No contributors