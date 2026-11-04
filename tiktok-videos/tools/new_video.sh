#!/usr/bin/env bash
# Neues Video-Projekt anlegen:  tools/new_video.sh 02-mein-thema "Titel des Videos"
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SLUG="$1"; TITLE="${2:-$1}"
P="$ROOT/videos/$SLUG"
[ -e "$P" ] && { echo "Existiert schon: $P"; exit 1; }
mkdir -p "$P/assets"
cp -r "$ROOT/shared/lib" "$P/lib"
cp "$ROOT/templates/index.template.html" "$P/index.html"
cp "$ROOT/templates/timing.template.js" "$P/timing.js"
sed -i "s|__TITLE__|$TITLE|g" "$P/index.html" "$P/timing.js"
cat > "$P/package.json" <<JSON
{ "name": "$SLUG", "private": true, "type": "module",
  "scripts": { "check": "npx --yes hyperframes@0.9.11 check", "render": "npx --yes hyperframes@0.9.11 render" } }
JSON
echo "{\"id\":\"$SLUG\",\"name\":\"$TITLE\"}" > "$P/meta.json"
echo '{"paths":{"blocks":"compositions","components":"compositions/components","assets":"assets"},"media":{"autoProxy":true}}' > "$P/hyperframes.json"
echo "Angelegt: $P"
