# Canonical 8-Repository Mirror Specification


**Scope**: Master directory topology and ingestion contracts across the exact 8 canonical repositories.  
**Archive Download Link**: [Canonical_8_Repo_Mirror.zip](https://drive.google.com/file/d/1CR5o48SMvOLrjADBY6CisZoEjZrj0JSU/view?usp=drivesdk)


---


## 1. The 8 Canonical Repositories


1. **`aesop-xi`** (`Æsop-Xi`): Universal orchestration layer, ethical policy governance & arbitration.
2. **`novae-xorpus`** (`NovÆxorpus`): Hardened universal database, Living Wiki vault & ground truth repository.
3. **`novus-aexenti`** (`NovusÆxenti`): Cognitive MoE reasoning engine (0.8B Triage vs. 9B Executor) & memory flywheel.
4. **`novaexopia`** (`Novaexopia`): Tool harness runtime, OpenWiki TUI, and MCP capability bridge.
5. **`raw_database`** (`Raw database`): Cold sensory ground truth, raw data ingestion & interceptor extraction zone.
6. **`horizons-ui`** (`Horizons-Ui`): Master visual presentation shell, Android Chromium WebView & concierge UI.
7. **`novus-aesc`** (`Æsc`): Native system terminal & shell daemon (ADB loopback on 127.0.0.1:5555).
8. **`novus-aeyre`** (`novus-aeyre`): Native media & sensory ingress daemon (Silero VAD, Moonshine STT, Kokoro TTS).


---


## 2. Universal Subsystem Directory Layout


Every single repository contains this exact layout:


```
<repo_name>/
├── MAP.md                # Human-readable navigation map & component ontology
├── manifest.jsonl        # Cryptographic file index & catalog
├── README.md             # Subsystem identity, scope & operational setup
├── AGENTS.md             # Operational boundaries & agent contracts
├── RESUME.md             # Verified progress checkpoints & session state
├── chunk.jsonl           # Pre-tokenized machine retrieval & RAG passage layer
│
├── raw/                  # Incoming source landing zone (Interceptor extracts here)
├── clean_md/             # High-density condensed markdown (100% build context preserved)
├── wiki_md/              # Compounding living LLM wiki nodes with wikilinks
├── skills/               # Local procedural skills developed and applied here
├── tools/                # Local executable scripts & CLI utilities
├── pending/              # Staged tickets, backlog tasks, and unverified outputs
└── audit/                # Structured logs, failure traces, and divergence reports
```


*Crucial Invariant: The Cross Agent Auditor operates strictly inside an isolated external sandbox and does not appear in any repository trees.*


---


## 3. Worker Agent / Subagent Ingestion Law


- **No 1:1 file parity**: Strip conversational fluff and redundant boilerplate, but preserve 100% of technical instructions, parameters, and build fidelity so that raw and clean markdown build the exact same output.
- **Locality of Reference**: Skills and tools live locally inside the repository where they are applied.
- **Cryptographic Grounding**: All assets are indexed in the repository's `manifest.jsonl`.