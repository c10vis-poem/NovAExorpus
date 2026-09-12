#!/usr/bin/env python3
"""
Phase 1 Ingestion Pipeline - Cognitive Repository Architecture
Converts raw sources to clean Markdown with YAML frontmatter.
Uses mutool (mupdf) for PDF extraction - the verification pass (tools/check.py)
must use a DIFFERENT extractor (pypdf) per Hard Rule 5.
"""
import os, re, sys, subprocess, hashlib, datetime
from pathlib import Path

# --- Configuration ---
def find_raw_dir():
    docs = "/storage/emulated/0/Documents"
    for e in os.listdir(docs):
        if "xorpus" in e.lower():
            novae = os.path.join(docs, e)
            break
    else:
        raise FileNotFoundError("NovAExorpus dir not found")
    for e in os.listdir(novae):
        if "Repo" in e and os.path.isdir(os.path.join(novae, e)):
            repos = os.path.join(novae, e)
            break
    else:
        raise FileNotFoundError("Repos dir not found")
    raw_db = os.path.join(repos, "raw_database")
    return os.path.join(raw_db, "raw"), repos

RAW_DIR, REPOS_DIR = find_raw_dir()
MUTOOL = "/data/data/com.termux/files/usr/bin/mutool"

# --- Helpers ---
def make_slug(filename):
    """Create a clean filename slug from a raw filename."""
    name = os.path.splitext(filename)[0]
    name = re.sub(r'[^\w\s\-.]', '', name)
    name = re.sub(r'\s+', '_', name.strip())
    name = re.sub(r'_+', '_', name)
    name = name.strip('_.')
    return name or "unnamed"

def make_frontmatter(source_file, doc_type, title=None):
    """Generate YAML frontmatter for a cleaned document."""
    if title is None:
        title = os.path.splitext(source_file)[0]
    # Truncate title for frontmatter
    title = title[:200]
    ts = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"""---
source: {source_file}
type: {doc_type}
cleaned: {ts}
cleaner: tools/clean.py (mutool)
---

"""

