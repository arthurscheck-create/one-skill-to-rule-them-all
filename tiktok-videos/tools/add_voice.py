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
import argparse, json, re, shutil, subprocess, sys
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
    clean = lambda s: re.sub(r"[*^~]", "", s)
    text = lambda l: clean(" ".join(l["chunks"]))

    # Sprechsegmente zwischen den Pausen
    segs, cur = [], s_on
    for ps, pe in pauses:
        if ps - cur > 0.05:
            segs.append((cur, ps))
        cur = pe
    if s_off - cur > 0.05:
        segs.append((cur, s_off))

    # Segmente per dynamischer Programmierung auf Sätze verteilen:
    # Sprechdauer jedes Satzes soll möglichst proportional zu seiner Zeichenzahl sein.
    chars = [len(re.sub(r"[^\wäöüÄÖÜß]", "", text(l))) or 1 for l in lines]
    n, m = len(segs), len(lines)
    if n < m:
        sys.exit(f"Nur {n} Sprechsegmente für {m} Sätze gefunden – Pausenschwelle anpassen.")
    k = sum(b - a for a, b in segs) / sum(chars)
    pre = [0.0]
    for a_, b_ in segs:
        pre.append(pre[-1] + (b_ - a_))
    INF = float("inf")
    cost = [[INF] * (n + 1) for _ in range(m + 1)]
    back = [[0] * (n + 1) for _ in range(m + 1)]
    cost[0][0] = 0.0
    for i in range(1, m + 1):
        e = k * chars[i - 1]
        for j in range(i, n - (m - i) + 1):
            for s in range(i - 1, j):
                if cost[i - 1][s] == INF:
                    continue
                d = pre[j] - pre[s]
                c = cost[i - 1][s] + ((d - e) / (e + 0.25)) ** 2
                if c < cost[i][j]:
                    cost[i][j], back[i][j] = c, s
    groups, j = [], n
    for i in range(m, 0, -1):
        s = back[i][j]; groups.append((s, j)); j = s
    groups.reverse()

    for l, (s, j) in zip(lines, groups):
        lsegs = segs[s:j]
        l["t0"] = round(lsegs[0][0], 3)
        l["t1"] = round(lsegs[-1][1], 3)
        # Chunk-Starts: Zeichenposition -> Zeit über die reine Sprechzeit des Satzes
        full = text(l); L = len(full) or 1
        speech = sum(b - a for a, b in lsegs)
        def t_at(frac):
            rest = frac * speech
            for a_, b_ in lsegs:
                if rest <= (b_ - a_):
                    return a_ + rest
                rest -= (b_ - a_)
            return lsegs[-1][1]
        starts, pos = [], 0
        for i, c in enumerate(l["chunks"]):
            t = t_at(pos / L)
            near = min((a_ for a_, _ in lsegs), key=lambda a_: abs(a_ - t))
            if abs(near - t) < 0.3:
                t = near  # an echte Sprechpause (Komma/Punkt) einrasten
            starts.append(round(t, 3))
            pos += len(clean(c)) + 1
        l["chunkStarts"] = starts
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
