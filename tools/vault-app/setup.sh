#!/usr/bin/env bash
# One-time setup of the vault GitHub App, which replaces the VAULT_DISPATCH_TOKEN PAT.
# Each Actions run then mints its own 1-hour token, so nothing ever needs renewing.
#
#   bash tools/vault-app/setup.sh            # create app, install, store keys, verify
#   bash tools/vault-app/setup.sh --drop-pat # same, then delete the old PAT secret
#
# Needs: gh (logged in, repo scope), python3, curl, jq, openssl. Works in Termux.
# Your taps: "Create ..." + "Create GitHub App" (step 1), then "Install" (step 2).
set -euo pipefail

OWNER=c10vis-poem
VAULT=NovAExorpus
BASE_REPOS=(NovAExopia Hyperion-XI CloviX-AEyre AEthX-AEsc NovusAExenti)
PORT=8765
KEY_DIR="$HOME/.config/vault-app"
HERE="$(cd "$(dirname "$0")" && pwd)"
DROP_PAT=0
[ "${1:-}" = "--drop-pat" ] && DROP_PAT=1

for cmd in gh python3 curl jq openssl; do
  command -v "$cmd" >/dev/null || { echo "Missing: $cmd (Termux: pkg install gh python curl jq openssl)"; exit 1; }
done
gh auth status >/dev/null 2>&1 || { echo "Run: gh auth login"; exit 1; }
mkdir -p "$KEY_DIR"; chmod 700 "$KEY_DIR"

open_url() { termux-open-url "$1" 2>/dev/null || xdg-open "$1" 2>/dev/null || true; echo "  $1"; }

# Step 1: create the app from a pre-filled manifest (skipped if one already exists).
if [ -f "$KEY_DIR/app.json" ]; then
  echo "Step 1: app already created ($(jq -r .slug "$KEY_DIR/app.json")), reusing it."
else
  name="nvaex-vault-$(openssl rand -hex 3)"
  code_file="$(mktemp)"; rm -f "$code_file"
  echo "Step 1: open this page and tap the button, then 'Create GitHub App':"
  python3 "$HERE/manifest_server.py" "$PORT" "$code_file" "$name" &
  server=$!
  sleep 1; open_url "http://127.0.0.1:$PORT/"
  wait "$server"
  code="$(cat "$code_file")"; rm -f "$code_file"
  # The code is single-use and expires after an hour; this turns it into the app id + key.
  resp="$(gh api -X POST "/app-manifests/$code/conversions")"
  (umask 077
   jq -r .pem <<<"$resp" > "$KEY_DIR/private-key.pem"
   jq '{id, slug, html_url}' <<<"$resp" > "$KEY_DIR/app.json")
  echo "  Created $(jq -r .slug "$KEY_DIR/app.json") (key saved in $KEY_DIR)."
fi
APP_ID="$(jq -r .id "$KEY_DIR/app.json")"
SLUG="$(jq -r .slug "$KEY_DIR/app.json")"
PEM="$KEY_DIR/private-key.pem"

# Step 2: install it on the vault repo (the only repo it needs to reach).
echo
echo "Step 2: tap 'Only select repositories', pick $VAULT, then tap Install:"
open_url "https://github.com/apps/$SLUG/installations/new"
read -r -p "  Press Enter once it is installed. " _

# Step 3: store the app id and key in every repo whose workflow mints tokens.
echo
echo "Step 3: storing VAULT_APP_ID and VAULT_APP_PRIVATE_KEY"
for r in "${BASE_REPOS[@]}" "$VAULT"; do
  gh variable set VAULT_APP_ID -R "$OWNER/$r" --body "$APP_ID" >/dev/null
  gh secret set VAULT_APP_PRIVATE_KEY -R "$OWNER/$r" < "$PEM" >/dev/null
  echo "  $r ok"
done

# Step 4: prove it end to end: sign a JWT, get an installation token, send one dispatch.
echo
echo "Step 4: verifying"
b64url() { openssl base64 -A | tr '+/' '-_' | tr -d '='; }
now=$(date +%s)
header=$(printf '{"alg":"RS256","typ":"JWT"}' | b64url)
payload=$(printf '{"iat":%d,"exp":%d,"iss":"%s"}' $((now - 60)) $((now + 540)) "$APP_ID" | b64url)
sig=$(printf '%s.%s' "$header" "$payload" | openssl dgst -sha256 -sign "$PEM" -binary | b64url)
jwt="$header.$payload.$sig"
api() { curl -fsS -H "Accept: application/vnd.github+json" "$@"; }
inst=$(api -H "Authorization: Bearer $jwt" "https://api.github.com/repos/$OWNER/$VAULT/installation" | jq -r .id) \
  || { echo "  The app is not installed on $VAULT yet. Install it, then run this script again."; exit 1; }
token=$(api -X POST -H "Authorization: Bearer $jwt" "https://api.github.com/app/installations/$inst/access_tokens" | jq -r .token)
api -X POST -H "Authorization: Bearer $token" "https://api.github.com/repos/$OWNER/$VAULT/dispatches" \
  -d '{"event_type":"base-repo-updated","client_payload":{"repo":"vault-app-setup-check"}}'
echo "  Dispatch to $VAULT accepted. The app works."

# Step 5 (optional): retire the PAT.
if [ "$DROP_PAT" = 1 ]; then
  echo
  echo "Step 5: deleting the old VAULT_DISPATCH_TOKEN secret"
  for r in "${BASE_REPOS[@]}" "$VAULT"; do
    gh secret delete VAULT_DISPATCH_TOKEN -R "$OWNER/$r" 2>/dev/null && echo "  $r removed" || echo "  $r had none"
  done
  echo "  Last tap: delete the token itself on this page:"
  open_url "https://github.com/settings/tokens"
fi
echo
echo "Done. Nothing here expires; the app key lives in $KEY_DIR and in the repo secrets."
