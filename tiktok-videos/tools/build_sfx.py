#!/usr/bin/env python3
"""Erzeugt assets/sfx.wav (Sound-Design) komplett aus Code, gesteuert über timing.js.

Ebenen:  Drone (dunkler Teppich) · Ticken (ab HUD) · Whoosh bei jedem Schnitt
         · Pop pro Untertitel-Chunk · Event-Sounds aus TIMING.sfx
Aufruf:  python3 tools/build_sfx.py videos/<projekt>
"""
import json, re, sys, wave
from pathlib import Path
import numpy as np

SR = 44100


def load_timing(project: Path):
    src = (project / "timing.js").read_text(encoding="utf-8")
    m = re.search(r"window\.TIMING\s*=\s*(\{.*\})\s*;?\s*$", src, re.S)
    return json.loads(m.group(1))


def main(project: Path):
    T = load_timing(project)
    dur = float(T["duration"])
    N = int(SR * dur)
    out = np.zeros(N, dtype=np.float64)
    rs = np.random.default_rng(1234)
    lines = {l["id"]: l for l in T["lines"]}
    at = lambda ref: lines[ref["at"]]["t0"] + ref.get("off", 0.0)

    def add(sig, t, gain=1.0):
        i = int(t * SR)
        if i >= N or i + len(sig) <= 0:
            return
        if i < 0:
            sig, i = sig[-i:], 0
        n = min(len(sig), N - i)
        out[i:i + n] += sig[:n] * gain

    def env(n, a=0.005, r=0.1):
        e = np.ones(n)
        na, nr = max(1, int(a * SR)), max(1, int(r * SR))
        e[:na] = np.linspace(0, 1, na)
        e[-nr:] *= np.linspace(1, 0, nr)
        return e

    def lowpass(x, alpha):
        y = np.empty_like(x); acc = 0.0
        for i in range(len(x)):
            acc += alpha * (x[i] - acc); y[i] = acc
        return y

    t_all = np.arange(N) / SR
    # --- Drone: tiefe Sinus-Schichten mit langsamer Modulation
    drone = (0.5 * np.sin(2 * np.pi * 55 * t_all) + 0.3 * np.sin(2 * np.pi * 82.4 * t_all + 1.3)
             + 0.15 * np.sin(2 * np.pi * 110.3 * t_all)) * (0.65 + 0.35 * np.sin(2 * np.pi * 0.11 * t_all))
    noise = lowpass(rs.standard_normal(N) * 0.4, 0.02)
    out += (drone * 0.05 + noise * 0.05) * np.clip(t_all / 1.5, 0, 1)

    # --- Szenen-Fenster
    scenes = sorted(max(0.0, at(s)) for s in T["scenes"])

    def whoosh(d=0.38):
        n = int(d * SR); x = rs.standard_normal(n)
        k = np.linspace(0.02, 0.35, n)  # öffnender Filter
        y = np.empty(n); acc = 0.0
        for i in range(n):
            acc += k[i] * (x[i] - acc); y[i] = acc
        return y * np.sin(np.linspace(0, np.pi, n)) ** 2 * 0.9

    for t in scenes[1:]:
        add(whoosh(), t - 0.18, 0.55)
        add(sine_hit(70, 0.25), t, 0.35)

    # --- Ticken ab HUD bis Ende HUD
    hud = T.get("hud")
    if hud:
        t0, t1 = at(hud["show"]), at(hud["hide"])
        tick = click(2600, 0.025)
        t = t0
        while t < t1:
            add(tick, t, 0.16)
            t += 1.0

    # --- Pop pro Untertitel-Chunk
    for l in T["lines"]:
        if l.get("noCap"):
            continue
        lens = [len(re.sub(r"[*^~]", "", c)) + 5 for c in l["chunks"]]
        tot = sum(lens); t = l["t0"]
        starts = l.get("chunkStarts")
        for i, L in enumerate(lens):
            if starts and i < len(starts):
                t = starts[i]
            add(click(1400, 0.03), t, 0.10)
            t += (l["t1"] - l["t0"]) * L / tot

    # --- Events
    for ev in T.get("sfx", []):
        t = at(ev); typ = ev["type"]; d = ev.get("dur", 1.0)
        if typ == "alarm":
            beep = np.sign(np.sin(2 * np.pi * 1760 * np.arange(int(0.09 * SR)) / SR)) * env(int(0.09 * SR), 0.002, 0.02)
            k = 0.0
            while k < d:
                for j in range(3):
                    add(beep, t + k + j * 0.13, 0.12)
                k += 0.75
        elif typ == "riser":
            n = int(1.2 * SR); tt = np.arange(n) / SR
            f = 200 + 900 * (tt / 1.2) ** 2
            add(np.sin(2 * np.pi * np.cumsum(f) / SR) * (tt / 1.2) ** 2 * 0.5 + rs.standard_normal(n) * 0.08 * (tt / 1.2) ** 3, t, 0.5)
        elif typ == "boom":
            n = int(2.2 * SR); tt = np.arange(n) / SR
            f = 90 * np.exp(-tt * 2.2) + 32
            sig = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 1.6)
            sig += lowpass(rs.standard_normal(n), 0.05) * np.exp(-tt * 2.5) * 1.6
            add(sig, t, 0.9)
        elif typ == "flicker":
            k = 0.0
            while k < d:
                n = int(0.05 * SR)
                add(np.sign(np.sin(2 * np.pi * 120 * np.arange(n) / SR)) * env(n, 0.001, 0.01) * 0.6 + rs.standard_normal(n) * 0.3, t + k, 0.22)
                k += 0.11
        elif typ == "drip":
            n = int(0.18 * SR); tt = np.arange(n) / SR
            f = 900 + 1600 * tt / 0.18
            add(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 28), t, 0.5)
        elif typ == "glitch":
            for j in range(6):
                n = int(0.04 * SR)
                add(np.sign(rs.standard_normal(n)) * 0.4, t + j * 0.07, 0.12)
        elif typ == "rats":
            k = 0.0
            while k < d:
                n = int(0.07 * SR); tt = np.arange(n) / SR
                add(np.sin(2 * np.pi * (3200 + 1500 * np.sin(tt * 90)) * tt) * env(n, 0.003, 0.03), t + k, 0.07)
                k += 0.16
        elif typ == "rise":
            n = int(d * SR); tt = np.arange(n) / SR
            chord = sum(np.sin(2 * np.pi * f * tt) for f in (261.6, 329.6, 392.0, 523.3)) / 4
            add(chord * np.clip(tt / d, 0, 1) ** 1.5 * env(n, 0.05, 0.6), t, 0.22)
        elif typ == "heartbeat":
            k = 0.0
            while k < d:
                for j, g in ((0.0, 1.0), (0.22, 0.7)):
                    n = int(0.18 * SR); tt = np.arange(n) / SR
                    add(np.sin(2 * np.pi * (55 + 40 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 18) * g, t + k + j, 0.8)
                k += 0.85
        elif typ == "ding":
            n = int(1.4 * SR); tt = np.arange(n) / SR
            add((np.sin(2 * np.pi * 1318 * tt) + 0.5 * np.sin(2 * np.pi * 1975 * tt)) * np.exp(-tt * 3.5), t, 0.3)

    # --- Interaktions-Einblendungen: doppelter "Pop"
    for it in T.get("interact", []):
        t = at(it)
        for j, f in enumerate((880, 1320)):
            n = int(0.12 * SR); tt = np.arange(n) / SR
            add(np.sin(2 * np.pi * f * tt) * np.exp(-tt * 30), t + j * 0.09, 0.28)

    # Ende: sanft ausblenden
    fade = int(0.6 * SR)
    out[-fade:] *= np.linspace(1, 0, fade)
    peak = np.max(np.abs(out)) or 1.0
    out = out / peak * 0.89
    pcm = (out * 32767).astype(np.int16)
    dst = project / "assets" / "sfx.wav"
    dst.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(dst), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print(f"sfx.wav geschrieben: {dst} ({dur:.1f}s)")


def click(freq, d):
    n = int(d * SR); tt = np.arange(n) / SR
    return np.sin(2 * np.pi * freq * tt) * np.exp(-tt * 180)


def sine_hit(freq, d):
    n = int(d * SR); tt = np.arange(n) / SR
    return np.sin(2 * np.pi * freq * tt) * np.exp(-tt * 14)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
