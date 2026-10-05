#!/usr/bin/env python3
"""
Raw Bucket -> Markdown Converter
Converts PDF, DOCX, TXT, HTML -> markdown for OpenWiki / RAG ingestion
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
            print(f" ✓ {file_path.name} -> {out_path.name}")
            converted += 1
        except Exception as e:
            print(f" ✗ {file_path.name}: {e}")
            errors += 1

    print(f"\nDone: {converted} converted, {skipped} skipped, {errors} errors")
    print(f"Output: {CURATED}")

if __name__ == "__main__":
    main()
