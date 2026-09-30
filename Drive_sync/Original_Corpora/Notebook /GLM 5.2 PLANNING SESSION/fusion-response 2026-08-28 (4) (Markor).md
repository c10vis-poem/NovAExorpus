<!-- Converted from fusion-response 2026-08-28 (4) (Markor).pdf — 3 pages -->

## Page 1

-e "\${CYAN}================================================\${NC}"
"\${CYAN} AESOP XI INFRASTRUCTURE SETUP\${NC}"
-e OpenWiki + GLM 5.2 + JSONL Markers\${NC}"
"\${CYAN}================================================\${NC}"
─── 0. PREFLIGHT CHECKS ─────────────────────────────────────
-e "\n\${YELLOW}[0/9] PREFLIGHT CHECKS\${NC}"
[ -z "\$PREFIX" ] || [ ! -d "/data/data/com.termux" ]; then
echo -e "\${RED}ERROR: Not running in Termux. Install Termux from F-Droid first.\${NC}"
exit 1
-e "\${GREEN} Termux detected\${NC}"
[ -z "\$OPENROUTER_API_KEY" ]; then
| echo -e "\n\${YELLOW} | OpenRouter API key not found in environment.\${NC}" |
|---|---|
| "\${YELLOW} | Get one from: https://openrouter.ai/keys\${NC}" |
| read -p " | Paste your OpenRouter API key now: " OR_KEY |
if   [ -z "\$OR_KEY"   ];   then
echo   -e   "\${RED} ERROR: No key provided. Exiting.\${NC}"
exit 1
fi
export   OPENROUTER_API_KEY="\$OR_KEY"
echo "export OPENROUTER_API_KEY=\"\$OR_KEY\""
  -e   "\${GREEN}     Key saved to ~/.bashrc\${NC}"
