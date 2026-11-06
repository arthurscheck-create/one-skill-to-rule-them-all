/* Bausteine für Szenen (Serie 3+): const K = Engine.kit(tl); K.badge(...), K.pop(...) usw. */
(function () {
  const E = window.Engine, svg = E.svg, INK = "#0d0b18";
  E.kit = function (tl) {
    const K = { INK };
    K.txt = (g, x, y, s, fs, fill, extra) => { const t = svg("text", Object.assign({ x, y, "font-family": "Montserrat", "font-weight": 900, "font-size": fs, fill, "text-anchor": "middle" }, extra || {}), g); t.textContent = s; return t; };
    K.otxt = (g, x, y, s, fs, fill) => K.txt(g, x, y, s, fs, fill, { stroke: INK, "stroke-width": Math.max(6, fs * .12), "paint-order": "stroke" });
    K.badge = (g, x, y, text, color, size) => {
      const b = svg("g", { transform: `translate(${x},${y})` }, g), fs = size || 60, w = text.length * fs * .66 + 80, h = fs * 1.6;
      svg("rect", { x: -w / 2, y: -h / 2, width: w, height: h, rx: 24, fill: "rgba(18,8,16,.94)", stroke: color, "stroke-width": 8 }, b);
      K.txt(b, 0, fs * .36, text, fs, color); return b;
    };
    K.pop = (el, t, origin) => { tl.set(el, { autoAlpha: 0 }, 0); tl.fromTo(el, { autoAlpha: 1, scale: .3, svgOrigin: origin }, { scale: 1, duration: .35, ease: "back.out(2.6)", immediateRender: false }, t); };
    K.hide = (el, t) => tl.to(el, { autoAlpha: 0, duration: .15 }, t);
    K.fadeIn = (el, t, d) => { tl.set(el, { autoAlpha: 0 }, 0); tl.to(el, { autoAlpha: 1, duration: d || .4 }, t); };
    K.shake = (el, t, n, a) => { tl.fromTo(el, { x: -(a || 12) }, { x: a || 12, duration: .05, repeat: n || 9, yoyo: true, ease: "none", immediateRender: false }, t); tl.set(el, { x: 0 }, t + .05 * ((n || 9) + 1)); };
    K.burst = (g, x, y, r, word, fill) => {
      const b = svg("g", {}, g); let d = "";
      for (let i = 0; i < 16; i++) { const a = i * Math.PI / 8, rr = i % 2 ? r * .55 : r; d += (i ? "L" : "M") + (x + Math.cos(a) * rr).toFixed(1) + "," + (y + Math.sin(a) * rr).toFixed(1); }
      svg("path", { d: d + "Z", fill: fill || "#ffd23f", stroke: INK, "stroke-width": 7, "stroke-linejoin": "round" }, b);
      if (word) K.otxt(b, x, y + r * .12, word, r * Math.min(.34, 1.9 / word.length), "#e8463c");
      return b;
    };
    K.check = (g, x, y, s) => { const c = svg("g", {}, g); s = s || 1; svg("circle", { cx: x, cy: y, r: 60 * s, fill: "#3ee08f", stroke: INK, "stroke-width": 7 }, c); svg("path", { d: `M${x - 28 * s},${y} l${20 * s},${22 * s} l${38 * s},${-42 * s}`, fill: "none", stroke: INK, "stroke-width": 14 * s, "stroke-linecap": "round", "stroke-linejoin": "round" }, c); return c; };
    K.cross = (g, x, y, s) => { const c = svg("g", {}, g), d = `M${x - s},${y - s} L${x + s},${y + s} M${x + s},${y - s} L${x - s},${y + s}`; svg("path", { d, stroke: INK, "stroke-width": s * .42, "stroke-linecap": "round" }, c); svg("path", { d, stroke: "#ff3b3b", "stroke-width": s * .27, "stroke-linecap": "round" }, c); return c; };
    K.panel = (g, x, y, w, h, fill, stroke) => svg("rect", { x: x - w / 2, y: y - h / 2, width: w, height: h, rx: 30, fill: fill || "rgba(18,8,16,.94)", stroke: stroke || "#fff", "stroke-width": 9 }, g);
    K.bolt = (g, x, y, s, fill) => svg("path", { d: `M${x},${y} l${-60 * s},${150 * s} h${55 * s} l${-35 * s},${130 * s} l${110 * s},${-175 * s} h${-60 * s} l${40 * s},${-105 * s}Z`, fill: fill || "#ffd23f", stroke: INK, "stroke-width": 7, "stroke-linejoin": "round" }, g);
    K.rays = (g, cx, cy, n, color, op) => { const r = svg("g", {}, g); for (let i = 0; i < n; i++) { const a = i * 2 * Math.PI / n, a2 = a + Math.PI / n * .6; svg("path", { d: `M${cx},${cy} L${cx + Math.cos(a) * 1600},${cy + Math.sin(a) * 1600} L${cx + Math.cos(a2) * 1600},${cy + Math.sin(a2) * 1600}Z`, fill: color || "#fff", opacity: op || .15 }, r); } E.clock(tl, (t) => r.setAttribute("transform", `rotate(${(t * 10).toFixed(2)} ${cx} ${cy})`)); return r; };
    K.pulse = (el, cx, cy, per, amp) => E.clock(tl, (t) => { const k = 1 + Math.abs(Math.sin(t * Math.PI / (per || 1))) * (amp || .1); el.setAttribute("transform", `translate(${(cx * (1 - k)).toFixed(1)},${(cy * (1 - k)).toFixed(1)}) scale(${k.toFixed(3)})`); });
    K.bob = (el, amp, sp, ph) => E.clock(tl, (t) => el.setAttribute("transform", `translate(0,${(Math.sin(t * (sp || 2) + (ph || 0)) * (amp || 10)).toFixed(1)})`));
    K.hudText = (pairs, first) => { const hn = document.querySelector("#hud .hud-num"); E.clock(tl, (t) => { let v = first; pairs.forEach(([a, s]) => { if (t >= a) v = s; }); hn.textContent = v; }); };
    K.hudFmt = () => { const hn = document.querySelector("#hud .hud-num"); E.clock(tl, (t) => { const v = parseInt(hn.textContent, 10); if (!isNaN(v) && /^\d+$/.test(hn.textContent)) hn.textContent = v.toLocaleString("de-DE"); }); };
    K.stars = (g, n, seed) => E.stars(g, n, seed);
    K.person = (g, o) => E.person(g, o);
    return K;
  };
})();
