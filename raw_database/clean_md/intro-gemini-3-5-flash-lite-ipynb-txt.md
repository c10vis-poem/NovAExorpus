---
source: raw/intro_gemini_3_5_flash_lite.ipynb.txt
cleaned: 2026-09-09
converter: custom Python script parsing the .ipynb JSON cell structure (stdlib json), rendering markdown cells as-is and code cells as fenced ```python blocks; no cell outputs existed in the source to preserve
---

```python
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
```

# Intro to Gemini 3.5 Flash-Lite

<table align="left">
  <td style="text-align: center">
    <a href="https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash_lite.ipynb">
      <img width="32px" src="https://www.gstatic.com/pantheon/images/bigquery/welcome_page/colab-logo.svg" alt="Google Colaboratory logo"><br> Open in Colab
    </a>
  </td>
  <td style="text-align: center">
    <a href="https://console.cloud.google.com/agent-platform/colab/import/https:%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fgetting-started%2Fintro_gemini_3_5_flash_lite.ipynb">
      <img width="32px" src="https://lh3.googleusercontent.com/JmcxdQi-qOpctIvWKgPtrzZdJJK-J3sWE1RsfjZNwshCFgE_9fULcNpuXYTilIR2hjwN" alt="Google Cloud Colab Enterprise logo"><br> Open in Colab Enterprise
    </a>
  </td>
  <td style="text-align: center">
    <a href="https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https://raw.githubusercontent.com/GoogleCloudPlatform/generative-ai/main/gemini/getting-started/intro_gemini_3_1_flash_lite.ipynb">
      <img width="32px" src="https://storage.googleapis.com/github-repo/workbench-icon.svg" alt="Workbench logo"><br> Open in Workbench
    </a>
  </td>
  <td style="text-align: center">
    <a href="https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash_lite.ipynb">
      <img width="32px" src="https://raw.githubusercontent.com/primer/octicons/refs/heads/main/icons/mark-github-24.svg" alt="GitHub logo"><br> View on GitHub
    </a>
  </td>
</table>

<div style="clear: both;"></div>

<p>
<b>Share to:</b>

<a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash_lite.ipynb" target="_blank">
  <img width="20px" src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" alt="LinkedIn logo">
</a>

<a href="https://bsky.app/intent/compose?text=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash_lite.ipynb" target="_blank">
  <img width="20px" src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Bluesky_Logo.svg" alt="Bluesky logo">
</a>

<a href="https://twitter.com/intent/tweet?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash_lite.ipynb" target="_blank">
  <img width="20px" src="https://upload.wikimedia.org/wikipedia/commons/5/5a/X_icon_2.svg" alt="X logo">
</a>

<a href="https://reddit.com/submit?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash_lite.ipynb" target="_blank">
  <img width="20px" src="https://redditinc.com/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png" alt="Reddit logo">
</a>

<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash_lite.ipynb" target="_blank">
  <img width="20px" src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook logo">
</a>
</p>

| Authors |
| --- |
| [Eric Dong](https://github.com/gericdong) |
| [Holt Skinner](https://github.com/holtskinner) |

## Overview

This notebook serves as a quickstart guide for developers to begin interacting with the **[Gemini 3.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite)** model via the Google Gen AI SDK on Google Cloud. It is designed to demonstrate key model capabilities and showcase new API features.

Gemini 3.5 Flash-Lite is our fastest and most cost-efficient model yet, optimized for production pressure and built for scaling high-volume agentic tasks.

* **Cost efficiency without compromise:** Scaled for routine agentic tasks—including tool-based search, data extraction, analysis, summarization, and rapid iterations—via the API.
* **Lowest latency:** The lowest-latency model in the 3.5 family, built to complete tasks quickly.
* **High scalability:** Sustains high-quality performance across workloads of varying volume and reasoning complexity.

#### Key Use Cases

* **Basic agentic tasks:** Entry point into a multi-model architecture. Acts as a gatekeeper and drives rapid execution of basic agentic loops.
* **Scaled production pipelines:** Low cost/token enables high-throughput production workflows, like document extraction and large-scale classification.
* **Everyday content & routine tasks:** Research tasks, high-volume data tasks like extraction, tool-based search, and summarization where cost efficiency is paramount.

## Getting Started

### Install Google Gen AI SDK for Python

```python
%pip install --upgrade --quiet google-genai
```

⚠️ **Note**: Ignore pip dependency errors.

### Import libraries


```python
import os
import sys

