#!/usr/bin/env python3
"""
extract_artifacts.py (Upgraded from doc_to_skill_and_tool.py)
-------------------------------------------------------------
Portable 1-to-N and N-to-1 Action-Artifact, Variable & Asset Extractor for NovAExorpus.
Runs identically on a custom Android terminal APK and Linux (NVIDIA Jetson / Orin Nano).

Capabilities:
  1. 1-to-N Extraction: Extracts multiple CLI tools (.sh), Python wrappers (.py),
     event hooks, JSON/YAML schemas/policies, Obsidian Bases (.base) / Canvas (.canvas),
     environment variable registries, and full (untruncated) SKILL.md files from a single document.
  2. N-to-1 Multi-Doc Compilation: Accepts 1 or more source/clean_md files and merges
     their extracted tools, variables, and procedural sections into a unified skill/tool set
     while preserving full SHA-256 provenance for every contributing document.
  3. Built-in Syntax & Secret Gate: Runs AST / bash -n checks and scans for leaked tokens
     before registering in 04_skills_runtime/manifest.jsonl.
"""
import argparse
import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Set, Tuple

DEFAULT_VAULT = "/storage/emulated/0/Documents/NovAExorpus"
PRIVATE_TAGS = {"private", "pii", "personal", "secret", "confidential"}
# Whole-document credential check (same families as gemini_infer.py CRED). The vault is public:
# a document holding a key is refused outright, because its full text is copied into SKILL.md.
DOC_CRED = re.compile(r"\bsk-[A-Za-z0-9_\-]{16,}|\bm0sk_\w{8,}|\bAIza[0-9A-Za-z_\-]{30,}"
                      r"|\bgh[pousr]_[A-Za-z0-9]{30,}|BEGIN [A-Z ]*PRIVATE KEY")


def refuse_reason(src: Path, text: str) -> str:
    """Return why a source must not be extracted into the public vault, or ''."""
    if "private-memory" in src.resolve().parts:
        return "under private-memory/"
    if DOC_CRED.search(text):
        return "contains a credential pattern"
    fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    head = (fm.group(1) if fm else "").lower()
    for tag in PRIVATE_TAGS:
        if re.search(rf"(tags|privacy|sensitivity)\s*:.*\b{tag}\b", head) or re.search(rf"(^|\s)#{tag}\b", text.lower()):
            return f"tagged {tag}"
    return ""


SECRET_PATTERNS = re.compile(
    r"(sk-[A-Za-z0-9]{20,}|m0sk_[A-Za-z0-9_]+|AIza[0-9A-Za-z\-_]{35}|"
    r"ghp_[A-Za-z0-9]{36}|-----BEGIN [A-Z ]*PRIVATE KEY-----|master_token\.json)"
)

CODE_BLOCK_RE = re.compile(r"```([a-zA-Z0-9_\-\.]+)\n(.*?)```", re.DOTALL)
ENV_VAR_RE = re.compile(r"\b([A-Z][A-Z0-9_]{2,})\b(?:\s*=\s*([^\s\n#\"']+|\"[^\"]*\"|'[^']*'))?")
HOOK_KEYWORDS = re.compile(
    r"\b(PreToolUse|PostToolUse|SessionStart|SessionEnd|Stop|post-commit|post-checkout|pre-commit)\b",
    re.IGNORECASE,
)


def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def slugify(text: str) -> str:
    text = text.lower().replace("æ", "ae").replace("œ", "oe")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "extracted-artifact"


