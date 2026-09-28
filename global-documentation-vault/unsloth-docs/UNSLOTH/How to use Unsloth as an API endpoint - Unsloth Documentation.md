# How to use Unsloth as an API endpoint - Unsloth Documentation

1
Basics
How to use Unsloth as an
API endpoint
You can run local LLMs with tools like Claude Code and Codex by
connecting those tools to Unsloth’s OpenAI-compatible API
endpoint. This lets you run models like Qwen and Gemma locally
for agentic coding. Unsloth also has beneficial features such as
self-healing tool calling, code execution, and web search.
Unsloth makes it easy to deploy a fast API inference endpoint that
provides:
• Self-healing tool calling, which helps reduce broken or
malformed tool calls by 50%
• Code execution support, allowing Bash and Python execution
for more accurate code outputs.
• Advanced Web search that visits and actually reads webpages
to gather in-depth info.
• Automatic inference settings for GGUF models (temp, top-k
etc.)
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
Models loaded in Unsloth
(including GGUFs) are exposed
as an authenticated API via 
llama-server . A long API key is
generated for security reasons
like how OpenAI provides one.
Your local models can then be
used directly in your preferred
AI agent, SDK, or chat client.
Unsloth speaks two dialects on
the same port. Both support
streaming, tool calling (OpenAI 
tools / Anthropic tools ), and
vision inputs:
• Anthropic-compatible /v1/messages  for Claude Code,
OpenClaw, the Anthropic SDK, and any client that expects the
Messages API.
• OpenAI-compatible /v1/chat/completions and /v1/responses for
the OpenAI SDK, OpenCode, Cursor, Continue, Cline, Open
WebUI, SillyTavern, and any OpenAI-compatible tool.
1. Install or update Unsloth Studio. Then launch Unsloth.
2. Load a model. Click New Chat, pick or search a model (GGUF),
and wait for it to finish loading.
3. Create an API key. Click your Unsloth avatar in the bottom-left
→ Settings → API → type a key name → Create. Copy the sk-
unsloth-… value that appears. Unsloth only shows it once.
⚡ Quickstart
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


3
4. Point your client at Unsloth. Use http://localhost:PORT as the
base URL and your sk-unsloth-… key for auth. Jump to the recipe
for your tool below.
1. Open the sidebar, click your Unsloth avatar at the bottom-left.
2. Go to Settings → API (globe 🌐 icon).
3. Enter a friendly name (e.g. claude-code-macbook ). Set an expiry
(optional)
4. Click Create.
5. Copy the key. Unsloth stores only a hash and you won't be able
to view it again.
All keys start with the sk-unsloth- prefix. Revoke a key from the
same page at any time. Requests made with a revoked key will fail
with 401 Unauthorized .
Treat your API key like a password. Anyone with the key and network
access to your Unsloth instance can send requests to your loaded
model.
🔑 Creating an API key
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


4
Before using the API, load a model from the Select model
dropdown in the top-left corner of the Chat page.
In this guide, we’ll use:
unsloth/gemma-4-26B-A4B-it-GGUF with the recommended 
UD-Q4_K_XL quantization.
⏳ Model Loading
1
Select Model
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


5
Before using the Client, send a quick message:
This confirms that the model loaded correctly and is ready to
respond.
In Unsloth, open Settings → API to view or create your API
key.
Treat your API key like a password and avoid exposing it in
screenshots or repositories.
2
Test the Model
3
Unsloth API key
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


6
1. Install or update Unsloth Studio. Earlier versions don't expose
the external API. See Installation.
2. Load a GGUF model. load a GGUF model using the run
command. This will also load the UI on the default port. The
endpoint URL and API Key will be printed out to the console ,
ready for you to be used with your client of choice.
You can load a model and have an API key created for you
automatically using the unsloth CLI tool. When the model finishes
loading, the endpoint URL and API key are printed to your console.
Copy them into your client of choice and you're ready to go.
Make sure you're on a recent version of Unsloth Studio as earlier
versions don't expose the external API. See installation.
Open a terminal and load a GGUF model:
This starts the server on the default port, loads the UI, and prints
your endpoint URL and API key.
 Unsloth run command
