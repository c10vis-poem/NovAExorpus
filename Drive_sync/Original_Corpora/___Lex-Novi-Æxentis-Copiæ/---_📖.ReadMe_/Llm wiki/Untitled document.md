---
title: "Untitled document"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ/---_📖.ReadMe_/Llm wiki/Untitled document.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Untangling the PDF Processing & JSONL Cache
Let’s clear up exactly what Docling does in your Termux environment and how you read the
data:
How it compiles: You give Docling a folder full of PDFs or raw text logs. It parses the files and
generates two outputs: a clean human-readable Markdown (.md) file and a machine-readable
JSONL file [1.5].
Can you open and close the JSONL? Yes. It isn't encrypted or compressed. It is just structured
line-
by-line code [1.5]. Your Termux CLI tools and local Qwen engine read the JSONL line-by-line to
instantaneously grab specific paragraphs without needing to read the entire massive document
again. This optimization keeps your Snapdragon 8 Elite's RAM completely clear.
The Strategy: Use the generated Markdown copy inside Obsidian to read it yourself. Let your
local
UI and Termux open-wiki CLI use the JSONL version behind the scenes for lightning-fast
keyword
caching and code retrieval.
4. Extracting Pure URLs from Chat History
If you dump a giant log file into Termux (like exporting this exact chat conversation) and want to
strip
out everything except clean, raw web addresses, run this command in Termux:
bash
GitHub
Reddit· r/Loc…
AI Mode All Images Videos News Maps Shopping Books Flights Finance grep -o 'https\?://[^" ]\+'
chat_log.txt | sort -u > clean_urls.txt
Use code with caution.
grep -o : Strips out all regular words and text, extracting only strings starting with http or https .
sort -u : Instantly deletes all duplicate links, giving you a perfectly unique list of resources saved
to
clean_urls.txt .
5. Getting a Printable PDF of a Chat Thread
If you want to instantly convert a raw web link or a saved HTML chat log directly into a clean,
presentation-ready PDF without ads or UI clutter, run it through PrintFriendly. It strips the
webpage
framework and formats the text natively into a clean document you can drop straight into your
storage.
Should we map out the system prompts for Qwen so it knows exactly how to handle code
conversions specifically for the Snapdragon 8 Elite's NPU architectures?
Llama 3.1
8B…
I did some
testing for …
Reddit
My


experie…
It seems the
prefix cache…
Reddit
Is qwen
2.5 code…
* Phi-4 has
awfully sma…
Reddit
Comparing
Open-…
1. Llama 3,
Qwen 2.5,…
www.ankursnew…
Qwen/Qwe
8B -…
Model
Overview.…
Hugging Face
The Qwen 3.5 4B Q4_0 is an absolute powerhouse for your Snapdragon 8 Elite setup.
Because Qwen 3.5 uses a unique, optimized hybrid Gated DeltaNet linear attention architecture
rather than heavy, traditional softmax attention layers, it delivers insanely high throughput
(tokens
per second) on edge devices. On your Elite's Oryon CPU, the Q4_0 matrix instructions will
compile
and process your text near-instantly while keeping your RAM usage incredibly light—leaving
plenty of
room to run your target UI, ONNX, and TFLite environments concurrently.
1. Booting Your Qwen 3.5 4B Server in Termux
Since you have the file ready, fire up the llama-cpp server inside Termux. Because Qwen 3.5
supports
a massive native context window, we will explicitly open up an 8,192 token canvas so you can
feed it
5 sites
Reddit· r/L… +1
Hugging F… +3
3:05AM
Okay, great cuz I got the QWEN3.54BQ4
{underscore} 0.
AI Mode All Images Videos News Maps Shopping Books Flights Finance deep repository files.
bash
# Start the local API server pointing to your downloaded file
llama-server -m /sdcard/Download/qwen3.5-4b-q4_0.gguf -c 8192 --host 0.0.0.0 --port 8080
Use code with caution.


Once this is running, your background terminal server is live. Your OpenWiki CLI, custom
scripts, or
your project UI can talk to it at http://localhost:8080/v1 .
2. Setting Up Your Specialized Fork Folders
Since you want to prevent a massive, messy directory on your Google Drive, let’s explicitly map
out
your separate, granular target frameworks. Creat
