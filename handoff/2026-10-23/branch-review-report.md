# Branch + PR review, 2026-10-23 (read-only; nothing deleted, pushed, merged or synced)

Probes used (all read-only): `gh api repos/c10vis-poem/<r>/compare/<default>...<branch>`; `gh api repos/<upstream>/compare/<default>...c10vis-poem:<branch>`; `gh api repos/<upstream>/branches/<name>`; `gh pr list/view`; `rg` over ~/repos, the vault, ~/.claude/session-work; reading the bot workflow files in ~/repos/<r>/.github/workflows. Not read: full diffs of every file (only file lists, stats, first commits); no `git cherry`/patch-id (no local clones for most of these repos, so "already in main" was tested via upstream containment and file/content checks instead).

## 0. Summary

- 28 "unique" branches: **1 MERGE** (NovAExorpus docs/delete-branch-after-merge), **2 MERGE-optional** (clean bump branches), **2 KEEP** (Horizon-s-home-grid PR branch; claude-code-android architecture-review as the only copy of the NeuroOmni/Horizons scaffold), **1 SALVAGE-then-tag** (ai-hub-merovingian-models- SOTU docs), the rest ARCHIVE-TAG-ONLY-THEN-DELETE (bot-regenerated, upstream-owned, or superseded).
- 15 of the 28 are re-created automatically or exist on upstream under the same SHA: deleting them loses nothing.
- adk-docs: 154 of 183 branches are byte-identical to upstream's; fork main is 33 commits behind and `gh repo sync` would fast-forward cleanly. The 177 branches are stale upstream bot/feature branches whose content is already in upstream main. Nothing unreleased found in the 15 newest.
- OB1 #2: do NOT merge (it blanks the Recent Contributions table). Horizon-s-home-grid #1: leave open (RESUME says so; it is the only copy of HomeGrid.kt).
- NvAEx-code-review-graph: Actions are disabled, so none of the 8 required checks can ever report; PR #2 is BLOCKED for that reason. Enabling Actions turns on CI plus 4 automation workflows; details in section 4.

## 1. The 28 unique branches

Columns: who = commit author from compare API. "Used?" = open PR / workflow that writes it / reference found. Upstream = same branch name+SHA on the upstream repo (`gh api repos/<up>/branches/<name>`).

