# RESUME: "Skills and Abilities" project handoff (2026-10-30)

Prepared for The Builder, to pick up on the other Claude account from a repo folder. Planned home: `c10vis-poem/novaexorpus` → `handoff/2026-10-30/` (earlier handoff: `handoff/2026-10-28/`).

**Naming rule for any agent reading this:** call the owner **The Builder** (or the owner / the architect). Never any other name.

---

## 1. Start here on the other account

1. Clone the repo and open this folder:
   ```bash
   git clone https://github.com/c10vis-poem/novaexorpus.git
   cd novaexorpus/handoff/2026-10-30
   ```
2. Start a fresh session in the repo root and paste:
   > Read `handoff/2026-10-30/RESUME.md` end to end, then `project-memory/` and each file in section 3 before acting. Follow the owner's rules in section 2. Work read-only until I sign off on any write.
3. On claude.ai (other account), put the same line in a new project's instructions, and attach the repo under Project settings > Resources.

## 2. The Builder's standing rules (carry these over)

- No writing rules, scripts, hooks, skills or tools without explicit direction. Show the content first.
- No building unless directed. New work goes in new files; never edit or merge into existing ones ("no frankensteining").
- No subagents until The Builder approves how they're used. When approved: Sonnet or Haiku for read tasks, never Opus for reading.
- Don't subscribe to anything (PRs, APIs) without direction.
- No failure loops: stop and ask. A half-answered question isn't answered.
- Never offer only yes/no or A/B/C; always leave room for a custom answer.
- Any script or hook must be disableable mid-session; nothing may block reading files or following The Builder.
- Judge plugins as parts to mix and match, never by hook count. Deep-read before recommending.

## 3. Index: what's done, what's next, where

| Workstream | Done | Next | Files |
|---|---|---|---|
| Slash commands and tools list | Full list for account 1, plus a paste-ready prompt for account 2 | Paste the prompt into account 2, compare the two lists | `thread-handoffs/commands-tools.md`, `inventory/slash-commands-and-tools-2026-10-30.md`, `inventory/other-account-prompt-commands-tools-2026-10-30.md` |
| Disable hooks, list all active rules | Live hooks/rules snapshot; all 5 repos' rule files read; repo rules list and a paste-in rules prompt for account 2 drafted; write-blocker found: `project-boundary@synced` | The Builder signs off on the rules list and prompt, and rules on 6 conflicts (hooks, subagent order, branch delete/keep, push timing, stale OmniRoute/mem0 config, superpowers "MUST invoke"); turn off project-boundary | `thread-handoffs/rules-and-repo-rules.md` (holds the paste-in prompt), `inventory/active-rules-hooks-plugins-2026-10-30.md`, `project-memory/rules-hooks-inventory.md` |
| Trim 365 synced plugins to ~100 | Keep-119 / cut-246 list with a reason per cut; full catalog of all 365 and 1588 skills. Nothing toggled | The Builder reviews and marks changes, then toggles on claude.ai (per account) and `"<name>@synced": false` per machine | `thread-handoffs/plugins-burn-memory.md`, `inventory/plugin-recommendations-2026-10-30.md`, `inventory/all-synced-plugins-2026-10-30.md`, `inventory/all-account-skills-2026-10-30.md` |
| nvaex-burn (spend usage before reset) | Built and tested (validation passes, type-checks on Claude Code 2.1.314, 4/4 unit tests). Not installed anywhere | Install on a device and try one real session: steps in `thread-handoffs/plugins-burn-memory.md` | `builds/nvaex-burn/`, `inventory/burn-planner-proposal-2026-10-30.md`, `project-memory/burn-planner-idea.md` |
| Skill review for the memory build | 358 candidates read in full; fit 3: 4 skills, fit 2: 57 | Attach the fit-3 skills (memory-as-skill, llm-wiki, build-mcp-server, obsidian-notes) to the Fable design session | `skill-review/memory-build-skills-2026-10-30.md` |
| Memory-as-skill / SmartFolder | Schema plan and builder request; deep-read notes on 60+ memory plugins | Answer the open questions in section 10 of the request, then phase 1 | `memory-design/nvaex-memory-builder-request-2026-10-30.md`, `memory-design/plugin-deep-read-notes.md`, `project-memory/memory-as-skill-design.md` |
| Custom assets inventory | Every skill/script/hook across sessions vs repo main (2026-10-19) | Per-file disposition pass | `inventory/custom-assets-inventory.md`, `project-memory/novaexorpus-corpus-handoff.md` |
| Project memory | All 8 memory files copied as-is | Load into account 2's project memory | `project-memory/` |

## 4. Resume and teleport commands (checked 2026-10-30)

Sources: https://code.claude.com/docs/en/cli-reference and https://code.claude.com/docs/en/claude-code-on-the-web (section "From cloud to terminal", "Teleport requirements").

| Command | What it does | Works across accounts? |
|---|---|---|
| `claude --teleport` / `claude --teleport <session-id>` | Pulls a cloud session into your local terminal (checks out its pushed branch) | **No.** Docs: "You must be authenticated to the same claude.ai account used in the cloud session." |
| `/teleport` or `/tp` | Same picker from inside a running CLI session. Typed inside a cloud session, it prints that session's exact `claude --teleport <id>` command | No (same rule) |
| `claude --continue` / `-c` | Reopens the most recent local conversation in this folder | Local history only |
| `claude --resume` / `-r` `<id\|name\|path.jsonl>` | Reopens a local conversation, by picker, ID, name, or transcript file path. Docs: it "doesn't list cloud sessions" | Docs don't say it checks the account. Unverified |
| `claude --resume <id> --fork-session` | Resumes as a new session ID | Same as above |
| `claude -p "msg" --cloud <session-id>` | Sends a follow-up into a running cloud session | No (needs the owning account) |
| `claude auth logout` then `claude auth login` | Switch which account the CLI uses | n/a |
| `/export` | Saves the current conversation as text | Yes: it's a plain file |

**Possible bridge (unverified, try it once):** while still signed in to account 1, run `claude --teleport <id>` on your PC/Termux so the session becomes a local transcript. Then `claude auth logout`, `claude auth login` with account 2, and `claude --resume <id>` in the same folder. The docs say teleport makes a local copy, but they don't say whether `--resume` refuses a transcript made under another account. If it refuses, use this RESUME.md instead.

## 5. What can't move across accounts

- Cloud sessions and project threads (teleport, `--cloud` follow-ups, the thread history itself).
- claude.ai project memory, project files, and Artifacts (the artifact links in `project-memory/` open only on account 1 unless shared).
- Account skills (the 20 uploaded skills) and synced plugins: these are per account; turning plugins on/off on one does nothing for the other.
- Connectors and their sign-ins (GitHub, Gmail, Drive, etc.) must be connected again on account 2.
- Usage limits are per account.

What does move: this repo folder, `/export` text, and local transcript files on your own machine.

## 6. Still open when this was written (05:10 UTC)

- All three thread handoffs are in `thread-handoffs/`.
- Committed to branch `handoff/2026-10-30-migration` of c10vis-poem/novaexorpus with a PR for The Builder to merge.
- Note: `c10vis-poem/novaexorpus` is public. These files hold no keys or tokens, but they do name your plugins, repos and container paths.
