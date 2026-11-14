---
name: memory-as-skill-design
description: User's target design (2026-10-29) for memory-as-skill v-next — corpus pointers, per-repo standard files, manifest.jsonl, extraction-route script, always-on hooks
metadata:
  type: project
  modified: 2026-10-29T07:53:21.818Z
---

The user's design, from 2026-10-29. Not built yet; any text needs their sign-off first.

- memory-as-skill (possibly several skills) carries more than a pointer:
  - the **manifest.jsonl** for the corpus repo's memory layers
  - a **script that picks the right extraction route** for what's needed
  - pointers to Recaps
- The **corpus repo (NovAExorpus vault) holds pointers to every other repo**.
- **Every repo keeps its own** MEMORY.md, RESUME.md, AGENTS.md, PENDING.md, handoffs, a settings .jsonl, a skills manifest.json, MAP.md and manifest.jsonl.
- "Memory persists as skills, hooks and scripts": a **SessionStart load on every session, wherever it starts**, plus a **Stop hook**.
- The D.U.M.B.A.S.S. routing logic gets mapped later and will cover this too.
- The user wants Claude fluent in their **memory plugins** (MD writing), **prompt-engineering plugins**, **data retention** and **file compilation** plugins, used as parts to mix and match.

2026-10-29 design brief (awaiting sign-off on 9 open questions): https://claude.ai/artifact/MvawjrRUA5QGCFK7NBFnAc. Per-plugin deep-read notes for 60+ memory, prompt, retention and compile plugins: /mnt/project-files/memory-design/plugin-deep-read-notes.md.
- Key fact: it has to be a PLUGIN. Skill-frontmatter hooks only register once the skill is invoked. Synced account plugins run hooks in terminal (v2.1.273+, /login), cloud and Cowork sessions, but not in claude.ai chats.
- Top parts: anchor-memory, continuity, whydone, llm-wiki, memory-agent, create-smartfolder, context-distill, cut-weight, drunken-master.
- The vault has both handoff/ and handoffs/.

**Why:** The account copy of memory-as-skill is a 2026-07-05 snapshot that never syncs back. The live memory is split across NvAEx-Recaps/memory/ and the vault.
**How to apply:** Design against this structure. Inventory before proposing. Show the exact SKILL.md, script and hook text before writing anything. See [[rules-hooks-inventory]] and [[feedback-plugins-are-parts]].

2026-10-29 user refinement: skills/plugins live in ONE flat folder at the workspace root (one layer deep). Session start loads ONLY MAP.md + manifest.jsonl as a shallow pointer. Hooks, launch scripts, startup hooks and output styles persist "in settings". Constraint found (cloud-environments docs): ~/.claude/settings.json never reaches cloud; repo .claude/settings.json hooks run in cloud sessions OUTSIDE projects only; project threads load only the repo's CLAUDE.md and .claude/rules plus account-synced plugins. So the settings layer needs an account plugin (hooks + output styles) and a repo CLAUDE.md pointer line. Awaiting the user's confirmation of the voice readback ("books" = hooks?, "registration straight hooks" = startup hooks?).
Clarified 2026-10-29: the user already knows hooks go in settings. The question was about SKILLS. Answer given: to register as real skills, the flat folder must be <root>/.claude/skills/<name>/SKILL.md (parent dirs are walked up to the repo root; /add-dir works outside a repo). Any other folder works only as pointer-read files. Project threads load no repo skills, so they rely on the CLAUDE.md/AGENTS.md pointer or account skills.
Docs-verified 2026-10-29 (code.claude.com/docs/en/claude-projects.md#what-threads-pick-up-from-your-repositories): project threads load ONLY the repo-root CLAUDE.md, .claude/CLAUDE.md and .claude/rules/. They do NOT load .claude/settings.json (hooks, permissions, env, plugins), .claude/skills, agents, commands or .mcp.json. Substitutes: Project settings > Plugins, account skills/connectors, the cloud environment for env, and Remote Control for hooks.
2026-10-30 builder request for Fable: /mnt/project-files/memory-design/nvaex-memory-builder-request-2026-10-30.md. It covers a SQLite per project, a separate episodic SQLite, a home ~/.nvaex/home.db, sha256 content addressing, a Next.js MCP server, the code-review-graph and graphify graph layers with an Obsidian export, vectors, per-agent and per-repo profiles, SmartFolder lazy loading (MAP.md + manifest.jsonl), and 10 build phases. The user HAS Supabase and Cloudflare, and wants to reverse-engineer mem0, OB1 (Open Brain) and OmniRoute.