from IPython.display import HTML, Image, Markdown, display
from google import genai
from google.genai import types
from pydantic import BaseModel
```

### Authenticate your notebook environment

If you are running this notebook on Google Colab, run the cell below to authenticate your environment.

```python
if "google.colab" in sys.modules:
    from google.colab import auth

    auth.authenticate_user()
```

### Autenticate your Google Cloud Project

You can use a Google Cloud Project or an API Key for authentication. This tutorial uses a Google Cloud Project.

- [Enable the Agent Platform API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)

```python
# fmt: off
PROJECT_ID = "[your-project-id]"  # @param {type: "string", placeholder: "[your-project-id]", isTemplate: true}
# fmt: on
if not PROJECT_ID or PROJECT_ID == "[your-project-id]":
    PROJECT_ID = str(os.environ.get("GOOGLE_CLOUD_PROJECT"))

LOCATION = "global"

client = genai.Client(enterprise=True, project=PROJECT_ID, location=LOCATION)
```

### Choose a Gemini 3.5 model

Use `gemini-3.5-flash-lite` in this tutorial. Learn more about all [Gemini models on Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models).

```python
# fmt: off
MODEL_ID = "gemini-3.5-flash-lite"  # @param ["gemini-3.5-flash-lite"] {type: "string"}
# fmt: on
```

## 🚀 Quickstart

By default, Gemini 3 uses dynamic thinking to reason through prompts. For faster, lower-latency responses when complex reasoning isn't required, you can constrain the model's thinking level by setting parameter `thinking_level` to `minimal`.

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            # For faster and lower-latency responses
            thinking_level=types.ThinkingLevel.MINIMAL
        )
    ),
)

display(Markdown(response.text))
```

## 🚨 New API Features

### 1️⃣ Thinking Level

The `thinking_level` parameter allows you to specify a thinking budget for the model's response generation. By selecting one of two states, you can explicitly balance the trade-offs between response quality/reasoning complexity and latency/cost.

- **`MINIMAL`:** Constrains the model to use as few tokens as possible for thinking and is best used for low-complexity tasks that wouldn't benefit from extensive reasoning. `MINIMAL` is as close as possible to a zero budget for thinking but still requires thought signatures.
- **`LOW`:** Constrains the model to use fewer tokens for thinking and is suitable for simpler tasks where extensive reasoning is not required.
- **`MEDIUM`:** Offers a balanced approach suitable for tasks of moderate complexity that benefit from reasoning but don't require deep, multi-step planning. It provides more reasoning capability than `LOW` while maintaining lower latency than `HIGH`.
- **`HIGH`:** Maximizes reasoning depth. The model may take significantly longer to reach a first token, but the output will be more thoroughly vetted.

#### ⚠️ Notes

- If `thinking_level` is not specified, the model defaults to `HIGH`, which is a dynamic setting that adjusts based on prompt complexity.
- You cannot use both `thinking_level` and the legacy `thinking_budget` parameter in the same request. Doing so will return a 400 error.

```python
prompt = """
You are tasked with implementing the classic Thread-Safe Double-Checked Locking (DCL) Singleton pattern in modern C++. This task is non-trivial and requires specialized concurrency knowledge to prevent memory reordering issues.

Write a complete, runnable C++ program named `dcl_singleton.cpp` that defines a class `Singleton` with a private constructor and a static `getInstance()` method.

Your solution MUST adhere to the following strict constraints:
1. The Singleton instance pointer (`static Singleton*`) must be wrapped in `std::atomic` to correctly manage memory visibility across threads.
2. The `getInstance()` method must use `std::memory_order_acquire` when reading the instance pointer in the outer check.
3. The instance creation and write-back must use `std::memory_order_release` when writing to the atomic pointer.
4. A standard `std::mutex` must be used only to protect the critical section (the actual instantiation).
5. The `main` function must demonstrate safe, concurrent access by launching at least three threads, each calling `Singleton::getInstance()`, and printing the address of the returned instance to prove all threads received the same object.
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.HIGH  # Dynamic thinking for high reasoning tasks
        )
    ),
)

display(Markdown(response.text))
```