unsloth run --model unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL
Loading a model from the CLI
Before you start
The quick way
unsloth run --model unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


7
You can point at a model in a few different ways. Pick the one you
find easiest:
You don't need any of this for a basic load, but unsloth run supports
many llama-server runtime flags for customizing performance,
memory usage, context length, generation behavior, networking,
and tool access.
Additional flags are forwarded directly to the underlying inference
server, and your values override Unsloth's defaults.
Sampling settings control how creative, focused, or deterministic
the model behaves during generation.
How the model name works
# Combined: repo and quantization variant in one string (recommended
— shortest)
unsloth run --model unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL
# Separate: repo and variant as two flags (the older style, still works)
unsloth run --model unsloth/gemma-4-26B-A4B-it-GGUF --gguf-variant
UD-Q4_K_XL
# Using -hf / --hf-repo (matches llama.cpp's spelling, handy if you're
coming from there)
unsloth run -hf unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL
Tuning the run (optional)
Adjust generation behavior
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


8
Lower temperature values usually produce more stable outputs,
while top-p, top-k, min-p, and repeat penalty settings further control
token selection and repetition.
Useful if you're working with large projects, long chats, or agent
workflows that need more memory.
By default, Unsloth only runs locally on your machine. You can
expose the API to other devices on your network by binding to 
0.0.0.0 .
# Lower randomness and improve reproducibility
unsloth run \
--model unsloth/Qwen3-1.7B-GGUF \
--temp 0.6 \
--seed 42
# Tune token selection and repetition behavior
unsloth run \
--model unsloth/Qwen3-1.7B-GGUF \
--top-p 0.95 \
--top-k 20 \
--min-p 0.05 \
--repeat-penalty 1.1
Increase context length and CPU threads
# Use a larger context window and more CPU threads
unsloth run \
--model unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL \
-c 131072 \
--threads 32
Expose the API on your local network
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


9
Some reasoning-capable models support additional flags for
controlling thinking and reasoning behavior.
Reasoning support depends on the model and backend
capabilities.
Control whether tools like web search and code execution are
exposed by the inference server.
# Allow LAN devices to connect
unsloth run \
--model unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL \
-H 0.0.0.0 \
-p 8888
Control reasoning behavior
# Disable reasoning / thinking output
unsloth run \
--model unsloth/Qwen3-1.7B-GGUF \
--reasoning off
# Enable reasoning mode
unsloth run \
--model unsloth/Qwen3-1.7B-GGUF \
--reasoning on
Enable or disable server-side tools
# Explicitly enable tools
unsloth run \
--model unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL \
--enable-tools
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


10
Unsloth supports most llama-server runtime flags, including
context sizing, GPU layers, threading, sampling, networking, and
tool configuration.
See the llama-server documentation for the full list of supported
runtime flags.
unsloth run controls whether server-side tools (web search, code
execution, etc.) are exposed by the inference server. Defaults are
based on the bind address:
•
127.0.0.1 (localhost) — tools on by default. Only your machine
can reach the server.
•
0.0.0.0 or any non-loopback address — tools off by default. A
leaked API key on a network-exposed server means arbitrary
code execution on the host.
Flags:
•
--enable-tools / --disable-tools — force on or off. On 0.0.0.0 , --
enable-tools shows a y/N security prompt.
•
--yes / -y — skip the prompt (for automation).
The resolved policy is a process-level hard override — individual
requests cannot bypass it via enable_tools=true in the request body.
# Explicitly disable tools
unsloth run \
--model unsloth/gemma-4-26B-A4B-it-GGUF:UD-Q4_K_XL \
--disable-tools
Server-side tool policy
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


