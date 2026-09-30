#!/bin/sh
# Termux-only: stand-in for node-addon-require-builtin's missing android-arm64 binding.
# Undo: rm -r "$D"  and remove --expose-internals from $PREFIX/bin/dsh
set -eu
D="$HOME/repos/novus-deepseek-harness/node_modules/node-addon-require-builtin-android-arm64"
mkdir -p "$D"
cat > "$D/package.json" <<'EOF'
{ "name": "node-addon-require-builtin-android-arm64", "version": "0.1.6-termux-shim", "main": "index.js", "private": true }
EOF
cat > "$D/index.js" <<'EOF'
'use strict'
module.exports = {
  requireBuiltin: (id) => require(id),
  isAllowedInternalId: () => true,
  getNativeBindingInfo: () => ({ mode: 'unrestricted', product: 'require-builtin', backend: 'napi', abi: 'napi-v9' }),
}
EOF
cat > "$PREFIX/bin/dsh" <<EOF
#!$PREFIX/bin/sh
exec node --expose-internals $HOME/repos/novus-deepseek-harness/apps/cli/lib/bin.js "\$@"
EOF
chmod 755 "$PREFIX/bin/dsh"
dsh --version
echo "shim installed"
