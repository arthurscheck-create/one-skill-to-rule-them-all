import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fd6ff"/><stop offset="1" stop-color="#e9f7ff"/></linearGradient></defs><rect width="1080" height="1920" fill="url(#g1)"/><g id="h-rays"></g><rect y="1060" width="1080" height="860" fill="#dff3ff"/><g id="h-cracks"></g><ellipse cx="540" cy="1190" rx="330" ry="90" fill="#0d3a66" stroke="#9fd3f5" stroke-width="10"/><g id="h-p"></g><g id="h-front"></g><g id="h-drops"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#0d3a66"/><rect width="1080" height="700" fill="#bfe6ff"/><path d="M0,700 Q270,670 540,700 T1080,700 V720 H0Z" fill="#9fd3f5"/><g id="b-p"></g><g id="b-bub"></g><g id="b-b1"></g><g id="b-b2"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#e9f7ff"/><g id="c-ice"></g><g id="c-steps"></g><g id="c-arrow"></g><g id="c-hand"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#7fc3ff"/><rect y="980" width="1080" height="940" fill="#0d3a66"/><rect x="380" y="930" width="700" height="70" fill="#f3fbff" stroke="#9fd3f5" stroke-width="8"/><g id="d-p"></g><g id="d-arr"></g><g id="d-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#1b1936"/><g id="e-clock"></g><g id="e-q"></g><g id="e-b"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#14324a"/><g id="f-cards"></g>', "1.05"),
]
JS = r'''
    /* S1 Hook: eingebrochen, hell, nah */
    K.rays($("#h-rays"), 540, 1190, 12, "#fff", .18);
    const CR = $("#h-cracks"); [[-1,-.25],[1,-.2],[-.7,.5],[.8,.6],[0,1]].forEach(([dx,dy],i)=>{ svg("path",{d:`M${540+dx*320},${1190+dy*80} l${dx*120},${dy*90+ (i%2?20:-20)} l${dx*90},${dy*70}`,fill:"none",stroke:"#7ab8e0","stroke-width":8,"stroke-linecap":"round"},CR); });
    const HP = svg("g", {}, $("#h-p")); K.person(HP, { x: 540, y: 1560, s: 1.25, face: "shock", arms: "down", shirt: "#e8463c", hair: "#5a3a1e" });
    svg("path", { d: "M210,1190 A330,90 0 0 0 870,1190 L1080,1190 L1080,1920 L0,1920 L0,1190Z", fill: "#dff3ff" }, $("#h-front"));
    svg("path", { d: "M210,1190 A330,90 0 0 0 870,1190", fill: "none", stroke: "#9fd3f5", "stroke-width": 12 }, $("#h-front"));
    E.clock(tl, (t) => HP.setAttribute("transform", `translate(${(Math.sin(t*5)*10).toFixed(1)},${(Math.abs(Math.sin(t*3.2))*-14).toFixed(1)})`));
    const DR = $("#h-drops"), drops = []; for (let i = 0; i < 10; i++) drops.push([svg("circle", { cx: 0, cy: 1150, r: 12 + (i % 3) * 4, fill: "#bfe6ff", stroke: INK, "stroke-width": 4 }, DR), i]);
    E.clock(tl, (t) => drops.forEach(([c, i]) => { const p = ((t * 1.3 + i * .17) % 1); c.setAttribute("cy", (1180 - Math.sin(p * Math.PI) * (160 + i * 12)).toFixed(1)); c.setAttribute("cx", ((i % 2 ? 780 : 300) + (i % 5) * 18 + (i % 2 ? 1 : -1) * p * 60).toFixed(1)); }));

    /* S2 Kälteschock */
    const BP = svg("g", {}, $("#b-p")); K.person(BP, { x: 540, y: 1400, s: 1.1, face: "shock", arms: "down", shirt: "#e8463c", hair: "#5a3a1e" });
    const BB = $("#b-bub"), bubs = []; for (let i = 0; i < 14; i++) bubs.push([svg("circle", { cx: 0, cy: 0, r: 10 + (i % 4) * 6, fill: "none", stroke: "#bfe6ff", "stroke-width": 5 }, BB), i]);
    const tCalm = cs("regel1", 1);
    E.clock(tl, (t) => { const sp = t < tCalm ? 2.2 : .6; bubs.forEach(([c, i]) => { const p = ((t * sp + i * .37) % 1); c.setAttribute("cx", (540 + Math.sin(i * 2.1 + t) * 120).toFixed(1)); c.setAttribute("cy", (820 - p * 260).toFixed(1)); c.setAttribute("opacity", (1 - p).toFixed(2)); }); BP.setAttribute("transform", `translate(${(t < tCalm ? Math.sin(t * 22) * 8 : 0).toFixed(1)},0)`); });
    const B1 = badge($("#b-b1"), 540, 1180, "KÄLTESCHOCK", "#3fd4ff", 66); pop(B1, cs("schock", 1), "540 1180"); K.hide(B1, at("regel1", -0.1));
    const B2 = badge($("#b-b2"), 540, 1180, "RUHIG ATMEN", "#3ee08f", 66); pop(B2, cs("regel1", 1), "540 1180");

    /* S3 Zurück zur Einbruchstelle (Draufsicht) */
    const CI = $("#c-ice"); svg("ellipse", { cx: 540, cy: 700, rx: 150, ry: 110, fill: "#0d3a66", stroke: "#9fd3f5", "stroke-width": 10 }, CI);
    for (let i = 0; i < 6; i++) svg("path", { d: `M${540 + Math.cos(i) * 150},${700 + Math.sin(i) * 110} l${Math.cos(i) * 140},${Math.sin(i) * 100}`, stroke: "#9fc8e6", "stroke-width": 6 }, CI);
    const ST = $("#c-steps"); for (let i = 0; i < 6; i++) { const s = svg("ellipse", { cx: 540 + (i % 2 ? 40 : -40), cy: 880 + i * 60, rx: 20, ry: 30, fill: "#9fc8e6" }, ST); K.fadeIn(s, cs("muskeln", 4, i * .12), .2); }
    const AR = $("#c-arrow"); svg("path", { d: "M540,1220 L540,900 M490,950 L540,890 L590,950", fill: "none", stroke: "#3ee08f", "stroke-width": 26, "stroke-linecap": "round", "stroke-linejoin": "round" }, AR); pop(AR, cs("muskeln", 5), "540 1050");
    const CH = svg("g", { transform: "translate(860,980) scale(.9)" }, $("#c-hand")); svg("rect", { x: -60, y: -60, width: 120, height: 140, rx: 40, fill: "#9fd3f5", stroke: INK, "stroke-width": 7 }, CH);
    for (let i = 0; i < 4; i++) svg("rect", { x: -58 + i * 30, y: -140, width: 26, height: 90, rx: 13, fill: "#9fd3f5", stroke: INK, "stroke-width": 6 }, CH);
    K.otxt(CH, 0, 40, "❄", 70, "#fff"); pop(CH, cs("muskeln", 3), "860 980");
    const C3 = badge($("#c-b"), 540, 1180, "DORT HIELT DAS EIS", "#3ee08f", 54); pop(C3, cs("muskeln", 7), "540 1180");

    /* S4 Rausrobben und wegrollen */
    const DP = svg("g", {}, $("#d-p")); const inner = svg("g", { transform: "rotate(-78 0 0)" }, DP); K.person(inner, { x: 0, y: 0, s: .7, face: "worried", arms: "down", shirt: "#e8463c", hair: "#5a3a1e" });
    tl.set(DP, { x: 420, y: 1010 }, 0);
    tl.to(DP, { x: 620, y: 925, duration: 1.6, ease: "power1.out" }, cs("raus", 1));
    tl.to(DP, { x: 960, duration: 1.4, ease: "none" }, cs("raus", 3)); tl.to(inner, { rotation: 282, svgOrigin: "0 -180", duration: 1.4, ease: "none" }, cs("raus", 3));
    const DA = $("#d-arr"); svg("path", { d: "M600,840 L900,840 M860,800 L910,840 L860,880", fill: "none", stroke: "#ffd23f", "stroke-width": 20, "stroke-linecap": "round", "stroke-linejoin": "round" }, DA); pop(DA, cs("raus", 3), "750 840");
    const D4 = badge($("#d-b"), 540, 1180, "ROLLEN, NICHT STEHEN", "#ffd23f", 54); pop(D4, cs("raus", 4), "540 1180");

    /* S5 Eine Stunde – trotzdem sterben die meisten früher */
    const EC = $("#e-clock"); svg("circle", { cx: 540, cy: 860, r: 250, fill: "#fff", stroke: INK, "stroke-width": 12 }, EC);
    const hand1 = svg("line", { x1: 540, y1: 860, x2: 540, y2: 660, stroke: INK, "stroke-width": 16, "stroke-linecap": "round" }, EC); svg("circle", { cx: 540, cy: 860, r: 20, fill: "#e8463c" }, EC);
    K.otxt(EC, 540, 1190, "1 STUNDE", 70, "#3fd4ff");
    E.clock(tl, (t) => hand1.setAttribute("transform", `rotate(${((t - at("stunde")) * 120).toFixed(1)} 540 860)`));
    const EQ = $("#e-q"); K.otxt(EQ, 540, 900, "?!", 260, "#ffd23f"); pop(EQ, at("verrueckt", 0), "540 820"); K.hide(EQ, at("stunde", -0.1)); tl.set(EC, { autoAlpha: 0 }, 0); tl.set(EC, { autoAlpha: 1 }, at("stunde", -0.1));
    const E5 = badge($("#e-b"), 540, 1180, "PANIK & ERSCHÖPFUNG", "#ff3b3b", 54); pop(E5, cs("stunde", 6), "540 1180");

    /* S6 1-10-1 */
    const FC = $("#f-cards"); [["1", "MINUTE", "RUHIG ATMEN", "#3fd4ff"], ["10", "MINUTEN", "RAUS AUFS EIS", "#ffd23f"], ["1", "STUNDE", "BIS ZUR OHNMACHT", "#3ee08f"]].forEach(([n, u, d, c], i) => {
      const g = svg("g", {}, FC), y = 625 + i * 205; K.panel(g, 540, y, 860, 190, "rgba(18,8,16,.94)", c);
      K.txt(g, 230, y + 40, n, 120, c); K.txt(g, 600, y - 10, u, 54, "#fff"); K.txt(g, 600, y + 52, d, 40, c); pop(g, cs("regel", 1, i * .55), `540 ${y}`); });
'''
POST = r'''    K.hudText([[at("m1", -0.2), "1 MIN"], [at("m10", -0.2), "10 MIN"], [at("stunde", -0.2), "1 STD"], [at("regel", -0.2), "1-10-1"]], "1 MIN");'''
page("17-eis-eingebrochen", S, 'INS EIS<br/><span class="r">EINGEBROCHEN</span>', "⚠ DU HAST 1 MINUTE",
     'WAS WÜRDEST <span class="y">DU</span> ZUERST TUN?', [("WILD STRAMPELN", "So schnell wie möglich raus"), ("RUHIG ATMEN", "Erst mal Luft holen"), ("UM HILFE RUFEN", "Und warten")],
     "UND FOLG MIR, BEVOR DER SEE ZUFRIERT", JS, 2, POST, css="#s1 .title.main.top{font-size:90px}")
