#!/usr/bin/env bash
# Video für das Szenario Studio vorbereiten (< 15 MB + Vorschaubild):
#   tools/studio_prepare.sh output/<slug>.mp4 <slug>
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; SRC="$1"; SLUG="$2"; OUT="$ROOT/studio/upload"
mkdir -p "$OUT"
ffmpeg -v error -y -i "$SRC" -c:v libx264 -preset slow -crf 23 -maxrate 2600k -bufsize 5200k -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart "$OUT/$SLUG.mp4"
ffmpeg -v error -y -ss 1.6 -i "$SRC" -frames:v 1 -vf scale=540:-1 -q:v 3 "$OUT/$SLUG.jpg"
ls -la "$OUT/$SLUG.mp4" "$OUT/$SLUG.jpg"