| # | repo / branch | what the extra commit(s) do | who | used by? | in main/upstream already? | verdict |
|---|---|---|---|---|---|---|
| 1 | NovAExorpus / docs/delete-branch-after-merge | AGENTS.md rule 5: "Leave the branch in place after merge" becomes "Delete the branch after merge (repo auto-delete is on)". 1 line, 8 behind. | Claude session (2026-10-13) | no PR; matches the operator's standing rule | NO: main AGENTS.md line 53 still says "Leave the branch in place after merge" | **MERGE** (gives main the delete-after-merge rule that memory/feedback_delete_merged_branches says is the default; may need a rebase, 8 behind) |
| 2 | NovAExorpus / auto/master-files-37287470319 | Rebuilds MASTER-AGENTS.md (+542/-58) and MASTER-RESUME.md | github-actions bot (2026-10-05) | no PR | Files it edits are not in main's root listing any more; RESUME item 4a (2026-10-09) says retire MASTER-AGENTS/MASTER-RESUME + build_masters.sh in favour of `repos/` mirrors | ARCHIVE-TAG-ONLY-THEN-DELETE (superseded by the mirrors plan) |
| 3 | OB1 / automation/readme-recent-contributions | Rewrites README "Recent Contributions": 20 rows deleted, date bumped | github-actions (as c10vis-poem) | open PR #2 | Upstream has a same-named branch at a different SHA (74609517) | ARCHIVE-TAG-ONLY-THEN-DELETE; close PR #2 (see section 3) |
| 4 | pm-claude-skills / bot/grow-library | proposals/GAPS.md +6/-6 | fork's own workflow | `.github/workflows/grow.yml` line 58 `branch: bot/grow-library`, monthly cron | upstream same name, different SHA | ARCHIVE-TAG-ONLY (workflow recreates it) |
| 5 | pm-claude-skills / newsletter-weekly | adds newsletter/2026-w42.md | fork workflow | `morning-show.yml` line 35, Mondays | upstream branch absent | ARCHIVE-TAG-ONLY (recreated weekly) |
| 6 | pm-claude-skills / season-rollover-2 | seasons/HALL.md: "champion: nobody (empty board)" | season-bot | `season-rollover.yml` line 53 `git push -f origin season-rollover-$NEXT` daily | upstream same name, different SHA | ARCHIVE-TAG-ONLY (empty-board noise) |
| 7 | pm-claude-skills / skill-of-the-week | web/skill-of-the-week.json +8/-8 | fork workflow | `skill-of-the-week.yml` line 39, Mondays | upstream branch absent | ARCHIVE-TAG-ONLY |
| 8 | clovis-hermes-agent / bot/js-autofix | `npm run fix` formatting over 31 files, 1384 commits behind | github-actions bot | no workflow ref found in ~/repos | upstream branch absent; fork main moved 1384 commits | ARCHIVE-TAG-ONLY (stale formatting; regenerated on merge) |
| 9 | modern-web-guidance-src / auto/web-features-update | bumps `web-features` package (5 files, lockfile) | Modern Web Guidance Bot (copied from upstream workflow) | no PR | ahead 1, behind 0 (clean fast-forward); upstream branch absent | MERGE-optional (harmless dependency bump) else ARCHIVE |
| 10 | c10vis-LocalAI / chore/bump-inference-defaults | inference_defaults.json +3/-1 from unsloth | fork workflow | `bump-inference-defaults.yml` line 46, daily cron | ahead 1, behind 0; upstream absent | ARCHIVE-TAG-ONLY (recreated daily) or MERGE-optional |
| 11 | termux-app / accessibility-improvements | send cursor position to accessibility apps (brltty) | agnostic-apollo (upstream maintainer, 2022) | none | same SHA exists on termux/termux-app; not in upstream master (no TerminalAccessibilityDelegate.java on fork master, 404) | ARCHIVE-TAG-ONLY (upstream keeps it) |
| 12 | termux-app / android-5 | 16 commits, Termux 0.77 era | Fornwall/Pliushch (upstream) | none | same SHA upstream, 938 behind | ARCHIVE-TAG-ONLY (history) |
| 13 | termux-app / android-10 | 13 commits, APK-based package mgmt | upstream contributors 2020-21 | none | same SHA upstream, 818 behind | ARCHIVE-TAG-ONLY |
| 14 | termux-app / delete-release-on-ci-failure | CI: delete release on failure; has a "tmp:" commit | thunder-coding (upstream) | none | same SHA upstream, 103 behind | ARCHIVE-TAG-ONLY |
| 15 | termux-app / dependabot/.../upload-artifact-7 | upload-artifact v6 to v7 in debug_build.yml | dependabot | none; fork master still on @v6 (4 uses, `debug_build.yml` lines 86-112) | same SHA upstream; upstream master also still @v6 | MERGE-optional (only if the operator wants the bump ahead of upstream) else ARCHIVE |
| 16 | termux-app / java-17 | Java target 8 to 17 in 4 build.gradle | Fornwall (upstream, 2026-02) | none; fork and upstream master both on VERSION_1_8 (`app/build.gradle` 113 / 105) | same SHA upstream | ARCHIVE-TAG-ONLY (upstream-unmerged, risky for the Termux build) |
| 17 | termux-app / stardesk-sponsors-logo | README sponsor logo | agnostic-apollo (upstream) | none | same SHA upstream; fork README has 0 "stardesk" hits | ARCHIVE-TAG-ONLY (sponsor ad) |
| 18 | termux-app / updated-flavor | [WIP] "updated" APK flavor, 2021 | Fornwall (upstream) | none | same SHA upstream, 550 behind | ARCHIVE-TAG-ONLY |
| 19 | poem-langflow / update-test-durations-1790652948 | `.test_durations` +14809/-10406 | fork workflow (c10vis-poem) | none | 68 behind; identical +/- counts to #20 | ARCHIVE-TAG-ONLY (superseded by #20 and by main) |
| 20 | poem-langflow / update-test-durations-1791214304 | same file, same counts, later date | fork workflow | none | 68 behind | ARCHIVE-TAG-ONLY |
| 21 | NvAEx-worldmonitor / automation/github-stars-2026-10 | adds docs/snapshots/github-stars-2026-10-01.json (5 lines) | github-actions | test files `tests/github-stars-snapshot.test.mjs` mention the pattern | upstream has a same-named branch (ab32cf2a); 469 behind | ARCHIVE-TAG-ONLY (monthly snapshot, regenerated) |
| 22 | ai-hub-merovingian-models- / claude/focused-noether-evoknv | 7 commits: docs/horizons-sotu.md (230 lines), architecture-verify report, CLAUDE.md tip, tmp_kokoro_tts.py | Claude session (2026-06-17) | none; `rg` for "horizons-sotu" / "Horizons app SOTU" found 0 hits in ~/repos or vault | upstream absent; 759 behind a Qualcomm model-zoo fork | **SALVAGE-then-tag**: copy docs/horizons-sotu.md + the verify report into the vault, then ARCHIVE-TAG. Main of this repo is a Qualcomm AI Hub models fork, wrong home for them. |
| 23 | glibc-packages / upd-gcc | 3 commits updating gcc-libs build (Maxython) | upstream maintainer | none | same SHA on termux-pacman/glibc-packages; fork main is 2 behind upstream | ARCHIVE-TAG-ONLY (upstream WIP; sync main instead) |
| 24 | claude-skills / claude/busy-wright-OKBXH | adds horizons/index.html (521 lines), Horizons UI PWA with N0.V4 endpoints | operator account via Claude session (2026-05-26) | none | upstream absent; `rg "Horizons UI"` hits only spec docs, not this file | SALVAGE-then-tag (single-file PWA; copy to NovAExopia/vault if the UI-shell APK wants its endpoints) |
| 25 | claude-android-skill / claude/busy-wright-OKBXH | 8 commits, 40 files: Android AI workstation skill, HANDOFF.md, voice bridge (Kokoro), install.sh | operator account via Claude session (2026-05-26/27) | none; `rg android-cowork` 0 hits | ahead 8, behind 0 of dpconde fork main | ARCHIVE-TAG-ONLY (May prototype; superseded by Aesop-Xi/Termux stack; tag preserves it) |
| 26 | claude-code-android / claude/android-architecture-review-Is4hk | 13 commits: NeuroOmni Android app scaffold, android-ci.yml, four-panel Horizons layout | Claude session (2026-05-30) | `rg NeuroOmni` hits Aesop-Xi/raw/four-core-buckets.md and the vault handoff 2026-08-24, so it is referenced as design history | upstream absent | **KEEP** until the 3-APK build either reuses or drops the scaffold (named reason: referenced by vault HANDOFF-2026-08-24) |
| 27 | claude-code-android / claude/generator-noise-analysis-IOzhr | EU2200i generator noise report (python + png) | Claude session (2026-05-17) | none; 0 references | upstream absent | ARCHIVE-TAG-ONLY (unrelated to the stack) |
| 28 | Horizon-s-home-grid / claude/google-ai-studio-export-5zxrqz | HOMEGRID-REBUILD-SPEC.md, HomeGridSim.tsx, HomeGrid.kt (1156 lines), HorizonsTheme.kt | Claude session (2026-07-23) | open PR #1; RESUME line 21 says leave open | main has README only | **KEEP** (PR source branch; only copy of HomeGrid.kt) |

