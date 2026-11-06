import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
DEFS = '<defs><pattern id="pst" width="44" height="44" patternUnits="userSpaceOnUse"><rect width="44" height="44" fill="#d6d9e2"/><rect width="20" height="44" fill="#4a5a7a"/></pattern></defs>'
S = [
 ('<rect width="1080" height="1920" fill="#f2e2b8"/><g id="a-forest"></g><g id="a-leaves"></g><g id="a-p"></g><g id="a-book"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#c9d3c0"/><rect y="1150" width="1080" height="770" fill="#7a8a5a"/><g id="b-forest"></g><g id="b-truck"></g><g id="b-p"></g><g id="b-book"></g><g id="b-b"></g>', "1.04"),
 ('<rect width="1080" height="1920" fill="#d8cfb8"/><rect x="640" y="520" width="300" height="380" fill="#a8c8e0" stroke="#5c4a3a" stroke-width="18"/><rect y="1260" width="1080" height="660" fill="#7a5a3a"/><g id="c-p"></g><g id="c-cap"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g id="d-note"></g><g id="d-b"></g>', "1.04"),
 ('<rect width="1080" height="1920" fill="#e8dcc0"/><g id="e-tree"></g><g id="e-k"></g><g id="e-kcap"></g><g id="e-r"></g><g id="e-bub"></g>', "1.04"),
 ('<rect width="1080" height="1920" fill="#3a2a2a"/><g id="f-p"></g><g id="f-sw"></g><g id="f-b"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#3b3768"/><g id="g-book"></g><g id="g-b"></g>', "1.04"),
 ('<rect width="1080" height="1920" fill="#1b1414"/><g id="h-files"></g><g id="h-fire"></g><g id="h-num"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#0f0e1f"/><g id="i-cand"></g><g id="i-b"></g>', "1.03"),
]
JS = r'''
    let PN = 0; const PRS = (g) => { const id = "pst" + (++PN), sv = g.ownerSVGElement || g; let d = sv.querySelector("defs"); if (!d) d = svg("defs", {}, sv); const pt = svg("pattern", { id, width: 44, height: 44, patternUnits: "userSpaceOnUse" }, d); svg("rect", { width: 44, height: 44, fill: "#d6d9e2" }, pt); svg("rect", { width: 20, height: 44, fill: "#4a5a7a" }, pt); return { shirt: `url(#${id})`, pants: `url(#${id})`, hair: "#2a1a10" }; };
    const R = E.rng(31), OF = { shirt: "#5f6b52", pants: "#4a5440", hair: "#c9a86a" };
    const cap = (g, x, y, s) => { const c = svg("g", { transform: `translate(${x},${y}) scale(${s})` }, g); svg("path", { d: "M-125,-40 C-130,-110 130,-110 125,-40 Z", fill: "#5f6b52", stroke: INK, "stroke-width": 7 }, c); svg("rect", { x: -112, y: -48, width: 224, height: 34, rx: 6, fill: "#2a2a2a", stroke: INK, "stroke-width": 6 }, c); svg("path", { d: "M-100,-14 C-60,22 60,22 100,-14 Z", fill: "#1b1b1b", stroke: INK, "stroke-width": 6 }, c); return c; };
    const book = (g, x, y, s) => { const b = svg("g", { transform: `translate(${x},${y}) scale(${s})` }, g); svg("rect", { x: -90, y: -120, width: 180, height: 240, rx: 10, fill: "#8a2a2a", stroke: INK, "stroke-width": 7 }, b); svg("rect", { x: -70, y: -100, width: 140, height: 200, rx: 6, fill: "none", stroke: "#e8c06a", "stroke-width": 6 }, b); svg("circle", { cx: 0, cy: 0, r: 38, fill: "none", stroke: "#e8c06a", "stroke-width": 6 }, b); svg("path", { d: "M-40,-60 q20,-20 40,0 t40,0", fill: "none", stroke: "#e8c06a", "stroke-width": 5 }, b); return b; };
    const forest = (g, y, c) => { for (let i = 0; i < 14; i++) { const x = i * 82 - 20 + R() * 30, h = 260 + R() * 220; svg("path", { d: `M${x},${y} L${x + 50},${y - h} L${x + 100},${y} Z`, fill: c }, g); } };
    /* S1 Nahaufnahme Reza + Buch */
    forest($("#a-forest"), 1250, "#8a9a6a");
    const LV = $("#a-leaves"), LS = []; for (let i = 0; i < 16; i++) LS.push([svg("ellipse", { rx: 16, ry: 8, fill: i % 2 ? "#c98a3a" : "#a8b04a" }, LV), R() * 1080, R() * 9]);
    E.clock(tl, (t) => LS.forEach(([l, x, p]) => { const y = ((t * 120 + p * 220) % 1500) + 380; l.setAttribute("cx", (x + Math.sin(t * 1.5 + p) * 50).toFixed(1)); l.setAttribute("cy", y.toFixed(1)); l.setAttribute("transform", `rotate(${(t * 80 + p * 40).toFixed(1)} ${(x + Math.sin(t * 1.5 + p) * 50).toFixed(1)} ${y.toFixed(1)})`); }));
    const AP = svg("g", {}, $("#a-p")); K.person(AP, Object.assign({ x: 470, y: 1810, s: 1.5, face: "worried", arms: "down" }, PRS(AP)));
    const AB = svg("g", {}, $("#a-book")); book(AB, 0, 0, 1.15); E.clock(tl, (t) => AB.setAttribute("transform", `translate(${(860 + Math.sin(t * 1.3) * 14).toFixed(1)},${(1060 + Math.cos(t * 1.7) * 20).toFixed(1)}) rotate(${(Math.sin(t * 1.1) * 8).toFixed(1)})`));
    /* S2 Die Lüge */
    forest($("#b-forest"), 1150, "#5a6a4a");
    const TR = $("#b-truck"); svg("rect", { x: -40, y: 860, width: 380, height: 220, rx: 14, fill: "#4a5440", stroke: INK, "stroke-width": 8 }, TR); svg("rect", { x: 330, y: 930, width: 130, height: 150, rx: 14, fill: "#3a4430", stroke: INK, "stroke-width": 8 }, TR); [60, 380].forEach((x) => svg("circle", { cx: x, cy: 1090, r: 46, fill: "#1b1b1b", stroke: INK, "stroke-width": 6 }, TR));
    const BP = svg("g", {}, $("#b-p")); K.person(BP, Object.assign({ x: 700, y: 1700, s: 1.2, face: "worried", arms: "down" }, PRS(BP)));
    const BB = svg("g", {}, $("#b-book")); book(BB, 880, 900, .8); K.pop(BB, cs("luege", 2), "880 900");
    const B2 = K.badge($("#b-b"), 540, 560, "„ICH BIN PERSER!“", "#ffd23f", 58); K.pop(B2, cs("luege", 2), "540 560");
    /* S3 Der Offizier */
    const CP = svg("g", {}, $("#c-p")); K.person(CP, Object.assign({ x: 420, y: 1810, s: 1.5, face: "neutral", arms: "down" }, OF));
    cap($("#c-cap"), 420, 1005, 1.05);
    const B3 = K.badge($("#c-b"), 540, 560, "PERSISCH-UNTERRICHT", "#ffd23f", 54); K.pop(B3, cs("koch", 2), "540 560");
    /* S4 Kein Wort – also erfinden */
    const NT = $("#d-note"); svg("rect", { x: 190, y: 500, width: 700, height: 680, rx: 16, fill: "#fff3c0", stroke: INK, "stroke-width": 10 }, NT); K.txt(NT, 540, 590, "VOKABELN", 60, INK);
    const W = ["BAUM", "BROT", "HAUS", "WASSER", "HIMMEL"], tE = at("erfinden", 0.3);
    W.forEach((w, i) => { const y = 690 + i * 100; K.txt(NT, 380, y, w + " =", 50, "#3a3560"); const q = K.txt(NT, 700, y, "???", 54, "#e8463c"); const sq = svg("path", { d: `M620,${y - 14} q20,-24 40,0 t40,0 t40,0`, fill: "none", stroke: "#2a6bff", "stroke-width": 8, "stroke-linecap": "round" }, NT);
      tl.set(sq, { autoAlpha: 0 }, 0); tl.set(q, { autoAlpha: 0 }, tE + i * .3); tl.set(sq, { autoAlpha: 1 }, tE + i * .3); });
    const B4 = K.badge($("#d-b"), 540, 1185, "KEIN EINZIGES WORT", "#ff3b3b", 58); K.pop(B4, cs("problem", 2), "540 1185"); K.hide(B4, at("erfinden", 0));
    /* S5 Was heißt Baum? – Radj. */
    const TE = $("#e-tree"); svg("rect", { x: 520, y: 900, width: 40, height: 300, fill: "#7a4a2a" }, TE); [[540, 820, 130], [470, 900, 100], [610, 900, 100]].forEach(([x, y, r]) => svg("circle", { cx: x, cy: y, r, fill: "#4caf50", stroke: INK, "stroke-width": 6 }, TE));
    const EK = svg("g", {}, $("#e-k")); K.person(EK, Object.assign({ x: 230, y: 1900, s: 1.3, face: "neutral", arms: "down" }, OF)); cap($("#e-kcap"), 230, 1150, .92);
    const ER = svg("g", {}, $("#e-r")); K.person(ER, Object.assign({ x: 850, y: 1900, s: 1.3, face: "worried", arms: "down" }, PRS(ER)));
    const BU = $("#e-bub"); const bub = (x, y, w, txt, col, tail) => { const b = svg("g", {}, BU); svg("rect", { x: x - w / 2, y: y - 70, width: w, height: 140, rx: 46, fill: "#fff", stroke: INK, "stroke-width": 8 }, b); svg("path", { d: tail, fill: "#fff", stroke: INK, "stroke-width": 8, "stroke-linejoin": "round" }, b); K.txt(b, x, y + 22, txt, 62, col); return b; };
    const Q1 = bub(420, 560, 700, "WAS HEISST BAUM?", INK, "M240,628 L210,720 L300,630 Z"); K.pop(Q1, cs("baum", 1), "420 560");
    const Q2 = bub(800, 760, 300, "RADJ.", "#e8463c", "M860,828 L900,900 L820,830 Z"); K.pop(Q2, cs("baum", 3), "800 760");
    /* S6 Gefahr */
    const FP = svg("g", {}, $("#f-p")); K.person(FP, Object.assign({ x: 540, y: 1800, s: 1.55, face: "worried", arms: "down" }, PRS(FP)));
    const SW = svg("path", { d: "M700,960 C690,990 690,1010 705,1015 C720,1010 718,990 700,960 Z", fill: "#8fd8ff", stroke: INK, "stroke-width": 4 }, $("#f-sw"));
    E.clock(tl, (t) => SW.setAttribute("transform", `translate(0,${(((t - at("gefahr")) * 60) % 90).toFixed(1)})`));
    const B6 = K.badge($("#f-b"), 540, 580, "EIN FEHLER = ENTTARNT", "#ff3b3b", 56); K.pop(B6, cs("gefahr", 3), "540 580");
    /* S7 Lagerbuch: Wörter aus Namen */
    const GB = $("#g-book"); svg("rect", { x: 120, y: 520, width: 840, height: 640, rx: 16, fill: "#5c3a1a", stroke: INK, "stroke-width": 10 }, GB); svg("rect", { x: 150, y: 545, width: 380, height: 590, fill: "#f6ecd2" }, GB); svg("rect", { x: 550, y: 545, width: 380, height: 590, fill: "#f6ecd2" }, GB); svg("line", { x1: 540, y1: 545, x2: 540, y2: 1135, stroke: "#c9b58a", "stroke-width": 6 }, GB);
    const HL = [];
    [180, 580].forEach((x0) => { for (let i = 0; i < 11; i++) { const y = 590 + i * 50, w = 200 + R() * 110; let d = `M${x0},${y}`; for (let k = 0; k < w; k += 18) d += ` q9,${-10 - R() * 8} 18,0`; const hl = svg("rect", { x: x0 + 20, y: y - 22, width: 70, height: 30, rx: 6, fill: "#ffd23f", opacity: 0 }, GB); HL.push(hl); svg("path", { d, fill: "none", stroke: "#3a3560", "stroke-width": 4 }, GB); } });
    E.clock(tl, (t) => { const n = Math.floor(Math.max(0, (t - at("trick", 0.8)) * 6)); HL.forEach((h, i) => h.setAttribute("opacity", i < n ? .65 : 0)); });
    const B7 = K.badge($("#g-b"), 540, 1185, "WÖRTER AUS NAMEN", "#ffd23f", 58); K.pop(B7, cs("trick", 2), "540 1185");
    /* S8 Akten brennen – 2.840 Namen */
    const FI = $("#h-files"); for (let i = 0; i < 6; i++) svg("rect", { x: 300 + (i % 3) * 30, y: 1060 - i * 40, width: 480, height: 40, rx: 4, fill: i % 2 ? "#e8dcc0" : "#d6c8a0", stroke: INK, "stroke-width": 4 }, FI);
    const FL = $("#h-fire"), FLS = []; for (let i = 0; i < 9; i++) FLS.push([svg("path", { fill: i % 2 ? "#ff8a3a" : "#ffd23f", opacity: .9 }, FL), 330 + i * 52, R() * 7]);
    E.clock(tl, (t) => FLS.forEach(([f, x, p]) => { const h = 120 + Math.abs(Math.sin(t * 6 + p)) * 110; f.setAttribute("d", `M${x - 34},${880} Q${x - 30},${880 - h * .6} ${x + Math.sin(t * 5 + p) * 14},${880 - h} Q${x + 30},${880 - h * .6} ${x + 34},${880} Z`); }));
    tl.set(FL, { autoAlpha: 0 }, 0); tl.to(FL, { autoAlpha: 1, duration: .4 }, cs("ende", 1));
    const NUM = $("#h-num"); svg("rect", { x: 0, y: 0, width: 1080, height: 1920, fill: "#0d0b18", opacity: .7 }, NUM); K.otxt(NUM, 540, 900, "2.840", 220, "#ffd23f"); K.otxt(NUM, 540, 1020, "NAMEN IM KOPF", 70, "#fff"); K.fadeIn(NUM, cs("ende", 3), .5);
    /* S9 Erinnerung: Kerzen */
    const CA = $("#i-cand"), CS = []; for (let r = 0; r < 6; r++) for (let c = 0; c < 9; c++) { const x = 140 + c * 100 + (r % 2) * 50, y = 720 + r * 80; const g = svg("g", {}, CA); svg("rect", { x: x - 10, y, width: 20, height: 44, rx: 4, fill: "#f6ecd2" }, g); const fl = svg("ellipse", { cx: x, cy: y - 12, rx: 8, ry: 16, fill: "#ffd23f" }, g); CS.push([g, fl, r * 9 + c]); }
    E.clock(tl, (t) => CS.forEach(([g, fl, i]) => { const on = t > at("mahn", 0) + i * .03; g.style.opacity = on ? 1 : 0; fl.setAttribute("ry", (14 + Math.sin(t * 9 + i) * 3).toFixed(1)); }));
    const B9 = K.badge($("#i-b"), 540, 600, "NIEMALS VERGESSEN", "#ffd23f", 62); K.pop(B9, cs("mahn", 1), "540 600");
'''
POST = r'''    { const hl = document.querySelector("#hud .hud-label"), hn = document.querySelector("#hud .hud-num");
      document.querySelectorAll("#captions .cap").forEach((c) => { const L = Math.max(...c.textContent.split(/\s+/).map((w) => w.length)); if (L > 13) c.style.fontSize = Math.min(92, Math.floor(980 / (L * .74))) + "px"; });
      const a1 = at("erfinden"), a2 = at("gefahr"), a3 = at("trick", 0.8), a4 = at("wende"), a5 = cs("ende", 3);
      E.clock(tl, (t) => { let n; if (t < a1) n = 0; else if (t < a2) n = Math.round(40 * Math.min(1, (t - a1) / (a2 - a1))); else if (t < a3) n = 40; else if (t < a4) n = Math.round(40 + 1460 * Math.min(1, (t - a3) / (a4 - a3))); else n = t < a5 ? 1500 : 2840;
        hl.textContent = t >= a5 ? "⚠ NAMEN IM KOPF" : "⚠ ERFUNDENE WÖRTER"; hn.textContent = n.toLocaleString("de-DE"); }); }'''
page("31-einen-tag-reza", S, 'EINEN TAG<br/>LANG <span class="r">REZA</span>', "⚠ NACH DEM FILM „PERSISCHSTUNDEN“",
     'KANNTEST <span class="y">DU</span> DIESEN FILM?', [],
     "UND FOLG MIR FÜR MEHR GESCHICHTEN WIE DIESE", JS, False, POST, cta1="SCHREIB ES IN DIE KOMMENTARE")
