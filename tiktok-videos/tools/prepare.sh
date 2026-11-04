#!/usr/bin/env bash
# Stimme einsetzen (Wortzeiten schon per align_words.py), lib aktualisieren, Sound bauen:
#   tools/prepare.sh <slug>
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; P="$ROOT/videos/$1"
cp -r "$ROOT/shared/lib/." "$P/lib/"
python3 "$ROOT/tools/add_voice.py" "$P" "$P/assets/take.mp3" --copy-only --tail 2.6 > "$P/assets/.voice.log"; head -1 "$P/assets/.voice.log"
python3 "$ROOT/tools/build_sfx.py" "$P"
