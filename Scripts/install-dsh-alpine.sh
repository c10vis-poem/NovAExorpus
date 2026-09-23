#!/bin/sh
# Install current DeepSeek Harness (dsh) on Alpine (Acode terminal, tablet)
# with OpenRouter as provider. Re-runnable. Run as root in Acode's Alpine.
set -eu

REPO=https://github.com/deepseek-ai/deepseek-harness.git   # upstream: fork c10vis-poem has no own commits
SRC=${DSH_SRC:-$HOME/deepseek-harness}
DSH_HOME=${DSH_HOME:-$HOME/.dsh}
SECRETS=$DSH_HOME/secrets.env

node_ok() {
  command -v node >/dev/null 2>&1 || return 1
  node -e 'const [a,b]=process.versions.node.split(".").map(Number);process.exit((a===22&&b>=19)||a>=24?0:1)'
}

echo "== 1/7 packages =="
apk add --no-cache git npm build-base python3 linux-headers curl
apk add --no-cache nodejs || true
if ! node_ok; then
  echo "node $(node -v 2>/dev/null || echo none) too old (need ^22.19 or >=24); trying nodejs-current"
  apk del nodejs >/dev/null 2>&1 || true
  apk add --no-cache nodejs-current
fi
node_ok || { echo "STOP: need node ^22.19 or >=24, have $(node -v)"; exit 1; }
echo "node $(node -v)"

echo "== 2/7 pnpm (version pinned by the repo) =="
npm install -g pnpm@11.7.0
pnpm -v

echo "== 3/7 source (upstream latest) =="
if [ -d "$SRC/.git" ]; then git -C "$SRC" pull --ff-only; else git clone --depth 1 "$REPO" "$SRC"; fi
cd "$SRC"; git log --oneline -1

echo "== 4/7 install + build (slow) =="
CI=true pnpm install --frozen-lockfile   # CI=true skips lefthook git-hook install
CI=true pnpm run build

echo "== 5/7 musl shim for node-addon-require-builtin (no musl prebuild exists) =="
D="$SRC/node_modules/node-addon-require-builtin-linux-arm64-musl"
mkdir -p "$D"
cat > "$D/package.json" <<'EOF'
{ "name": "node-addon-require-builtin-linux-arm64-musl", "version": "0.1.6-alpine-shim", "main": "index.js", "private": true }
EOF
cat > "$D/index.js" <<'EOF'
'use strict'
module.exports = {
  requireBuiltin: (id) => require(id),
  isAllowedInternalId: () => true,
  getNativeBindingInfo: () => ({ mode: 'unrestricted', product: 'require-builtin', backend: 'napi', abi: 'napi-v9' }),
}
EOF

echo "== 6/7 OpenRouter key + dsh launcher =="
mkdir -p "$DSH_HOME"; chmod 700 "$DSH_HOME"
if [ ! -s "$SECRETS" ]; then
  printf 'OpenRouter API key (input hidden): '
  stty -echo; read -r KEY; stty echo; echo
  [ -n "$KEY" ] || { echo "STOP: empty key"; exit 1; }
  umask 077; printf 'export OPENROUTER_API_KEY=%s\n' "$KEY" > "$SECRETS"; unset KEY
fi
chmod 600 "$SECRETS"; . "$SECRETS"
[ -f "$DSH_HOME/.credentials.yaml" ] || { umask 077; printf 'OPENROUTER_API_KEY: %s\n' "$OPENROUTER_API_KEY" > "$DSH_HOME/.credentials.yaml"; }
[ -d "$DSH_HOME/profiles" ] || [ -f "$DSH_HOME/settings.yaml" ] || \
  printf 'llm-pi-ai:\n  providers:\n    openrouter:\n      apiKeyEnv: OPENROUTER_API_KEY\n' > "$DSH_HOME/settings.yaml"
cat > /usr/local/bin/dsh <<EOF
#!/bin/sh
[ -f "$SECRETS" ] && . "$SECRETS"
exec node --expose-internals $SRC/apps/cli/lib/bin.js "\$@"
EOF
chmod 755 /usr/local/bin/dsh

echo "== 7/7 verify =="
code=$(curl -s -o /dev/null -w '%{http_code}' -H "Authorization: Bearer $OPENROUTER_API_KEY" https://openrouter.ai/api/v1/key)
[ "$code" = 200 ] && echo "OpenRouter key: valid" || echo "OpenRouter key: HTTP $code - check $SECRETS"
dsh --version
echo "Done. Start: dsh web   then open the printed ?token= URL in the tablet browser."
