/* Wiederverwendbare Flat-Vector-Figuren und Requisiten (SVG <defs>).
 * Farben über CSS-Variablen pro Instanz: --shirt --pants --hair --skin
 * Ursprung jeder Figur = Mitte zwischen den Füßen (0,0). Kopf bei y=-490.
 */
(function () {
  const DEFS = `
  <defs>
    <g id="p-body">
      <ellipse cx="0" cy="2" rx="118" ry="18" fill="rgba(0,0,0,.28)"/>
      <ellipse cx="-42" cy="-10" rx="46" ry="18" fill="#22212e"/>
      <ellipse cx="42" cy="-10" rx="46" ry="18" fill="#22212e"/>
      <rect x="-66" y="-232" width="54" height="222" rx="20" fill="var(--pants,#2f3352)"/>
      <rect x="12" y="-232" width="54" height="222" rx="20" fill="var(--pants,#2f3352)"/>
      <rect x="-22" y="-425" width="44" height="40" rx="10" fill="var(--skin,#f3c6a0)"/>
      <path d="M-108,-212 C-116,-300 -112,-372 -72,-398 L72,-398 C112,-372 116,-300 108,-212 Q0,-196 -108,-212Z" fill="var(--shirt,#4d5275)"/>
      <path d="M-62,-400 Q0,-366 62,-400 Q30,-350 0,-352 Q-30,-350 -62,-400Z" fill="rgba(0,0,0,.2)"/>
      <path d="M-55,-262 L55,-262 L46,-222 L-46,-222Z" fill="rgba(0,0,0,.13)"/>
      <line x1="-16" y1="-360" x2="-20" y2="-300" stroke="rgba(255,255,255,.55)" stroke-width="5" stroke-linecap="round"/>
      <line x1="16" y1="-360" x2="20" y2="-300" stroke="rgba(255,255,255,.55)" stroke-width="5" stroke-linecap="round"/>
      <circle cx="-94" cy="-484" r="19" fill="var(--skin,#f3c6a0)"/>
      <circle cx="94" cy="-484" r="19" fill="var(--skin,#f3c6a0)"/>
      <circle cx="0" cy="-490" r="96" fill="var(--skin,#f3c6a0)"/>
      <path d="M-98,-500 C-104,-592 -40,-616 2,-614 C56,-614 108,-586 98,-500 C86,-540 50,-556 18,-552 C10,-575 -20,-580 -30,-560 C-60,-556 -84,-536 -98,-500Z" fill="var(--hair,#5b3a22)"/>
      <circle cx="-60" cy="-452" r="15" fill="#ff7f86" opacity=".45"/>
      <circle cx="60" cy="-452" r="15" fill="#ff7f86" opacity=".45"/>
    </g>

    <g id="p-hairlong">
      <path d="M-108,-500 C-118,-612 118,-612 108,-500 L126,-372 Q60,-344 0,-352 Q-60,-344 -126,-372Z" fill="var(--hair,#5b3a22)"/>
    </g>
    <g id="f-happy">
      <circle cx="-32" cy="-490" r="9" fill="#1a1726"/><circle cx="32" cy="-490" r="9" fill="#1a1726"/>
      <path d="M-56,-524 Q-34,-536 -14,-526" stroke="#3b2614" stroke-width="7" fill="none" stroke-linecap="round"/>
      <path d="M56,-524 Q34,-536 14,-526" stroke="#3b2614" stroke-width="7" fill="none" stroke-linecap="round"/>
      <path d="M-30,-446 Q0,-414 30,-446" stroke="#5a2a2a" stroke-width="7" fill="#fff" stroke-linecap="round"/>
    </g>
    <g id="f-worried">
      <circle cx="-34" cy="-492" r="18" fill="#fff"/><circle cx="34" cy="-492" r="18" fill="#fff"/>
      <circle cx="-32" cy="-488" r="8.5" fill="#1a1726"/><circle cx="32" cy="-488" r="8.5" fill="#1a1726"/>
      <path d="M-58,-520 L-16,-532" stroke="#3b2614" stroke-width="7" stroke-linecap="round"/>
      <path d="M58,-520 L16,-532" stroke="#3b2614" stroke-width="7" stroke-linecap="round"/>
      <path d="M-22,-436 Q0,-450 22,-436" stroke="#5a2a2a" stroke-width="6" fill="none" stroke-linecap="round"/>
    </g>
    <g id="f-shock">
      <circle cx="-34" cy="-494" r="22" fill="#fff"/><circle cx="34" cy="-494" r="22" fill="#fff"/>
      <circle cx="-34" cy="-492" r="7" fill="#1a1726"/><circle cx="34" cy="-492" r="7" fill="#1a1726"/>
      <path d="M-58,-536 Q-36,-548 -14,-538" stroke="#3b2614" stroke-width="7" fill="none" stroke-linecap="round"/>
      <path d="M58,-536 Q36,-548 14,-538" stroke="#3b2614" stroke-width="7" fill="none" stroke-linecap="round"/>
      <ellipse cx="0" cy="-438" rx="17" ry="21" fill="#5a2430"/>
      <ellipse cx="0" cy="-430" rx="10" ry="7" fill="#e86a7a"/>
    </g>
    <g id="f-smirk">
      <circle cx="-34" cy="-490" r="17" fill="#fff"/><circle cx="34" cy="-490" r="17" fill="#fff"/>
      <circle cx="-30" cy="-486" r="8" fill="#1a1726"/><circle cx="38" cy="-486" r="8" fill="#1a1726"/>
      <rect x="-54" y="-512" width="40" height="16" fill="var(--skin,#f3c6a0)"/>
      <path d="M-58,-516 L-14,-514" stroke="#3b2614" stroke-width="7" stroke-linecap="round"/>
      <path d="M58,-540 Q36,-552 14,-534" stroke="#3b2614" stroke-width="7" fill="none" stroke-linecap="round"/>
      <path d="M-24,-442 Q6,-430 28,-452" stroke="#5a2a2a" stroke-width="6" fill="none" stroke-linecap="round"/>
    </g>
    <g id="f-neutral">
      <circle cx="-32" cy="-490" r="9" fill="#1a1726"/><circle cx="32" cy="-490" r="9" fill="#1a1726"/>
      <path d="M-14,-440 L14,-440" stroke="#5a2a2a" stroke-width="6" stroke-linecap="round"/>
    </g>

    <g id="a-down">
      <path d="M-98,-378 Q-136,-330 -136,-232" stroke="var(--shirt,#4d5275)" stroke-width="46" fill="none" stroke-linecap="round"/>
      <path d="M98,-378 Q136,-330 136,-232" stroke="var(--shirt,#4d5275)" stroke-width="46" fill="none" stroke-linecap="round"/>
      <circle cx="-136" cy="-214" r="25" fill="var(--skin,#f3c6a0)"/><circle cx="136" cy="-214" r="25" fill="var(--skin,#f3c6a0)"/>
    </g>
    <g id="a-phone">
      <path d="M-98,-378 Q-136,-330 -136,-232" stroke="var(--shirt,#4d5275)" stroke-width="46" fill="none" stroke-linecap="round"/>
      <circle cx="-136" cy="-214" r="25" fill="var(--skin,#f3c6a0)"/>
      <path d="M98,-378 Q140,-300 118,-262 Q90,-240 50,-290" stroke="var(--shirt,#4d5275)" stroke-width="46" fill="none" stroke-linecap="round"/>
      <rect x="6" y="-380" width="56" height="96" rx="10" fill="#14131d"/>
      <rect x="12" y="-372" width="44" height="78" rx="6" fill="#8fd6ff"/>
      <circle cx="44" cy="-300" r="25" fill="var(--skin,#f3c6a0)"/>
    </g>
    <g id="a-box">
      <path d="M-98,-378 Q-126,-320 -90,-300" stroke="var(--shirt,#4d5275)" stroke-width="46" fill="none" stroke-linecap="round"/>
      <path d="M98,-378 Q126,-320 90,-300" stroke="var(--shirt,#4d5275)" stroke-width="46" fill="none" stroke-linecap="round"/>
      <rect x="-95" y="-390" width="190" height="150" rx="8" fill="#c98c55"/>
      <rect x="-95" y="-390" width="190" height="28" fill="#b47a46"/>
      <rect x="-14" y="-390" width="28" height="150" fill="#e2b077" opacity=".8"/>
      <circle cx="-96" cy="-300" r="25" fill="var(--skin,#f3c6a0)"/><circle cx="96" cy="-300" r="25" fill="var(--skin,#f3c6a0)"/>
    </g>
    <g id="a-bag">
      <path d="M-98,-378 Q-136,-330 -136,-232" stroke="var(--shirt,#4d5275)" stroke-width="46" fill="none" stroke-linecap="round"/>
      <path d="M98,-378 Q136,-330 136,-232" stroke="var(--shirt,#4d5275)" stroke-width="46" fill="none" stroke-linecap="round"/>
      <path d="M-176,-200 L-96,-200 L-104,-60 L-168,-60Z" fill="#f2f0f7"/><path d="M-160,-200 Q-136,-240 -112,-200" stroke="#f2f0f7" stroke-width="8" fill="none"/>
      <rect x="-170" y="-224" width="20" height="30" fill="#e8463c"/><rect x="-146" y="-232" width="18" height="38" fill="#ffd23f"/>
      <path d="M176,-200 L96,-200 L104,-60 L168,-60Z" fill="#f2f0f7"/><path d="M160,-200 Q136,-240 112,-200" stroke="#f2f0f7" stroke-width="8" fill="none"/>
      <rect x="116" y="-230" width="22" height="34" fill="#3ee08f"/>
      <circle cx="-136" cy="-214" r="25" fill="var(--skin,#f3c6a0)"/><circle cx="136" cy="-214" r="25" fill="var(--skin,#f3c6a0)"/>
    </g>

    <g id="rat">
      <path d="M-50,4 Q-110,-34 -160,8" stroke="#c48f9a" stroke-width="7" fill="none" stroke-linecap="round"/>
      <ellipse cx="0" cy="0" rx="62" ry="30" fill="#6f6b7b"/>
      <ellipse cx="58" cy="-6" rx="32" ry="22" fill="#7a7686"/>
      <circle cx="44" cy="-28" r="13" fill="#7a7686"/><circle cx="44" cy="-28" r="7" fill="#e7a3b0"/>
      <circle cx="68" cy="-12" r="4" fill="#111"/>
      <circle cx="90" cy="-4" r="6" fill="#e7a3b0"/>
      <rect x="-36" y="20" width="12" height="16" rx="5" fill="#5d5968"/><rect x="24" y="20" width="12" height="16" rx="5" fill="#5d5968"/>
    </g>
    <g id="bag">
      <path d="M-72,0 C-96,-40 -86,-112 -32,-126 L-12,-138 L-24,-160 L0,-150 L24,-160 L12,-138 L32,-126 C86,-112 96,-40 72,0 Z" fill="#26282f"/>
      <path d="M-50,-20 C-62,-60 -50,-96 -20,-108" stroke="rgba(255,255,255,.12)" stroke-width="10" fill="none" stroke-linecap="round"/>
      <path d="M-74,0 L74,0" stroke="rgba(0,0,0,.35)" stroke-width="6"/>
    </g>
    <g id="truck">
      <ellipse cx="0" cy="4" rx="230" ry="20" fill="rgba(0,0,0,.35)"/>
      <rect x="-200" y="-500" width="400" height="430" rx="10" fill="#dad6e8"/>
      <rect x="-200" y="-500" width="400" height="34" rx="8" fill="#bcb7cf"/>
      <rect x="-3" y="-466" width="6" height="396" fill="#9e99b5"/>
      <rect x="-128" y="-460" width="8" height="386" fill="#b5b0c8"/><rect x="-68" y="-460" width="8" height="386" fill="#b5b0c8"/>
      <rect x="60" y="-460" width="8" height="386" fill="#b5b0c8"/><rect x="120" y="-460" width="8" height="386" fill="#b5b0c8"/>
      <rect x="-200" y="-330" width="400" height="44" fill="var(--brand,#e8463c)"/>
      <rect x="-210" y="-82" width="420" height="30" rx="6" fill="#2b2a38"/>
      <rect x="-190" y="-132" width="26" height="44" rx="5" fill="#5a1d24"/><rect x="164" y="-132" width="26" height="44" rx="5" fill="#5a1d24"/>
      <rect x="-180" y="-52" width="80" height="54" rx="8" fill="#14141b"/><rect x="100" y="-52" width="80" height="54" rx="8" fill="#14141b"/>
      <rect x="-60" y="-50" width="120" height="30" rx="4" fill="#f2f0f7"/>
    </g>
    <g id="tower">
      <path d="M-160,0 C-112,-150 -112,-270 -98,-400 L98,-400 C112,-270 112,-150 160,0 Z" fill="#4d4977"/>
      <path d="M-160,0 C-112,-150 -112,-270 -98,-400 L-40,-400 C-56,-270 -60,-150 -90,0 Z" fill="rgba(255,255,255,.07)"/>
      <rect x="-104" y="-410" width="208" height="16" rx="4" fill="#5d598a"/>
      <path d="M-124,-120 L124,-120" stroke="rgba(0,0,0,.18)" stroke-width="8"/>
    </g>
  </defs>`;

  const holder = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  holder.setAttribute("width", "0");
  holder.setAttribute("height", "0");
  holder.setAttribute("style", "position:absolute;width:0;height:0;overflow:hidden");
  holder.innerHTML = DEFS;
  document.body.insertBefore(holder, document.body.firstChild);

  /** Figur platzieren: Engine.person(svgGroup, {x,y,s,face:'worried',arms:'down',shirt,hair,pants,flip}) */
  window.Engine.person = function (parent, o) {
    const g = window.Engine.svg("g", { transform: `translate(${o.x || 0},${o.y || 0}) scale(${(o.flip ? -1 : 1) * (o.s || 1)},${o.s || 1})` }, parent);
    let style = "";
    if (o.shirt) style += `--shirt:${o.shirt};`;
    if (o.hair) style += `--hair:${o.hair};`;
    if (o.pants) style += `--pants:${o.pants};`;
    if (o.skin) style += `--skin:${o.skin};`;
    if (style) g.setAttribute("style", style);
    const inner = window.Engine.svg("g", {}, g);
    if (o.long) window.Engine.svg("use", { href: "#p-hairlong" }, inner);
    window.Engine.svg("use", { href: "#p-body" }, inner);
    window.Engine.svg("use", { href: "#a-" + (o.arms || "down") }, inner);
    window.Engine.svg("use", { href: "#f-" + (o.face || "worried") }, inner);
    if (o.id) g.id = o.id;
    return g;
  };
  window.Engine.use = function (parent, ref, x, y, s, extra) {
    const g = window.Engine.svg("g", { transform: `translate(${x},${y}) scale(${s || 1})` }, parent);
    window.Engine.svg("use", Object.assign({ href: "#" + ref }, extra || {}), g);
    return g;
  };
})();

