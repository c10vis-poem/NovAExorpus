---
source: fusion-response 2026-08-28 (4) (Markor)
type: pdf
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

Here’s one script. Save it as ~/setup-aesop.sh and run it. It creates the converter and JSONL scripts, installs everything, and pauses only for the interactive OpenWiki init step.

#!/usr/bin/env bash

# ==============================================================

# AESOP XI: ONE-SHOT SETUP SCRIPT
# Termux / Android / aarch64

# ==============================================================

set -e



# Colors
RED='\033[0;31m'

GREEN='\033[0;32m'

YELLOW='\033[1;33m'

CYAN='\033[0;36m'

NC='\033[0m'


echo -e "\${CYAN}================================================\${NC}"

echo -e "\${CYAN}  AESOP XI INFRASTRUCTURE SETUP\${NC}"

echo -e "\${CYAN}  OpenWiki + GLM 5.2 + JSONL Markers\${NC}"

echo -e "\${CYAN}================================================\${NC}"


# ─── 0. PREFLIGHT CHECKS ─────────────────────────────────────

echo -e "\n\${YELLOW}[0/9] PREFLIGHT CHECKS\${NC}"



# Check Termux
if [ -z "\$PREFIX" ] || [ ! -d "/data/data/com.termux" ]; then

    echo -e "\${RED}ERROR: Not running in Termux. Install Termux from F-Droid first.\${NC}"

    exit 1

fi

echo -e "\${GREEN}  ✓ Termux detected\${NC}"


# Check OpenRouter key

if [ -z "\$OPENROUTER_API_KEY" ]; then

    echo -e "\n\${YELLOW}  OpenRouter API key not found in environment.\${NC}"

    echo -e "\${YELLOW}  Get one from: https://openrouter.ai/keys\${NC}"
    read -p "  Paste your OpenRouter API key now: " OR_KEY

    if [ -z "\$OR_KEY" ]; then

        echo -e "\${RED}  ERROR: No key provided. Exiting.\${NC}"

        exit 1

    fi
    export OPENROUTER_API_KEY="\$OR_KEY"

    echo "export OPENROUTER_API_KEY=\"\$OR_KEY\"" >> ~/.bashrc

    echo -e "\${GREEN}  ✓ Key saved to ~/.bashrc\${NC}"

else

    echo -e "\${GREEN}  ✓ OpenRouter key found in environment\${NC}"
fi



# Check repos

NOVAE_DIR="\$HOME/novae-xorpus"
RAW_DIR="\$HOME/raw-bucket"



if [ ! -d "\$NOVAE_DIR/.git" ]; then

    echo -e "\n\${YELLOW}  novae-xorpus not found at ~/novae-xorpus\${NC}"

    read -p "  Enter clone URL (or press Enter to skip): " NOVAE_URL
    if [ -n "\$NOVAE_URL" ]; then

        git clone "\$NOVAE_URL" "\$NOVAE_DIR"

        echo -e "\${GREEN}  ✓ novae-xorpus cloned\${NC}"

    else

        echo -e "\${YELLOW}  Creating empty novae-xorpus directory\${NC}"
        mkdir -p "\$NOVAE_DIR"

    fi

else

    echo -e "\${GREEN}  ✓ novae-xorpus found\${NC}"

fi


if [ ! -d "\$RAW_DIR" ]; then

    echo -e "\n\${YELLOW}  raw-bucket not found at ~/raw-bucket\${NC}"

    read -p "  Enter clone URL for raw-bucket (or press Enter to create empty dir): " RAW_URL

    if [ -n "\$RAW_URL" ]; then
        git clone "\$RAW_URL" "\$RAW_DIR"

        echo -e "\${GREEN}  ✓ raw-bucket cloned\${NC}"

    else

        mkdir -p "\$RAW_DIR"

        echo -e "\${YELLOW}  ✓ Empty raw-bucket directory created\${NC}"
    fi

else

    echo -e "\${GREEN}  ✓ raw-bucket found\${NC}"

fi


# Create curation subdirs in novae-xorpus

mkdir -p "\$NOVAE_DIR/01-sources"

mkdir -p "\$NOVAE_DIR/02-clean"

mkdir -p "\$NOVAE_DIR/03-check"


# ─── 1. INSTALL SYSTEM PACKAGES ──────────────────────────────

echo -e "\n\${YELLOW}[1/9] INSTALLING SYSTEM PACKAGES\${NC}"

pkg update -y && pkg upgrade -y

