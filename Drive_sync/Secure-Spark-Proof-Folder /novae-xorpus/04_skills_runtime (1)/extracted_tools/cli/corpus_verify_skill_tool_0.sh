#!/usr/bin/env bash
set -euo pipefail

# Standard run — reads 01-sources/, compares against 02-clean/, writes 03-check/
python3 tools/check.py

# Dry run — prints roll-up to stdout, writes nothing
python3 tools/check.py --dry-run