### 2️⃣ Media Resolution

Gemini 3 introduces granular control over multimodal vision processing via the `media_resolution` parameter. Higher resolutions improve the model's ability to read fine text or identify small details, but increase token usage and latency. The `media_resolution` parameter determines the  maximum number of tokens allocated per input image or video frame.

**⚠️ Note**: Because media resolution directly impacts token count, you may need to lower the resolution (e.g., to `low`) to fit very long inputs, such as long videos or extensive documents.

You can set the resolution to `LOW`, `MEDIUM`, `HIGH`, or `ULTRA_HIGH` per individual media part, as example:

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part(
            file_data=types.FileData(
                file_uri="gs://cloud-samples-data/generative-ai/image/a-man-and-a-dog.png",
                mime_type="image/jpeg",
            ),
            media_resolution=types.PartMediaResolution(
                level=types.PartMediaResolutionLevel.MEDIA_RESOLUTION_ULTRA_HIGH
            ),
        ),
        types.Part(
            file_data=types.FileData(
                file_uri="gs://cloud-samples-data/generative-ai/video/behind_the_scenes_pixel.mp4",
                mime_type="video/mp4",
            ),
            media_resolution=types.PartMediaResolution(
                level=types.PartMediaResolutionLevel.MEDIA_RESOLUTION_LOW
            ),
        ),
        "When does the image appear in the video? What is the context?",
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.LOW)
    ),
)

display(Markdown(response.text))
```

Or set it globally via `GenerateContentConfig`. If unspecified, the model uses optimal defaults based on the media type.

**⚠️ NOTE:** `ULTRA_HIGH` is only supported for individual parts.

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part(
            file_data=types.FileData(
                file_uri="gs://cloud-samples-data/generative-ai/image/a-man-and-a-dog.png",
                mime_type="image/jpeg",
            ),
        ),
        "What is in the image?",
    ],
    config=types.GenerateContentConfig(
        media_resolution=types.MediaResolution.MEDIA_RESOLUTION_LOW
    ),
)

display(Markdown(response.text))
```

### 3️⃣ Thought Signature