pkg install -y nodejs-lts git python tmux

echo -e "\${GREEN}  ✓ nodejs-lts, git, python, tmux installed\${NC}"


# ─── 2. INSTALL PYTHON CONVERTERS ────────────────────────────

echo -e "\n\${YELLOW}[2/9] INSTALLING PYTHON FILE CONVERTERS\${NC}"

pip install --upgrade pip

pip install pymupdf python-docx markdownify
echo -e "\${GREEN}  ✓ pymupdf, python-docx, markdownify installed\${NC}"



# ─── 3. INSTALL OPENWIKI ─────────────────────────────────────

echo -e "\n\${YELLOW}[3/9] INSTALLING OPENWIKI\${NC}"

echo -e "\${YELLOW}  This can take 5-10 minutes (compiles native deps)...\${NC}"
npm install -g openwiki

echo -e "\${GREEN}  ✓ openwiki installed\${NC}"



# ─── 4. SET ENVIRONMENT VARIABLES ────────────────────────────

echo -e "\n\${YELLOW}[4/9] SETTING ENVIRONMENT VARIABLES\${NC}"


# OpenRouter key already set in preflight

export OPENWIKI_PROVIDER=openrouter

export OPENWIKI_MODEL=z-ai/glm-5.2


grep -q "OPENWIKI_PROVIDER" ~/.bashrc || echo 'export OPENWIKI_PROVIDER=openrouter' >> ~/.bashrc

grep -q "OPENWIKI_MODEL" ~/.bashrc || echo 'export OPENWIKI_MODEL=z-ai/glm-5.2' >> ~/.bashrc



echo -e "\${GREEN}  ✓ OPENWIKI_PROVIDER=openrouter\${NC}"
echo -e "\${GREEN}  ✓ OPENWIKI_MODEL=z-ai/glm-5.2\${NC}"



# ─── 5. WRITE CONVERTER SCRIPT ───────────────────────────────

echo -e "\n\${YELLOW}[5/9] WRITING RAW-TO-MARKDOWN CONVERTER\${NC}"


cat > "\$HOME/convert-raw-to-md.py" << 'PYEOF'

#!/usr/bin/env python3

"""

Raw Bucket → Markdown Converter

Converts PDF, DOCX, TXT, HTML → markdown for OpenWiki ingestion
"""

import sys

from pathlib import Path

from datetime import datetime


RAW_BUCKET = Path("~/raw-bucket").expanduser()

CURATED = Path("~/novae-xorpus/01-sources").expanduser()



def convert_pdf(pdf_path):

    import fitz
    doc = fitz.open(str(pdf_path))

    parts = []

    for page in doc:

        parts.append(page.get_text())

    doc.close()
    return "\n\n".join(parts)



def convert_docx(docx_path):

    from docx import Document

    doc = Document(str(docx_path))
    lines = []

    for para in doc.paragraphs:

        if para.style.name.startswith("Heading"):

            try:

                level = int(para.style.name.replace("Heading ", ""))
                lines.append(f"{'#' * level} {para.text}")

            except ValueError:

                lines.append(para.text)

        else:

            lines.append(para.text)
    return "\n\n".join(lines)



def convert_html(html_path):

    from markdownify import markdownify

    content = html_path.read_text(encoding="utf-8", errors="ignore")
    return markdownify(content)



def convert_txt(txt_path):

    content = txt_path.read_text(encoding="utf-8", errors="ignore")

    return f"# {txt_path.stem}\n\n{content}"


def add_frontmatter(content, source_path):

    fm = f"""---

source_file: "{source_path.name}"

source_format: "{source_path.suffix}"
converted_at: "{datetime.now().isoformat()}"

original_path: "{source_path}"

---



"""
    return fm + content



CONVERTERS = {

    ".pdf": convert_pdf,
    ".docx": convert_docx,

    ".html": convert_html,

    ".htm": convert_html,

    ".txt": convert_txt,

    ".md": lambda p: p.read_text(encoding="utf-8", errors="ignore"),
}



