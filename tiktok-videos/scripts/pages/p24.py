import sys; sys.path.insert(0, "/home/user/tiktok-videos/scripts"); from pagegen import page
S = [
 ('<defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb86b"/><stop offset="1" stop-color="#fff0d6"/></linearGradient></defs><rect width="1080" height="1920" fill="url(#g1)"/><g id="h-rays"></g><g id="h-cups"></g><g id="h-steam"></g>', "1.06"),
 ('<rect width="1080" height="1920" fill="#3a2a1e"/><g id="b-cup"></g><g id="b-brain"></g><g id="b-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#2a2347"/><g transform="translate(0,70)"><g id="c-heart"></g></g><g id="c-wc"></g><g id="c-b"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#14324a"/><g id="d-cups"></g><g id="d-moon"></g><g id="d-b"></g><g id="d-b2"></g>', "1.05"),
 ('<rect width="1080" height="1920" fill="#1b1936"/><g id="e-q"></g><g id="e-ch"></g><g id="e-b"></g>', "1.06"),
]
JS = r'''
    const cup = (g, x, y, s) => { const c = svg("g", { transform: `translate(${x},${y}) scale(${s})` }, g); svg("path", { d: "M-90,-80 L90,-80 L70,90 Q0,120 -70,90 Z", fill: "#fff", stroke: INK, "stroke-width": 8 }, c); svg("ellipse", { cx: 0, cy: -80, rx: 90, ry: 22, fill: "#6b3e1e", stroke: INK, "stroke-width": 6 }, c); svg("path", { d: "M88,-40 Q150,-40 140,20 Q130,60 76,50", fill: "none", stroke: INK, "stroke-width": 14 }, c); return c; };
    /* S1 fünf Tassen */
    K.rays($("#h-rays"), 540, 1150, 12, "#fff", .22);
    const CU = $("#h-cups"); [[300, 1000, 1.1], [780, 1000, 1.1], [540, 1150, 1.6], [270, 1330, 1], [810, 1330, 1]].forEach(([x, y, s], i) => { const w = svg("g", {}, CU); cup(w, x, y, s); K.bob(w, 6, 2 + i * .4, i); });
    const SM = $("#h-steam"), st = []; for (let i = 0; i < 3; i++) st.push([svg("path", { d: "M0,0 q-20,-40 0,-80 q20,-40 0,-80", fill: "none", stroke: "#fff", "stroke-width": 12, "stroke-linecap": "round", opacity: .8 }, SM), i]);
    E.clock(tl, (t) => st.forEach(([p, i]) => { const k = (t * .8 + i * .33) % 1; p.setAttribute("transform", `translate(${500 + i * 40},${(990 - k * 120).toFixed(1)})`); p.setAttribute("opacity", (0.9 * (1 - k)).toFixed(2)); }));
    /* S2 Koffein blockiert Müdigkeit */
    cup($("#b-cup"), 280, 900, 1.2);
    const BR = svg("g", {}, $("#b-brain")); svg("path", { d: "M640,760 C600,640 760,580 820,640 C880,580 1000,650 960,760 C1010,820 960,940 860,920 C820,980 700,960 690,900 C600,900 590,800 640,760 Z", fill: "#ff9ab0", stroke: INK, "stroke-width": 9 }, BR);
    K.otxt(BR, 800, 820, "ZZZ", 54, "#5c6390"); const BX = K.cross(BR, 800, 800, 70); pop(BX, cs("wach", 3), "800 800");
    pop(BR, cs("wach", 2), "800 800");
    const B2 = badge($("#b-b"), 540, 1190, "MÜDIGKEIT BLOCKIERT", "#ffd23f", 54); pop(B2, cs("wach", 3), "540 1190");
    /* S3 Herz + Klo */
    const HT = svg("g", {}, $("#c-heart")); svg("path", { d: "M540,980 C380,860 300,780 300,690 C300,610 360,560 430,560 C480,560 520,590 540,630 C560,590 600,560 650,560 C720,560 780,610 780,690 C780,780 700,860 540,980 Z", fill: "#ff3b5c", stroke: INK, "stroke-width": 10 }, HT);
    K.pulse(HT, 540, 770, .35, .08);
    const WC = svg("g", {}, $("#c-wc")); K.panel(WC, 860, 1060, 220, 150, "#fff", INK); K.txt(WC, 860, 1085, "WC", 70, "#3fd4ff"); pop(WC, cs("herz", 2), "860 1060");
    const B3 = badge($("#c-b"), 540, 1190 - 40, "PULS ↑", "#ff3b5c", 62); pop(B3, cs("herz", 1), "540 1150");
    /* S4 400 mg + Schlaf */
    const DC = $("#d-cups"); for (let i = 0; i < 5; i++) { const c = cup(DC, 150 + i * 195, 760, .75); pop(c, at("tasse5", i * .12), `${150 + i * 195} 760`); }
    const B4 = badge($("#d-b"), 540, 1000, "≈ 400 MG = NOCH OK", "#3ee08f", 56); pop(B4, cs("grenze", 5), "540 1000");
    const MN = svg("g", {}, $("#d-moon")); svg("path", { d: "M880,1080 A120,120 0 1 1 760,960 A90,90 0 1 0 880,1080 Z", fill: "#ffd23f", stroke: INK, "stroke-width": 8 }, MN); pop(MN, cs("schlaf", 2), "820 1000");
    const B5 = badge($("#d-b2"), 540, 1190, "SCHLAF LEIDET", "#ff3b3b", 62); pop(B5, cs("schlaf", 3), "540 1190"); K.hide(B4, cs("schlaf", 0, -0.05));
    /* S5 Studie */
    const Q = $("#e-q"); K.otxt(Q, 540, 860, "?!", 260, "#ffd23f"); pop(Q, at("verrueckt", 0), "540 780"); K.hide(Q, at("studie", -0.1));
    const CH = $("#e-ch"); svg("line", { x1: 200, y1: 1100, x2: 900, y2: 1100, stroke: "#fff", "stroke-width": 8 }, CH);
    [[300, 260, "#c9c3e6", "KEIN"], [540, 340, "#ffb86b", "2–3"], [780, 400, "#3ee08f", "4–5"]].forEach(([x, h, c, l], i) => { const b = svg("rect", { x: x - 70, y: 1100 - h, width: 140, height: h, rx: 14, fill: c, stroke: INK, "stroke-width": 7 }, CH); K.txt(CH, x, 1160, l, 42, "#fff"); tl.set(b, { scaleY: 0, svgOrigin: `${x} 1100` }, 0); tl.to(b, { scaleY: 1, duration: .6, ease: "back.out(1.6)" }, cs("studie", 2, i * .2)); });
    K.otxt(CH, 540, 660, "TASSEN PRO TAG", 44, "#c9c3e6"); K.fadeIn(CH, at("studie", 0));
    const B6 = badge($("#e-b"), 540, 560, "URSACHE UNKLAR", "#ffd23f", 56); pop(B6, cs("studie", 5), "540 560");
'''
page("24-fuenf-kaffee", S, '5 TASSEN<br/><span class="r">KAFFEE</span><br/>JEDEN TAG', "⚠ ZU VIEL?",
     'WIE VIELE TASSEN TRINKST <span class="y">DU</span>?', [("KEINE", "Ich trink lieber Tee"), ("EINE BIS ZWEI", "Morgens reicht"), ("FÜNF UND MEHR", "Ohne geht nix")],
     "UND FOLG MIR – AM BESTEN MIT EINEM KAFFEE", JS, False, "    K.hudFmt();")
