import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<rect width="1080" height="1920" fill="#ffd23f"/><g id="a-rays"></g><g id="a-bills"></g><g id="a-coin"></g><g id="a-case"></g><g id="a-or"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#3ee08f"/><g id="b-rain"></g><g id="b-p"></g><g id="b-b"></g><g id="b-b2"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#3b3768"/><rect y="1200" width="1080" height="720" fill="#2a2650"/><g id="c-w"></g><g id="c-b"></g>', "1.04"),
 ('<rect width="1080" height="1920" fill="#ff8ad8"/><g id="d-rain"></g><g id="d-p"></g><g id="d-bub"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#2a3a6a"/><rect y="1200" width="1080" height="720" fill="#1f2b52"/><g id="e-w"></g><g id="e-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#3a1f3a"/><rect y="1200" width="1080" height="720" fill="#2a1428"/><rect id="f-red" width="1080" height="1920" fill="#ff3b3b" opacity="0"/><g id="f-w"></g><g id="f-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#14122b"/><rect y="1200" width="1080" height="720" fill="#0d0b20"/><rect id="g-fl" width="1080" height="1920" fill="#fff6b0" opacity="0"/><g id="g-w"></g><g id="g-burst"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#ffc93f"/><g id="h-rays"></g><g id="h-pile"></g><g id="h-p"></g><g id="h-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#1b1936"/><g id="i-q"></g><g id="i-bar"></g><g id="i-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g id="j-board"></g><g id="j-b"></g>', "1.04"),
]
JS = r'''
    const R = E.rng(28);
    /* Tag + Kontostand als reine Funktion der Zeit */
    const AN = [[at("t1"), 1], [at("t10"), 10], [at("t20"), 20], [at("t25"), 25], [at("t27"), 27], [cs("t28", 1), 28], [at("t30"), 30]];
    const dayAt = (t) => { if (t <= AN[0][0]) return 1; for (let i = 1; i < AN.length; i++) if (t < AN[i][0]) { const [a, da] = AN[i - 1], [b, db] = AN[i]; return Math.floor(da + (db - da) * (t - a) / (b - a)); } return 30; };
    const amt = (t) => 0.01 * Math.pow(2, dayAt(t) - 1);
    const eur = (v) => (v < 1000 ? v.toLocaleString("de-DE", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : Math.floor(v).toLocaleString("de-DE")) + " €";
    const coin = (g, x, y, r) => { const c = svg("g", {}, g); svg("circle", { cx: x, cy: y, r, fill: "#e0884a", stroke: INK, "stroke-width": Math.max(4, r * .08) }, c); svg("circle", { cx: x, cy: y, r: r * .78, fill: "none", stroke: "#b8622a", "stroke-width": Math.max(3, r * .05) }, c); return c; };
    const bill = (g, x, y, w, rot) => { const b = svg("g", { transform: `translate(${x},${y}) rotate(${rot || 0})` }, g); svg("rect", { x: -w / 2, y: -w * .24, width: w, height: w * .48, rx: 6, fill: "#7ed38a", stroke: INK, "stroke-width": 4 }, b); svg("circle", { cx: 0, cy: 0, r: w * .13, fill: "#4caf50" }, b); return b; };
    const bundle = (g, x, y, w) => { const b = svg("g", {}, g); svg("rect", { x: x - w / 2, y: y - 34, width: w, height: 34, rx: 5, fill: "#7ed38a", stroke: INK, "stroke-width": 4 }, b); svg("rect", { x: x - 12, y: y - 34, width: 24, height: 34, fill: "#ffd23f" }, b); return b; };
    /* Waage: links die Million, rechts dein Cent */
    const scale = (root) => {
      const g = svg("g", {}, root), PX = 540, PY = 660, HL = 350;
      svg("rect", { x: 522, y: PY, width: 36, height: 560, fill: "#c9c3dd", stroke: INK, "stroke-width": 6 }, g); svg("path", { d: "M400,1200 L680,1200 L620,1140 L460,1140 Z", fill: "#c9c3dd", stroke: INK, "stroke-width": 6 }, g);
      const beam = svg("g", {}, g); svg("rect", { x: PX - HL - 20, y: PY - 14, width: 2 * HL + 40, height: 28, rx: 14, fill: "#ffd23f", stroke: INK, "stroke-width": 6 }, beam); svg("circle", { cx: PX, cy: PY, r: 26, fill: "#ff3b3b", stroke: INK, "stroke-width": 6 }, g);
      const pan = (side) => { const p = svg("g", {}, g); svg("path", { d: "M0,0 L-105,200 M0,0 L105,200", stroke: INK, "stroke-width": 5 }, p); svg("path", { d: "M-130,200 L130,200 C104,250 -104,250 -130,200 Z", fill: "#c9c3dd", stroke: INK, "stroke-width": 6 }, p); const c = svg("g", {}, p); return [p, c]; };
      const [LP, LC] = pan(-1), [RP, RC] = pan(1);
      for (let i = 0; i < 5; i++) bundle(LC, 0, 198 - i * 34, 200); K.otxt(LC, 0, 0, "1 MIO", 52, "#fff");
      const ST = [svg("g", {}, RC), svg("g", {}, RC), svg("g", {}, RC), svg("g", {}, RC), svg("g", {}, RC)];
      coin(ST[0], 0, 175, 24);
      for (let i = 0; i < 4; i++) coin(ST[1], -50 + i * 34, 178 - (i % 2) * 10, 22); bill(ST[1], 10, 140, 120, -8);
      for (let i = 0; i < 3; i++) bill(ST[2], -40 + i * 40, 185 - i * 26, 150, -10 + i * 9);
      for (let i = 0; i < 3; i++) bundle(ST[3], 0, 198 - i * 34, 200);
      for (let i = 0; i < 6; i++) bundle(ST[4], -55 + (i % 2) * 110, 198 - Math.floor(i / 2) * 34, 105); for (let i = 0; i < 4; i++) bundle(ST[4], 0, 96 - i * 34, 210);
      const lab = K.otxt(RC, 0, -40, "", 40, "#ffd23f");
      E.clock(tl, (t) => {
        const a = amt(t), r = a / 1e6, ang = (r < 1 ? Math.max(-17, Math.min(-5, Math.log10(r) * 6)) : Math.min(17, Math.max(12, Math.log10(r) * 8))) * Math.PI / 180;
        beam.setAttribute("transform", `rotate(${(ang * 180 / Math.PI).toFixed(2)} ${PX} ${PY})`);
        LP.setAttribute("transform", `translate(${(PX - HL * Math.cos(ang)).toFixed(1)},${(PY - HL * Math.sin(ang)).toFixed(1)})`);
        RP.setAttribute("transform", `translate(${(PX + HL * Math.cos(ang)).toFixed(1)},${(PY + HL * Math.sin(ang)).toFixed(1)})`);
        const s = a < 1 ? 0 : a < 100 ? 1 : a < 10000 ? 2 : a < 500000 ? 3 : 4; ST.forEach((e, i) => e.style.opacity = i === s ? 1 : 0);
        lab.textContent = eur(a); lab.setAttribute("y", [130, 100, 90, 70, -20][s]);
      });
      return g;
    };
    /* S1 Münze vs. Koffer */
    K.rays($("#a-rays"), 540, 1080, 16, "#fff", .25);
    const BI = $("#a-bills"), FLY = []; for (let i = 0; i < 14; i++) FLY.push([bill(svg("g", {}, BI), 0, 0, 110, 0), R() * 6, 560 + R() * 480]);
    E.clock(tl, (t) => FLY.forEach(([b, p, x]) => { const y = 1900 - ((t * 260 + p * 300) % 1100); b.parentNode.setAttribute("transform", `translate(${(x + Math.sin(t * 2 + p) * 40).toFixed(1)},${(y - 1200).toFixed(1)}) rotate(${(t * 60 + p * 50).toFixed(1)} 0 1200)`); }));
    const CW = svg("g", {}, $("#a-coin")), CI = svg("g", {}, CW); coin(CI, 300, 1110, 190); K.otxt(CI, 300, 1160, "1", 165, "#fff3c0"); K.txt(CI, 300, 1218, "CENT", 40, "#7a3a1a");
    E.clock(tl, (t) => { const k = Math.max(.08, Math.abs(Math.cos(t * 2.6))); CI.setAttribute("transform", `translate(${(300 * (1 - k)).toFixed(1)},0) scale(${k.toFixed(3)},1)`); });
    const CA = svg("g", {}, $("#a-case")); svg("rect", { x: 600, y: 960, width: 400, height: 280, rx: 24, fill: "#5c3a1a", stroke: INK, "stroke-width": 10 }, CA); svg("rect", { x: 740, y: 920, width: 120, height: 50, rx: 14, fill: "none", stroke: INK, "stroke-width": 12 }, CA);
    for (let i = 0; i < 4; i++) bundle(CA, 800, 1220 - i * 36, 330); K.otxt(CA, 800, 1060, "1.000.000 €", 56, "#fff");
    const CAW = svg("g", {}, $("#a-case")); CAW.appendChild(CA); K.bob(CAW, 10, 2.4);
    K.otxt($("#a-or"), 545, 1080, "?", 130, "#e8463c");
    /* S2 Fast jeder nimmt die Million */
    const RN = $("#b-rain"), RB = []; for (let i = 0; i < 18; i++) { const w = svg("g", {}, RN); bill(w, 0, 0, 100, R() * 90); RB.push([w, R() * 1080, R() * 8]); }
    E.clock(tl, (t) => RB.forEach(([w, x, p]) => w.setAttribute("transform", `translate(${(x + Math.sin(t + p) * 30).toFixed(1)},${(((t * 300 + p * 260) % 1700) + 300).toFixed(1)})`)));
    const BP = svg("g", {}, $("#b-p")); K.person(BP, { x: 540, y: 1820, s: 1.55, face: "smirk", arms: "bag", shirt: "#ffd23f" });
    const B2 = K.badge($("#b-b"), 540, 560, "1.000.000 € SOFORT", "#ffd23f", 56); K.pop(B2, cs("wahl", 1), "540 560");
    const B2b = K.badge($("#b-b2"), 540, 1180, "LOGISCH?", "#ff3b3b", 60); K.pop(B2b, cs("wahl", 2), "540 1180");
    /* S3/S5/S6/S7 Waage */
    scale($("#c-w")); scale($("#e-w")); scale($("#f-w")); scale($("#g-w"));
    const B5 = K.badge($("#e-b"), 540, 1180, "LÄCHERLICH", "#ff3b3b", 60); K.pop(B5, cs("t20", 3), "540 1180"); K.hide(B5, at("t25", -0.1));
    const B6 = K.badge($("#f-b"), 540, 1180, "IMMER NOCH HINTEN", "#ff3b3b", 56); K.pop(B6, cs("t27", 2), "540 1180");
    E.clock(tl, (t) => { const k = t - at("t27"); document.getElementById("f-red").setAttribute("opacity", k > 0 ? (Math.abs(Math.sin(k * 3.2)) * .18).toFixed(3) : 0); });
    const GB = K.burst($("#g-burst"), 540, 1060, 170, "ÜBERHOLT!", "#3ee08f"); K.pop(GB, cs("t28", 2), "540 1060");
    tl.to("#g-fl", { attr: { opacity: .7 }, duration: .08 }, cs("t28", 1)); tl.to("#g-fl", { attr: { opacity: 0 }, duration: .5 }, cs("t28", 1) + .08);
    /* S4 Freund lacht */
    const DR = $("#d-rain"); for (let i = 0; i < 10; i++) bill(DR, 80 + R() * 920, 500 + R() * 700, 110, R() * 90);
    const DP = svg("g", {}, $("#d-p")); K.person(DP, { x: 540, y: 1900, s: 1.75, face: "smirk", arms: "bag", shirt: "#ffd23f" }); const DPW = svg("g", {}, $("#d-p")); DPW.appendChild(DP); K.bob(DPW, 9, 14);
    const BU = $("#d-bub"); svg("rect", { x: 610, y: 480, width: 380, height: 170, rx: 50, fill: "#fff", stroke: INK, "stroke-width": 8 }, BU); svg("path", { d: "M690,640 L660,730 L760,645 Z", fill: "#fff", stroke: INK, "stroke-width": 8, "stroke-linejoin": "round" }, BU); K.txt(BU, 800, 595, "HAHA!", 90, "#e8463c");
    K.pop(BU, cs("spott", 2), "800 600");
    /* S8 Geldberg */
    K.rays($("#h-rays"), 540, 900, 16, "#fff", .22);
    const PL = $("#h-pile"); for (let r = 0; r < 9; r++) for (let c = 0; c <= r; c++) bundle(PL, 540 - r * 55 + c * 110, 760 + r * 50, 104);
    tl.set(PL, { scaleY: 0, svgOrigin: "540 1210" }, 0); tl.to(PL, { scaleY: 1, duration: 1.2, ease: "back.out(1.6)" }, at("t30", 0));
    const HP = svg("g", {}, $("#h-p")); K.person(HP, { x: 140, y: 1500, s: .75, face: "shock", arms: "bag", shirt: "#ffd23f" });
    const B8 = K.badge($("#h-b"), 540, 560, "5.368.709 €", "#3ee08f", 76); K.pop(B8, cs("t30", 1), "540 560");
    /* S9 Hälfte am letzten Tag */
    const Q9 = $("#i-q"); K.otxt(Q9, 540, 860, "?!", 260, "#e8463c"); K.pop(Q9, at("verrueckt", 0), "540 780"); K.hide(Q9, at("haelfte", -0.1));
    const BR = $("#i-bar"); svg("rect", { x: 90, y: 760, width: 450, height: 260, fill: "#5c5890", stroke: INK, "stroke-width": 8 }, BR); svg("rect", { x: 540, y: 760, width: 450, height: 260, fill: "#ffd23f", stroke: INK, "stroke-width": 8 }, BR);
    K.otxt(BR, 315, 880, "TAG 1–29", 58, "#fff"); K.otxt(BR, 315, 950, "2,68 MIO €", 44, "#c9c3dd"); K.otxt(BR, 765, 880, "TAG 30", 64, "#e8463c"); K.otxt(BR, 765, 950, "2,68 MIO €", 44, "#fff");
    tl.set(BR, { autoAlpha: 0 }, 0); tl.fromTo(BR, { autoAlpha: 1, scaleX: 0, svgOrigin: "540 890" }, { scaleX: 1, duration: .5, ease: "power2.out", immediateRender: false }, at("haelfte", 0));
    const B9 = K.badge($("#i-b"), 540, 600, "50 % AM LETZTEN TAG", "#ffd23f", 58); K.pop(B9, cs("haelfte", 3), "540 600");
    /* S10 Schachbrett: 64 Tage */
    const BD = $("#j-board"), SQS = []; for (let r = 0; r < 8; r++) for (let c = 0; c < 8; c++) { const i = r * 8 + (r % 2 ? 7 - c : c); SQS[i] = svg("rect", { x: 220 + c * 80, y: 1040 - r * 80, width: 80, height: 80, fill: (r + c) % 2 ? "#5c5890" : "#e8e4f5", stroke: INK, "stroke-width": 3 }, BD); }
    svg("rect", { x: 220, y: 480, width: 640, height: 640, fill: "none", stroke: INK, "stroke-width": 10 }, BD);
    const t0 = at("schach", 0.2);
    E.clock(tl, (t) => { const n = Math.floor(Math.max(0, Math.min(64, (t - t0) / 2.6 * 64))); SQS.forEach((s, i) => s.style.fill = i < n ? (i === 63 ? "#ff3b3b" : "#ffd23f") : ""); });
    const BJ = K.badge($("#j-b"), 540, 1190, "760 × ALLES GELD DER WELT", "#ff3b3b", 46); K.pop(BJ, cs("schach", 4), "540 1190");
'''
POST = r'''    { const hl = document.querySelector("#hud .hud-label"), hn = document.querySelector("#hud .hud-num"), t64 = at("schach", 0.2);
      document.querySelectorAll("#captions .cap").forEach((c) => { const L = Math.max(...c.textContent.split(/\s+/).map((w) => w.length)); if (L > 13) c.style.fontSize = Math.min(92, Math.floor(980 / (L * .74))) + "px"; });
      E.clock(tl, (t) => { if (t >= t64) { hl.textContent = "⚠ TAG 64"; hn.textContent = "92 BRD. €"; return; } hl.textContent = "⚠ TAG " + dayAt(t) + " / 30"; hn.textContent = eur(amt(t)); }); }'''
page("28-cent-oder-million", S, '1 MILLION<br/>ODER <span class="r">1 CENT?</span>', "⚠ VERDOPPELT SICH JEDEN TAG",
     'WAS HÄTTEST <span class="y">DU</span> GENOMMEN?', [("DIE MILLION", "Sicher ist sicher"), ("DEN CENT", "Geduld zahlt sich aus"), ("BEIDES", "Ich will alles")],
     "UND FOLG MIR – KOSTET DICH KEINEN CENT", JS, False, POST)
