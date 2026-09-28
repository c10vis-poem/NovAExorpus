# PDF → structured Markdown + JSONL chunks, without dropping text

**Research date:** 2026-08-20
**Target device:** Android aarch64 / Termux (CPython 3.14.6), proot Debian (CPython 3.13.5), no CUDA, limited RAM
**Question:** which extraction tool conserves every token of the source *while* adding real structure (headings, lists, tables, code fences, reading order)?

Sources are primary only: project source code, official docs, published specs, and read-only probes run on this device. Everything marked **[verified on-device]** was executed here; everything else is cited to a URL.

---

## 1. Bottom line

**Do not adopt a new extraction library. Build the markdown layer yourself on top of `PyMuPDF.get_text("dict")`, using the PDF outline (`doc.get_toc()`) for headings and `page.find_tables().to_markdown()` for tables, and emit JSONL shaped as `{"id", "text", "metadata"}` — a schema LangChain, LlamaIndex and Docling all trivially map onto.** I prototyped exactly this and measured it here: on all three real PDFs in this research folder the output is a **strict superset of `get_text()` — every non-whitespace character present, in order, ratio 1.0000–1.0650** — while recovering **20 of 20 outline headings and 10 tables** on the academic PDF. [verified on-device]

The reasoning: the conservation problem and the structure problem have different causes, and only the structure problem is hard here. `get_text()` is already lossless on this device; `pymupdf4llm` loses 13–52% not because PyMuPDF extracts less but because `to_markdown()` *deliberately skips* text lines that fall inside detected image/vector-graphic regions and inside table bounding boxes, then re-emits only what its table and image handlers manage to reconstruct — the drop is in the markdown assembler, not the extractor ([source, `pymupdf_rag.py:558-561`](#pymupdf4llm-where-the-tokens-go)). Every heavyweight alternative that would genuinely beat it on structure — Docling, marker, MinerU, unstructured `hi_res` — requires **torch, which has no wheel for Termux Python 3.14 at all** [verified on-device], pushing you into the proot container (torch 2.13 aarch64 = **427 MB wheel** [verified on-device]) plus hundreds of MB of model downloads, for CPU inference on a phone. **[Merge note, added by the coordinating session]** marker specifically has a second, independent disqualifier beyond the platform issue: its own issue tracker (`github.com/datalab-to/marker/issues/1081`, opened 2026-08-16, current release 2.0.0) documents its default mode fabricating a 58-word passage that was never in the source document while separately dropping a title and paragraph in the same run — detail in §3.4. Even with unlimited RAM and a working torch install, that's a reason to exclude marker specifically, not just a platform-availability problem shared with the others. That trade is only worth making if these documents actually contain structure the heuristic misses — and for two of the three test documents **they do not: they carry exactly one font, one font size, no outline, and their `.docx` twins carry zero paragraph styles** [verified on-device]. There is no structural signal in those files for *any* tool to find; a tool that emits headings for them is inventing them. So: own the assembler, keep the lossless extractor, and accept flat output for genuinely flat documents.

**Secondary recommendation for `.docx`/`.mht`:** handle these on separate paths, not through the PDF pipeline. `.docx` is a zip of XML with explicit `<w:pStyle w:val="Heading1">`, `<w:numPr>` and `<w:tbl>` markers — read them directly (stdlib `zipfile` + regex, or `python-docx`) and you get real structure for free, no ML. `.mht` is MIME-wrapped HTML: unpack with stdlib `email`, then convert with `markdownify` (already a dependency of the installed `markitdown`).

**[Merge note, added by the coordinating session, not the sub-agent pass above]** `pandoc` (3.10.1) and `python-docx` (1.2.0) are both already installed on this device [verified — `pandoc --version`, `pip show python-docx`], and `pandoc --list-input-formats` includes `docx`/`html` natively — a zero-install alternative to hand-rolled OOXML parsing for `.docx` specifically, not benchmarked against it here. Separately: this repo's own parent `CLAUDE.md` (`/data/data/com.termux/files/home/repos/NovA-Corpus/CLAUDE.md`) documents an **already-working, currently-used** `.mht` pipeline that differs from the one recommended above — it unpacks the MIME envelope with stdlib `email` (matching this file) but then runs the extracted HTML through **`trafilatura`**, not `markdownify`, specifically because "raw pandoc HTML conversion keeps nav/header chrome, trafilatura strips it." This is a genuine disagreement, not a rewrite: this file's `markdownify` recommendation is an untested design proposal (per §4 below); the parent repo's `trafilatura` pipeline is documented as already in production use for this exact vault. Both are named here rather than silently resolved in favor of one.

---

## 2. Comparison table

| Tool | Conserves all text? | Structure emitted | Native JSONL/chunks | Termux py3.14 | proot Debian py3.13 | License | Fully offline |
|---|---|---|---|---|---|---|---|
| **PyMuPDF `get_text("dict")` + DIY assembler** *(recommended)* | **Yes — strict superset verified on 3/3 docs** [verified] | Headings from PDF outline; tables via `find_tables()`; reading order = block/line order; code/lists = your rules | No — you write it (trivial) | **Installed, works** (1.28.0) [verified] | Same | AGPL-3.0 / commercial | **Yes**, no network at all |
| `pymupdf4llm.to_markdown()` | **No — 13% / 52% loss measured previously; skip-paths confirmed in source** | Headings (font-size or TOC), tables, code, multi-column | `page_chunks=True` → list of dicts (`metadata`, `toc_items`, `tables`, `images`, `graphics`, `text`, `words`) | Installed, works | Same | AGPL-3.0 / commercial | Yes |
| **Docling** | Not claimed lossless; no completeness guarantee in docs | Full: headings, lists, tables, code, figures, reading order | **Yes** — `DocChunk{text, meta}`, `DocMeta{schema_name, version, doc_items, headings, captions, origin}`; JSONL not built in | **No** — needs torch for layout/table models; **no torch wheel** [verified] | Yes — torch 427 MB + onnxruntime 20.8 MB + models [verified] | **MIT** | Yes, after `docling-tools models download` + `artifacts_path` |
| **marker** | No completeness claim; LLM-assisted modes can rewrite text | Full: headings, tables, lists, code, LaTeX equations, reading order | **Yes** — `chunk` renderer: `FlatBlockOutput{id, block_type, html, page, polygon, bbox, section_hierarchy, images}` | **No** — hard `torch>=2.7` dependency | Yes, but heavy (surya models) | Code Apache-2.0; **model weights modified OpenRAIL-M, free only under $5M funding/revenue** | Yes after model download |
| **MinerU** | 86.5–95.4 OmniDocBench accuracy (≠ conservation) | Full: headings w/ `text_level`, tables as **HTML**, formulas as **LaTeX**, reading order; *deliberately deletes headers/footers/page numbers* | **Yes** — `content_list.json`: `{type, text, text_level, bbox, page_idx, img_path, table_body}` | **No** — `requires-python = ">=3.10,<3.14"` | Yes (wheel resolves) [verified] but **16 GB RAM minimum documented** | Apache-2.0 **+ commercial threshold + mandatory attribution for online services** | Yes, local model mode documented |
| **unstructured** | `fast` = pdfminer.six; falls back to OCR when no extractable text | Element types (`Title`, `NarrativeText`, `ListItem`, `Table`…), not markdown-first | **Yes** — `Element.to_dict()` → `{type, element_id, text, metadata{...}}`; `chunk_by_title` | **No** — `requires-python = ">=3.11, <3.14"` | Yes; `[pdf]` extra needs `pikepdf`/`pi_heif` source builds | Apache-2.0 | Yes for `fast`; `hi_res` downloads models |
| `pypdf` | Flat text only | **None** — docs explicitly disclaim a semantic layer | No | Yes | Yes | BSD-3-Clause | Yes |
| `pdftotext -layout` / `-bbox-layout` | Column-aware text; bbox XHTML has per-word boxes | Whitespace layout, or word/line/block bboxes in XHTML — no semantic tags | No | **Installed** (poppler 26.02.0) [verified] | Yes | GPL-2/GPL-3 | Yes |
| `markitdown` | pdfplumber/pdfminer text | Weak: pipe tables from word alignment; no headings | No | Installed but **PDF path needs `pdfplumber` + `pdfminer-six`** — see §3.7 | Yes | MIT | Yes |

**[Merge note, added by the coordinating session]** The marker row's "No completeness claim; LLM-assisted modes can rewrite text" undersells it — its issue tracker shows the *default* (non-LLM) mode fabricating text outright, not just an LLM-assisted mode risking a rewrite. See §3.4 for the specific issue (`#1081`, 2026-08-16, marker 2.0.0).

---

## 3. Per-tool findings

### 3.1 PyMuPDF structured APIs — the recommended substrate

**Extraction modes.** `Page.get_text(option)` returns different structures per option ([Page.get_text docs](https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_text), [Appendix 1: Text extraction](https://pymupdf.readthedocs.io/en/latest/app1.html)):

| Option | Returns | Fields |
|---|---|---|
| `"text"` | `str` | plain text, `\n` separated — the current lossless baseline |
| `"blocks"` | `list[tuple]` | `(x0, y0, x1, y1, "lines in block", block_no, block_type)` |
| `"words"` | `list[tuple]` | `(x0, y0, x1, y1, "word", block_no, line_no, word_no)` |
| `"dict"` | `dict` | **block:** `type` (0=text, 1=image), `bbox`, `lines`; **line:** `wmode`, `dir`, `bbox`, `spans`; **span:** `text`, `font`, `size`, `flags`, `color`, `bbox`, `origin` |
| `"rawdict"` | `dict` | same as `"dict"` but span `text` → `chars`, each `{c, bbox, origin}` |
| `"xhtml"` | `str` | text + images, **`<div>`/`<p>` only** — no `<h1>`–`<h6>` [verified on-device] |
| `"html"` | `str` | styled HTML with font/position info |
| `"xml"` | `str` | character-level with `quad` attributes inside `<font>` elements |

**This is the key point for heading inference:** `"dict"` gives you `size`, `font`, `flags` and `bbox` per span — exactly the inputs `pymupdf4llm` uses. `"xhtml"` does **not** give you headings, so it is not a shortcut. [verified on-device: `get_text("xhtml")` on `mote july 5th genini.pdf` p1 emitted only `div` and `p` tags]

**Tables.** `Page.find_tables()` returns a `TableFinder`; each `Table` exposes `extract()` (list of list of cell strings), `to_markdown()` ("returns the table as a string in markdown format (compatible to Github)"), `to_pandas()`, `header`, `bbox`, `cells`, `row_count`, `col_count`. Strategies: `"lines"` (default, uses vector graphics as grid lines), `"lines_strict"` (ignores borderless rectangles), `"text"` (virtual boundaries from text positions), with separate `vertical_strategy`/`horizontal_strategy` ([table docs](https://pymupdf.readthedocs.io/en/latest/page.html#Page.find_tables)). *Unverified:* the docs I read do not credit pdfplumber for the algorithm; I could not confirm the lineage from primary sources.

**Measured structural signal in the actual corpus** [verified on-device, all 3 PDFs in this folder]:

| Document | Pages | `get_text()` chars | Distinct font sizes | Fonts | Tables found | Outline (TOC) entries |
|---|---|---|---|---|---|---|
| `Copy of FraQAT Doc..pdf` | 16 | 48,287 | 10.0 / 10.1 / 9.9 / 4.8 / 7.7 / 9.0 | NimbusRomNo9L-Regu, -Medi, CMTT10/9 | 10 | **20** |
| `mote july 5th genini.pdf` | 5 | 10,529 | **11.0 only** | **ArialMT only** | 0 | **0** |
| `ookLm Planning query .pdf` | 16 | 41,013 | **11.0 only** | **ArialMT only** | 0 | **0** |

Two of three documents have **no typographic and no outline signal whatsoever**. Font-size heading inference is mathematically incapable of producing a heading on them. Their `.docx` counterparts are equally bare: zero `<w:pStyle>`, zero `<w:numPr>`, zero `<w:tbl>`, zero `<w:b/>`, zero `<w:sz>`, and no `docProps/app.xml` (i.e. not authored by Word or Google Docs — they are themselves converter output). [verified on-device]

**Prototype result.** A reconstruction that walks `get_text("dict")` block→line→span, tags a line as `#`×level when it matches a `doc.get_toc()` entry for that page, and appends `Table.to_markdown()` per detected table [verified on-device]:

| Document | baseline non-ws chars | reconstruction non-ws | ratio | strict superset? | real headings |
|---|---|---|---|---|---|
| `Copy of FraQAT Doc..pdf` | 40,814 | 43,466 | 1.0650 | **True** | **20 / 20** |
| `mote july 5th genini.pdf` | 8,809 | 8,809 | 1.0000 | **True** | 0 (no TOC exists) |
| `ookLm Planning query .pdf` | 33,338 | 33,338 | 1.0000 | **True** | 0 (no TOC exists) |

"Strict superset" = every non-whitespace character of `get_text()` appears, in order, in the markdown. Ratio >1 on FraQAT is table cell text being emitted twice (once in body flow, once in the markdown table) plus pipe characters — additive, never subtractive. This is the property the requirement asks for, and it holds because the assembler never has a `continue` that discards a line.

**[Merge note, added by the coordinating session]** Independently re-tested on a *different* pair of documents, outside this research folder — `corpus/raw/src-001.pdf` and `src-002.pdf`: `get_text("dict")` span text is byte-identical to `get_text()` after whitespace normalization, **57,021 and 4,344 non-whitespace characters, delta zero on both**. `src-001.pdf` also yields **39 tables** via `find_tables()`. [verified — main coordinating session, distinct from the 3-document prototype test above] This corroborates the strict-superset property on a second, independent document set rather than resting on the 3-document sample alone.

**License:** PyMuPDF is **AGPL-3.0 or commercial** ([PyMuPDF licensing](https://pymupdf.readthedocs.io/en/latest/about.html#license-and-copyright)) — the most restrictive item in the recommended stack. Flag this if the corpus tooling is ever distributed as a service. **Offline:** total, no network path exists.

### 3.2 pymupdf4llm — where the tokens go {#pymupdf4llm-where-the-tokens-go}

Read from the installed source at `/data/data/com.termux/files/usr/lib/python3.14/site-packages/pymupdf4llm/helpers/pymupdf_rag.py` (v1.28.0) [verified on-device], mirrored at [github.com/pymupdf/RAG](https://github.com/pymupdf/RAG).

Confirmed text-discarding paths, which explain the previously measured 13% / 52% loss:

1. **`pymupdf_rag.py:558-561`** — inside `write_text()`:
   ```python
   for lrect, spans in nlines:
       # there may be tables or images inside the text block: skip them
       if not outside_all_bboxes(lrect, parms.img_rects):
           continue
   ```
   Any text line overlapping an image **or vector-graphic cluster** rectangle is dropped outright. `parms.img_rects` is extended with `vg_clusters0` (line ~1163), so decorative vector art that happens to overlap prose silently eats that prose. Recovery only happens if the image-pickup branch later re-runs `write_text` with `force_text=True` on that rect — and only for images picked up *above* a surviving text block.
2. **`pymupdf_rag.py:547-549`** — lines inside table bboxes are filtered out of `nlines` and re-emitted only via `Table.to_markdown()`. Whatever the table extractor fails to place in a cell is gone.
3. **`column_boxes(..., avoid=parms.tab_rects0 + parms.vg_clusters0, footer_margin=margins[3], header_margin=margins[1])`** (line ~1185) — text regions are computed *excluding* table and graphics areas. (`margins=0` is the default, so header/footer trimming is off unless requested.)
4. **`img_info = img_info[:30]`** (line ~1071) — "only accept the largest up to 30 images"; with `force_text`, text riding on images beyond the 30th is not recovered.

**No configuration flag fixes this in general.** `ignore_images=True` / `ignore_graphics=True` prevent images being *written*, but the line-skip at 558-561 keys off `parms.img_rects`, and `force_text=True` (already the default) only partially recovers. Note also `fontsize_limit=3` is accepted and assigned to `FONTSIZE_LIMIT` (line 407) but **never read anywhere in the module** in this version — a dead parameter. [verified on-device]

**[Merge note, added by the coordinating session — confirms the above from the public docs page, independent of the source read]** `pymupdf4llm`'s own API docs ([pymupdf4llm API reference](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/api.html)) list `write_images` (default `False`), `image_size_limit` (default `0.05` — images below this page-fraction are dropped), `margins` (default `0`, full page), and `table_strategy` (default `"lines_strict"`) as the only content-affecting parameters, and document no combination as a "preserve everything" mode; the page makes no completeness claim for `to_markdown()` in either direction. Consistent with the source-level finding above, from the documentation side rather than the code side.

Heading logic, for reference, is `IdentifyHeaders` (line 86): it counts characters per rounded font size across the document, takes the most frequent size as body text, then maps up to 6 larger sizes to `#`…`######`. `TocHeaders` (line 176) is the alternative that uses `doc.get_toc()` levels — **this is the one that works on real documents**, and is what my prototype adopts.

**Chunk output:** `to_markdown(page_chunks=True)` returns a list of dicts with keys `metadata`, `toc_items`, `tables`, `images`, `graphics`, `text`, `words` (line 1302-1311). Usable as JSONL, but inherits the loss.

### 3.3 Docling (IBM)

- **License: MIT** ([pyproject.toml](https://github.com/docling-project/docling/blob/main/pyproject.toml)) — cleanest license of any full-featured option.
- **Base install is genuinely light:** 8 dependencies — `pydantic`, `docling-core`, `pydantic-settings`, `filetype`, `requests`, `certifi`, `pluggy`, `tqdm`. **torch is *not* a core dependency**; it lives in the `models-local` extra alongside `torchvision`, `docling-ibm-models`, `accelerate`, `huggingface_hub`. OCR engines (`rapidocr`, `easyocr`, `tesserocr`, `ocrmac`) and `onnxruntime<1.24` are also extras. ([pyproject.toml](https://github.com/docling-project/docling/blob/main/pyproject.toml))
- **But the PDF pipeline's layout and table-structure models are torch models** from `docling-ibm-models`. Without them you do not get Docling's structure — which is the entire reason to use it. *Unverified:* I did not confirm from primary sources whether a torch-free PDF configuration exists that still produces headings and tables; the docs I read do not describe one.
- **[Merge note, added by the coordinating session — this resolves the question immediately above, and the one flagged in §4 as "the single most decision-relevant open question."]** No torch-free PDF path exists, confirmed by reading Docling's pipeline source directly rather than the docs: `docling/pipeline/simple_pipeline.py` ([source](https://raw.githubusercontent.com/docling-project/docling/main/docling/pipeline/simple_pipeline.py)) shows `SimplePipeline` — the one pipeline class that builds a `DoclingDocument` with no model at all — is explicitly restricted to `DeclarativeDocumentBackend` subclasses ("used at the moment for formats/backends which produce straight DoclingDocument output," direct quote from the class docstring). `PyPdfiumDocumentBackend` (the lightweight PDF backend) is not one of those — it extends `ManagedPdfiumDocumentBackend`, confirmed by reading `docling/backend/pypdfium2_backend.py` directly. So PDF input always routes through `StandardPdfPipeline`, and `docling/datamodel/pipeline_options.py`'s `PdfPipelineOptions` class exposes `do_ocr` and `do_table_structure` toggles but **no toggle to skip layout analysis** — the torch-based layout model is not optional for any PDF conversion in Docling, full stop, regardless of which PDF backend opens the file. Separately: `pypdfium2` itself (the PDF-opening backend, as opposed to the layout model) *does* publish a native Termux wheel — `pypdfium2-5.13.0-py3-none-android_23_arm64_v8a.whl`, confirmed via direct PyPI JSON inspection — so the reason Docling can't structure a PDF on Termux is the layout model specifically, not an inability to open the file at all.
- **[Merge note, added by the coordinating session]** The "no completeness or conservation claim found" line two bullets below is accurate for the docs, but Docling's own **issue tracker directly contradicts a lossless impression in practice** — checked directly, all open at time of writing: #3858 (`export_to_markdown()` embeds NUL bytes for superscript unit/exponent glyphs, "causing silent truncation downstream"), #2846 ("All layout models produce empty markdown output with no text content"), #3409 (DocLayNet misclassifies a structured table region as picture, "content entirely lost"), #1225 ("Missing text while parsing a PDF"), #585 (link URLs lost during parsing), #3671 (large PDFs fail silently with `std::bad_alloc` on some pages), #3839 (OCR text dropped for 180°-rotated images even with `force_full_page_ocr`) — all at `github.com/docling-project/docling/issues/{3858,2846,3409,1225,585,3671,3839}`. Not independently re-measured on this device; this is issue-tracker evidence of a reported-failure pattern, not a completeness percentage.
- **Chunking schema — confirmed from source** ([docling-core `chunker/base.py`](https://github.com/docling-project/docling-core/blob/main/docling_core/transforms/chunker/base.py), [`chunker/doc_chunk.py`](https://github.com/docling-project/docling-core/blob/main/docling_core/transforms/chunker/doc_chunk.py)):
  ```python
  class BaseChunk(BaseModel):
      text: str
      meta: BaseMeta

  class DocMeta(BaseMeta):
      schema_name: Literal["docling_core.transforms.chunker.DocMeta"]
      version: str
      doc_items: list[DocItem]          # min_length=1
      headings: Optional[list[str]]
      captions: Optional[list[str]]     # deprecated
      origin: Optional[DocumentOrigin]

  class DocChunk(BaseChunk):
      meta: DocMeta
  ```
  `HierarchicalChunker` "uses the document structure information from the `DoclingDocument` to create one chunk for each individual detected document element, by default only merging together list items"; `HybridChunker` post-processes that with a tokenizer, splitting oversized chunks and merging undersized ones ([chunking concepts](https://docling-project.github.io/docling/concepts/chunking/)). **`headings` on every chunk is exactly the RAG metadata you want** — the strongest argument for Docling.
  **No built-in JSONL writer** — serialization is left to the caller (`chunk.model_dump_json()` per line is one obvious mapping). *Unverified:* I found no primary-source JSONL example.
- **Offline: fully supported and well documented.** `docling-tools models download` prefetches; then `PdfPipelineOptions(artifacts_path="/local/path/to/models")`, or `docling --artifacts-path=...`, or `DOCLING_ARTIFACTS_PATH`. Docs state that "by default, Docling runs entirely locally without transmitting user data to external services" and remote APIs require explicit `enable_remote_services=True` ([advanced options](https://docling-project.github.io/docling/usage/advanced_options/)).
- **Lossiness:** I found **no completeness or conservation claim** in Docling's documentation either way. *Unverified.*
- **Device viability:** `docling` and `docling-core` wheels resolve on Termux py3.14 [verified on-device], but `torch` does not exist for this platform at all [verified: `pip download --no-deps torch` → "from versions: none"]. In proot Debian py3.13, `torch 2.13.0 manylinux_2_28_aarch64` (427 MB), `onnxruntime 1.29.0 aarch64` (20.8 MB), `docling-ibm-models 3.14.0`, `easyocr`, `rapidocr` all resolve [verified on-device]. So Docling is a **proot-only** option, and an expensive one on RAM.

### 3.4 marker (Datalab)

- **License — the important detail.** The repo `LICENSE` is stock **Apache-2.0**, 202 lines, verbatim ([LICENSE](https://github.com/datalab-to/marker/blob/master/LICENSE)), and `pyproject.toml` declares `license = { text = "Apache-2.0" }`. The restriction is on **model weights, not code**. From the README verbatim ([README.md](https://github.com/datalab-to/marker/blob/master/README.md)):
  > "Our code is licensed under **Apache 2.0** — free to use, including commercially. Our model weights use a modified AI Pubs Open Rail-M license (free for research, personal use, and startups under $5M funding/revenue). For commercial use of the model weights beyond that, visit our pricing page"

  The README badges it as `Model License: OpenRAIL-M`. **Since marker is useless without its weights, the OpenRAIL-M threshold is the operative constraint.**
- **Dependencies** ([pyproject.toml](https://github.com/datalab-to/marker/blob/master/pyproject.toml)): hard `torch>=2.7.0,<3`, `transformers>=5.12.1`, `surya-ocr>=0.22.1`, `pdftext`, `markdownify`, `scikit-learn`, plus `google-genai`, `anthropic`, `openai` clients as **core** dependencies (LLM-assisted modes). `requires-python = ">=3.10,<4"`.
- **Chunk output schema — confirmed from source** ([`marker/renderers/chunk.py`](https://github.com/datalab-to/marker/blob/master/marker/renderers/chunk.py)):
  ```python
  class FlatBlockOutput(BaseModel):
      id: str
      block_type: str
      html: str
      page: int
      polygon: List[List[float]]
      bbox: List[float]
      section_hierarchy: Dict[int, str] | None = None
      images: dict | None = None

  class ChunkOutput(BaseModel):
      blocks: List[FlatBlockOutput]
      page_info: Dict[int, dict]
      metadata: dict
  ```
  and the nested JSON renderer ([`marker/renderers/json.py`](https://github.com/datalab-to/marker/blob/master/marker/renderers/json.py)) uses `JSONBlockOutput{id, block_type, html, polygon, bbox, children, section_hierarchy, images}`. Renderers available: `chunk`, `html`, `json`, `markdown`, `ocr_json`. **`section_hierarchy` is a first-class field** — good RAG metadata. Note chunk content is **HTML**, not markdown.
- **Conservation:** no conservation claim located; and marker's optional LLM modes actively *rewrite* content, which is the opposite of conservation. *Unverified:* I did not audit marker's issue tracker for dropped-text reports.
- **[Merge note, added by the coordinating session — this is the single most decision-relevant finding in the whole document and was missing entirely from the pass above, which explicitly flagged the issue tracker as unaudited.]** marker's issue tracker was checked directly. It shows marker's default mode doing something worse than dropping text: **inventing it.** A live, open issue — **#1081**, opened 2026-08-16 against marker 2.0.0 (`github.com/datalab-to/marker/issues/1081`) — documents the default "balanced" mode weaving a deterministic **58-word fabricated passage** into the transcription of a bleed-through page ("Marker's output weaves the ghost text into the transcription and degenerates into a loop," direct quote from the issue), while on a separate clean page in the *same run* it silently drops a title and a final paragraph. Additional open reports of dropped (not fabricated) content, same tracker: **#1071** (`filter_blank_lines` silently deletes a paragraph's short final line), **#1072** (`MarginaliaProcessor` deletes body text on PDFs with a non-zero CropBox origin), **#860** (embedded hyperlinks lost), **#988**, **#556**, **#471** (further dropped/missing-text reports) — all at `github.com/datalab-to/marker/issues/{1071,1072,860,988,556,471}`. The only mode with a plausible no-fabrication argument is `--disable_ocr` (pure text-layer extraction, no VLM/inference-server calls per the README) — but it also skips equations and scanned pages, and no primary source claims that mode is complete either. This directly answers the "conservation" question two bullets above: not unverified, and not just non-lossless — actively worse than dropping, on the current release, this month.
- **Device viability: no.** `torch` is unavailable on Termux py3.14 [verified on-device]; the surya model stack on CPU on a phone is not a serious proposition.

### 3.5 MinerU (OpenDataLab)

- **License: Apache-2.0 + additional terms** ([LICENSE.md](https://github.com/opendatalab/MinerU/blob/master/LICENSE.md), read verbatim). Quoting:
  > "if you and your Affiliates, on a consolidated basis, meet either of the following thresholds, you must obtain a separate commercial license … a. monthly active users (MAU) exceed 100 million; or b. total monthly revenue exceeds USD 20 million."

  > "If you provide online services to third parties based on MinerU, you must clearly and prominently indicate, in the relevant product or service interface or in publicly available documentation, that MinerU is used."

  Termination is automatic and without notice if either clause is breached. The thresholds are irrelevant at this scale; **the attribution obligation is not** if this ever fronts an online service.
- **`requires-python = ">=3.10,<3.14"`** ([pyproject.toml](https://github.com/opendatalab/MinerU/blob/master/pyproject.toml)) — **excludes Termux's Python 3.14 by declaration.** Core deps are light-ish (`pypdfium2`, `pypdf`, `pdftext`, `modelscope`, `huggingface-hub`, `opencv-python`, `magika`, `mineru-vl-utils`…), but the `pipeline` extra pulls `torch>=2.6`, `torchvision`, `transformers`, `onnxruntime`; `vlm` pulls `torch` + `accelerate`; `vllm`/`lmdeploy`/`mlx` are the other backends.
- **Documented hardware floor: 16 GB RAM minimum** for all backends; VRAM 4 GB (pipeline) / 8 GB (hybrid, vlm); GPU support limited to "Volta and later architecture GPUs or Apple Silicon"; pipeline backend explicitly supports "pure CPU" ([README](https://github.com/opendatalab/MinerU/blob/master/README.md)). **No ARM/aarch64 statement anywhere in the README.**
- **Output schema — well documented** ([output files reference](https://opendatalab.github.io/MinerU/reference/output_files/)): `content_list.json` records carry `type` (one of image, table, chart, text, equation, code, list, header, footer, page_number, aside_text, page_footnote), `page_idx` (0-based), `bbox` normalised to 0–1000, plus `text` and **`text_level`** (0 = body, 1+ = heading depth), `img_path`, `table_body` (HTML). Example record from the docs: `{"type": "text", "text": "The response of flow duration curves to afforestation", "text_level": 1, "bbox": [62, 480, 946, 904], "page_idx": 0}`. Also emits `middle.json` (`pdf_info` → per-page `para_blocks` → `lines` → `spans`) and `model.json` (raw detections: `cls_id`, `label`, `score`, `bbox`, `index`).
- **Structure:** reading order for single/multi-column, headings/paragraphs/lists preserved, **formulas → LaTeX**, **tables → HTML**. Accuracy on OmniDocBench v1.6: pipeline 86.47, hybrid 95.39/95.26, VLM 95.30.
- **Conservation — a documented anti-feature:** the README lists as a capability "Remove headers, footers, footnotes, page numbers, etc." That is **deliberate, by-design text deletion**. For a conservation-first pipeline this disqualifies MinerU's default behaviour regardless of platform. *Unverified:* whether that removal can be disabled by configuration.
- **Wheel does resolve** in proot Debian py3.13 (`mineru-3.4.5-py3-none-any.whl`) [verified on-device], but the 16 GB RAM floor makes it a non-starter on this device.
- **[Merge note, added by the coordinating session]** MinerU's unconditional base dependencies (reading `pyproject.toml`'s `[project.dependencies]` directly) already include `python-docx`, `mammoth`, `pypptx-with-oxml`, and `openpyxl` — it's explicitly a `.docx`/`.pptx`/`.xlsx` converter too, per its own PyPI description ("A practical document parsing tool for converting PDF, images, DOCX, PPTX, and XLSX into Markdown and JSON"), relevant to this file's secondary `.docx` question — but the `requires-python <3.14` ceiling above blocks all of it on Termux regardless of which conversion path is intended. Separately, MinerU's own docs ship a `span.pdf` debug-visualization file (pipeline backend) described as existing specifically to "quickly troubleshoot text loss issues... verify text segmentation accuracy" ([output_files.md](https://raw.githubusercontent.com/opendatalab/MinerU/master/docs/en/reference/output_files.md)) — a softer signal than the header/footer-removal anti-feature above, but another instance of the project's own tooling being built around the expectation that text gets lost.

### 3.6 unstructured

- **License: Apache-2.0** (`license = "Apache-2.0"` in [pyproject.toml](https://github.com/Unstructured-IO/unstructured/blob/main/pyproject.toml)).
- **`requires-python = ">=3.11, <3.14"` — excludes Termux Python 3.14 by declaration.** (The bare `unstructured` wheel still downloads on py3.14 [verified on-device] because it is `py3-none-any`, but the metadata bound and the base deps `numba`/`spacy` make it unsupported.)
- **Element model — confirmed from source** ([`unstructured/documents/elements.py`](https://github.com/Unstructured-IO/unstructured/blob/main/unstructured/documents/elements.py)): abstract `Element` with `category = "UncategorizedText"`; `Text(Element)` subclasses include `Title`, `NarrativeText`, `ListItem`, `Formula`, `FigureCaption`, `Form`, `Address`, `EmailAddress`, `CompositeElement`, plus `CheckBox`. Serialization is:
  ```python
  def to_dict(self) -> dict[str, Any]:
      return {"type": None, "element_id": self.id, "text": self.text, "metadata": self.metadata.to_dict()}
  ```
  `element_id` is a SHA-256 of `filename + text + page_number + sequence_number`, truncated to 32 chars (or a UUID with `unique_element_ids=True`). `ElementMetadata` declares among others: `category_depth`, `coordinates`, `page_number`, `parent_id`, `filename`, `filetype`, `languages`, `link_texts`, `link_urls`, `text_as_html`, `is_continuation`, `orig_elements`, `detection_class_prob`, `detection_origin`. **`parent_id` + `category_depth` are how hierarchy is expressed** — there is no `headings` list like Docling's.
- **`partition_pdf` strategies** ([partitioning docs](https://docs.unstructured.io/open-source/core-functionality/partitioning)): `"fast"` — "extract the text using `pdfminer` and process the raw text with `partition_text`"; `"hi_res"` — "identify the layout of the document using `detectron2_onnx`"; `"ocr_only"` — Tesseract then `partition_text`; `"auto"` — picks per document, defaulting to `fast` for text-extractable PDFs. Documented failure mode: "If the PDF text is not extractable, `partition_pdf` will fall back to `ocr_only`."
- **Is `fast` lossless?** It is pdfminer.six text, so it is text-complete for text-bearing PDFs — but its *structure* is `partition_text` heuristics over a flat string, which is barely better than `get_text()`. The docs recommend `hi_res` "if your use case is highly sensitive to correct classifications" and `ocr_only` for multi-column documents without extractable text. So **the cheap strategy has weak structure and the strong strategy needs models** — the same trade as everywhere else. *Unverified:* no primary-source statement quantifying text loss for any strategy.
- **Dependency cost** (from [pyproject.toml](https://github.com/Unstructured-IO/unstructured/blob/main/pyproject.toml)): `pdf` is an alias for `image`, which is `google-cloud-vision`, `pdf2image`, `pdfminer.six`, `pi-heif`, `pikepdf`, `pypdf`, `unstructured-inference`, `unstructured-pytesseract`. Note `pikepdf` and `pi_heif` have **no aarch64 wheels for py3.14 and fall back to source builds** [verified on-device: both downloaded as `.tar.gz`, requiring a compiler and qpdf]. torch is only in the `huggingface` extra. Also note `paddleocr` extra explicitly excludes aarch64: `platform_machine != 'aarch64'`.
  - **[Merge note, added by the coordinating session]** `unstructured-inference` (the `hi_res` layout-model package) has its own, separate PyPI-declared `requires_python: <3.14,>=3.11` — confirmed via the PyPI JSON API's `info.requires_python` field directly — so `hi_res` is blocked on Termux by version ceiling as well as by torch/onnxruntime wheel unavailability; two independent reasons, not one. Separately, the underlying primitives `fast`/`ocr_only` actually depend on — `pdfminer.six`, Tesseract, `pytesseract`, `pdf2image`/`pdftoppm` — are each individually present or installable on this exact device (Termux ships a native `tesseract` package; `pdftoppm`/`pdfinfo` are already installed via poppler-utils; `pytesseract`/`pdf2image` are pure-Python with `pip index` entries) — but `pdfminer.six`'s own import chain is broken here via the `cryptography` ABI break documented in §3.7, which would sink `fast`/`auto`/`ocr_only`'s text-extraction step even if the packaging-level `pip install unstructured[pdf]` failure above were somehow worked around.
- **No markdown export** — unstructured is element/JSON-first; markdown would be yours to write anyway, which removes most of its appeal here.

### 3.7 markitdown — why it fails on this device

The installed `markitdown` 0.1.7 fails on PDFs with `MissingDependencyException`. **Root cause confirmed by reading the installed source** at `.../site-packages/markitdown/converters/_pdf_converter.py` [verified on-device]:

```python
try:
    import pdfminer
    import pdfminer.high_level
    import pdfplumber
except ImportError:
    _dependency_exc_info = sys.exc_info()
```

`PdfConverter.convert()` raises `MissingDependencyException` if *either* import failed. It needs **both `pdfminer.six` and `pdfplumber`** — and `pdfplumber` is the one that is ABI-broken on Python 3.14 here. Confirmed against package metadata: the `pdf` extra is `["pdfminer-six>=20251230", "pdfplumber>=0.11.9"]` [verified on-device via `importlib.metadata`]. So installing `pdfminer.six` alone can never satisfy it.

**[Merge note, added by the coordinating session — traces the "pdfplumber is ABI-broken" fact one layer deeper, does not contradict it]** Tested directly, independent of the above: `pip show pdfminer.six` confirms it's installed (v20260107) with a valid `INSTALLED` line, but `python3 -c "from pdfminer.high_level import extract_text"` fails on its own, before pdfplumber even enters the picture, with a full traceback ending in:
```
File ".../pdfminer/pdfdocument.py", line 14, in <module>
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
File ".../cryptography/hazmat/primitives/ciphers/base.py", line 10, in <module>
    from cryptography.hazmat.bindings._rust import openssl as rust_openssl
ImportError: dlopen failed: cannot locate symbol "PyLong_Type" referenced by
".../cryptography/hazmat/bindings/_rust.abi3.so"...
```
The chain: `pdfminer.high_level` → `pdfminer.pdfdocument` → `cryptography.hazmat.primitives.ciphers` → `cryptography`'s compiled Rust extension (`_rust.abi3.so`, from `cryptography` v50.0.0 as installed here) → that extension can't resolve `PyLong_Type` on this Python 3.14/Android build and fails to load. This is a **`cryptography` binary-ABI break on Termux Python 3.14**, not a markitdown bug and not really "missing" pdfminer.six either — it's installed, it just can't finish importing. Since `pdfplumber` is itself built on `pdfminer.six` internally, it almost certainly fails at this identical import for the identical reason — meaning this one broken binary plausibly explains *both* markitdown's failure *and* the "pdfplumber is ABI-broken" fact stated above, one root cause underneath both, not two separate ones. Not fixable by installing more of markitdown's own extras; would need a `cryptography` build that actually matches this Python/platform's ABI, which was not found or tested.

Worth knowing even if you fix that: the converter's primary path is a hand-rolled word-position clusterer (`_extract_form_content_from_words`) that emits pipe tables, and it **falls back to `pdfminer.high_level.extract_text` for the whole document whenever no page looks form-like** (`if form_page_count == 0`). It produces **no headings at all**. Its `_to_markdown_table` also drops empty rows (`table = [row for row in table if any(cell.strip() for cell in row)]`). Not a conservation-first tool.

### 3.8 pypdf

`extract_text(extraction_mode="layout")` produces "text in a fixed width format that closely adheres to the rendered layout in the source pdf", tunable with `layout_mode_space_vertically`, `layout_mode_scale_weight`, `layout_mode_strip_rotated` ([extract-text docs](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)). The docs disclaim structure explicitly:

> "PDF files don't contain a semantic layer. Specifically, there is no information what the header, footer, page numbers, tables, and paragraphs are."

Visitor functions expose positioning, not semantics. **No structure extraction — not a candidate**, though it's a reasonable second opinion for conservation cross-checks.

### 3.9 poppler `pdftotext`

Already installed: **poppler 26.02.0** [verified on-device]. Flag semantics from the binary's own help output [verified on-device, `pdftotext -h`]:

```
-layout              : maintain original physical layout
-fixed <fp>          : assume fixed-pitch (or tabular) text
-raw                 : keep strings in content stream order
-tsv                 : generate a simple TSV file, including the meta information for bounding boxes
-bbox                : output bounding box for each word and page size to html. Sets -htmlmeta
-bbox-layout         : like -bbox but with extra layout bounding box data.  Sets -htmlmeta
-colspacing <fp>     : how much spacing we allow after a word before considering adjacent text to be
                       a new column, as a fraction of the font size (default is 0.7, ...)
```

So `-bbox` gives per-word boxes in XHTML; `-bbox-layout` adds the layout hierarchy (block/line grouping) on top. Useful as an **independent conservation oracle** — a second engine to diff against PyMuPDF — and `-colspacing` makes its column detection tunable. But no font-size or semantic information, so it cannot drive heading inference. Note poppler is GPL.

### 3.10 JSONL chunk schemas — what actually exists

There is **no formal cross-project JSONL standard**. What exists is three well-defined in-memory record types, all of which reduce to *text + a metadata dict + an id*:

**Docling** ([source](https://github.com/docling-project/docling-core/blob/main/docling_core/transforms/chunker/doc_chunk.py)): `BaseChunk{text, meta}` / `DocMeta{schema_name, version, doc_items, headings, captions(deprecated), origin}`. `DocMeta` also declares `excluded_embed` and `excluded_llm` class-vars naming fields to omit when serializing for embedding/LLM. Richest structural metadata of the three (`headings` is a list of ancestor headings). No built-in JSONL writer. **[Merge note, added by the coordinating session]** This embed/LLM-exclusion split is worth flagging as a validated pattern, not an idiosyncrasy: LlamaIndex (below) independently implements the identical concept under different names (`excluded_embed_metadata_keys`/`excluded_llm_metadata_keys`) — two unrelated projects converging on the same design, not one copying the other.

**LlamaIndex** ([`llama-index-core/llama_index/core/schema.py`](https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/schema.py)): `TextNode` carries `id_`, `text`, `mimetype`, `metadata`, `embedding`, `excluded_embed_metadata_keys`, `excluded_llm_metadata_keys`, `relationships`, `start_char_idx`, `end_char_idx`, `text_template`, `metadata_template`, `metadata_separator`. `NodeRelationship` enum: `SOURCE`, `PREVIOUS`, `NEXT`, `PARENT`, `CHILD`. `Document` extends `Node` and exposes backward-compatible `text`, `doc_id` (→ `id_`), `extra_info` (→ `metadata`) properties; current storage is `text_resource`/`image_resource`/`audio_resource`/`video_resource` as `MediaResource`. **`PREVIOUS`/`NEXT`/`PARENT` is the most expressive chunk-graph model of the three.**

**LangChain** ([`libs/core/langchain_core/documents/base.py`](https://github.com/langchain-ai/langchain/blob/master/libs/core/langchain_core/documents/base.py)):
```python
class Document(BaseMedia):
    page_content: str
    type: Literal["Document"] = "Document"
```
with `id: str | None` and `metadata: dict` inherited from `BaseMedia`. Note the field is **`page_content`, not `text`** — the single most common integration mistake.

**unstructured** ([source](https://github.com/Unstructured-IO/unstructured/blob/main/unstructured/documents/elements.py)): `{type, element_id, text, metadata{...}}` per `Element.to_dict()`.

**Recommended emission schema**, chosen because it maps to all four with a one-line adapter:
```json
{"id": "<doc>#p3#b12", "text": "...", "metadata": {"source": "...", "page": 3, "headings": ["A", "A.2"], "block_type": "paragraph", "bbox": [x0,y0,x1,y1], "prev_id": "...", "next_id": "..."}}
```
`text` → LangChain `page_content`, LlamaIndex `TextNode.text`, Docling `DocChunk.text`; `metadata.headings` mirrors `DocMeta.headings`; `prev_id`/`next_id` mirror `NodeRelationship.PREVIOUS/NEXT`.

---

## 4. What is unverified

Stated plainly, because a wrong confident claim costs more here than a gap.

**[Merge note, added by the coordinating session]** This file was assembled from two passes: an initial sub-agent pass (everything above this note originally, including this §4 list as first written) and a merge pass by the coordinating session that added on-device re-verification, resolved some of the open items below, and added findings the first pass didn't reach (notably marker's issue-tracker fabrication report, a deeper root cause for the markitdown/pdfplumber failure, and a source-level resolution of the Docling torch-free-path question). Items resolved by the merge are marked **(resolved in merge)** below rather than deleted, so the original open question is still visible next to its answer.

**Not verified from primary sources:**
- ~~Whether Docling can produce headings/tables from PDFs **without** torch.~~ **(resolved in merge, §3.3)** — no, confirmed from Docling's own pipeline source: `SimplePipeline` (the no-model path) only accepts declarative backends, PDF backends aren't declarative, and `PdfPipelineOptions` has no toggle to skip layout analysis. This *was* "the single most decision-relevant open question" as originally written; the answer doesn't change the Bottom Line recommendation, it just removes the uncertainty behind it.
- Whether MinerU's header/footer/page-number **removal can be disabled**. It is advertised as a feature; I found no config flag in the sources I read. **Still open** — not addressed in the merge pass either.
- Whether PyMuPDF's `find_tables()` derives from pdfplumber's algorithm. The docs I read make no attribution. **Still open.**
- Whether any primary source publishes a **JSONL** example as an official export format. I found none — the `{"id","text","metadata"}` line format above is my synthesis from the three schemas, not a cited standard. Do not treat it as one. **Still open** — the merge pass added a cross-schema observation (Docling/LlamaIndex's convergent embed/LLM-exclusion split, §3.10) but did not find a JSONL-specific standard either.
- ~~Docling's, marker's, and unstructured's **issue trackers were not searched** for dropped-text reports.~~ **(partially resolved in merge)** — Docling's and marker's issue trackers were checked directly in the merge pass (§3.3, §3.4); marker's shows active text fabrication, not just dropping. **unstructured's and MinerU's issue trackers were still not searched** for dropped-text reports in either pass — absence of a loss claim there is still not evidence of no loss.
- marker's and Docling's **model download sizes** — not stated in the primary sources I read. **Still open.**
- MinerU's real-world CPU throughput on aarch64. The README documents CPU support and a 16 GB RAM floor but gives no ARM figures. **Still open.**
- **[New, from the merge pass]** Whether the `cryptography` Rust-extension ABI break underlying the markitdown/pdfminer.six failure (§3.7) is fixable — e.g. by a different `cryptography` version, or is inherent to how Termux packages that extension for Python 3.14. Only the failure itself was reproduced and traced to its exact import chain; no fix was attempted or found.
- **[New, from the merge pass]** The `.mht` conversion tool disagreement flagged in §1 (`markdownify` per this file's original recommendation vs. `trafilatura` per the parent repo's already-documented, already-in-use pipeline) was not adjudicated either way — neither tool's output was compared on a real `.mht` file in this pass.

**Not tested on-device (by rule — no installs were performed):**
- Docling, marker, MinerU, unstructured were **never installed or executed**. All platform conclusions come from `pip download --no-deps` resolution, declared `requires-python`, and dependency lists. Specifically verified: `torch` has **no** Termux py3.14 wheel; `torch 2.13.0` / `onnxruntime 1.29.0` / `docling-ibm-models` / `easyocr` / `rapidocr` / `mineru` **do** resolve in proot Debian py3.13; `pikepdf` and `pi_heif` resolve only as source tarballs on Termux py3.14.
- I did **not** check whether `numba` and `spacy` (base `unstructured` deps) have Termux py3.14 wheels — that probe was stopped before running. unstructured's own `requires-python = ">=3.11, <3.14"` already excludes the platform, so the conclusion stands independently, but the specific wheel status is unknown.
- The previously measured **13% / 52% `pymupdf4llm` loss was not re-measured** in this session. I took it as given per the brief and instead located the mechanism in source. The mechanism is confirmed; the exact percentages are inherited, not re-derived.
- The prototype in §3.1 was measured on **3 PDFs only** (those present in this research folder), not on the 6-document test set referenced in the brief, and **not on `.docx` or `.mht` at all**. The strict-superset property is a structural consequence of the assembler having no discard path, but 3 documents is 3 documents.
- The `.docx`/`.mht` recommendations in §1 are **design proposals, not tested code**.

**A caveat on the corpus itself, which changes what "success" means:** two of the three sample PDFs contain no structural signal of any kind — one font, one size, no outline — and their `.docx` counterparts contain no paragraph styles, no lists, no tables, no bold runs, and no `docProps/app.xml`, meaning they were machine-generated rather than authored. For those documents, **no tool at any price can recover headings**, because there is nothing to recover. Any pipeline that appears to produce structure for them is either inventing it heuristically or hallucinating it with an LLM. That is a corpus problem, not a tooling problem, and it should be fixed upstream — by keeping the authored originals — rather than by buying a bigger extractor.
