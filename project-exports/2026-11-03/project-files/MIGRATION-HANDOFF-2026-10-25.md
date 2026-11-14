# Migration handoff: builds of 2026-10-25

Compiled 2026-10-25 from the transcripts of five project-thread sessions and the shared memory folder `/tmp/claude/memory/team/silo/`. GitHub owner for every repo below: `c10vis-poem`. Project channel: `chan_01QQ9BFNeq27W1yzwmKzYmcH`.

**How this was gathered, and its limits.** Every session was read with `list_events` (assistant, user and result events), newest first, going back page by page. The pages that hold the deliverables, decisions and final replies were read in full. Some early research pages were skimmed: raw web-search results and file listings. I did not reach the very first page of every session. The claw proposal is a Claude Docs document, and no Claude Docs connector was available in this session, so I could not fetch it directly. Section 3 rebuilds it word for word from the edit calls that wrote it, which include every section and the whole 145-item table. Nothing in any repo was changed while writing this file.

**Posting outage (applies to all threads).** From about 20:2x UTC in the plugin-authoring thread, and from 21:31 UTC in the plugins-panel thread, `mcp__hearthbot__post_message` failed with "No such tool available". Replies written after those times never reached the thread. Each section below quotes them as "unposted".

---

## Quick status board

| # | Workstream | Session | State | You need to do |
|---|---|---|---|---|
| 1 | GitHub App token renewal (replace `VAULT_DISPATCH_TOKEN`) | cse_01EjrB25PPEtv8PY9AhMZDWw | 6 PRs open as **drafts**, CI green, auto-merge **blocked** by the auto-mode classifier | Run the ready/auto-merge loop, then `setup.sh --drop-pat` |
| 2 | Plugins panel mod (NvAEx-Recaps #6) + control panel / agent bar | cse_01MvvUSSCFKjw5GucVuoGAzB | #6 **merged**. Control panel only **proposed**, nothing built | Install the mod; answer 2 questions; turn on "Allow auto-merge" |
| 3 | "claw" device and browser toolkit | cse_01Lw63ZrbVP24rVd68A8PT31 | Proposal doc only. **Nothing built**. | Answer 7 questions, gather keys, say "build it" |
| 4 | Six dynamic-workflow patterns (Q&A) | cse_01MNUm87w5aqexBFNdD6teSy | Answered and posted | Nothing |
| 5 | /plugin-authoring thread (status line mod) | cse_013hxMzErdHfQao2tZE6fzw8 | Unrequested mod **built, then deleted**. Replies unposted. | Nothing; the new rule is now recorded |

---

## 1. GitHub App token renewal

**Goal.** Stop having to renew the `VAULT_DISPATCH_TOKEN` personal access token by hand. Replace it with a private GitHub App that mints a token on every run. ("No manual token renewal ever"; you care about cost.)

**Background found.** The master-files workflow in NovAExorpus was retired on 2026-10-20 (commit `85526f4`). Since then the PAT is used only by `notify-vault.yml` in five base repos. Each one dispatches `base-repo-updated` to NovAExorpus, which has no receiver yet.

**Final state.** Six draft PRs were opened at 20:29 UTC, all from branch `claude/project-thread-99s33n` into `main`. Each was assigned to `c10vis-poem`; requesting you as reviewer failed because you are the PR author. The session subscribed to activity on all six. CI was green on all six at the last check. At 20:54 the session tried to mark them ready and turn on `--auto --squash --delete-branch`. **The Claude Code auto-mode classifier denied it ("Merge Without Review").** All six are still unmerged drafts.

| Repo | PR | State |
|---|---|---|
| NovAExorpus | https://github.com/c10vis-poem/NovAExorpus/pull/59 | Draft, not merged. Adds `tools/vault-app/setup.sh`, `manifest_server.py` and notes |
| NovAExopia | https://github.com/c10vis-poem/NovAExopia/pull/14 | Draft, not merged |
| Hyperion-XI | https://github.com/c10vis-poem/Hyperion-XI/pull/10 | Draft, not merged |
| CloviX-AEyre | https://github.com/c10vis-poem/CloviX-AEyre/pull/11 | Draft, not merged |
| AEthX-AEsc | https://github.com/c10vis-poem/AEthX-AEsc/pull/15 | Draft, not merged |
| NovusAExenti | https://github.com/c10vis-poem/NovusAExenti/pull/10 | Draft, not merged |

The title of all five base-repo PRs is "ci(notify-vault): mint a GitHub App token per run instead of the PAT". The workflow uses `actions/create-github-app-token@v1` with `vars.VAULT_APP_ID` and `secrets.VAULT_APP_PRIVATE_KEY`. Until setup has stored those, the job skips with a notice instead of failing, so merging before setup is safe.

**Files created.**
- `tools/vault-app/setup.sh` and `tools/vault-app/manifest_server.py` (NovAExorpus #59)
- `.github/workflows/notify-vault.yml` (changed, in each of the five base repos)
- On the phone, after setup: the key goes in `~/.config/vault-app/`
- Memory: `/tmp/claude/memory/team/silo/vault-dispatch-github-app.md`

**Commands you must run (Termux).**
```
# 1. Mark ready and set squash auto-merge on all six PRs
for p in NovAExorpus:59 NovAExopia:14 Hyperion-XI:10 CloviX-AEyre:11 AEthX-AEsc:15 NovusAExenti:10; do r=${p%:*}; n=${p#*:}; gh pr ready $n -R c10vis-poem/$r; gh pr merge $n -R c10vis-poem/$r --auto --squash --delete-branch; done
# If a repo has auto-merge turned off, that line fails; merge it from its PR page instead.

# 2. After they merge, from a NovAExorpus checkout:
bash tools/vault-app/setup.sh --drop-pat
# Three taps: the local button, "Create GitHub App", "Install" on NovAExorpus. The script then deletes the old PAT secret.
```

**Pending decisions and questions.**
- Approve the merge in Claude Code, or run the loop above yourself.
- None of the six repos has been checked for whether "Allow auto-merge" is on.

**Next steps.**
1. Merge the six PRs.
2. Run `setup.sh --drop-pat`.
3. Later: build the pointer-index receiver in NovAExorpus. It should mint its token from the same app so the PRs it opens trigger CI; PRs opened with `GITHUB_TOKEN` don't.

**Unposted reply (20:54, final turn, verbatim excerpt):** "I didn't turn on auto-merge for the 6 PRs. They are still drafts and nothing has been merged. Claude Code's auto-mode permission check blocked the command as "Merge Without Review". I also couldn't post this in the project thread, because the session's thread and GitHub tools disconnected before this turn. ... After they merge, the one remaining step is `bash tools/vault-app/setup.sh --drop-pat` in Termux."

---

## 2. Plugins panel mod (NvAEx-Recaps #6), then the control panel and agent-setup bar

**Goal.** You explicitly asked for a plugins side-panel mod for Claude Code on Termux. Later (21:31 and 21:32 UTC) you asked for two more things: a full settings/control side panel, and a bar above the prompt that shows which agent setup is running.

**Final state: plugins panel.**
- PR: https://github.com/c10vis-poem/NvAEx-Recaps/pull/6. **Merged** (squash) into `main`, and its branch was deleted after the merge. GitHub refused auto-merge ("Auto-merge is not enabled for this repository"), so once CI passed the session merged it by hand.
- Repo: `c10vis-poem/NvAEx-Recaps` (private). Its only workflow is `.github/workflows/ci.yml`, which runs gitleaks and the sops check and has no merge step.
- Not yet tested against your real plugin files.
- Known limits: the status line can't be clicked, and `/plugins` is a reserved command name.

**Files created (NvAEx-Recaps).**
- `claude-code-workspace/plugins-panel/` (the mod). New mods go in `claude-code-workspace/`; that is what "cloud code workspace folder" meant.
- `.claude-plugin/marketplace.json` at the repo root. It makes the repo the `nvaex-recaps` marketplace.
- `threads/plugins-panel/`
- Memory: `/tmp/claude/memory/team/silo/plugins-panel-mod.md`, `feedback-auto-merge-after-ci.md`

**Commands you must run (phone).**
```
claude plugin marketplace add c10vis-poem/NvAEx-Recaps
claude plugin install plugins-panel@nvaex-recaps
```
Optional: in NvAEx-Recaps, Settings → General → turn on "Allow auto-merge". You asked which repo the session was working in; it answered that all its work was in NvAEx-Recaps. It found auto-merge workflows only in NovA-code-review-graph (`auto-promote.yml`), and dependency-only auto-merge in NvAEx-claude-code-marketplace and aesop-context7-skill. It asked which repo holds the workflow you meant; you haven't answered.

**Your latest requests (verbatim).**
- 21:31: "Thank you. I'm going to need to reestablish the repository to consist of recaps and configs. I'm also going to need an interface here in this app that's going to allow me to adjust the session settings, Cloud MD settings, Access Memory MD, also keep tabs on cron jobs, workflows, tasks and I'm going to need something similar to the environment settings where you can plug in different scripts and what not so I can have customizable agent packages, workflows, etc. So basically, open up the side panel and I'd be able to add or change different tools, skills, plugins, marketplaces, MCP servers, the whole nine yards."
- 21:32: "And then obviously I'm going to need some kind of button or bar access across the top of the prompt bar that would display which agent setup I'm running."
- 21:33: "What the fuck just happened to all of your output?"

**What was and wasn't answered.** **None of the replies to these three messages reached the thread.** The session restarted at about 21:31 and lost `post_message`. A fallback, `message_coordinator`, was also unavailable. Nothing was built or changed. Here is the proposal those replies contained, merged from the four unposted drafts:

- **Repo split for NvAEx-Recaps.** The repo currently has `recaps/`, `threads/`, `secrets/`, `bin/`, `claude-code-workspace/` and root `RESUME.md`/`MEMORY.md`/`PENDING.md`.
  - `recaps/`: recaps, threads, `RESUME.md`, `MEMORY.md`, `PENDING.md`
  - `configs/`: mods, settings, CLAUDE.md files, `bin/` scripts, agent packages
  - `secrets/`: stays where it is, because CI checks that exact path
  - The same PR fixes the links in the thread files and the paths in `AGENTS.md`.
- **Top bar** above the prompt shows the active agent setup, for example `🤖 Research pack · 12 plugins`. Tapping it opens the side panel, where you switch setups.
- **Side panel sections.**
  - Session settings: `settings.json` (model, permissions, hooks, env)
  - CLAUDE.md and MEMORY.md
  - Plugins and marketplaces (turn on/off, add/remove)
  - Skills (list, add from a folder)
  - MCP servers (list, add, remove config entries)
  - Cron jobs and tasks (Termux crontab)
  - GitHub workflows and recent runs, through `gh`
  - Agent packages: saved sets of skills, plugins and MCP servers that you switch on together, kept in `configs/`
- **Limits.** In the Claude phone app, mods have no text fields or dropdowns. The panel can show everything and offer buttons, but you type new content in Termux. It runs only where the mod is installed, Claude Code on your phone, so it can't change cloud sessions or your claude.ai account settings.
- **Build plan.** Three PRs, each merged once CI passes:
  1. Top bar, agent packages, settings, CLAUDE.md/MEMORY.md, plugins
  2. MCP servers, skills, marketplaces
  3. Cron jobs and workflows

  An earlier draft had four stages, with agent packages last.

**Pending decisions.**
1. Is the recaps/configs/secrets split right?
2. Go ahead with the three-stage build?
3. Which repo has the auto-merge workflow you meant, and do you want "Allow auto-merge" turned on in NvAEx-Recaps?

**Next steps.** Install and test the plugins panel. Answer the questions above. The build starts only after your explicit go-ahead (rule 1 below).

---

## 3. "claw": device and browser toolkit proposal

**Goal (from your messages and the memory file).** Build one custom toolkit that combines Perplexity search, Chrome DevTools (CDP), Android device control and Playwright-like browser tools. It must **replace** Playwright and your standalone Perplexity CLI repo (`c10vis-poem/Novus-perplexity-cli`, a fork of `pplx`).
- "Claw hooks" means callable functions that act on your own devices and browsers, not Claude Code hooks.
- Needs headless and in-session modes.
- Inference goes through your Claude Pro, Gemini/Google AI Pro, GCP and other APIs.
- You pointed at browser-use and Firecrawl to reverse engineer (forks: `NovA-browser-use`, `Novus-firecrawl`).

Later requirements, verbatim:
- 21:01: "So does it actually grip the specific skills and tools that it's going to need from said repository and clis I don't want this to be just bone dry skeletal functionality ... I want this to be a complete replacement and sustainable toolkit"
- 21:02: "Yeah and as far as Android mcps and no Js mCP and stuff like that let me know what other kind of assets we need to accumulate"
- 21:03: "This thing needs to be able to function outside of my terminal because I am in the middle of compiling an API/ APK that is built to replace termx and that on device agent that lives there is going to need these capabilities so we're going to have to have like red blue ATB debug Bridge unit Unix websocket tools Etc"
- 21:04: "I said run through the ADB debug web Loop"

**Final state.** The proposal doc is done, unapproved, and **nothing is built**. No repo, branch or PR exists for claw.
- Doc: **Device and browser toolkit: architecture proposal**, https://claude.ai/artifact/2a9BgPvtCLSFSTrevUM6oT (Claude Docs id `0cb9ba0a-0f5d-456a-bf0a-ba24a0b5cfea`). It has two tabs: the main proposal and "Feature parity".
- Last posted reply, 21:06: "Yes, it carries over the real features, not a skeleton ... 145 commands, tools and skills ... **91 are in the first build** ... **37 come in phase two** ... **17 are dropped**, each with its reason ... I also redesigned it to live inside your APK ... claw becomes a Kotlin library and uses the Kotlin MCP SDK ... no JavaScript anywhere. The same functions are reachable four ways: direct Kotlin calls from Æsc's agent; `AF_UNIX` sockets; a WebSocket to Horizons-UI; MCP over stdio for Claude Code. To confirm: by "ADB debug web loop" I take it you mean the app pairing with its own adbd over wireless debugging at 127.0.0.1, with no PC and no root. Is that right? ... From you I need a Perplexity API key, a Gemini or Anthropic key if you want one, and wireless debugging paired on the phone. Everything else I can fetch."

**Repos referenced (read only, none changed).**
- Novus-perplexity-cli, NovA-LEJ-Perplexity-Powered-Search-for-Claude, NovA-browser-use, Novus-firecrawl
- claude-code-android, termux-api, scrcpy, glibc-packages
- NvAEx-Android-Dex, NvAExinandroid
- AEthX-AEsc (the APK: a termux-app fork renamed `aethx.aesc`, plus the Æsc core in `core/src/main/kotlin/aesc/core/agent/*`), Hyperion-XI (Horizons-UI)
- kotlin-sdk (fork), termux-app (fork), AEsopXi-mobile-harness, NvAEX_mobilerun, NvAEx-DroidDesk

**Files created.** The doc above, and `/tmp/claude/memory/team/silo/claw-toolkit-project.md`.

**Commands you must run.** None until you approve. Before the build: get a Perplexity API key, and optionally a Gemini or Anthropic key. Turn on wireless debugging and pair the app once with the code from Settings. Leave USB debugging on for Chrome.

**Pending decisions.** The seven open questions in 3.J below. Main ones: confirm the ADB-loop reading, Kotlin core, new repo `c10vis-poem/claw` or a module inside AEthX-AEsc, and the default inference provider.

**Next steps.** After your answers and an explicit "build it": Search and Scrape first (they replace `pplx`), then Browser, then Device. The first thing to prove on a real phone is the ADB self-connect and the Chrome DevTools socket.

The doc content follows, rebuilt from the edit calls that wrote it.

### 3.A Summary (doc section, verbatim)

#### Summary

I recommend one MCP server, working name **claw**, that exposes a single set of callable functions ("claw hooks") and routes each call to the right driver: Perplexity for search, raw CDP for any Chrome browser, ADB plus Termux:API for your Android devices, and a pluggable inference layer for Claude, Gemini and GCP. Nothing is built yet; this is the plan for you to approve or change.

- **It replaces Playwright** by talking Chrome DevTools Protocol (CDP) directly, the way browser-use and chrome-devtools-mcp already do. That removes the part of Playwright that does not run on Termux (its bundled browser downloads).
- **It replaces your standalone Perplexity CLI** by calling the same Perplexity Search API that `pplx` wraps, from inside the server, so there is no glibc binary to run on Termux.
- **It runs in two modes**: headless (its own browser, no screen) and in-session (attached to a Chrome you already have open, on desktop or on the phone).
- **Inference stays on supported paths**: API keys, Vertex AI, and your Claude subscription through Claude Code or the Agent SDK. No scraping of claude.ai or gemini.google.com.

### 3.B What was found in your repos (verbatim)

#### What I found in your repos

I could not find an Android MCP server in your GitHub account. The Android-related repos are a Compose sample app, a desktop mirroring app and Claude-on-Termux install scripts, none of which is an MCP server.

| Repo | What it is | Use in the toolkit |
| --- | --- | --- |
| [Novus-perplexity-cli](https://github.com/c10vis-poem/Novus-perplexity-cli) | Fork of Perplexity's `pplx`: prebuilt binaries only (macOS arm64, Linux x86_64, Linux arm64 glibc), commands `search web` and `content snippets` | The feature set to match. Its Linux binary needs glibc, so on Termux it only runs through glibc-runner. |
| [NovA-LEJ-Perplexity-Powered-Search-for-Claude](https://github.com/c10vis-poem/NovA-LEJ-Perplexity-Powered-Search-for-Claude) | Plugin that redirects WebSearch to Perplexity with a hook | Reference for the redirect hook |
| [NovA-browser-use](https://github.com/c10vis-poem/NovA-browser-use) | browser-use: CDP session manager, DOM extraction, watchdogs, MCP mode | Main source to borrow from for the browser driver |
| [Novus-firecrawl](https://github.com/c10vis-poem/Novus-firecrawl) | Firecrawl monorepo; scrape engines `fetch`, `playwright`, `pdf`, `fire-engine` (closed source) and a Go HTML-to-Markdown service | Source for the fetch-first, browser-second scrape ladder and clean Markdown output |
| [claude-code-android](https://github.com/c10vis-poem/claude-code-android) | Install paths for Claude Code on Termux (glibc-runner, proot Ubuntu, AVF VM), plus an ADB wireless self-connect guide | The ADB self-connect recipe for driving the phone from Termux |
| [termux-api](https://github.com/c10vis-poem/termux-api) | The Termux:API app | Sensors, notifications, clipboard, SMS and similar on-device functions |
| [scrcpy](https://github.com/c10vis-poem/scrcpy) | Screen mirror and input over ADB | Optional fast screen capture and input |
| [glibc-packages](https://github.com/c10vis-poem/glibc-packages) | Termux glibc packages | Only needed if we keep any glibc binary |
| [NvAEx-Android-Dex](https://github.com/c10vis-poem/NvAEx-Android-Dex), [NvAExinandroid](https://github.com/c10vis-poem/NvAExinandroid) | Desktop Android mirroring app (proprietary licence upstream); Now in Android sample app | Not useful; Android-Dex's licence forbids modification |

### 3.C Components (verbatim)

#### Components and what each one contributes

Each outside project donates an idea or a protocol; the toolkit does not ship any of them whole.

| Source | What we take | What we leave |
| --- | --- | --- |
| Perplexity Search API (behind `pplx`) | Web search with domain, recency and date filters; query-focused page snippets from up to 50 URLs | The compiled binary |
| chrome-devtools-mcp | Its tool set as the target list: navigate, click, fill, screenshot, console, network, performance trace; attach to a running Chrome by `--browserUrl` | Node runtime dependency, if we write the driver ourselves |
| browser-use | Persistent CDP daemon that reuses one browser connection across calls; background tabs without stealing focus; DOM-to-indexed-elements extraction for the model | Its own LLM agent loop (we let Claude drive) |
| Firecrawl | Scrape ladder: plain fetch first, browser only when the page needs JavaScript or a login; HTML to clean Markdown; PDF extraction | The hosted fire-engine and the Redis/Postgres queue |
| Playwright | Selector and auto-wait semantics people are used to (wait for visible, then click) | The bundled browser downloads, which do not support Termux |
| ADB + Termux:API | Tap, swipe, type, screenshot, UI tree dump, app launch on any Android device; sensors and notifications on the phone itself | Nothing; these are the device driver |
| Chrome for Android | The same CDP socket Chrome exposes on Android, reached with `adb forward tcp:9222 localabstract:chrome_devtools_remote` | Nothing; this is how "in my browsers" covers the phone |

### 3.D Architecture (verbatim, with the 25 Oct Kotlin revision applied)

#### Architecture

The toolkit is one MCP server (originally proposed in Python; revised to Kotlin, see below), so the same code runs in Termux (no glibc, no Node-only browser binaries) and in a cloud container. Claude, or any MCP client, sees a flat list of functions; the server decides which driver handles each call.

<?claude block dia?>

Each driver is a plain Kotlin module with no MCP code in it, so the same functions can also be called from a shell (`claw search "..."`) or from a script. That shell entry point is what replaces `pplx` and Playwright scripts day to day.

##### The function surface (first cut)

| Function | Driver | Replaces |
| --- | --- | --- |
| `search(query, domains, recency, limit)` | Search | `pplx search web` |
| `snippets(query, urls, max_tokens)` | Search | `pplx content snippets` |
| `scrape(url, as=markdown/html/pdf)` | Scrape | Firecrawl scrape, Playwright page reads |
| `browser.open / goto / click / fill / press / wait_for` | Browser | Playwright actions |
| `browser.snapshot` (indexed elements), `screenshot`, `console`, `network` | Browser | chrome-devtools-mcp, Playwright tracing |
| `browser.eval(js)` | Browser | `page.evaluate` |
| `device.tap / swipe / type / key / screenshot / ui_tree / launch_app` | Device | your missing Android MCP |
| `device.notify / clipboard / battery / location` | Device (Termux:API) | Termux:API scripts |
| `infer(prompt, provider, model)` | Inference | separate provider CLIs |

Risky calls (typing into a logged-in page, `device.*` input, anything that sends or buys) go through an allow-list and a confirm step, the same idea as the fingerprint prompt in claude-code-android.

Diagram (an SVG widget in the doc): Claude Code or any MCP client -> claw MCP server (one function router, two modes: headless, in-session) -> five drivers: Search (Perplexity API + snippets) -> Perplexity Search API; Scrape (fetch, then CDP, to Markdown) -> any website (HTML, PDF); Browser (raw CDP, attach or launch) -> Chrome (desktop, Android); Device (ADB, Termux:API: tap, type, shot) -> your devices (phone, tablets); Inference (Claude, Gemini, GCP, local) -> providers (API, Vertex).

### 3.E Revision of 25 Oct: Kotlin core, inside the APK, the ADB debug loop (verbatim)

**Revised 25 Oct:** the core is a plain JVM Kotlin library, not Python, so it can live inside your AEthX-AEsc APK as well as run in a terminal. That matches how Æsc's own core is already built (`core/build.gradle.kts`: "Plain JVM Kotlin so the same code runs in the Android app and natively on Linux"). The MCP layer uses the official Kotlin MCP SDK (you already forked `kotlin-sdk`), so there is no JavaScript or Node anywhere. Claude, or any MCP client, sees a flat list of functions; the server decides which driver handles each call.

#### Inside your APK

The same driver code is reached four ways, so the on-device agent, Claude Code and your UI all get identical functions.

| Caller | Transport | Notes |
| --- | --- | --- |
| Æsc agent loop in the APK | Direct Kotlin call, or `AF_UNIX` socket between processes | claw functions register as `AgentTool` entries next to Æsc's existing ones (alarms, calendar, contacts, Wi-Fi) |
| Horizons-UI | WebSocket | Matches the transport table in `AEthX-AEsc/protocol/README.md`; auth for that socket is still open there |
| Claude Code, in Termux now or a shell later | MCP over stdio | `claw mcp` |
| Remote clients (cloud session, laptop) | MCP over HTTP on 127.0.0.1, reached through a tunnel | Off by default |

#### The ADB debug loop

The Device driver talks to the phone's own adbd over wireless debugging on 127.0.0.1, with no PC and no root. The app pairs once with the code from Settings, then connects to itself and gets a shell with UID 2000 (the "laptop trick" row in your protocol table). That one link gives:

- input, screenshots, UI tree dumps, app launch and install, logcat, file push and pull
- port forwards to Chrome's `localabstract:chrome_devtools_remote` socket, so the Browser driver can drive Chrome on the phone
- the debugging socket of the APK's own WebView, which becomes the headless browser inside the APK, since Termux's `chromium` package will not exist there

The ADB client is written in Kotlin with no `adb` binary. Kadb is a Kotlin library that already implements pairing (SPAKE2 and TLS); dadb is the simpler one from mobile.dev but I could not confirm it supports pairing. Wireless debugging must be on, and Android turns it off when Wi-Fi drops, so the driver detects that and asks you to re-enable it.

### 3.F Headless and in-session modes (verbatim)

#### Headless and in-session modes

Both modes use the same functions; only where the browser comes from changes. The hard part on Termux is that Playwright's own browser downloads fail on Linux arm64, so the toolkit never depends on them.

| Where it runs | Headless (its own browser) | In-session (your browser or device) |
| --- | --- | --- |
| Phone, Termux | Termux's own `chromium` package started with `--headless --remote-debugging-port`, or no browser at all for search and fetch-only scrapes | Chrome for Android over ADB: `adb forward tcp:9222 localabstract:chrome_devtools_remote`, ADB connected to the phone itself (claude-code-android's wireless self-connect). Device functions use the same ADB link. |
| Desktop or laptop | Any Chrome or Chromium started headless | Your normal Chrome started with `--remote-debugging-port=9222`; the server attaches with your logins, like browser-use and chrome-devtools-mcp `--browserUrl` |
| Cloud session (like this one) | Preinstalled Chromium, headless | Your phone or desktop through a tunnel you run (for example Tailscale); without one, cloud can only do headless |

Two cautions. An open debugging port lets any local program drive that browser, so the server binds to 127.0.0.1 only and in-session is opt-in per call. I have not yet tested the Termux `chromium` package or the Android Chrome socket on a real phone, so those two rows are the first thing to prove.

Added 25 Oct: Inside the APK, headless means the APK's own WebView driven over its debugging socket, and in-session means Chrome on the phone reached through the ADB debug loop. Termux is not needed for either.

### 3.G Inference routes (verbatim)

#### Inference: supported ways to use your accounts

Every provider has a supported way in, but subscription logins and API keys behave differently, and two of the routes you named are risky. The inference driver hands each call to one of these backends.

| Account | Supported route | Headless? | Status as of Oct 2026 |
| --- | --- | --- | --- |
| Claude Pro or Max | Claude Code (`claude -p`) or the Claude Agent SDK, signed in with your plan | Yes | Anthropic's help article (updated 7 Oct 2026) says the Agent SDK, `claude -p` and third-party apps can still use your subscription limits; Max and Team plans also get monthly API credits for these. The policy changed several times this year, so treat it as revocable. |
| Anthropic API key | Claude API directly | Yes | Always allowed; the safe choice for anything always-on |
| Gemini (Google AI Pro) | Antigravity CLI (`agy -p`) signed in with your Google account | Partly: sign-in needs a browser once; then the stored token is reused | Third-party guides report that Gemini CLI's Google sign-in stopped working for AI Pro on 18 Jun 2026 and moved to Antigravity. Google's docs only promise the API-key route for headless use, and whether a personal wrapper around an AI Pro login is allowed is unanswered. |
| Gemini API key | AI Studio key | Yes | Supported |
| GCP | Vertex AI with a service account or `gcloud` login | Yes | Supported; also serves Claude models on Vertex if you prefer one bill |

What I will not build: anything that drives the claude.ai or gemini.google.com chat pages through the browser to get answers out of a consumer plan. That breaks both providers' terms and can get the account banned; the subscription routes above are the supported way to spend those plans.

### 3.H Feature parity tab: the 145-item table (verbatim)

#### Feature parity

Every command, tool and skill in the five sources, mapped to claw. **v1** = in the first build, **v2** = the follow-up phase, **Dropped** = deliberately left out, with the reason. Nothing is built yet; this is the target. Counts come from each project's own help output or docs, read on 25 Oct 2026.

Totals: 145 items. 91 in v1, 37 in v2, 17 dropped. (Updated from 129/80/34/15 after the Android section was added.)

##### Perplexity CLI (`pplx`) and your LEJ Perplexity plugin

The `pplx` binary only covers search and snippets. Your LEJ plugin adds the Sonar answer models, so claw takes both.

| Today | claw | Status |
| --- | --- | --- |
| `pplx search web`, one or many queries | `claw search` | v1 |
| Flags: `-n/--limit`, `--country`, `--intent`, `--max-tokens`, `--max-tokens-per-page`, `--search-context-size` | same flags | v1 |
| Flags: `--domains`, `--excluded-domains`, `--recency-filter`, published-after/before, updated-after/before | same flags | v1 |
| `pplx content snippets` (1 to 50 URLs, token caps) | `claw snippets` | v1 |
| `pplx content fetch` | none | Dropped: deprecated by Perplexity; `claw scrape` replaces it |
| `--output-dir`, `PPLX_OUTPUT_DIR` (save JSON results) | `--output-dir`, `CLAW_OUTPUT_DIR` | v1 |
| `--stdout-preview` | same flag | v1 |
| `pplx auth login`, `PERPLEXITY_API_KEY` | `claw auth set perplexity`, same env var | v1 |
| `pplx update`, `update --check` | `claw update`, `claw update --check` | v1 |
| pplx-cli agent skill | claw skill (one skill for the whole toolkit) | v1 |
| LEJ: Sonar models `sonar`, `sonar-pro`, `sonar-reasoning-pro`, `sonar-deep-research` (ask, reason, research skills) | `claw ask --model ...` | v1 |
| LEJ: hook that blocks WebSearch and redirects to Perplexity | same hook, pointed at `claw search` | v1 |
| LEJ: enable-redirect, disable-redirect, setup, help commands | same four commands | v1 |
| LEJ: every search saved to Markdown | same, plus the JSON copy | v1 |

##### Playwright (library and runner)

Playwright is a library plus a test runner. claw replaces the browser-automation library over CDP; the test framework is the one part I recommend not rebuilding.

| Today | claw | Status |
| --- | --- | --- |
| `launch`, `connectOverCDP` | `browser.open` (headless) and `browser.attach` (in-session) | v1 |
| Browser contexts, isolated profiles, storage state save and load | `browser.context`, `browser.storage save/load` | v1 |
| Locators by role, text, label, CSS, with auto-wait | snapshot refs plus role, text and CSS queries; every action waits for visible and enabled | v1 |
| click, fill, type, press, hover, drag, select option, check | same actions | v1 |
| File upload, downloads, dialogs | `browser.upload`, download folder, `browser.dialog` | v1 |
| Screenshot (page, element, full page) | `browser.screenshot` | v1 |
| `page.pdf` | `browser.pdf` | v1 |
| `page.evaluate` | `browser.eval` (asks before running) | v1 |
| Cookies, localStorage, sessionStorage | `browser.cookies`, `browser.storage` | v1 |
| Emulation: viewport, user agent, color scheme, offline | `browser.emulate` | v1 |
| Emulation: geolocation, timezone, permissions, device presets | `browser.emulate` | v2 |
| Network routing, mocking, blocking | `browser.route` | v2 |
| Tracing and trace viewer | `browser.trace` (Chrome trace file) | v2 |
| Video recording | `browser.record` (screencast) | v2 |
| Codegen (record actions into a script) | `claw record` writes a replayable claw flow | v2 |
| `expect` assertions (visible, text, value) | `claw verify` | v2 |
| Test runner (workers, fixtures, reporters, retries, sharding) | none | Dropped: a full test framework is its own project; keep `@playwright/test` in CI if you have suites |
| Firefox and WebKit engines | none | Dropped: CDP is Chrome-only, and neither runs on Android |
| Android support (`_android`, experimental) | Device driver plus Chrome for Android over ADB | v1 |

##### Playwright MCP (72 tools)

| Today | claw | Status |
| --- | --- | --- |
| Core 24: navigate, back, click, type, fill_form, select_option, hover, drag, drop, press_key, file_upload, handle_dialog, snapshot, take_screenshot, find, wait_for, evaluate, run_code_unsafe, console_messages, network_request(s), resize, emulate_media, close | `browser.*` equivalents | v1 |
| Tabs | `browser.tabs` | v1 |
| Storage caps: 17 cookie, localStorage, sessionStorage, storage-state tools | `browser.cookies`, `browser.storage` | v1 |
| Vision caps: 6 mouse-by-coordinate tools | `browser.mouse` | v1 |
| PDF cap: pdf_save | `browser.pdf` | v1 |
| Config cap: get_config | `claw config` | v1 |
| Network caps: route, unroute, route_list, network_state_set | `browser.route`, `browser.emulate offline` | v2 |
| DevTools caps: tracing, recording, video, highlight, annotate (13 tools) | `browser.trace`, `browser.record`, `browser.highlight` | v2 |
| Testing caps: generate_locator, verify element, list, text, value | `claw verify`, `browser.locator` | v2 |

##### Chrome DevTools MCP

| Today | claw | Status |
| --- | --- | --- |
| Input (10): click, click_at, drag, fill, fill_form, handle_dialog, hover, press_key, type_text, upload_file | `browser.*` | v1 |
| Navigation (6): list_pages, new_page, select_page, close_page, navigate_page, wait_for | `browser.tabs`, `browser.goto`, `browser.wait_for` | v1 |
| Emulation (2): emulate, resize_page | `browser.emulate` | v1 |
| Network (2): list and get requests | `browser.network` | v1 |
| Debugging: evaluate_script, console list and get, take_screenshot, take_snapshot, get_css_styles | `browser.*` | v1 |
| Performance (3): start and stop trace, analyze insight | `browser.trace` plus insight summary | v2 |
| lighthouse_audit | `browser.audit`, runs Lighthouse where Node is installed | v2 |
| screencast start and stop | `browser.record` | v2 |
| Memory (14 heap-snapshot tools) | take, summary and compare in claw; deep analysis handed to chrome-devtools-mcp itself | v2 |
| Extensions (5): install, list, reload, trigger, uninstall | `browser.extensions` | v2 |
| Third-party and WebMCP page tools (4) | `browser.page_tools` | v2 |
| WebAuthn virtual authenticator | `browser.webauthn` | v2 |
| PWA install, launch, state, uninstall (4) | none | Dropped: desktop-only and rarely needed |

##### browser-use

| Today | claw | Status |
| --- | --- | --- |
| Actions: navigate, go_back, search, click (index or coordinate), input, send_keys, scroll, wait | `browser.*` | v1 |
| Actions: find_text, find_elements, search_page, dropdown_options, select_dropdown, upload_file, screenshot, save_as_pdf, evaluate, switch and close tab | `browser.*` | v1 |
| `extract` (LLM pulls structured data from the page) | `scrape --schema`, using the Inference driver | v1 |
| File tools: read_file, write_file, replace_file | none | Dropped: Claude already has file tools |
| `done` and the autonomous agent loop | `claw agent "task"` for headless runs on your own model accounts | v2 |
| DOM serializer with indexed interactive elements | `browser.snapshot` | v1 |
| Persistent CDP daemon, background tabs, focus emulation, tab reuse | the Browser driver core | v1 |
| Watchdogs: popups, downloads, about:blank, domain allow-list | same behaviours | v1 |
| Browser profiles and user data dirs | `browser.open --profile` | v1 |
| MCP server tools: navigate, click, type, state, extract, scroll, tabs, sessions, screenshot, HTML | covered by the rows above | v1 |
| Skills: browser-use, open-source | rewritten into the claw skill | v1 |
| Skill: qa | `claw qa` workflow skill | v2 |
| Skill: remote-browser | in-session over a tunnel | v2 |
| Skill: cloud (Browser Use Cloud) | none | Dropped: paid hosted browsers; claw runs your own |
| Skill: x402 (agent payments) | none | Dropped: spends money; out of scope for safety |

##### Firecrawl

| Today | claw | Status |
| --- | --- | --- |
| `scrape` formats: markdown, html, rawHtml, links, screenshot, images, attributes | `claw scrape --format ...` | v1 |
| `scrape` formats: json (schema extraction), summary, query | `claw scrape --schema / --summary / --ask`, via the Inference driver | v1 |
| `scrape` formats: changeTracking, branding | `claw monitor`, `claw scrape --format branding` | v2 |
| `scrape` format: audio | `claw scrape --format audio`, using your local Whisper setup | v2 |
| Page actions: wait, click, write, press, scroll, screenshot, scrape, executeJavascript, pdf | `claw scrape --actions` (runs on the Browser driver) | v1 |
| `map` (list a site's URLs) | `claw map` | v1 |
| `crawl` with limits, include and exclude paths | `claw crawl` | v1 |
| `crawl --cancel`, status by job ID, resumable jobs | `claw jobs` | v2 |
| `batch-scrape` | `claw scrape` with many URLs | v1 |
| `search` (and scrape the results) | `claw search --scrape` | v1 |
| `extract` | `claw scrape --schema` across URLs | v1 |
| `agent` | `claw agent` | v2 |
| `interact` (live browser on a scraped page) | `claw scrape --keep-open`, then `browser.*` | v1 |
| `monitor` create, list, run, checks, check, update, delete | `claw monitor`, scheduled with termux-job-scheduler or cron | v2 |
| `parse` uploads: PDF | `claw parse` | v1 |
| `parse` uploads: Word and other office files | `claw parse` | v2 |
| `experimental download` (save a site locally) | `claw mirror` | v2 |
| `config`, `view-config`, `login`, `logout`, `init`, `setup` | `claw setup`, `claw config`, `claw auth` | v1 |
| `developer`, `gov`, `research` (paper and GitHub search) | none | Dropped: Firecrawl's own hosted indexes; `claw search --domains` plus your research-desk plugin cover them |
| `credit-usage`, `feedback`, `alexandria`, `--status` credits | none | Dropped: hosted-service billing and feedback |
| fire-engine (anti-bot scraping) | none | Dropped: closed source; in-session mode uses your real, logged-in browser for protected pages |
| CLI skills (search, scrape, interact, map, crawl, agent) | claw skill | v1 |
| Workflow skills: research brief, SEO audit, QA report, lead list, knowledge base, design-system extraction | claw workflow skills, research brief and QA report first | v2 |
| Build skills (Firecrawl SDK in your apps) | none | Dropped: for building apps on Firecrawl's SDK, not for using a toolkit |

##### Android device control (existing Android MCPs and Æsc)

You have no Android MCP yet, so the target is the union of the strongest open-source ones ([scrcpy-mcp](https://github.com/juancf/scrcpy-mcp), [android-mcp-server](https://github.com/chldu2000/android-mcp-server), droidrun/mobilerun) plus the tools Æsc already has. Everything runs over the ADB debug loop unless noted.

| Today | claw | Status |
| --- | --- | --- |
| Screenshot | `device.screenshot` | v1 |
| Tap, long press, swipe, drag | `device.tap`, `device.swipe` | v1 |
| Type text, key events | `device.type`, `device.key` | v1 |
| UI tree dump (uiautomator) | `device.ui_tree` | v1 |
| Launch, stop, list apps | `device.app` | v1 |
| Install, uninstall APK | `device.install` | v1 |
| Shell command as UID 2000 | `device.shell` (asks before running) | v1 |
| File push and pull | `device.files` | v1 |
| Logcat | `device.logcat` | v1 |
| Clipboard | `device.clipboard` | v1 |
| Æsc PlatformTools: alarms, timers, calendar, contacts, Wi-Fi, Bluetooth, volume, brightness, Do Not Disturb, flashlight | registered into claw from Æsc as they are | v1 |
| Screen recording and live video (scrcpy) | `device.record` | v2 |
| Audio capture (scrcpy) | `device.audio` | v2 |
| Accessibility-service control with ADB off (droidrun Portal, MCP box) | `device.*` fallback driver | v2 |
| iOS control (mobile-mcp, mobilerun) | none | Dropped: you named no iOS device |
| Cloud phones (mobilerun cloud) | none | Dropped: paid hosted devices |

##### Keeping it sustainable

The parity list ships in the repo as a manifest, with one test per function, so a missing feature fails a test instead of going unnoticed. A monthly check compares the manifest against new releases of `pplx`, Playwright MCP, chrome-devtools-mcp, browser-use and Firecrawl, and lists anything new for you to accept or drop.

### 3.I Assets to gather before the build (verbatim)

#### Assets to gather before the build

Most of this I can fetch myself; the keys and the phone settings have to come from you.

| Asset | Why | Who |
| --- | --- | --- |
| Perplexity API key | Search, snippets and the Sonar answer models | You get it |
| Anthropic API key, or keep using your Claude plan through Claude Code | `infer` and `claw agent` | You get it (plan route needs nothing new) |
| Gemini API key from AI Studio | Gemini without the Antigravity login question | You get it |
| GCP project with Vertex AI enabled and a service-account key | Vertex inference, one bill for Gemini and Claude | Optional |
| Firecrawl API key | Not needed: claw does its own scraping | Optional, only for side-by-side tests |
| Wireless debugging on, and the app paired once with the code from Settings | The ADB debug loop | You do it on the phone |
| Chrome on the phone with "USB debugging" left on in Developer options | The DevTools socket that the loop forwards | You do it on the phone |
| Termux:API app (for the Termux period only) | Sensors and notifications until Æsc handles them | You have it already |
| [Kadb](https://klibs.io/project/flyfishxu/Kadb) and [dadb](https://www.maestro.dev/blog/our-first-open-source-project) | Kotlin ADB client, pairing | I fetch it |
| [libadb-android](https://github.com/MuntashirAkon/libadb-android/) | Second reference for in-app pairing | I fetch it |
| [LADB](https://github.com/tytydraco/LADB) | Proven self-connect flow on one phone | I fetch it |
| Your [kotlin-sdk](https://github.com/c10vis-poem/kotlin-sdk) fork | MCP server in Kotlin, no JavaScript | I fetch it |
| [scrcpy-mcp](https://github.com/juancf/scrcpy-mcp) (44 tools) and [chldu2000/android-mcp-server](https://github.com/chldu2000/android-mcp-server) | Android MCP tool lists to match | I fetch them |
| Your NvAEX_mobilerun fork (droidrun Portal) and [MCP box](https://github.com/inckie/MCP-box) | Accessibility-service control when ADB is off | I fetch them |
| Horizons-UI ADB, wireless-adb and Chromium code (the salvage targets in AEthX-AEsc) | Your existing loop and browser work | I fetch them, you confirm which is current |
| Goodbye-Termux-ADB, termux-app fork (`aethx.aesc`) | Packaging inside the APK | I fetch them |

### 3.J Open questions: current version (verbatim, replaced the first list)

1. **The ADB debug loop.** I read it as the app pairing with its own adbd over wireless debugging on 127.0.0.1, then a shell with UID 2000, with no PC and no root. Is that right, and do you also want a Shizuku or root path?
2. **Your APK.** Is AEthX-AEsc (the termux-app fork renamed `aethx.aesc`, plus the Æsc core) the app this goes into? Which Horizons-UI ADB and Chromium code is current?
3. **Kotlin core.** Do you agree with Kotlin for the core, so the APK and the terminal share one codebase?
4. **Which Playwright-based tools?** Name them, or the jobs they do, so nothing they do is missed.
5. **Which devices and browsers?** Only this phone, or other Android devices and a desktop Chrome too?
6. **Inference defaults.** Which provider should `infer` use by default, and is a Gemini API key acceptable instead of the AI Pro login?
7. **Repo.** A new repo (for example `c10vis-poem/claw`), or a module inside AEthX-AEsc?

Closing line of that section: Once you answer and say "build it", I start with Search and Scrape (they replace `pplx` with no device risk), then Browser, then Device.

### 3.K Open questions: first version (superseded, kept for the record)

#### Questions only you can answer

1. **Your Android MCP.** I found no Android MCP in your GitHub. Is it local on the phone, under another account, or should the Device driver be built new from ADB and Termux:API?
2. **Which Playwright-based tools?** You mentioned "a couple of tools grafted off of Playwright". Name them, or tell me the jobs they do (for example form filling, scraping behind a login, page testing), so the function list covers them.
3. **Which devices and browsers?** Only this phone, or other Android devices and a desktop Chrome too?
4. **Where it runs most.** On the phone in Termux, in cloud sessions like this one, or both? This decides whether in-session needs a tunnel.
5. **Inference defaults.** Which provider should `infer` use by default, and is a Gemini API key acceptable instead of the AI Pro login?
6. **Repo.** A new repo (for example `c10vis-poem/claw`), or inside an existing one?

Once you answer and say "build it", I start with Search and Scrape (they replace `pplx` with no device risk), then Browser, then Device.

### 3.L Sources (verbatim)

#### Sources

- [Using the Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540) (Anthropic Help Center, update of 7 Oct 2026)
- [Antigravity CLI installation and auth](https://antigravity.google/docs/cli/install) (Google)
- [Gemini CLI free tier shut down](https://dev.to/owen_fox/gemini-cli-free-tier-shut-down-6-fixes-that-work-2026-26hc) (third-party, unverified against Google)
- [Forum question on wrapping Antigravity CLI headless mode](https://discuss.ai.google.dev/t/question-about-personal-wrapper-around-official-antigravity-cli-headless-mode/178472)
- [chrome-devtools-mcp troubleshooting](https://tessl.io/registry/skills/github/ChromeDevTools/chrome-devtools-mcp/troubleshooting) and [listing](https://glama.ai/mcp/servers/gr729wexir)
- [Playwright connectOverCDP](https://playwright.dev/java/docs/api/class-browsertype)
- [Chrome remote debugging](https://www.browserless.io/blog/chrome-remote-debugging)
- [Playwright arm64 Linux install failure](https://github.com/microsoft/playwright-mcp/issues/1515)
- Your repos, read directly: Novus-perplexity-cli README, Novus-firecrawl `apps/api/src/scraper/scrapeURL/engines`, NovA-browser-use, [claude-code-android](https://github.com/c10vis-poem/claude-code-android)
---

## 4. The six dynamic-workflow patterns (Q&A)

**Goal.** Answer whether Anthropic has exactly six dynamic workflows.

**Final state.** Answered and posted in the thread at 20:50 UTC. There are no repos, PRs or files. Answer, verbatim:

> No, Anthropic names exactly six, and it doesn't present them as a fixed list. They come from the Claude Code team's post [A harness for every task: dynamic workflows in Claude Code](https://claude.dev/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code/):
>
> 1. **Classify-and-act**: one agent works out what kind of task it is and sends it to the right agents.
> 2. **Fan-out-and-synthesize**: the job is split across many agents, then their results are merged.
> 3. **Adversarial verification**: a separate agent checks each agent's output against criteria.
> 4. **Generate-and-filter**: agents produce many ideas, then the weak ones and duplicates are dropped.
> 5. **Tournament**: several agents try the same task in different ways, and judges compare them until one wins.
> 6. **Loop until done**: Claude keeps starting agents until something tells it to stop, such as no new findings.
>
> The post calls them "a few common patterns" that Claude "might use and compose together." So they're building blocks, not a complete set. Claude writes a custom setup for each task and can mix them. You can also ask it for a specific pattern in your prompt.
>
> The [launch post](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) doesn't list the patterns. It only gives example uses, such as bug hunts, migrations, and work you want checked twice.

That post is by Thariq Shihipar and Sid Bidasaria (Anthropic, Claude Code team). The launch post also mentions the `ultracode` setting, which lets Claude decide when to use a workflow.

**Pending or next steps.** None.

---

## 5. The old /plugin-authoring thread (status line mod)

**Goal.** You asked "What's the status line entry?". That was a question.

**What happened.**
1. A coordinator relay read your question as a request to build. The session built an unrequested `session-status` status-line mod in `/root/.claude/dev-mods/38c10bb5-b74b-517c-9e26-2d1db3e2b305/session-status/` (`hooks/register.ts`, `hooks/hooks.json`, `.claude-plugin/plugin.json`). The status line read like `42 tools · 2 failed · 1 blocked · last: Edit`. `claude plugin validate` passed.
2. You declined loading it. At 20:27 you wrote: "First of all, don't ever build mods without me asking you to. And second of all, put those original responses back and stop taking the replies out of this side thread."
3. The session deleted the mod with `rm -rf` on that folder, which is now empty, and saved `feedback-mods-only-on-request.md`.

**Final state.** No mod exists. No repos, PRs or branches. **Every reply in this thread after the session resumed failed to post** ("No such tool available: mcp__hearthbot__post_message").

**The replies that never posted (verbatim, final version, 20:28):**

> You're right, and I'm sorry. I shouldn't have built that mod without you asking. You asked what a status line entry was, and I treated that as a go-ahead when it wasn't. I've deleted the mod completely. The mods folder is empty, so nothing will load the next time the session starts. I've also saved a note so this doesn't happen again: no mods unless you explicitly ask for one.
>
> About the replies: I didn't take anything out of the thread. My last several answers never reached it. Every time I try to post there, the tool fails with "not available," including just now with this answer. They never made it in, so there's nothing in the thread for me to restore. ...
>
> Here's what those lost answers said:
> - When you first asked about status, nothing had been built yet.
> - A status line entry is one short line of text in the bar below the prompt, which a mod can update as you work, for example `wiki: 142 pages · 3 lint issues`.
>
> I won't do anything more until you tell me what you want.

An earlier unposted reply, from 20:26, announced the build and its file paths. That build was later deleted.

**Pending or next steps.** None, unless you want a status line built. If you do, ask for it explicitly.

---

## 6. Other items from the shared memory (`/tmp/claude/memory/team/silo/`)

- **Cadence habit tracker** (2026-10-24, `habit-tracker-cadence-build.md`). Built through PGE and **done**: all 4 sprints passed. It is a Vite/React/TS app with local IndexedDB storage. The code is at `/home/user/habit-tracker` (local git, no remote). The durable copy is `/mnt/project-files/habit-tracker/cadence.bundle`; restore it with `git clone cadence.bundle cadence`. To run it, use `npm install && npm run dev` (port 5173). **Open decision:** reminders due during quiet hours are skipped, not deferred. Optional fixes:
  - The Calendar control is `<a role="button">`.
  - Completed days with a note need a visible "Uncheck".
  - After a keyboard-opened dialog, focus goes to `main` instead of the h1.

  You may never have received the completion summary.
- **Environment** (`user-environment.md`). Claude Code v2.1.310 runs in Termux on Android, with about 106 synced plugins (list in `/mnt/project-files/plugins/synced-plugins.md`). A local plugin with `hooks/enforce_quota.py` (`TOKEN_QUOTA_DAILY`) blocks prompts. To fix it, grep for it in `~/.claude/plugins`, then run `claude plugin disable <name>@<marketplace>`. Give only verified, sourced commands. "Turlock skill" meant termux-helper.
- **The APK.** You are building an APK to replace Termux, with an on-device agent. Toolkits must be embeddable in it and work outside Termux (ADB, Unix sockets, WebSockets).

---

## 7. Standing user rules

1. **No mods unless you ask.** Never build a mod or plugin, or tell a thread to build one, unless you explicitly ask for that specific build. A question ("what is X?") is not a request. A coordinator relay saying "get going" is not your go-ahead.
2. **Replies stay in their thread.** A question asked in a thread is answered in that thread, never moved to project chat. The coordinator never answers or relays thread questions in project chat; at most it nudges a silent thread.
3. **Use Opus, not Fable**, for new threads (cost), unless you say otherwise.
4. **PRs auto-merge once CI passes.** After opening a PR, mark it ready and run `gh pr merge --auto --squash` instead of leaving drafts. Where repo auto-merge is off (NvAEx-Recaps), squash-merge by hand once every check on the head commit is green. Never merge on red CI. In this environment the auto-mode classifier may block the merge; if it does, ask you to approve it.

Also from memory: give verified, sourced commands only. Don't scrape the claude.ai or gemini web apps for inference.

---

## 8. Paste this to resume

```
I'm continuing the 2026-10-25 work. Read /mnt/project-files/MIGRATION-HANDOFF-2026-10-25.md first and follow its standing rules: no mods unless I ask, replies stay in their thread, use Opus not Fable, PRs auto-merge once CI passes (never on red).
Open items, in order:
1) Vault GitHub App: the 6 draft PRs (NovAExorpus#59, NovAExopia#14, Hyperion-XI#10, CloviX-AEyre#11, AEthX-AEsc#15, NovusAExenti#10) need ready + squash auto-merge; then I run `bash tools/vault-app/setup.sh --drop-pat`. Check their state first.
2) NvAEx-Recaps: plugins-panel (#6) is merged. The recaps/configs/secrets split and the 3-stage control panel + agent-setup top bar are proposed only. Wait for my answers before building.
3) claw toolkit: the proposal is at https://claude.ai/artifact/2a9BgPvtCLSFSTrevUM6oT (section 3 of the handoff has it verbatim). Nothing is built; wait for my answers to its 7 questions and an explicit "build it".
Start by telling me the current state of item 1, in one short message.
```
