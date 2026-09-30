# c10vis-poem／off-grid-ai-mobile

Watch
0
The Swiss Army Knife of Offline AI. Chat, Speak, and Generate Images - Privacy First, Zero Internet. Download an LLM and
use it on your mobile device. No data ever leaves your phone. Supports text-to-text, vision, text-to-image
MIT License
join.slack.com/t/off-grid-mobile/shared_invite/zt-3swt3s84k-R0CHRwISaUpExV2~3qUUdQ
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from off-grid-ai/OGAM
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with off-grid-ai/OGAM:main .
Contribute
Sync fork
alichherawalla Merge pull request off-grid-ai#618 from off-grid-ai/feat/setting-disa…
c266e2e · 4 days ago
.bundle
feat: initial commit
6 months ago
.claude
temp
3 months ago
.github
chore(ci): drop android-build job — run…
5 days ago
.husky
fix(hooks): package*.json changes tri…
5 days ago
.maestro
fix: address PR review feedback
4 months ago
.vscode
chore: sonar connection
5 months ago
__tests__
Merge pull request off-grid-ai#618 fro…
4 days ago
android
chore(beta): 0.0.103-beta.4 (build 178…
2 weeks ago
demo-gifs
Add files via upload
4 months ago
docs
docs(gaps): A1 vision VERIFIED on bo…
last week
e2e
disable sonar for seed file
4 months ago
fastlane
fix(release): pin promote to the tested …
3 weeks ago
ios
chore(beta): 0.0.103-beta.4 (build 178…
2 weeks ago
patches
fix(ios): marshal background-downloa…
last month
pro @ ff0d874
chore: bump pro pointer to fix/tts-load…
2 weeks ago
c10vis-poem
off-grid-ai-mobile
Code
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
Fork
0
T


scripts
chore(release): tag production Slack a…
2 weeks ago
src
Merge pull request off-grid-ai#618 fro…
4 days ago
.dependency-cruiser.js
chore(arch): depcruise runs baseline-f…
3 weeks ago
.eslintignore
refactor(max-params): decompose fu…
5 months ago
.eslintrc.js
chore(deadcode): knip sweep — remo…
3 weeks ago
.gitattributes
feat: add pre-built APK and update do…
6 months ago
.gitignore
chore: gitignore docs/wire-captures (r…
2 weeks ago
.gitmodules
ci: build with private pro submodule o…
last month
.prettierrc.js
feat: initial commit
6 months ago
.swiftlint.yml
fix(ios): resolve SwiftLint violations in …
5 months ago
.watchmanconfig
feat: initial commit
6 months ago
AGENTS.md
docs: single tool-neutral rules.md; CLA…
last week
App.tsx
fix(downloads): in-flight downloads su…
2 weeks ago
CLAUDE.md
docs: single tool-neutral rules.md; CLA…
last week
FAST_FOLLOW.md
docs: fast-follow backlog after v0.0.10…
last month
Gemfile
chore(fastlane): add release automati…
last month
Gemfile.lock
chore(fastlane): add release automati…
last month
LICENSE
Create LICENSE
5 months ago
README.md
docs(readme): document GPU/NPU a…
4 days ago
altstore-source.json
chore: replace old packagename
5 months ago
app.json
chore(brand): rename app name to 'Of…
last month
babel.config.js
test: disable React Compiler for Jest
2 months ago
codecov.yml
chore: add Codecov coverage reportin…
5 months ago
index.js
feat(mcp): wire MCP SDK OAuth — UR…
last month
jest.config.js
fix(voice): background STT download …
2 weeks ago
jest.setup.ts
test(harness): reusable voice-mode/T…
3 weeks ago
knip.json
chore(deps): actually remove the 9 de…
3 weeks ago
metro.config.js
fix(ios): consolidate react-native-fs ont…
last month
package-lock.json
chore(release): 0.0.103
2 weeks ago


package.json
chore(release): 0.0.103
2 weeks ago
rules.md
docs(rules): reflect native builds move…
5 days ago
sonar-project.properties
ci(sonar): point Sonar at the off-grid-ai…
3 weeks ago
tsconfig.json
test(pro): real unit/integration coverag…
3 weeks ago
Chat. Generate images. Use tools. See. Listen. All on your phone or Mac. All offline. Zero data leaves your device.
Stars
Stars
2.8k
2.8k
License
License MIT
MIT
Google Play
Google Play Download
Download
App Store
App Store Download
Download
Platform
Platform Android | iOS | macOS
Android | iOS | macOS
codecov
codecov
unknown
unknown
Slack
Slack Join Community
Join Community
Off Grid Pro
Off Grid Pro $69 lifetime and $49 annual
$69 lifetime and $49 annual
A voice, personas, and actions. $69 for life, or $49/year.
Pro is an optional, additive tier. It gives the assistant a voice that talks back, personas you shape, and the tools to
draft real actions you approve. One license covers your phone and your Mac. All on-device.
Off Grid AI
The Swiss Army Knife of On-Device AI
BUILT BY
Off Grid AI Pro
What Pro adds
README
License


Voice mode - the free app transcribes your speech; Pro adds on-device Kokoro text-to-speech, so it talks back
and you run the whole thing hands-free. The voice runs in your phone's RAM.
Custom personas - give each assistant its own system prompt, voice, and persistent memory, so it stays in
character across conversations.
Draft, then approve - connect Calendar, email, and MCP servers like Linear, Notion, and GitHub. It drafts the reply
or files the ticket and waits. Nothing sends without your tap.
Sync, landing through July - your phone and your Mac merge into one picture over your own network, never a
relay. Your license includes it the day it ships.
→ Get Pro access - $69 once and it is yours forever (the price climbs as more people join, never down), or $49/year.
Pair it with Off Grid AI Desktop on your Mac. One Pro license covers both.
Most "local LLM" apps give you a text chatbot and call it a day. Off Grid AI is a complete offline AI suite — text
generation, image generation, vision AI, voice transcription, tool calling, and document analysis, all running natively
on your phone's or Mac's hardware.
Onboarding
Text Generation
Image Generation
Not just another chat app
What can it do?


Vision AI
Attachments
Tool Calling
Text Generation — Run Qwen 3, Llama 3.2, Gemma 3, Phi-4, and any GGUF model. Streaming responses, thinking
mode, markdown rendering, 15-30 tok/s on flagship devices. Bring your own .gguf files too.
GPU & NPU Acceleration — Your phone has silicon sitting idle. Off Grid uses it. Adreno GPUs via OpenCL run 20-40
tok/s on a Snapdragon 8 Gen 2+, against 15-30 on CPU; Apple Silicon uses Metal. The app detects what your device
has and defaults to the fastest backend that works, and you can override it in Settings. The Hexagon NPU
(Snapdragon) is there too, marked experimental because it is — it only accelerates Q4_0 and Q8_0 quants, a K-
quant silently falls back to CPU, and some model architectures come out garbled on it. Models that can actually use
the GPU or NPU are badged in the model list, so you pick the right quant before you download 4GB.
Remote LLM Servers — Connect to any OpenAI-compatible server on your local network (Ollama, LM Studio,
LocalAI). Discover models automatically, stream responses via SSE, store API keys securely in the system keychain.
Switch seamlessly between local and remote models.
Tool Calling — Models that support function calling can use built-in tools: web search, calculator, date/time, device
info, and knowledge base search. Automatic tool loop with runaway prevention. Clickable links in search results.
Project Knowledge Base — Upload PDFs and text documents to a project's knowledge base. Documents are
chunked, embedded on-device with a bundled MiniLM model, and retrieved via cosine similarity — all stored locally in
SQLite. The search_knowledge_base tool is automatically available in project conversations.
Image Generation — On-device Stable Diffusion with real-time preview. NPU-accelerated on Snapdragon (5-10s per
image), Core ML on iOS. 20+ models including Absolute Reality, DreamShaper, Anything V5.
Vision AI — Point your camera at anything and ask questions. SmolVLM, Qwen3-VL, Gemma 3n — analyze
documents, describe scenes, read receipts. ~7s on flagship devices.
Voice Input — On-device Whisper speech-to-text. Hold to record, auto-transcribe. No audio ever leaves your phone.
Document Analysis — Attach PDFs, code files, CSVs, and more to your conversations. Native PDF text extraction on
both platforms.


AI Prompt Enhancement — Simple prompt in, detailed Stable Diffusion prompt out. Your text model automatically
enhances image generation prompts.
Memory You Can See and Control — A phone has finite RAM, and a 4GB model does not politely share it. The model
manager shows you what is resident right now and what each one is costing you in RAM, with a per-model eject.
Model Loading picks the policy: Lean keeps one model in memory at a time, Balanced co-resides models that fit and
swaps the ones that don't, Aggressive commits a larger share of RAM so bigger models load. If a load is refused,
Load Anyway overrides it — your device, your call. When a model gets evicted mid-conversation, the chat says so
and offers to bring it back rather than silently failing.
Download Manager — Three downloads run at once, the rest FIFO-queue and show as Queued instead of quietly
stalling. Pause, resume, retry, cancel. Downloads survive backgrounding the app.
Task
Flagship
Mid-range
Text generation (CPU)
15-30 tok/s
5-15 tok/s
Text generation (GPU / OpenCL)
20-40 tok/s
—
Image gen (NPU)
5-10s
—
Image gen (CPU)
~15s
~30s
Vision inference
~7s
~15s
Voice transcription
Real-time
Real-time
Tested on Snapdragon 8 Gen 2/3, Apple A17 Pro. Results vary by model size and quantization.
Or grab the latest APK from GitHub Releases.
macOS: The iOS App Store version runs natively on Apple Silicon Macs via Mac Catalyst / iPad compatibility.
Performance
Install
Build from source
git clone https://github.com/off-grid-ai/OGAM.git
cd OGAM
npm install
# Android
cd android && ./gradlew clean && cd ..
npm run android


Requires Node.js 20+, JDK 17 / Android SDK 36 (Android), Xcode 15+ (iOS). See full build guide.
CI
CI
passing
passing
codecov
codecov
unknown
unknown
Tests run across three platforms on every PR:
Platform
Framework
What's covered
React Native
Jest + RNTL
Stores, services, components, screens, contracts
Android
JUnit
LocalDream, DownloadManager, BroadcastReceiver
iOS
XCTest
PDFExtractor, CoreMLDiffusion, DownloadManager
E2E
Maestro
Critical path flows (launch, chat, models, downloads)
This project is tested with BrowserStack.
Document
Description
Architecture & Technical Reference
System architecture, design patterns, native modules, performance tuning
Codebase Guide
Comprehensive code walkthrough
Design System
Brutalist design philosophy, theme system, tokens
Visual Hierarchy Standard
Visual hierarchy and layout standards
Join the conversation on Slack — ask questions, share feedback, and connect with other Off Grid AI users and
contributors.
# iOS
cd ios && pod install && cd ..
npm run ios
Testing
npm test              # Run all tests (Jest + Android + iOS)
npm run test:e2e      # Run Maestro E2E flows (requires running app)
Documentation
Community


Contributions welcome! Fork, branch, PR. See development guidelines for code style and the codebase guide for
patterns.
Built on the shoulders of giants: llama.cpp | whisper.cpp | llama.rn | whisper.rn | local-dream | ml-stable-diffusion |
MNN | Hugging Face
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
TypeScript 94.7%
Kotlin 3.1%
Swift 1.6%
Shell 0.2%
JavaScript 0.2%
Objective-C 0.1%
Ruby 0.1%
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
Webpack
Build a NodeJS project with npm and webpack.
By GitHub Actions
Configure
More workflows
Contributing
Acknowledgments
