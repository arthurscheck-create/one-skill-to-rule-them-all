#!/usr/bin/env python3
"""Vertont ein Projekt mit ElevenLabs und synchronisiert Untertitel WORTGENAU.

Liest den Sprechertext aus timing.js (alle lines, Markup entfernt), ruft
  POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps
auf, speichert assets/voice.mp3 + assets/voice_alignment.json und schreibt
t0/t1 jedes Satzes sowie chunkStarts (Startzeit jedes Untertitel-Chunks) in timing.js.

Voraussetzung: Umgebungsvariable ELEVENLABS_API_KEY, Netz-Freigabe für api.elevenlabs.io.

Aufruf:
  python3 tools/elevenlabs_tts.py videos/<projekt> [--voice rDmv3mOhK6TnhYWckFaD]
          [--model eleven_multilingual_v2] [--min-duration 50] [--fit 50] [--tail 2.2]
  python3 tools/elevenlabs_tts.py videos/<projekt> --reuse   # vorhandene Audio+Alignment neu anwenden (kostet nichts)
"""
import argparse, base64, json, os, re, subprocess, sys, urllib.request
from pathlib import Path

DEFAULT_VOICE = "rDmv3mOhK6TnhYWckFaD"  # Felix Serenitas – German
DEFAULT_MODEL = "eleven_multilingual_v2"
clean = lambda s: re.sub(r"[*^~]", "", s)


def load_timing(proj):
    src = (proj / "timing.js").read_text(encoding="utf-8")
    return json.loads(re.search(r"window\.TIMING\s*=\s*(\{.*\})\s*;?\s*$", src, re.S).group(1))


def save_timing(proj, T):
    (proj / "timing.js").write_text("window.TIMING = " + json.dumps(T, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")


def script_and_spans(T):
    """Gesamttext + Zeichenbereiche je Zeile und je Chunk."""
    text, lines = "", []
    for l in T["lines"]:
        if text:
            text += " "
        chunks = []
        for i, c in enumerate(l["chunks"]):
            if i:
                text += " "
            a = len(text); text += clean(c); chunks.append((a, len(text)))
        lines.append((chunks[0][0], chunks[-1][1], chunks))
    return text, lines


def tts(text, voice, model, key):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128"
    body = json.dumps({
        "text": text, "model_id": model,
        "voice_settings": {"stability": 0.45, "similarity_boost": 0.8, "style": 0.3, "use_speaker_boost": True, "speed": 1.0},
    }).encode()
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"ElevenLabs-Fehler {e.code}: {e.read().decode(errors='replace')[:500]}")


def duration(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return float(r.stdout.strip())


def patch_html(proj, dur, voice_name, voice_dur):
    p = proj / "index.html"; html = p.read_text(encoding="utf-8")
    html = re.sub(r'(data-composition-id="main"[^>]*data-duration=")[0-9.]+', lambda m: m.group(1) + str(dur), html)
    html = re.sub(r'(<audio id="sfx"[^>]*data-duration=")[0-9.]+', lambda m: m.group(1) + str(dur), html)
    tag = f'<audio id="voice" src="assets/{voice_name}" data-start="0" data-duration="{round(voice_dur, 2)}" data-volume="1"></audio>'
    if 'id="voice"' in html:
        html = re.sub(r'<audio id="voice"[^>]*></audio>', tag, html)
    else:
        html = html.replace('<audio id="sfx"', tag + '\n    <audio id="sfx"', 1)
    p.write_text(html, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--voice", default=os.environ.get("ELEVENLABS_VOICE_ID", DEFAULT_VOICE))
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--min-duration", type=float, default=0.0)
    ap.add_argument("--fit", type=float, default=0.0, help="Zieldauer: Stimme bei Bedarf bis 1.15x beschleunigen")
    ap.add_argument("--tail", type=float, default=2.2)
    ap.add_argument("--reuse", action="store_true")
    a = ap.parse_args()
    proj = Path(a.project); assets = proj / "assets"; assets.mkdir(exist_ok=True)
    T = load_timing(proj)
    text, spans = script_and_spans(T)
    mp3, alj = assets / "voice.mp3", assets / "voice_alignment.json"

    if not a.reuse:
        key = os.environ.get("ELEVENLABS_API_KEY")
        if not key:
            sys.exit("ELEVENLABS_API_KEY fehlt (in den Umgebungs-Einstellungen hinterlegen, neue Session starten).")
        print(f"Vertone {len(text.split())} Wörter mit Stimme {a.voice} ({a.model}) …")
        res = tts(text, a.voice, a.model, key)
        mp3.write_bytes(base64.b64decode(res["audio_base64"]))
        al = res.get("alignment") or res.get("normalized_alignment")
        alj.write_text(json.dumps({"text": text, "alignment": al}, ensure_ascii=False), encoding="utf-8")
    data = json.loads(alj.read_text(encoding="utf-8"))
    al = data["alignment"]
    chars, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    if "".join(chars) != text:
        print("Warnung: Alignment-Text weicht vom Skript ab – ordne über Position zu.")

    voice_name = mp3.name
    raw_dur = duration(mp3)
    tempo = 1.0
    speech_end = max(en) if en else raw_dur
    if a.fit and speech_end + a.tail > a.fit:
        tempo = min(1.15, (speech_end + a.tail) / a.fit)
        out = assets / "voice_fit.mp3"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp3), "-af", f"atempo={tempo:.4f}", str(out)], check=True)
        voice_name = out.name
        print(f"Stimme um {tempo:.3f}x beschleunigt, um in {a.fit}s zu passen")
    n = len(chars)
    ts = lambda i: st[min(i, n - 1)] / tempo
    te = lambda i: en[min(max(i, 0), n - 1)] / tempo

    for l, (a0, a1, chunks) in zip(T["lines"], spans):
        l["t0"] = round(ts(a0), 3)
        l["t1"] = round(te(a1 - 1), 3)
        l["chunkStarts"] = [round(ts(c0), 3) for c0, _ in chunks]
    end_speech = T["lines"][-1]["t1"]
    T["duration"] = round(max(a.min_duration, end_speech + a.tail), 2)
    T["voice"] = "assets/" + voice_name
    save_timing(proj, T)
    patch_html(proj, T["duration"], voice_name, duration(assets / voice_name))
    print(f"Fertig: Sprache endet bei {end_speech:.2f}s, Video {T['duration']}s")
    for l in T["lines"]:
        print(f"  {l['id']:<10} {l['t0']:6.2f} – {l['t1']:6.2f}  {clean(' '.join(l['chunks']))[:48]}")


if __name__ == "__main__":
    main()
