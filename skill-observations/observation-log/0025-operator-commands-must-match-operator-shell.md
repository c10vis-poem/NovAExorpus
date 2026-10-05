---
id: 25
title: "Gave the operator a bash-only command in a zsh terminal; it silently stored empty secrets"
status: open
type: open-source
skill: [android-termux-operator]
proposes_skill: []
target_file: []
siblings_checked: "none — android-termux-operator is not in a family"
area: "commands handed to the operator to run"
date: 2026-10-05
session_context: "Setting a GitHub Actions secret in 7 repos from the operator's terminal"
parked_until:
resolved:
resolution:
reference:
---

**Issue:** I gave `read -rs -p "token: " T` for the operator to paste. Their shell is zsh, where `-p` means coprocess. The read failed with "no coprocess", T stayed empty, and the loop still ran `gh secret set` 7 times, storing empty secrets and printing "set" each time. A first attempt failed differently: a pasted trailing newline was consumed as the value. It took 3 rounds.

**Suggested improvement:** In android-termux-operator, add a rule: commands for the operator must be written for the operator's actual shell (check `$SHELL`; the session env states it), and any command that consumes a secret must guard against an empty value (`[ -n "$T" ] || exit`) before it acts. Prefer the tool's own prompt (`gh secret set NAME -R repo` prompts interactively) over hand-rolled `read`.

**Principle:** A command that writes a secret must fail closed on an empty value. Shell builtins differ across shells, so write for the shell the person is actually running and let the tool do its own prompting.