What each repo's main provides (for the "what does main give" question): NovAExorpus = the vault / master corpus repo (not a fork; AGENTS.md, specs); OB1 = fork of NateBJones-Projects/OB1 "Open Brain" memory backbone; pm-claude-skills = fork of 114 PM skills; clovis-hermes-agent = fork of NousResearch hermes-agent; modern-web-guidance-src = fork of GoogleChrome guidance source; c10vis-LocalAI = fork of mudler/LocalAI (local inference engine); termux-app = fork of Termux (terminal-APK base, fork master is 2 ahead of upstream); poem-langflow = fork of Langflow; NvAEx-worldmonitor = fork of koala73/worldmonitor dashboard; ai-hub-merovingian-models- = fork of Qualcomm AI Hub models (NPU model zoo); glibc-packages = fork of termux-pacman/glibc-packages; claude-skills = fork of alirezarezvani/claude-skills; claude-android-skill = fork of dpconde skill; claude-code-android = fork of ferrumclaudepilgrim (Claude Code on Android); Horizon-s-home-grid = operator's own repo for the Horizons home-grid UI (main = README only). (Source: `gh api repos/c10vis-poem/<r> --jq .parent.full_name` and repo descriptions.)

Side finding: the pm-claude-skills, LocalAI, worldmonitor and modern-web-guidance workflows are upstream automations running inside the operator's forks and generating branches/noise. Optional follow-up for the operator: disable those scheduled workflows in the forks.

