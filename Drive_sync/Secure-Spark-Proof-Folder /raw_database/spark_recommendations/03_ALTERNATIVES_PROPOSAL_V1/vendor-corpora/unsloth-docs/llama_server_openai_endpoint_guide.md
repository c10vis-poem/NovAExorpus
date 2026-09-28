# Llama-server & OpenAI endpoint Deployment Guide - Unsloth Documentation

1
Basics
🖥️Inference & Deployment
llama-server & OpenAI
endpoint Deployment Guide
Deploying via llama-server with an OpenAI compatible
endpoint
We are going to deploy Devstral-2 - see Devstral 2 for more details
on the model. 
Obtain the latest llama.cpp on GitHub here . You can follow the
build instructions below as well. Change -DGGML_CUDA=ON to -
DGGML_CUDA=OFF if you don't have a GPU or just want CPU
inference. For Apple Mac / Metal devices, set -DGGML_CUDA=OFF
then continue as usual - Metal support is on by default.
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
-DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target
llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
Copy
Reddit
Discord
🇺🇸 English
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.
Accept
Reject


2
When using --jinja llama-server appends the following system
message if tools are supported: Respond in JSON format, either with
tool_call (a request to call tools) or with response reply to the user's request .
This sometimes causes issues with fine-tunes! See the llama.cpp
repo
 for more details.
First download Devstral 2:
To deploy Devstral 2 for production, we use llama-server In a new
terminal say via tmux, deploy the model via:
When you run the above, you will get:
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
repo_id = "unsloth/Devstral-2-123B-Instruct-2512-GGUF",
local_dir = "Devstral-2-123B-Instruct-2512-GGUF",
allow_patterns = ["*UD-Q2_K_XL*", "*mmproj-F16*"],
)
./llama.cpp/llama-server \
--model Devstral-Small-2-24B-Instruct-2512-GGUF/Devstral-Small-2-
24B-Instruct-2512-UD-Q4_K_XL.gguf \
--mmproj Devstral-Small-2-24B-Instruct-2512-GGUF/mmproj-F16.gguf
\
--alias "unsloth/Devstral-Small-2-24B-Instruct-2512" \
--threads -1 \
--n-gpu-layers 999 \
--prio 3 \
--min-p 0.01 \
--ctx-size 16384 \
--port 8001 \
--jinja
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


3
Then in a new terminal, after doing pip install openai , do:
Which will simply print 4.
You can go back to the llama-server screen and you might see
some statistics which might be interesting:
from openai import OpenAI
import json
openai_client = OpenAI(
base_url = "http://127.0.0.1:8001/v1",
api_key = "sk-no-key-required",
)
completion = openai_client.chat.completions.create(
model = "unsloth/Devstral-Small-2-24B-Instruct-2512",
messages = [{"role": "user", "content": "What is 2+2?"},],
)
print(completion.choices[0].message.content)
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


4
For arguments like using speculative decoding, see 
https://github.com/ggml-
org/llama.cpp/blob/master/tools/server/README.md
• When using --jinja llama-server appends the following system
message if tools are supported: Respond in JSON format, either
with tool_call (a request to call tools) or with response reply to the user's
request . This sometimes causes issues with fine-tunes! See the
llama.cpp repo for more details.
You can stop this by using --no-jinja but then tools becomes
unsupported.
For example FunctionGemma by default uses:
But because of llama-server appending an extra message, we
get:
We reported the issue to https://github.com/ggml-
org/llama.cpp/issues/18323 and llama.cpp developers are
working on a fix!
In the meantime, for all fine-tunes, please add the prompt
specifically for tool calling!
❔Llama-server quirks
You are a model that can do function calling with the following
functions
You are a model that can do function calling with the following
functions\n\nRespond in JSON format, either with `tool_call` (a
request to call tools) or with `response` reply to the user's request
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


5
Community
Reddit r/unsloth
Twitter (X)
LinkedIn
Resources
Tutorials
Docker
Hugging Face
Company
Unsloth Studio
Contact
Events
See Tool Calling Guide on how to do tool calling!
Previous
SGLang
Next
Run LLMs on your Phone
Last updated 2 months ago
Was this helpful?
🧰Tool Calling with llama-server
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


6
© Unsloth, 2026
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.
