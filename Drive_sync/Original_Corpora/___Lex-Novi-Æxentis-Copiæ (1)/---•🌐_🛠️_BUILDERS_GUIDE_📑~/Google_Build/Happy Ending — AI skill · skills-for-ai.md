---
title: "Happy Ending — AI skill · skills-for-ai"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/---•🌐_🛠️_BUILDERS_GUIDE_📑~/Google_Build/Happy Ending — AI skill · skills-for-ai.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Home › Happy Ending
Development
Every session deserves a Happy Ending — the clean close for your AI session, without losing the
thread.
Session close
Context handoff
Handoff
Wrap-up
Memory Patch
Project memory
Decision log
Next-session start
Memory safety
Reversal detection
Commit suggestion
Free
Get it free
107
↓ 9
★ 5.0
v1.0.0
Updated 07.07.2026
by @Hiro
SKILL.md in the open agentskills.io standard — works directly in Claude, ChatGPT/Codex, Cursor, Copilot &
more.
Happy Ending is an AI skill for closing AI work sessions cleanly, turning the chat into the valid project
state: final decisions, open tasks, a memory patch and a copy-paste next-session prompt. Its core is
a Memory Safety layer, so discarded, canceled or superseded work is not mistakenly saved as the
valid state.
WHAT THIS SKILL DOES
Extracts final decisions, open tasks, learnings and discarded points from the session
Protects your memory: canceled, reverted or superseded work is not saved as the valid state (Memory
Safety)
Emits a memory patch (Add/Update/Ignore) instead of blind-rewriting whole memory files
Separates "don't adopt" (Do Not Carry Forward) from "don't try again" (Do Not Repeat)
Delivers a directly pasteable next-session prompt plus a compact Delta block
Suggests commit messages and commit groups for code — but executes nothing unasked
Two depths: Quick (compact default) and Deep (on request)
Productivity
Skill
Happy Ending
(1)


DESCRIPTION
Happy Ending is a skill for closing AI sessions — it turns a messy chat into a clean, reusable project state
instead of a novel. Guiding line: Happy Ending doesn't save everything that happened, it secures what holds
from now on. It runs in three phases (Look Back → Clean Up → Kiss Goodnight) and picks up final
decisions, open tasks, learnings, user corrections, references and discarded points. Out of that comes a
compact report: Result, Decisions, Open, Do Not Carry Forward, Do Not Repeat, a Memory Patch
(Add/Update/Ignore), file/git notes when relevant, the single next best step, a directly pasteable next-
session prompt, a Delta block (+ ~ − !) and a short closing line with counters. The core feature is the
**Memory Safety layer**: every point gets a status (final, open, tentative, reverted, canceled, superseded,
rejected, do-not-repeat, do-not-carry-forward, unclear) and a confidence — only final + high (or your
explicit confirmation) may enter long-term memory. A reversal detector watches for undo signals ("actually
no", "canceled", "take that out"), when the session contradicts itself the last confirmed state wins (final-
state-wins), and instead of blind-rewriting whole memory files the skill emits a patch. Git and files are only
ever suggested — Happy Ending never commits, pushes, deploys or overwrites without your explicit
instruction. Two depths: Quick as the compact default, Deep on request.
EXAMPLES
Close the session quickly
Wrap up the session.
You
August 31, 2026
Happy Ending
# Happy Ending
## Result
Landing-page hero copy and the primary CTA are settled. One asset is still open.
## Decisions
[final · high] Hero headline: "Ship faster, guess less."
[final · high] Primary CTA: "Start free" (secondary "See how it works").
## Open
[open] Export the hero background as WebP (1600px).
## Do Not Carry Forward
The purple-gradient hero — dropped mid-session, don't reintroduce.
## Memory Patch
+ Add
Preference: CTA voice is plain-imperative ("Start free"), not "Get started now".