/* ---------- Bausatz: Skyline, Sterne, Erdkugel ---------- */
(function () {
  const E = window.Engine, svg = E.svg;
  /** Skyline mit Fenstern. o: {seed, base, x0, x1, wMin, wMax, hMin, hMax, fill, gap, lit, win, litColor, lightsInto} → Liste der Fenster */
  E.skyline = function (g, o) {
    const r = E.rng(o.seed || 1); let x = o.x0 || 0; const out = [];
    const L = o.lightsInto || g;
    while (x < (o.x1 || 1080)) {
      const w = o.wMin + r() * (o.wMax - o.wMin), h = o.hMin + r() * (o.hMax - o.hMin), y = o.base - h;
      svg("rect", { x, y, width: w, height: h + 4, fill: o.fill }, g);
      if (o.lit) { const c = o.win || 14; for (let wy = y + c; wy < o.base - c; wy += c * 2) for (let wx = x + c * .8; wx < x + w - c; wx += c * 1.8) if (r() < o.lit) out.push(svg("rect", { x: wx, y: wy, width: c, height: c * 1.2, fill: r() < .85 ? (o.litColor || "#ffd27a") : "#ff8a5c" }, L)); }
      x += w + (o.gap || 0);
    }
    return out;
  };
  /** Sternenhimmel */
  E.stars = function (g, n, seed, h) { const r = E.rng(seed || 3); for (let i = 0; i < n; i++) svg("circle", { cx: r() * 1080, cy: r() * (h || 1920), r: 1 + r() * 2.6, fill: "#fff", opacity: .25 + r() * .6 }, g); };
  /** Erdkugel mit drehbaren Kontinenten. Rückgabe {land, period}: tl.fromTo(land,{x:0},{x:-period,...}) dreht sie. */
  E.globe = function (g, o) {
    const cx = o.cx, cy = o.cy, R = o.r, id = o.id || "gl" + Math.round(cx + cy);
    const defs = svg("defs", {}, g);
    const cp = svg("clipPath", { id: id + "-c" }, defs); svg("circle", { cx, cy, r: R }, cp);
    const rg = svg("radialGradient", { id: id + "-o", cx: ".35", cy: ".3", r: ".8" }, defs);
    svg("stop", { offset: "0", "stop-color": "#4fa8ff" }, rg); svg("stop", { offset: "1", "stop-color": "#123a86" }, rg);
    const sh = svg("radialGradient", { id: id + "-s", cx: ".3", cy: ".3", r: ".9" }, defs);
    svg("stop", { offset: ".55", "stop-color": "#000", "stop-opacity": "0" }, sh); svg("stop", { offset: "1", "stop-color": "#000", "stop-opacity": ".6" }, sh);
    svg("circle", { cx, cy, r: R * 1.08, fill: "#6fd6ff", opacity: .18 }, g);
    const body = svg("g", { "clip-path": `url(#${id}-c)` }, g);
    svg("circle", { cx, cy, r: R, fill: `url(#${id}-o)` }, body);
    const land = svg("g", {}, body);
    const W = R * 4, r = E.rng(o.seed || 7);
    const blobs = [];
    for (let i = 0; i < 7; i++) blobs.push({ x: (i / 7) * W + r() * R * .3, y: cy - R * .7 + r() * R * 1.4, s: R * (.18 + r() * .28) });
    [0, W].forEach((dx) => blobs.forEach((b) => {
      const p = [];
      for (let k = 0; k < 9; k++) { const a = (k / 9) * Math.PI * 2, rr = b.s * (.7 + ((k * 37 + b.x) % 7) / 14); p.push([cx - R + b.x + dx + Math.cos(a) * rr * 1.3, b.y + Math.sin(a) * rr]); }
      svg("path", { d: "M" + p.map((q) => q.map((v) => v.toFixed(1)).join(",")).join(" L") + "Z", fill: "#3fae5a", stroke: "#2e8a47", "stroke-width": 6, "stroke-linejoin": "round" }, land);
    }));
    svg("ellipse", { cx, cy: cy - R * .92, rx: R * .55, ry: R * .14, fill: "#eef6ff", opacity: .9 }, body);
    svg("ellipse", { cx, cy: cy + R * .94, rx: R * .5, ry: R * .12, fill: "#eef6ff", opacity: .9 }, body);
    svg("circle", { cx, cy, r: R, fill: `url(#${id}-s)` }, body);
    return { land, period: W };
  };
})();
