# Handoff: plugin trim, nvaex-burn, skill review, memory builder (2026-10-30, about 01:30 UTC)

The owner is **The Builder** (or "the owner" / "the architect"). Never "Drew", and not "the user".

Everything below lives in `/mnt/project-files/` (this project's shared folder) unless the path says otherwise. To pick this up from another account, copy this folder's files into a repo folder. Every path here is relative to the project-files root.

## State, in one screen

| Workstream | State | Files |
|---|---|---|
| Live rules, hooks and plugins inventory | Done, read-only | `inventory/active-rules-hooks-plugins-2026-10-30.md` |
| All 365 synced plugins, listed | Done | `inventory/all-synced-plugins-2026-10-30.md` |
| Every skill on the account (1,588), with one-line descriptions | Done | `inventory/all-account-skills-2026-10-30.md` |
| Plugin trim recommendation | Done: **keep 119, cut 246**, a reason for every cut, plus overlaps and combine ideas. **Nothing toggled yet** | `inventory/plugin-recommendations-2026-10-30.md` |
| nvaex-burn (custom mod) | **Built and tested.** Validation passes, it type-checks against Claude Code 2.1.314, and 4 of 4 unit tests pass. **Not installed anywhere yet** | `builds/nvaex-burn/`, plus the design notes in `inventory/burn-planner-proposal-2026-10-30.md` |
| Skill review for the memory build | **Done.** 358 candidates, all read in full by 4 Sonnet subagents. Fit 3: 4, fit 2: 57 | `skill-review/memory-build-skills-2026-10-30.md` |
| Memory and SmartFolder builder request (for Fable) | Done, waiting on answers to the open questions in its section 10 | `memory-design/nvaex-memory-builder-request-2026-10-30.md` |
| Earlier design brief and plugin deep-read notes | Reference | Brief: https://claude.ai/artifact/MvawjrRUA5QGCFK7NBFnAc · Notes: `memory-design/plugin-deep-read-notes.md` |

## Key facts learned

- **This cloud container's live hooks:**
  - 5 platform hooks in `~/.claude/settings.json`. The platform generates that file, and it denies edits to it.
  - 9 enabled plugins with hooks.
  - **The only hook that can block a file read** is claude-context-optimizer's `read-cache.js`. It's on the to-turn-off list.
  - superpowers injects "MUST invoke skills" at session start.
- **Plugins:** 35 are enabled in settings. 9 of them have no files (agent-engineering, agent-protocols, agentkeeper, akc-cycle, context-bar, gas-gauge, hookify, maddog, supabase).
- **Owner corrections:**
  - The Builder **does** use Supabase and Cloudflare, so both are on the keep list.
  - The reverse-engineering targets are mem0, OB1 (Open Brain) and OmniRoute.
  - The Builder prefers **lean custom plugins built from stripped parts** over stacking several plugins.
- **Subagents** are OK for read tasks, but only on **Sonnet or Haiku**, never Opus. Their output is a **new standalone file**, never merged into existing files.

## nvaex-burn: how to install (once The Builder says go)

On a terminal or Termux session, Claude Code 2.1.287 or newer, signed in:

1. Copy `builds/nvaex-burn/` to a device folder, for example `~/nvaex/mods/nvaex-burn/`.
2. Try it for one session: `claude --plugin-dir ~/nvaex/mods/nvaex-burn`. Or, to keep it, add it to the NovAExopia marketplace and run `/plugin install nvaex-burn --marketplace <owner>/NovAExopia`.
3. Copy `burn-queue.example.json` to `~/.nvaex/burn-queue.json` and edit the jobs.
4. Optional: set `webhookUrl` in `/config` to an ntfy.sh topic URL, so phone routines can react. By default it notifies through your own Claude notification channel.
5. The kill switch: `/burn off`, or create the file `~/.nvaex/off`.

**Not yet verified on a real device:** whether the app notification and the wind-down append behave as the API docs describe. Run it in one real session to confirm.

## Next steps (in order)

1. **The Builder:** review `inventory/plugin-recommendations-2026-10-30.md` and mark any changes. Then toggle plugins in the claude.ai account plugin settings. For each machine, `"<name>@synced": false` in that machine's `~/.claude/settings.json` turns a plugin off locally.
2. **The Builder:** answer section 10 of the builder request. Then upload these to a Fable session:
   - the builder request;
   - `skill-review/memory-build-skills-2026-10-30.md`;
   - `memory-design/plugin-deep-read-notes.md`.
3. **The fit-3 skills to attach to design sessions:** memory-as-skill (account), llm-wiki, mcp-server-dev `build-mcp-server`, and obsidian-notes. The 57 fit-2 skills come next, by phase.
4. Install and try nvaex-burn on a device, as above.
5. **Still open from the earlier brief:**
   - `handoff/` versus `handoffs/` in the vault;
   - the settings .jsonl definition;
   - whether Gemini parity comes now or later.

## Commands to resume

- Read this file, then `inventory/plugin-recommendations-2026-10-30.md` and `memory-design/nvaex-memory-builder-request-2026-10-30.md`.
- Project memory notes that carry the same facts: `rules-hooks-inventory`, `burn-planner-idea`, `memory-as-skill-design`, `feedback-plugins-are-parts` and `user-naming`.
