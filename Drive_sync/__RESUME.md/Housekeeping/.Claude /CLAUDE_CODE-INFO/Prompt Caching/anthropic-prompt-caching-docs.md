# Anthropic Prompt Caching — Official Documentation

Source: "PROMPT.CACHING#" (Drive `1JmZhTGG33Zh1pKjli4zyaN-h_Q_pcsTnM6LFWfEJz5Y`, Google Doc — appears to be a copy/export of Anthropic's official prompt-caching documentation page). Category: **official API reference documentation**. **HIGH PRIORITY** per the user, alongside the skills work. Note: the extracted content ends mid-sentence in the "Edge cases" section ("If the last block has an explicit `cache_control` with a...") — the source document appears to be truncated at that point; treat this as a faithful-but-incomplete transcription and consult Anthropic's live docs for the full edge-case list if needed.

## Overview

Prompt caching optimizes API usage by allowing resuming from specific prefixes in prompts, significantly reducing processing time and costs for repetitive tasks or prompts with consistent elements.

This feature is eligible for Zero Data Retention (ZDR) — when an organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

Two ways to enable prompt caching:
- **Automatic caching**: add a single `cache_control` field at the top level of the request. The system automatically applies the cache breakpoint to the last cacheable block and moves it forward as conversations grow. Best for multi-turn conversations where the growing message history should be cached automatically.
- **Explicit cache breakpoints**: place `cache_control` directly on individual content blocks for fine-grained control over exactly what gets cached.

### Simplest example (automatic caching, cURL)

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "cache_control": {"type": "ephemeral"},
    "system": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.",
    "messages": [
      {
        "role": "user",
        "content": "Analyze the major themes in Pride and Prejudice."
      }
    ]
  }'
```

### Equivalent (Python)

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},
    system="You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.",
    messages=[
        {
            "role": "user",
            "content": "Analyze the major themes in 'Pride and Prejudice'.",
        }
    ],
)
print(response.usage.model_dump_json())
```

*(The source document also shows equivalent examples in TypeScript, C#, Go, Java, PHP, Ruby, and a dedicated `ant` CLI YAML form — all functionally identical, just language-specific SDK syntax. Not all reproduced here; the shape is: set `model`, `max_tokens`, `cache_control: {"type": "ephemeral"}`, `system`, and `messages`, then read `response.usage` for the cache token breakdown.)*

With automatic caching, the system caches all content up to and including the last cacheable block. On subsequent requests with the same prefix, cached content is reused automatically.

## How Prompt Caching Works

When a request with prompt caching enabled is sent:
1. The system checks if a prompt prefix, up to a specified cache breakpoint, is already cached from a recent query.
2. If found, it uses the cached version, reducing processing time and costs.
3. Otherwise, it processes the full prompt and caches the prefix once the response begins.

Especially useful for: prompts with many examples; large amounts of context or background information; repetitive tasks with consistent instructions; long multi-turn conversations.

By default, the cache has a **5-minute lifetime**, refreshed for no additional cost each time the cached content is used. A **1-hour cache duration** is available at additional cost for cases where 5 minutes is too short.

**Prompt caching caches the full prefix**: it references the entire prompt — `tools`, `system`, and `messages` (in that order) — up to and including the block designated with `cache_control`.

## Pricing

Price per million tokens by model (as captured in this source document):

| Model | Base Input Tokens | 5m Cache Writes | 1h Cache Writes | Cache Hits & Refreshes | Output Tokens |
|---|---|---|---|---|---|
| Claude Opus 4.8 | $5 / MTok | $6.25 / MTok | $10 / MTok | $0.50 / MTok | $25 / MTok |
| Claude Opus 4.7 | $5 / MTok | $6.25 / MTok | $10 / MTok | $0.50 / MTok | $25 / MTok |
| Claude Opus 4.6 | $5 / MTok | $6.25 / MTok | $10 / MTok | $0.50 / MTok | $25 / MTok |
| Claude Opus 4.5 | $5 / MTok | $6.25 / MTok | $10 / MTok | $0.50 / MTok | $25 / MTok |
| Claude Opus 4.1 | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
| Claude Opus 4 (deprecated) | $15 / MTok | $18.75 / MTok | $30 / MTok | $1.50 / MTok | $75 / MTok |
| Claude Sonnet 4.6 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
| Claude Sonnet 4.5 | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
| Claude Sonnet 4 (deprecated) | $3 / MTok | $3.75 / MTok | $6 / MTok | $0.30 / MTok | $15 / MTok |
| Claude Haiku 4.5 | $1 / MTok | $1.25 / MTok | $2 / MTok | $0.10 / MTok | $5 / MTok |
| Claude Haiku 3.5 (retired except Bedrock/Vertex AI) | $0.80 / MTok | $1 / MTok | $1.60 / MTok | $0.08 / MTok | $4 / MTok |

Pricing multipliers reflected in the table: 5-minute cache write tokens are **1.25x** base input token price; 1-hour cache write tokens are **2x** base input token price; cache read tokens are **0.1x** base input token price. These multipliers stack with other pricing modifiers such as the Batch API discount and data residency.

## Supported Models

Prompt caching (both automatic and explicit) is supported on all active Claude models.

## Automatic Caching

Add a single `cache_control` field at the top level of the request body — no need to place it on individual content blocks. The system automatically applies the cache breakpoint to the last cacheable block.

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "cache_control": {"type": "ephemeral"},
    "system": "You are a helpful assistant that remembers our conversation.",
    "messages": [
      {"role": "user", "content": "My name is Alex. I work on machine learning."},
      {"role": "assistant", "content": "Nice to meet you, Alex! How can I help with your ML work today?"},
      {"role": "user", "content": "What did I say I work on?"}
    ]
  }'
