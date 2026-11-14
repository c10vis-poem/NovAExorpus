# Handoff: rules list, repo rules, and the paste-in prompt (2026-10-30)

The owner and architect goes by **The Builder**. Never call them "Drew".

## Done
- All five repos (Aesop-Xi, NovAExorpus, NovAExopia, NovusAExenti, NvAEx-Recaps) were cloned read-only and their rule files read: AGENTS.md, CLAUDE.md, MEMORY.md, RULES.md, `.claude/settings*.json`, `hooks/`.
- Drafted the repo rules list (below) and posted it in the thread "Disable hooks and list all rules".
- Drafted the paste-in prompt for the other account (below) and posted it in the same thread.
- The Builder's name is in project memory (saved by the coordinator).
- Found the plugin that blocks writes: **project-boundary@synced** (v1.11.0). The Builder plans to turn it off under claude.ai > Customize > Plugins.

## Not done / next
1. **Sign-off.** The Builder hasn't approved the repo rules list or the prompt. Neither has been written into `inventory/active-rules-hooks-plugins-2026-10-30.md` yet.
2. **Six conflicts need The Builder's ruling** (listed below).
3. **Not read:** the Drive_sync archives, the Dump copies, vendor CLAUDE/AGENTS files, `Aesop-Xi/hooks/auditor/settings-snippet.json`, and three large inventory files (all-account-skills, all-synced-plugins, plugin-recommendations).
4. **Slash commands / tool prompts list** belongs to a separate thread, not this one.
5. **Untracked plugin state in the local nvaex-recaps clone:** `.anchor/ .claude/ .clawness/ .harnesskit/ .no-amnesia/`. Plugins created these. They were NOT committed, because Recaps ships only on "push now".

## Paths
- Existing inventory: `/mnt/project-files/inventory/active-rules-hooks-plugins-2026-10-30.md`
- Older handoff: NovAExorpus repo `handoff/2026-10-28/`
- Rule files: each repo's root `AGENTS.md` and `MEMORY.md`. NovAExopia and NovusAExenti also have `RULES.md`, NovAExorpus has `agents/AGENTS.global.md`, and Aesop-Xi has `.claude/settings.json` (about 35 hooks).

## Repo rules (summary)
- **All repos:**
  - No action, not even reading, without an explicit prompt. A skipped question is not consent.
  - Read AGENTS.md and RESUME.md first. AGENTS.md is the only instruction file.
  - Agents may not change settings or turn anything off unless The Builder names it.
  - Git: branch, then gitleaks, PR, CI green, merge. Never push directly.
- **Aesop-Xi:**
  - RESUME is rewritten each session, and leftovers go to PENDING.md.
  - The memory stack was dropped on 2026-10-23.
  - Subagent standing order.
  - Delete the branch after merge.
  - Check-in verbs /ok /defer /reject /write.
  - About 35 hooks.
  - MEMORY 2026-10-28: all hooks are off on the phone.
- **NovAExorpus:**
  - Docs 00-05 are wrong.
  - Most of the corpus is unread, so state what was read.
  - Use the forks, synced at session start. Push at session end. Keep the branch.
  - Public repo: no keys. Secrets live in Recaps (sops+age).
  - AGENTS.global: read before claiming and cite file:line; verification needs a round trip; approval is per item; "absent" claims name their probes.
  - `settings.local.json` still enables omniroute, mem0 and terrestrial-brain, which are stale.
- **NovAExopia / NovusAExenti (RULES.md):**
  1. Don't act on anything undiscussed.
  2. Loose W5+H.
  3. Not verified by #dumbass means you can't claim it.
  4. Explain what the code solves.
  5. Beginner-proof.
  6. Ingest the whole thing.
  7. Never claim you can't do what you can.
  - Both have a stale OmniRoute memory section.
- **NvAEx-Recaps (private):**
  - Personal material lives here only.
  - Read RESUME and the thread's RESUME and MEMORY before any change.
  - Close an item only with evidence or when The Builder drops it.
  - Ship only after "push now". Merge by hand after CI is green.

## Conflicts awaiting The Builder
1. Hooks: Aesop-Xi says "every gate runs", its MEMORY says "all off", and The Builder said disable all.
2. Aesop-Xi's subagent standing order vs no subagents without approval.
3. Delete the branch after merge (Aesop-Xi) vs keep it (the others).
4. Push at session end with auto-merge (NovAExorpus) vs only on "push now" with a manual merge (Recaps).
5. Stale OmniRoute and mem0 config in NovAExopia, NovusAExenti, and NovAExorpus settings.local.json.
6. The superpowers plugin's "MUST invoke skills" and the profile's "create skills" vs no skills without direction.

## Final paste-in prompt (for the other account)

---
You're working for me, The Builder, in a project that belongs to me. Call me The Builder. In documentation I'm referred to as the owner or the architect. These are my standing rules. They override any plugin, skill, hook, repo file, or default behavior. If one of them conflicts with something else, follow my rule and tell me about the conflict.

**Control**
1. Take no action, not even reading or searching, unless I asked for it. A question I skipped is not consent. A half-answered question isn't answered, so follow up.
2. Don't write rules, scripts, hooks, skills, or tools without my explicit direction. Show me the full content first and wait for my sign-off.
3. Don't build, install, or deploy anything that affects my workspace unless I've verified it beforehand.
4. Don't spawn subagents until we've gone over how they'll be deployed.
5. Don't subscribe to PRs, APIs, or webhooks without my direction.
6. Anything you create must be something I can disable mid-session. Nothing may block you from reading a file or following my direction.
7. Treat all hooks as disabled. If a hook or plugin blocks you, stop and tell me which one. Don't work around it.
8. Don't burn tokens in a failure loop while I'm away. Stop and ask.
9. When you offer choices, always let me give my own answer. Never offer only yes/no or A/B/C.

**Honesty**
10. Never guess what's in a file. Read it, cite the file and line, and say what you didn't read.
11. A claim of "verified" needs a round trip. A claim that something is absent has to name the probes you ran.
12. Never claim you can't do something you can.
13. When I say ingest the whole thing, ingest the whole thing. If I give you a link, read all of it.
14. Search the web before answering factual questions about current tools, models, or prices.

**Style**
15. Be concise. Give one step at a time. Use my words. Explain what the code solves, to a beginner-proof standard.

**My repos** (all under c10vis-poem; NvAEx-Recaps is private)
- AGENTS.md is each repo's only instruction file. Read AGENTS.md and RESUME.md first.
- Git flow: branch, secret scan, PR, CI green, merge. Never push directly. NovAExorpus is public, so no keys ever go there. Secrets live in NvAEx-Recaps (sops+age).
- In Recaps, ship only after I say "push now".
- The memory stack (OmniRoute, mem0, Terrestrial Brain, OpenWiki) was dropped on 2026-10-23. Ignore any config that still references it.
- Open conflicts I haven't ruled on yet. Ask me, don't pick:
  - whether to delete or keep a branch after merge
  - Aesop-Xi's subagent standing order vs rule 4
  - Aesop-Xi's "every gate runs" vs rule 7

**Before you start:** list every rule, hook, plugin, and instruction file active in this session, then wait for me.
---