[Thought signatures](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking#signatures) are encrypted tokens that preserve the model's reasoning state during multi-turn conversations, specifically when using Function Calling.

When a thinking model decides to call an external tool, it pauses its internal reasoning process. The thought signature acts as a "save state", allowing the model to resume its chain of thought seamlessly once you provide the function's result.

Gemini 3 enforces stricter validation and updated handling on thought signatures which were originally introduced in Gemini 2.5. To ensure the model maintains context across multiple turns of a conversation, you must return the thought signatures in your subsequent requests.


#### Automatic Handling of Thought Signatures (Recommended)

If you are using the Google Gen AI SDKs (Python, Node.js, Go, Java) or OpenAI Chat Completions API, and utilizing the standard chat history features or appending the full model response, thought signatures are handled automatically. You do not need to make any changes to your code.


#### **Example 1**: Automatic Function Calling

When using the Gen AI SDK in automatic function calling, thought signatures are handled automatically.


```python
def get_weather(city: str):
    """Gets the weather in a city."""
    if "london" in city.lower():
        return "Rainy"
    if "new york" in city.lower():
        return "Sunny"
    return "Cloudy"


response = client.models.generate_content(
    model=MODEL_ID,
    contents="What's the weather in London and New York?",
    config=types.GenerateContentConfig(
        tools=[get_weather],
    ),
)

# The SDK handles the function calls and thought signatures, and returns the final text
display(Markdown("## Final Response"))
display(Markdown(response.text))

# Print function calling history
hist_turn = response.automatic_function_calling_history[1]
print("\nFunction Call 1:", hist_turn.parts[1].function_call.name)
```

#### **Example 2**: Manual Function Calling

When using the Gen AI SDK in manual function calling, thought signatures are also handled automatically if you append the full model response in sequential model requests.

```python
# 1. Define your tool
get_weather_declaration = types.FunctionDeclaration(
    name="get_weather",
    description="Gets the current weather temperature for a given location.",
    parameters={
        "type": "object",
        "properties": {"location": {"type": "string"}},
        "required": ["location"],
    },
)
get_weather_tool = types.Tool(function_declarations=[get_weather_declaration])

# 2. Send a message that triggers the tool
prompt = "What's the weather like in London?"
response = client.models.generate_content(
    model=MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        tools=[get_weather_tool],
        thinking_config=types.ThinkingConfig(include_thoughts=True),
    ),
)

# 3. Handle the function call
function_call = response.function_calls[0]
location = function_call.args["location"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {location}")
function_response_data = {
    "location": location,
    "temperature": "30C",
}

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
# The `content` object automatically attaches the required thought_signature behind the scenes.
history = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    response.candidates[0].content,  # Signature preserved here
    types.Content(
        role="user",
        parts=[
            types.Part.from_function_response(
                name=function_call.name,
                response=function_response_data,
            )
        ],
    ),
]

response_2 = client.models.generate_content(
    model=MODEL_ID,
    contents=history,
    config=types.GenerateContentConfig(
        tools=[get_weather_tool],
        thinking_config=types.ThinkingConfig(include_thoughts=True),
    ),
)

# 5. Get the final, natural-language answer
print(f"\nFinal model response: {response_2.text}")
```

#### Manual Handling of Thought Signatures

If you are interacting with the API directly or managing raw JSON payloads, you must correctly handle the `thought_signature` included in the model's turn.
You must return this signature in the exact part where it was received when sending the conversation history back.

⚠️ If proper signatures are not returned, the model will return a 400 Error `"Function Call in the content block is missing a thought_signature"`.

See [documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#thinking) for more details.

### 5️⃣ Multimodal Function Responses

Multimodal function calling allows users to have function responses containing multimodal objects allowing for improved utilization of function calling capabilities of the model. Currently function calling only supports text based function responses.


```python
# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
    name="get_image",
    description="Retrieves the image file reference for a specific order item.",
    parameters={
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'green shirt').",
            }
        },
        "required": ["item_name"],
    },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the green shirt I ordered last month."
response_1 = client.models.generate_content(
    model=MODEL_ID,
    contents=[prompt],
    config=types.GenerateContentConfig(
        tools=[tool_config],
    ),
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
    "image_ref": {"$ref": "dress.jpg"},
}

function_response_multimodal_data = types.FunctionResponsePart(
    file_data=types.FunctionResponseFileData(
        mime_type="image/png",
        display_name="dress.jpg",
        file_uri="gs://cloud-samples-data/generative-ai/image/dress.jpg",
    )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    response_1.candidates[0].content,
    types.Content(
        role="user",
        parts=[
            types.Part.from_function_response(
                name=function_call.name,
                response=function_response_data,
                parts=[function_response_multimodal_data],
            )
        ],
    ),
]

response_2 = client.models.generate_content(
    model=MODEL_ID,
    contents=history,
    config=types.GenerateContentConfig(
        tools=[tool_config], thinking_config=types.ThinkingConfig(include_thoughts=True)
    ),
)

print(f"\nFinal model response: {response_2.text}")
```

### 6️⃣ Inline Citations

Inline citations use the structured `grounding_metadata` returned by the API to link specific segments of generated text to verifiable sources.

This capability supports all grounding methods including Google Search, Google Maps, Agent Search, and Elasticsearch, providing the precise source details required to display accurate, interactive citations within your application.


```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents="Where will the next FIFA World Cup be held?",
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())],
    ),
)

display(Markdown(response.text))
print(response.candidates[0].grounding_metadata.grounding_chunks)
display(
    HTML(response.candidates[0].grounding_metadata.search_entry_point.rendered_content)
)
```

## ⭐️ Supported Features

### ✅ Set System Instructions

```python
system_instruction = """
  You are a helpful language translator.
  Your mission is to translate text in English to Spanish.
"""

prompt = """
  User input: I like bagels.
  Answer:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
    ),
)

display(Markdown(response.text))
```

### ✅ Configure Model Parameters

⚠️ **Notes**: For Gemini 3, we strongly recommend keeping the `temperature` parameter at its default value of `1.0`.

While previous models often benefitted from tuning `temperature` to control creativity versus determinism, Gemini 3's reasoning capabilities are optimized for the default setting.


```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents="Tell me how the internet works, but pretend I'm a puppy who only understands squeaky toys.",
    config=types.GenerateContentConfig(
        temperature=1.0,
        max_output_tokens=500,
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.MINIMAL,
        ),
    ),
)

display(Markdown(response.text))
```

### ✅ Generate Content Stream

```python
prompt = """
A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball.
How much does the ball cost?
"""

for chunk in client.models.generate_content_stream(
    model=MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.LOW,
        )
    ),
):
    print(chunk.text, end="")
```

### ✅ Thought Summaries

You can include thought summaries in model response by setting `include_thoughts` to `true`.


```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents="How many R's are in the word strawberry?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_level=types.ThinkingLevel.LOW,
        )
    ),
)

for part in response.candidates[0].content.parts:
    if part.thought:
        display(
            Markdown(
                f"""## Thoughts:
         {part.text}
        """
            )
        )
    else:
        display(
            Markdown(
                f"""## Answer:
         {part.text}
        """
            )
        )
```

### ✅  Multi-turn Chat

Conversation: Starting and maintaining a Multi-turn Chat history.

```python
chat = client.chats.create(
    model=MODEL_ID,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.MINIMAL)
    ),
)
```

```python
response = chat.send_message(
    "Write a Python function that checks if a year is a leap year."
)

display(Markdown(response.text))
```

This follow-up prompt shows how the model responds based on the previous prompt:

```python
response = chat.send_message("Write a unit test of the generated function.")

display(Markdown(response.text))
```

### ✅ Safety Filters

```python
system_instruction = "Be as mean and hateful as possible."

prompt = """
Write a list of 5 disrespectful things that I might say to the universe after stubbing my toe in the dark.
"""

safety_settings = [
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_JAILBREAK,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
]

response = client.models.generate_content(
    model=MODEL_ID,
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        safety_settings=safety_settings,
    ),
)

# Response will be `None` if it is blocked.
print(response.text)
# Finish Reason will be `SAFETY` if it is blocked.
print(response.candidates[0].finish_reason)
# Safety Ratings show the levels for each filter.
for safety_rating in response.candidates[0].safety_ratings:
    if safety_rating.blocked:
        print(safety_rating)
```

### ✅ Send Asynchronous Requests


```python
response = await client.aio.models.generate_content(
    model=MODEL_ID,
    contents="Compose a song about the adventures of a time-traveling squirrel.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.MINIMAL  # Dynamic thinking for high reasoning tasks
        )
    ),
)

display(Markdown(response.text))
```

### ✅ Multimodality

- If your content is stored in [Google Cloud Storage](https://cloud.google.com/storage) or on a public website, you can use the `from_uri`  method to create a `Part` object.
- If your content is stored in your local file system, you can read it in as bytes data and use the `from_bytes` method to create a `Part` object.


#### 💡 **Image**

In this example, we will use an image stored locally.


```python
# Download and open an image locally.
! wget https://storage.googleapis.com/cloud-samples-data/generative-ai/image/meal.png

with open("meal.png", "rb") as f:
    image = f.read()
    display(Image(image, width=500))

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image, mime_type="image/png"),
        "Write a short and engaging blog post based on this picture.",
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.MINIMAL
        ),
        media_resolution=types.MediaResolution.MEDIA_RESOLUTION_LOW,
    ),
)

display(Markdown(response.text))
```

#### 💡 **PDF**

In this example, we will use a PDF Document stored on Google Cloud Storage.

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_uri(
            file_uri="gs://cloud-samples-data/generative-ai/pdf/1706.03762v7.pdf",
            mime_type="application/pdf",
        ),
        "Summarize the document.",
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.LOW,
        ),
        media_resolution=types.MediaResolution.MEDIA_RESOLUTION_LOW,
    ),
)

