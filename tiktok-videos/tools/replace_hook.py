#!/usr/bin/env python3
"""Ersetzt den Hook (die ersten beiden Zeilen hook + loop) eines fertigen Videos durch einen neuen 3-Satz-Hook
(hook / kata / loop, Hook-Regeln v2) – ohne das ganze Video neu zu vertonen.

Voraussetzung: assets/hook2.mp3 + assets/hook2_words.json (Scribe) für die neuen Sätze,
assets/take_orig.mp3 + assets/take_words_orig.json (Original-Aufnahme, von speedup.py angelegt).

Aufruf: python3 tools/replace_hook.py videos/<slug> spec.json
  spec.json: {"hook": [...chunks], "kata": [...], "loop": [...], "key": <Chunk-Index in kata für Blitz/Boom>,
              "title": "<HTML Titel>", "sub": "<HTML Unterzeile>"}
Danach: speedup.py → align_words.py --tempo 1 → tools/replace_hook.py --finish videos/<slug> spec.json → prepare.sh
"""
import json, re, shutil, subprocess, sys
from pathlib import Path
import numpy as np

SR = 44100
norm = lambda s: re.sub(r"[^\wäöüß]", "", s.lower())


def dec(p):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).copy()


def load_T(proj):
    s = (proj / "timing.js").read_text(encoding="utf-8")
    return json.loads(re.search(r"window\.TIMING\s*=\s*(\{.*\})\s*;?\s*$", s, re.S).group(1))


def save_T(proj, T):
    (proj / "timing.js").write_text("window.TIMING = " + json.dumps(T, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")


def words_of(chunks):
    return [w for w in re.sub(r"[*^~]", "", " ".join(chunks)).split() if norm(w)]


def prepare(proj, spec):
    A = proj / "assets"
    for a, b in [("take_orig.mp3", "take_orig_v1.mp3"), ("take_words_orig.json", "take_words_orig_v1.json"), ("../timing.js", "timing_v1.js"), ("../index.html", "index_v1.html")]:
        if not (A / b).exists(): shutil.copy(A / a, A / b)
    T = json.loads(re.search(r"window\.TIMING\s*=\s*(\{.*\})\s*;?\s*$", (A / "timing_v1.js").read_text(encoding="utf-8"), re.S).group(1))
    old = T["lines"][:2]; assert old[0]["id"] == "hook" and old[1]["id"] == "loop", [l["id"] for l in old]
    n_old = sum(len(words_of(l["chunks"])) for l in old)
    ow = [w for w in json.loads((A / "take_words_orig_v1.json").read_text())["words"] if w.get("type", "word") == "word"]
    hw = [w for w in json.loads((A / "hook2_words.json").read_text())["words"] if w.get("type", "word") == "word"]
    exp_new = words_of(spec["hook"]) + words_of(spec["kata"]) + words_of(spec["loop"])
    assert [norm(w) for w in exp_new] == [norm(w["text"]) for w in hw], ("Hook-Text passt nicht zur Transkription", exp_new, [w["text"] for w in hw])
    first_next = words_of(T["lines"][2]["chunks"])[0]
    assert norm(ow[n_old]["text"]) == norm(first_next), (ow[n_old]["text"], first_next)
    h, o = dec(A / "hook2.mp3"), dec(A / "take_orig_v1.mp3")
    h = h[: int((hw[-1]["end"] + 0.12) * SR)]
    c = ow[n_old]["start"] - 0.15; L = len(h) / SR; gap = 0.35
    y = np.concatenate([h, np.zeros(int(gap * SR), np.float32), o[int(c * SR):]])
    off = L + gap - c
    W = hw + [dict(w, start=round(w["start"] + off, 3), end=round(w["end"] + off, 3)) for w in ow[n_old:]]
    tmp = A / ".splice.f32"; tmp.write_bytes(y.astype(np.float32).tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", str(tmp), "-c:a", "libmp3lame", "-b:a", "160k", str(A / "take_orig.mp3")], check=True)
    tmp.unlink()
    (A / "take_words_orig.json").write_text(json.dumps({"words": W}, ensure_ascii=False), encoding="utf-8")
    new = [{"id": "hook", "t0": 0, "t1": 1, "chunks": spec["hook"], "noCap": True},
           {"id": "kata", "t0": 1, "t1": 2, "chunks": spec["kata"]},
           {"id": "loop", "t0": 2, "t1": 3, "chunks": spec["loop"]}]
    T["lines"] = new + T["lines"][2:]
    T["sfx"] = [e for e in T["sfx"] if not (e.get("at") == "kata")]
    save_T(proj, T)
    # index.html: Titel, Ausblenden vor erstem Untertitel, Hook-Effekt
    p = proj / "index.html"; s = (A / "index_v1.html").read_text(encoding="utf-8")
    s = re.sub(r'<div class="title main">.*?</div>', f'<div class="title main">{spec["title"]}</div>', s, count=1, flags=re.S)
    s = re.sub(r'<div class="title sub">.*?</div>', f'<div class="title sub">{spec["sub"]}</div>', s, count=1, flags=re.S)
    s = s.replace('{ autoAlpha: 0, duration: .15 }, at("loop", -0.15));', '{ autoAlpha: 0, duration: .15 }, at("kata", -0.15));')
    s = s.replace('cs("hook", 0, 3.2));', '0.5);')
    a = "E.buildScenes(tl); E.buildCaptions(tl); E.buildHud(tl); E.buildInteract(tl);"
    assert a in s
    s = s.replace(a, a + f'\n    E.hookFx(tl, cs("kata", {spec["key"]}));', 1)
    p.write_text(s, encoding="utf-8")
    print(f"{proj.name}: Hook {L:.2f}s eingesetzt, Schnitt bei {c:.2f}s, {len(W)} Wörter")


def finish(proj, spec):
    """Nach align_words: Boom genau auf das Schlüsselwort des zweiten Satzes legen."""
    T = load_T(proj)
    k = next(l for l in T["lines"] if l["id"] == "kata")
    off = round(k["chunkStarts"][spec["key"]] - k["t0"], 3)
    T["sfx"] = [e for e in T["sfx"] if e.get("at") != "kata"] + [{"type": "boom", "at": "kata", "off": off}]
    save_T(proj, T)
    print(f"{proj.name}: Boom bei kata+{off}s")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--finish"]
    proj, spec = Path(args[0]), json.loads(Path(args[1]).read_text(encoding="utf-8"))
    (finish if "--finish" in sys.argv else prepare)(proj, spec)
