#!/usr/bin/env python3
"""
Phase 3: Pre-tokenized Chunking & SHA-256 Manifest Cataloging
Reads clean_md/ files, splits into chunks, writes chunk.jsonl and manifest.jsonl
with SHA-256 checksums for RAG retrieval.
"""
import os, re, json, hashlib

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
    novae_xorpus = os.path.join(repos, "novae-xorpus")
    return os.path.join(novae_xorpus, "clean_md"), novae_xorpus

CLEAN_DIR, REPO_ROOT = find_dirs()
CHUNK_SIZE = 2048  # chars per chunk
CHUNK_OVERLAP = 200  # overlap between chunks

def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split text into overlapping chunks at paragraph boundaries."""
    # Strip frontmatter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].strip()
    
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        if end < len(text):
            # Try to break at a paragraph or line boundary
            for boundary in ["\n\n", "\n", ". "]:
                last = text.rfind(boundary, end - overlap, end + overlap)
                if last > start:
                    end = last + len(boundary)
                    break
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap if end < len(text) else end
    return chunks

def sha256(data):
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def get_frontmatter(text):
    """Extract frontmatter as a dict."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            result = {}
            for line in fm_text.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    result[k.strip()] = v.strip()
            return result, parts[2].strip()
    return {}, text

def main():
    chunk_path = os.path.join(REPO_ROOT, "chunk.jsonl")
    manifest_path = os.path.join(REPO_ROOT, "manifest.jsonl")
    
    clean_files = sorted([f for f in os.listdir(CLEAN_DIR) if f.endswith(".md")])
    print(f"Phase 3: Chunking & Manifest Cataloging")
    print(f"Clean files: {len(clean_files)}")
    print(f"Chunk size: {CHUNK_SIZE} chars, overlap: {CHUNK_OVERLAP}")
    print()
    
    chunks_written = 0
    manifest_entries = []
    
    with open(chunk_path, "w", encoding="utf-8") as chunk_file:
        for clean_file in clean_files:
            clean_path = os.path.join(CLEAN_DIR, clean_file)
            with open(clean_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            fm, body = get_frontmatter(content)
            file_hash = sha256(content)
            chunks = chunk_text(content)
            
            for i, chunk in enumerate(chunks):
                chunk_entry = {
                    "file": clean_file,
                    "chunk": i,
                    "source": fm.get("source", ""),
                    "type": fm.get("type", ""),
                    "sha256": sha256(chunk),
                    "text": chunk
                }
                chunk_file.write(json.dumps(chunk_entry, ensure_ascii=False) + "\n")
                chunks_written += 1
            
            manifest_entries.append({
                "file": clean_file,
                "source": fm.get("source", ""),
                "type": fm.get("type", ""),
                "sha256": file_hash,
                "chunks": len(chunks),
                "bytes": os.path.getsize(clean_path)
            })
            
            print(f"  {clean_file[:60]:<60} -> {len(chunks)} chunks")
    
    with open(manifest_path, "w", encoding="utf-8") as manifest_file:
        for entry in manifest_entries:
            manifest_file.write(json.dumps(entry, ensure_ascii=False) + "\n")
    
    print()
    print(f"--- Summary ---")
    print(f"Files cataloged: {len(manifest_entries)}")
    print(f"Chunks written: {chunks_written}")
    print(f"Manifest: {manifest_path}")
    print(f"Chunks:  {chunk_path}")

if __name__ == "__main__":
    main()
