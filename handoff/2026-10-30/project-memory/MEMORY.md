- This project was upgraded from a classic claude.ai project on 2026-10-17. The project's files are under /mnt/project-files/, and /mnt/project-files/UPGRADE-NOTES.md lists what did and did not come over. The app lists the original project's chats and Cowork tasks among this project's threads. To continue one, start a thread that reads it; the original-project tools list them and read the ones they can.

## How to refer to the user (2026-10-30)
- Never call them "Drew". In prompts and docs, refer to them as "The Builder" (also: the owner, or the architect).

## User's standing rules (2026-10-29, verbatim intent)
- No writing rules, scripts, hooks, skills, or tools without explicit user direction. Show content before asking to write.
- No building actions unless explicitly directed.
- No subagents until the user has gone over how they'll be deployed.
- Subagents (2026-10-30): use Sonnet or Haiku where capable; never Opus for read tasks.
- New work produces its own new files; don't modify/merge into existing files ("no frankensteining").
- No burning tokens in failure loops while waiting on the user; stop and ask.
- Don't subscribe to anything (PRs/APIs) without explicit direction.
- A half-answered question is not answered; follow up.
- Never offer only yes/no or A/B/C options; always allow a custom answer.
- Any script/hook must be disableable mid-session; nothing may block reading files or following the user's direction.
- User wants all existing hooks disabled and every rule in accessible files listed for review.
- Context: user's NovÆxorpus repos (Aesop-Xi, NovAExopia, NovusAExenti, NvAEx-Recaps, NovAExorpus); handoff in NovAExorpus handoff/2026-10-28/. Wants future work to use their wiki-admin, web tools, Gemini CLI, reverse-engineering repos, memory-as-skill.
