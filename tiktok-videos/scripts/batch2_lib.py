# Skripte für Serie 2 (Videos 08–10). Erzeugt timing.js + script.txt je Projekt.
import json, re
from pathlib import Path
ROOT = Path("/home/user/tiktok-videos")

def build(slug, title, L, scenes, hud, interact, sfx):
    t = 0.3; lines = []
    for id, ch, nc in L:
        w = len(" ".join(ch).split()); d = w / 2.3 + 0.2
        e = {"id": id, "t0": round(t, 2), "t1": round(t + d, 2), "chunks": ch}
        if nc: e["noCap"] = True
        lines.append(e); t += d + 0.4
    T = {"title": title, "duration": round(t + 2, 2), "voice": None, "lines": lines,
         "scenes": [{"id": s, "at": a, "off": o} for s, a, o in scenes], "hud": hud, "interact": interact, "sfx": sfx}
    p = ROOT / "videos" / slug; p.mkdir(parents=True, exist_ok=True)
    (p / "timing.js").write_text("window.TIMING = " + json.dumps(T, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    text = " ".join(re.sub(r"[*^~]", "", " ".join(l["chunks"])) for l in lines)
    (p / "script.txt").write_text(text + "\n", encoding="utf-8")
    print(f"{slug}: {len(text.split())} Wörter, ~{T['duration']}s")

F = lambda at, off=0.0: {"at": at, "off": off}

