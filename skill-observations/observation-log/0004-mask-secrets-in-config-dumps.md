---
id: 4
title: Config inspection dumped live bearer tokens into the transcript
status: open
type: open-source
skill: [android-termux-operator]
proposes_skill: []
siblings_checked: none (no skill-families.md registry present on device)
area: Safety section — read-only inspection
date: 2026-09-25
session_context: Reviewing MCP server config (~/.claude.json) and a systemd unit on a GCP VM during a cost/architecture audit
resolved:
resolution:
reference:
---

**Issue:** Two "read-only" inspections printed secrets into the conversation: `cat` of a systemd unit containing an OpenRouter API key, and a python one-liner printing MCP server entries including `Authorization: Bearer` headers for two services. Read-only was treated as harmless, but anything printed becomes part of the transcript and requires key rotation.

**Suggested improvement:** Add to android-termux-operator Safety: "When inspecting config files, units, .env, or MCP entries, redact values of keys matching key/token/secret/password/Authorization before printing (e.g. pipe through `sed -E 's/(key|token|secret|password|Bearer)[^\"]*/\1=<redacted>/Ig'`), or print only key names."

**Principle:** Read-only is not side-effect-free: printing a secret leaks it to the transcript. Redact by default in any inspection of configuration, and treat an accidental print as requiring rotation.
