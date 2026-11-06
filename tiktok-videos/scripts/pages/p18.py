import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff9ad5"/><stop offset="1" stop-color="#ffe0f1"/></linearGradient></defs><rect width="1080" height="1920" fill="url(#g1)"/><g id="h-rays"></g><g id="h-p"></g><g id="h-gum"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g transform="translate(0,90)"><g id="b-st"></g><g id="b-sugar"></g><g id="b-gum"></g></g><g id="b-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#3b2a4a"/><g transform="translate(0,70)"><g id="c-gut"></g><g id="c-gum"></g><g id="c-ok"></g></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#1b1936"/><g id="d-q"></g><g id="d-cal"></g><g id="d-ball"></g><g id="d-doc"></g><g id="d-b"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#14324a"/><g id="e-a"></g><g id="e-b"></g>', "1.05"),
]
JS = r'''
    const gum = (g, x, y, s, c) => { const k = svg("g", { transform: `translate(${x},${y}) scale(${s})` }, g); svg("rect", { x: -50, y: -26, width: 100, height: 52, rx: 26, fill: c || "#ff5fb0", stroke: INK, "stroke-width": 6 }, k); svg("path", { d: "M-30,-8 q20,-10 40,0", fill: "none", stroke: "#ffc2e2", "stroke-width": 6, "stroke-linecap": "round" }, k); return k; };
    /* S1 */
    K.rays($("#h-rays"), 540, 1000, 12, "#fff", .2);
    const HP = svg("g", {}, $("#h-p")); K.person(HP, { x: 540, y: 2090, s: 1.9, face: "shock", arms: "down", shirt: "#3fd4ff", hair: "#2a1a10" });
    const G1 = svg("g", {}, $("#h-gum")); gum(G1, 0, 0, 1.1);
    E.clock(tl, (t) => { const p = (t % 1.6) / 1.6; G1.setAttribute("transform", `translate(${(730 - p * 182).toFixed(1)},${(870 + p * p * 430).toFixed(1)}) rotate(${(p * 260).toFixed(1)})`); G1.style.opacity = p > .92 ? 0 : 1; });
    /* S2 Magen */
    const ST = $("#b-st"); svg("path", { d: "M380,520 C380,620 300,640 300,780 C300,1000 480,1120 680,1080 C860,1040 900,880 820,800 C760,740 640,760 600,700 C560,640 600,560 560,520 Z", fill: "#ff8fb1", stroke: INK, "stroke-width": 10 }, ST);
    svg("path", { d: "M330,900 C340,1010 480,1090 680,1060 C820,1030 870,930 840,880 C700,920 500,930 330,900 Z", fill: "#9ee05a", opacity: .85 }, ST);
    const SG = $("#b-sugar"); for (let i = 0; i < 8; i++) { const r = svg("rect", { x: 420 + (i % 4) * 70, y: 900 + Math.floor(i / 4) * 60, width: 26, height: 26, fill: "#fff", stroke: INK, "stroke-width": 4, transform: `rotate(${i * 20} ${433 + (i % 4) * 70} ${913 + Math.floor(i / 4) * 60})` }, SG); }
    tl.to(SG, { autoAlpha: 0, duration: 1.2 }, cs("magen", 2));
    const BG = svg("g", {}, $("#b-gum")); gum(BG, 0, 0, 1.4); tl.set(BG, { x: 470, y: 480 }, 0); tl.to(BG, { x: 560, y: 930, rotation: 200, duration: 1.4, ease: "bounce.out" }, cs("magen", 0));
    const B2 = badge($("#b-b"), 540, 1190, "UNVERDAULICH", "#ff5fb0", 66); pop(B2, cs("magen", 6), "540 1190");
    /* S3 Darm */
    const GU = $("#c-gut"); const path = "M160,520 C160,640 920,600 920,720 C920,840 160,800 160,920 C160,1040 920,1000 920,1120";
    svg("path", { d: path, fill: "none", stroke: INK, "stroke-width": 92, "stroke-linecap": "round" }, GU); svg("path", { d: path, fill: "none", stroke: "#ff9ab0", "stroke-width": 76, "stroke-linecap": "round" }, GU);
    const PP = svg("path", { d: path, fill: "none", stroke: "none" }, GU); const L = PP.getTotalLength ? PP.getTotalLength() : 3000;
    const CG = svg("g", {}, $("#c-gum")); gum(CG, 0, 0, .7);
    const t0 = at("weg"), t1 = cs("weg", 3, .5);
    E.clock(tl, (t) => { const k = Math.max(0, Math.min(1, (t - t0) / Math.max(.5, t1 - t0))); const pt = PP.getPointAtLength ? PP.getPointAtLength(k * L) : { x: 160, y: 520 }; CG.setAttribute("transform", `translate(${pt.x.toFixed(1)},${pt.y.toFixed(1)})`); });
    const OK = K.check($("#c-ok"), 920, 1120, 1.2); pop(OK, t1, "920 1120");
    const B3 = badge($("#c-b"), 540, 1240 - 50, "KEINE 7 JAHRE", "#3ee08f", 62); pop(B3, cs("weg", 4), "540 1190");
    /* S4 Fall */
    const Q = $("#d-q"); K.otxt(Q, 540, 860, "?!", 260, "#ffd23f"); pop(Q, at("verrueckt", 0), "540 780"); K.hide(Q, at("fall", -0.1));
    const CA = $("#d-cal"); K.panel(CA, 540, 620, 560, 130, "#fff", INK); K.txt(CA, 540, 645, "JEDEN TAG: 5–7", 58, "#e8463c"); pop(CA, cs("fall", 1), "540 620");
    const BA = $("#d-ball"); for (let i = 0; i < 7; i++) { const g = gum(BA, 400 + (i % 4) * 90, 820 + Math.floor(i / 4) * 70, .8, ["#ff5fb0", "#3fd4ff", "#3ee08f", "#ffd23f"][i % 4]); pop(g, cs("fall", 2, i * .12), `${400 + (i % 4) * 90} 850`); }
    tl.to(BA, { scale: .55, svgOrigin: "540 860", duration: .6, ease: "power2.in" }, cs("fall", 4));
    const DC = $("#d-doc"); svg("circle", { cx: 540, cy: 860, r: 150, fill: "none", stroke: "#ff3b3b", "stroke-width": 16, "stroke-dasharray": "30 18" }, DC); pop(DC, cs("fall", 4), "540 860");
    const B4 = badge($("#d-b"), 540, 1190, "KAUGUMMI-KLUMPEN", "#ff3b3b", 58); pop(B4, cs("fall", 4), "540 1190");
    /* S5 Fazit */
    const EA = $("#e-a"); const g1 = svg("g", {}, EA); gum(g1, 300, 760, 1.3); K.check(g1, 300, 940, 1.1); K.otxt(g1, 300, 1080, "EINER", 56, "#3ee08f"); pop(g1, cs("fazit", 2), "300 860");
    const g2 = svg("g", {}, EA); [0, 1, 2, 3].forEach((i) => gum(g2, 720 + (i % 2) * 110, 700 + Math.floor(i / 2) * 70, .9)); K.cross(g2, 780, 940, 60); K.otxt(g2, 780, 1080, "JEDEN TAG VIELE", 50, "#ff3b3b"); pop(g2, cs("fazit", 3), "780 860");
'''
POST = r'''    K.hudText([[at("min", -0.2), "1 MIN"], [at("tage", -0.2), "3 TAGE"], [at("verrueckt", -0.2), "?"], [at("fazit", -0.2), "1 = OK"]], "1 MIN");'''
page("18-kaugummi-verschluckt", S, 'KAUGUMMI<br/><span class="r">VERSCHLUCKT</span>', "⚠ 7 JAHRE IM BAUCH?",
     'HAST <span class="y">DU</span> SCHON MAL EINEN VERSCHLUCKT?', [("JA, AUS VERSEHEN", "Passiert halt"), ("JA, MIT ABSICHT", "Kein Mülleimer da"), ("NIE", "Ich spuck ihn aus")],
     "UND FOLG MIR – UND SPUCK IHN LIEBER AUS", JS, False, POST, css="#s1 .title.main.top{font-size:92px}")