```

### How Automatic Caching Works in Multi-Turn Conversations

The cache point moves forward automatically as conversations grow. Each new request caches everything up to the last cacheable block, and previous content is read from cache:

| Request | Content | Cache behavior |
|---|---|---|
| Request 1 | System + User(1) + Asst(1) + **User(2)** ◀ cache | Everything written to cache |
| Request 2 | System + User(1) + Asst(1) + User(2) + Asst(2) + **User(3)** ◀ cache | System through User(2) read from cache; Asst(2) + User(3) written to cache |
| Request 3 | System + User(1) + Asst(1) + User(2) + Asst(2) + User(3) + Asst(3) + **User(4)** ◀ cache | System through User(3) read from cache; Asst(3) + User(4) written to cache |

The cache breakpoint automatically moves to the last cacheable block in each request — no need to manually update `cache_control` markers as the conversation grows.

### TTL Support

By default, automatic caching uses a 5-minute TTL. Specify a 1-hour TTL at 2x the base input token price:

```json
{ "cache_control": { "type": "ephemeral", "ttl": "1h" } }
```

### Combining With Block-Level Caching

Automatic caching is compatible with explicit cache breakpoints. When used together, the automatic cache breakpoint uses one of the 4 available breakpoint slots. Example — explicit breakpoint on the system prompt, automatic caching handling the conversation:

```json
{
  "model": "claude-opus-4-8",
  "max_tokens": 1024,
  "cache_control": { "type": "ephemeral" },
  "system": [
    {
      "type": "text",
      "text": "You are a helpful assistant.",
      "cache_control": { "type": "ephemeral" }
    }
  ],
  "messages": [{ "role": "user", "content": "What are the key terms?" }]
}
```

### What Stays the Same

Automatic caching uses the same underlying caching infrastructure. Pricing, minimum token thresholds, context ordering requirements, and the 20-block lookback window all apply the same as with explicit breakpoints.

### Edge Cases

- If the last block already has an explicit `cache_control` with the same TTL, automatic caching is a no-op.
- If the last block has an explicit `cache_control` with a *(document truncated here in the source — this bullet point's ending was cut off)*

## Relative Doc Links Referenced in This Page

The source document contains several relative links to other Anthropic docs pages (paths as found, likely resolving under `docs.anthropic.com` or `docs.claude.com`):
- `/docs/en/build-with-claude/api-and-data-retention` (Zero Data Retention)
- `/docs/en/about-claude/model-deprecations` (model deprecation notices, referenced twice for Opus 4 and Sonnet 4)
- `/docs/en/about-claude/pricing` (full pricing details, referenced for how multipliers stack)
- In-page anchors: `#automatic-caching`, `#explicit-cache-breakpoints`, `#pricing`, `#1-hour-cache-duration`

## Relevance to This Project

This is the authoritative source underpinning the entire NotebookLM planning conversation (see `notebooklm-prompt-caching-planning-qa.md`) — every specific number (pricing multipliers, 5-minute/1-hour TTLs, the tools→system→messages prefix order) traces back to this page. Directly actionable for the eventual Agent CLI / Omni Claw system: the pricing table should drive model selection for cost-sensitive sub-agent tasks (e.g. Haiku 4.5's far cheaper cache-read rate for high-frequency small agents vs. Opus for the main orchestrator), and the exact JSON shapes shown here (top-level `cache_control`, block-level `cache_control` with `ttl`) are the literal request structures the CLI's HTTP client needs to construct.