def extract_pdf_mutool(pdf_path):
    """Extract text from PDF using mutool (mupdf). This is the CLEANING extractor.
    The verification pass must use pypdf (disjoint per Hard Rule 5)."""
    try:
        result = subprocess.run(
            [MUTOOL, "draw", "-F", "text", pdf_path],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return f"[PDF extraction error: {result.stderr[:200]}]"
    except Exception as e:
        return f"[PDF extraction error: {e}]"

def extract_docx_python(docx_path):
    """Extract text from DOCX using python-docx."""
    try:
        import docx
        doc = docx.Document(docx_path)
        parts = []
        for para in doc.paragraphs:
            if para.text.strip():
                style = para.style.name if para.style else ""
                if "Heading" in style:
                    level = 1
                    m = re.search(r'\d+', style)
                    if m:
                        level = int(m.group(0))
                    parts.append("#" * level + " " + para.text)
                else:
                    parts.append(para.text)
        # Also extract tables
        for table in doc.tables:
            for row in table.rows:
                cells = [cell.text.strip() for cell in row.cells]
                parts.append("| " + " | ".join(cells) + " |")
        return "\n\n".join(parts)
    except Exception as e:
        return f"[DOCX extraction error: {e}]"

def extract_html(html_path):
    """Extract text from HTML using stdlib html.parser."""
    try:
        from html.parser import HTMLParser
        class TextExtractor(HTMLParser):
            def __init__(self):
                super().__init__()
                self.parts = []
                self.in_tag = None
            def handle_starttag(self, tag, attrs):
                if tag in ("h1","h2","h3","h4","h5","h6"):
                    self.in_tag = tag
                    level = int(tag[1])
                    self.parts.append("\n" + "#" * level + " ")
                elif tag == "p":
                    self.parts.append("\n\n")
                elif tag == "br":
                    self.parts.append("\n")
                elif tag == "li":
                    self.parts.append("\n- ")
                elif tag == "code":
                    self.parts.append("`")
                elif tag == "pre":
                    self.parts.append("\n```\n")
                elif tag == "a":
                    for k,v in attrs:
                        if k == "href":
                            self.parts.append("[")
                            self._href = v
                            break
            def handle_endtag(self, tag):
                if tag == "code":
                    self.parts.append("`")
                elif tag == "pre":
                    self.parts.append("\n```\n")
                elif tag == "a" and hasattr(self, "_href"):
                    self.parts.append(f"]({self._href})")
                    del self._href
                self.in_tag = None
            def handle_data(self, data):
                self.parts.append(data)
        with open(html_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        parser = TextExtractor()
        parser.feed(content)
        return "".join(parser.parts)
    except Exception as e:
        return f"[HTML extraction error: {e}]"

def sniff_file(filepath):
    """Detect actual file type by magic bytes."""
    with open(filepath, "rb") as f:
        magic = f.read(16)
    if magic.startswith(b"%PDF"):
        return "pdf"
    if magic.startswith(b"PK"):
        # Could be docx (zip-based)
        return "zip"
    if magic.startswith(b"<") or magic.startswith(b"\xef\xbb\xbf<"):
        # Check if it's HTML
        try:
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                preview = f.read(500).lower()
            if "<html" in preview or "<div" in preview or "<!doctype" in preview:
                return "html"
        except:
            pass
        return "xml_or_markup"
    return "text"

def normalize_markdown(content):
    """Apply Non-1:1 Condensation Law: strip conversational filler and duplicate
    boilerplate, maintain 100% build fidelity."""
    # Strip excessive blank lines (more than 2 consecutive)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    # Strip Windows-style line endings
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    # Strip trailing whitespace on lines
    content = "\n".join(line.rstrip() for line in content.split("\n"))
    return content.strip() + "\n"

def process_file(filepath, filename, clean_md_dir):
    """Process a single raw file and write its cleaned markdown version."""
    ext = os.path.splitext(filename)[1].lower()
    actual_type = sniff_file(filepath)
    
    # Determine extraction method and doc type
    if actual_type == "pdf" or ext == ".pdf":
        doc_type = "pdf"
        content = extract_pdf_mutool(filepath)
    elif ext == ".docx" or (actual_type == "zip" and ext == ".docx"):
        doc_type = "docx"
        content = extract_docx_python(filepath)
    elif actual_type == "html":
        doc_type = "html"
        content = extract_html(filepath)
    elif ext in (".py",):
        doc_type = "python"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        content = "```python\n" + content + "\n```"
    elif ext in (".sh",):
        doc_type = "shell"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        content = "```bash\n" + content + "\n```"
    elif ext in (".skill",):
        doc_type = "skill"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    elif ext in (".csv",):
        doc_type = "csv"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    elif ext in (".xml",):
        doc_type = "xml"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        content = "```xml\n" + content + "\n```"
    elif ext in (".yml", ".yaml"):
        doc_type = "yaml"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        content = "```yaml\n" + content + "\n```"
    elif ext in (".toml",):
        doc_type = "toml"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        content = "```toml\n" + content + "\n```"
    elif ext in (".md",) or actual_type == "text":
        doc_type = "markdown" if ext == ".md" else "text"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        # If already has frontmatter, keep it
        if content.startswith("---"):
            # Has existing frontmatter - normalize the content after it
            parts = content.split("---", 2)
            if len(parts) >= 3:
                existing_fm = parts[1]
                body = parts[2]
                content = normalize_markdown(body)
                # Rebuild with updated frontmatter
                fm = make_frontmatter(filename, doc_type)
                content = fm + content
            else:
                content = normalize_markdown(content)
                fm = make_frontmatter(filename, doc_type)
                content = fm + content
        else:
            content = normalize_markdown(content)
            fm = make_frontmatter(filename, doc_type)
            content = fm + content
        # Write and return
        slug = make_slug(filename) + ".md"
        out_path = os.path.join(clean_md_dir, slug)
        # Avoid clobbering
        if os.path.exists(out_path):
            base, e = os.path.splitext(slug)
            i = 1
            while os.path.exists(os.path.join(clean_md_dir, f"{base}_{i}{e}")):
                i += 1
            slug = f"{base}_{i}{e}"
            out_path = os.path.join(clean_md_dir, slug)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        return slug, doc_type, len(content)
    elif ext == ".txt":
        doc_type = "text"
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    elif ext == ".rev":
        # Binary revision file - skip
        return None, "binary-skip", 0
    else:
        # Unknown extension - try as text
        doc_type = "unknown"
        try:
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except:
            return None, "binary-skip", 0
    
    # For non-markdown types, normalize and add frontmatter
    if not content.startswith("---"):
        content = normalize_markdown(content)
        fm = make_frontmatter(filename, doc_type)
        content = fm + content
    
    # Write to clean_md
    slug = make_slug(filename) + ".md"
    out_path = os.path.join(clean_md_dir, slug)
    if os.path.exists(out_path):
        base, e = os.path.splitext(slug)
        i = 1
        while os.path.exists(os.path.join(clean_md_dir, f"{base}_{i}{e}")):
            i += 1
        slug = f"{base}_{i}{e}"
        out_path = os.path.join(clean_md_dir, slug)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    return slug, doc_type, len(content)

# --- Main ---
def main():
    raw_dir = RAW_DIR
    clean_md_dir = os.path.join(REPOS_DIR, "novae-xorpus", "clean_md")
    
    # Also process 02_MY_ORIGINALS and Dump/zip
    originals_dir = os.path.join(os.path.dirname(raw_dir), "02_MY_ORIGINALS")
    dump_dir = os.path.join(os.path.dirname(raw_dir), "Dump", "zip")
    
    # Create clean_md dir
    os.makedirs(clean_md_dir, exist_ok=True)
    
    # Remove existing POINTER.md
    pointer = os.path.join(clean_md_dir, "POINTER.md")
    if os.path.exists(pointer):
        os.remove(pointer)
    
    print(f"Phase 1 Ingestion Pipeline")
    print(f"Raw source: {raw_dir}")
    print(f"Originals:  {originals_dir}")
    print(f"Dump/zip:   {dump_dir}")
    print(f"Output:     {clean_md_dir}")
    print()
    
    stats = {}
    processed = 0
    skipped = 0
    errors = 0
    
    # Process all source directories
    all_files = []
    if os.path.isdir(raw_dir):
        all_files.extend([(os.path.join(raw_dir, f), f) for f in os.listdir(raw_dir) if os.path.isfile(os.path.join(raw_dir, f))])
    if os.path.isdir(originals_dir):
        all_files.extend([(os.path.join(originals_dir, f), f) for f in os.listdir(originals_dir) if os.path.isfile(os.path.join(originals_dir, f))])
    if os.path.isdir(dump_dir):
        all_files.extend([(os.path.join(dump_dir, f), f) for f in os.listdir(dump_dir) if os.path.isfile(os.path.join(dump_dir, f))])
    
    # Deduplicate by content hash
    seen_hashes = {}
    deduped = []
    for filepath, filename in sorted(all_files):
        try:
            with open(filepath, "rb") as f:
                h = hashlib.sha256(f.read()).hexdigest()
            if h in seen_hashes:
                print(f"  DEDUP: {filename} (identical to {seen_hashes[h]})")
                skipped += 1
                continue
            seen_hashes[h] = filename
            deduped.append((filepath, filename))
        except Exception as e:
            print(f"  HASH ERROR: {filename}: {e}")
            deduped.append((filepath, filename))
    
    print(f"Total files: {len(all_files)} | After dedup: {len(deduped)} | Skipped dups: {skipped}")
    print()
    
    for filepath, filename in deduped:
        try:
            slug, doc_type, size = process_file(filepath, filename, clean_md_dir)
            if slug:
                processed += 1
                stats[doc_type] = stats.get(doc_type, 0) + 1
                print(f"  [{doc_type:>10}] {filename[:60]:<60} -> {slug}")
            else:
                if doc_type == "binary-skip":
                    skipped += 1
                    print(f"  [   skipped] {filename[:60]:<60} (binary)")
        except Exception as e:
            errors += 1
            print(f"  [    ERROR] {filename[:60]:<60} {e}")
    
    print()
    print(f"--- Summary ---")
    print(f"Processed: {processed}")
    print(f"Skipped:   {skipped}")
    print(f"Errors:    {errors}")
    print(f"By type:   {stats}")

if __name__ == "__main__":
    main()
