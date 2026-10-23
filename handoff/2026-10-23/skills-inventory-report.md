# Skills inventory + install plan (Phase 1, read-only) 2026-10-23

Pattern in use now (settings.json extraKnownMarketplaces + plugins/known_marketplaces.json): `"source":{"source":"directory","path":"~/repos/<clone>"}` for obsidian-skills, claude-video, happy-ending, openwiki-for-claude-code, obsidian-wiki, llm-wiki-compiler; `"source":"github","repo":"c10vis-poem/..."` for greenpt (honey), mem0-plugins, mattpocock, netresearch, android-reverse-engineering. Search for "directory-marketplace" / "marketplace.json" in session-work, vault PENDING.md/RESUME.md and the memory dir: not found by grep of those paths. The pattern is inferred from config only.

"Behind" = fork commits missing vs upstream default branch (gh compare).

| Pack | Local path | Fork (c10vis-poem) | Upstream | Manifest | Skills | Installed? | Fork behind / ahead |
|---|---|---|---|---|---|---|---|
| obsidian-skills (kepano) | ~/repos/obsidian-skills | obsidian-skills | kepano/obsidian-skills | marketplace+plugin | 6 upstream (defuddle json-canvas knap bases cli markdown); local dir ALSO has aesop-wiki, horizons-repo-skill, memory-as-skill, termux-helper (local additions) | yes obsidian@obsidian-skills 1.0.1, enabled | 0 / 4 ahead |
| obsidian-wiki (Ar9av) | ~/repos/AEsops-obsidian-wiki | AEsops-obsidian-wiki | Ar9av/obsidian-wiki | marketplace+plugin (skills: ./.skills/) | 40 in .skills | project scope only (wiki-admin), not in enabledPlugins | 25 behind / 0 |
| openwiki-for-claude-code (jatinmayekar) | ~/repos/NvAEx-openwiki-for-claude-code | NvAEx-openwiki-for-claude-code | jatinmayekar/openwiki-for-claude-code | marketplace (plugin at plugins/openwiki) | 4 (ask generate schedule update) | yes user + wiki-admin v0.1.0, enabledPlugins=false | 0 / 0 |
| openwiki-skills (kinensake) | NOT cloned | NvAEx-openwiki-skills | kinensake/openwiki-skills | none (README, skills/ dir) | unknown | no | 0 / 0 |
| openwiki (langchain) | ~/repos/openwiki | openwiki | langchain-ai/openwiki | none | 4 SKILL.md; also bare ~/.claude/skills/openwiki | skill dir only | not checked |
| llm-wiki-nocode (rosidotidev) = likely "OpenWiki no-code" (unconfirmed) | ~/repos/NvAEx-llm-wiki-nocode | NvAEx-llm-wiki-nocode | rosidotidev/llm-wiki-nocode | none; .claude/commands (wiki-ingest, wiki-lint, wiki-query) | 0 SKILL.md, 3 commands | no | 0 / 0 |
| llm-wiki-compiler (ussumant) | ~/repos/llm-wiki-compiler-NvAEx | llm-wiki-compiler-NvAEx | ussumant/llm-wiki-compiler | marketplace (plugin ./plugin) | 1 | project scope (wiki-admin) v2.1.0, not enabled | 0 / 0 |
| Obsidian Tars | NOT cloned | AEsopXi-obsidian-tars | TarsLab/obsidian-tars | none (Obsidian app plugin: manifest.json, TypeScript) | 0, not a Claude skill pack | no | 0 / 0 |
| graphify | ~/repos/graphify | graphify (default branch v8) | Graphify-Labs/graphify | none in repo | bare skill at ~/.claude/skills/graphify (listing denied); repo has graphify/skills/{claude,codex,...} per-agent dirs | skill yes, not a plugin | 330 behind / 0 |
| graphify "plugin for Obsidian" | - | - | - | - | - | - | not found by: gh repo list c10vis-poem, ls ~/repos |
| notebooklm-py | ~/repos/notebooklm-py | notebooklm-py | teng-lin/notebooklm-py | none | 1 root SKILL.md (+ bare ~/.claude/skills/notebooklm) | skill yes, not a plugin | 18 behind / 0 |
| honey-for-devs | ~/repos/NoVa-honey-for-devs (also honey-main) | NvAEx-honey-for-devs | Green-PT/honey-for-devs | marketplace "greenpt" + plugin | ~14 in skills/ | yes honey@greenpt 1.4.0 enabled; bare ~/.claude/skills/honey* symlinks point at stale cache 1.3.1 | 0 / 5 ahead |
| mem0 | ~/repos/clovis-mem0-vingiaN | clovis-mem0-vingiaN | mem0ai/mem0 | marketplace "mem0-plugins" | plugin mem0 0.3.3 (+ memory-triage symlink) | yes enabled | 3 behind / 9 ahead |
| MemVault | NOT cloned | NO FORK | dreamor/MemVault (not itself a fork; branch master) | .claude-plugin/marketplace.json (plugin memvault, ./plugins/memvault, 18 MCP tools) | n/a | no | needs fork |
| claude-mem | NOT cloned | NO FORK | thedotmack/claude-mem | marketplace + plugin | n/a | no | needs fork |
| agentmem(ory) | NOT cloned | NO FORK for rohitg00/agentmemory (has marketplace.json). Related fork AEsopXi-codex-agent-mem (MarceloCaporale/codex-agent-mem, 0/0) | rohitg00/agentmemory is unconfirmed as the operator's "agentmem" | marketplace | n/a | no | ask operator which |
| pmm | account-synced plugin (marketplace anthropic-plugin-directory); dir ~/.claude/plugins/synced/a5d13a90-.../b907fbde-.../pmm | none | not a git repo here | cloud-synced | 12 pmm:* skills (dump hydrate init init-local-skills onboard query recall save settings status update viz) | yes (synced from claude.ai account) | no fork possible |
| memsearch | ~/repos/memsearch-aesop | memsearch-aesop | zilliztech/memsearch | marketplace | 17 SKILL.md | no | 17 behind / 0 |
| terrestrial-brain | ~/repos/NovA-terrestrial-brain | NvAEx-terrestrial-brain | TerrestrialOrigin/terrestrial-brain | not checked | not checked | MCP server (timed out this session), not a plugin | 0 / 7 ahead |
| OB1 | ~/repos/OB1 | OB1 | NateBJones-Projects/OB1 | none | 26 SKILL.md | no | not checked |
| pm-claude-skills | ~/repos/pm-claude-skills | pm-claude-skills | mohitagw15856/pm-claude-skills | marketplace | not counted | no | not checked |

