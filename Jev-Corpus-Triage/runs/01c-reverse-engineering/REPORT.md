# Jev corpus triage: 01c-reverse-engineering

Model `jev-1.14.0`, thresholds yes > 0.7, no < 0.3. 58 sections from 17 files, 6 files handled in code, 105755 input tokens, 0 failed requests.
Folders: `reverse-engineering`, `global-documentation-vault/reverse-engneering`, `Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/---📜🪶AEsop-Xi_/#D.U.M.B.A.S.S..md/#REVERSE.ENG& RESEARCH_`

These are Jev's judgments per section, not a reading of the files. Use them to choose what to read.

A file is a **third-party copy** when most of its text describes another project; its sections count as
decisions or open work only where Jev rates the section as the operator's own writing.

## Operator's own files (6): read these first

| File | Sections | Main kind | Decisions | Open work | RE findings | Components | Dropped stack |
|---|---|---|---|---|---|---|---|
| `reverse-engineering/README.md` | 2 | index_or_pointer | 1 | 0 | 0 | - | - |
| `reverse-engineering/llm_wiki.md` | 2 | index_or_pointer | 0 | 1 | 0 | - | - |
| `reverse-engineering/CLAUDE.md` | 4 | research_notes | 0 | 0 | 0 | - | - |
| `reverse-engineering/duplicates-review/4.docx` | 1 | third_party_docs | 0 | 0 | 0 | - | - |
| `reverse-engineering/duplicates-review/5.docx` | 2 | third_party_docs | 0 | 0 | 2 | - | - |
| `reverse-engineering/skill_manifest.json` | 1 | code_or_config | 0 | 0 | 0 | - | - |

## Third-party copies (11): reference only

| File | Sections | Main kind | Decisions | Open work | RE findings | Components | Dropped stack |
|---|---|---|---|---|---|---|---|
| `reverse-engineering/research/AI-Agents-Projects-Tutorials/c10vis-poem／AI-Agents-Projects-Tutorials- Multi-agent systems, memory, planning, reasoning loops.md` | 5 | index_or_pointer | 0 | 0 | 0 | - | mem0 |
| `reverse-engineering/research/CLAUDE.CODE-ANDROID_REV.ENG_/c10vis-poem／android-reverse-engineering-skill- Claude Code skill to support Android app's reverse engineering.md` | 7 | third_party_docs | 0 | 0 | 0 | - | - |
| `reverse-engineering/research/CQRS (Command Query Responsibility Segregation) Pattern with an Example - by İnci KÜÇÜK - Stackademic.md` | 2 | third_party_docs | 0 | 0 | 0 | - | - |
| `reverse-engineering/research/Edge overlay AI & Off-Grid AI/c10vis-poem／off-grid-ai-mobile.md` | 4 | third_party_docs | 0 | 0 | 0 | - | Qwen3-VL |
| `reverse-engineering/research/How to Build a Custom Agent Harness.md` | 2 | third_party_docs | 0 | 0 | 0 | - | - |
| `reverse-engineering/research/MLC LLM/c10vis-poem／mlc-llm- Universal LLM Deployment Engine with ML Compilation.md` | 1 | third_party_docs | 0 | 0 | 0 | - | - |
| `reverse-engineering/research/Web guidance skill repo/c10vis-poem／modern-web-guidance-src.md` | 3 | third_party_docs | 0 | 0 | 0 | - | - |
| `global-documentation-vault/reverse-engneering/Off Grid AI.md` | 2 | third_party_docs | 0 | 0 | 0 | - | Qwen3-VL |
| `global-documentation-vault/reverse-engneering/overlayd-ai-technical-guide.md` | 11 | third_party_docs | 0 | 0 | 4 | - | OmniRoute |
| `global-documentation-vault/reverse-engneering/socketsweep-readme.jsonl` | 1 | third_party_docs | 0 | 0 | 1 | - | - |
| `Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/---📜🪶AEsop-Xi_/#D.U.M.B.A.S.S..md/#REVERSE.ENG& RESEARCH_/PROOFS/socketsweep-readme.md` | 8 | third_party_docs | 0 | 0 | 2 | - | - |

