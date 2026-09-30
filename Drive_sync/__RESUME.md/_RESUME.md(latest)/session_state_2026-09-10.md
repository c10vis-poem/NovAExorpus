<!-- Converted from Untitled document.pdf — 18 pages -->

## Page 1

raw_database/ files — those are Tier 1 immutable raw sources, read-only. The canonical specs and handoff docs are the ones future agents read as instructions. Let me make all three edits. * Execute(command="cat > \"/storage/emulated/0/Documents/NovÆxorpus (1)/LlmWiki/Current repo skeleton and hand off guide.txt\" << 'ENDOFFILE'\nStep 1: The Canonical Repository Skeletons & Mirror Package\nArchive: NovAeXorpus_Complete_Mirrors.zip\n\nFraming & Topology:\n\nnovae-xorpus: Framed as the master core containing:\n\nThe Living Wiki (02_wiki_md/): vendors/ (Google, Qualcomm, Nvidia, GitHub, Anthropic, PrimeIntellect, DeepSeek), weights/, runtimes/, engines/, harnesses/, agents/, protocols/, scripts/, tools/, skills/, projects/, entities/, architectures/, memory-subsystem/, runbooks/, references/, operator-log/, and indexes/.\n\n#d.u.m.b.a.s.s. Core (_dumbass_universal_memory/): sqlite/, postgres/, mem0/, ob1_protocol/, omniroute/, reasoning_bank/, and continual_harness/.\n\nThe 5+1 Cognitive Tiers: 01_raw_sources/, 02_wiki_md/, 03_recall_cache/, 04_skills_runtime/, 05_episodic_logs/, plus root MAP.md and manifest.jsonl.\n\nThe 6 Paired Repositories:\n\nnovus-aexenti: dual_agent_router/, mem0_episodic/ (with ob1_static_protocols/), reasoning_bank/ (failure_logs/, reward_variables/, post_regression/), and nope_databank/.\n\nnovaexopia: openwiki-tui-harness/, modular swarm harnesses (prime-agent/, ringer-notif-loop/, hermes-soul/, local-nanobots/, smol-agents/, turbo-quant-swarms/), and mcp_connectors/.\n\naesop-xi: arbitration/ and policies/.\n\nhorizons-ui: model_loaders/, ui_tiles/, connectivity/, and webview/.\n\nnovus-aesc: laptop_trick_tunnel/, npu_watchdog/, and scripts/.\n\nnovus-aeyre: screen_vision/ and voice_ast_stack/.\n\nEach repo contains universal subfolders (raw/, clean_md/, wiki_md/, skills/, tools/, pending/, audit/) and standard control files (MAP.md, manifest.jsonl, README.md, AGENTS.md, RESUME.md, chunk.jsonl). The canonical control-file pattern is the structural guideline across repos — repos vary slightly in contents but share identical structure. No hard min or max on file or folder counts; the structure and the control-file references in route are the guideline, not any particular number.\n\nStep 2: Master Compilation Execution Plan & Handoff Protocol\nDocument: MASTER_COMPILATION_EXECUTION_PLAN_AND_HANDOFF.md\n\nOperational Invariants Codified:\n\nNon-1:1 Condensation Law: Strip conversational filler and duplicate boilerplate, but maintain 100% build fidelity so that raw and clean markdown build the exact same output.\n\nLocality of Reference: Skills and tools live locally where they are applied.\n\nThe First-Move Directive: Read MAP.md (orient) then Read tier MAP.md (focus) then Query manifest.jsonl (stream/filter) then Load targeted files only.\n\nHard Rule 5 (Extractor Independence): Ingestion passes must be verified by corpus-verify (tools/check.py) using disjoint extractors (pypdf, zipfile+xml.etree, html.parser).\n\nThe 4-Phase Workflow:\n\nPhase 1: Normalization and dual extraction (raw/ to clean_md/,

---

## Page 2

skills/, tools/).\n\nPhase 2: Independent RLVR validation (clean_md/ to audit/).\n\nPhase 3: Pre-tokenized chunking and SHA-256 manifest cataloging (clean_md/ to chunk.jsonl, manifest.jsonl).\n\nPhase 4: Living Wiki population with bidirectional wikilinks.\n\nCopy-Paste Resume Prompt for the Next Session\n\n```\nRESUME INSTRUCTION:\nContinue execution on Project NovAExorpus living canon compilation.\n\n1. Reference MASTER_COMPILATION_EXECUTION_PLAN_AND_HANDOFF.md and NovAeXorpus_Complete_Mirrors.zip in Secure-Spark-Proof-Folder / 01_MASTER_MIRROR_GLIDE.\n\n2. The 7 canonical repository skeletons are staged: novae-xorpus, novus-aexenti, novaexopia, aesop-xi, horizons-ui, novus-aesc, novus-aeyre.\n\n3. Execute Phase 1 Ingestion and Normalization on the raw files in 02_MY_ORIGINALS:\n - Convert raw inputs to clean Markdown with YAML frontmatter.\n - Extract procedural heuristics to skills/ and executable scripts to tools/.\n - Enforce the Non-1:1 Condensation Law: preserve 100 percent build context, eliminate conversational fat.\n\n4. Run corpus-verify (tools/check.py) per Hard Rule 5 for independent RLVR validation before committing.\n\n5. Populate the Living Wiki in novae-xorpus/02_wiki_md/ and index in manifest.jsonl.\n```\nENDOFFILE\necho \"WROTE: handoff guide\"; echo \"exit: $?\"")
NovÆxorpus repo. You are resuming work on Project NovAExorpus — a distributed edge-AI cognitive repository architecture running on this Android device via Termux. This is NOT a GitHub repo. It is the device's local filesystem. You have full read/write access to it through the shell.
KEY FACTS ABOUT THIS ENVIRONMENT - Device: Android aarch64, kernel 5.15, Termux, user u0_a280 - The project root is at: /storage/em ulated/0/Documents/NovAExorpus (1)/ - 7 federated repos live under: /stor age/emulated/0/Documents/NovAExorpus (1)/NovAExorpus_Repo's/ They are: novae-xorpus, novus-aexenti, novaexopia, aesop-xi, horizons-ui, novus-aesc, novus-aeyre - raw_database/ holds the ingestion source corpus (raw/ and