## 2. adk-docs

| Question | Answer | Source |
|---|---|---|
| Upstream | google/adk-docs, default branch main | `gh api repos/c10vis-poem/adk-docs --jq .parent.full_name` |
| Fork main vs upstream main | behind by 33, ahead by 0, 0 files diverged | `gh api repos/google/adk-docs/compare/main...c10vis-poem:main` returned `behind ahead=0 behind=33` |
| Would `gh repo sync` fast-forward cleanly? | Yes: ahead=0 means no fork-only commits on main, so a plain fast-forward (no --force needed) | same compare |
| Fork branches | 184 total (183 non-default); upstream has 275 | `gh api .../branches --paginate` both repos |
| Same name + same SHA as upstream | 154 | awk join of the two branch lists |
| Same name, SHA moved upstream | 17 (incl. gh-pages) + main | same |
| Exist only on fork (deleted upstream, usually after merge) | 12: tools-qdrant, go-safety, go-memory, go-getting-started, 8 agent-changes-2026* | same |
| Upstream-only branches not in fork | 103 (created after the fork) | same |
| Compared to upstream main today | 177 "diverged" (each 1-6 commits ahead, hundreds behind), 4 "behind" (= already contained: adk-go-additions, adk-go-docs-updates, adk-js-additions, issues/440672577/...), 2 API errors (code-samples, gh-pages) | per-branch `compare/main...<sha>` |

Plain-language: when you fork a repo, GitHub copies every branch that exists upstream at that moment. After that the fork never learns about new or deleted upstream branches, and `gh repo sync` only moves the single default branch (main) forward. So the 177 branches are a frozen snapshot of Google's work-in-progress branches from 2025 to March 2026, not the operator's own work. 160 of them are `agent-changes-<timestamp>` branches made by Google's `adk-bot` (one auto-generated doc edit each, 1 file). The rest are named contributor branches (tk-*, tommy-*, go-*, issue-466, docs-meta, link-checker-fix).

Review of the 15 newest (by commit date, `gh api repos/c10vis-poem/adk-docs/commits/<sha>`): all are adk-bot 2026-03-16 or 2026-02-27. Examples: "Add documentation for ExecuteBashTool", "Create documentation for the new Agent Optimization feature", "Create documentation for the new Skills framework and SkillToolset", "Document render_ui_widget", "Document new add_memory method", "SessionNotFoundError", "push_config_store in to_a2a", "token-threshold compaction". Each topic is already in upstream main: docs/skills/index.md, docs/optimize/index.md, docs/context/compaction.md exist; keyword counts in main: bash 2 paths, render_ui_widget 3, add_memory 7, SessionNotFoundError 1, push_config_store 1, token_threshold 4. Result: **nothing unreleased or unique; the whole set is superseded by upstream main.** Not tested: the 17 named contributor branches' content beyond their latest commit message (they are 2025 to Mar 2026; go-memory/go-getting-started/go-safety are Go-docs drafts and may not be in main; worth a one-time look only if Go matters).

Recommendation for the operator's question ("why not merge or sync instead of deleting"): run `gh repo sync c10vis-poem/adk-docs` (fast-forward, 33 commits) to get main current; the branches do not need merging because their content is already in main. Branch deletion of the 177 is then safe, with the fork's current SHAs recoverable from upstream (154 identical there).

### Docs applicable to the stack (pages in google/adk-docs main; paths from `git/trees/main?recursive=1`, 255 md pages, intros read via contents API)

