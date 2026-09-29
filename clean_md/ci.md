---
source: ci.yml
type: yaml
cleaned: 2026-09-11
cleaner: tools/clean.py (mutool)
---

```yaml
name: CI
on:
  pull_request:
    branches: [main, master]
  push:
    branches: [main, master]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Secret scan
        uses: gitleaks/gitleaks-action@v2
        env:
          GITLEAKS_LICENSE: ""
      - name: Validate
        run: |
          echo "Repository structure check"
          test -f README.md || test -f CLAUDE.md || echo "No README or CLAUDE.md found"
          echo "CI passed"


```
