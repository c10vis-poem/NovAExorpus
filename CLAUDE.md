# CLAUDE.md: NovAExorpus (loads automatically at every session start)

STOP. Before your first reply, before any tool call, the files imported below are
already in your context. Read them. Don't ask the operator what they say.

## Startup order (every session, every repo)
1. `AGENTS.md`: the rules. RULE 1 means no action without an explicit prompt.
2. `RESUME.md`: current state and the ordered START HERE list.
3. `PENDING.md`: the durable backlog.
4. `MEMORY.md`: durable facts.
5. `handoff/<newest date>/`: open the newest folder and read what is there.
6. `agents/AGENTS.global.md`: the shared rules for every agent.
7. Private repo `c10vis-poem/NvAEx-Recaps`: read `RESUME.md`, `MEMORY.md`,
   `memory/general.md` and `memory/active/*.md`. In a cloud session it isn't
   cloned by default: attach it with the add_repo tool and clone it first.
8. Run `git log -10` here and in NvAEx-Recaps. The newest commits are the last
   thing worked on, and they may be newer than RESUME.md.

Do the same for every other attached repo: its AGENTS.md, RESUME.md, PENDING.md
and MEMORY.md, then its newest handoff docs.

## Cloud sessions
The vault clone sits at `/root/storage/shared/Documents/NovAExorpus`, and the
working directory may be an empty `/home/user`. Look there before claiming a
file doesn't exist. The phone's `~/.claude/CLAUDE.md` doesn't exist in the cloud.

## Never
- Never say "I don't have memory" or "I can't find X" before doing steps 1-8.
- Never invent a file or folder name. If the operator names something you can't
  find, say where you looked and ask.

@AGENTS.md
@RESUME.md
@PENDING.md
@MEMORY.md
@agents/AGENTS.global.md