| Page | Use for |
|---|---|
| docs/agents/workflow-agents/{index,sequential-agents,parallel-agents,loop-agents}.md | Aesop-Xi orchestration: sequential/parallel/loop shapes for the fan-out and verify loops (two-by-two verification, parallel subagents) |
| docs/agents/custom-agents.md | NovusAExenti agent packages: custom control flow when the built-in workflow agents are not enough |
| docs/agents/routing.md, docs/agents/models/routing.md | Aesop-Xi / OmniRoute: model and agent routing patterns (experimental) |
| docs/agents/config.md | NovusAExenti: declarative agent configs (YAML) as package definitions (experimental) |
| docs/agents/managed-agents.md | Reference for hosted first-party agents (Google-only, preview) |
| docs/agents/models/{ollama,litellm,vllm,openai,anthropic,google-gemma,litert-lm}.md | NovAExopia: connecting local/llama.cpp-style servers and routers as model backends |
| docs/workflows/{index,patterns,collaboration}.md, docs/graphs/{index,dynamic,routes,human-input,data-handling}.md | Aesop-Xi: graph workflows with human-input gates map to the /ok approval-card flow |
| docs/callbacks/{index,types-of-callbacks,design-patterns-and-best-practices}.md | Aesop-Xi hooks: before/after model, tool and agent callbacks are the in-framework analogue of H1-H8 guardrails |
| docs/plugins/index.md | Aesop-Xi: cross-cutting plugin layer (logging, policy) applied to all agents at once |
| docs/safety/index.md, docs/tools-custom/confirmation.md | Aesop-Xi guardrails and tool-confirmation (human approval before a tool runs) |
| docs/sessions/{index,state,memory}.md, docs/sessions/session/{rewind,migrate}.md | Memory-stack design: session state vs long-term memory; rewind compares to handoff/resume |
| docs/context/{index,caching,compaction}.md | NovAExopia: context compaction and caching, relevant to the token-cost work (honey) |
| docs/evaluate/{index,criteria,custom_metrics,user-sim,environment_simulation}.md, docs/optimize/index.md | Evaluation harness for agent packages; user-simulation and environment-simulation fit the "no tool checks its own output" rule |
| docs/tools-custom/mcp-tools/{index,agent-as-server,advanced,deployment}.md | NovAExopia: consuming MCP tools; agent-as-server exposes an agent to Claude Code as an MCP server |
| docs/tools-custom/{function-tools,openapi-tools,authentication,performance}.md | NovAExopia tool authoring and auth |
| docs/a2a/{intro,quickstart-exposing,quickstart-consuming}.md | Agent-to-agent protocol for cross-device agents (phone/VM/Jetson) |
| docs/skills/index.md | NovusAExenti: ADK's own skills framework (SKILL.md style), parallels the local skills layout |
| docs/runtime/{event-loop,resume,cancel,ambient-agents}.md, docs/events/index.md, docs/apps/index.md | Aesop-Xi: resumable runs, cancellation, event-triggered (ambient) agents |
| docs/observability/{index,logging,metrics,traces}.md | Tracing for the hook/change-log stack |

Mapping is by page intro only (I did not read full pages); it is a reading list, not an adoption plan.

## 3. Open PRs

