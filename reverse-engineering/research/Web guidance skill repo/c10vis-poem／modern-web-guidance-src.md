# c10vis-poem／modern-web-guidance-src

Watch
0
Apache License 2.0
goo.gle/modern-web-guidance
Code of conduct
Contributing
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from GoogleChrome/modern-web-guidance-src
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with GoogleChrome/modern-web-guidance-src:main .
Contribute
Sync fork
micahjo7 feat(evals): Phase 2 - base-app target generation and calibration ref…
7b9d071 · 8 hours ago
.agents/skills
feat(evals): Phase 2 - base-app target gener…
8 hours ago
.github
build(deps): bump actions/checkout from 6 …
2 days ago
bin
feat(evals): Phase 2 - base-app target gener…
8 hours ago
eval-view
fix: improve eval harness PATH interception,…
3 weeks ago
features
Dedupe popover fallback guidance (Google…
2 weeks ago
guides
feat(evals): Phase 2 - base-app target gener…
8 hours ago
harness
feat(evals): Phase 2 - base-app target gener…
8 hours ago
lib
feat(evals): Phase 2 - base-app target gener…
8 hours ago
nightly
nightly eval investigation skill (GoogleChrom…
last month
scripts
infra: add document-coherence-audit skill (G…
2 weeks ago
serving
Docs: Add Grok Build CLI install option (Goo…
2 days ago
skills-src
chrome-extensions skill: add userScripts AP…
last month
.env.example
feat(evals): Phase 2 - base-app target gener…
8 hours ago
.gitattributes
Content ATL config and scripts (GoogleChro…
2 weeks ago
.gitignore
nightly eval investigation skill (GoogleChrom…
last month
.oxlintignore
Source and integrate devtools-times base a…
3 months ago
.oxlintrc.json
oxlint: ignore unused catch variables (Googl…
4 months ago
CODEOWNERS
Content ATL config and scripts (GoogleChro…
2 weeks ago
CODE_OF_CONDUCT.md
mwg readme: big refactor for readability (Go…
2 months ago
CONTEXT.md
Content ATL docs (GoogleChrome#997)
2 weeks ago
CONTRIBUTING.md
Content ATL docs (GoogleChrome#997)
2 weeks ago
EVALS.md
feat(evals): Phase 2 - base-app target gener…
8 hours ago
c10vis-poem
modern-web-guidance-src
Code
Pull requests
Agents
Actions
Projects
Security and quality
Insights
Settings
Fork
0
m
T


LICENSE
license: add apache 2.0 license (GoogleChr…
2 months ago
README.md
Docs: Add Grok Build CLI install option (Goo…
2 days ago
config.ts.example
Support for multiple tasks per guide (Google…
3 months ago
constants.ts
Adds Skills + CLI approach (GoogleChrome…
4 months ago
package.json
feat(evals): Phase 2 - base-app target gener…
8 hours ago
pnpm-lock.yaml
feat(evals): Phase 2 - base-app target gener…
8 hours ago
pnpm-workspace.yaml
Add gradergen impl, infra to run agent & gra…
5 months ago
tsconfig.json
feat(evals): Phase 2 - base-app target gener…
8 hours ago
This repo is the source repository for GoogleChrome/modern-web-guidance and includes the code and documentation for authoring,
calibrating, and evaluating its contents.
Modern Web Guidance is a set of skills that embed web platform expertise, best practices, and browser compatibility data directly into your
coding agents. It helps to steer your coding agents away from legacy patterns, and instead toward solutions that harness the power and
capabilities of the modern web platform.
Note
This is a preview release of Modern Web Guidance. We're actively adding new content and we welcome contributions or feedback on
GitHub.
See CONTRIBUTING.md for how we work on the project and orientation of the codebase. We're open to contributions to guidance, eval cases,
eval infra and more. :)
Supported by the Google Chrome team, the Microsoft Edge team, and the web development community.
This command runs an interactive wizard to install Modern Web Guidance. See Alternative Installation Methods below.
Coding agents often default to older patterns because LLM training data contains vast amounts of legacy code. This often leads them to
generate bloated JavaScript for tasks that now have native, high-performance web platform solutions.
Even if a model knows an API exists, it often lacks the density of real-world, modern implementation patterns required for production-ready
code.
 Modern Web Guidance (Source)
 Quickstart
npx modern-web-guidance@latest install
Try it out (without installing)
# Search for relevant guides
npx modern-web-guidance@latest search "animate a dialog modal backdrop"
# Retrieve a guide by ID
npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"
 Why?
README
Code of conduct
Contributing
License


Modern Web Guidance bridges this gap. Our skill's CLI returns targeted, expert-curated guidelines directly into your agent's context window,
focusing on:
Modern Browser APIs: Helping models correctly structure APIs they frequently misuse.
Performance & Accessibility: Preferring platform-level APIs that can be optimized by the browser and include built-in accessibility
affordances.
Responsible Fallbacks: Guiding models to use sensible, lightweight fallbacks instead of heavy polyfills or legacy libraries.
We cover the past several years of the web platform's new features, all the way up to the cutting edge. The guides are designed to be token-
efficient; we run evals enabling us to prune lowest-common-denominator content that models already know.
Smooth visual states (View Transitions,
entry/exit animations, parallax scroll, CSS
scrollbar-color ).
Modern layout systems (container queries,
subgrid , modern color spaces like
oklch , text-wrap tuning, and line-height
trimming).
Speed optimizations (instant preloading,
Interaction to Next Paint (INP) diagnostics,
and scheduling tasks via
scheduler.yield ).
Native components (Anchor Positioning for
tooltips, Popover API, dialogs, :user-
invalid validation, and auto-sizing fields).
Important considerations (screen reader
and keyboard operability, content
navigation and discoverability).
Local client models (native translation,
summarization, and language detection
APIs).
View an example: the navigation-drawer guide.
103 modern web features
130 real-world developer use cases
Progressive Enhancement & Nuanced Fallbacks: We distinguish between purely additive enhancements (like speculative preloading)
which are safe to let older browsers silently ignore, and critical behaviors (like dialog controls or network beacons) where we write highly
considered, low-overhead fallbacks.
Responsible Fallbacks: We prioritize lightweight, case-specific custom fallbacks (<50 LOC) or conditionally-loaded polyfills instead of
heavy third-party bundles.
Gotchas & Quirks: We document hidden platform limitations, such as the 64KB payload quota for fetchLater() or macOS-specific
scrollbar behaviors.
Baseline-Aware Integration: We leverage real-time compatibility data from the Baseline project so agents can dynamically adapt to curren
browser support and any browser support preferences.
1. Activation: The coding agent activates the modern-web-guidance skill because of a relevant task. The agent is instructed to use the
modern-web-guidance CLI for web platform queries.
2. Local Semantic Search: The agent runs modern-web-guidance search "<query>" . The tool matches the query to the best guide using an
offline, CPU-efficient TensorFlow.js model (no network calls, no API keys).
3. Guide Fetch: The agent retrieves the guide via modern-web-guidance retrieve <guide-id> , inserting targeted code patterns, gotchas,
and fallbacks directly into its context window.
Tip
 What's Included?
Core Disciplines
🎨 User Experience
📐 CSS Layout
⚡ Performance
📝 Forms & UI
♿ Accessibility
🤖 Built-in AI
The full list
Safe Adoption of Modern Features
 How It Works


Note: We use npx to ensure the content doesn't go stale, but the CLI works offline, completely private and local. The npm package is self-
contained, with no extra dependencies to ensure both low-latency and supply-chain security.
Vercel Skills CLI (aka npx skills )
GitHub CLI
Google Antigravity
GitHub Copilot CLI
Claude Code Plugin
Grok Build CLI
If you installed the skill using npx modern-web-guidance@latest install , you can update with: npx modern-web-guidance@latest update .
Otherwise, consult your agent's documentation for updating plugins and skills.
We developed a robust eval harness to ensure that the content is empirically proven and continuously calibrated to ensure AI agents write
better code. We run automated evaluations using a closed-loop validation pipeline:
0. Simulated Developer Tasks: We define realistic, developer prompts that mimic real-world requests (e.g., "make my images load faster").
The prompts avoid naming APIs or features, testing whether the agent can successfully discover the relevant guides naturally.
1. Browser-based Assertions: We write browser automation scripts that verify the guide was followed correctly: exact runtime behaviors,
computed styles, accessibility states, etc.
2. Self-Healing Calibration: Graders are calibrated against both a reference implementation (100% pass target) and a control page (0% pass
target). The agent automatically refines tests on failure.
3. E2E Testing: We measure coding agent performance on real tasks with and without guidance. The opportunity (100% - unguided pass rate
and uplift (guided - unguided pass rate) are key. If there's little opportunity, then models already do a great job and our guidance isn't
providing much value. Based on the results, we revise guides to maximize the uplift, optimizing their effectiveness.
Date
Agent + Model
Tasks / Assertions
Unguided → Guided (Uplift)
Jul 6
codex_cli (gpt-5.5)
129 / 1071
57% → 84% (+27pp)
Jul 6
claude_code (sonnet-5)
129 / 1071
52% → 87% (+35pp)
Jul 6
antigravity
129 / 1071
54% → 87% (+33pp)
Jul 3
codex_cli (gpt-5.5)
129 / 1071
52% → 78% (+26pp)
Jul 3
claude_code (sonnet-5)
129 / 1071
48% → 82% (+34pp)
 Alternative Installation Methods
 Updating
 Evals to prove this works well ;)
  [ Expert-authored guidance and demo ]
            │
            ▼
  [ Generated assets ] ──> Playwright Grader (.spec.ts) & Negative Demo (.html)
            │
            ▼
  [ Calibration loop ] ───────> Runs Grader on Gold-Standard Demo (Must Pass 100%)
            │                   Runs Grader on Negative Demo (Must Fail 100%)
            ▼
  [ E2E agent evals ] ────────> Runs coding agents in guided vs. unguided modes
                                Compares accuracy w/ and w/o the skill
Recent eval results snapshot


Date
Agent + Model
Tasks / Assertions
Unguided → Guided (Uplift)
Jul 1
claude_code (sonnet-5)
129 / 1071
49% → 84% (+35pp)
Jul 1
antigravity
129 / 1071
53% → 83% (+30pp)
Jun 29
codex_cli (gpt-5.5)
129 / 1071
51% → 78% (+27pp)
Jun 29
claude_code (opus-4-8)
129 / 1071
53% → 88% (+35pp)
Jun 29
antigravity
129 / 1071
50% → 78% (+28pp)
You can customize which skill packs are installed using the --choose flag:
modern-web-guidance (~234 tokens): Comprehensive guidance on modern browser APIs, layouts, and performance.
chrome-extensions (~181 tokens): Guidance on Manifest V3, background workers, extension APIs, and Chrome Web Store publishing.
Google collects anonymous usage statistics (such as search queries, guide retrievals, and installation) to improve the reliability, relevance, and
performance of the tool. You can inspect what is collected in modern-web.ts.
Tip
To Opt-Out: set the DISABLE_TELEMETRY=1 env variable in your shell profile (e.g., .bashrc or .zshrc ):
Google handles this data in accordance with the Google Privacy Policy.
If you'd like to contribute to modern-web-guidance, please see the source repo's CONTRIBUTING.md . The modern-web-guidance repo is purely
a publish target for clean skills installation.
Huge thanks to everyone who has contributed!
Unless otherwise noted:
Software code in this repository is licensed under the Apache License 2.0.
Documentation and guide content under guides/ are licensed under Creative Commons Attribution 4.0 International (CC-BY 4.0).
 Available Skill Packs
npx modern-web-guidance@latest install --choose
 Telemetry & Privacy
export DISABLE_TELEMETRY=1
 Contributors
 License


Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
TypeScript 62.4%
JavaScript 22.6%
HTML 6%
CSS 4.1%
Astro 3.2%
Shell 1.4%
Other 0.3%
Suggested workflows
Based on your tech stack
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
By Open Source Security Foundation (OpenSSF)
Configure
Datadog Synthetics
Run Datadog Synthetic tests within your GitHub Actions workflow
By Datadog
Configure
Deno
Test your Deno project
By GitHub Actions
Configure
More workflows
