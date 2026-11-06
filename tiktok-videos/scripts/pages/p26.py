import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<rect width="1080" height="1920" fill="#3a4a9a"/><rect id="h-fl" width="1080" height="1920" fill="#f3f7ff" opacity="0"/><rect y="1400" width="1080" height="520" fill="#4caf50"/><g id="h-p"></g><g id="h-bolt"></g><g id="h-glow"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#14122b"/><g transform="translate(0,90)"><g id="b-p"></g><g id="b-cur"></g></g><g id="b-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a1a2a"/><g id="c-heart"></g><g id="c-ecg"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#3b2a3a"/><g id="d-arm"></g><g id="d-fern"></g><g id="d-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#1b1936"/><g id="e-q"></g><g id="e-ear"></g><g id="e-nerve"></g><g id="e-b"></g>', "1.06"),
]
JS = r'''
    const BPATH = "M560,0 L470,380 L560,380 L430,780 L520,780 L420,1160";
    /* S1 */
    const HP = svg("g", {}, $("#h-p")); K.person(HP, { x: 440, y: 1760, s: 1.35, face: "shock", arms: "down", shirt: "#e8463c" });
    const BO = svg("g", {}, $("#h-bolt")); svg("path", { d: BPATH, fill: "none", stroke: "#fff", "stroke-width": 38, "stroke-linejoin": "round" }, BO); svg("path", { d: BPATH, fill: "none", stroke: "#ffd23f", "stroke-width": 14, "stroke-linejoin": "round" }, BO);
    const GL = svg("circle", { cx: 430, cy: 1150, r: 170, fill: "#fff6b0", opacity: .5 }, $("#h-glow"));
    E.clock(tl, (t) => { const p = (t % 1.1) / 1.1, on = p < .14 || (p > .22 && p < .28); BO.style.opacity = on ? 1 : 0; GL.style.opacity = on ? .55 : 0; document.getElementById("h-fl").setAttribute("opacity", on ? .4 : 0); HP.setAttribute("transform", `translate(${on ? (Math.sin(t * 90) * 10).toFixed(1) : 0},0)`); });
    /* S2 Strom über die Haut */
    K.person($("#b-p"), { x: 540, y: 1420, s: 1.35, face: "shock", arms: "down", shirt: "#5c6390" });
    const CU = $("#b-cur"); const outline = "M540,700 C640,700 680,780 660,860 L700,880 C760,900 790,980 790,1100 L760,1300 M540,700 C440,700 400,780 420,860 L380,880 C320,900 290,980 290,1100 L320,1300 M640,1300 L640,1420 M440,1300 L440,1420";
    svg("path", { d: outline, fill: "none", stroke: "#ffd23f", "stroke-width": 14, "stroke-dasharray": "30 18", "stroke-linecap": "round" }, CU);
    E.clock(tl, (t) => CU.firstChild.setAttribute("stroke-dashoffset", (-t * 360).toFixed(1))); K.fadeIn(CU, cs("strom", 0));
    const B2 = badge($("#b-b"), 540, 600, "ÜBER DIE HAUT", "#ffd23f", 62); pop(B2, cs("strom", 1), "540 600");
    /* S3 Herz + Wiederbelebung */
    const HT = svg("g", {}, $("#c-heart")); svg("path", { d: "M540,960 C390,850 320,780 320,700 C320,630 375,585 440,585 C485,585 520,610 540,650 C560,610 595,585 640,585 C705,585 760,630 760,700 C760,780 690,850 540,960 Z", fill: "#ff3b5c", stroke: INK, "stroke-width": 10 }, HT);
    const t0 = cs("herz", 2), t1 = cs("herz", 5);
    E.clock(tl, (t) => { const stopped = t >= t0 && t < t1; const k = stopped ? 1 : 1 + Math.abs(Math.sin(t * 6)) * .08; HT.setAttribute("transform", `translate(${(540 * (1 - k)).toFixed(1)},${(770 * (1 - k)).toFixed(1)}) scale(${k.toFixed(3)})`); HT.style.opacity = stopped ? .45 : 1; });
    const EC = $("#c-ecg"); svg("rect", { x: 120, y: 1010, width: 840, height: 140, rx: 20, fill: "#0d0b18", stroke: "#3ee08f", "stroke-width": 6 }, EC);
    const line = svg("polyline", { points: "", fill: "none", stroke: "#3ee08f", "stroke-width": 7 }, EC);
    E.clock(tl, (t) => { const pts = []; for (let i = 0; i <= 80; i++) { const x = 140 + i * 10, tt = t - (80 - i) * .02, stopped = tt >= t0 && tt < t1, ph = (tt * 1.4) % 1; let y = 1080; if (!stopped && ph > .4 && ph < .5) y = 1080 - Math.sin((ph - .4) * 31.4) * 55; pts.push(`${x},${y.toFixed(1)}`); } line.setAttribute("points", pts.join(" ")); line.setAttribute("stroke", t >= t0 && t < t1 ? "#ff3b3b" : "#3ee08f"); });
    const B3 = badge($("#c-b"), 540, 1190 + 20, "SOFORT WIEDERBELEBEN", "#3ee08f", 50); pop(B3, cs("herz", 5), "540 1210");
    /* S4 Lichtenberg-Figur */
    const ARM = $("#d-arm"); svg("path", { d: "M80,1100 C200,980 420,900 640,860 C800,830 940,820 1000,780 L1040,860 C960,900 820,940 660,970 C440,1010 240,1100 140,1200 Z", fill: "#f2c29b", stroke: INK, "stroke-width": 10 }, ARM);
    const FE = $("#d-fern"); const fern = (x, y, a, len, d) => { if (d > 4 || len < 18) return; const x2 = x + Math.cos(a) * len, y2 = y + Math.sin(a) * len; const p = svg("line", { x1: x, y1: y, x2, y2, stroke: "#d0566a", "stroke-width": Math.max(2, 9 - d * 2), "stroke-linecap": "round" }, FE); fern(x2, y2, a - .5, len * .7, d + 1); fern(x2, y2, a + .5, len * .7, d + 1); fern(x2, y2, a, len * .75, d + 1); };
    fern(300, 1060, -.4, 90, 0); fern(560, 950, -.25, 80, 0);
    tl.set(FE, { autoAlpha: 0 }, 0); tl.to(FE, { autoAlpha: 1, duration: .8 }, cs("figur", 1)); tl.to(FE, { autoAlpha: .15, duration: 1.2 }, cs("figur", 5));
    const B4 = badge($("#d-b"), 540, 640, "LICHTENBERG-FIGUR", "#ff9ab0", 56); pop(B4, cs("figur", 3), "540 640");
    /* S5 Langzeitfolgen */
    const Q = $("#e-q"); K.otxt(Q, 540, 860, "?!", 260, "#ffd23f"); pop(Q, at("verrueckt", 0), "540 780"); K.hide(Q, at("folgen", -0.1));
    const EAR = svg("g", {}, $("#e-ear")); svg("path", { d: "M380,640 C240,640 220,800 280,880 C320,930 300,1000 360,1040 C420,1080 470,1010 450,960 C440,920 500,900 500,820 C500,720 460,640 380,640 Z", fill: "#f2c29b", stroke: INK, "stroke-width": 10 }, EAR);
    [0, 1, 2].forEach((i) => svg("path", { d: `M${560 + i * 50},${740 - i * 20} q40,90 0,180`, fill: "none", stroke: "#c9c3e6", "stroke-width": 10, "stroke-linecap": "round" }, EAR)); K.cross(EAR, 640, 830, 70);
    pop(EAR, cs("folgen", 1), "400 840");
    const NV = svg("g", {}, $("#e-nerve")); K.bolt(NV, 860, 640, 1.2, "#ff3b3b"); pop(NV, cs("folgen", 3), "860 800");
    const B5 = badge($("#e-b"), 540, 1190, "MANCHMAL JAHRELANG", "#ff3b3b", 54); pop(B5, cs("folgen", 4), "540 1190");
'''
page("26-blitz-trifft-dich", S, 'DER BLITZ<br/><span class="r">TRIFFT DICH</span>', "⚠ HEISSER ALS DIE SONNE",
     'WO BIST <span class="y">DU</span> BEI GEWITTER?', [("DRINNEN", "Fenster zu, fertig"), ("IM AUTO", "Faradayscher Käfig"), ("DRAUSSEN", "Mir doch egal")],
     "UND FOLG MIR, BEVOR ES DONNERT", JS, 1, "    K.hudFmt();", css="#s1 .title.main.top{font-size:96px}")
