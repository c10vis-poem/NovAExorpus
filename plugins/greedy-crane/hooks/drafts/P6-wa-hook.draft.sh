#!/bin/sh
# wa-hook.sh ID CMD [ARGS...]  (DRAFT) -- the single door every wiki-admin hook goes through.
# Off switches, checked on EVERY call so they work mid-session without a restart:
#   1. env WIKI_ADMIN_HOOKS=off          (whole set, for a launch)
#   2. file ~/.wiki-admin/hooks.off      (whole set:  touch to stop, rm to resume)
#   3. file ~/.wiki-admin/hooks.d/ID.off (one hook)
# Fail-open: if anything here is wrong, exit 0 and let the tool call proceed.
id=$1; shift
[ "$WIKI_ADMIN_HOOKS" = "off" ] && exit 0
h=${WIKI_ADMIN_HOME:-$HOME/.wiki-admin}
[ -e "$h/hooks.off" ] && exit 0
[ -e "$h/hooks.d/$id.off" ] && exit 0
"$@" || exit 0