---

## Page 3

02_MY_ORIGINALS/) - The master specs are numbered 00-05 in novae-xorpus/ root - The working docs and handoff guides are in: /storage/emulated/0/Document s/NovAExorpus (1)/LlmWiki/ - The global cross-session backlog is at: __RESUME.md/_Unresolved/unresolved.md - The OBSIDIAN-Master_Wiki git vault is at: ~/work/OBSIDIAN-Master_Wiki/ - OpenWiki fork is at: ~/openwiki/ (branch claude/wiki-quinn-npu-local-m1crql) - GenieX fork is at: ~/work/genie-x-fork/
MEMORY SYSTEM - The persistent memory layer is #d.u.m.b.a.s.s. (Database and Universal Memory Bank Across Split Services) in novae-xorpus/_dumbass_un iversal_memory/ - unresolved.md is the durable cross-session backlog — items persist across sessions and repos - The previous session's handoff guide is at LlmWiki/Current repo skeleton and hand off guide.txt — read it first - There is NO cross-session context memory. Only what is on disk survives. Read the handoff guide and unresolved.md before doing anything else.
CORRECTIONS MADE THIS SESSION (already written to disk, do not redo) 1. Red Auditor / ~/.red/ / .incognito_red_sandbox/ — fully removed from all authoritative instruction docs (master spec 00, handoff guide, OPERATOR_README,

---

## Page 4

unresolved.md). Do not mention, flag, or re-add any Red Auditor rule. The APK and daemon that were called "red audit agent" will be used directly in this environment under a different name. Do not talk about it. 2. No hard min or max on repository file or folder counts. The structural guideline is the canonical control-file pattern (MAP.md, manifest.jsonl, README.md, AGENTS.md, RESUME.md, chunk.jsonl) plus the universal subfolders (raw/, clean_md/, wiki_md/, skills/, tools/, pending/, audit/). Reposos vary slightly in contents but share identical structure. Never flag file-count discrepancies as conflicts. 3. ECC is no longer used. Aider is no longer used. Do not flag their absence or presence as conflicts. Tools and harnesses naturally populate as the environment evolves — do not waste time ironing this out. You will know what you need when you need it. 4. The resume prompt in the handoff guide was put in a code block because this Termux environment blanks out parentheses, numbers, and special characters when they are not in code blocks.
WHERE THE WORK STANDS - The 7 repo skeletons are staged (created Sep 9). Directory structure is in place. - Most subdirectories contain POINTER.md stubs only — the actual cleaned content has NOT been populated yet. - Raw sources are loaded in raw_database/raw/ and

