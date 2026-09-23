#!/bin/sh
# Install current OpenWiki (fork c10vis-poem/openwiki, branch upstream-latest)
# on Alpine (Acode terminal), provider OpenRouter. Re-runnable.
set -eu

REPO=https://github.com/c10vis-poem/openwiki.git
BRANCH=upstream-latest
SRC=${OPENWIKI_SRC:-$HOME/openwiki}
CFG=${OPENWIKI_CONFIG_DIR:-$HOME/.openwiki}
MODEL=${OPENWIKI_MODEL_ID:-z-ai/glm-5.2}

node_ok() {
  command -v node >/dev/null 2>&1 || return 1
  node -e 'const [a,b]=process.versions.node.split(".").map(Number);process.exit(a>=24||(a===22&&b>=22)?0:1)'
}

echo "== 1/6 packages =="
apk add --no-cache git npm build-base python3 linux-headers curl
apk add --no-cache nodejs || true
if ! node_ok; then
  echo "node $(node -v 2>/dev/null || echo none) too old (need >=22.22); trying nodejs-current"
  apk del nodejs >/dev/null 2>&1 || true
  apk add --no-cache nodejs-current
fi
node_ok || { echo "STOP: need node >=22.22, have $(node -v)"; exit 1; }
echo "node $(node -v)"

echo "== 2/6 pnpm =="
npm install -g pnpm@11.25.0 node-gyp
pnpm -v

echo "== 3/6 source ($BRANCH) =="
if [ -d "$SRC/.git" ]; then
  git -C "$SRC" fetch origin "$BRANCH" && git -C "$SRC" checkout "$BRANCH" && git -C "$SRC" pull --ff-only
else
  git clone --depth 1 -b "$BRANCH" "$REPO" "$SRC"
fi

echo "== 4/6 build =="
cd "$SRC"
pnpm install --frozen-lockfile
pnpm run build
npm link
openwiki --help >/dev/null && echo "openwiki $(node -p 'require("./package.json").version') on PATH"

echo "== 5/6 OpenRouter config =="
mkdir -p "$CFG"; chmod 700 "$CFG"
touch "$CFG/.env"; chmod 600 "$CFG/.env"
if ! grep -q '^OPENROUTER_API_KEY=' "$CFG/.env"; then
  KEY=${OPENROUTER_API_KEY:-}
  [ -z "$KEY" ] && [ -f "$HOME/.dsh/secrets.env" ] && KEY=$(. "$HOME/.dsh/secrets.env"; printf %s "$OPENROUTER_API_KEY")
  if [ -z "$KEY" ]; then printf 'OpenRouter API key (input hidden): '; stty -echo; read -r KEY; stty echo; echo; fi
  [ -n "$KEY" ] || { echo "STOP: empty key"; exit 1; }
  printf 'OPENROUTER_API_KEY="%s"\n' "$KEY" >> "$CFG/.env"; unset KEY
fi
set_env() { grep -q "^$1=" "$CFG/.env" || printf '%s="%s"\n' "$1" "$2" >> "$CFG/.env"; }
set_env OPENWIKI_PROVIDER openrouter
set_env OPENWIKI_MODEL_ID "$MODEL"
set_env OPENWIKI_PAGE_CONCURRENCY 3
set_env OPENWIKI_OPENROUTER_MAX_TOKENS 8192

echo "== 6/6 verify =="
K=$(sed -n 's/^OPENROUTER_API_KEY="\{0,1\}\([^"]*\)"\{0,1\}$/\1/p' "$CFG/.env" | head -1)
code=$(curl -s -o /dev/null -w '%{http_code}' -H "Authorization: Bearer $K" https://openrouter.ai/api/v1/key); unset K
[ "$code" = 200 ] && echo "OpenRouter key: valid" || echo "OpenRouter key: HTTP $code - check $CFG/.env"
echo "Done. Next: cd <repo> && openwiki --init   |   openwiki personal --init"
