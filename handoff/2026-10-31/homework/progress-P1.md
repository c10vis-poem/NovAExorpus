# progress-P1
## Plan
- [ ] read BRIEF.md, work-order.md, P1-paths.txt, TOOLS.md, corpus-ingest.md
- [ ] survey on-phone tools
- [ ] map source type -> converter + fallback
- [ ] write P1-intake-convert.md
- [ ] corpus-verify own claims
## Last action
2026-10-30 started
## Findings
## Blocked
- 2026-10-30: read corpus-ingest.md, TOOLS.md, BRIEF, work-order; gdrive-to-markdown (full), google-multi-account (partial: tools, drive.js export, sanitize head, scopes). None of the 9 plugins has hooks/.
- firecrawl plugin (full on main SKILL, security, parse, download; descriptions of rest), anydoc README/SKILL (partial), LiteDoc README (grep), convert_raw_to_md.py full (195 lines), clean.py outline. On phone (which): anydoc wrapper(proot), litedoc wrapper(proot), pdftotext, mutool, pandoc, ffmpeg, tesseract(eng only), yt-dlp, markitdown. NOT: whisper, ocrmypdf, soffice.
- TODO: apify, watch-video, local-whisper, desktop-commander, drunken-master, claude-bridge, other phone repos, extraction-index, mapping, write deliverable
- 2026-10-30: read apify (agent+skills desc+rag workflow), local-whisper (full SKILL), watch-video (SKILL outline+key sections, server.py tool list), C10vis-claude-video (README head, SKILL grep, hook), WhisperKitAndroid README head (DEPRECATED), operator research pdf-to-structured-markdown-jsonl.md (sections 1,2,3.7-3.9,4). Python on phone: pymupdf, docx, pypdf, bs4 OK; openpyxl, pptx, faster_whisper, pytesseract MISSING.
- NEXT: live-test converters on samples (scratchpad), read desktop-commander, drunken-master, claude-bridge, remaining phone repos (crawl4ai, browser-use, Novus-firecrawl), write deliverable.
- 2026-10-30 LIVE TESTS (scratchpad .../scratchpad/p1): anydoc docx+pdf OK (md out), anydoc scan.pdf exit 3 "needs OCR"; markitdown docx OK, markitdown pdf = MissingDependencyException; tesseract on rendered png OK; litedoc convert scan.pdf --ocr OK 11.6s (via proot); pandoc html drops <script>. STT on phone: ~/tools/whisper-parakeet/whisper-cli (glibc, proot, --help OK, no ggml whisper model found by find), moonshine sherpa 10s ceiling, parakeet dir.
- LIVE: parakeet-cli (proot, ~/models/parakeet/ggml-parakeet-tdt-0.6b-v3-q8_0.bin) transcribed espeak wav 4.4s -> text in 3.3s wall. Long-audio untested.
- 2026-10-30 deliverable P1-intake-convert.md written. Next: spot-verify claims, handback.
## Pass 2 (coordinator: full read of all non-media files)
- [ ] google-multi-account  [ ] firecrawl  [ ] apify  [ ] watch-video  [ ] desktop-commander  [ ] drunken-master  [ ] claude-bridge  [ ] update deliverable + citations
- 2026-10-30 pass 2 started; doing google-multi-account first
- [x] google-multi-account pass 2: read auth.js, config.js, gmail.js (all), drive.js (all but lines 300+ tail), calendar.js (1-260), sanitize.js (all), index.js (1-107, 440-end), scopes.js, setup-tokens.js (skim w/ grep), commands add-account/reauth/setup (skim), skill+gcp-walkthrough, PRIVACY. NEW: gmail.js:33,160-162 + sanitize.js truncate bodies at 5000 chars ("[...truncated]"); drive.js:129 requests nextPageToken but never returns it (no paging past 100/200); drive.js has 0 withAuthErrorHandling; PRIVACY.md/setup.md/skill stale (.tokens.json, "pre-baked creds", no Drive scope in walkthrough).
- [x] firecrawl pass 2: read agent, interact, search, monitor (full), goals/json-tracking/developer/research (first ~28 lines), install rest, README top, skill-gen headings. NEW: SKILL.md:107-126 + firecrawl-search send vendor feedback (URLs, notes) unless FIRECRAWL_NO_ENDPOINT_FEEDBACK=1 / FIRECRAWL_NO_SEARCH_FEEDBACK=1: set opt-out; `interact --profile` persists cookies cloud-side; keyless covers search/scrape/interact (install.md), crawl/map/download need login.
- [x] apify pass 2: agent.md (all), ultimate-scraper SKILL (all), gotchas.md (first 60 lines: PPE cost protocol >$5 warn, >$20 confirm), actor-index head, 4 dev skills heading outlines only (cut anyway; NOT full read).
- [~] watch-video pass 2: read probe.py, _cache.py, _common.py, frames.py (to line ~160 of ~290) in full-ish. Useful for P3: _cache.py:11-15 size:mtime step fingerprint + output-aware cache, _common.py atomic_path/finalize, ExitCode table, JSON-line stderr events. Next: fetch.py, transcribe.py, watch_video.py, server.py, dedup/ocr/report/highlights/relabel/watch_batch/post_to_jira/fetch_attachment/smoketest (outlines).
- watch-video: also read fetch.py url section (61-182), transcribe.py 1-45, 91-167, 311-366, 909-982 + def outline; watch_video.py 1-45 + outline. NEW: transcribe_local uses vad_filter=True (may drop quiet speech: lossy); hosted providers (groq/openai/deepgram) send audio off device, keys from env or creds file (transcribe.py:128-167); fetch.py subtitles en-only default; imagehash module MISSING on phone (frames --dedup needs it).
- watch-video: docstring heads of dedup/highlights/ocr/report/relabel/watch_batch/post_to_jira/fetch_attachment/smoketest (NOT full bodies). highlights.py calls Anthropic API with a key (cut). ocr.py uses tesseract (matches phone). watch_batch.py: per-item workdir + batch.json + continue-on-error + --parallel N (P3 pattern). SKILL.md cache + batch + workspace sections read. server.py outline only.
- [x] desktop-commander (README, overview 1-200, knowledge-base+obsidian-vault heads, other 3 skill outlines), drunken-master (SKILL all 140ish lines, evals.json parsed: 13 evals), claude-bridge (SKILL all, agent all, README top). NEW: claude-bridge repo = github.com/Stigmavlc/claude-bridge (README badge). Next: grab line numbers, rewrite deliverable sections with read-depth + new findings.
- deliverable updated with section 6 (read depth, 13 findings, citations). DONE pass 2.
