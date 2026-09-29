---
id: 5
title: Sync forks with upstream and read repo docs before any install/build
status: open
type: open-source
skill: [android-termux-operator]
proposes_skill: [repo-onboarding-preflight]
siblings_checked: "termux family: termux-helper, android-termux-operator — operator workflow belongs in android-termux-operator; termux-helper instance-specific"
area: required workflow (inspect read-only state first)
date: 2026-09-23
session_context: OpenWiki and dsh installs on Termux
---

**Issue:** Launched an OpenWiki install 301 commits behind upstream (v0.0.1 vs 0.5.2) and started building dsh 3,009 commits behind; trial-and-errored native build failures instead of reading the repo's docs/platform notes first. A prior session set OpenWiki up bare-bones without reading its feature docs.

**Suggested improvement:** Add a preflight step to android-termux-operator's Required workflow: (1) if the repo is a fork, compare with upstream and bring current (or build from a local upstream-latest branch when the fork branch is ruleset-protected); (2) read README/install/platform notes and packageManager/engines/build allowlists before running anything.

**Principle:** Know what version you're installing and what the project says about your platform before the first install command.