WHAT IT DOES NOT DO
Not a chat summary and not a chronological retelling — it secures the valid state
Not an auto memory-dump — only final + high (or your confirmation) is saved for good
Never commits, pushes, deploys or overwrites without an explicit instruction — it suggests
Not a full project-management system and no substitute for tests, review or release
Doesn't impose a memory layout — it patches your real memory (CLAUDE.md, a memory folder, Cursor
rules …)
COMPATIBILITY & TECH
Claude
ChatGPT/Codex
Cursor
Copilot
Gemini CLI
Windsurf
Cline
Tested (internal)
4 scenarios
Recommended runtime
Claude Opus or Sonnet; with git/file access for commit/file suggestions,
otherwise pure copy-paste suggestions
Modes
Quick (default) · Deep · Handoff · Git suggestion (optional) · Skill notes (optional)
Inputs
The session's chat history · Git status (optional) · Existing project memory
(optional)
Output format
Compact Markdown report: Result · Decisions · Open · Do-not lists · Memory
Patch · Next-session prompt · Delta · Closing line
Subcategory
Session close & handoff
License
Proprietär
SECURITY PROFILE
Local
Runs entirely on your machine with
your own AI — no external runtime,
no running costs.
Instruction-only
Only instructions, templates and
references — no executable scripts.
No network access
Works offline with what you provide
— does not call external services on
its own.
What do these badges mean? →
1 / 2
›
– Ignore
The purple-gradient hero direction (discarded).
…
‹


WHAT YOU GET
happy-ending-1.0.0/
5 files
.claude-plugin/marketplace.json
plugins/happy-ending/skills/happy-ending/
5 files
SKILL.md
manifest.json
references/
3 files
.agents/skills/happy-
ending/
→ universal — same content (Codex, Cursor, Copilot, Gemini,
Windsurf, Cline)
LICENSE.txt
INSTALLATION
After unlocking, you install with a single command — it auto-detects your AI tool.
Runs in
Claude Code
GitHub Copilot
Gemini CLI
Cursor
Codex CLI
Windsurf
Cline
ALSO WORKS AS A CHAT PROMPT
Full in chat
No AI tool? Paste it into Claude, ChatGPT or Gemini and use the method right away.
This skill ships no scripts, so the prompt carries its full method.
Installing is the full version — it triggers automatically, runs its scripts and loads references as needed. As a chat prompt
you drive the method by hand.
Unlock to copy the ready-to-paste prompt — then in “My Skills”.
REVIEWS
5.0 1 review
NOTE
Start it manually by default ("make a Happy Ending" or "/happy-ending"). The skill only suggests memory,
git and file changes — it saves, commits or overwrites nothing without your explicit approval. When the final
state is unclear, it asks one short question instead of guessing.
★★★★★
★★★★★


CHANGELOG
v1.0.0 07.07.2026
Initial release: three-phase session close (Look Back → Clean Up → Kiss Goodnight) with a Memory Safety layer (status +
confidence, reversal detector, final-state-wins, patch-not-rewrite), separate Do Not Carry Forward / Do Not Repeat, a
memory patch, a copy-paste next-session prompt, a compact Delta block and a closing line. Two depths (Quick/Deep) +
optional Git/skill blocks; git and files are only ever suggested. References for templates, memory-safety and examples.
FREQUENTLY ASKED QUESTIONS
What does Happy Ending do?
Happy Ending is an AI skill for closing AI work sessions cleanly, turning the chat into the valid
project state: final decisions, open tasks, a memory patch and a copy-paste next-session
prompt. Its core is a Memory Safety layer, so discarded, canceled or superseded work is not
mistakenly saved as the valid state.
How do I close an AI session cleanly?
Is Happy Ending just a summary?
How does Happy Ending keep wrong entries out of memory?
Can Happy Ending commit or push?
What's the difference between Do Not Carry Forward and Do Not Repeat?
Which AI tools does Happy Ending work with?
How do I use Happy Ending?
Works well with
Deep Research
Deep research that doesn't stop at the third hit: search broad, hunt primary sources, cross-check, show contradictions,
cite cleanly. Neutral — it reports sources and how strong they are, never a true/false verdict.
AI Blueprint Assistant
Turn a rough idea into an AI-ready project plan and AGENTS.md handoff — for software AND everything else.


Decision Board
Stress-test your decision before you commit — a structured panel of experts, stakeholders and critical counter-voices
that argue it out, so you get a real second opinion instead of one answer.
Code Reviewer Pro
Senior code review line by line: bugs, security, missing tests — with concrete fixes and a clear verdict.
skills-for-ai
The marketplace for ready-made AI skills & agents.
Pick, install, deploy.
skills-for-ai.de · skills-for-ai.com
A project by M.E.A.T.
Join the Dev Discord
DISCOVER
Skills & Agents
How it works
Install guide
Creators
Trust & Safety
LEGAL
Imprint
Privacy
Terms
Creator Terms
Contact
Cookie settings
LANGUAGE
English
Deutsch
Français
Español
© 2026 skills-for-ai. All rights reserved.
Crafted with care.
