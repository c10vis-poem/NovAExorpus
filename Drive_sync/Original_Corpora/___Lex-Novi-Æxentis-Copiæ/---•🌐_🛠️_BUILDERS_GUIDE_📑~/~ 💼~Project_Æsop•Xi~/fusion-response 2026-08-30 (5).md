You're right — Part 8 got cut off and was incomplete. Here's the full grill session manifest. This is the actual instruction set the grill agent follows:

---

## PART 8: GRILL SESSION MANIFEST (COMPLETE)

Save this as `~/novae-xorpus/GRILL-MANIFEST.md`:

```markdown
# GRILL WITH DOCS — ÆSOP-XI MASTER ARCHITECTURE SESSION

## SESSION CONTEXT

### Canonical Branding
- Motto: Xçineribus, in-variis-nunquam-varius, Novi-Æxentis-Copiæ, Vincent
- Translation: "From the ashes, unwavering in the midst of adversity, new forces of abundance conquer"
- Protocol: Æsop-Xi™ (aesop-xi) — tactical, narrative logic, ethical operations
- Agent Core: NovusÆxenti™ (novus-aexenti) — the new dynamic force
- Tools/Harness: NovÆxopia™ (novaexopia) — the abundance of the new agent (Claw harness)
- Database: NovÆxorpus™ (novae-xorpus) — the hardened unbreakable body of knowledge
- UI: Horizons UI™ (horizons-ui) — the ever-expanding canopy
- Shell Daemon: Æsc (nova-daemon-shell) — rooted and unwavering
- Media Daemon: Æyre (nova-daemon-media) — in the eye of the storm
- Verification standard: #d.u.m.b.a.s.s. — "It isn't dumbass-proof if it hasn't been #d.u.m.b.a.s.s. proven"

### Corrected Model Pathways (Ground Truth)

- **Executor Model**: Qwen 3.5 0.8B
  - Source: QAI Hub (pre-compiled Genie bundle)
  - Pathway: QAIRT runtime → HTP0 (Hexagon NPU v79)
  - NO llama.cpp, NO GenieX — runs through QAIRT directly
  - Compute: NPU-pinned (HTP0)
  - Context: 4096
  - Role: Fast task execution, prompt synthesis, mem0 + Reasoning Bank access
  - Runs: Node Alpha (phone), always-on

- **Query Model**: Qwen 3.5 9B (Unsloth GGUF)
  - Source: Unsloth GGUF release
  - Pathway: GGUF → GenieX llama_cpp → GGML Hexagon backend → librc → kernel → HTP0
  - Compute: --device npu (pinned to Hexagon NPU v79)
  - Context: 4096
  - Role: Meta-prompt compilation, OB1 vector queries, JSONL index retrieval, tool calling including frontier models
  - Runs: Node Alpha (phone), on-demand
  - CAN call frontier models: Claude, GLM 5.2, Fable 5, Opus, Gemini as tool calls in research/deep query/conversation modes
  - Gemini usage: good for ideas/infrastructure data, bad at code. Use for ideas, end session when it starts coding.

- **Fallback Hierarchy** (if 9B NPU chokes on unsupported ops):
  1. 9B Q4_0 → npu (preferred, test first)
  2. 9B Q4_0 → hybrid (if NPU-pinned has op fallback issues)
  3. 4B Q4_0 → npu (drop to smaller model, stay on NPU)
  - Architecture goal: largest model running on bare metal NPU
  - 0.8B stays NPU-pinned via QAIRT regardless — it's the executor, not negotiable

- **Voice Stack**: NOT IN SCOPE for this session
  - Deferred to Phase 3 (post-APK build)
  - 3-APK architecture (Horizons UI + Æsc Shell Daemon + Æyre Media Daemon) is the solution
  - No existing solution to reference — this is greenfield work
  - Every AI session that has tried to help with voice on Android has failed — no prior art

### Harness & Tool Corrections (Ground Truth)

- **ECC** (affaan-m): For Claude Code sessions (cloud + terminal + desktop). Plugin marketplace, 68 agents, 286 skills. Has desktop UI with manifest guide. Can be wired to Gemini. Does NOT integrate with Prime Agent —