---

## Page 5

raw_database/02_MY_ORIGINALS/ (PDFs, DOCX, MHT, txt — architecture blueprints, Qualcomm QAIRT docs, grill session transcripts, etc.) - Phase 1 of the 4-phase compilation plan is incomplete. That is where to resume.
THE 4-PHASE WORKFLOW Phase 1: Normalization and dual extraction (raw/ to clean_md/, skills/, tools/). Convert raw inputs to clean Markdown with YAML frontmatter. Extract procedural heuristics to skills/ and executable scripts to tools/. Enforce the Non-1:1 Condensation Law: preserve 100 percent build context, eliminate conversational fat. Phase 2: Independent RLVR validation (clean_md/ to audit/). Run corpus-verify (tools/check.py) per Hard Rule 5 using disjoint extractors. Phase 3: Pre-tokenized chunking and SHA-256 manifest cataloging (clean_md/ to chunk.jsonl, manifest.jsonl). Phase 4: Living Wiki population with bidirectional wikilinks.
OPERATIONAL RULES - Tier 1 (01_raw_sources/) is READ-ONLY. Never modify raw sources. - Read MAP.md first, then tier MAP.md, then manifest.jsonl before doing recursive filesystem scans. - Hard Rule 5: the tool that cleaned a file does not get a vote on whether the cleaning was good. Use disjoint extractors for verification. - When writing files that contain parentheses, numbers, or special characters that the operator needs to

---

## Page 6

