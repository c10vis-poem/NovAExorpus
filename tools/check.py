#!/usr/bin/env python3
"""
Phase 2 RLVR Validation - Corpus Verify (Hard Rule 5)
Independent verification that content survived the cleaning pass.
Uses DISJOINT extractors from tools/clean.py:
  - PDF: clean.py uses mutool (mupdf/C); check.py uses pypdf (pure Python)
  - DOCX: clean.py uses python-docx; check.py uses stdlib zipfile + xml.etree
  - HTML: clean.py uses stdlib html.parser; check.py uses BeautifulSoup4
  - Text: clean.py uses open().read(); check.py uses byte read + encoding probe
The tool that cleaned a file does not get a vote on whether the cleaning was good.
"""
import os, re, sys, hashlib, unicodedata
from pathlib import Path

def find_dirs():
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
    raw_dir = os.path.join(repos, "raw_database", "raw")
    originals_dir = os.path.join(repos, "raw_database", "02_MY_ORIGINALS")
    clean_dir = os.path.join(repos, "novae-xorpus", "clean_md")
    audit_dir = os.path.join(repos, "novae-xorpus", "audit")
    return raw_dir, originals_dir, clean_dir, audit_dir

RAW_DIR, ORIGINALS_DIR, CLEAN_DIR, AUDIT_DIR = find_dirs()

