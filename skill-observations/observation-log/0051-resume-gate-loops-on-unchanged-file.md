---
id: 51
title: "resume-gate repeatedly reported the vault RESUME.md as changed while its mtime stayed the same, blocking every tool in a loop"
status: open
type: internal
skill: []
proposes_skill: []
target_file: ["Aesop-Xi/hooks/resume-gate.sh"]
siblings_checked: "checked, instance-specific to resume-gate's fingerprint state; other gates were already stubs"
area: "hooks / resume-gate"
date: 2026-10-28
session_context: "Phone session 5fc2c8e1, with several subagents running in other repos"
parked_until:
resolved:
resolution:
reference:
commands_verified: "run: stat -c %y vault RESUME.md -> 2026-10-28 04:05 throughout; gate kept blocking after each full re-read"
---

**Issue:** After subagents in the same session read RESUME.md files in other repos (and after cwd moved between repos and worktrees), resume-gate blocked almost every tool call with "changed since this session read it". The vault file had not changed. Each full re-read let about one call through. It blocked SendMessage, Agent, Bash and even Read of the hook's own source. The operator then ordered every hook off (all stubbed, originals `*.disabled-20261028`).

**Suggested improvement:** Key the gate's snapshot per agent and per RESUME path, not one shared slot per session; compare content hashes, not "last file read"; never block Read.

**Principle:** A gate that cannot tell its own bookkeeping change from a real change becomes a denial of service. Test a gate with parallel subagents and multiple repos before turning it on.
