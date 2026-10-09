---
title: "c10vis-poem_aesop"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/--🗂️~SKILLS.md_🛠️_/Repo-Bank_/##AESOP/c10vis-poem_aesop.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Watch
0
0 stars
0 forks
0 watching
3 branches
0 tags
Activity
Public repository
3 Branches
0 Tags
Go to file
Go to file
Add file
Code
nav-c1ovis and claude docs: lock STT model choice (Moonshine-base-int8) + shared-model/per-…
d1e4fa6 · 2 weeks ago
profiles
docs: scaffold AESOP protocol spine (archit…
2 weeks ago
protocol
docs: scaffold AESOP protocol spine (archit…
2 weeks ago
ARCHITECTURE.md
docs: scaffold AESOP protocol spine (archit…
2 weeks ago
README.md
docs: scaffold AESOP protocol spine (archit…
2 weeks ago
RESUME.md
docs: lock STT model choice (Moonshine-b…
2 weeks ago
A device-agnostic protocol for running a split agent stack across the machines you already own — mobile, workstation, home node, and
cloud — behind one shared, auditable memory.
Aesop distilled a moral from every fable. AESOP distills a strategy from every trajectory.
AESOP defines a small set of agent roles, three memory types, and a set of capability tiers that any hardware maps onto. Roles bind to tiers
with graceful fallback, so the same stack runs whether you have a phone + laptop + cloud, or a full home-node rig. The specific hardware
layout is a profile; the protocol itself is device-agnostic.
Role
Job
Default tier
Query / tool-exec
intake, meta-prompting, tool calls, reads memory
Edge (mobile)
Executive
heavy reasoning, direct file/memory access
Home node → Cloud
Librarian / switchboard
intercept prompts+outputs, select memory, log, commit learnings back (the flywheel)
Home node
Auditor (red)
independent gate on side-effecting actions; judges trajectories
Cloud (out-of-band)
Memory
Holds
Backed by
Declarative
facts, "what things are" (source of truth)
wiki markdown — OpenWiki / Obsidian
c10vis-poem
aesop
Code
Issues
Pull requests
2
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
Fork
0
m
T
AESOP — Agentic Executions Split Operations Protocol
What it is
Agent roles
Memory — three types, markdown as interchange
README


Memory
Holds
Backed by
Recall
semantic search across everything
OB1 / Open Brain (vector)
Strategic
distilled reasoning from successes and failures
ReasoningBank (fed by the auditor)
Markdown is canonical and human-auditable; the vector indexes are derived and rebuildable from it.
Private draft. protocol/ is device-agnostic and intended for public release; profiles/ holds personal hardware mappings and stays
i
t
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
2
claude Claude
nav-c1ovis
Repo layout
aesop/
  ARCHITECTURE.md      # the full spec
  protocol/            # tier definitions + role→tier bindings + fallback  ← device-agnostic, public
  profiles/            # hardware→tier mappings  ← personal
    _example.yaml      #   the common case: phone + laptop + cloud
    nav.yaml           #   a full 4-tier reference rig
  clients/omni-claw/   # on-device UI / client layer
  agents/              # query · executive · librarian · auditor contracts
  memory/              # wiki + OB1 + reasoning-bank adapters
  deploy/              # per-tier bootstrap
Status
