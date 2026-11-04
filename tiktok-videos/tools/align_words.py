#!/usr/bin/env python3
"""Setzt Untertitel WORTGENAU aus einer Transkription mit Wort-Zeitstempeln
(z. B. ElevenLabs Scribe words.json: [{"text","type","start","end"}, ...]).

Vorher add_voice.py ausführen (kopiert/beschleunigt die Stimme und trägt <audio> ein).
Wurde die Stimme dabei beschleunigt, rechnet --source <original.mp3> den Faktor automatisch heraus.

Aufruf: python3 tools/align_words.py videos/<projekt> words.json [--source original.mp3]
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

norm = lambda s: re.sub(r"[^\wäöüß]", "", s.lower())


def duration(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return float(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project"); ap.add_argument("words")
    ap.add_argument("--source", help="Original-Audio vor der Beschleunigung (für den Tempo-Faktor)")
    ap.add_argument("--tempo", type=float, default=0.0)
    a = ap.parse_args()
    proj = Path(a.project)
    src = (proj / "timing.js").read_text(encoding="utf-8")
    T = json.loads(re.search(r"window\.TIMING\s*=\s*(\{.*\})\s*;?\s*$", src, re.S).group(1))
    W = json.loads(Path(a.words).read_text(encoding="utf-8"))
    if isinstance(W, dict):
        W = W.get("words", W)
    W = [w for w in W if w.get("type", "word") == "word"]

    tempo = a.tempo or 1.0
    if not a.tempo and a.source and T.get("voice"):
        tempo = duration(a.source) / duration(proj / T["voice"])
    print(f"Tempo-Faktor: {tempo:.4f}")

    i, bad = 0, 0
    for l in T["lines"]:
        starts = []
        for c in l["chunks"]:
            toks = [t for t in re.sub(r"[*^~]", "", c).split() if norm(t)]
            if i >= len(W):
                sys.exit(f"Transkription zu kurz bei Zeile {l['id']}")
            starts.append(round(W[i]["start"] / tempo, 3))
            for t in toks:
                if norm(t) != norm(W[i]["text"]):
                    bad += 1
                    print(f"  Abweichung: Skript '{t}' ≠ gesprochen '{W[i]['text']}' ({l['id']})")
                last = W[i]; i += 1
        l["chunkStarts"] = starts
        l["t0"] = starts[0]
        l["t1"] = round(last["end"] / tempo, 3)
    if i != len(W):
        print(f"Warnung: {len(W) - i} Wörter der Transkription übrig.")
    (proj / "timing.js").write_text("window.TIMING = " + json.dumps(T, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    print(f"{i} Wörter zugeordnet, {bad} Abweichungen.")
    for l in T["lines"]:
        print(f"  {l['id']:<10} {l['t0']:6.2f} – {l['t1']:6.2f}")


if __name__ == "__main__":
    main()
