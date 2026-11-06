#!/usr/bin/env python3
"""Neuvertonung eines fertigen Videos mit neuer Stimme (gleiches Skript):
  python3 tools/revoice.py <slug> <ziel-wörter-pro-s> [--key N]
Erwartet assets/<src>/take.mp3 + take_words.json (Scribe), Standard --src helmut.
Ersetzt take/take_orig, wählt das Tempo so, dass die alte Sprechgeschwindigkeit erreicht wird,
richtet die Wortzeiten aus, setzt den Hook-Boom (--key) neu und baut Stimme + Sound."""
import json, re, shutil, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
slug, target = sys.argv[1], float(sys.argv[2])
key = int(sys.argv[sys.argv.index("--key") + 1]) if "--key" in sys.argv else None
src = sys.argv[sys.argv.index("--src") + 1] if "--src" in sys.argv else "helmut"
P = ROOT / "videos" / slug; A = P / "assets"; N = A / src
for f in ("take_orig.mp3", "take_words_orig.json"):
    (A / f).unlink(missing_ok=True)
shutil.copy(N / "take.mp3", A / "take.mp3")
# v3: Scribe übernimmt die [Tags] als "Wörter" – herausfiltern (auch mehrteilige wie "[trembling voice]")
d = json.loads((N / "take_words.json").read_text(encoding="utf-8")); ws = d["words"] if isinstance(d, dict) else d
clean, inside = [], False
for w in ws:
    t = w.get("text", "").strip()
    if w.get("type", "word") == "word" and (inside or t.startswith("[")):
        inside = not t.endswith("]"); continue
    clean.append(w)
dropped = len(ws) - len(clean)
(A / "take_words.json").write_text(json.dumps({"words": clean}, ensure_ascii=False), encoding="utf-8")
if dropped: print(f"{dropped} Tag-Tokens entfernt")
run = lambda *c: subprocess.run([str(x) for x in c], check=True, capture_output=True, text=True).stdout
out = run("python3", ROOT / "tools/speedup.py", P, "--tempo", 1.0, "--maxpause", 0.3, "--qpause", 0.5)
r1 = float(re.search(r"-> ([0-9.]+) Wörter/s", out).group(1))
tempo = round(max(1.0, min(1.55, target / r1)), 3)
print(run("python3", ROOT / "tools/speedup.py", P, "--tempo", tempo, "--maxpause", 0.3, "--qpause", 0.5).strip(), f"[tempo {tempo}]")
al = run("python3", ROOT / "tools/align_words.py", P, A / "take_words.json", "--tempo", 1)
print([l for l in al.splitlines() if "Abweich" in l][0])
if key is not None:
    (A / ".hookkey.json").write_text(json.dumps({"key": key}))
    print(run("python3", ROOT / "tools/replace_hook.py", "--finish", P, A / ".hookkey.json").strip())
print(run("bash", ROOT / "tools/prepare.sh", slug).strip())
