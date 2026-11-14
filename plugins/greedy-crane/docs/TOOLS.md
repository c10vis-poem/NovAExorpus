# Corpus ingest: tools per stage

Everything listed is already on the phone (checked 2026-10-29). Paths: `~` = /data/data/com.termux/files/home; vault = /storage/emulated/0/Documents/NovAExorpus; wiki-admin scripts = `plugins/greedy-crane/scripts/` in the vault. The 274 older extraction scripts and skills across the vault and repos are indexed in `~/.claude/session-work/2026-10-29/wiki-admin-homework/extraction-index.txt`; check it before writing anything new.

| Stage | Use first | Fallback | Notes |
|---|---|---|---|
| Intake: Google Drive, Docs, Sheets, Slides | Google Drive connector (`read_file_content`, `download_file_content`) | vault `Drive_sync/` mirror | Binary files need the download call |
| Intake: Gmail | Gmail connector (`search_threads`, `get_thread`) | none | |
| Intake: web pages | `~/repos/Novus-firecrawl`, TinyFish `fetch_content` | `~/repos/c10vis-crawl4ai`, `~/repos/NvAEx-browser-use` | |
| Intake: video, audio | `~/repos/C10vis-claude-video` | `~/repos/Novus-WhisperKitAndroid` | |
| Convert: PDF, DOCX, XLSX, PPTX, HTML | `anydoc` (`~/repos/aesop-anydoc`), `convert_raw_to_md.py RAW OUT` | vault `tools/clean.py`; the pdf, docx, xlsx, pptx skills | The converter reports EMPTY / ERROR / unsupported by name |
| Convert: scanned PDF, images | OCR (open: no OCR tool chosen yet) | | Converter reports these as EMPTY |
| Size-gate | vault `tools/chunk.py`; `honey-px` skill for huge read-only text | `honey-ccr` skill for huge uniform lists | Read huge files outline-first |
| Fan-out | `corpus-batch-processing` skill; the Workflow tool | `gemini_infer.py` (Gemini lane); Gemini app and Spark agents | Each worker gets one batch and a progress file |
| Wiki and search | `wiki-admin-ingest`, `wiki-admin-query`, `wiki-reference-router` skills; `manifest.py build` / `query` | `llm-wiki` plugin | MAP.md first, manifest queried, never loaded whole |
| Extract | `w5h-extraction` skill (decisions); `skill-creator` skill (skills and tools) | | Nothing becomes a skill or tool without the operator's approval |
| Check | `corpus-verify` skill with `verify.py` / vault `tools/check.py` (independent extractors) | `wiki-admin-lint` skill | The tool that converted a file never judges it |
| Stage and promote | `audit_staging.py`, then `promote.py --approved-by NAME` | | Promotion is the wiki admin's, not this agent's |
