# Erzeugt index.html für Serie-3-Videos aus einer kompakten Beschreibung.
import json, re
from pathlib import Path
ROOT = Path("/home/user/tiktok-videos")
HEAD = """<!doctype html>
<html lang="de" data-resolution="portrait">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=1080, height=1920" />
  <title>{title}</title>
  <link rel="stylesheet" href="lib/style.css" />
  <script src="lib/gsap.min.js"></script>
  <script src="timing.js"></script>
  <script src="lib/engine.js"></script>
  <style>{css}</style>
</head>
<body>
  <div id="root" data-composition-id="main" data-start="0" data-duration="50" data-width="1080" data-height="1920">
"""
SCENE = """    <section class="scene" id="{id}" data-drift="{drift}"><div class="cam"><div class="drift">
      <svg class="art" viewBox="0 0 1080 1920">{svg}</svg>{extra}
    </div></div></section>
"""
TAIL = """    <div id="hud"><div class="hud-panel"><div class="hud-label"></div><div class="hud-row"><span class="hud-num">000</span><span class="hud-unit"></span></div><div class="hud-sub"></div><div class="hud-delta"></div></div><div class="chip"><span class="chip-label"></span><span class="chip-val"></span></div></div>
    <div id="captions"></div>
    <svg id="grain" width="1080" height="1920"><filter id="f-grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/></filter><rect width="1080" height="1920" filter="url(#f-grain)"/></svg>
    <div id="vignette"></div><div id="flash"></div>
    <audio id="voice" src="assets/voice.mp3" data-start="0" data-duration="48" data-volume="1"></audio>
    <audio id="sfx" src="assets/sfx.wav" data-start="0" data-duration="50" data-volume="0.9"></audio>
  </div>
  <script src="lib/cast.js"></script>
  <script src="lib/kit.js"></script>
  <script>
  (function () {{
    const E = window.Engine, at = E.at, end = E.end, cs = E.cs, svg = E.svg, D = E.T.duration;
    const $ = (s) => document.querySelector(s);
    const tl = gsap.timeline({{ paused: true }});
    const K = E.kit(tl), INK = K.INK, txt = K.txt, otxt = K.otxt, badge = K.badge, pop = K.pop;
{js}
    E.stars($("#{ec}-stars"), 60, 171);
    E.buildEndcard(tl, "{ec}", at("frage", -0.05), at("komm", -0.1));
    E.buildScenes(tl); E.buildCaptions(tl); E.buildHud(tl); E.buildInteract(tl);
    E.hookOpen(tl);
    {hookfx}
{post}
    tl.set({{}}, {{}}, D);
    window.__timelines = window.__timelines || {{}}; window.__timelines["main"] = tl; tl.seek(0);
  }})();
  </script>
</body>
</html>
"""
def page(slug, scenes, title_html, sub_html, q_html, opts, cta2, js, dramatic, post="", css="", flash=True):
    T = json.loads(re.sub(r"^window.TIMING = |;\s*$", "", (ROOT / "videos" / slug / "timing.js").read_text(encoding="utf-8")))
    ids = [s["id"] for s in T["scenes"]]; ec = ids[-1]
    assert len(scenes) == len(ids) - 1, (slug, len(scenes), ids)
    h = HEAD.format(title=T["title"], css=".lbl{font-family:Montserrat;font-weight:900}" + css)
    for i, (svgc, drift) in enumerate(scenes):
        extra = ""
        if i == 0: extra = f'\n      <div class="title main top">{title_html}</div>\n      <div class="title sub top">{sub_html}</div>'
        h += SCENE.format(id=ids[i], drift=drift, svg=svgc, extra=extra)
    o = "".join(f'\n      <div class="ec-opt {k}"><span class="k">{k.upper()}</span><span class="t">{a}<small>{b}</small></span></div>' for k, (a, b) in zip("abc", opts))
    ecx = (f'\n      <div class="ec-q" style="font-size:78px">{q_html}</div>{o}'
           f'\n      <div class="ec-cta">SCHREIB A, B ODER C IN DIE KOMMENTARE<br/><span style="color:var(--yellow)">{cta2}</span></div>'
           '\n      <div class="ec-ring"><svg viewBox="0 0 130 130" width="130" height="130"><circle cx="65" cy="65" r="56" fill="#0d0b18" stroke="#3a3560" stroke-width="10"/><circle class="ec-arc" cx="65" cy="65" r="56" fill="none" stroke="#ff3b3b" stroke-width="10" stroke-linecap="round" stroke-dasharray="352" transform="rotate(-90 65 65)"/></svg><div class="ec-n">6</div></div>')
    h += SCENE.format(id=ec, drift="1.0", svg=f'<rect width="1080" height="1920" fill="#14122b"/><g id="{ec}-stars"></g>', extra=ecx).replace('data-drift="1.0"', 'data-punch="1.06" data-drift="1.0"')
    hide_at = "kata" if dramatic else "loop"
    hookfx = (f'tl.to(["#{ids[0]} .title.main", "#{ids[0]} .title.sub"], {{ autoAlpha: 0, duration: .15 }}, at("{hide_at}", -0.15));\n    '
              + (f'E.hookFx(tl, cs("kata", {dramatic})' + ('' if flash else ', { flash: false }') + ');' if dramatic is not False and dramatic is not None else 'E.hookFx(tl, null, { dramatic: false });'))
    h += TAIL.format(js=js, ec=ec, hookfx=hookfx, post=post)
    (ROOT / "videos" / slug / "index.html").write_text(h, encoding="utf-8")
    print("index.html:", slug)
