/* TikTok-Erklärvideo-Engine für HyperFrames.
 * Liest window.TIMING (timing.js) und baut darauf:
 *   - Szenenwechsel (harte Schnitte mit Punch-in + langsamer Kamerafahrt)
 *   - Wort-für-Wort-Untertitel (Markup: *rot*  ^gelb^  ~grün~)
 *   - HUD oben (rotes Zähler-Panel + farbiger Status-Chip)
 * Alles deterministisch (kein Math.random / Date.now): seekbar Frame für Frame.
 */
(function () {
  const T = window.TIMING;
  const L = {};
  T.lines.forEach((l) => (L[l.id] = l));

  /** Startzeit eines Satzes (+ Offset). */
  const at = (id, off = 0) => {
    if (!L[id]) throw new Error("Unbekannte Zeile: " + id);
    return +(L[id].t0 + off).toFixed(3);
  };
  /** Endzeit eines Satzes (+ Offset). */
  const end = (id, off = 0) => +(L[id].t1 + off).toFixed(3);
  const ref = (r) => at(r.at, r.off || 0);

  /** Deterministischer Zufall (Mulberry32). */
  function rng(seed) {
    let a = seed >>> 0;
    return function () {
      a |= 0; a = (a + 0x6d2b79f5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  const SVGNS = "http://www.w3.org/2000/svg";
  /** SVG-Element erzeugen: svg('rect', {x:1}, parent) */
  function svg(tag, attrs, parent) {
    const el = document.createElementNS(SVGNS, tag);
    for (const k in attrs) el.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(el);
    return el;
  }

  function fmt(s) {
    return s
      .replace(/\*([^*]+)\*/g, '<span class="r">$1</span>')
      .replace(/\^([^^]+)\^/g, '<span class="y">$1</span>')
      .replace(/~([^~]+)~/g, '<span class="g">$1</span>');
  }

  /** Szenen-Fenster aus TIMING.scenes: [{id,t0,t1}] */
  function sceneWindows() {
    const s = T.scenes.map((x) => ({ id: x.id, t0: Math.max(0, ref(x)) }));
    s.forEach((x, i) => (x.t1 = i + 1 < s.length ? s[i + 1].t0 : T.duration));
    return s;
  }

  /** Sichtbarkeit + Punch-in + Drift jeder Szene.
   *  Erwartet: <section class="scene" id="s1"><div class="cam"><div class="drift">…</div></div></section> */
  function buildScenes(tl) {
    const wins = sceneWindows();
    document.querySelectorAll(".scene").forEach((el) => tl.set(el, { autoAlpha: 0 }, 0));
    wins.forEach((w) => {
      const el = document.getElementById(w.id);
      if (!el) return;
      const cam = el.querySelector(".cam");
      const drift = el.querySelector(".drift");
      tl.set(el, { autoAlpha: 1 }, w.t0);
      if (w.t1 < T.duration) tl.set(el, { autoAlpha: 0 }, w.t1);
      const punch = el.dataset.punch !== undefined ? +el.dataset.punch : 1.12;
      if (cam && w.t0 > 0) tl.fromTo(cam, { scale: punch }, { scale: 1, duration: 0.45, ease: "power3.out" }, w.t0);
      const dz = el.dataset.drift !== undefined ? +el.dataset.drift : 1.06;
      const dy = el.dataset.driftY !== undefined ? +el.dataset.driftY : 0;
      if (drift) tl.fromTo(drift, { scale: 1, y: 0 }, { scale: dz, y: dy, duration: w.t1 - w.t0, ease: "none" }, w.t0);
    });
    // Weißer Blitz bei jedem Schnitt (sehr kurz, wie in der Vorlage)
    const flash = document.getElementById("flash");
    if (flash) {
      tl.set(flash, { opacity: 0 }, 0);
      wins.slice(1).forEach((w) => tl.fromTo(flash, { opacity: 0.22 }, { opacity: 0, duration: 0.18, ease: "power2.out", immediateRender: false }, w.t0));
    }
    return wins;
  }

  /** Wort-Untertitel: pro Chunk eine Einblendung, Dauer proportional zur Länge. */
  function buildCaptions(tl) {
    const host = document.getElementById("captions");
    const lines = T.lines;
    lines.forEach((line, li) => {
      if (line.noCap) return;
      const nextStart = li + 1 < lines.length ? lines[li + 1].t0 : T.duration;
      const lens = line.chunks.map((c) => c.replace(/[*^~]/g, "").length + 5);
      const total = lens.reduce((a, b) => a + b, 0);
      const span = line.t1 - line.t0;
      let t = line.t0;
      const cs = line.chunkStarts; // wortgenaue Startzeiten (ElevenLabs-Alignment), falls vorhanden
      line.chunks.forEach((c, i) => {
        if (cs && cs[i] !== undefined) t = cs[i];
        const d = cs ? (i + 1 < cs.length ? cs[i + 1] : line.t1) - t : (span * lens[i]) / total;
        const el = document.createElement("div");
        el.className = "cap";
        el.innerHTML = fmt(c);
        host.appendChild(el);
        const last = i === line.chunks.length - 1;
        const off = last ? Math.min(line.t1 + 0.35, nextStart - 0.02) : t + d;
        tl.set(el, { autoAlpha: 0 }, 0);
        tl.set(el, { autoAlpha: 1 }, t);
        tl.fromTo(el, { scale: 0.7, y: 18 }, { scale: 1, y: 0, duration: 0.17, ease: "back.out(2.6)" }, t);
        tl.set(el, { autoAlpha: 0 }, off);
        t += d;
      });
    });
  }

  /** HUD: rotes Panel mit Zähler + Status-Chip, Werte aus TIMING.hud.steps */
  function buildHud(tl) {
    const H = T.hud;
    if (!H) return;
    const hud = document.getElementById("hud");
    hud.querySelector(".hud-label").textContent = "⚠ " + H.label;
    hud.querySelector(".hud-unit").textContent = H.unit;
    hud.querySelector(".hud-sub").textContent = H.sub;
    hud.querySelector(".chip-label").textContent = H.chipLabel;
    const num = hud.querySelector(".hud-num");
    const chip = hud.querySelector(".chip");
    const chipVal = hud.querySelector(".chip-val");
    const delta = hud.querySelector(".hud-delta");
    const pad = (v) => String(Math.round(v)).padStart(3, "0");
    const chipClass = (v) => (v >= 60 ? "ok" : v >= 30 ? "warn" : "bad");

    tl.set(hud, { autoAlpha: 0 }, 0);
    const t0 = ref(H.show);
    tl.set(hud, { autoAlpha: 1 }, t0);
    tl.fromTo(hud, { y: -40, scale: 0.85 }, { y: 0, scale: 1, duration: 0.35, ease: "back.out(2)" }, t0);
    tl.set(hud, { autoAlpha: 0 }, ref(H.hide));

    // Werte als reine Funktion der Zeit -> korrekt bei jedem Seek (auch rückwärts / Sprünge)
    const steps = H.steps.map((s) => ({ t: ref(s), v: s.value, c: s.chip }));
    const ease = (x) => 1 - Math.pow(1 - x, 3);
    function valueAt(t, key) {
      let val = steps[0][key];
      for (let i = 1; i < steps.length; i++) {
        const s = steps[i], p = steps[i - 1];
        if (t >= s.t) { const k = Math.min(1, (t - s.t) / 0.6); val = p[key] + (s[key] - p[key]) * ease(k); }
      }
      return val;
    }
    const render = (t) => {
      const v = valueAt(t, "v"), c = valueAt(t, "c");
      num.textContent = pad(v);
      chipVal.textContent = Math.round(c) + "%";
      chip.className = "chip " + chipClass(c);
    };
    clock(tl, render);
    let prev = H.steps[0];
    H.steps.forEach((s, i) => {
      const t = ref(s);
      if (i === 0) return;
      const dv = s.value - prev.value;
      if (dv >= 3) {
        tl.set(delta, { textContent: "+" + dv + " " + H.unit }, t);
        tl.fromTo(delta, { autoAlpha: 1, scale: 1.4 }, { scale: 1, duration: 0.25, ease: "back.out(3)" }, t);
        tl.to(delta, { autoAlpha: 0, duration: 0.25 }, t + 1.3);
      }
      if (s.chip !== prev.chip) tl.fromTo(chip, { scale: 1.15 }, { scale: 1, duration: 0.3, ease: "back.out(3)" }, t);
      prev = s;
    });
    tl.set(delta, { autoAlpha: 0 }, 0);
  }

  /** Interaktions-Einblendungen aus TIMING.interact:
   *  [{type:"like"|"follow"|"comment"|"save"|"share", at:"<zeile>", off:0, dur:2.5, text:"…"}]
   *  Pille unter den Untertiteln (y≈1570) mit animiertem Icon. */
  const ICONS = {
    like: '<path d="M50 84 C20 62 8 48 8 32 C8 19 18 10 30 10 C39 10 46 15 50 22 C54 15 61 10 70 10 C82 10 92 19 92 32 C92 48 80 62 50 84Z" fill="#ff3b5c"/>',
    follow: '<circle cx="50" cy="50" r="42" fill="#ff3b5c"/><path d="M50 28 V72 M28 50 H72" stroke="#fff" stroke-width="12" stroke-linecap="round"/>',
    comment: '<path d="M14 18 H86 Q92 18 92 24 V64 Q92 70 86 70 H44 L24 88 V70 H14 Q8 70 8 64 V24 Q8 18 14 18Z" fill="#3fd4ff"/><circle cx="32" cy="44" r="7" fill="#0d0b18"/><circle cx="50" cy="44" r="7" fill="#0d0b18"/><circle cx="68" cy="44" r="7" fill="#0d0b18"/>',
    save: '<path d="M22 8 H78 V92 L50 72 L22 92Z" fill="#ffd23f"/>',
    share: '<path d="M56 10 L94 44 L56 78 V58 C32 58 18 66 6 86 C10 58 24 36 56 30Z" fill="#3ee08f"/>',
  };
  const DEFAULT_TEXT = { like: "LIKE, WENN DU'S WUSSTEST", follow: "FOLG FÜR TEIL 2", comment: "SCHREIB'S IN DIE KOMMENTARE", save: "SPEICHERN FÜR SPÄTER", share: "SCHICK'S DEINEM BESTEN FREUND" };
  function buildInteract(tl) {
    const list = T.interact || [];
    if (!list.length) return;
    const root = document.getElementById("root");
    list.forEach((it, i) => {
      const el = document.createElement("div");
      el.className = "interact " + it.type;
      el.innerHTML = `<svg class="ico" viewBox="0 0 100 100">${ICONS[it.type] || ICONS.like}</svg><span>${fmt(it.text || DEFAULT_TEXT[it.type] || "")}</span>`;
      root.appendChild(el);
      const t = ref(it), d = it.dur || 2.6;
      const ico = el.querySelector(".ico");
      tl.set(el, { autoAlpha: 0, xPercent: -50 }, 0);
      tl.fromTo(el, { autoAlpha: 0, y: 60, scale: 0.6 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.35, ease: "back.out(2.2)", immediateRender: false }, t);
      tl.fromTo(ico, { scale: 1 }, { scale: 1.3, duration: 0.18, repeat: Math.max(1, Math.floor(d / 0.36) - 1), yoyo: true, ease: "sine.inOut", immediateRender: false }, t + 0.35);
      tl.to(el, { autoAlpha: 0, y: 30, duration: 0.25, ease: "power2.in" }, t + d);
    });
  }

  /** Ruft fn(t) bei jedem Frame mit der absoluten Videozeit auf (seek-sicher).
   *  Für Text-Zähler, Uhren usw. — niemals Zustand zwischen Frames speichern. */
  function clock(tl, fn) {
    const p = { t: 0 };
    tl.fromTo(p, { t: 0 }, { t: T.duration, duration: T.duration, ease: "none", immediateRender: true, onUpdate: () => fn(p.t) }, 0);
    fn(0);
  }

  window.Engine = { T, at, end, ref, rng, svg, fmt, clock, sceneWindows, buildScenes, buildCaptions, buildHud, buildInteract };
})();