def squash(s):
    """Fold Unicode to ASCII, lowercase, strip non-alphanumeric. For containment checks.
    Does NOT concatenate - preserves token boundaries so atoms can be compared individually."""
    s = unicodedata.normalize("NFD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.lower()
    s = re.sub(r"[^a-z0-9]", " ", s)
    return s

def extract_pdf_pypdf(pdf_path):
    """PDF extraction using pypdf (DISJOINT from clean.py's mutool)."""
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    parts = []
    for page in reader.pages:
        parts.append(page.extract_text())
    return "\n".join(parts)

def extract_docx_stdlib(docx_path):
    """DOCX extraction using stdlib zipfile + xml.etree (DISJOINT from clean.py's python-docx)."""
    import zipfile
    import xml.etree.ElementTree as ET
    with zipfile.ZipFile(docx_path) as z:
        # Read word/document.xml
        with z.open("word/document.xml") as f:
            tree = ET.parse(f)
        root = tree.getroot()
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        parts = []
        for para in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
            texts = []
            for t in para.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"):
                if t.text:
                    texts.append(t.text)
            if texts:
                parts.append("".join(texts))
        return "\n".join(parts)

def extract_html_bs4(html_path):
    """HTML extraction using BeautifulSoup4 (DISJOINT from clean.py's stdlib html.parser)."""
    from bs4 import BeautifulSoup
    with open(html_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text(separator="\n")

def extract_text_bytes(filepath):
    """Text extraction via byte read + encoding probe (DISJOINT from clean.py's utf-8 open)."""
    with open(filepath, "rb") as f:
        raw = f.read()
    # Try utf-8, then latin-1, then ascii
    for enc in ["utf-8", "latin-1", "ascii"]:
        try:
            return raw.decode(enc)
        except:
            continue
    return raw.decode("utf-8", errors="replace")

def sniff_file(filepath):
    with open(filepath, "rb") as f:
        magic = f.read(16)
    if magic.startswith(b"%PDF"):
        return "pdf"
    if magic.startswith(b"PK"):
        return "docx"
    if magic.startswith(b"<") or magic.startswith(b"\xef\xbb\xbf<"):
        try:
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                preview = f.read(500).lower()
            if "<html" in preview or "<div" in preview or "<!doctype" in preview:
                return "html"
        except:
            pass
        return "xml"
    return "text"

def get_source_file(clean_file_path):
    """Extract the source filename from the YAML frontmatter."""
    with open(clean_file_path, "r", encoding="utf-8") as f:
        content = f.read(500)
    m = re.search(r"source:\s*(.+)", content)
    if m:
        return m.group(1).strip()
    return None

def find_source(source_name, raw_dir, originals_dir):
    """Find the source file in raw/ or 02_MY_ORIGINALS/."""
    for search_dir in [raw_dir, originals_dir]:
        if os.path.isdir(search_dir):
            for f in os.listdir(search_dir):
                if f == source_name:
                    return os.path.join(search_dir, f)
    return None

def check_containment(source_text, clean_text):
    """Check if key atoms from the source survived in the clean version.
    Uses squash() for whitespace/punctuation-insensitive containment.
    Atoms are individual words/tokens (4+ chars), not concatenated strings."""
    source_sq = squash(source_text)
    clean_sq = squash(clean_text)
    
    # Extract significant atoms (individual words of 4+ chars)
    source_atoms = set(re.findall(r"\b[a-z0-9]{4,}\b", source_sq))
    clean_atoms = set(re.findall(r"\b[a-z0-9]{4,}\b", clean_sq))
    
    if not source_atoms:
        return {"missing": [], "coverage": 100.0}
    
    missing = source_atoms - clean_atoms
    coverage = (1 - len(missing) / len(source_atoms)) * 100.0
    
    # Filter out very common short atoms that might differ due to extraction artifacts
    significant_missing = [a for a in missing if len(a) >= 6]
    
    return {
        "missing": sorted(significant_missing)[:20],
        "missing_count": len(missing),
        "total_source_atoms": len(source_atoms),
        "coverage": round(coverage, 1)
    }

def main():
    dry_run = "--dry-run" in sys.argv
    
    os.makedirs(AUDIT_DIR, exist_ok=True)
    # Remove existing POINTER.md
    pointer = os.path.join(AUDIT_DIR, "POINTER.md")
    if os.path.exists(pointer):
        os.remove(pointer)
    
    print("Phase 2 RLVR Validation - Corpus Verify")
    print(f"Raw:    {RAW_DIR}")
    print(f"Clean:  {CLEAN_DIR}")
    print(f"Audit:  {AUDIT_DIR}")
    print()
    
    clean_files = [f for f in os.listdir(CLEAN_DIR) if f.endswith(".md")]
    print(f"Clean files to verify: {len(clean_files)}")
    print()
    
    results = []
    passed = 0
    failed = 0
    warnings = 0
    
    for clean_file in sorted(clean_files):
        clean_path = os.path.join(CLEAN_DIR, clean_file)
        source_name = get_source_file(clean_path)
        
        if not source_name:
            warnings += 1
            results.append((clean_file, "NO_SOURCE", "No source in frontmatter"))
            print(f"  [  WARN] {clean_file[:60]:<60} no source in frontmatter")
            continue
        
        source_path = find_source(source_name, RAW_DIR, ORIGINALS_DIR)
        if not source_path:
            warnings += 1
            results.append((clean_file, "SOURCE_NOT_FOUND", source_name))
            print(f"  [  WARN] {clean_file[:60]:<60} source not found: {source_name}")
            continue
        
        # Extract source text using DISJOINT extractor
        source_type = sniff_file(source_path)
        ext = os.path.splitext(source_name)[1].lower()
        
        try:
            if source_type == "pdf" or ext == ".pdf":
                source_text = extract_pdf_pypdf(source_path)
            elif source_type == "docx" or ext == ".docx":
                source_text = extract_docx_stdlib(source_path)
            elif source_type == "html":
                source_text = extract_html_bs4(source_path)
            else:
                source_text = extract_text_bytes(source_path)
        except Exception as e:
            warnings += 1
            results.append((clean_file, "EXTRACT_ERROR", str(e)))
            print(f"  [  WARN] {clean_file[:60]:<60} extract error: {e}")
            continue
        
        # Read clean text (strip frontmatter)
        with open(clean_path, "r", encoding="utf-8") as f:
            clean_content = f.read()
        # Strip frontmatter
        if clean_content.startswith("---"):
            parts = clean_content.split("---", 2)
            if len(parts) >= 3:
                clean_body = parts[2]
            else:
                clean_body = clean_content
        else:
            clean_body = clean_content
        
        # Check containment
        result = check_containment(source_text, clean_body)
        
        if result["coverage"] >= 80.0:
            passed += 1
            status = "PASS"
            print(f"  [  PASS] {clean_file[:60]:<60} {result['coverage']}% coverage")
        elif result["coverage"] >= 50.0:
            warnings += 1
            status = "WARN"
            print(f"  [  WARN] {clean_file[:60]:<60} {result['coverage']}% coverage, {result['missing_count']} atoms missing")
        else:
            failed += 1
            status = "FAIL"
            print(f"  [  FAIL] {clean_file[:60]:<60} {result['coverage']}% coverage, missing: {result['missing'][:5]}")
        
        results.append((clean_file, status, result))
    
    print()
    print("--- Summary ---")
    print(f"Total:   {len(results)}")
    print(f"Passed:  {passed}")
    print(f"Warning: {warnings}")
    print(f"Failed:  {failed}")
    
    if not dry_run:
        # Write audit report
        report_path = os.path.join(AUDIT_DIR, "rlvr_verification_report.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("---\nsource: tools/check.py (pypdf/zipfile+xml.etree/BeautifulSoup4)\ntype: rlvr-audit\n---\n\n")
            f.write("# Phase 2 RLVR Verification Report\n\n")
            f.write(f"Total: {len(results)} | Passed: {passed} | Warning: {warnings} | Failed: {failed}\n\n")
            f.write("| File | Status | Coverage | Missing Atoms |\n")
            f.write("|------|--------|----------|---------------|\n")
            for clean_file, status, result in results:
                if isinstance(result, dict) and "coverage" in result:
                    missing = ", ".join(result.get("missing", [])[:5])
                    f.write(f"| {clean_file} | {status} | {result['coverage']}% | {missing} |\n")
                else:
                    f.write(f"| {clean_file} | {status} | - | {result} |\n")
        print(f"\nReport written to: {report_path}")

if __name__ == "__main__":
    main()
