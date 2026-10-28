#!/bin/sh
# Resolve symlink-installed skills to their owning checkout. No duplicate library.
set -eu
HERE=$(CDPATH= cd -P -- "$(dirname -- "$0")" && pwd)
LIB=$(CDPATH= cd -- "$HERE/../../../.." && pwd -P)
[ -f "$LIB/core/render/video.mjs" ] && [ -f "$LIB/plugin/skills/lemo-opuscar/scripts/setup.sh" ] || {
  echo 'Keep this skill in its library checkout; install it with codex/install-skill.sh.' >&2
  exit 1
}
# Managed sparse clones use destructive upstream refreshes; require an ordinary checkout.
[ "$(git -C "$LIB" config --get lemo.managed || true)" != true ] || {
  echo 'Use an ordinary git clone for Codex, not an automatically managed library.' >&2
  exit 1
}
case "${1:-}" in
  '') printf 'LIB=%s\n' "$LIB" ;;
  deps|demo)
    cd "$LIB"
    LEMO_OPUSCAR_HOME="$LIB" sh plugin/skills/lemo-opuscar/scripts/setup.sh "$@"
    ;;
  *) echo 'usage: setup.sh [deps [voice] [music] | demo <slug>]' >&2; exit 2 ;;
esac
