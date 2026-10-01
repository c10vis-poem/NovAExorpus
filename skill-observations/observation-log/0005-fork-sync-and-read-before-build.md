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
session_context: "OpenWiki and dsh installs on Termux; 2026-09-30 Hermes reinstall on Termux"
---

**Issue:** Launched an OpenWiki install 301 commits behind upstream (v0.0.1 vs 0.5.2) and started building dsh 3,009 commits behind; trial-and-errored native build failures instead of reading the repo's docs/platform notes first. A prior session set OpenWiki up bare-bones without reading its feature docs.

**Suggested improvement:** Add a preflight step to android-termux-operator's Required workflow: (1) if the repo is a fork, compare with upstream and bring current (or build from a local upstream-latest branch when the fork branch is ruleset-protected); (2) read README/install/platform notes and packageManager/engines/build allowlists before running anything.

**Principle:** Know what version you're installing and what the project says about your platform before the first install command.

**Recurrence (2026-09-30, Hermes on Termux):** Proposed and launched a pip/venv source build from the fork before reading the repo's platform doc (`website/docs/getting-started/termux.md`), which says source/desktop installers are not the Termux path. The user had to correct it ("you already documented that… saying that for a few days now"). Second violation of this rule with no intervening fix, so the fix must be structural, not rewording: e.g. a PreToolUse hook that blocks `pip install`/`npm install`/`make`/`cargo build` inside a git checkout until a marker shows the platform/install doc was read and the fork was compared with upstream this session.
