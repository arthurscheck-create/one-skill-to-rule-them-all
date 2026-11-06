import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<rect width="1080" height="1920" fill="#ffd23f"/><g id="a-board"></g><g id="a-p"></g><g id="a-hat"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#f4e9d0"/><rect y="1180" width="1080" height="740" fill="#c9a26a"/><g id="b-board"></g><g id="b-p"></g><g id="b-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#0d1a2a"/><g id="c-xray"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g id="d-note"></g>', "1.04"),
 ('<rect width="1080" height="1920" fill="#ff8a4a"/><rect y="760" width="1080" height="1160" fill="#a8345a" opacity=".55"/><g id="e-mesa"></g><g id="e-p"></g><g id="e-hat"></g><g id="e-b"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#3ee08f"/><g id="f-q"></g><g id="f-pile"></g><g id="f-w"></g><g id="f-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a3a6a"/><rect id="g-red" width="1080" height="1920" fill="#ff3b3b" opacity="0"/><g id="g-bank"></g><g id="g-paper"></g><g id="g-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#14183a"/><g id="h-stars"></g><circle cx="860" cy="560" r="70" fill="#fff3c0"/><rect y="1000" width="1080" height="920" fill="#c98a4a"/><g id="h-dig"></g><g id="h-b"></g>', "1.05"),
]
JS = r'''
    const R = E.rng(30);
    const hat = (g) => { const h = svg("g", {}, g); svg("path", { d: "M-100,0 C-100,-60 -90,-110 -60,-120 L60,-120 C90,-110 100,-60 100,0 Z", fill: "#1b1b22", stroke: INK, "stroke-width": 7 }, h); svg("rect", { x: -101, y: -36, width: 202, height: 26, fill: "#3a3a46" }, h); svg("ellipse", { cx: 0, cy: 2, rx: 175, ry: 28, fill: "#1b1b22", stroke: INK, "stroke-width": 7 }, h); return h; };
    const bundle = (g, x, y, w) => { const b = svg("g", {}, g); svg("rect", { x: x - w / 2, y: y - 34, width: w, height: 34, rx: 5, fill: "#7ed38a", stroke: INK, "stroke-width": 4 }, b); svg("rect", { x: x - 12, y: y - 34, width: 24, height: 34, fill: "#ffd23f" }, b); return b; };
    const board = (g, x, y, w, h, n) => { svg("rect", { x, y, width: w, height: h, rx: 10, fill: "#2e5a46", stroke: "#7a4a2a", "stroke-width": 18 }, g); ["H₂O", "NaCl", "CO₂", "E = mc²", "pH 7", "C₆H₁₂O₆", "O₂", "Fe"].slice(0, n).forEach((s, i) => K.txt(g, x + 90 + (i % 4) * (w - 180) / 3, y + 100 + Math.floor(i / 4) * 160, s, 50, "rgba(255,255,255,.75)")); };
    /* S1 Lehrer + Hut fällt auf „Heisenberg“ */
    board($("#a-board"), 60, 880, 960, 420, 8);
    const AP = svg("g", {}, $("#a-p")); K.person(AP, { x: 540, y: 1810, s: 1.5, face: "neutral", arms: "down", shirt: "#e8d68a", hair: "#6b5a4a" });
    const HW = svg("g", {}, $("#a-hat")), H1 = hat(HW), tH = cs("kata", 1);
    E.clock(tl, (t) => { const k = Math.max(0, Math.min(1, (t - tH + .25) / .35)), e = 1 - Math.pow(1 - k, 3); const x0 = 860 + Math.sin(t * 2) * 20, y0 = 1080 + Math.cos(t * 2.6) * 26, r0 = Math.sin(t * 2.2) * 14; const x = x0 + (540 - x0) * e, y = y0 + (958 - y0) * e, r = r0 * (1 - e) - 6 * e; HW.setAttribute("transform", `translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)})`); });
    tl.to(AP, { y: 0, duration: .01 }, 0);
    /* S2 Chemie-Unterricht */
    board($("#b-board"), 80, 500, 920, 520, 8); K.txt($("#b-board"), 540, 980, "CHEMIE", 54, "#ffd23f");
    const BP = svg("g", {}, $("#b-p")); K.person(BP, { x: 800, y: 1700, s: 1.15, face: "neutral", arms: "down", shirt: "#e8d68a", hair: "#6b5a4a" });
    const B2 = K.badge($("#b-b"), 400, 1150, "< 50.000 $ / JAHR", "#ff3b3b", 54); K.pop(B2, cs("m7", 3), "400 1150");
    /* S3 Röntgenbild */
    const XR = $("#c-xray"); svg("rect", { x: 190, y: 480, width: 700, height: 720, rx: 20, fill: "#5f93b8", stroke: "#c9e6ff", "stroke-width": 10 }, XR);
    svg("path", { d: "M520,560 C380,560 300,720 310,960 C320,1100 420,1130 510,1080 Z", fill: "#9cc6e4" }, XR); svg("path", { d: "M560,560 C700,560 780,720 770,960 C760,1100 660,1130 570,1080 Z", fill: "#9cc6e4" }, XR);
    for (let i = 0; i < 6; i++) { const y = 640 + i * 80; svg("path", { d: `M540,${y} C450,${y - 30} 330,${y + 10} 280,${y + 60} M540,${y} C630,${y - 30} 750,${y + 10} 800,${y + 60}`, fill: "none", stroke: "#e8f4ff", "stroke-width": 12, "stroke-linecap": "round" }, XR); }
    svg("rect", { x: 528, y: 560, width: 24, height: 560, rx: 10, fill: "#e8f4ff" }, XR);
    const SPOT = svg("g", {}, XR); svg("circle", { cx: 680, cy: 820, r: 46, fill: "#ff3b3b", opacity: .9 }, SPOT); K.pulse(SPOT, 680, 820, .45, .25); K.fadeIn(SPOT, cs("diag", 1));
    const B3 = K.badge($("#c-b"), 540, 1185, "LUNGENKREBS", "#ff3b3b", 62); K.pop(B3, cs("diag", 1), "540 1185");
    /* S4 Die Rechnung */
    const NT = $("#d-note"); svg("rect", { x: 190, y: 500, width: 700, height: 700, rx: 16, fill: "#fff3c0", stroke: INK, "stroke-width": 10 }, NT); for (let y = 640; y < 1180; y += 80) svg("line", { x1: 220, y1: y, x2: 860, y2: y, stroke: "#b8c8ff", "stroke-width": 4 }, NT);
    K.txt(NT, 540, 600, "FÜR DIE FAMILIE", 54, INK);
    ["HAUS ABBEZAHLEN", "STUDIUM KINDER", "RÜCKLAGEN"].forEach((s, k) => { const it = K.txt(NT, 540, 720 + k * 90, s, 46, "#3a3560"); K.fadeIn(it, cs("plan", 0) + k * .25, .25); });
    svg("line", { x1: 260, y1: 990, x2: 820, y2: 990, stroke: INK, "stroke-width": 8 }, NT);
    const SUM = K.otxt(NT, 540, 1100, "= 737.000 $", 96, "#e8463c"); K.pop(SUM, cs("plan", 2), "540 1070");
    /* S5 18 Uhr: Heisenberg */
    const MS = $("#e-mesa"); svg("path", { d: "M0,1150 L0,900 L120,900 L160,960 L330,960 L380,1040 L560,1040 L620,880 L820,880 L860,980 L1080,980 L1080,1150 Z", fill: "#5a1f3a" }, MS);
    const EP = svg("g", {}, $("#e-p")); K.person(EP, { x: 540, y: 1810, s: 1.5, face: "smirk", arms: "down", shirt: "#1b1b22", hair: "#6b5a4a" });
    const EH = svg("g", { transform: "translate(540,958) rotate(-6)" }, $("#e-hat")); hat(EH);
    const B5 = K.badge($("#e-b"), 540, 620, "HEISENBERG", "#ffd23f", 70); K.pop(B5, cs("m18", 3), "540 620");
    /* S6 Geldberg + Gewicht */
    const Q6 = $("#f-q"); K.otxt(Q6, 540, 860, "?!", 260, "#e8463c"); K.pop(Q6, at("verrueckt", 0), "540 780"); K.hide(Q6, at("geld", -0.1));
    const PL = $("#f-pile"); for (let r = 0; r < 9; r++) for (let c = 0; c <= r; c++) bundle(PL, 540 - r * 55 + c * 110, 800 + r * 46, 104);
    tl.set(PL, { scaleY: 0, svgOrigin: "540 1210" }, 0); tl.to(PL, { scaleY: 1, duration: 1.0, ease: "back.out(1.6)" }, at("geld", 0.2));
    const B6 = K.badge($("#f-b"), 540, 535, "80 MIO $ IN BAR", "#ffd23f", 58); K.pop(B6, cs("geld", 1), "540 535");
    const WG = svg("g", { transform: "translate(0,-62)" }, $("#f-w")); svg("path", { d: "M440,690 L640,690 L690,820 L390,820 Z", fill: "#3a3a46", stroke: INK, "stroke-width": 8, "stroke-linejoin": "round" }, WG); svg("path", { d: "M490,690 C490,630 590,630 590,690", fill: "none", stroke: INK, "stroke-width": 16 }, WG); K.txt(WG, 540, 785, "800 KG", 56, "#fff");
    K.pop(WG, cs("geld", 4), "540 750");
    /* S7 Bank meldet */
    const BK = $("#g-bank"); svg("path", { d: "M180,640 L540,480 L900,640 Z", fill: "#e8e4f5", stroke: INK, "stroke-width": 10, "stroke-linejoin": "round" }, BK); svg("rect", { x: 200, y: 640, width: 680, height: 40, fill: "#c9c3dd", stroke: INK, "stroke-width": 8 }, BK);
    for (let i = 0; i < 5; i++) svg("rect", { x: 240 + i * 130, y: 680, width: 60, height: 360, fill: "#e8e4f5", stroke: INK, "stroke-width": 6 }, BK); svg("rect", { x: 180, y: 1040, width: 720, height: 50, fill: "#c9c3dd", stroke: INK, "stroke-width": 8 }, BK); K.txt(BK, 540, 615, "BANK", 64, INK);
    const SI = svg("circle", { cx: 200, cy: 590, r: 34, fill: "#ff3b3b", stroke: INK, "stroke-width": 6 }, BK);
    E.clock(tl, (t) => { const k = t - cs("bank", 2), on = k > 0 && Math.floor(k * 4) % 2 === 0; SI.setAttribute("fill", on ? "#fff6b0" : "#ff3b3b"); document.getElementById("g-red").setAttribute("opacity", on ? .25 : 0); });
    const PP = svg("g", {}, $("#g-paper")); svg("rect", { x: -90, y: -120, width: 180, height: 240, rx: 10, fill: "#fff", stroke: INK, "stroke-width": 6 }, PP); K.txt(PP, 0, -60, "MELDUNG", 32, "#e8463c"); for (let i = 0; i < 4; i++) svg("rect", { x: -60, y: -20 + i * 30, width: 120, height: 10, rx: 5, fill: "#c9c3dd" }, PP);
    tl.set(PP, { x: 540, y: 900, autoAlpha: 0, scale: .4 }, 0); tl.to(PP, { autoAlpha: 1, x: 860, y: 560, scale: 1, rotation: 12, duration: .8, ease: "power2.out" }, cs("bank", 2));
    const B7 = K.badge($("#g-b"), 540, 1185, "> 10.000 $ = MELDUNG", "#ff3b3b", 54); K.pop(B7, cs("bank", 4), "540 1185");
    /* S8 Fässer in der Wüste */
    K.stars($("#h-stars"), 60, 300);
    const DG = $("#h-dig"); svg("ellipse", { cx: 540, cy: 1110, rx: 380, ry: 90, fill: "#7a4a2a" }, DG);
    const BAR = svg("g", {}, DG); [400, 540, 680].forEach((x) => { svg("rect", { x: x - 60, y: 900, width: 120, height: 210, rx: 14, fill: "#2a6bff", stroke: INK, "stroke-width": 7 }, BAR); svg("rect", { x: x - 64, y: 960, width: 128, height: 14, fill: "#1a4abf" }, BAR); svg("rect", { x: x - 64, y: 1040, width: 128, height: 14, fill: "#1a4abf" }, BAR); });
    tl.set(BAR, { y: 160 }, 0); tl.to(BAR, { y: 0, duration: .8, ease: "back.out(1.5)" }, at("ende", 0.3));
    svg("path", { d: "M850,1080 L900,800", stroke: "#7a4a2a", "stroke-width": 16, "stroke-linecap": "round" }, DG); svg("path", { d: "M830,1060 L870,1130 L800,1150 Z", fill: "#9aa0b5", stroke: INK, "stroke-width": 6 }, DG);
    const B8 = K.badge($("#h-b"), 540, 640, "IN DER WÜSTE", "#ffd23f", 66); K.pop(B8, cs("ende", 3), "540 640");
'''
POST = r'''    { const hl = document.querySelector("#hud .hud-label"), hn = document.querySelector("#hud .hud-num");
      document.querySelectorAll("#captions .cap").forEach((c) => { const L = Math.max(...c.textContent.split(/\s+/).map((w) => w.length)); if (L > 13) c.style.fontSize = Math.min(92, Math.floor(980 / (L * .74))) + "px"; });
      const P = [[at("m7", -0.2), "GEHALT", "< 50.000 $"], [at("diag", -0.2), "DIAGNOSE", "KREBS"], [at("plan", -0.2), "ZIEL", "737.000 $"], [at("m18", -0.2), "UHRZEIT", "18:00"],
                 [at("verrueckt", -0.2), "BARGELD", "?"], [at("geld", -0.2), "BARGELD", "80 MIO $"], [at("bank", -0.2), "MELDEGRENZE", "10.000 $"], [at("ende", -0.2), "VERSTECK", "WÜSTE"]];
      E.clock(tl, (t) => { let v = P[0]; P.forEach((p) => { if (t >= p[0]) v = p; }); hl.textContent = "⚠ " + v[1]; hn.textContent = v[2]; }); }'''
page("30-einen-tag-walter-white", S, 'EINEN TAG<br/><span class="r">WALTER WHITE</span>', "⚠ LEHRER ODER HEISENBERG?",
     'LEHRER BLEIBEN ODER <span class="y">HEISENBERG</span> WERDEN?', [("LEHRER BLEIBEN", "Sicher ist sicher"), ("HEISENBERG", "Say my name"), ("NUR SERIE GUCKEN", "Vom Sofa aus")],
     "UND FOLG MIR – SAG MEINEN NAMEN", JS, 1, POST, css="#s1 .title.main.top{font-size:86px}", flash=False)