def check_syntax(filepath: Path, lang: str) -> Tuple[bool, str]:
    if lang == "python":
        try:
            ast.parse(filepath.read_text(encoding="utf-8"))
            return True, "ast_ok"
        except SyntaxError as exc:
            return False, f"SyntaxError: {exc}"
    if lang in ("bash", "sh"):
        try:
            res = subprocess.run(
                ["bash", "-n", str(filepath)],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if res.returncode == 0:
                return True, "bash_n_ok"
            return False, res.stderr.strip()
        except FileNotFoundError:
            return True, "bash_not_found_skipped"
    return True, "unchecked"


def extract_from_documents(
    source_files: List[Path],
    vault_root: Path,
    merged_name: str = "",
    min_code_len: int = 20,
) -> Dict:
    skills_dir = vault_root / "04_skills_runtime" / "prompt_skills"
    tools_cli_dir = vault_root / "04_skills_runtime" / "extracted_tools" / "cli"
    tools_py_dir = vault_root / "04_skills_runtime" / "extracted_tools" / "wrappers"
    hooks_dir = vault_root / "04_skills_runtime" / "runtimes" / "hooks"
    policies_dir = vault_root / "04_skills_runtime" / "policies"
    manifest_file = vault_root / "04_skills_runtime" / "manifest.jsonl"

    for d in (skills_dir, tools_cli_dir, tools_py_dir, hooks_dir, policies_dir):
        d.mkdir(parents=True, exist_ok=True)

    if merged_name:
        base_slug = slugify(merged_name)
    elif len(source_files) == 1:
        base_slug = slugify(source_files[0].stem)
    else:
        base_slug = slugify(f"combined-{source_files[0].stem}-{len(source_files)}docs")

    base_py_name = base_slug.replace("-", "_")

    extracted_artifacts: List[Dict] = []
    env_vars_found: Dict[str, Set[str]] = {}
    combined_sections: List[str] = []
    source_records: List[Dict] = []

    block_counter = 0

    for src in source_files:
        if not src.exists():
            print(f"[!] Skipping missing file: {src}", file=sys.stderr)
            continue

        raw_text = src.read_text(encoding="utf-8", errors="ignore")
        why = refuse_reason(src, raw_text)
        if why:
            print(f"[!] REFUSED {src}: {why}; nothing extracted from it", file=sys.stderr)
            continue
        src_hash = sha256_file(src)
        rel_src = (
            str(src.relative_to(vault_root))
            if vault_root in src.resolve().parents
            else str(src)
        )
        source_records.append({"path": rel_src, "sha256": src_hash})
        combined_sections.append(f"## Source: `{rel_src}` (`{src_hash[:12]}`)\n\n{raw_text.strip()}")

        # 1. Extract Environment Variables & Tunables
        for var_name, var_val in ENV_VAR_RE.findall(raw_text):
            if var_name in {"TRUE", "FALSE", "NULL", "NONE", "TODO", "NOTE", "PASS", "FAIL", "JSON", "YAML", "HTTP", "HTTPS"}:
                continue
            env_vars_found.setdefault(var_name, set())
            if var_val:
                env_vars_found[var_name].add(var_val.strip("\"'"))

        # 2. Extract Fenced Code Blocks (1-to-N: CLI tools, Python wrappers, Hooks, Policies/Schemas)
        for lang_raw, code in CODE_BLOCK_RE.findall(raw_text):
            lang = lang_raw.strip().lower()
            code_stripped = code.strip()
            if len(code_stripped) < min_code_len:
                continue

            if SECRET_PATTERNS.search(code_stripped):
                print(f"[!] Quarantined block in {src.name}: matched secret leak regex", file=sys.stderr)
                continue

            is_hook = bool(HOOK_KEYWORDS.search(code_stripped))

            if lang in ("bash", "sh", "zsh", "shell"):
                target_dir = hooks_dir if is_hook else tools_cli_dir
                kind = "hook_shell" if is_hook else "cli_shell"
                out_file = target_dir / f"{base_py_name}_{'hook' if is_hook else 'tool'}_{block_counter}.sh"
                if not code_stripped.startswith("#!"):
                    code_stripped = f"#!/usr/bin/env bash\nset -euo pipefail\n\n{code_stripped}"
                out_file.write_text(code_stripped + "\n", encoding="utf-8")
                try:
                    out_file.chmod(0o755)  # Safe no-op on Android /sdcard FUSE mounts
                except OSError:
                    pass
                valid, check_msg = check_syntax(out_file, "bash")

            elif lang in ("python", "py"):
                target_dir = hooks_dir if is_hook else tools_py_dir
                kind = "hook_python" if is_hook else "python_wrapper"
                out_file = target_dir / f"{base_py_name}_{'hook' if is_hook else 'tool'}_{block_counter}.py"
                if not code_stripped.startswith("#!"):
                    code_stripped = f"#!/usr/bin/env python3\n\n{code_stripped}"
                out_file.write_text(code_stripped + "\n", encoding="utf-8")
                try:
                    out_file.chmod(0o755)
                except OSError:
                    pass
                valid, check_msg = check_syntax(out_file, "python")

            elif lang in ("json", "yaml", "yml", "base", "canvas"):
                ext = "yaml" if lang == "yml" else lang
                out_file = policies_dir / f"{base_slug}_schema_{block_counter}.{ext}"
                out_file.write_text(code_stripped + "\n", encoding="utf-8")
                kind = f"policy_or_asset_{ext}"
                valid, check_msg = True, "schema_saved"
            else:
                continue

            block_counter += 1
            rel_out = str(out_file.relative_to(vault_root))
            extracted_artifacts.append(
                {
                    "type": "hook" if is_hook else ("policy" if "policy" in kind else "tool"),
                    "subtype": kind,
                    "path": rel_out,
                    "sha256": sha256_file(out_file)[:16],
                    "syntax_valid": valid,
                    "syntax_note": check_msg,
                    "source_path": rel_src,
                }
            )
            print(f"  [+] Extracted {kind}: {rel_out} ({check_msg})")

    if not source_records:
        print("[!] No source was extracted; nothing written", file=sys.stderr)
        return {}

    # 3. Write Extracted Variables & Asset Registry JSON if variables were found
    if env_vars_found:
        vars_payload = {
            "artifact_id": base_slug,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "sources": source_records,
            "variables": {
                k: sorted(list(v)) if v else ["<unset>"]
                for k, v in sorted(env_vars_found.items())
            },
        }
        vars_file = policies_dir / f"{base_slug}_variables.json"
        vars_file.write_text(json.dumps(vars_payload, indent=2) + "\n", encoding="utf-8")
        rel_vars = str(vars_file.relative_to(vault_root))
        extracted_artifacts.append(
            {
                "type": "variables_registry",
                "subtype": "env_and_tunables_json",
                "path": rel_vars,
                "sha256": sha256_file(vars_file)[:16],
                "syntax_valid": True,
                "syntax_note": f"{len(env_vars_found)} variables extracted",
            }
        )
        print(f"  [+] Extracted variable registry ({len(env_vars_found)} vars): {rel_vars}")

    # 4. Write Full (Untruncated) Modular SKILL.md into 04_skills_runtime/prompt_skills/<slug>/SKILL.md
    skill_subdir = skills_dir / base_slug
    skill_subdir.mkdir(parents=True, exist_ok=True)
    skill_file = skill_subdir / "SKILL.md"

    tool_paths = [a["path"] for a in extracted_artifacts if a["type"] in ("tool", "hook")]
    source_paths = [s["path"] for s in source_records]

    vars_table_lines = []
    if env_vars_found:
        vars_table_lines.append("## Extracted Environment Variables & Tunables\n")
        vars_table_lines.append("| Variable | Observed Default / Values |")
        vars_table_lines.append("|---|---|")
        for k, vals in sorted(env_vars_found.items()):
            val_str = ", ".join(f"`{v}`" for v in sorted(vals)) if vals else "*not stated*"
            vars_table_lines.append(f"| `{k}` | {val_str} |")
        vars_table_lines.append("")

    tools_table_lines = []
    if extracted_artifacts:
        tools_table_lines.append("## Extracted Tools, Hooks & Schemas\n")
        tools_table_lines.append("| Type | Subtype | Path | Validation |")
        tools_table_lines.append("|---|---|---|---|")
        for a in extracted_artifacts:
            tools_table_lines.append(
                f"| `{a['type']}` | `{a['subtype']}` | `{a['path']}` | `{a['syntax_note']}` |"
            )
        tools_table_lines.append("")

    yaml_frontmatter = (
        f"---\n"
        f"name: {base_slug}\n"
        f"description: Procedural skill and operational workflow compiled from {', '.join(Path(p).name for p in source_paths)}.\n"
        f"extracted_at: {datetime.now(timezone.utc).isoformat()}\n"
        f"sources: {json.dumps(source_paths)}\n"
        f"extracted_tools: {json.dumps(tool_paths)}\n"
        f"---\n\n"
    )

    full_skill_body = (
        f"# {base_slug}\n\n"
        + ("\n".join(vars_table_lines) + "\n" if vars_table_lines else "")
        + ("\n".join(tools_table_lines) + "\n" if tools_table_lines else "")
        + "\n\n".join(combined_sections)
        + "\n"
    )

    skill_file.write_text(yaml_frontmatter + full_skill_body, encoding="utf-8")
    rel_skill = str(skill_file.relative_to(vault_root))
    print(f"  [+] Wrote full SKILL.md: {rel_skill}")

    # 5. Append to 04_skills_runtime/manifest.jsonl
    combined_hash_input = "".join(s["sha256"] for s in source_records).encode("utf-8")
    combined_hash = hashlib.sha256(combined_hash_input).hexdigest()

    manifest_entry = {
        "id": f"EXT_{combined_hash[:16]}",
        "path": rel_skill,
        "tier": 4,
        "category": "extracted_skill_and_tools",
        "sha256": sha256_file(skill_file),
        "sources": source_records,
        "skill_created": rel_skill,
        "skills_tools_extracted": extracted_artifacts,
        "variables_count": len(env_vars_found),
        "last_synced": datetime.now(timezone.utc).isoformat(),
    }

    manifest_file.parent.mkdir(parents=True, exist_ok=True)
    # Re-running the same sources replaces their entry instead of appending a duplicate.
    kept = []
    if manifest_file.exists():
        for line in manifest_file.read_text(encoding="utf-8").splitlines():
            try:
                if json.loads(line).get("id") == manifest_entry["id"]:
                    continue
            except ValueError:
                pass
            kept.append(line)
    kept.append(json.dumps(manifest_entry))
    manifest_file.write_text("\n".join(kept) + "\n", encoding="utf-8")
    print(f"  [OK] Registered in {manifest_file.relative_to(vault_root)}")
    return manifest_entry


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract 1-to-N or N-to-1 skills, tools, hooks, variables, and schemas into 04_skills_runtime/."
    )
    parser.add_argument(
        "sources",
        nargs="+",
        type=Path,
        help="One or more source/clean_md files to extract or combine.",
    )
    parser.add_argument(
        "--vault-root",
        type=Path,
        default=Path(os.environ.get("VAULT_ROOT", DEFAULT_VAULT)).expanduser(),
        help=f"Path to the vault root (defaults to $VAULT_ROOT or {DEFAULT_VAULT}).",
    )
    parser.add_argument(
        "--name",
        type=str,
        default="",
        help="Optional canonical slug name when combining multiple documents (N-to-1).",
    )
    parser.add_argument(
        "--min-code-len",
        type=int,
        default=20,
        help="Minimum character length for a fenced code block to be extracted (default: 20).",
    )
    args = parser.parse_args()

    entry = extract_from_documents(
        source_files=args.sources,
        vault_root=args.vault_root.resolve(),
        merged_name=args.name,
        min_code_len=args.min_code_len,
    )
    if not entry:
        sys.exit(2)


if __name__ == "__main__":
    main()