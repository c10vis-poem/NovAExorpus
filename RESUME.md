Session files: [[AGENTS]] · [[PENDING]] · [[MAP]] · [[GRILL-MANIFEST]] · [[NAMING-CANON]]

# RESUME.md — Session Ledger (rewritten every session)

Repository: NovÆxorpus (`c10vis-poem/NovAExorpus`, PUBLIC), the master wiki and vault.
**Last session: 2026-10-02** (phone, Claude Code, Opus 5.5, personal account). It covered workspace and enforcement, then the NPU server and benchmark. Full ledger: `~/.claude/session-work/2026-10-02/SESSION-LOG.md`.
*This is a mid-session rewrite (the wrap-up gate fired on a mention). The real wrap-up rewrites it again.*

## NEXT SESSION — START HERE
The Stop gate requires a status for each numbered item: `resume-item <n> done|blocked "<evidence / what's needed>"`.

1. **Run the tier-1 NPU benchmark, with the phone prepped** (plugged in, extra browsers and apps closed): `cd ~/tools/npu-bench && python3 bench.py --tier 1 /storage/emulated/0/Download/Qwen3.5-0.8B-Q4_0.gguf ~/downloads/Qwen3.5-2B-Q4_0.gguf /storage/emulated/0/Documents/Models/gemma-4-E2B_q4_0-it.gguf /storage/emulated/0/Download/SmolVLM2-2.2B-Instruct-Q8_0.gguf`. Results go to `docs/NPU-BENCHMARKS.md` + `benchmarks/results/`.
2. **Finish the skill-observation bookkeeping:** 5 were actioned on 2026-10-01 (0003, 0010, 0011, 0013, 0014). Nine are still open (0001, 0002, 0004–0009, 0012) plus 0015 and 0016 from today. Check each against the hooks built since (H1 Stop gate, H2 sync-on-use, H5 secrets), mark them point by point, and write `last-review-date.txt`.
3. **Build the next benchmark pieces:** the QAIRT route in the server shim (bundles: Qwen3-VL-4B, InternVL3.5-4B, SmolLM2), vision input (`geniex_vlm_*` + mmproj), then tiers 2 and 3 and the role map.

