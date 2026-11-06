import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<rect width="1080" height="1920" fill="#dfe6f0"/><g transform="translate(0,110)"><g id="h-win"></g><g id="h-door"></g><g id="h-hand"></g></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#7fc3ff"/><g transform="translate(0,60) scale(1)"><g id="b-fus"></g><g id="b-arr"></g><g id="b-lbl"></g></g><g id="b-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g id="c-plug"></g><g id="c-ton"></g><g id="c-men"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#8fd0ff"/><rect y="1120" width="1080" height="800" fill="#6abf5a"/><rect x="0" y="1080" width="1080" height="60" fill="#4a4a5a"/><g id="d-q"></g><g id="d-plane"></g><g id="d-wind"></g><g id="d-b"></g>', "1.06"),
]
JS = r'''
    /* S1 Kabinentür nah */
    const W = $("#h-win"); svg("rect", { x: 90, y: 860, width: 260, height: 340, rx: 120, fill: "#3fd4ff", stroke: "#8a93a8", "stroke-width": 26 }, W);
    const CL = svg("g", {}, W); for (let i = 0; i < 4; i++) svg("ellipse", { cx: 0, cy: 0, rx: 60, ry: 22, fill: "#fff", opacity: .9 }, CL);
    E.clock(tl, (t) => [...CL.children].forEach((c, i) => { c.setAttribute("cx", (100 + ((t * 120 + i * 90) % 340)).toFixed(1)); c.setAttribute("cy", (930 + i * 70).toFixed(1)); }));
    const DR = $("#h-door"); svg("rect", { x: 420, y: 760, width: 560, height: 900, rx: 60, fill: "#c9ced8", stroke: INK, "stroke-width": 10 }, DR);
    svg("rect", { x: 470, y: 810, width: 460, height: 800, rx: 40, fill: "none", stroke: "#9aa1b0", "stroke-width": 8 }, DR);
    K.otxt(DR, 700, 900, "EXIT", 60, "#3ee08f");
    const HD = svg("g", {}, $("#h-hand")); svg("rect", { x: 600, y: 1080, width: 220, height: 56, rx: 28, fill: "#e8463c", stroke: INK, "stroke-width": 8 }, HD);
    K.person(HD, { x: 860, y: 1600, s: .9, face: "worried", arms: "down", shirt: "#3fd4ff" });
    E.clock(tl, (t) => HD.setAttribute("transform", `translate(${(Math.abs(Math.sin(t * 7)) * -16).toFixed(1)},0)`));
    /* S2 Druck im Rumpf */
    const FU = $("#b-fus"); svg("circle", { cx: 540, cy: 860, r: 300, fill: "#f3f5fa", stroke: INK, "stroke-width": 12 }, FU); svg("rect", { x: 820, y: 740, width: 70, height: 240, rx: 14, fill: "#c9ced8", stroke: INK, "stroke-width": 8 }, FU);
    const AR = $("#b-arr"); for (let i = 0; i < 8; i++) { const a = i * Math.PI / 4; const g = svg("path", { d: `M${540 + Math.cos(a) * 120},${860 + Math.sin(a) * 120} L${540 + Math.cos(a) * 260},${860 + Math.sin(a) * 260}`, stroke: "#e8463c", "stroke-width": 22, "stroke-linecap": "round" }, AR); }
    K.pulse(AR, 540, 860, .6, .08); K.fadeIn(AR, cs("druck", 1));
    const LB = $("#b-lbl"); K.panel(LB, 540, 862, 400, 90, "#fff", "#e8463c"); K.txt(LB, 540, 880, "HOHER DRUCK", 50, "#e8463c"); K.fadeIn(LB, cs("druck", 1));
    const B2 = badge($("#b-b"), 540, 1240 - 50, "TÜR WIRD ZUGEPRESST", "#ffd23f", 52); pop(B2, cs("druck", 3), "540 1190");
    /* S3 Stöpsel + 10 Tonnen */
    const PL = $("#c-plug"); svg("rect", { x: 200, y: 560, width: 120, height: 560, fill: "#8a93a8", stroke: INK, "stroke-width": 8 }, PL); svg("rect", { x: 760, y: 560, width: 120, height: 560, fill: "#8a93a8", stroke: INK, "stroke-width": 8 }, PL);
    svg("path", { d: "M300,600 L780,600 L740,1080 L340,1080 Z", fill: "#c9ced8", stroke: INK, "stroke-width": 10 }, PL); K.otxt(PL, 540, 860, "TÜR", 70, "#fff");
    const TN = svg("g", {}, $("#c-ton")); svg("path", { d: "M540,540 L540,640 M500,600 L540,650 L580,600", fill: "none", stroke: "#ff3b3b", "stroke-width": 22, "stroke-linecap": "round", "stroke-linejoin": "round" }, TN);
    K.panel(TN, 540, 1150, 520, 110, "rgba(18,8,16,.94)", "#ff3b3b"); K.txt(TN, 540, 1172, "≈ 10 TONNEN", 64, "#ff3b3b"); pop(TN, cs("stopfen", 5), "540 1000");
    const MN = $("#c-men"); tl.set(MN, { autoAlpha: 0 }, 0); tl.set(MN, { autoAlpha: 1 }, at("mensch", -0.1)); tl.set(PL, { autoAlpha: 0 }, at("mensch", -0.1)); tl.set(TN, { autoAlpha: 0 }, at("mensch", -0.1));
    for (let i = 0; i < 10; i++) K.person(MN, { x: 150 + (i % 5) * 190, y: 780 + Math.floor(i / 5) * 360, s: .45, face: i % 2 ? "worried" : "shock", arms: "down", shirt: ["#e8463c", "#3fd4ff", "#3ee08f", "#ffd23f", "#b05cd6"][i % 5] });
    const XX = K.cross(MN, 540, 860, 230); pop(XX, cs("mensch", 2), "540 860");
    /* S4 Landeanflug */
    const Q = $("#d-q"); K.otxt(Q, 540, 820, "?!", 260, "#ffd23f"); pop(Q, at("verrueckt", 0), "540 740"); K.hide(Q, at("landung", -0.1));
    const PLN = svg("g", {}, $("#d-plane")); svg("path", { d: "M-150,0 L130,-20 Q180,0 130,20 L-150,10 Z", fill: "#fff", stroke: INK, "stroke-width": 8 }, PLN); svg("path", { d: "M-20,0 L-80,90 L-30,90 L40,5 Z M-20,0 L-80,-80 L-40,-80 L30,-5 Z M-130,0 L-160,-60 L-120,-60 L-100,0Z", fill: "#c9ced8", stroke: INK, "stroke-width": 7 }, PLN);
    tl.set(PLN, { x: 140, y: 560, rotation: 12, svgOrigin: "0 0" }, 0); tl.to(PLN, { x: 900, y: 1010, duration: Math.max(4, end("landung") - at("landung")), ease: "none" }, at("landung"));
    const WD = $("#d-wind"); for (let i = 0; i < 10; i++) { const r = svg("rect", { x: 0, y: 600 + i * 50, width: 200, height: 10, rx: 5, fill: "#fff", opacity: .8 }, WD); }
    tl.set(WD, { autoAlpha: 0 }, 0); tl.set(WD, { autoAlpha: 1 }, cs("landung", 7));
    E.clock(tl, (t) => [...WD.children].forEach((r, i) => r.setAttribute("x", (((t * 1600 + i * 170) % 1400) - 200).toFixed(1))));
    const B4 = badge($("#d-b"), 540, 1190, "2023: TÜR IM LANDEANFLUG", "#ff3b3b", 48); pop(B4, cs("landung", 4), "540 1190");
'''
POST = r'''    K.hudFmt();'''
page("19-flugzeugtuer", S, 'FLUGZEUGTÜR<br/><span class="r">ÖFFNEN?</span>', "⚠ IN 10.000 METERN",
     'WÜRDEST <span class="y">DU</span> AM NOTAUSGANG SITZEN?', [("JA, KLAR", "Mehr Beinfreiheit"), ("NIE IM LEBEN", "Zu gruselig"), ("NUR AM FENSTER", "Ich will rausschauen")],
     "UND FOLG MIR, BEVOR DU DAS NÄCHSTE MAL FLIEGST", JS, 1, POST, css="#s1 .title.main.top{font-size:96px}")