## Operator decisions (1)

- 0.83 `reverse-engineering/README.md` § Rules that apply here: ## Rules that apply here

## Open work (1)

- 0.83 `reverse-engineering/llm_wiki.md` § Contents: # llm_wiki — Reverse engineering and troubleshooting

## How-it-works findings, any source (9)

- 0.97 `global-documentation-vault/reverse-engneering/socketsweep-readme.jsonl` § (top of file): {"id": "socketsweep-001", "section": "problem", "heading": "The Problem", "content": "Standard Android-to-PC USB file browsing uses MTP (Media Transfer Protocol
- 0.95 `Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/---📜🪶AEsop-Xi_/#D.U.M.B.A.S.S..md/#REVERSE.ENG& RESEARCH_/PROOFS/socketsweep-readme.md` § Interaction Lifecycle: ## Architecture (Three Layers)
- 0.93 `Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/---📜🪶AEsop-Xi_/#D.U.M.B.A.S.S..md/#REVERSE.ENG& RESEARCH_/PROOFS/socketsweep-readme.md` § How It Works: ## How It Works
- 0.89 `reverse-engineering/duplicates-review/5.docx` § (top of file): To securely decouple and implement an interdependent background daemon architecture inside Android, you must strictly align your implementation with the Officia
- 0.89 `global-documentation-vault/reverse-engneering/overlayd-ai-technical-guide.md` § 4. The Logic Glue: Node.js & Telegram Bridge: # Server startup configuration
- 0.88 `reverse-engineering/duplicates-review/5.docx` § (top of file): // MainOrchestratorService.ktimport android.app.Notificationimport android.app.NotificationChannelimport android.app.NotificationManagerimport android.app.Servi
- 0.87 `global-documentation-vault/reverse-engneering/overlayd-ai-technical-guide.md` § - /v1/embeddings: # Intercepted endpoint configuration
- 0.79 `global-documentation-vault/reverse-engneering/overlayd-ai-technical-guide.md` § Relevance to this project: ## Relevance to this project
- 0.72 `global-documentation-vault/reverse-engneering/overlayd-ai-technical-guide.md` § 5. Vision Integration: OpenClaw & Multimodal AI: ## 5. Vision Integration: OpenClaw & Multimodal AI

## Unsettled sections in the operator's own writing (5)

Jev could not settle decision or open work here; read these by hand.

- `reverse-engineering/CLAUDE.md` § HOW
- `reverse-engineering/CLAUDE.md` § The kit
- `reverse-engineering/CLAUDE.md` § Working rules
- `reverse-engineering/README.md` § Conventions
- `reverse-engineering/llm_wiki.md` § Retrieval notes

## Handled in code (6)

- `global-documentation-vault/reverse-engneering/Off Grid AI`: copy of the same-name `Off Grid AI.md` (four-artifact convention)
- `global-documentation-vault/reverse-engneering/overlayd-ai-technical-guide.jsonl`: copy of the same-name `overlayd-ai-technical-guide.md` (four-artifact convention)
- `reverse-engineering/research/Edge overlay AI & Off-Grid AI/c10vis-poem／edge-overlay-ai`: link stub: https://github.com/c10vis-poem/edge-overlay-ai
- `reverse-engineering/research/How to Build a Custom Agent Harness`: copy of the same-name `How to Build a Custom Agent Harness.md` (four-artifact convention)
- `reverse-engineering/research/Kotlin SDK/c10vis-poem／kotlin-sdk- The official Kotlin SDK for Model Context Protocol servers and clients. Maintained in collaboration with JetBrains`: link stub: https://github.com/c10vis-poem/kotlin-sdk
- `reverse-engineering/research/VIA_BROWSER/c10vis-poem／Via- Via is a simple browser, and this repository is set for localization.`: link stub: https://github.com/c10vis-poem/Via
