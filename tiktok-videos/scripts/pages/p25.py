import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a5cff"/><stop offset="1" stop-color="#3fd4ff"/></linearGradient></defs><rect width="1080" height="1920" fill="url(#g1)"/><g id="h-rays"></g><g id="h-ph"></g><g id="h-not"></g><g id="h-x"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g id="b-p"></g><g id="b-vib"></g><g id="b-home"></g><g id="b-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#3b3768"/><g id="c-clock"></g><g id="c-p"></g><g id="c-bulb"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#14324a"/><g id="d-target"></g><g id="d-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#1b1936"/><g id="e-bed"></g><g id="e-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g id="f-q"></g><g id="f-ppl"></g><g id="f-b"></g>', "1.06"),
]
JS = r'''
    const phone = (g, x, y, s) => { const p = svg("g", { transform: `translate(${x},${y}) scale(${s})` }, g); svg("rect", { x: -150, y: -280, width: 300, height: 560, rx: 46, fill: "#1b1936", stroke: INK, "stroke-width": 12 }, p); svg("rect", { x: -125, y: -240, width: 250, height: 470, rx: 20, fill: "#3fd4ff" }, p); svg("rect", { x: -40, y: -265, width: 80, height: 12, rx: 6, fill: "#3a3560" }, p); return p; };
    /* S1 */
    K.rays($("#h-rays"), 540, 1150, 12, "#fff", .15);
    phone($("#h-ph"), 540, 1290, 1.15);
    const NT = $("#h-not"), nots = []; [["#ff3b5c", "99+"], ["#3ee08f", "12"], ["#ffd23f", "7"]].forEach(([c, n], i) => { const g = svg("g", {}, NT); K.panel(g, 0, 0, 130, 80, c, INK); K.txt(g, 0, 18, n, 46, "#fff"); nots.push([g, i]); });
    E.clock(tl, (t) => nots.forEach(([g, i]) => g.setAttribute("transform", `translate(${[230, 860, 850][i]},${([1060, 1180, 1460][i] + Math.sin(t * 3 + i) * 14).toFixed(1)})`)));
    const HX = K.cross($("#h-x"), 540, 1290, 240); K.pulse(HX, 540, 1290, .8, .05);
    /* S2 Griff in die Tasche */
    const BP = svg("g", {}, $("#b-p")); K.person(BP, { x: 420, y: 1380, s: 1.15, face: "worried", arms: "down", shirt: "#3fd4ff" });
    const VB = $("#b-vib"); [0, 1, 2].forEach((i) => svg("path", { d: `M${590 + i * 30},${1000 - i * 20} q20,40 0,80`, fill: "none", stroke: "#ffd23f", "stroke-width": 10, "stroke-linecap": "round" }, VB));
    tl.set(VB, { autoAlpha: 0 }, 0); tl.to(VB, { autoAlpha: 1, duration: .08, repeat: 9, yoyo: true }, cs("griff", 3));
    const HM = svg("g", {}, $("#b-home")); svg("path", { d: "M760,700 L900,590 L1040,700 L1040,860 L760,860 Z", fill: "#e8463c", stroke: INK, "stroke-width": 8 }, HM); svg("rect", { x: 860, y: 760, width: 80, height: 100, fill: "#1b1936" }, HM); phone(HM, 900, 660, .18);
    pop(HM, cs("griff", 4), "900 760");
    const B2 = badge($("#b-b"), 540, 1190 - 40, "PHANTOM-VIBRATION", "#ffd23f", 54); pop(B2, cs("griff", 3), "540 1150");
    /* S3 Langeweile -> Nachdenken */
    const CL = $("#c-clock"); svg("circle", { cx: 800, cy: 680, r: 120, fill: "#fff", stroke: INK, "stroke-width": 10 }, CL); const hd = svg("line", { x1: 800, y1: 680, x2: 800, y2: 590, stroke: INK, "stroke-width": 12, "stroke-linecap": "round" }, CL);
    E.clock(tl, (t) => hd.setAttribute("transform", `rotate(${(t * 90).toFixed(1)} 800 680)`));
    K.person($("#c-p"), { x: 380, y: 1380, s: 1.1, face: "neutral", arms: "down", shirt: "#ff8a5c" });
    const BU = svg("g", {}, $("#c-bulb")); svg("circle", { cx: 380, cy: 640, r: 90, fill: "#ffd23f", stroke: INK, "stroke-width": 9 }, BU); svg("rect", { x: 345, y: 720, width: 70, height: 60, rx: 10, fill: "#c9ced8", stroke: INK, "stroke-width": 7 }, BU);
    pop(BU, cs("leer", 4), "380 680");
    const B3 = badge($("#c-b"), 540, 1190 - 40, "LANGEWEILE", "#c9c3e6", 62); pop(B3, cs("leer", 1), "540 1150");
    /* S4 Konzentration */
    const TG = svg("g", {}, $("#d-target")); [220, 160, 100, 45].forEach((r, i) => svg("circle", { cx: 540, cy: 860, r, fill: i % 2 ? "#fff" : "#e8463c", stroke: INK, "stroke-width": 8 }, TG));
    const AR = svg("g", {}, TG); svg("path", { d: "M900,500 L560,840", stroke: INK, "stroke-width": 18, "stroke-linecap": "round" }, AR); svg("path", { d: "M900,500 l-10,70 l60,-60 Z", fill: "#3ee08f", stroke: INK, "stroke-width": 6 }, AR);
    tl.set(AR, { x: 300, y: -300, autoAlpha: 0 }, 0); tl.to(AR, { x: 0, y: 0, autoAlpha: 1, duration: .4, ease: "power3.in" }, cs("studie", 6));
    K.fadeIn(TG, at("studie", 0));
    const B4 = badge($("#d-b"), 540, 1190, "NUR 2 WOCHEN", "#3ee08f", 62); pop(B4, cs("studie", 4), "540 1190");
    /* S5 Schlaf */
    const BD = svg("g", {}, $("#e-bed")); svg("rect", { x: 200, y: 900, width: 680, height: 160, rx: 30, fill: "#7a5cff", stroke: INK, "stroke-width": 10 }, BD); svg("rect", { x: 230, y: 860, width: 170, height: 80, rx: 30, fill: "#fff", stroke: INK, "stroke-width": 8 }, BD);
    svg("rect", { x: 200, y: 1060, width: 30, height: 80, fill: INK }, BD); svg("rect", { x: 850, y: 1060, width: 30, height: 80, fill: INK }, BD); K.otxt(BD, 700, 780, "ZZZ", 80, "#c9c3e6");
    svg("path", { d: "M900,600 A110,110 0 1 1 790,490 A80,80 0 1 0 900,600 Z", fill: "#ffd23f", stroke: INK, "stroke-width": 8 }, BD);
    K.fadeIn(BD, at("w3", 0));
    const B5 = badge($("#e-b"), 540, 1190 - 20, "−20 % SCHLAFPROBLEME", "#3fd4ff", 52); pop(B5, cs("schlaf", 2), "540 1170");
    /* S6 Ein Drittel gibt auf */
    const Q = $("#f-q"); K.otxt(Q, 540, 860, "?!", 260, "#ffd23f"); pop(Q, at("verrueckt", 0), "540 780"); K.hide(Q, at("aufgeben", -0.1));
    const PP = $("#f-ppl"); [["happy", "#3ee08f"], ["happy", "#3ee08f"], ["shock", "#e8463c"]].forEach(([f, c], i) => { const g = svg("g", {}, PP); K.person(g, { x: 220 + i * 320, y: 1150, s: .8, face: f, arms: i === 2 ? "phone" : "down", shirt: c }); pop(g, at("aufgeben", i * .15), `${220 + i * 320} 950`); });
    const B6 = badge($("#f-b"), 540, 600, "1 VON 3 GIBT AUF", "#ff3b3b", 60); pop(B6, cs("aufgeben", 2), "540 600");
'''
POST = r'''    K.hudText([[at("t1", -0.2), "TAG 1"], [at("t3", -0.2), "TAG 3"], [at("w2", -0.2), "TAG 14"], [at("w3", -0.2), "TAG 21"]], "TAG 1");'''
page("25-ohne-handy", S, '30 TAGE<br/><span class="r">KEIN HANDY</span>', "⚠ SCHAFFST DU DAS?",
     'WÜRDEST <span class="y">DU</span> 30 TAGE SCHAFFEN?', [("LOCKER", "Brauch ich eh nicht"), ("KEINEN TAG", "Unmöglich"), ("NUR MIT TABLET", "Das zählt nicht, oder?")],
     "UND FOLG MIR, SOLANGE DU NOCH EIN HANDY HAST", JS, False, POST, css="#s1 .title.main.top{font-size:96px}")
