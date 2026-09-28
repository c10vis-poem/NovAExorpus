---
name: parallel-session-orchestration
description: Decision guide for which parallel-execution mechanism to use — in-process background subagents (Agent tool), a genuinely separate on-device session with its own conversation (mem0:sidekick), or an isolated git worktree/remote environment. Use whenever a task needs more than one line of execution at once, or when one line of work would otherwise block another. Trigger on "run this in parallel", "spin up another session", "work on this while I do that", "don't block on this".
---

# Parallel Session Orchestration

## The three real mechanisms (not the same thing)

| Mechanism | What it actually is | Own conversation? | Own working copy? | When to use |
|---|---|---|---|---|
| **Agent tool, background dispatch** | A subagent that runs in this session's process, reports back via a notification, and whose transcript you don't read directly | No — reports back to the dispatching session | Shares the working directory unless given `isolation` | Bounded, well-scoped batches of work (e.g. converting 25 files) that don't need back-and-forth — fire, wait, collect the report |
| **`mem0:sidekick` agent** | A Sonnet coding agent that works in a **separate Git worktree** and keeps **its own conversation** | **Yes** — you can send it follow-up messages and it remembers its own context, independent of this session | Yes — its own worktree, isolated from the main working tree | Work that needs iteration/correction over time (not fire-and-forget), or that you want to keep talking to independently of the main session |
| **`isolation: "worktree"` / `"remote"` on any Agent dispatch** | Runs any agent type in an isolated git worktree (local) or a remote cloud environment (fully separate infrastructure) | Depends on agent type | Yes, always | When a subagent's file writes must not collide with the main session's working tree at all, or when the task should run somewhere else entirely (remote) |

**The distinction that matters:** a background Agent dispatch is *this session, delegated* — it disappears once it reports back, and you can't have a running dialogue with it. `mem0:sidekick` is *a second, standing session* — it persists, has its own memory of the conversation you're having with it, and you resume it the same way you'd resume any other agent (by name, via SendMessage).

## Decision rule

1. **Is the task a bounded batch with clear rules and no need for follow-up?** → Background Agent dispatch (what `corpus-batch-processing` uses).
2. **Does the task need iteration — you'll want to correct it, ask it to redo part of the work, or keep it running across multiple turns of this conversation?** → `mem0:sidekick`.
3. **Does a subagent's work need to be fully isolated from the main working tree** (e.g. testing a risky change, or running something that could touch the same files another agent is using)? → add `isolation: "worktree"` to the dispatch.
4. **Does the task need to run somewhere other than this device entirely?** → `isolation: "remote"`.

## Using `mem0:sidekick` concretely

- Dispatch it with the Agent tool, `subagent_type` targeting the sidekick, and a full, self-contained brief — it starts cold, same as any fresh agent.
- To continue talking to it later (review its work, send corrections), use `SendMessage` addressed to it by name — this resumes it with its own accumulated context, not a fresh start.
- It keeps its own conversation and its own worktree — changes it makes don't land in the main working tree until merged/reviewed, same as any worktree-isolated agent.

## What NOT to do

- Don't dispatch a background Agent for work you expect to correct iteratively — you can't have a conversation with one after it reports back; you'd have to write a whole new dispatch with the correction baked in. Use `mem0:sidekick` instead for anything you expect to go back and forth on.
- Don't use `isolation: "remote"` by default — it's a genuinely separate cloud environment; only reach for it when the task specifically needs to run off-device.
- Don't run more parallel dispatches than the session's actual rate limit supports — a burst of agents sharing one account's API budget can all fail together (this happened this session: 4 batch dispatches, 2 hit a shared rate limit mid-run).
