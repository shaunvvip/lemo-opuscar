#!/bin/sh
# Link this checkout into Codex's user skill directory; never replace an existing skill.
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)
DEST=${1:-${CODEX_HOME:-$HOME/.codex}/skills}
mkdir -p "$DEST"
DEST=$(CDPATH= cd -- "$DEST" && pwd -P)
TARGET="$DEST/lemo-opuscar"
SOURCE="$ROOT/.agents/skills/lemo-opuscar"
if [ -L "$TARGET" ] && [ "$(readlink "$TARGET")" = "$SOURCE" ]; then
  printf 'Already linked: %s\n' "$TARGET"
elif [ -e "$TARGET" ] || [ -L "$TARGET" ]; then
  echo "Refusing to replace existing skill: $TARGET" >&2; exit 1
else
  ln -s "$SOURCE" "$TARGET"
  printf 'Linked: %s -> %s\n' "$TARGET" "$SOURCE"
fi