def main():

    if not RAW_BUCKET.exists():

        print(f"ERROR: {RAW_BUCKET} does not exist")
        sys.exit(1)



    CURATED.mkdir(parents=True, exist_ok=True)



    converted = 0
    skipped = 0

    errors = 0



    for file_path in RAW_BUCKET.rglob("*"):

        if not file_path.is_file():
            continue



        ext = file_path.suffix.lower()


        if ext not in CONVERTERS:

            skipped += 1

            continue


        rel_path = file_path.relative_to(RAW_BUCKET)

        out_path = CURATED / rel_path.with_suffix(".md")

        out_path.parent.mkdir(parents=True, exist_ok=True)


        if out_path.exists():

            if out_path.stat().st_mtime >= file_path.stat().st_mtime:

                skipped += 1

                continue


        try:

            content = CONVERTERS[ext](file_path)

            content_with_meta = add_frontmatter(content, file_path)

            out_path.write_text(content_with_meta, encoding="utf-8")

            print(f"  ✓ {file_path.name} → {out_path.name}")
            converted += 1

        except Exception as e:

            print(f"  ✗ {file_path.name}: {e}")

            errors += 1


    print(f"\nDone: {converted} converted, {skipped} skipped, {errors} errors")

    print(f"Output: {CURATED}")



if __name__ == "__main__":

    main()
PYEOF



chmod +x "\$HOME/convert-raw-to-md.py"

echo -e "\${GREEN}  ✓ Converter written to ~/convert-raw-to-md.py\${NC}"


# ─── 6. WRITE JSONL MARKER SCRIPT ────────────────────────────

echo -e "\n\${YELLOW}[6/9] WRITING JSONL MARKER GENERATOR\${NC}"



cat > "\$HOME/generate-jsonl-markers.py" << 'PYEOF'
#!/usr/bin/env python3

"""

JSONL Marker Generator — processes source docs and OpenWiki output

Produces universal-index.jsonl with markers for everything

"""
import json

import hashlib

from pathlib import Path

from datetime import datetime


SOURCES = [

    Path("~/novae-xorpus").expanduser(),

    Path("~/.openwiki/wiki").expanduser(),

]


OUTPUT = Path("~/universal-index.jsonl").expanduser()



def make_marker(file_path, source_type):

    content = file_path.read_text(encoding="utf-8", errors="ignore")


    title = file_path.stem

    for line in content.split("\n"):

        if line.startswith("# "):

            title = line.lstrip("# ").strip()

            break


    description = ""

    for line in content.split("\n"):

        stripped = line.strip()

        if stripped and not stripped.startswith("#") and not stripped.startswith("---"):
            description = stripped[:200]

            break



    tokens = set()

    for line in content.split("\n"):
        if line.startswith("##") or line.startswith("###"):

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

        "source_type": source_type,
        "category": "TECHNICAL_REFERENCE",

        "metadata": {

            "title": title,

            "description": description,

            "content_hash": content_hash,
            "file_size_bytes": len(content.encode()),

            "last_modified": datetime.fromtimestamp(

                file_path.stat().st_mtime

            ).isoformat()

        },
        "retrieval_tokens": list(tokens)[:15],

        "entry_points": {

            "repl_command": f"/skill run {file_path.stem.lower().replace(' ', '-')}",

            "jsonrpc_method": "agent.skills.execute"
        }

    }



def main():

    markers = []


    for source_dir in SOURCES:

        if not source_dir.exists():

            print(f"  Skipping {source_dir} — not found")

            continue


        source_type = "RAW_SOURCE" if "novae" in str(source_dir) else "WIKI_SYNTHESIS"



        for md_file in source_dir.rglob("*.md"):

            try:
                marker = make_marker(md_file, source_type)

                markers.append(marker)

                print(f"  [{len(markers):04d}] {source_type}: {md_file.name}")

            except Exception as e:

                print(f"  ERROR on {md_file}: {e}")


    with open(OUTPUT, "w") as f:

        for marker in markers:

            f.write(json.dumps(marker, ensure_ascii=False) + "\n")


    raw_count = sum(1 for m in markers if m["source_type"] == "RAW_SOURCE")

    wiki_count = sum(1 for m in markers if m["source_type"] == "WIKI_SYNTHESIS")



    print(f"\nDone: {len(markers)} markers → {OUTPUT}")

    print(f"  Raw sources: {raw_count}")
    print(f"  Wiki synthesis: {wiki_count}")



if __name__ == "__main__":

    main()

PYEOF


chmod +x "\$HOME/generate-jsonl-markers.py"

echo -e "\${GREEN}  ✓ JSONL marker generator written to ~/generate-jsonl-markers.py\${NC}"



# ─── 7. RUN CONVERTER ───────────────────────────────────────
echo -e "\n\${YELLOW}[7/9] CONVERTING RAW FILES → MARKDOWN\${NC}"



