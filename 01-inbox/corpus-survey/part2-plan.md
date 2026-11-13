---
status: staged
source: wiki-admin session 3c1dfa47, contract B task P
date: 2026-11-11
---
# Plan for part 2 (from inventory.md and vendors-and-models.md)

## What the owner asked for (his words, 2026-11-11)
- "i point you at a much larger compilation of wiki admin skills and attributes" -> found: `_File-Driven-Agent-Operating-Environment/Greedy-crane/` (24 files).
- "we can also audit thhis setup and clean it uo too" -> `01-inbox/wiki-admin-refine/audit.md` (26 items, waiting on approval by number).
- "there's no way in hell I would use an API when I have a terminal CLI with my account credits" -> `agy` first.
- "You should be parsing this shit up in separate docs ... in separate folders ... inside of Git, Inside my Nova Corpus GitHub, You could create 256 SHA"
  -> one folder per asset in the vault repo, each with clean MD, `manifest.jsonl` (sha256 per file), `chunk.jsonl`, MAP.md.
- "Oh hey, I havesupabase" -> candidate store for embeddings (pgvector) beside the files in git.

## Phase 1: the planning documents (owner's research), about 300 files, 12 batches of 25
| Set | Path | Files | Size |
|---|---|---|---|
| A wiki-admin compilation | `_File-Driven-.../Greedy-crane/` | 24 (2 zips, 1 HTML 1.2 M) | 1.9 M |
| B targets and build orders | `_Target-planning_objectives/` 4, `Plan-Order-1,2&3/` 3, `More-Argon-Builds/` 4, `plan-docs/` 16, `Cloudflare/`, `embeddinggemma-2-/`, `Jev Observation Database ...` | ~30 | ~0.7 M |
| C `_README.txt/` folder | Cialdini/JEV/Subagent Persuasion, APK_3=HyperionXi, Repo-File-Structure | 31 | 369 K |
| D Jev docs | `_Jev/` | 178 | 1.8 M |
| E Download planning files | blueprints (.md/.html/.mht), `19_Phase1...`, `Frankenstein/`, `Fable-2026-11-03/`, `OR/`, `Copy of Agent os/` | ~25 + folder contents (not counted) | ? |
| F vault root reports | `Argon reports*.md` (3), `Frontier Agent Engineering ... .html` (2, likely identical) | 5 | 172 K |
Order: A first (it is the wiki-admin spec the owner pointed at), then B, C, F, E, D (D is vendor docs, lowest priority).

## Phase 2: vendor and model documentation into per-asset folders
- One folder per vendor under `Vendor-Registries/<vendor>/`: `VENDOR.md` (standalone vendor doc), `clean/` MD, `manifest.jsonl`
  (path, sha256, size, source, date), `chunk.jsonl`, `MAP.md`. Raw files stay where they are; only the inbox-staged copy is new.
- One per model in a new `Vendor-Registries/<vendor>/models/<model>.md` card (file path, size, sha256, runtime, chip, route),
  covering the ~30 models in vendors-and-models.md. Weights are never put in git (sha256 + path only).
- Large stores later, each its own work order: `global-documentation-vault/` (168), `QAIRT-QNN/` (2,258; dedupe first),
  `Drive_sync/` (2,363), `raw_database/` (889), `__RESUME.md/` (867).
- Hashing 79 G of weights takes time on the phone: hash model files in one background run per folder, record to the manifest.

## Routes for the reading (CLI first)
| Job | Route | Fallback |
|---|---|---|
| Bulk text extraction and drafting | `agy -p ... --model <Gemini 3.8 Flash slug> --output-format json` (account credits) | corpus-ingest workers on Claude (sonnet), 4 at a time |
| Hard synthesis (the compilation, the merge into greedy-crane) | `agy` with Gemini 4 Argon, or Carbon if the Ultra account holds it | Claude Opus in this session |
| Injection scan | `wa_quarantine.py` (detect only) | |
| Triage (which set, private or not, duplicate or not) | JEV, or Qwen 3.5 0.8B on GenieX | |
| Scans, images, HTML screenshots (OCR) | Qwen 3.5 2B/4B + mmproj on GenieX, or Gemini Flash via `agy` | InternVL 3.5 on QAIRT |
| Embeddings for the index | EmbeddingGemma 2 `eg2-text` on the NPU (port 8085) | generic LiteRT on CPU |
| Index store | `chunk.jsonl` in git; Supabase pgvector if the owner wants search over it | |
| Independent verify | `verify.py` / `check.py` (different extractors) and a second model that did not draft | |
| Frontier second opinion | OpenRouter (`anthropic/claude-fable-5.2`, `google/gemini-4-carbon`) | |

## The next work order would hold (owner signs each)
1. Route tests: one round trip each (agy Flash, agy Argon/Carbon, EG2 server, Qwen 0.8B on GenieX, OpenRouter, Supabase).
2. Phase 1 set A read in full (24 files) + compare with greedy-crane (A1/A2 of the first order).
3. Batch ledger for phase 1 sets B-F (`batch_ledger.py plan`), workers only on the owner's okay per dispatch (vault AGENTS.md Rule 6).
4. Per-asset folders with sha256 manifests for Vendor-Registries (10 vendors) in `01-inbox/` first; promotion per file by name.
5. The audit items the owner approves by number.
To spawn workers or agy under a contract, the order needs `AGENT corpus-ingest model: sonnet` lines and a `SCOPE Bash: agy -p` line.

## Questions only the owner can answer
1. Which account is logged into `agy` (Pro with Argon, or Ultra with Carbon)? Where is the second Gemini account?
2. The second Claude Pro account: this phone or another device?
3. Supabase: which project, and do you want embeddings there, or only in git (`chunk.jsonl`)?
4. OpenRouter key name in `nvaex-secret`?
5. Vault is PUBLIC (AGENTS.md:95): may vendor docs and your planning docs go into it as clean MD? Anything to keep out?
6. `tablet-age-key.txt` sits in shared Documents: move it into the secret store?
7. The duplicate vault copies in `_Merovingians_Keep/` (14 G + 3.1 G) and the 7.1 G QAIRT dump twice: keep, or a cleanup order?
8. Download set E: which folders count as research (`Frankenstein/`, `Fable-2026-11-03/`, `OR/`, `Copy of Agent os/`)?
