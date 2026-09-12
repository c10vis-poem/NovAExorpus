# RESUME.md - Session Ledger
Repository: novae-xorpus
Last session: 2026-09-11

## STATUS: PHASES 1-4 COMPLETE ON novae-xorpus

### Phase 1: Ingestion - COMPLETE
- 585 files cleaned from raw_database/raw/, 02_MY_ORIGINALS/, and Dump/zip/
- 371 duplicates removed by SHA-256
- PDF extraction: mutool (mupdf). DOCX: python-docx. HTML: stdlib html.parser.
- Output: novae-xorpus/clean_md/ (585 .md files with YAML frontmatter)
- Tool: tools/clean.py

### Phase 2: RLVR Validation - COMPLETE
- Disjoint extractors: pypdf vs mutool, zipfile+xml.etree vs python-docx, BeautifulSoup vs html.parser
- 172 PASS, 407 WARN (duplicate copies with extractor differences), 6 FAIL (edge cases)
- Report: audit/rlvr_verification_report.md
- Tool: tools/check.py

### Phase 3: Chunking and Manifest - COMPLETE
- 3135 chunks in chunk.jsonl (2048-char chunks, 200 overlap)
- 585 entries in manifest.jsonl with SHA-256 checksums
- Tool: tools/chunk.py

### Phase 4: Living Wiki Population - COMPLETE
- 02_wiki_md/ populated with 592 documents across branches:
  - vendors/qualcomm: 160 docs
  - vendors/google: 123 docs
  - vendors/anthropic: 54 docs
  - vendors/github: 33 docs
  - concepts: 148 docs
  - architectures: 39 docs
  - entities: 18 docs
  - vendors/primeintellect: 6 docs
  - vendors/nvidia: 3 docs
  - references: 1 doc
- Index: 02_wiki_md/INDEX.md with wikilinks to all documents

## NOT YET DONE

### Other 6 Repos
novus-aexenti, novaexopia, aesop-xi, horizons-ui, novus-aesc, novus-aeyre
All still have POINTER.md stubs. Each needs its own ingestion pass.

### QNN-QAIRT SDK (3035 files)
Located in __RESUME.md/whatisit-/QNN-QAIRT/ - not yet ingested.

### canvas-ui-main (416 files)
Located in __RESUME.md/whatisit-/canvas-ui-main/ - not yet ingested.

### LlmWiki (259 files)
Working docs in LlmWiki/ - partially referenced but not fully ingested.

## ALL 6 MASTER SPECS CLEANED
Cross Agent Auditor, ECC, and Aider references removed from specs 00-05.
Specs are at novae-xorpus/ root:
- 00_DEFINITIVE_MASTER_SPECIFICATION_V3_COMPLETE.md
- 01_SOVEREIGN_NODE_AND_APK_TOPOLOGY.md
- 02_DUMBASS_UNIVERSAL_MEMORY_SPEC.md
- 03_DUAL_OPERATIONAL_HARNESS_AND_MCP_SPEC.md
- 04_ON_DEVICE_INGESTION_AND_W5H_FRAMEWORK.md
- 05_FEDERATED_FILE_TREE_TOPOLOGY_MASTER.md

## TOOLS
- tools/clean.py - ingestion (mutool for PDF, python-docx for DOCX)
- tools/check.py - RLVR (pypdf, zipfile+xml.etree, BeautifulSoup - disjoint from clean.py)
- tools/chunk.py - chunking and manifest cataloging
- mutool: /data/data/com.termux/files/usr/bin/mutool
- python3.14, pypdf, python-docx, beautifulsoup4, markdownify via pip
- pymupdf: cannot build on this platform

## ENVIRONMENT
- Device: Android aarch64, Termux, kernel 5.15
- This is the device filesystem, not GitHub
- Shell paths with special chars need python os.path.join
- Output with parentheses/numbers gets blanked in terminal - use code blocks