echo -e "\${GREEN} OpenRouter key found in environment\${NC}"
[ ! -d "\$NOVAE_DIR/.git" ]; then
echo -e "\n\${YELLOW} novae-xorpus not found at ~/novae-xorpus\${NC}"
read -p " Enter clone URL (or press Enter to skip): " NOVAE_URL if [ -n "\$NOVAE_URL" ]; then
git clone "\$NOVAE_URL" "\$NOVAE_DIR"
echo -e "\${GREEN} novae-xorpus cloned\${NC}"
else
echo -e "\${YELLOW} Creating empty novae-xorpus directory\${NC}" mkdir -p "\$NOVAE_DIR"
fi
echo -e "\${GREEN} novae-xorpus found\${NC}"
[ ! -d "\$RAW_DIR" ]; then
echo -e "\n\${YELLOW} raw-bucket not found at ~/raw-bucket\${NC}"
read -p " Enter clone URL for raw-bucket (or press Enter to create empty dir): " RAW_URL
if [ -n "\$RAW_URL" ]; then git clone "\$RAW_URL" "\$RAW_DIR"
echo -e "\${GREEN} raw-bucket cloned\${NC}"
else
mkdir -p "\$RAW_DIR"
echo -e "\${YELLOW} Empty raw-bucket directory created\${NC}" fi
echo -e "\${GREEN} raw-bucket found\${NC}"
-p "\$NOVAE_DIR/01-sources"
"\$NOVAE_DIR/02-clean"
-p "\$NOVAE_DIR/03-check"
─── 1. INSTALL SYSTEM PACKAGES ──────────────────────────────
-e "\n\${YELLOW}[1/9] INSTALLING SYSTEM PACKAGES\${NC}"
&& pkg upgrade -y
-y nodejs-lts git python tmux
-e "\${GREEN} nodejs-lts, git, python, tmux installed\${NC}"
─── 2. INSTALL PYTHON CONVERTERS ────────────────────────────
-e "\n\${YELLOW}[2/9] INSTALLING PYTHON FILE CONVERTERS\${NC}"
--upgrade pip
pymupdf python-docx markdownify -e "\${GREEN} pymupdf, python-docx, markdownify installed\${NC}"
─── 3. INSTALL OPENWIKI ─────────────────────────────────────
-e "\n\${YELLOW}[3/9] INSTALLING OPENWIKI\${NC}"
"\${YELLOW} This can take 5-10 minutes (compiles native deps)...\${NC}" -g openwiki
-e "\${GREEN} openwiki installed\${NC}"
─── 4. SET ENVIRONMENT VARIABLES ────────────────────────────
-e "\n\${YELLOW}[4/9] SETTING ENVIRONMENT VARIABLES\${NC}"
OPENWIKI_PROVIDER=openrouter
OPENWIKI_MODEL=z-ai/glm-5.2
-q "OPENWIKI_PROVIDER" ~/.bashrc || echo 'export OPENWIKI_PROVIDER=openrouter' >> ~/.bashrc
"OPENWIKI_MODEL" ~/.bashrc || echo 'export OPENWIKI_MODEL=z-ai/glm-5.2' >> ~/.bashrc
-e "\${GREEN} OPENWIKI_PROVIDER=openrouter\${NC}" OPENWIKI_MODEL=z-ai/glm-5.2\${NC}"
─── 5. WRITE CONVERTER SCRIPT ───────────────────────────────
-e "\n\${YELLOW}[5/9] WRITING RAW-TO-MARKDOWN CONVERTER\${NC}"
"\$HOME/convert-raw-to-md.py" << 'PYEOF'
→ Markdown Converter
→ markdown for OpenWiki ingestion
import fitz doc = fitz.open(str(pdf_path))
parts = []
for page in doc:
parts.append(page.get_text())
doc.close() return "\n\n".join(parts)
from docx import Document
doc = Document(str(docx_path)) lines = []
for para in doc.paragraphs:
if para.style.name.startswith("Heading"):
try:
level = int(para.style.name.replace("Heading ", "")) lines.append(f"{'#' * level} {para.text}")
except ValueError:
lines.append(para.text)
else:
lines.append(para.text) return "\n\n".join(lines)
from markdownify import markdownify
content = html_path.read_text(encoding="utf-8", errors="ignore") return markdownify(content)
content = txt_path.read_text(encoding="utf-8", errors="ignore")
return f"# {txt_path.stem}\n\n{content}"
fm = f"""---
return fm + content
".pdf": convert_pdf, ".docx": convert_docx,
".html": convert_html,
".htm": convert_html,
".txt": convert_txt,
".md": lambda p: p.read_text(encoding="utf-8", errors="ignore"),
if not RAW_BUCKET.exists():
print(f"ERROR: {RAW_BUCKET} does not exist") sys.exit(1)
CURATED.mkdir(parents=True, exist_ok=True)
converted = 0

---

## Page 2

if out_path.exists():
if out_path.stat().st_mtime >= file_path.stat().st_mtime:
skipped += 1
content = CONVERTERS[ext](file_path)
content_with_meta = add_frontmatter(content, file_path)
out_path.write_text(content_with_meta, encoding="utf-8")
print(f" {file_path.name} → {out_path.name}") converted += 1
except Exception as e:
print(f" {file_path.name}: {e}")
errors += 1
print(f"\nDone: {converted} converted, {skipped} skipped, {errors} errors")
print(f"Output: {CURATED}")
-e "\${GREEN} Converter written to ~/convert-raw-to-md.py\${NC}"
─── 6. WRITE JSONL MARKER SCRIPT ────────────────────────────
-e "\n\${YELLOW}[6/9] WRITING JSONL MARKER GENERATOR\${NC}"
"\$HOME/generate-jsonl-markers.py" << 'PYEOF'
Path("~/novae-xorpus").expanduser(),
Path("~/.openwiki/wiki").expanduser(),
content = file_path.read_text(encoding="utf-8", errors="ignore")
title = file_path.stem
for line in content.split("\n"):
if line.startswith("# "):
title = line.lstrip("# ").strip()
break
description = ""
for line in content.split("\n"):
stripped = line.strip()
if stripped and not stripped.startswith("#") and not stripped.startswith("---"): description = stripped[:200]
break
tokens = set()
for line in content.split("\n"): if line.startswith("##") or line.startswith("###"):
for word in line.lstrip("# ").lower().split():
if len(word) > 3:
tokens.add(word)
for word in file_path.stem.lower().split("-"):
if len(word) > 3:
tokens.add(word)
content_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
return {
"record_id": f"{source_type}_{file_path.stem.upper()[:40]}",
"document_path": str(file_path),
"source_type": source_type, "category": "TECHNICAL_REFERENCE",
"metadata": {
"title": title,
"description": description,
"content_hash": content_hash, "file_size_bytes": len(content.encode()),
"last_modified": datetime.fromtimestamp(
file_path.stat().st_mtime
).isoformat()
}, "retrieval_tokens": list(tokens)[:15],
"entry_points": {
"repl_command": f"/skill run {file_path.stem.lower().replace(' ', '-')}",
"jsonrpc_method": "agent.skills.execute" }
}
markers = []
for source_dir in SOURCES:
if not source_dir.exists():
print(f" Skipping {source_dir} — not found")
continue
source_type = "RAW_SOURCE" if "novae" in str(source_dir) else "WIKI_SYNTHESIS"
for md_file in source_dir.rglob("*.md"):
try: marker = make_marker(md_file, source_type)
markers.append(marker)
print(f" [{len(markers):04d}] {source_type}: {md_file.name}")
except Exception as e:
print(f" ERROR on {md_file}: {e}")
with open(OUTPUT, "w") as f:
for marker in markers:
f.write(json.dumps(marker, ensure_ascii=False) + "\n")
raw_count = sum(1 for m in markers if m["source_type"] == "RAW_SOURCE")
wiki_count = sum(1 for m in markers if m["source_type"] == "WIKI_SYNTHESIS")
print(f"\nDone: {len(markers)} markers → {OUTPUT}")
print(f" Raw sources: {raw_count}") Wiki synthesis: {wiki_count}")
main()
-e "\${GREEN} JSONL marker generator written to ~/generate-jsonl-markers.py\${NC}"
─── 7. RUN CONVERTER ─────────────────────────────────────── -e "\n\${YELLOW}[7/9] CONVERTING RAW FILES → MARKDOWN\${NC}"
[ "\$(find "\$RAW_DIR" -type f | head -1)" ]; then
python3 "\$HOME/convert-raw-to-md.py"
echo -e "\${GREEN} Raw files converted to novae-xorpus/01-sources/\${NC}"
echo -e "\${YELLOW} raw-bucket is empty — nothing to convert yet.\${NC}"
Add files to ~/raw-bucket/ and re-run converter later.\${NC}"
─── 8. INITIALIZE OPENWIKI (INTERACTIVE) ────────────────────
-e "\n\${YELLOW}[8/9] INITIALIZING OPENWIKI\${NC}"
| echo -e "\n\${YELLOW} | OpenRouter API key not found in environment.\${NC}" |
|---|---|
| "\${CYAN} | ──────────────────────────────────────────── \${NC}" |
| -e | This step is INTERACTIVE. When prompted:\${NC}" |
| "\${CYAN} | → Provider: select OpenRouter\${NC}" |
| -e | API key: your OpenRouter key (already in env)\${NC}" |
| "\${CYAN} | → Model: z-ai/glm-5.2\${NC}" |
| -e | Connector: git-repo, path: ~/novae-xorpus\${NC}" |
| "\${CYAN} | → Scope: AESOP XI architecture, model pathways,\${NC}" |
| -e | tool harnesses, and build priorities\${NC}" |
| "\${CYAN} | ──────────────────────────────────────────── \${NC}" |
"\${CYAN} ────────────────────────────────────────────\${NC}"
"\${CYAN} → Provider: select OpenRouter\${NC}"
"\${CYAN} → Model: z-ai/glm-5.2\${NC}"
"\${CYAN} → Scope: AESOP XI architecture, model pathways,\${NC}"
"\${CYAN} ────────────────────────────────────────────\${NC}"
""
-p " Press Enter to launch openwiki init (or Ctrl+C to skip)..."
-e "\${GREEN} OpenWiki initialized\${NC}"
─── 9. RUN SYNTHESIS + JSONL MARKERS ──────────────────────── -e "\n\${YELLOW}[9/9] RUNNING SYNTHESIS + JSONL MARKERS\${NC}"
-e "\${YELLOW} Running OpenWiki synthesis (GLM 5.2 reads your docs)...\${NC}"
"Initial synthesis from curated documentation"
-e "\${YELLOW} Generating JSONL markers...\${NC}"
─── DONE ────────────────────────────────────────────────────
-e "\n\${GREEN}================================================\${NC}" "\${GREEN} SETUP COMPLETE\${NC}"
-e "\${GREEN}================================================\${NC}"
""
"What was installed:"
" • Node.js LTS, Python, Git, tmux" • pymupdf, python-docx, markdownify (file converters)"
" • openwiki (wiki engine)"
• OpenRouter + GLM 5.2 configured"
""
"Scripts created:" " ~/convert-raw-to-md.py — converts raw files to markdown"
~/generate-jsonl-markers.py — generates JSONL markers"
""
"Directories:"

---

## Page 3

1. OpenRouter API key — if you don’t have it in your environment 2. OpenWiki init — interactive prompts where you select OpenRouter, GLM 5.2, and point it at novae-xorpus
npm install -g openwiki takes too long or runs out of memory, run the whole thing inside tmux:
-s setup