read or copy, use code blocks — this Termux display environment blanks them out otherwise.
START BY 1. Read LlmWiki/Current repo skeleton and hand off guide.txt 2. Read __RESUME.md/_Unresolved/unresolved.md 3. Read novae-xorpus/00_DEFINITIVE_MA STER_SPECIFICATION_V3_COMPLETE.md for the current canonical spec 4. Survey what is in raw_database/raw/ and raw_database/02_MY_ORIGINALS/ 5. Begin Phase 1 ingestion on the raw sources, writing clean Markdown to each repo's clean_md/ directory
read it first - There is NO cross-session context memory. Only what is on disk survives. Read the handoff guide and unresolved.md before doing anything else.
CORRECTIONS MADE THIS
directory. * Execute(command="PY=/data/data/com.t ermux/files/usr/bin/python3\n\n# First, let me test that mutool and pypdf both work on one of the actual PDFs\n$PY << 'PYEOF'\nimport os, subprocess\n\ndocs = \"/storage/emulat ed/0/Documents\"\nnovae = None\nfor e in os.listdir(docs):\n if \"xorpus\" in e.lower():\n novae = os.path.join(docs, e)\n break\n\nrepos = None\nfor e in os.listdir(novae):\n if \"Repo\" in e and os.path.isdir(os.path.join(novae,

---

## Page 7

e)):\n repos = os.path.join(novae, e)\n break\n\nraw_db = os.path.join(repos, \"raw_database\")\nraw_dir = os.path.join(raw_db, \"raw\")\n\n# Test mutool on \"Four Core Buckets.pdf\"\ntest_pdf = None\nfor f in os.listdir(raw_dir):\n if f == \"Four Core Buckets.pdf\":\n test_pdf = os.path.join(raw_dir, f)\n break\n\nif test_pdf:\n print(f\"Testing mutool on: {os.path.basename(test_pdf)}\")\n result = subprocess.run(\n [\"/data/data/com.termux/files/usr/bin /mutool\", \"draw\", \"-F\", \"text\", test_pdf],\n capture_output=True, text=True\n )\n if result.returncode == 0:\n print(f\" mutool: OK -{len(result.stdout)} chars extracted\")\n print(f\" First 200: {result.stdout[:200]}\")\n else:\n print(f\" mutool error: {result.stderr[:200]}\")\n\n print()\n print(f\"Testing pypdf on: {os.path.basename(test_pdf)}\")\n from pypdf import PdfReader\n reader = PdfReader(test_pdf)\n print(f\" Pages: {len(reader.pages)}\")\n text = reader.pages[0].extract_text()\n print(f\" pypdf: OK - {len(text)} chars from page 1\")\n print(f\" First 200: {text[:200]}\")\nelse:\n print(\"Test PDF not found\")\nPYEOF")
* Both extractors work and produce different output (mutool gets 6406 chars, pypdf gets different spacing patterns) — that's exactly what Hard Rule 5 needs. Now let me write the full ingestion pipeline.

---

## Page 8