display(Markdown(response.text))
```

#### 💡 **Audio**

This example uses an audio file stored at a general web URL.


```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_uri(
            file_uri="https://storage.googleapis.com/cloud-samples-data/generative-ai/audio/pixel.mp3",
            mime_type="audio/mpeg",
        ),
        "Write a summary of this podcast episode.",
    ],
    config=types.GenerateContentConfig(
        audio_timestamp=True,
        thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.LOW),
    ),
)

display(Markdown(response.text))
```

#### 💡 **YouTube Video**

This example is the YouTube video [Google — 25 Years in Search: The Most Searched](https://www.youtube.com/watch?v=3KtWfp0UopM).


```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_uri(
            file_uri="https://www.youtube.com/watch?v=3KtWfp0UopM",
            mime_type="video/mp4",
        ),
        "At what point in the video is Harry Potter shown?",
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.LOW)
    ),
)

display(Markdown(response.text))
```

#### 💡 **Web Page (HTTP Support)**

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_uri(
            file_uri="https://docs.cloud.google.com/gemini-enterprise-agent-platform",
            mime_type="text/html",
        ),
        "Write a summary of this documentation.",
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.LOW)
    ),
)

display(Markdown(response.text))
```

### ✅ Structured Output

#### 💡 [Pydantic](https://docs.pydantic.dev/latest/) Model Schema support