11
Unsloth exposes these endpoints on whichever port it booted on
(typically http://localhost:8000 or http://localhost:8888 ):
Authenticate with an Authorization: Bearer sk-unsloth-… header on
every request.
🌐 Endpoints
Endpoint
Compatible with
Use it from
POST /v1/messages
Anthropic Messages
API
Claude Code,
Anthropic SDK,
OpenClaw, anything
that speaks Anthropic
POST
/v1/chat/completions
OpenAI Chat
Completions API
OpenAI SDK,
opencode, Cursor,
Continue, Cline, Open
WebUI, curl, etc.
GET /v1/models
OpenAI models list
List the models
currently loaded in
Unsloth
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


12
You don't need to run different servers for the two formats. Unsloth
handles both on the same port.
Unsloth enables you run local LLMs via most frameworks including 
Claude Code, Codex, OpenClaw, OpenCode and more. Click the
specific tools below for a guide:
Claude Code
OpenAI Codex
Curl & HTTP
OpenClaw
OpenCode
Python SDK
Both endpoints support function / tool calling in their native format,
plus an Unsloth-specific shorthand for Unsloth's built-in tools.
OpenAI-style tools: send tools and tool_choice to 
/v1/chat/completions exactly as you would with OpenAI. Claude
Code (via /v1/messages ), opencode, Cursor, Continue, and Cline all
work out of the box.
Anthropic-style tools: send tools (with input_schema ) and 
tool_choice to /v1/messages exactly as you would with Claude.
🖇️ Connecting your client
🧰 Tool calling
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


13
Unsloth server side tools: Unsloth can execute Python, web search,
and bash server-side and stream the results back as tool_result
events. Opt in by adding these extra fields to either endpoint:
The model sees each tool's output on its next turn. For deeper
coverage (schemas, streaming events, chaining), see .
If you're using the Anthropic /v1/messages endpoint, tool_choice
maps cleanly: Anthropic auto → OpenAI auto , Anthropic any →
OpenAI required , Anthropic {type: "tool", name: "x"} → OpenAI {type:
"function", function: {name: "x"}} , Anthropic none → OpenAI none .
401 Unauthorized :  either the Authorization header is missing or the
key is wrong. Keys must be passed as Authorization: Bearer sk-
unsloth-… . If you lost the key, create a new one from Settings →
API. Unsloth doesn't show old keys after creation.
Lost connection to the model server : Unsloth couldn't reach the
underlying llama.cpp server. Usually the model finished loading but
crashed, or the model tab was closed inside Unsloth. Reload the
model from New Chat and retry.
{
"messages": [{"role": "user", "content": "What is 123 * 456? Use
Python."}],
"stream": true,
"enable_tools": true,
"enabled_tools": ["python", "web_search","terminal"],
"session_id": "my-session"
}
❔ Troubleshooting
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


14
Claude Code shows the default Anthropic model, not my local one
:  check all three env vars are exported in the same shell where you
run claude :
Then run /model inside Claude Code to confirm. On Windows
PowerShell use $env:ANTHROPIC_BASE_URL etc.
stream: true returns a single JSON blob instead of SSE :  make
sure you're hitting the right path ( /v1/messages or 
/v1/chat/completions ) and that your HTTP client is actually
consuming the response as a stream, not buffering it.
I can't find the name of the model to add to opencode (or
OpenClaw / any other client) : ask Unsloth directly. GET /v1/models
returns the exact model ID you need to plug into the client's "Model
ID" field:
You'll get back a JSON payload of the form {"data": [{"id": "gemma-4-
26B-A4B-it-GGUF", ...}]} . Copy the id value, that's the string
opencode's Model ID field (left column) and OpenClaw's models[].id
expect. The display name on the right is whatever you want users
to see.
echo $ANTHROPIC_BASE_URL
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_MODEL
curl http://localhost:8888/v1/models \
-H "Authorization: Bearer sk-unsloth-xxxxxxxxxxxx"
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


15
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
Tool calls aren't executed :  The model needs to support tool calling
for client-side tools ( tools / tool_choice ). For Unsloth's built-in
tools, remember to set enable_tools: true and list the ones you want
in enabled_tools (e.g. ["python", "web_search"] ).
Previous
Qwen3.5 GGUF
Benchmarks
Next
Inference & Deployment
Last updated 6 days ago
Was this helpful?
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.


16
Events
© Unsloth, 2026
This site uses cookies to deliver its
service and to analyze traffic. By browsing
this site, you accept the privacy policy.