if [ "\$(find "\$RAW_DIR" -type f | head -1)" ]; then

    python3 "\$HOME/convert-raw-to-md.py"

    echo -e "\${GREEN}  ✓ Raw files converted to novae-xorpus/01-sources/\${NC}"
else

    echo -e "\${YELLOW}  raw-bucket is empty — nothing to convert yet.\${NC}"

    echo -e "\${YELLOW}  Add files to ~/raw-bucket/ and re-run converter later.\${NC}"

fi


# ─── 8. INITIALIZE OPENWIKI (INTERACTIVE) ────────────────────

echo -e "\n\${YELLOW}[8/9] INITIALIZING OPENWIKI\${NC}"

echo -e "\${CYAN}  ────────────────────────────────────────────\${NC}"

echo -e "\${CYAN}  This step is INTERACTIVE. When prompted:\${NC}"

echo -e "\${CYAN}  → Provider: select OpenRouter\${NC}"
echo -e "\${CYAN}  → API key: your OpenRouter key (already in env)\${NC}"

echo -e "\${CYAN}  → Model: z-ai/glm-5.2\${NC}"

echo -e "\${CYAN}  → Connector: git-repo, path: ~/novae-xorpus\${NC}"

echo -e "\${CYAN}  → Scope: AESOP XI architecture, model pathways,\${NC}"

echo -e "\${CYAN}    tool harnesses, and build priorities\${NC}"
echo -e "\${CYAN}  ────────────────────────────────────────────\${NC}"

echo ""

read -p "  Press Enter to launch openwiki init (or Ctrl+C to skip)..."


openwiki personal --init



echo -e "\${GREEN}  ✓ OpenWiki initialized\${NC}"



# ─── 9. RUN SYNTHESIS + JSONL MARKERS ────────────────────────
echo -e "\n\${YELLOW}[9/9] RUNNING SYNTHESIS + JSONL MARKERS\${NC}"



echo -e "\${YELLOW}  Running OpenWiki synthesis (GLM 5.2 reads your docs)...\${NC}"

openwiki personal --update "Initial synthesis from curated documentation"


echo -e "\${YELLOW}  Generating JSONL markers...\${NC}"

python3 "\$HOME/generate-jsonl-markers.py"



# ─── DONE ────────────────────────────────────────────────────

echo -e "\n\${GREEN}================================================\${NC}"
echo -e "\${GREEN}  SETUP COMPLETE\${NC}"

echo -e "\${GREEN}================================================\${NC}"

echo ""

echo "What was installed:"

echo "  • Node.js LTS, Python, Git, tmux"
echo "  • pymupdf, python-docx, markdownify (file converters)"

echo "  • openwiki (wiki engine)"

echo "  • OpenRouter + GLM 5.2 configured"

echo ""

echo "Scripts created:"
echo "  ~/convert-raw-to-md.py     — converts raw files to markdown"

echo "  ~/generate-jsonl-markers.py — generates JSONL markers"

echo ""

echo "Directories:"

echo "  ~/raw-bucket/              — your raw file dump (any format)"
echo "  ~/novae-xorpus/             — curated markdown repo"

echo "  ~/novae-xorpus/01-sources/ — converted markdown from raw-bucket"

echo "  ~/.openwiki/wiki/           — GLM 5.2 synthesized wiki output"

echo "  ~/universal-index.jsonl     — JSONL markers for everything"

echo ""
echo "Daily workflow:"

echo "  1. Add raw files to ~/raw-bucket/"


How to Run It

It will pause twice for input:

1. OpenRouter API key — if you don’t have it in your environment
2. OpenWiki init — interactive prompts where you select OpenRouter, GLM 5.2, and point it at novae-xorpus

Everything else is automated. If any step fails, it stops and tells you what went wrong. If npm install -g openwiki takes too long or runs out of memory, run the whole thing inside tmux:

echo "  2. python3 ~/convert-raw-to-md.py"

echo "  3. openwiki personal --update \"description of what's new\""

echo "  4. python3 ~/generate-jsonl-markers.py"
echo ""

echo -e "\${CYAN}Open Obsidian → Open folder as vault → ~/.openwiki/wiki/\${NC}"

echo -e "\${CYAN}to browse the wiki GLM 5.2 synthesized.\${NC}"

# Save the script
nano ~/setup-aesop.sh

# Paste the above, save: Ctrl+O, Enter, Ctrl+X



# Make executable

chmod +x ~/setup-aesop.sh


# Run it

~/setup-aesop.sh

tmux new-session -s setup

~/setup-aesop.sh
# If Termux closes: tmux attach -t setup
