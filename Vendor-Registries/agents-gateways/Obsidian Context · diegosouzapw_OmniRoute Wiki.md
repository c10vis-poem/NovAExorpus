<!-- Converted from Obsidian Context · diegosouzapw_OmniRoute Wiki.pdf — 9 pages -->

## Page 1

OmniRoute
Code Issues 248 More
# Obsidian Context
Jump to bottom
github-actions[bot] edited this page on Jun 15 · 1 revision
# 🌍 View in other languages
# Obsidian Context Source
Source of truth: src/lib/obsidian/api.ts (REST + sync client),
src/lib/db/obsidian.ts (token / base-URL / WebDAV persistence),
src/lib/obsidianSync.ts (WebDAV vault sync), open-sse/mcp-
server/tools/obsidianTools.ts (22 MCP tools),
src/app/api/settings/obsidian/route.ts +
src/app/api/settings/obsidian/webdav/route.ts (settings APIs). Tool registration
and scope wiring lives in open-sse/mcp-server/server.ts .
# What it is
# OmniRoute connects to an Obsidian vault as a context source — a local Markdown knowledge
# base that agents read and write through the built-in MCP server. The integration talks to the
# Obsidian Local REST API community plugin running inside the desktop app, so agents can
# search notes, read/write/patch files, list the vault, work with daily/weekly periodic notes,
# manage tags, run Obsidian commands, and (optionally) coordinate a bidirectional
# desktop↔mobile vault sync.
The client ( src/lib/obsidian/api.ts ) wraps the Local REST API with:
5xx Retry with backoff for transient , 30-second timeout via AbortController .
ObsidianAuthError Typed error classification — (401/403), ObsidianNotFoundError
ObsidianServerError (404), (5xx), ObsidianTimeoutError .

---

## Page 2

# A friendly "cannot reach Obsidian" hint that calls out the common port mistake (HTTP on
, not the MCP endpoint on 27124 ) and the Tailscale form.
# Vault-relative path encoding so note paths with spaces/slashes are safe.
# Setup
# There is no environment variable for the Obsidian token or base URL — both are stored in the
key_value obsidian SQLite table (namespace ) via src/lib/db/obsidian.ts . The token is
# encrypted at rest (AES-256-GCM, with plaintext backward-compat fallback). Configure from the
Context Sources tab of the Endpoint dashboard ( ObsidianSourceCard ), or via the settings
# REST API.
# Important
# The Obsidian Local REST API plugin must be installed and running. Its REST interface
127.0.0.1:27123 listens on HTTP (the default base URL). Port 27124 is a separate
# MCP/HTTPS endpoint and is explicitly rejected by the settings route. If connecting from
another device, use http://<tailscale-ip>:27123 .
# Configuration keys (SQLite key_value, namespace obsidian)
# Key Purpose Encrypted
api_key Local REST API bearer token yes
base_url REST base URL (default http://127.0.0.1:27123 ) no
vault_path Absolute path to the vault directory (for sync) no
webdav_username Generated WebDAV username (vault sync) no
webdav_password Generated WebDAV password (vault sync) yes
webdav_enabled Whether WebDAV vault sync is enabled no
# Configure via REST
# Save + validate the Local REST API token (POST validates via a status check) curl -X POST http://localhost:20128/api/settings/obsidian \ -H "Content-Type: application/json" \ -d '{"token":"<obsidian-rest-api-key>","baseUrl":"http://127.0.0.1:27123"}'
# Check connection status (returns connected, hasToken, baseUrl, vaultPath) curl http://localhost:20128/api/settings/obsidian

---

## Page 3

# Disconnect (clears the stored token) curl -X DELETE http://localhost:20128/api/settings/obsidian
POST All methods require dashboard authentication. rejects any URL on port 27124 and
### validates the token by calling the Local REST API status endpoint before persisting.
## WebDAV vault sync
src/app/api/settings/obsidian/webdav/route.ts manages an optional WebDAV-backed
vault sync (driven by src/lib/obsidianSync.ts ). Enabling it points OmniRoute at a local vault
### directory and mints a random WebDAV username/password pair:
# Enable WebDAV sync for a vault directory (mints username/password) curl -X POST http://localhost:20128/api/settings/obsidian/webdav \ -H "Content-Type: application/json" \ -d '{"vaultPath":"/home/me/MyVault"}'
# Get WebDAV sync status (credentials returned only while enabled) curl http://localhost:20128/api/settings/obsidian/webdav
# Disable WebDAV sync (clears credentials + managed .stignore) curl -X DELETE http://localhost:20128/api/settings/obsidian/webdav
## Per-API-key context source (optional)
Obsidian config can be scoped per API key via the api_key_context_sources table
( src/lib/db/apiKeyContextSources.ts ). When an MCP call carries an authenticated API key
id, getObsidianConfigForApiKey() prefers that key's own token/base-URL/vault-path
source: "api_key" ( ) and otherwise falls back to the global config ( source: "global" ).
## MCP tools (22)
### Defined in
### open-sse/mcp-server/tools/obsidianTools.ts . The token/base-URL are resolved
### per call (per-API-key first, then global). Tools that hit the OmniRoute sync server (the four
### obsidian_sync_* tools) additionally require the sync auth token configured in OmniRoute
### settings.
## Read tools (read:obsidian)

---

## Page 4

Tool Description
authenticated.
file paths.
(and/or/regex/path filters).
heading/block/frontmatter.
obsidian_list_vault List files and directories in the vault (tree of entries).
→ line numbers.
full content.
Obsidian.
(today if omitted).
obsidian_get_tags List all vault tags with their frequencies.
obsidian_list_commands obsidian_execute_command ).
uptime, last sync.
detected-at).
### Write tools (write:obsidian)
Tool Description
content.