"terrestrial-brain obsidian plugin": not found by gh repo list c10vis-poem and ls ~/repos (only the NovA-terrestrial-brain clone, not inspected).

## Conflicts / overlaps
- Name collisions: `skill-creator` (obsidian-wiki .skills vs anthropic-skills:skill-creator); `memory-as-skill`, `termux-helper` (local additions in the obsidian-skills clone vs anthropic-skills:* and bare ~/.claude/skills/termux-helper). Remove or namespace the local additions. Plugin skills are namespaced plugin:skill, so collisions are mostly with bare ~/.claude/skills entries (honey*, graphify, notebooklm, openwiki, memory-triage).
- openwiki: bare ~/.claude/skills/openwiki vs openwiki plugin (disabled) vs langchain-ai/openwiki vs kinensake/openwiki-skills. Pick one primary.
- Memory hooks: mem0 plugin (enabled) vs claude-mem / MemVault / agentmemory each add SessionStart/Stop hooks that inject context. More than one active doubles injection and token cost. pmm is a fifth memory path. Recommend one auto-capture hook pack; others skills-only or off.
- obsidian-wiki, llm-wiki-compiler, llm-wiki-nocode all implement the Karpathy LLM-wiki pattern (wiki-ingest/query/lint names repeat).
- honey bare symlinks target cache 1.3.1 while the plugin is 1.4.0: stale.

## Install plan (each step after operator approval; `gh repo sync c10vis-poem/<repo>` first, report the commit, then `git pull` in the clone)
Directory-marketplace pattern: add `{source:directory,path:~/repos/<clone>}` to extraKnownMarketplaces, then `claude plugin marketplace add <path>` and `claude plugin install <plugin>@<marketplace>`.
1. Already wired, just sync: obsidian-skills (PR its 4 ahead commits and move the local-addition skills out), honey (greenpt), mem0-plugins (sync 3 behind; 9 ahead go through PR to fork main).
2. Sync + refresh: AEsops-obsidian-wiki (25 behind), then `claude plugin marketplace update obsidian-wiki`; decide user scope vs wiki-admin only.
3. Enable decision: openwiki@openwiki-for-claude-code (installed, disabled).
4. Need a manifest first (PR to fork adding .claude-plugin/): graphify, notebooklm-py, llm-wiki-nocode; clone and inspect NvAEx-openwiki-skills.
5. New forks needed (`gh repo fork` dreamor/MemVault, thedotmack/claude-mem, rohitg00/agentmemory, naming per NvAEx-* convention), clone, add directory marketplace, install one at a time. Do not enable all memory hook packs together.
6. Obsidian Tars: Obsidian app plugin, not installable via claude plugin; leave as fork only.
7. pmm: no action (account-synced).
Order: 1, 2, 3, 4, then 5 with a hook-overlap review.
Every manifest change ships via branch, secret scan, push, PR, CI, auto-merge.

## Not read / not done
~/.claude/skills/graphify (permission denied on listing), the home-dir claude.json (excluded by instruction), contents of kinensake/openwiki-skills beyond top level, pm-claude-skills and OB1 detail, sync status for openwiki / OB1 / pm-claude-skills. No installs or config changes made.
