---
source: System Mapping (1).txt
type: condensed
condensed_from: NovA-Corpus/condensed/termux-tool-pipeline-and-npu-prompts (2026-08-20)
original_moved_to: Merovingian's_keep/_salvage/NovA-Corpus/originals/
---

# System mapping: data-flow tool grid, and Snapdragon 8 Elite NPU system prompts

## System Mapping & Data Flow Graph

Maps how tools interact on a Snapdragon 8 Elite device: data starts as a raw URL or chat log, flows through extraction pipelines, compresses into local storage formats, and feeds the Termux engines.

**The process tool grid**:

| Input | Output | Tool |
|---|---|---|
| Raw Chat Thread Text | Unique text list of URLs | `grep` (built-in Termux command line) |
| Public Website URL | Clean, ad-free PDF | PrintFriendly (web scraper engine) |
| Raw Website URL | Pure text Markdown (.md) | Firecrawl / Jina AI Reader |
| PDFs / MD Files | Structured caching line file | Docling (Python pipeline) |
| PDF / Markdown / Docs | Pre-tokenized `.jsonl` | Docling |

## The Gemini/ChatGPT live-link exception

90% of scrapers say "Unable to open" on a live Gemini/ChatGPT/Claude chat URL because AI chats sit behind secure login walls and heavy JavaScript frameworks — external scraping engines only see a blank login screen.

**The fix to scrape a chat thread**:
1. Inside the Gemini/ChatGPT app, hit Share → Create Public Link.
2. Feed that public link to Firecrawl or Jina AI Reader.
3. Bulletproof mobile method: export the chat transcript as HTML, or copy-paste the text straight into a file named `chat_log.txt` inside Termux, then run local processing tools directly over it.

## Snapdragon 8 Elite NPU system prompts for Qwen

The Snapdragon 8 Elite's Hexagon NPU needs specialized vector extensions — standard ARM CPU code runs slowly. Force Qwen to wrap logic around Qualcomm's native runtimes: QNN (Qualcomm Neural Network) SDK and SNPE (Snapdragon Neural Processing Engine).

System instruction block for Qwen 3.5 when building for target forks:

```
You are an expert system optimization engineer specializing in the Qualcomm
Snapdragon 8 Elite (Oryon Architecture). Context: writing code conversions for
GGUF, ONNX, and TFLite runtimes targeted specifically for Android.

Strict Code Generation Instructions:
1. Target the Qualcomm Neural Network (QNN) API or SNPE workflows.
2. For TFLite conversions: explicitly define the hardware acceleration
   delegate to invoke the NPU.
3. For ONNX conversions: explicitly utilize the QNN Execution Provider
   ('QNNExecutionProvider') configuration.
4. Memory Constraint: optimize operations for LPDDR5X layout blocks. Avoid
   massive tensor copies in loops.
5. Output format: provide isolated code blocks matching the split
   architecture structure ('docs/core_wiki/'). No conversational filler.
```

## Termux script: quick-switch model engine

Alternates between a fast 4B model for text processing and a heavy 9B model for complex Snapdragon optimization tasks:

```bash
#!/bin/bash
MODEL_DIR="/sdcard/Download"
echo "Select your Qwen 3.5 Engine to boot:"
echo "1) Qwen 3.5 4B (Ultra-fast Wiki & Extraction)"
echo "2) Qwen 3.5 9B (Complex Code Optimization)"
read -p "Enter choice [1 or 2]: " choice
if [ "$choice" == "1" ]; then
  echo "Launching Qwen 3.5 4B..."
  llama-server -m "$MODEL_DIR/qwen3.5-4b-q4_0.gguf" -c 8192 --host 0.0.0.0 --port 8080
elif [ "$choice" == "2" ]; then
  echo "Launching Qwen 3.5 9B..."
  llama-server -m "$MODEL_DIR/qwen3.5-9b-instruct-q4_k_m.gguf" -c 4096 --host 0.0.0.0 --port 8080
else
  echo "Invalid selection."
fi
```

Save as `toggle_qwen.sh`, `chmod +x toggle_qwen.sh`, run with `./toggle_qwen.sh`.

## Testing the Termux local endpoint

Before letting an OpenWiki CLI handle automated syncing, verify the Termux network layer properly routes traffic to the running Qwen server: open two Termux sessions (swipe from the left edge → "New Session"), run the Qwen model server in session 1, and test the connection from session 2.