```python
class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    gdp: int
    official_language: str
    total_area_sq_mi: int


response = client.models.generate_content(
    model=MODEL_ID,
    contents="Give me information for the United States.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=CountryInfo,
    ),
)
# Response as JSON
print(response.text)
# Response as Pydantic object
print(response.parsed)
```

```python
class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    gdp: int
    official_language: str
    total_area_sq_mi: int


response = client.models.generate_content(
    model=MODEL_ID,
    contents="Give me information for the United States.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=CountryInfo,
    ),
)
# Response as JSON
print(response.text)
# Response as Pydantic object
print(response.parsed)
```

#### 💡 [OpenAPI Schema](https://swagger.io/specification/) support

```python
response_schema = {
    "required": [
        "name",
        "population",
        "capital",
        "continent",
        "gdp",
        "official_language",
        "total_area_sq_mi",
    ],
    "properties": {
        "name": {"type": "STRING"},
        "population": {"type": "INTEGER"},
        "capital": {"type": "STRING"},
        "continent": {"type": "STRING"},
        "gdp": {"type": "INTEGER"},
        "official_language": {"type": "STRING"},
        "total_area_sq_mi": {"type": "INTEGER"},
    },
    "type": "OBJECT",
}

response = client.models.generate_content(
    model=MODEL_ID,
    contents="Give me information for the United States.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=response_schema,
    ),
)
# As JSON
print(response.text)
# As Dict
print(response.parsed)
```

### ✅ Search as a Tool


```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents="Where will the next FIFA World Cup be held?",
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())],
    ),
)

display(Markdown(response.text))
print(response.candidates[0].grounding_metadata.grounding_chunks)
display(
    HTML(response.candidates[0].grounding_metadata.search_entry_point.rendered_content)
)
```

### ✅ Code Execution

```python
# Define code execution tool
code_execution_tool = types.Tool(code_execution=types.ToolCodeExecution())

response = client.models.generate_content(
    model=MODEL_ID,
    contents="Calculate 20th fibonacci number. Then find the nearest palindrome to it.",
    config=types.GenerateContentConfig(
        tools=[code_execution_tool],
    ),
)

display(
    Markdown(
        f"""
## Code

```py
{response.executable_code}
```

### Output

```
{response.code_execution_result}
```
"""
    )
)
```

### ✅ URL Context

```python
# Define the Url context tool
url_context_tool = types.Tool(url_context=types.UrlContext)

url = "https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/"

response = client.models.generate_content(
    model=MODEL_ID,
    contents=f"Summarize this document: {url}",
    config=types.GenerateContentConfig(
        tools=[url_context_tool],
        thinking_config=types.ThinkingConfig(thinking_level=types.ThinkingLevel.LOW),
    ),
)

display(Markdown(response.text))
print(response.candidates[0].grounding_metadata)
```

### ✅ Function Calling


```python
def get_weather(location: str):
    """Get the current weather in a specific location.

    Args:
        location: The city and state, e.g. San Francisco, CA or a zip code.
    """
    # This is a placeholder for a real API call.
    return {"temperature": "32", "unit": "celsius"}


response = client.models.generate_content(
    model=MODEL_ID,
    contents="What is the weather like in Toronto?",
    config=types.GenerateContentConfig(
        tools=[get_weather],
    ),
)

display(Markdown(response.text))
```

### ✅ Count Tokens

```python
# Count tokens
response = client.models.count_tokens(
    model=MODEL_ID,
    contents="why is the sky blue?",
)

print(response)
```

```python
# Compute tokens
response = client.models.compute_tokens(
    model=MODEL_ID,
    contents="why is the sky blue?",
)

print(response)
```
