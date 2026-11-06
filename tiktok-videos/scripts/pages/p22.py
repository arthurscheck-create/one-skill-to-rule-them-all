import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<rect width="1080" height="1920" fill="#ffd23f"/><g id="h-cab"></g><g id="h-p"></g><g id="h-cable"></g><g id="h-sp"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#c9a24a"/><rect x="80" y="560" width="920" height="1000" rx="20" fill="#e8c76a" stroke="#0d0b18" stroke-width="10"/><g id="b-disp"></g><g id="b-p"></g><g id="b-ph"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g id="c-shaft"></g><g id="c-cab"></g><g id="c-sp"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#3b3768"/><g id="d-cab"></g><g id="d-arr"></g><g id="d-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#8fd0ff"/><g id="e-q"></g><g transform="translate(0,110)"><g id="e-esb"></g><g id="e-cab"></g></g><g id="e-b"></g><g id="e-b2"></g>', "1.06"),
]
JS = r'''
    const cabin = (g, x, y, w, h) => { const c = svg("g", {}, g); svg("rect", { x: x - w / 2, y, width: w, height: h, rx: 16, fill: "#e8c76a", stroke: INK, "stroke-width": 10 }, c); svg("line", { x1: x, y1: y + 20, x2: x, y2: y + h - 20, stroke: "#b08a3a", "stroke-width": 8 }, c); return c; };
    /* S1 Kabine, Seil reißt */
    const CB = $("#h-cab"); svg("rect", { x: 60, y: 900, width: 960, height: 1020, fill: "#e8c76a", stroke: INK, "stroke-width": 12 }, CB); svg("rect", { x: 60, y: 900, width: 960, height: 60, fill: "#fff6b0" }, CB);
    svg("rect", { x: 820, y: 980, width: 120, height: 220, rx: 14, fill: "#5c6390", stroke: INK, "stroke-width": 7 }, CB); for (let i = 0; i < 6; i++) svg("circle", { cx: 855 + (i % 2) * 50, cy: 1020 + Math.floor(i / 2) * 60, r: 16, fill: i === 5 ? "#e8463c" : "#fff" }, CB);
    const HP = svg("g", {}, $("#h-p")); K.person(HP, { x: 460, y: 1920, s: 1.5, face: "shock", arms: "down", shirt: "#3fd4ff" });
    const CA = $("#h-cable"); svg("path", { d: "M760,960 L760,1040", fill: "none", stroke: INK, "stroke-width": 16, "stroke-linecap": "round" }, CA);
    const SP = K.burst($("#h-sp"), 760, 1060, 70, "", "#fff6b0"); K.pulse(SP, 760, 1060, .25, .3);
    E.clock(tl, (t) => { const j = Math.sin(t * 40) * 6; CB.setAttribute("transform", `translate(${j.toFixed(1)},${(Math.abs(Math.sin(t * 23)) * 5).toFixed(1)})`); HP.setAttribute("transform", `translate(${j.toFixed(1)},${(-Math.abs(Math.sin(t * 3)) * 16).toFixed(1)})`); });
    /* S2 schwerelos */
    const DI = $("#b-disp"); K.panel(DI, 540, 650, 260, 110, "#14122b", "#ff3b3b"); const DT = K.txt(DI, 540, 675, "20", 70, "#ff3b3b");
    E.clock(tl, (t) => { DT.textContent = t < cs("schwerelos", 1) ? "20" : "19"; });
    const BP = svg("g", {}, $("#b-p")); K.person(BP, { x: 540, y: 1400, s: 1.05, face: "shock", arms: "phone", shirt: "#3fd4ff" });
    const PH = svg("g", {}, $("#b-ph")); svg("rect", { x: -45, y: -80, width: 90, height: 160, rx: 16, fill: "#1b1936", stroke: "#fff", "stroke-width": 6 }, PH);
    E.clock(tl, (t) => { const s0 = at("schwerelos"), k = Math.max(0, t - s0); BP.setAttribute("transform", `translate(0,${(-Math.min(1, k) * 60 + Math.sin(t * 2) * 12).toFixed(1)}) rotate(${(Math.sin(t * 1.4) * 6).toFixed(1)} 540 1000)`); PH.setAttribute("transform", `translate(${(700 + Math.sin(t * 1.7) * 30).toFixed(1)},${(820 - Math.min(1, k) * 80 + Math.cos(t * 2.1) * 20).toFixed(1)}) rotate(${(t * 40).toFixed(1)})`); });
    /* S3 Fangbremse */
    const SH = $("#c-shaft"); [300, 780].forEach((x) => svg("rect", { x: x - 20, y: 0, width: 40, height: 1920, fill: "#8a93a8", stroke: INK, "stroke-width": 6 }, SH));
    [480, 540, 600].forEach((x) => svg("line", { x1: x, y1: 0, x2: x, y2: 640, stroke: INK, "stroke-width": 8 }, SH));
    const CC = svg("g", {}, $("#c-cab")); cabin(CC, 540, 640, 420, 480);
    const JW = svg("g", {}, CC); [[268, "#ff3b3b"], [812, "#ff3b3b"]].forEach(([x, c]) => svg("rect", { x: x - 30, y: 700, width: 60, height: 90, rx: 10, fill: c, stroke: INK, "stroke-width": 6 }, JW));
    tl.set(CC, { y: -120 }, 0); tl.to(CC, { y: 0, duration: Math.max(1, cs("bremse", 6) - at("bremse")), ease: "power1.in" }, at("bremse"));
    pop(JW, cs("bremse", 5), "540 745");
    const SPK = $("#c-sp"); [300, 780].forEach((x) => { const b = K.burst(SPK, x, 760, 70, "", "#fff6b0"); }); tl.set(SPK, { autoAlpha: 0 }, 0); tl.to(SPK, { autoAlpha: 1, duration: .1, repeat: 5, yoyo: true }, cs("bremse", 6));
    const B3 = badge($("#c-b"), 540, 1190, "FANGBREMSE", "#3ee08f", 70); pop(B3, cs("bremse", 4), "540 1190");
    /* S4 Springen */
    const DC = svg("g", {}, $("#d-cab")); cabin(DC, 540, 580, 520, 620); const JP = svg("g", {}, DC); K.person(JP, { x: 540, y: 1180, s: .8, face: "worried", arms: "down", shirt: "#3fd4ff" });
    E.clock(tl, (t) => { const j = t > cs("springen", 0) ? Math.abs(Math.sin((t - cs("springen", 0)) * 4)) * -60 : 0; JP.setAttribute("transform", `translate(0,${j.toFixed(1)})`); DC.setAttribute("transform", `translate(0,${(Math.sin(t * 30) * 4).toFixed(1)})`); });
    const DA = $("#d-arr"); svg("path", { d: "M900,600 L900,1100 M850,1040 L900,1110 L950,1040", fill: "none", stroke: "#ff3b3b", "stroke-width": 24, "stroke-linecap": "round", "stroke-linejoin": "round" }, DA); K.fadeIn(DA, at("versagt", 0));
    const B4 = badge($("#d-b"), 540, 1190, "SPRINGEN? FAST NUTZLOS", "#ff3b3b", 50); pop(B4, cs("springen", 1), "540 1190");
    /* S5 Rekord 1945 */
    const Q = $("#e-q"); K.otxt(Q, 540, 860, "?!", 260, "#e8463c"); pop(Q, at("verrueckt", 0), "540 780"); K.hide(Q, at("rekord", -0.1));
    const ES = svg("g", {}, $("#e-esb")); svg("path", { d: "M440,1260 L440,820 L470,820 L470,700 L500,700 L500,600 L520,600 L520,480 L560,480 L560,600 L580,600 L580,700 L610,700 L610,820 L640,820 L640,1260 Z", fill: "#5c6390", stroke: INK, "stroke-width": 8 }, ES);
    for (let r = 0; r < 12; r++) for (let c = 0; c < 4; c++) svg("rect", { x: 455 + c * 45, y: 840 + r * 34, width: 20, height: 16, fill: (r * 4 + c) % 5 ? "#ffd23f" : "#3a3560" }, ES);
    K.fadeIn(ES, at("rekord", 0));
    const EC = svg("g", {}, $("#e-cab")); svg("rect", { x: 680, y: 0, width: 70, height: 90, rx: 8, fill: "#e8c76a", stroke: INK, "stroke-width": 6 }, EC);
    tl.set(EC, { y: 560, autoAlpha: 0 }, 0); tl.set(EC, { autoAlpha: 1 }, cs("rekord", 3)); tl.to(EC, { y: 1140, duration: 1.2, ease: "power2.in" }, cs("rekord", 3));
    const B5 = badge($("#e-b"), 540, 1190, "75 STOCKWERKE", "#ffd23f", 62); pop(B5, cs("rekord", 3), "540 1190");
    const B6 = badge($("#e-b2"), 540, 600, "ÜBERLEBT · REKORD", "#3ee08f", 56); pop(B6, cs("rekord", 5), "540 600");
'''
page("22-fahrstuhl-absturz", S, 'SEIL<br/><span class="r">GERISSEN</span>', "⚠ 20 STOCKWERKE FREIER FALL",
     'FÄHRST <span class="y">DU</span> JETZT NOCH FAHRSTUHL?', [("KLAR, JEDEN TAG", "Ist doch sicher"), ("NUR NOCH TREPPE", "Nie wieder"), ("NUR MIT SPRUNG", "Ich spring trotzdem")],
     "UND FOLG MIR, BEVOR DU DIE TREPPE NIMMST", JS, 2, "    K.hudFmt();")