## STATE (verified 2026-10-02)
- **Enforcement (all live, user-level settings, so every session in every repo):**
  - H1 RESUME gate + the **Stop gate** (`stop-gate.sh`). The Stop gate blocks turn end until RESUME is read, the START HERE items have a status, task-observer has run, no ENFORCEMENTS requirement is pending, and in wrap-up mode RESUME.md is rewritten.
  - H1b housekeeping reminder; H2 sync-on-use; H3 session ledger; H4 ship-session; H5 secrets; H6 ENFORCEMENTS gate; H7 classifier (keyword rows; `CLASSIFY_URL` slot unused).
  - Operator override = `#skip-enforce` typed by the user only.
  - New rows 2026-10-02: vault, graphify, voice, bench.
  - Hook sources + the exact live registrations (`settings.hooks.json`) are in aesop-xi `deploy/phone/hooks/` (PR #34 merged).
- **Workspace:** `additionalDirectories` = vault, aesop-xi, NovA-skills, aesop-task-observer, NoVa-honey-for-devs, NovA-code-review-graph, obsidian-skills, graphify, NovA-terrestrial-brain. The `claude()` launcher in `~/.zshrc` adds `--add-dir` for all 9 (their skills/agents). `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` loads their CLAUDE.md. Start sessions in the repo you work in for its own hooks and `.mcp.json`.
- **NPU:**
  - `npu-serve` → GenieX **v0.7.1** (sha verified) on the NPU at `127.0.0.1:18181/v1`, through a C shim over `libgeniex.so`. Proven to be GenieX, not llama-server. Defaults are `npu`, not hybrid.
  - Placement is decided per model: Unsloth's Qwen 3.5 files keep `ssm_out` in Q5_K, so those weights run on the CPU (38 handoffs per token; 2B NPU 12.7 vs CPU 34 tok/s). Gemma E2B is clean (NPU 18 vs CPU 9.4).
  - QAIRT bundles decode about 2× faster than llama.cpp (AI Hub S25 numbers).
  - Facts: `~/.claude/NPU-ON-DEVICE.md`. Guide: `docs/LOCAL-AI-GUIDE.md`. Build log: `docs/NPU-SERVE-BUILD-LOG.md`.
- **AI Hub CLI:** `proot-distro login debian -- /root/venvs/qai-hub/bin/qai-hub-models info|perf|fetch …` (needs Python <3.14). Chipset for this phone: `qualcomm-snapdragon-8-elite-for-galaxy` (HTP v79, soc 69).
- **Models (fingerprinted; byte-identical duplicates removed; cross-chip variants kept on purpose):**
  - Qwen 3.5 0.8B / 2B / 9B (Unsloth); bartowski 9B (better NPU mix)
  - InternVL3.5-8B Q4_0 (good fit, 4.8 GB)
  - Qwen3-VL-4B bundle (8 Elite) and 8B bundle (X2 Elite, v81; test-load it)
  - SmolLM2-1.7B bundle (8 Elite), Qwen3-1.7B bundle (X Elite)
  - SmolVLM2-2.2B Q8_0
  - Whisper large-v3-turbo QNN-ONNX (8 Elite for Galaxy)
  - deepspeech2 TFLite (needs LiteRT)
- **Benchmark:** `~/tools/npu-bench/bench.py`. Records runtime / mode, placement verdict (full HTP or partial, naming the CPU weights) and provenance (uploader, sha, as downloaded vs requantized).
  - Tiers: T1 = Oracle app (help desk / install guide: photo part-ID → manual → part number → where to buy); T2 = routing / tools / planning / frontier hand-off; T3 = vision+language.
  - Oracle photo set: 23 items in `benchmarks/oracle/` (git-ignored: private-use diagrams; includes the 1985 Johnson 9.9 J10RCOM gearcase).

## DECISIONS 2026-10-02
- The fork rule doesn't cover release binaries: forks don't carry releases, so GenieX tarballs come from qualcomm/GenieX releases with checksum verification.
- Never say "won't run" from labels: test-load cross-chip variants. Delete only SHA-identical duplicates.
- "Make it work, per model": requant, other uploaders, QAIRT bundles, AI Hub Workbench (free compute), HF, Vertex (credits).
- H5/H6 stay keyword-based until the grill session. Overrides belong to the operator only.
- Wrap-up order: rewrite RESUME → operator runs GitSync → "push now" / wrap up → the ship step merges vault-sync.

## OPEN ITEMS, IN ORDER
1. The START HERE items above.
2. Ship the pending aesop-xi branch `feat/stop-gate-resume-enforce` (worktree `~/repos/.wt-aesop-xi-wrapup`: RESUME-in-wrap-up check + 4 ENFORCEMENTS rows) on the next "push now".
3. Operator fetches: mmproj for SmolVLM2 2.2B and InternVL3.5 8B; Intern3.5-VL-4B QAIRT bundle for 8 Elite for Galaxy.
4. Requant Qwen 3.5 files to pure Q4_0 (`llama-quantize --pure`; phone, GitHub runner or Vertex) and compare with bartowski's mix.
5. TFLite / LiteRT setup (deepspeech2, Gemma mobile).
6. Vault code-review-graph build crash (long filename under `Drive_sync/`, stat before ignore). Fix in the fork.
7. Check three leftover worktrees from 2026-10-01 (`~/.claude/session-work/2026-10-01/wt-*`) for unmerged work.
8. Voice: operator runs `vv cancel`; try `/voice tap`.
9. **Grill session:** H5/H6 per-tool blocks; H7 auto-classifier (longer timeout, model reads skill descriptions); post-task flagging via task-observer + Reasoning Bank; keyword mention-vs-command false triggers; Hermes, dsh, terrestrial-brain (VM unreachable); llm-wiki / OmniRoute / dumbass config; plus the 2026-10-01 grill agenda (aesop-xi PR #18, wiki agent home, custom-skill home, Continual Harness).
10. Gemma 4 fine-tune: our own LoRA job on Vertex (managed SFT is Gemini-only and not exportable) → GGUF Q4_0. Start from QAT checkpoints.

## HANDOFF SOURCES
Read this session: RESUME (old), ENFORCEMENTS.md, hooks README, INVENTORY.md, WRAP-UP.md, NPU-ON-DEVICE.md, LOCAL-AI-GUIDE.md, resume-gate.sh, enforce-gate.sh, classify.sh (head), git-gate.sh, task-observer + android-termux-operator skills, Claude Code docs (memory, skills, voice), GenieX docs + `geniex.h` (d8852590, v0.7.1), llama.cpp #22352 / PR #22334, transcript b6ab92d6 (review, H1–H7 and observation-edit passages), Vendor-Registries docs (Qwen 3.5 release, InternVL3.5 paper, AI Hub READMEs, GenieX Quickstart / Android install, Gemma 4 ×3, Vertex SFT; partly via helpers), PENDING.md (structure + key lines).
Not read: most of transcript b6ab92d6; vault docs 00–05; Hexagon SDK; ECC.