---

## Page 5

# Tool Description
# Append content to a note; optionally to a specific
obsidian_append_note
# heading/block.
# Surgically append/prepend/replace at a heading,
obsidian_patch_note
# block, or frontmatter field.
| pdf-official | Produce, read, fill, and transform PDF files |
|---|---|
| obsidian_delete_note | Permanently delete a note from the vault. |
| obsidian_move_note | Move or rename a note within the vault. |
| obsidian_execute_command | Execute an Obsidian command by its command ID. |
obsidian_delete_note Permanently delete a note from the vault.
obsidian_move_note Move or rename a note within the vault.
obsidian_execute_command Execute an Obsidian command by its command ID.
# Open a file in Obsidian (creates it if it does not
obsidian_open_file
# exist).
# Trigger an immediate bidirectional
obsidian_sync_trigger
# desktop↔mobile vault sync.
Resolve a sync conflict: keep local (mobile), obsidian_sync_resolve_conflict remote (desktop), or keep-both .
# Note
obsidian_patch_note targetType targets accept of heading | block | frontmatter
operation and of append | prepend | replace , with an optional
createTargetIfMissing . The four obsidian_sync_* tools talk to the local sync server
( http://127.0.0.1:27781 by default) and require the sync token.
# Scopes
read:obsidian Read tools require ; write tools require write:obsidian . Enforcement is
identical to Notion — handled by withScopeEnforcement() in open-sse/mcp-
server/server.ts , gated on OMNIROUTE_MCP_ENFORCE_SCOPES=true , with allowed scopes
sourced from OMNIROUTE_MCP_SCOPES or the API key's scope context. See MCP-SERVER.md.
# Endpoints
# Method Path Purpose
Return { connected, hasToken, GET /api/settings/obsidian baseUrl, vaultPath } .

---

## Page 6

# Method Path Purpose
# Save + validate token (rejects port
POST /api/settings/obsidian 27124 ).
DELETE /api/settings/obsidian Disconnect (clear stored token).
# WebDAV sync status + credentials
GET /api/settings/obsidian/webdav
# (while enabled).
# Enable WebDAV sync for a vault
POST /api/settings/obsidian/webdav
# directory.
DELETE /api/settings/obsidian/webdav Disable WebDAV sync.
# These are dashboard settings routes. The vault itself is reached through the Obsidian
Local REST API (the configured base_url ) and through the MCP tools above — there is
no public /v1 Obsidian proxy endpoint.
# Use cases
Vault-grounded answers — obsidian_search_simple / obsidian_search_structured
then obsidian_read_note so an agent answers from your real notes.
Note authoring / journaling — obsidian_write_note , obsidian_append_note , or the
surgical obsidian_patch_note to log agent output, summaries, or daily notes
( obsidian_get_periodic_note ) into the vault.
Vault navigation — obsidian_list_vault , obsidian_get_document_map , and
obsidian_get_tags to explore structure before reading/writing.
Obsidian automation — obsidian_list_commands + obsidian_execute_command to drive
plugins/commands from an agent; obsidian_open_file to surface a note in the UI.
Mobile sync — enable WebDAV sync, then obsidian_sync_trigger /
obsidian_sync_status / obsidian_sync_conflicts /
obsidian_sync_resolve_conflict to coordinate desktop↔mobile and resolve conflicts.
# Related
# MCP Server — transports, scope enforcement, full tool inventory.
# Notion Context Source — the other built-in context source.
# Memory System — persistent conversational memory (complementary context layer,
# injected automatically rather than tool-fetched).

---

## Page 7

OmniRoute · Website · npm · Docker Hub
### Pages 1,106
# 🏠 Home
# 🌍 Languages (40+)
# 🚀 Getting Started
Setup Guide
User Guide
Features
Quick Start (Docker)
Electron Desktop App
Termux (Android)
PWA Guide
# 🌐 Providers
Provider Reference
All Providers
Free Tiers
Kiro Setup
# 🎯 Routing & Combos
Auto-Combo
Reasoning Replay
# 🗜 Compression
Compression Guide
Compression Engines
RTK Compression
Language Packs
Rules Format
# 🔌 Integrations
MCP Server
A2A Server
Agent Protocols
OpenCode Plugin

---

## Page 8

Webhooks
Cloud Agents
Skills
Memory
Evals
Gamification
## 🏗 Architecture
Architecture Overview
Codebase Documentation
Repository Map
Authorization Guide
Resilience Guide
## 🔒 Security
Guardrails
Compliance
Error Sanitization
Public Credentials
Route Guard Tiers
Stealth Guide
CLI Token Auth
## 📋 Reference
API Reference
CLI Tools
Environment Variables
## 🚀 Operations
VM Deployment
Fly.io Deployment
Tunnels Guide
Proxy Guide
SQLite Runtime
Coverage Plan
Release Checklist
## ℹ More
Troubleshooting
i18n / Translations
Uninstall
Contributing
Comparison vs Alternatives

---

## Page 9

# Clone this wiki locally
https://github.com/diegosouzapw/OmniRoute.wiki.git