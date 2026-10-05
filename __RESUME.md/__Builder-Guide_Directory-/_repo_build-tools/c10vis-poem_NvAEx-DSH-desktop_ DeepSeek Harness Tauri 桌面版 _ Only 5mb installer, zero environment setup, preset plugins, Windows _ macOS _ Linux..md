<!-- Converted from c10vis-poem_NvAEx-DSH-desktop_ DeepSeek Harness Tauri 桌面版 _ Only 5mb installer, zero environment setup, preset plugins, Windows _ macOS _ Linux..pdf — 6 pages -->

## Page 1

NvAEx-DSH-desktop
Code Pull requests Agents Actions Projects Wiki Security and quality Insights Settings
Watch 0 Fork 0
## DeepSeek Harness Tauri
## | Only 5mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.
MIT License
dshtauri.mintlify.site
0 stars 0 forks 0 watching 1 branch 0 tags Activity
Public repository · Forked from dsh-tauri/deepseek-harness-desktop
m… 1 Branch 0 Tags Go to file T Go to file Add file Code
This branch is up to date with dsh-tauri/deepseek-harness-desktop:main . Contribute Sync fork
hairyf fix(plugins): ， rc (dsh-tauri#778) 72ac3b3 · 7 minutes ago
.github ci(release): Release Relea… 3 days ago
assets feat(macos): fixed the issue of dock icon be… last month
docs chore(kernel): dsh-v0.2.0-rc.… yesterday
packages fix(pet): rewind
| patches fix(pet): | IndexedDB |
|---|---|
|  | … |
public feat(assets, docs): add mobile remote soluti… last month
scripts fix(adapter): … 2 hours ago
skills/handle docs(skill): handle dev/release … last week
source chore(kernel): dsh-v0.2.0-rc.… yesterday
src-tauri fix(plugins): ， … 7 minutes ago
src fix(core): … 1 hour ago
test fix(adapter): … 2 hours ago
types docs: drop dsh-tauri-panel references and st… 2 weeks ago
.editorconfig feat: one-click install desktop app for DeepS… last month
.env.example fix(plugin): repair broken preset plugin instal… last month
.gitattributes fix(linux): AppImage
.gitignore Merge branch 'main' into feat/ssh-remote-m… 3 days ago
.gitmodules feat: zcode
AGENTS.md fix(docs): … last week
LICENSE fix(license): make license identifiable by Git… last month
LICENSE.details chore: update change readme last month
README.en.md chore(macos): macOS … 5 hours ago
chore(macos): macOS … 5 hours ago

---

## Page 2

README.es.md
README.md chore(macos): macOS … 5 hours ago
THIRD_PARTY_NOTICES.md chore(kernel): dsh-v0.2.0-rc.… yesterday
bump.config.ts chore(lint): add ESLint with antfu config and… last month
eslint.config.mjs fix(adapter): … 2 hours ago
genapi.config.ts feat(model): dsh-tauri-model
genapi.pipeline.ts feat(tooling): drive genapi from route metad… 2 weeks ago
index.html chore: display app name as Deepseek Harne… last month
package.json chore: release v0.19.0 18 hours ago
pet.html Revert "Merge pull request dsh-tauri#355 fro… last month
pnpm-lock.yaml chore(kernel): dsh-v0.2.0-rc.… yesterday
pnpm-workspace.yaml chore(kernel): dsh-v0.2.0-rc.… yesterday
postcss.config.js chore(lint): add ESLint with antfu config and… last month
skills-lock.json docs(testing): Spec 4 … last week
tailwind.config.js feat(shell): dsh alias token 19 hours ago
tailwind.plugins.config.js refactor(ui): Tailwind CSS dsh-tau… yesterday
tsconfig.json refactor(ssh): dsh-tauri-ssh-ui dsh-ta… yesterday
tsconfig.node.json fix(ci): typecheck plugin build script with its … last week
| vite.config.ts feat(remote): | reause |
|---|---|
|  | （ n … |
vitest.config.ts test(unit): ——
vitest.desktop.config.ts test(e2e): global-setup setup-plugin，… last week
vitest.plugin.config.ts test(e2e): global-setup setup-plugin，… last week
vitest.unit.config.ts refactor(ssh): dsh-tauri-ssh-ui dsh-ta… yesterday
README License
### DeepSeek Harness
DeepSeek Harness ——
Node.js pnpm Docker，
release v 0 . 1 9 . 0 downloads 8 7 k stars 2 . 8 k license MIT Windows | macOS | Linux dsh 0.2.0-rc.1
English · Español · ·
6 #6 Repository Of The Day

---

## Page 3

🧩 — ， / ，
🎁 — ，
🪶 — Tauri 2 （ Electron）：
⌨ — dsh ，
🧭  
  —  
，
🚀  
  —
，
；
🐾     —   Pets / Codex   ，
， ：
DSH Market — （ ）
DSH Better Sidebar — VSCode ， （ ）
DSH Rewind — ， ； ， （ ）
DSH Bridge — Cloudflare ， / QQ / / Telegram ， Harness； （ ）
DSH-IM — QQ Slack Telegram Discord WhatsApp iMessage Harness， IM （ ）
（ ）
， ， deepseek-harness-desktop/issues
：
）
DSH Tauri UI — Tauri 2
DSH Tauri Worktree — Git Worktree，
DSH Tauri Extension — Skills/MCP ，
DSH Tauri Scheduler — ； Agent ，

---

## Page 4

# DSH Tauri Archive —
# ，
# DSH Tauri Pet —
# Chat / Codex
# DSH Tauri Rightclick —
# DSH Tauri Model —
# ...
# Releases
# ，
# macOS（Homebrew）：
# Homebrew
# ：
brew install dsh-tauri/desktop/deepseek-harness
dsh
Node Harness （ ， ）， http://127.0.0.1:3080 Harness
，
# ： Windows 10+ · macOS 12+（Safari 17.4+）· Linux（AppImage / .deb）·
# · Harness
# 0.1.5-rc.1
Deepseek.Harness.Desktop_Bundle_< >.< （Windows / macOS / Linux）： Releases > ：Node
# Harness
# ，
# ，
# /
# （
# ；git
# Git） Linux
.deb /usr/lib ，root
# Linux Wayland
# （PikaOS / GNOME Wayland / Ubuntu 22.04+）： AppImage Wayland
# WebKitGTK
# /
# ，
# /
# ：
Linux （Arch / CachyOS / Fedora ）： AppImage （Ubuntu 22.04） libwayland-client WebKitWebProcess
， Mesa ABI  abort() ——
（ .github/workflows/build-linux.yml scripts/fix-appimage-host-libs.sh ）， .deb ； ， LD_PRELOAD=/usr/lib/libwayland-client.so.0 ./AppImage （
# ）
# Discord

---

## Page 5

## QQ
## (
## ,
## ) ->
## ？
## docs/DEVELOPMENT.zh.md
┌──────────────────────────────────────────────┐
| ├── .mcp.json |  |  | ← personal MCP config (copy from .mc |
|---|---|---|---|
| │ Tauri WebView (React) |  |  | │ |
| │ | → | → iframe | │ |
| │ | dsh Web | + | │ |
└──────────────────────┬───────────────────────┘
│   invoke  
+  
┌──────────────────────┴───────────────────────┐
│   Tauri Rust   │
│  
  +  
│
│   service/core   Harness  
  │
│     dsh  
  │
│  
/     │
│ service/cli dsh shim + PATH │ │ service/update │ │ service/workflow dsh │ │ task dsh │ └──────┬───────────────────────────┬───────────┘ │ │ runtime/ (Node.js v22.22.0) dependencies/dsh/ ( ) └─────────────┬─────────────┘ ▼ dsh --profile < > --host 127.0.0.1 --port 3080 │ DSH_HOME=~/.dsh ▼ http://127.0.0.1:3080/ ←
## Harness
## deepseek-harness-pkg
## ，
## CLI
## ；GitHub

---

## Page 6

## Warning
— dsh
## Note
### — dsh
## /
## /
## ，
## Releases
No releases published Create a new release
## Packages
No packages published Publish your first package
## Contributors
No contributors
## Languages
TypeScript 62.5% Rust 33.6% Python 1.4% HTML 0.8% JavaScript 0.7% NSIS 0.5% Other 0.5%
## Suggested workflows
Based on your tech stack
Deno Test your Deno project
By GitHub Actions
Webpack Build a NodeJS project with npm and webpack.
By GitHub Actions
Datadog Synthetics Run Datadog Synthetic tests within your GitHub Actions workflow
By Datadog
More workflows
Configure
Configure
Configure