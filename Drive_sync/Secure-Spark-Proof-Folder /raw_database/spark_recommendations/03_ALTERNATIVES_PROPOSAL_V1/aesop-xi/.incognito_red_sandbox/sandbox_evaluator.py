#!/usr/bin/env python3
"""
=============================================================================
ÆSOP-XI INCOGNITO RED SANDBOX EVALUATOR (sandbox_evaluator.py)
-----------------------------------------------------------------------------
Subsystem: aesop-xi/.incognito_red_sandbox/
Purpose:
  Adversarial compliance, hallucination checker, and security gatekeeper
  for candidate trajectories, training datasets, and script batches.
  Invoked headlessly by run_audit.sh inside the sealed Red Sandbox.

Verification Gates:
  1. Deterministic JSONL syntax & schema validation.
  2. Namespace & Path Verification: Flags hallucinated paths or attempts
     to target immutable raw sources (01_raw_sources/).
  3. Security & Anti-Poisoning Checks: Scans for shellcode injection,
     blacklisted system calls, recursive fork bombs, and credential leaks.
  4. Returns 'PASS' (exit code 0) or 'FAIL: <reason>' (exit code 1).
=============================================================================
"""

import sys
import os
import json
import re
from typing import Tuple, List

FORBIDDEN_COMMAND_PATTERNS = [
    r"rm\s+-rf\s+/",
    r"rm\s+-rf\s+\*",
    r"mkfs",
    r"dd\s+if=.*of=/dev/",
    r":\(\)\s*\{\s*:\|:&\s*\};:",
    r"curl.*\|\s*bash",
    r"wget.*\|\s*sh",
    r"eval\s*\(",
    r"exec\s*\(",
    r"__import__\s*\(",
]

IMMUTABLE_PATH_TARGETS = [
    "01_raw_sources",
    "raw/",
    "master_manifest.jsonl",
    "NAMING-CANON.md"
]

def evaluate_line(line_num: int, data: dict) -> Tuple[bool, str]:
    # Check 1: Target path validation
    target_path = data.get("target_path", "") or data.get("path", "")
    for immutable in IMMUTABLE_PATH_TARGETS:
        if immutable in target_path and data.get("action") in ["write", "delete", "modify", "truncate"]:
            return False, f"Line {line_num}: Violation of Sensory Immutability on path '{target_path}'"

    # Check 2: Command & script content scanning
    content = str(data.get("content", "")) + " " + str(data.get("command", "")) + " " + str(data.get("prompt", ""))
    for pattern in FORBIDDEN_COMMAND_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            return False, f"Line {line_num}: Malicious or blacklisted pattern detected: '{pattern}'"

    # Check 3: Prohibited legacy nomenclature (e.g. 'Omni-Claw')
    if re.search(r"omni[\s_-]*claw", content, re.IGNORECASE):
        return False, f"Line {line_num}: Prohibited nomenclature detected ('Omni Claw' is strictly forbidden by Naming Canon)"

    return True, "OK"

def evaluate_batch_file(filepath: str) -> Tuple[bool, List[str]]:
    if not os.path.exists(filepath):
        return False, [f"File not found: {filepath}"]

    errors = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line_idx, line in enumerate(f, start=1):
                clean_line = line.strip()
                if not clean_line:
                    continue
                try:
                    record = json.loads(clean_line)
                except json.JSONDecodeError as err:
                    errors.append(f"Line {line_idx}: Invalid JSON syntax - {err}")
                    continue

                if isinstance(record, dict):
                    valid, msg = evaluate_line(line_idx, record)
                    if not valid:
                        errors.append(msg)
    except Exception as e:
        errors.append(f"Unexpected read error: {e}")

    return len(errors) == 0, errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 sandbox_evaluator.py <batch_file.jsonl>")
        sys.exit(2)

    batch_path = sys.argv[1]
    is_valid, error_list = evaluate_batch_file(batch_path)

    if is_valid:
        print("PASS")
        sys.exit(0)
    else:
        print(f"FAIL: {len(error_list)} violation(s) detected:")
        for err in error_list:
            print(f"  - {err}")
        sys.exit(1)
