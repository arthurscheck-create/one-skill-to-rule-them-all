#!/usr/bin/env python3
"""Legt eine Sprecherspur (voice.wav/mp3) unter ein Projekt und synchronisiert timing.js darauf.

Vorgehen (ohne Spracherkennung, funktioniert offline):
  1. Sprechpausen mit ffmpeg silencedetect finden.
  2. Erwartete Satzgrenzen aus der Zeichenanzahl der Sätze schätzen.
  3. Jede Grenze auf die nächstgelegene echte Pause einrasten (Toleranz ±0,8 s).
  4. t0/t1 aller Zeilen neu schreiben, duration = Stimmenende + Nachlauf (mind. --min-duration).
  5. <audio id="voice"> in index.html eintragen (falls nicht vorhanden).
Danach: python3 tools/build_sfx.py <projekt>  und rendern.

Aufruf: python3 tools/add_voice.py videos/<projekt> pfad/zur/stimme.wav [--min-duration 50] [--fit 50] [--tail 2.2]
"""
import argparse, json, re, shutil, subprocess
from pathlib import Path


def silences(path, noise="-38dB", d=0.14):
    r = subprocess.run(["ffmpeg", "-i", str(path), "-af", f"silencedetect=n={noise}:d={d}", "-f", "null", "-"],
                       capture_output=True, text=True)
    st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    return list(zip(st, en + [None] * (len(st) - len(en))))


def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project"); ap.add_argument("voice")
    ap.add_argument("--min-duration", type=float, default=0.0)
    ap.add_argument("--tail", type=float, default=2.2)
    ap.add_argument("--fit", type=float, default=0.0, help="Zieldauer in s: Stimme bei Bedarf bis max. 1.15x beschleunigen")
    a = ap.parse_args()
    proj = Path(a.project)
    src = (proj / "timing.js").read_text(encoding="utf-8")
    m = re.search(r"window\.TIMING\s*=\s*(\{.*\})\s*;?\s*$", src, re.S)
    T = json.loads(m.group(1))

    dst = proj / "assets" / ("voice" + Path(a.voice).suffix.lower())
    dst.parent.mkdir(exist_ok=True)
    if Path(a.voice).resolve() != dst.resolve():
        shutil.copy(a.voice, dst)
    total = duration(dst)
    if a.fit and total + a.tail > a.fit:
        tempo = min(1.15, (total + a.tail) / a.fit)
        tmp = dst.with_name("voice_tmp" + dst.suffix)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(dst), "-af", f"atempo={tempo:.4f}", str(tmp)], check=True)
        tmp.replace(dst)
        print(f"Stimme um {tempo:.3f}x beschleunigt, um in {a.fit}s zu passen")
        total = duration(dst)
    sil = silences(dst)
    # Sprechbereich: vom Ende der Anfangsstille bis zum Beginn der Endstille
    s_on = sil[0][1] if sil and sil[0][0] < 0.05 and sil[0][1] else 0.0
    s_off = sil[-1][0] if sil and (sil[-1][1] is None or sil[-1][1] >= total - 0.05) else total
    pauses = [(s, e) for s, e in sil if e and s > s_on + 0.05 and s < s_off - 0.05]

    lines = T["lines"]
    text = lambda l: re.sub(r"[*^~]", "", " ".join(l["chunks"]))
    w = [len(text(l)) + 6 for l in lines]
    tot = sum(w); acc = 0; bounds = []
    for i in range(len(lines) - 1):
        acc += w[i]
        exp = s_on + (s_off - s_on) * acc / tot
        best = None
        for (ps, pe) in pauses:
            mid = (ps + pe) / 2
            if abs(mid - exp) <= 0.8 and (best is None or abs(mid - exp) < abs((best[0] + best[1]) / 2 - exp)):
                best = (ps, pe)
        if best:
            pauses.remove(best)
            bounds.append(best)
        else:
            bounds.append((exp, exp))
    # Monotonie sicherstellen
    starts = [s_on] + [b[1] for b in bounds]
    ends = [b[0] for b in bounds] + [s_off]
    for i, l in enumerate(lines):
        l["t0"] = round(max(starts[i], ends[i - 1] if i else 0), 3)
        l["t1"] = round(max(ends[i], l["t0"] + 0.3), 3)
    T["duration"] = round(max(a.min_duration, s_off + a.tail), 2)
    T["voice"] = "assets/" + dst.name
    (proj / "timing.js").write_text("window.TIMING = " + json.dumps(T, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")

    html = (proj / "index.html").read_text(encoding="utf-8")
    dur = T["duration"]
    html = re.sub(r'(data-composition-id="main"[^>]*data-duration=")[0-9.]+', lambda mm: mm.group(1) + str(dur), html)
    html = re.sub(r'(<audio id="sfx"[^>]*data-duration=")[0-9.]+', lambda mm: mm.group(1) + str(dur), html)
    tag = f'<audio id="voice" src="assets/{dst.name}" data-start="0" data-duration="{round(total, 2)}" data-volume="1"></audio>'
    if 'id="voice"' in html:
        html = re.sub(r'<audio id="voice"[^>]*></audio>', tag, html)
    else:
        html = html.replace('<audio id="sfx"', tag + '\n    <audio id="sfx"', 1)
    (proj / "index.html").write_text(html, encoding="utf-8")

    print(f"Stimme: {total:.2f}s, Sprache {s_on:.2f}–{s_off:.2f}s, Video jetzt {dur}s")
    for l in lines:
        print(f"  {l['id']:<10} {l['t0']:6.2f} – {l['t1']:6.2f}  {text(l)[:50]}")


if __name__ == "__main__":
    main()
