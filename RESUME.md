Session files: [[AGENTS]] · [[PENDING]] · [[MEMORY]] · [[MAP]] · [[NAMING-CANON]]

# RESUME.md — Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC). Private files removed 2026-10-05; history not yet erased (item 0b).
**Last session: 2026-10-04/05** (phone, Claude Code, Opus 5.5, session `edd68643`, started in `~`).
It covered the vault privacy cleanup, the master-files workflow, AGENTS.md only, Hyperion-XI, the wiki corpus search and the wiki-admin agent draft.
Reports you can open: `Documents/Session-reports/2026-10-05/` (01 = wiki search results).

## NEXT SESSION — START HERE
The Stop gate requires a status for each numbered item: `resume-item <n> done|blocked "<evidence / what's needed>"`.

0. **Fix the master-files token, then prove it works.** The pings and builds work, but `VAULT_DISPATCH_TOKEN` can't open PRs ("Resource not accessible by personal access token"). The operator makes a token that has **Contents + Pull requests: read and write** on NovAExorpus (or a classic token with `repo`) and re-sets it in all 7 repos (zsh: `read -rs "T?token: "`, then the `gh secret set` loop, then `unset T`). Then run the Master files workflow once and check that `MASTER-AGENTS.md` / `MASTER-RESUME.md` have real content.
0b. **Repo history (operator runs; Claude Code's safety check blocked it as irreversible):** old commits still hold the removed private files. To erase them: `gh repo rename NovAExorpus-old -R c10vis-poem/NovAExorpus`, create a fresh public `NovAExorpus`, push today's `main` as a single commit, re-set the secret, re-point GitSync, then `gh repo delete c10vis-poem/NovAExorpus-old`. Ask Claude to prepare the exact commands.
1. **Grill session** (`wiki-admin`, Pocock chain typed by the operator: `/setup-matt-pocock-skills` → `/grill-with-docs` → `/to-spec` → `/to-tickets` → `/implement`). Inputs: the PRIORITY ONE docs (`_#Repository-layout.txt` + `Master_dumbass_plan-session/`), `Documents/Session-reports/2026-10-05/`, the wiki-admin agent draft (`~/wiki-admin/AGENTS.md`), PENDING "Added 2026-10-05".
2. **Vault cleanups awaiting the operator's yes** (PENDING "Added 2026-10-05"): the conflict copies, `WebView/`, the empty files, `_quarantine/` + `qairt_/` out, the Documents write-guard hook.
3. **NPU work, one model at a time WITH the operator** (`docs/NPU-FINDINGS-2026-10-02.md` §4): reboot, check the clock caps, InternVL 2B first. Carried over, not started.
4. **Housekeeping** (overdue): recaps rollup, 7-repo branch audit, observation review (0022–0025 new), cloud billing / VM retirement, ~22 GB disk.

## STATE (verified 2026-10-05)
- **Privacy:** personal memory files, every copy of the unfiled-designs "Device Stack" doc, a subscriptions list and a billing CSV were removed from GitHub (PR #34). Old commits still hold them (item 0b). One saved Google page with embedded keys is gitignored (device only). Originals: `Documents/private-memory/` (outside the vault).
- **Master files:** `.github/workflows/master-files.yml` + `tools/build_masters.sh` build MASTER-AGENTS/RESUME from every base repo's main. They're triggered by each base repo's `notify-vault.yml`; no timer. `MASTER-CLAUDE.md` is retired; the phone post-commit hook is removed.
- **AGENTS.md only** in all 6 base repos + `~/wiki-admin` (Claude Code reads it natively). The Stop gate checks it at wrap-up, along with MEMORY.md per touched repo and the PENDING update.
- **Hyperion-OXiLm → Hyperion-XI** (repo + clone).
- **Wiki toolkit (chosen 2026-10-02):** OpenWiki for Claude Code, obsidian-wiki, wiki-compiler (+ nocode, anydoc, NotebookLM, graphify, Obsidian skills). The wiki lives in this vault. The wiki-admin agent is a DRAFT.
- **Launchers:** `wiki-admin`, `nvaex`, `nvaex-all` (all 7 repos read/write).
- **Device:** `Documents/Zip/` = exact vault backup (15 GB); nested mirror moved to `Documents/NovAExorpus-nested-mirror/`.
- **Public toolkit repo** `c10vis-poem/NvAEx-agentk` (MIT, plugin `nvaex`, skill `subagent-protocol`).

## DECISIONS 2026-10-05
- PRIORITY ONE: `_#Repository-layout.txt` + `Master_dumbass_plan-session/`. The restructure is grill work; `__RESUME.md/` dissolves into the 00–10 layout. The device vault ends up an exact mirror of this repo.
- Documents outside the vault stays outside; never pull it into the vault.
- No CLAUDE.md in repos; the only one is the user-level `~/.claude/CLAUDE.md`.
- RESUME.md is the handoff: no separate handoff docs.
- The master files rebuild only on change, never on a timer.
- `file_administrator.yaml` / `oracle_helpdesk.yaml` are wrong; real roles come from the grill.
- Replies to the operator stay short.

## OPEN ITEMS, IN ORDER
1. The START HERE items above.
2. The APK session: `cd ~/agent-stack && claude --resume 125f2d23-df2c-4a1b-823c-45acfa0cf8af` (package IDs `com.aethx.aesc` / `com.clovix.aeyre` awaiting confirmation).
3. NvAEx-agentk: the operator creates the GitHub org; then transfer the repo in as `NvAEx-agentk/skills`.
4. wiki-admin decisions 2b–2e (Obsidian skills loading twice, OmniGlyph, Render MCP, delete `~/.openwiki/`).
5. Everything else in `PENDING.md`.

## RESUMING ON THE OTHER ACCOUNT (same phone)
Sessions are stored on the phone: `claude auth logout`, then `claude auth login`, then `cd <start folder> && claude --resume <id>`.
This session: `cd ~ && claude --resume edd68643-a1df-46c4-a17b-3ef5a61d291f`.

## HANDOFF SOURCES
Read this session: this RESUME (old) + PENDING, `_#Repository-layout.txt`, all of `Master_dumbass_plan-session/` (00–13), `docs/WIKI-ADMIN-GUIDE.md`, `WRAP-UP.md`, `stop-gate.sh`, `git-gate.sh`, `regenerate_masters.sh`, the base repos' CLAUDE/AGENTS/MEMORY files, the Claude Code memory docs (AGENTS.md section), the 11 reader reports, the GitSync plugin settings.
Not read directly: most of `__RESUME.md/` and `Drive_sync/` (the readers covered the usable artifacts; chats only listed), `planner.md` (reader A), docs 00–05.