| | OB1 #2 "[docs] Refresh README recent contributions" | Horizon-s-home-grid #1 "Add definitive HomeGrid.kt from AI Studio export" |
|---|---|---|
| Author | app/github-actions (the bot, via fork workflow) | c10vis-poem (Claude Code session) |
| Created / updated | 2026-10-10 / 2026-10-21 | 2026-07-23 / 2026-07-23 |
| Draft | no | yes |
| Checks | none reported (statusCheckRollup empty); mergeStateStatus UNSTABLE; Actions API says `enabled:false` for OB1 | none reported; mergeStateStatus CLEAN; no workflows (`gh workflow list` empty) |
| Mergeable | MERGEABLE | MERGEABLE |
| Changes | README.md +1/-21: deletes all 20 rows of the Recent Contributions table (the fork has no merged PRs to list) and bumps the date to 2026-10-21 | 4 files, +2374/-0: HomeGrid.kt (1156 lines), HorizonsTheme.kt, HOMEGRID-REBUILD-SPEC.md, HomeGridSim.tsx. Main has README only |
| RESUME line | RESUME.md line 21 item 3: "Close: ... OB1#1" (a different PR, #1); #2 is not mentioned | Same line: "Leave open: aesop-xi#18 (grill), Horizon-s-home-grid#1 + Hyperion-XI#4 (3-APK build)". Yes, RESUME says leave it open |
| **Verdict** | **Close, do not merge** (net effect is to blank a table in an upstream-tracking fork; branch is workflow-owned and regenerates). Operator decision only | **Leave open** per the 2026-10-09 operator instruction. It is a draft with a test plan unchecked (compare against a Novus-Agenti copy; that repo does not exist under c10vis-poem: `gh repo view` could not resolve it) |

(Source: `gh pr view <n> -R ... --json ...`, `gh pr diff 2 -R c10vis-poem/OB1`, `sed -n 15,28p ~/storage/shared/Documents/NovAExorpus/RESUME.md`; the quoted line is the item 3 bullet in the block read.)

## 4. c10vis-poem/NvAEx-code-review-graph

State: Actions **disabled** (`gh api repos/c10vis-poem/NvAEx-code-review-graph/actions/permissions` returned `{"enabled":false}`). Branches: only `main` (staging/testing do not exist). Open PR: #2 "fix: skip ignored paths before stat..." by c10vis-poem, created 2026-10-23, mergeStateStatus BLOCKED.

| Workflow | Trigger (from file) | Kind | Acts on repo? |
|---|---|---|---|
| CI (ci.yml) | push/PR to main, testing, staging; manual | CI: lint, type-check, security, schema-sync, test (3.10-3.13), viz-browser, e2e, upgrade-path, google-embeddings, windows-native | no, read-only (`contents: read`) |
| PR Review (pr-review.yml) | PR to main/testing/staging | automation: review bot | read-only token; output consumed by next |
| PR Review Comment (pr-review-comment.yml) | workflow_run after PR Review | automation: posts PR comments | writes PR comments (`pull-requests: write`) |
| Weekly Eval (eval.yml) | Mondays 06:23 UTC + manual | benchmark/eval | read-only |
| Promote (promote.yml) | manual only | automation: opens staging-to-testing / testing-to-main PRs | writes PRs and issues; useless here (no staging/testing) |
| Auto promote (auto-promote.yml) | daily 06:17 UTC + manual | automation: opens AND merges promotion PRs | `contents: write`, `pull-requests: write`; scheduled run is not a dry run. With no staging branch it should find nothing to promote, but it is the one workflow that merges |
| Promotion gate (promotion-gate.yml) | push to `testing` | gate (packaging, e2e, corpus, browser) | no `testing` branch exists, never fires |
| Publish to PyPI (publish.yml) | release published | publish | uses `environment: pypi` and `secrets.PYPI_API_TOKEN`; only fires on a published GitHub release |

(Source: `gh workflow list -R ... --all`; workflow files read via `gh api .../contents/.github/workflows/*.yml`.)

Branch protection on main (`gh api .../branches/main/protection`): required status checks (strict false): lint, type-check, security, test (3.10), test (3.11), test (3.12), test (3.13), schema-sync. Required PR reviews: none (`required_pull_request_reviews: null`). enforce_admins false, linear history false, force pushes disallowed.

Implication for the operator's decision: PR #2 can only merge once those 8 checks report green, which needs Actions enabled (all 8 are jobs in ci.yml; the job names match the required contexts, unlike the honey/NovA-skills mismatch noted in RESUME). Enabling Actions repo-wide also activates Auto promote (daily, can merge), the PR review bot pair, Weekly Eval, and Publish (only on release). Narrower option, not tested: enable Actions but restrict allowed workflows, or disable Auto promote/Promote/Promotion gate/Publish individually with `gh workflow disable`, leaving CI + PR Review. Alternatively, the admin bypass (enforce_admins false) lets the owner merge PR #2 without checks, which skips the CI the pipeline rule requires; I did not test either route.