* Execute(command="PY=/data/data/com.t ermux/files/usr/bin/python3\n\n# Write the ingestion script to a file in the novae-xorpus repo\n$PY << 'SCRIPT_EOF'\nimport os\n\ndocs = \"/s torage/emulated/0/Documents\"\nnovae = None\nfor e in os.listdir(docs):\n if \"xorpus\" in e.lower():\n novae = os.path.join(docs, e)\n break\n\nrepos_dir = None\nfor e in os.listdir(novae):\n if \"Repo\" in e and os.path.isdir(os.path.join(novae, e)):\n repos_dir = os.path.join(novae, e)\n break\n\n# Write the script to novae-xorpus/tools/\nnovae_xorpus = os.path.join(repos_dir, \"novae-xorpus\")\ntools_dir = os.path.join(novae_xorpus, \"tools\")\nos.makedirs(tools_dir, exist_ok=True)\n\nscript_path = os.path.join(tools_dir, \"clean.py\")\n\nscript = r'''#!/usr/bin/env python3\n\"\"\"\nPhase 1 Ingestion Pipeline - Cognitive Repository Architecture\nConverts raw sources to clean Markdown with YAML frontmatter.\nUses mutool (mupdf) for PDF extraction - the verification pass (tools/check.py)\nmust use a DIFFERENT extractor (pypdf) per Hard Rule 5.\n\"\"\"\nimport os, re, sys, subprocess, hashlib, datetime\nfrom pathlib import Path\n\n# ---Configuration ---\ndef find_raw_dir():\n docs = \"/storage/emulated/0/Documents\"\n for e in os.listdir(docs):\n if \"xorpus\" in e.lower():\n novae = os.path.join(docs, e)\n break\n else:\n raise FileNotFoundError(\"NovAExorpus

---

## Page 9

dir not found\")\n for e in os.listdir(novae):\n if \"Repo\" in e and os.path.isdir(os.path.join(novae, e)):\n repos = os.path.join(novae, e)\n break\n else:\n raise FileNotFoundError(\"Repos dir not found\")\n raw_db = os.path.join(repos, \"raw_database\")\n return os.path.join(raw_db, \"raw\"), repos\n\nRAW_DIR, REPOS_DIR = find_raw_dir()\nMUTOOL = \"/data/data/ com.termux/files/usr/bin/mutool\"\n\n# --- Helpers ---\ndef make_slug(filename):\n \"\"\"Create a clean filename slug from a raw filename.\"\"\"\n name = os.path.splitext(filename)[0]\n name = re.sub(r'[^\\w\\s\\-.]', '', name)\n name = re.sub(r'\\s+', '_', name.strip())\n name = re.sub(r'_+', '_', name)\n name = name.strip('_.')\n return name or \"unnamed\"\n\ndef make_frontmatter(source_file, doc_type, title=None):\n \"\"\"Generate YAML frontmatter for a cleaned document.\"\"\"\n if title is None:\n title = os.path.splitext(source_file)[0]\n # Truncate title for frontmatter\n title = title[:200]\n ts = datetime.datetime.now().strftime(\"%Y-%m-%d\")\n return f\"\"\"---\nsource: {source_file}\ntype: {doc_type}\ncleaned: {ts}\ncleaner: tools/clean.py (mutool)\n---\n\n\"\"\"\n\ndef extract_pdf_mutool(pdf_path):\n \"\"\"Extract text from PDF using mutool (mupdf). This is the CLEANING

---

## Page 10

extractor.\n The verification pass must use pypdf (disjoint per Hard Rule 5).\"\"\"\n try:\n result = subprocess.run(\n [MUTOOL, \"draw\", \"-F\", \"text\", pdf_path],\n capture_output=True, text=True, timeout=60\n )\n if result.returncode == 0:\n return result.stdout\n else:\n return f\"[PDF extraction error: {result.stderr[:200]}]\"\n except Exception as e:\n return f\"[PDF extraction error: {e}]\"\n\ndef extract_docx_python(docx_path):\n \"\"\"Extract text from DOCX using python-docx.\"\"\"\n try:\n import docx\n doc = docx.Document(docx_path)\n parts = []\n for para in doc.paragraphs:\n if para.text.strip():\n style = para.style.name if para.style else \"\"\n if \"Heading\" in style:\n level = 1\n m = re.search(r'\\d+', style)\n if m:\n level = int(m.group(0))\n parts.append(\"#\" * level + \" \" + para.text)\n
| else:\n | parts.append(para.text)\n |  | # |
|---|---|---|---|
| Also extract tables\n | for table |  |  |
| in doc.tables:\n | for row | in table.rows:\n | cells |
= [cell.text.strip() for cell in
row.cells]\n
parts.append(\"| \" + \" |
\".join(cells) + \" |\")\n  
except Exception as e:\n   return
f\"[DOCX extraction error:
{e}]\"\n\ndef
extract_html(html_path):\n   \"\"\"Extract text from HTML using
stdlib html.parser.\"\"\"\n   try:\n

---

## Page 11

from html.parser import HTMLParser\n class TextExtractor(HTMLParser):\n def __init__(self):\n super().__init__()\n self.parts = []\n self.in_tag = None\n def handle_starttag(self, tag, attrs):\n if tag in (\"h1\",\"h2\" ,\"h3\",\"h4\",\"h5\",\"h6\"):\n self.in_tag = tag\n level = int(tag[1])\n
self.parts.append(\"\\n\" + \"#\" * level + \" \")\n elif tag == \"p\":\n self.parts.append(\"\\n\\n\")\n elif tag == \"br\":\n self.parts.append(\"\\n\")\n elif tag == \"li\":\n self.parts.append(\"\\n-\")\n elif tag == \"code\":\n self.parts.append(\"`\")\n elif tag == \"pre\":\n
self.parts.append(\"\\n```\\n\")\n elif tag == \"a\":\n for k,v in attrs:\n if k == \"href\":\n
self.parts.append(\"[\")\n self._href = v\n break\n def handle_endtag(self, tag):\n if tag == \"code\":\n self.parts.append(\"`\")\n elif tag == \"pre\":\n self.parts.append(\"\\n```\\n\")\n elif tag == \"a\" and hasattr(self, \"_href\"):\n self.parts.append(f\"]({self. _href})\")\n del self._href\n self.in_tag = None\n def handle_data(self, data):\n self.parts.append(data)\n with open(html_path, \"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n content = f.read()\n parser = TextExtractor()\n

---

## Page 12

| parser.feed(content)\n | return |
|---|---|
| \"\".join(parser.parts)\n | except |
| Exception as e:\n | return |
parser.feed(content)\n return \"\".join(parser.parts)\n except Exception as e:\n return f\"[HTML extraction error: {e}]\"\n\ndef sniff_file(filepath):\n \"\"\"Detect actual file type by magic bytes.\"\"\"\n with open(filepath, \"rb\") as f:\n magic = f.read(16)\n if magic.startswith(b\"%PDF\"):\n return \"pdf\"\n if magic.startswith(b\"PK\"):\n # Could be docx (zip-based)\n return \"zip\"\n if magic.startswith(b\"<\") or magic.star tswith(b\"\\xef\\xbb\\xbf<\"):\n # Check if it's HTML\n try:\n with open(filepath, \"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n preview = f.read(500).lower()\n if \"<html\" in preview or \"<div\" in preview or \"<!doctype\"
| in preview:\n |  | return |
|---|---|---|
| \"html\"\n | except:\n |  |
| pass\n | return |  |
| \"xml_or_markup\"\n |  | return |
in preview:\n return \"html\"\n except:\n pass\n return \"xml_or_markup\"\n return \"text\"\n\ndef normalize_markdown(content):\n \"\"\"Apply Non-1:1 Condensation Law: strip conversational filler and duplicate\n boilerplate, maintain 100% build fidelity.\"\"\"\n # Strip excessive blank lines (more than 2 consecutive)\n content = re.sub(r'\\n{4,}', '\\n\\n\\n', content)\n # Strip Windows-style line endings\n content = content.replace(\"\\r\\n\", \"\\n\").replace(\"\\r\", \"\\n\")\n # Strip trailing whitespace on lines\n content = \"\\n\".join(line.rstrip() for line in content.split(\"\\n\"))\n return content.strip() + \"\\n\"\n\ndef process_file(filepath, filename, clean_md_dir):\n \"\"\"Process a single raw file and write its cleaned markdown version.\"\"\"\n ext = os.

---

## Page 13

path.splitext(filename)[1].lower()\n actual_type = sniff_file(filepath)\n \n # Determine extraction method and doc type\n if actual_type == \"pdf\" or ext ==
| in preview:\n |  | return |
|---|---|---|
| \".pdf\":\n | doc_type = |  |
| \"pdf\"\n | content = |  |
| extract_pdf_mutool(filepath)\n |  | elif |
\".pdf\":\n doc_type = \"pdf\"\n content = extract_pdf_mutool(filepath)\n elif ext == \".docx\" or (actual_type == \"zip\" and ext == \".docx\"):\n doc_type = \"docx\"\n content = extract_docx_python(filepath)\n elif actual_type == \"html\":\n
| doc_type = \"html\"\n |  | content |
|---|---|---|
| = extract_html(filepath)\n |  | elif ext |
| in (\".py\",):\n | doc_type = |  |
| \"python\"\n | with |  |
doc_type = \"html\"\n content = extract_html(filepath)\n elif ext in (\".py\",):\n doc_type = \"python\"\n with open(filepath, \"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n content = f.read()\n content = \"```python\\n\" + content +
| \"\\n```\"\n | elif ext in |
|---|---|
| (\".sh\",):\n | doc_type = |
| \"shell\"\n | with open(filepath, |
\"\\n```\"\n elif ext in (\".sh\",):\n doc_type = \"shell\"\n with open(filepath, \"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n content = f.read()\n content = \"```bash\\n\" + content +
| \"\\n```\"\n | elif ext in |
|---|---|
| (\".skill\",):\n | doc_type = |
| \"skill\"\n | with open(filepath, \"r\", encoding=\"utf-8\", |
\"\\n```\"\n elif ext in (\".skill\",):\n doc_type =
errors=\"replace\") as f:\n
content = f.read()\n elif ext in
(\".csv\",):\n     \"csv\"\n
\"r\", encoding=\"utf-8\",
| errors=\"replace\") as f:\n |  | content = f.read()\n | elif ext in |
|---|---|---|---|
| (\".xml\",):\n | doc_type = |  |  |
| \"xml\"\n | with open(filepath, |  |  |
| \"\\n```\"\n | elif ext in (\".yml\", |
|---|---|
| \".yaml\"):\n | doc_type = |
| \"yaml\"\n | with open(filepath, |
\"\\n```\"\n elif ext in (\".yml\", \".yaml\"):\n doc_type = \"yaml\"\n with open(filepath,

---

## Page 14

\"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n content = f.read()\n content = \"```yaml\\n\" + content + \"\\n```\"\n elif ext in
| \"\\n```\"\n | elif ext in (\".yml\", |
|---|---|
| (\".toml\",):\n | doc_type = |
| \"toml\"\n | with open(filepath, |
(\".toml\",):\n doc_type = \"toml\"\n with open(filepath, \"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n content = f.read()\n content = \"```toml\\n\" + content + \"\\n```\"\n elif ext in (\".md\",) or actual_type == \"text\":\n doc_type = \"markdown\" if ext == \".md\" else \"text\"\n with open(filepath, \"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n content = f.read()\n # If already has frontmatter, keep it\n if content.startswith(\"---\"):\n # Has existing frontmatter - normalize the content after it\n parts = content.split(\"---\", 2)\n if len(parts) >= 3:\n existing_fm = parts[1]\n body = parts[2]\n content = normalize_markdown(body)\n # Rebuild with updated frontmatter\n fm = make_frontmatter(filename, doc_type)\n content = fm + content\n else:\n content = normalize_markdown(content)\n fm = make_frontmatter(filename, doc_type)\n content = fm + content\n else:\n content = normalize_markdown(content)\n fm = make_frontmatter(filename, doc_type)\n content = fm + content\n # Write and return\n slug = make_slug(filename) + \".md\"\n out_path = os.path.join(clean_md_dir, slug)\n # Avoid clobbering\n if

---

## Page 15

os.path.exists(out_path):\n base, e = os.path.splitext(slug)\n i = 1\n while os.p ath.exists(os.path.join(clean_md_dir, f\"{base}_{i}{e}\")):\n i += 1\n slug = f\"{base}_{i}{e}\"\n out_path = os.path.join(clean_md_dir, slug)\n with open(out_path, \"w\", encoding=\"utf-8\") as f:\n f.write(content)\n return slug, doc_type, len(content)\n elif ext == \".txt\":\n doc_type = \"text\"\n with open(filepath, \"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n content = f.read()\n elif ext == \".rev\":\n # Binary revision file - skip\n return None, \"binary-skip\", 0\n else:\n # Unknown extension - try as text\n doc_type = \"unknown\"\n try:\n with open(filepath, \"r\", encoding=\"utf-8\", errors=\"replace\") as f:\n content = f.read()\n
| except:\n | return None, |  |  |
|---|---|---|---|
| \"binary-skip\", 0\n |  | \n # For | non-markdown types, normalize and add |
| frontmatter\n | if not |  |  |
except:\n return None,
content.startswith(\"---\"):\n
normalize_markdown(content)\n
fm = make_frontmatter(filename,
  content = fm +   content\n
  slug =
make_slug(filename) + \".md\"\n
out_path = os.path.join(clean_md_dir,
os.path.exists(out_path):\n
base, e = os.path.splitext(slug)\n
  while os.path.exist
s(os.path.join(clean_md_dir,
  i
slug =   f\"{base}_{i}{e}\"\n
os.path.join(clean_md_dir, slug)\n
with open(out_path, \"w\",
encoding=\"utf-8\") as f:\n
  return slug,

---

## Page 16

doc_type, len(content)\n\n# --- Main ---\ndef main():\n raw_dir = RAW_DIR\n clean_md_dir = os.path.join(REPOS_DIR, \"novae-xorpus\", \"clean_md\")\n \n # Also process 02_MY_ORIGINALS\n originals_dir = os.path.join(os.path.dirname(raw_dir), \"02_MY_ORIGINALS\")\n \n # Create clean_md dir\n os.makedirs(clean_md_dir, exist_ok=True)\n \n # Remove existing POINTER.md\n pointer = os.path.join(clean_md_dir, \"POINTER.md\")\n if os.path.exists(pointer):\n os.remove(pointer)\n \n print(f\"Phase 1 Ingestion Pipeline\")\n print(f\"Raw source: {raw_dir}\")\n print(f\"Originals: {originals_dir}\")\n print(f\"Output: {clean_md_dir}\")\n print()\n \n stats = {}\n processed = 0\n skipped = 0\n errors = 0\n \n # Process raw/ directory\n all_files = []\n if os.path.isdir(raw_dir):\n all_f iles.extend([(os.path.join(raw_dir, f), f) for f in os.listdir(raw_dir) if os.path.isfile(os.path.join(raw_dir, f))])\n if os.path.isdir(originals_dir):\n all_files.extend([(os.path.join(origi nals_dir, f), f) for f in os.listdir(originals_dir) if os.path.i sfile(os.path.join(originals_dir,
| f))])\n | \n # Deduplicate by |  |
|---|---|---|
| content hash\n |  | seen_hashes = {}\n |
| deduped = []\n |  | for filepath, |
f))])\n \n # Deduplicate by content hash\n seen_hashes = {}\n deduped = []\n for filepath, filename in sorted(all_files):\n try:\n with open(filepath, \"rb\") as f:\n h = hashlib.sha256(f.read()).hexdigest()\n

---

## Page 17

if h in seen_hashes:\n print(f\" DEDUP: {filename} (identical to {seen_hashes[h]})\")\n skipped += 1\n continue\n seen_hashes[h] = filename\n deduped.append((filepath, filename))\n except Exception as e:\n print(f\" HASH ERROR: {filename}: {e}\")\n deduped.append((filepath, filename))\n \n print(f\"Total files: {len(all_files)} | After dedup: {len(deduped)} | Skipped dups: {skipped}\")\n print()\n \n for filepath, filename in deduped:\n try:\n slug, doc_type, size = process_file(filepath, filename, clean_md_dir)\n if slug:\n processed += 1\n stats[doc_type] = stats.get(doc_type, 0) + 1\n print(f\" [{doc_type:>10}] {filename[:60]:<60} -> {slug}\")\n else:\n if doc_type == \"binary-skip\":\n skipped += 1\n print(f\" [ skipped] {filename[:60]:<60} (binary)\")\n except Exception as e:\n errors += 1\n print(f\" [ ERROR] {filename[:60]:<60} {e}\")\n \n print()\n print(f\"--- Summary ---\")\n print(f\"Processed: {processed}\")\n print(f\"Skipped: {skipped}\")\n print(f\"Errors: {errors}\")\n print(f\"By type: {stats}\")\n\nif __name__ == \"__main__\":\n main()\n'''\n\nwith open(script_path, \"w\", encoding=\"utf-8\") as f:\n f.write(script)\n\nprint(f\"Script written to: {script_path}\")\nprint(f\"Size: {os.path.getsize(script_path)} bytes\")\nSCRIPT_EOF")

---

## Page 18

* Now let me run the ingestion pipeline. * Ran 2 actionsI wrote a full session state file at LlmWiki/session_state_2026-09-10.md — the n