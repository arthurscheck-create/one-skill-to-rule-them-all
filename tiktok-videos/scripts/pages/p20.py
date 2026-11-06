import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<rect width="1080" height="1920" fill="#0b1030"/><g id="h-stars"></g><circle cx="540" cy="2300" r="1100" fill="#3fa9ff"/><path d="M-200,1500 Q300,1350 700,1480 T1300,1420 L1300,1920 L-200,1920Z" fill="#3ee08f" opacity=".85"/><g id="h-rays"></g><g id="h-p"></g><g id="h-helm"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#14122b"/><g id="b-stars"></g><g id="b-p"></g><g id="b-air"></g><g id="b-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a1a3a"/><g id="c-mouth"></g><g id="c-bub"></g><g id="c-th"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#14122b"/><g id="d-stars"></g><g id="d-p"></g><rect id="d-black" width="1080" height="1920" fill="#000" opacity="0"/><g id="d-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#dfe6f0"/><g id="e-q"></g><g id="e-ch"></g><g id="e-ok"></g><g id="e-b"></g>', "1.06"),
]
JS = r'''
    const helm = (g, x, y, s) => { const h = svg("g", { transform: `translate(${x},${y}) scale(${s})` }, g); svg("circle", { cx: 0, cy: 0, r: 120, fill: "#fff", stroke: INK, "stroke-width": 10 }, h); svg("circle", { cx: 0, cy: 10, r: 85, fill: "#3fd4ff", opacity: .7, stroke: INK, "stroke-width": 7 }, h); svg("path", { d: "M-40,-30 q20,-25 50,-20", fill: "none", stroke: "#fff", "stroke-width": 12, "stroke-linecap": "round" }, h); return h; };
    /* S1 */
    K.stars($("#h-stars"), 80, 201); K.rays($("#h-rays"), 540, 1000, 10, "#fff", .08);
    const HP = svg("g", {}, $("#h-p")); K.person(HP, { x: 520, y: 1900, s: 1.7, face: "shock", arms: "down", shirt: "#f3f5fa", pants: "#c9ced8", hair: "#5a3a1e" });
    const HM = svg("g", {}, $("#h-helm")); helm(HM, 0, 0, 1.1);
    E.clock(tl, (t) => { HP.setAttribute("transform", `translate(0,${(Math.sin(t * 1.6) * 14).toFixed(1)}) rotate(${(Math.sin(t * .9) * 3).toFixed(2)} 540 1200)`); HM.setAttribute("transform", `translate(${(860 + Math.sin(t * 1.3) * 20).toFixed(1)},${(1180 + Math.cos(t * 1.1) * 26).toFixed(1)}) rotate(${(t * 25).toFixed(1)})`); });
    /* S2 Luft schießt raus */
    K.stars($("#b-stars"), 60, 202);
    K.person($("#b-p"), { x: 420, y: 1500, s: 1.2, face: "shock", arms: "down", shirt: "#f3f5fa", pants: "#c9ced8" });
    const AI = $("#b-air"), puffs = []; for (let i = 0; i < 9; i++) puffs.push([svg("circle", { cx: 0, cy: 0, r: 30, fill: "#fff", opacity: .7 }, AI), i]);
    E.clock(tl, (t) => puffs.forEach(([c, i]) => { const p = ((t * 1.4 + i * .11) % 1); c.setAttribute("cx", (460 + p * 600).toFixed(1)); c.setAttribute("cy", (930 + Math.sin(i * 3 + p * 6) * 60).toFixed(1)); c.setAttribute("r", (20 + p * 50).toFixed(1)); c.setAttribute("opacity", (0.8 * (1 - p)).toFixed(2)); }));
    K.fadeIn(AI, at("luft", 0));
    const B2 = badge($("#b-b"), 540, 640, "LUFT NICHT ANHALTEN", "#ff3b3b", 54); pop(B2, cs("luft", 2), "540 640");
    /* S3 Spucke blubbert */
    const MO = $("#c-mouth"); svg("ellipse", { cx: 540, cy: 860, rx: 330, ry: 220, fill: "#8a2a3a", stroke: INK, "stroke-width": 12 }, MO); svg("ellipse", { cx: 540, cy: 960, rx: 230, ry: 110, fill: "#ff8fa3", stroke: INK, "stroke-width": 8 }, MO);
    for (let i = 0; i < 6; i++) svg("rect", { x: 300 + i * 80, y: 650, width: 70, height: 70, rx: 14, fill: "#fff", stroke: INK, "stroke-width": 5 }, MO);
    const BU = $("#c-bub"), bb = []; for (let i = 0; i < 16; i++) bb.push([svg("circle", { cx: 380 + (i * 37) % 320, cy: 940, r: 10 + (i % 4) * 7, fill: "#fff", "fill-opacity": .5, stroke: "#fff", "stroke-width": 4 }, BU), i]);
    const tb = cs("kochen", 1); E.clock(tl, (t) => bb.forEach(([c, i]) => { const p = t < tb ? 0 : ((t * 1.5 + i * .23) % 1); c.setAttribute("cy", (950 - p * 220).toFixed(1)); c.setAttribute("opacity", t < tb ? 0 : (1 - p).toFixed(2)); }));
    const TH = svg("g", {}, $("#c-th")); svg("rect", { x: 900, y: 560, width: 60, height: 360, rx: 30, fill: "#fff", stroke: INK, "stroke-width": 8 }, TH); svg("circle", { cx: 930, cy: 950, r: 55, fill: "#e8463c", stroke: INK, "stroke-width": 8 }, TH); svg("rect", { x: 915, y: 760, width: 30, height: 170, fill: "#e8463c" }, TH); K.otxt(TH, 930, 540, "37 °C", 48, "#ffd23f");
    pop(TH, cs("kochen", 3), "930 760");
    const B3 = badge($("#c-b"), 540, 1190, "KOCHT BEI 37 °C", "#ffd23f", 62); pop(B3, cs("kochen", 4), "540 1190");
    /* S4 Schwellen + schwarz */
    K.stars($("#d-stars"), 60, 203);
    const DP = svg("g", {}, $("#d-p")); K.person(DP, { x: 540, y: 1560, s: 1.25, face: "worried", arms: "down", shirt: "#f3f5fa", pants: "#c9ced8" });
    tl.to(DP, { scale: 1.12, svgOrigin: "540 1100", duration: 1.6, ease: "sine.inOut" }, cs("haut", 0));
    const B4 = badge($("#d-b"), 540, 640, "HAUT HÄLT", "#3ee08f", 66); pop(B4, cs("haut", 1), "540 640");
    tl.to("#d-black", { opacity: .92, duration: 1.2, ease: "power2.in" }, cs("haut", 2));
    /* S5 NASA-Test */
    const Q = $("#e-q"); K.otxt(Q, 540, 860, "?!", 260, "#e8463c"); pop(Q, at("verrueckt", 0), "540 780"); K.hide(Q, at("nasa", -0.1));
    const CH = $("#e-ch"); svg("rect", { x: 220, y: 560, width: 640, height: 600, rx: 50, fill: "#5c6390", stroke: INK, "stroke-width": 12 }, CH); svg("rect", { x: 280, y: 620, width: 520, height: 420, rx: 30, fill: "#1b1936" }, CH);
    K.person(CH, { x: 540, y: 1020, s: .65, face: "shock", arms: "down", shirt: "#f3f5fa", pants: "#c9ced8" }); K.txt(CH, 540, 1110, "VAKUUMKAMMER", 44, "#fff");
    K.fadeIn(CH, at("nasa", 0));
    const TM = svg("g", {}, $("#e-ch")); K.panel(TM, 820, 600, 220, 110, "#e8463c", INK); K.txt(TM, 820, 622, "14 s", 66, "#fff"); pop(TM, cs("nasa", 4), "820 600");
    const OK = K.check($("#e-ok"), 540, 830, 1.8); pop(OK, cs("nasa", 6), "540 830");
    const B5 = badge($("#e-b"), 540, 1190, "NASA-TEST", "#3fd4ff", 66); pop(B5, cs("nasa", 2), "540 1190");
'''
page("20-helm-im-all", S, 'HELM AB<br/><span class="r">IM ALL</span>', "⚠ WIE LANGE ÜBERLEBST DU?",
     'WÜRDEST <span class="y">DU</span> INS ALL FLIEGEN?', [("SOFORT", "Einmal die Erde sehen"), ("NUR MIT HELM", "Und zwei Ersatzhelmen"), ("NIEMALS", "Ich bleib am Boden")],
     "UND FOLG MIR, BEVOR DIR DIE LUFT AUSGEHT", JS, 2)
