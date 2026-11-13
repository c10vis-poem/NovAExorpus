# Memory system spec (owner dictation 2026-11-13 05:14 PST, engineered by session 8e3a65ec)

## Mission
Build the agent memory system: five memory layers plus a router, used by every agent harness on every repo, for
code-base retrieval, in-task observation, auditing and routing. Memory work comes first; everything else waits.
The claude-mem build (`claude-mem-strip-plan.md`) is finished later and slots into this spec.

## Ground rules
- **Reverse-engineer** means read the fork's source, keep the core capability, strip bloat, telemetry and hosted
  lock-in, and rebuild it in our own MCP. Nothing is installed as-is unless marked "straight over".
- Every source is the owner's `c10vis-poem` fork, synced to upstream before it is read.
- Every layer works **per repo** and **per agent harness**, and rolls up **enterprise-wide**.
- Every layer has a local copy on the phone and at least two off-phone copies (see Storage).
- The stop hooks force the agent to use every layer, tool and skill whenever needed: opening, negotiation and
  mid-contract alike (frozen claim 846bdf4e).

## Layer 0: Router
| | |
|---|---|
| Purpose | Decide which model, tool and memory layer answers each request |
| Source | Reverse-engineer **OmniRoute** (local fork `~/repos/OmniRoute`) |
| Brain | **Jev** as the routing judge, with small local weights as the router agent |
| Local models | QAI Hub compiled **Qwen 3.5 0.8B** first; also Gemma E2B / E4B, InternVL, Qwen 3.5 multimodal, Liquid AI (vision, voice), SmolLM and other small agents from the owner's voice/vision stack |
| Reach | **claw MCP** web tools: OpenRouter, the owner's terminal CLIs, and his Frontier Pro accounts through web access |
| Fans out to | Layers 1-5 in parallel |

## Layer 1: Episodic memory (what happened)
| | |
|---|---|
| Purpose | Sessions, events, decisions, observations over time |
| Source | Reverse-engineer **mem0** (local fork `~/repos/clovis-mem0-vingiaN`) |
| Scope | One episodic store **per repository** and one **per agent harness** |
| Offload | Each harness can offload to a **local SQL** store |
| Fits with | claude-mem's capture (hooks, observer, session summaries) |

## Layer 2: Semantic / static memory and governing principles (what is true, what the rules are)
| | |
|---|---|
| Purpose | Settled facts, decisions and the governing principles every agent follows |
| Source | Reverse-engineer **OB1** (local fork `~/repos/OB1`) and follow it as the guide |
| Copy exactly | Its **SHA-256** content addressing and its **Postgres** schema |
| Scope | Postgres **per repo** and an **enterprise-wide** Postgres |
| History | OB1 was chosen as the backbone 2026-09-26 (Recaps `memory/claude-auto/project_ob1_backbone_2026_09_26.md`) |

## Layer 3: AST code graph and code vectors
| | |
|---|---|
| Purpose | Code structure, call graphs, impact radius, code search |
| Source | **code-review-graph** **straight over** (not reverse-engineered), with its **tree-sitter** parsing |
| Scope | One graph per repo (`.code-review-graph/graph.db`; 8 repos already have one) |

## Layer 4: ASR graph / knowledge retrieval
| | |
|---|---|
| Purpose | Knowledge graph over documents and notes for retrieval |
| Tools | **Graphify** (official skills package; Graphify plugin for **Obsidian** desktop), official **Obsidian** skills, official **notebooklm-py** skills |
| Combine | NotebookLM + Graphify + Obsidian as one retrieval layer |
| Lives in | The vault (NovAExorpus) and Obsidian desktop |

## Layer 5: RLM vector graph (recursive retrieval and algebraic mapping)
| | |
|---|---|
| Purpose | Recursive fragmentation of large inputs plus vector-graph categorization |
| Source | Reverse-engineer the **Prime Agent** harness (local fork `~/repos/NvAEx-prime-agent`): copy its RLM recursive fragmentation |
| Layer on top | **MLR** and a **holograph** tool, using Jev's vector-graph categorization |
| Embeddings | **EmbeddingGemma 2** on the phone, same vector mapping |
| Owner's input | His research and planning documents on RLM (location to confirm) |

## Storage targets
Supabase, Cloudflare, Docker, Google Cloud Storage buckets, GitHub (private NvAEx-Recaps), the phone (local SQL).
Which layer goes where: to decide (draft for Layer 1 in `claude-mem-strip-plan.md`, "Where it runs").

## Build order (proposed)
1. Read each fork in full: OmniRoute, mem0, OB1, Prime Agent (Rule 12), one capability card each.
2. Layer 2 (OB1: SHA-256 + Postgres) first: every other layer writes facts into it.
3. Layer 1 (mem0 + claude-mem capture), per repo and per harness.
4. Layers 3 and 4 wired in (code-review-graph, Graphify + Obsidian + NotebookLM).
5. Layer 5 (RLM, MLR, holograph, EmbeddingGemma 2).
6. Layer 0 router (OmniRoute + Jev + Qwen 3.5 0.8B) over all of them.
7. Stop hooks that enforce use of every layer.

## Conflicts to clear with the owner
- Aesop-Xi and NovAExopia AGENTS.md say OmniRoute, mem0 and Terrestrial Brain are "dropped: do not set them up".
  This spec reverse-engineers OmniRoute and mem0. AGENTS.md needs the owner's new wording.
- SETTLED (owner 05:51): Terrestrial Brain IS OB1. One layer (Layer 2).
- Owner 05:51: also reverse-engineer ECC (with Prime Agent) to configure agent harnesses. Greedy-crane is the first
  harness: compare the owner's `Documents/_File-Driven-Agent-Operating-Environment/Greedy-crane/` with the plugin
  and update it. The heart of the agent identity: the **continual-harness** and **reasoning-bank** plugins.

## Unknown, to find before building
- **MLR**: not found in any note searched.
- **Holograph** tool: not found; possible match the local fork `~/repos/NvAEx-OmniGlyph` (unchecked).
- The owner's RLM research and planning documents: location.
- Notes searched: Recaps `memory/`, `handoff/`, vault `docs/`, `01-inbox/`, Aesop-Xi `docs/`; repo names in `~/repos`.
