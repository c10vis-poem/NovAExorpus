---
title: "c10vis-poem_llama.cpp_ LLM inference in C_C++"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ/--•📱📎_GITHUB_📂💻~/#REPO.s/c10vis-poem_llama.cpp_ LLM inference in C_C++.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

Watch
0
LLM inference in C/C++
MIT License
llama.app
Contributing
Security policy
0 stars
0 forks
0 watching
1 branch
1 tag
Activity
Public repository · Forked from ggml-org/llama.cpp
1 Branch
1 Tag
Go to file
Go to file
Add file
Code
This branch is up to date with ggml-org/llama.cpp:master .
Contribute
Sync fork
ramicaza cli : persist reasoning_content in chat history (ggml-org#26362)
c629da5 · 33 minutes ago
.devops
devops : add llama in all docker images (gg…
2 months ago
.gemini
contributing: tighten AI usage policy (ggml-o…
8 months ago
.github
vulkan: update vulkan sdk to 1.4.357.0 (ggm…
yesterday
.pi/gg
pi : remove docs from system prompt (ggml…
2 months ago
app
app : allow --version, --licenses & --help (ggm…
2 months ago
benches
benches : add Nemotron 3 Nano on DGX Sp…
5 months ago
ci
common : fix env names to all have LLAMA_…
3 months ago
cmake
cmake : do not check for bin install dir (ggm…
3 months ago
common
chat : enable tool call in thinking for DS4 (gg…
11 hours ago
conversion
mtmd: add minicpmv46 downsample (ggml-…
5 hours ago
docs
SYCL: add oneMKL GEMM flash attention fo…
yesterday
examples
args: refactor mlock/mmap/directio into loa…
last week
ggml
vulkan: add POOL_1D op (ggml-org#25431)
yesterday
gguf-py
mtmd: add n_embd_head (ggml-org#26342)
yesterday
grammars
docs : fix typos in CUDA-FEDORA.md and gr…
2 months ago
include
llama : load MTP tensors only if they are real…
yesterday
licenses
refactor : remove libcurl, use OpenSSL when…
7 months ago
media
media : add transparent icon svg and png [n…
11 months ago
models
common/chat: add specialized minimax m3…
4 days ago
pocs
libs : rename libcommon -> libllama-commo…
4 months ago
requirements
model: add Mellum architecture (ggml-org#…
2 months ago
c10vis-poem
llama.cpp
Code
Pull requests
Agents
Actions
Projects
Wiki
Security and quality
Insights
Settings
Fork
0
m…
T


scripts
sync : ggml
2 days ago
skills
docs: add exception about weight folding (g…
5 days ago
src
Support rotated kv cache quant (ggml-org#…
yesterday
tests
chat : enable tool call in thinking for DS4 (gg…
11 hours ago
tools
cli : persist reasoning_content in chat histor…
33 minutes ago
vendor
vendor: update BoringSSL to 0.20260728.0 (…
3 days ago
.clang-format
fix: apply clang-format to CUDA macros (gg…
11 months ago
.clang-tidy
clang-tidy : disable warning about performa…
11 months ago
.dockerignore
docker : prebuild web UI for s390x build [no …
2 months ago
.ecrc
common : Update stb_image.h to latest vers…
2 years ago
.editorconfig
ui: Restructure repo to use tools/ui folder a…
3 months ago
.flake8
llama : move end-user examples to tools dir…
last year
.gitignore
ui: PWA support (ggml-org#23871)
2 months ago
.gitmodules
ggml : remove kompute backend (ggml-org…
last year
.pre-commit-config.yaml
convert.py : add python logging instead of p…
2 years ago
AGENTS.md
skill: create add-new-model and code-revie…
last week
AUTHORS
authors : update (ggml-org#19263)
6 months ago
CLAUDE.md
contributing: tighten AI usage policy (ggml-o…
8 months ago
CMakeLists.txt
common: add subproc.h wrapper, disabled …
last week
CMakePresets.json
cmake : Add CMake presets for Linux and G…
last year
CODEOWNERS
HIP: remove rocWMMA FlashAttention (gg…
last week
CONTRIBUTING.md
contrib : add guideline about the "merge rea…
4 days ago
LICENSE
docs : Minor cleanups (ggml-org#19252)
6 months ago
Makefile
make : remove make in favor of CMake (gg…
last year
README.md
readme : refresh (ggml-org#26280)
2 days ago
SECURITY.md
binaries : Improve rpc-server and export-gra…
2 months ago
build-xcframework.sh
xcframework : disable mtmd video on i/tv/vi…
2 months ago
convert_hf_to_gguf.py
convert_hf_to_gguf: support split MTP expo…
3 weeks ago
convert_hf_to_gguf_update.py
Add support for Laguna XS.2 & M.1 (ggml-or…
2 weeks ago
convert_llama_ggml_to_gguf.py
ci : switch from pyright to ty (ggml-org#208…
5 months ago
convert_lora_to_gguf.py
convert : fix lora base model arch retrieval (…
2 months ago
flake.nix
fix(nix): remove non-functional llama-cpp ca…
last year
mypy.ini
convert : partially revert PR ggml-org#4818 (…
2 years ago
pyproject.toml
model: add Mellum architecture (ggml-org#…
2 months ago
pyrightconfig.json
ci : switch from pyright to ty (ggml-org#208…
5 months ago


requirements.txt
tool-call: fix Qwen 2.5 Coder support, add …
last year
ty.toml
mtmd : DeepSeek-OCR image processing fix…
3 months ago
LLM inference in C/C++
license
license MIT
MIT
release
release b10218
b10218
Server
Server
passing
passing
Publish Docker image
Publish Docker image
failing
failing
Update Winget Package
Update Winget Package
passing
passing
manifesto / ggml / ops / maintainer PRs / dev branches / compile times / lib llama API / llama-server REST API
A few options to get llama.cpp installed on your machine:
Visit https://llama.app and follow the instructions
Run with Docker - see our Docker documentation
Download pre-built binaries from the releases page
Build from source by cloning this repository - check out our build guide
Once installed:
llama.cpp
Quick start
# Download and run a model directly from Hugging Face
llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF
# Launch OpenAI-compatible API server
llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF
README
Contributing
License
Security


VLM session with llama cli
Built-in web UI against llama serve
The main goal of llama.cpp is to enable LLM (and VLM) inference with minimal setup and state-of-the-art performance on a wide range of
hardware - locally and in the cloud.
Plain C/C++ implementation without any dependencies
Apple silicon is a first-class citizen - optimized via ARM NEON, Accelerate and Metal frameworks
AVX, AVX2, AVX512 and AMX support for x86 architectures
RVV, ZVFH, ZFH, ZICBOP and ZIHINTPAUSE support for RISC-V architectures
1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization for faster inference and reduced memory use
Custom CUDA kernels for running LLMs on NVIDIA GPUs (support for AMD GPUs via HIP and Moore Threads GPUs via MUSA)
Vulkan and SYCL backend support
CPU+GPU hybrid inference to partially accelerate models larger than the total VRAM capacity
The llama.cpp project is build on top of the ggml library.
Backend
Target devices
BLAS
All
BLIS
All
CANN
Ascend NPU
CUDA
Nvidia GPU
HIP
AMD GPU
Hexagon [In Progress]
Snapdragon
IBM zDNN
IBM Z & LinuxONE
MUSA
Moore Threads GPU
Metal
Apple Silicon
OpenCL
Adreno GPU
OpenVINO [In Progress]
Intel CPUs, GPUs, and NPUs
RPC
All
SYCL
Intel GPU
VirtGPU
VirtGPU APIR
Description
Supported backends


Backend
Target devices
Vulkan
GPU
WebGPU
All
ZenDNN
AMD CPU
cli
completion
server
GBNF grammars
How to build
Running on Docker
Build on Android
Multi-GPU usage
Performance troubleshooting
GGML tips & tricks
XCFramework
Completions
Models
Contributors can open PRs
Releases
1 tag
Create a new release
Packages
1
llama.cpp
Contributors
No contributors
Languages
C++ 55.1%
C 16.5%
Python 7.1%
Cuda 5.6%
TypeScript 4%
HTML 2.3%
Other 9.4%
Documentation
Tools
Development
Contributing
