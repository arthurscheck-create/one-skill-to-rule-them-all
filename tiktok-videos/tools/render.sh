#!/usr/bin/env bash
# Video bauen:  tools/render.sh videos/<projekt> [ausgabe.mp4]
# Aktualisiert lib/ aus shared/, erzeugt Sound-Design, prüft und rendert nach output/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
P="$(cd "$1" && pwd)"; SLUG="$(basename "$P")"
OUT="${2:-$ROOT/output/$SLUG.mp4}"
mkdir -p "$(dirname "$OUT")"
cp -r "$ROOT/shared/lib/." "$P/lib/"
python3 -I "$ROOT/tools/build_sfx.py" "$P"
cd "$P"
npx --yes hyperframes@0.9.11 lint . | grep -v -i telemetry || true
npx --yes hyperframes@0.9.11 render -o "$OUT" -w 4 2>&1 | grep -E "Render complete|MB ·|rror" || true
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT" | xargs -I{} echo "Fertig: $OUT ({}s)"
