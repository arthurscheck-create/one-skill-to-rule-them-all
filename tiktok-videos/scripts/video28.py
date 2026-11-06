# Video 28: 1 Million oder 1 Cent, der sich 30 Tage verdoppelt (klassischer Hook, v3-Stimme)
import importlib.util, json, re
from pathlib import Path
spec = importlib.util.spec_from_file_location("b2", "/home/user/tiktok-videos/scripts/batch2_lib.py"); b2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b2)
build, F = b2.build, b2.F
slug, title = "28-cent-oder-million", "Eine Million sofort oder ein Cent, der sich jeden Tag verdoppelt?"
L = [
 ("hook", ["Eine Million oder ein Cent?"], True),
 ("loop", ["Der Cent verdoppelt sich", "^jeden Tag,^", "dreißig Tage lang.", "Am Ende siehst du,", "welche Wahl", "dich ^reich^ macht."], False),
 ("wahl", ["Fast jeder", "nimmt die *Million.*", "Logisch, oder?"], False),
 ("t1", ["^Tag eins:^", "ein Cent."], False),
 ("t10", ["^Tag zehn:^", "gerade mal", "fünf Euro."], False),
 ("spott", ["Dein Freund", "mit der Million", "lacht dich *aus.*"], False),
 ("t20", ["^Tag zwanzig:^", "rund fünftausend Euro.", "Immer noch", "*lächerlich.*"], False),
 ("t25", ["^Tag fünfundzwanzig:^", "fast hundertsiebzigtausend."], False),
 ("t27", ["^Tag siebenundzwanzig:^", "sechshundertsiebzigtausend.", "Du liegst", "*immer noch* hinten."], False),
 ("dann", ["Und dann", "passiert es."], False),
 ("t28", ["^Tag achtundzwanzig:^", "~eins Komma drei Millionen.~", "Du überholst ihn."], False),
 ("t30", ["^Tag dreißig:^", "~über fünf Millionen Euro.~"], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("haelfte", ["Die Hälfte", "von allem", "kommt erst", "am ^letzten Tag.^"], False),
 ("schach", ["Und nach", "^vierundsechzig Tagen?^", "Mehr Geld,", "als es auf der", "*ganzen Welt* gibt."], False),
 ("frage", ["Was hättest du genommen?"], True),
 ("komm", ["Schreib A, B oder C."], True),
 ("folg", ["Und folg mir. Kostet dich keinen Cent."], True),
]
SC = [("s1","hook",-0.3),("s2","wahl",-0.2),("s3","t1",-0.2),("s4","spott",-0.2),("s5","t20",-0.2),("s6","t27",-0.2),("s7","dann",-0.2),("s8","t30",-0.2),("s9","verrueckt",-0.2),("s10","schach",-0.2),("s11","frage",-0.05)]
HUD = {"show":F("t1",-0.2),"hide":F("frage",-0.05),"label":"TAG 1 / 30","unit":"","sub":"DEIN CENT · VERDOPPELT","chipLabel":"VON 1 MIO",
  "steps":[{"at":"t1","off":-0.2,"value":0,"chip":1},{"at":"t25","off":0.3,"value":0,"chip":17},{"at":"t27","off":0.3,"value":0,"chip":67},{"at":"t28","off":0.3,"value":0,"chip":100}]}
IA = [{"type":"follow","at":"t20","off":1.6,"dur":2.6,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
      {"type":"like","at":"haelfte","off":0.6,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
      {"type":"comment","at":"komm","off":0,"dur":1.7,"text":"SCHREIB A, B ODER C"},
      {"type":"follow","at":"folg","off":0,"dur":2.6,"text":"FOLG MIR – <span class='y'>0,00 €</span>"}]
SFX = [{"type":"ding","at":"hook","off":0},{"type":"ding","at":"t1","off":0},{"type":"ding","at":"t10","off":0},{"type":"ding","at":"t20","off":0},{"type":"rise","at":"t25","off":0,"dur":3},
       {"type":"heartbeat","at":"t27","off":1,"dur":2},{"type":"riser","at":"dann","off":0},{"type":"boom","at":"t28","off":1.0},{"type":"ding","at":"verrueckt","off":0},{"type":"rise","at":"schach","off":0.5,"dur":2.5},{"type":"ding","at":"frage","off":-0.2}]
TAGS = {"hook":"[curious]","loop":"[mischievously]","wahl":"[amused]","t1":"[calmly]","t10":"[amused]","spott":"[sarcastically]","t20":"[calmly]","t25":"[curious]","t27":"[nervous]",
        "dann":"[whispers]","t28":"[excited]","t30":"[dramatically]","verrueckt":"[excited]","haelfte":"[surprised]","schach":"[dramatically]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}
build(slug, title, L, SC, HUD, IA, SFX)
p = Path("/home/user/tiktok-videos/videos") / slug
prompt = " ".join(f"{TAGS.get(i, '')} " + re.sub(r"[*^~]", "", " ".join(ch)) for i, ch, _ in L).replace("  ", " ").strip()
(p / "script_v3.txt").write_text(prompt + "\n", encoding="utf-8")
print(len(prompt), len(re.sub(r"\[[^\]]*\]", "", prompt).split())); print(prompt)
