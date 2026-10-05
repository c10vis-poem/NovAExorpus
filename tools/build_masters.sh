#!/usr/bin/env bash
# Builds MASTER-AGENTS.md and MASTER-RESUME.md: the real AGENTS.md / RESUME.md
# of every base repo, read from each repo's main branch on GitHub.
# Run by .github/workflows/master-files.yml. No timestamp: the files change only
# when a repo's file changes. Each repo's heading shows the commit its file came from.
set -euo pipefail
cd "$(dirname "$0")/.."
OWNER=c10vis-poem
REPOS=(NovAExorpus aesop-xi novus-aexenti NovAExopia Hyperion-XI novus-aesc novus-aeyre)

build() {
  local file="$1" out="$2"
  {
    echo "# MASTER-${file%.md} (auto-generated, do not hand-edit)"
    echo
    echo "Every base repo's \`$file\` from its \`main\` branch, rebuilt by"
    echo "\`.github/workflows/master-files.yml\` whenever one of them changes."
    echo "Edit the repo's own \`$file\`, never this file."
    for repo in "${REPOS[@]}"; do
      local sha
      sha=$(gh api "repos/$OWNER/$repo/commits?path=$file&sha=main&per_page=1" --jq '.[0].sha // ""' | cut -c1-7)
      echo; echo "---"; echo
      if [ -z "$sha" ]; then
        echo "## $repo"; echo; echo "_No \`$file\` on main yet._"; continue
      fi
      echo "## $repo  (\`$file\` @ $sha)"; echo
      # Demote headings two levels so each repo stays under its own ## section.
      gh api "repos/$OWNER/$repo/contents/$file?ref=main" -H 'Accept: application/vnd.github.raw' \
        | sed -E 's/^(#{1,4}) /##\1 /'
    done
  } > "$out"
}

build AGENTS.md MASTER-AGENTS.md
build RESUME.md MASTER-RESUME.md
