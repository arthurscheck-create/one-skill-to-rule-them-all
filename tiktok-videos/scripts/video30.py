# Video 30: Einen Tag lang Walter White (dramatisch ohne roten Blitz, v3-Stimme) – keine Drogen-Details, Fokus Doppelleben + Geld-Twist
import importlib.util, json, re
from pathlib import Path
spec = importlib.util.spec_from_file_location("b2", "/home/user/tiktok-videos/scripts/batch2_lib.py"); b2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b2)
build, F = b2.build, b2.F
slug, title = "30-einen-tag-walter-white", "Was wäre, wenn du einen Tag lang Walter White wärst?"
L = [
 ("hook", ["Du bist einen Tag Walter White."], True),
 ("kata", ["Morgens Lehrer.", "Abends *Heisenberg.*"], False),
 ("loop", ["Am Ende siehst du,", "warum ^das Geld^", "dein größtes Problem wird."], False),
 ("m7", ["^Sieben Uhr.^", "Du unterrichtest Chemie", "für unter", "^fünfzigtausend Dollar^", "im Jahr."], False),
 ("diag", ["Dann die Diagnose:", "*Lungenkrebs.*", "Die Behandlung", "kostet ein Vermögen."], False),
 ("plan", ["Du rechnest aus:", "Deine Familie braucht", "^siebenhundertsiebenunddreißigtausend^", "Dollar."], False),
 ("m18", ["^Achtzehn Uhr.^", "Hut auf.", "Jetzt bist du", "*Heisenberg.*"], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("geld", ["Am Ende hast du", "rund ^achtzig Millionen^", "in bar.", "Das sind", "^achthundert Kilo^", "Geldscheine."], False),
 ("bank", ["Ausgeben?", "*Kaum möglich.*", "Banken melden", "jede Bareinzahlung", "über ^zehntausend Dollar^", "an den Staat."], False),
 ("ende", ["Darum vergräbt", "Walter sein Geld", "in Fässern", "^in der Wüste.^"], False),
 ("frage", ["Lehrer bleiben oder Heisenberg werden?"], True),
 ("komm", ["Schreib A, B oder C."], True),
 ("folg", ["Und folg mir. Sag meinen Namen."], True),
]
SC = [("s1","hook",-0.3),("s2","m7",-0.2),("s3","diag",-0.2),("s4","plan",-0.2),("s5","m18",-0.2),("s6","verrueckt",-0.2),("s7","bank",-0.2),("s8","ende",-0.2),("s9","frage",-0.05)]
HUD = {"show":F("m7",-0.2),"hide":F("frage",-0.05),"label":"GEHALT","unit":"","sub":"DOPPELLEBEN · FIKTION","chipLabel":"TARNUNG",
  "steps":[{"at":"m7","off":-0.2,"value":0,"chip":100},{"at":"m18","off":0.5,"value":0,"chip":75},{"at":"geld","off":2,"value":0,"chip":40},{"at":"bank","off":2,"value":0,"chip":10}]}
IA = [{"type":"follow","at":"plan","off":1.0,"dur":2.6,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
      {"type":"like","at":"bank","off":1.5,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
      {"type":"comment","at":"komm","off":0,"dur":1.7,"text":"SCHREIB A, B ODER C"},
      {"type":"follow","at":"folg","off":0,"dur":2.6,"text":"FOLG MIR – <span class='y'>SAY MY NAME</span>"}]
SFX = [{"type":"riser","at":"hook","off":0},{"type":"ding","at":"m7","off":0},{"type":"heartbeat","at":"diag","off":0.8,"dur":2.5},{"type":"ding","at":"plan","off":1.5},
       {"type":"rise","at":"m18","off":0.3,"dur":2},{"type":"ding","at":"verrueckt","off":0},{"type":"alarm","at":"bank","off":1.5,"dur":1.5},{"type":"rise","at":"ende","off":0.3,"dur":2.5},{"type":"ding","at":"frage","off":-0.2}]
TAGS = {"hook":"[whispers]","kata":"[dramatically]","loop":"[curious]","m7":"[calmly]","diag":"[sad]","plan":"[serious]","m18":"[dramatically]","verrueckt":"[excited]",
        "geld":"[surprised]","bank":"[mischievously]","ende":"[serious]","frage":"[curious]","komm":"[warmly]","folg":"[dramatically]"}
build(slug, title, L, SC, HUD, IA, SFX)
p = Path("/home/user/tiktok-videos/videos") / slug
prompt = " ".join(f"{TAGS.get(i, '')} " + re.sub(r"[*^~]", "", " ".join(ch)) for i, ch, _ in L).replace("  ", " ").strip()
(p / "script_v3.txt").write_text(prompt + "\n", encoding="utf-8")
print(len(prompt), len(re.sub(r"\[[^\]]*\]", "", prompt).split())); print(prompt)
