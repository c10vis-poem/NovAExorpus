#!/usr/bin/env python3
"""guards.py {raw|wiki} (DRAFT) -- PreToolUse(Write|Edit|MultiEdit). Only ever answers 'ask' (owner can approve) or nothing.
raw : paths under raw/, raw_database/, references/ are immutable (wiki-admin-ingest SKILL hard rule 1).
wiki: paths under wiki/ (except wiki/_archive/) are reached through promote.py only (corpus-ingest.md rule 2).
WIKI_ADMIN_INGEST=1 (set by the hash-store step) skips 'raw'. Exit is always 0; reading is never touched."""
import json, os, sys
RULES = {"raw": (("raw", "raw_database", "references"), "immutable source folder"),
         "wiki": (("wiki",), "wiki pages are promoted with promote.py after the audit and your approval")}
def main():
    kind = sys.argv[1]
    if kind == "raw" and os.environ.get("WIKI_ADMIN_INGEST") == "1":
        return
    ev = json.load(sys.stdin)
    p = (ev.get("tool_input") or {}).get("file_path") or ""
    parts = os.path.normpath(p).split(os.sep)
    names, why = RULES[kind]
    if any(n in parts[:-1] for n in names) and not (kind == "wiki" and "_archive" in parts):
        json.dump({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "ask",
                   "permissionDecisionReason": f"wiki-admin: {p} is in a guarded folder ({why}). Approve only if intended."}}, sys.stdout)
try:
    main()
except Exception:
    pass
