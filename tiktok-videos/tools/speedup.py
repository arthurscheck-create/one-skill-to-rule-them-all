#!/usr/bin/env python3
"""Macht eine fertige Vertonung zügiger – ohne neue Credits:
  1. kürzt Pausen zwischen Wörtern auf max. --maxpause s (nach "?"/"!" max. --qpause s),
  2. beschleunigt danach mit ffmpeg atempo (Tonhöhe bleibt gleich),
  3. rechnet die Scribe-Wortzeiten mit um.
Original bleibt als assets/take_orig.mp3 + assets/take_words_orig.json erhalten (wird bei erneutem Aufruf wieder als Quelle genutzt).

Danach:  python3 tools/align_words.py videos/<slug> videos/<slug>/assets/take_words.json --tempo 1
         tools/prepare.sh <slug>
Aufruf:  python3 tools/speedup.py videos/<slug> [--tempo 1.1] [--maxpause 0.32] [--qpause 0.5]
"""
import argparse, json, shutil, subprocess, tempfile
from pathlib import Path
import numpy as np

SR = 44100


def decode(p):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).copy()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project"); ap.add_argument("--tempo", type=float, default=1.1)
    ap.add_argument("--maxpause", type=float, default=0.32); ap.add_argument("--qpause", type=float, default=0.5)
    a = ap.parse_args()
    A = Path(a.project) / "assets"
    if not (A / "take_orig.mp3").exists():
        shutil.copy(A / "take.mp3", A / "take_orig.mp3"); shutil.copy(A / "take_words.json", A / "take_words_orig.json")
    x = decode(A / "take_orig.mp3")
    d = json.loads((A / "take_words_orig.json").read_text(encoding="utf-8"))
    W = [w for w in (d["words"] if isinstance(d, dict) else d) if w.get("type", "word") == "word"]

    # Zu behaltende Abschnitte [a, b) in Sekunden des Originals
    keep, t = [], 0.0
    for i in range(len(W) - 1):
        e, s = W[i]["end"], W[i + 1]["start"]
        lim = a.qpause if W[i]["text"].rstrip().endswith(("?", "!")) else a.maxpause
        if s - e > lim:
            keep.append((t, e + lim / 2)); t = s - lim / 2
    keep.append((t, min(len(x) / SR, W[-1]["end"] + 0.35)))

    fade = int(0.008 * SR); parts = []
    for s0, s1 in keep:
        seg = x[int(s0 * SR):int(s1 * SR)].copy()
        if len(seg) > 2 * fade:
            seg[:fade] *= np.linspace(0, 1, fade); seg[-fade:] *= np.linspace(1, 0, fade)
        parts.append(seg)
    y = np.concatenate(parts)

    def remap(tt):
        acc = 0.0
        for s0, s1 in keep:
            if tt < s0: return acc / a.tempo
            if tt <= s1: return (acc + tt - s0) / a.tempo
            acc += s1 - s0
        return acc / a.tempo

    with tempfile.NamedTemporaryFile(suffix=".f32") as f:
        f.write(y.astype(np.float32).tobytes()); f.flush()
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", f.name,
                        "-af", f"atempo={a.tempo}", "-c:a", "libmp3lame", "-b:a", "128k", str(A / "take.mp3")], check=True)
    out = [dict(w, start=round(remap(w["start"]), 3), end=round(remap(w["end"]), 3)) for w in W]
    (A / "take_words.json").write_text(json.dumps({"words": out}, ensure_ascii=False), encoding="utf-8")
    o, n = W[-1]["end"], out[-1]["end"]
    print(f"{a.project}: {o:.1f}s -> {n:.1f}s  ({len(W)/o:.2f} -> {len(W)/n:.2f} Wörter/s)")


if __name__ == "__main__":
    main()
