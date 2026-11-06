# Video 27: Die ganze Erde in einem Wohnblock (dramatischer Hook, v3-Stimme)
import importlib.util, json, re
from pathlib import Path
spec = importlib.util.spec_from_file_location("b2", "/home/user/tiktok-videos/scripts/batch2_lib.py"); b2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b2)
build, F = b2.build, b2.F
slug, title = "27-erde-im-wohnblock", "Was wäre, wenn die ganze Erde in einem Wohnblock leben würde?"
L = [
 ("hook", ["Alle Menschen. Ein Wohnblock."], True),
 ("kata", ["Und das wird", "zum *Albtraum.*"], False),
 ("loop", ["Am Ende siehst du,", "warum die Erde", "^trotzdem^ nicht leer wird."], False),
 ("zahlen", ["^Acht Komma zwei^", "Milliarden Menschen.", "Jeder bekommt", "^zwanzig Quadratmeter.^"], False),
 ("turm", ["Der Block hat", "^zweihundertfünfzig^", "Stockwerke.", "*Einen Kilometer* hoch.", "Grundfläche:", "kleiner als ^Berlin.^"], False),
 ("etage", ["Auf jeder Etage", "^dreiunddreißig Millionen^", "Menschen."], False),
 ("licht", ["Erstes Problem:", "*Licht.*"], False),
 ("fenster", ["Nur ^zwei von tausend^", "Wohnungen", "haben ein Fenster.", "Alle anderen", "sehen *nie wieder*", "die Sonne."], False),
 ("weg", ["Und raus willst du?", "Bis zum Ausgang", "läufst du", "^fast drei Stunden.^"], False),
 ("hunger", ["Dann kommt", "der *Hunger.*"], False),
 ("essen", ["Der Block braucht", "jeden Tag", "^fünfzehn Millionen^", "Tonnen Essen.", "Das sind", "^sechshunderttausend^", "Lastwagen.", "*Jeden Tag.*"], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("frei", ["Der Rest der Erde", "wäre ~menschenleer.~"], False),
 ("twist", ["Aber leer wird sie", "*trotzdem nicht.*", "Denn unsere Felder", "brauchen weiter", "die ^Hälfte^", "des bewohnbaren Landes."], False),
 ("frage", ["Würdest du einziehen?"], True),
 ("komm", ["Schreib A, B oder C."], True),
 ("folg", ["Und folg mir. Bevor die Aufzüge voll sind."], True),
]
SC = [("s1","hook",-0.3),("s2","zahlen",-0.2),("s3","turm",-0.2),("s4","etage",-0.2),("s5","licht",-0.2),("s6","weg",-0.2),("s7","hunger",-0.2),("s8","verrueckt",-0.2),("s9","twist",-0.2),("s10","frage",-0.05)]
HUD = {"show":F("zahlen",-0.2),"hide":F("frage",-0.05),"label":"BEWOHNER","unit":"","sub":"EIN WOHNBLOCK · FIKTION","chipLabel":"LEBENSQUALITÄT",
  "steps":[{"at":"zahlen","off":-0.2,"value":0,"chip":90},{"at":"etage","off":0.5,"value":0,"chip":65},{"at":"fenster","off":1,"value":0,"chip":30},{"at":"weg","off":1.5,"value":0,"chip":20},{"at":"essen","off":2,"value":0,"chip":10},{"at":"frei","off":0.5,"value":0,"chip":60},{"at":"twist","off":1,"value":0,"chip":40}]}
IA = [{"type":"follow","at":"fenster","off":0.6,"dur":2.6,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
      {"type":"like","at":"frei","off":1.2,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
      {"type":"comment","at":"komm","off":0,"dur":1.7,"text":"SCHREIB A, B ODER C"},
      {"type":"follow","at":"folg","off":0,"dur":2.6,"text":"FOLG MIR – <span class='y'>AUFZUG FREI</span>"}]
SFX = [{"type":"riser","at":"hook","off":0},{"type":"ding","at":"zahlen","off":0},{"type":"rise","at":"turm","off":0.3,"dur":3},{"type":"ding","at":"etage","off":0.3},
       {"type":"flicker","at":"licht","off":0.6},{"type":"alarm","at":"hunger","off":0,"dur":1},{"type":"ding","at":"verrueckt","off":0},{"type":"rise","at":"twist","off":0.5,"dur":2.5},{"type":"ding","at":"frage","off":-0.2}]
TAGS = {"hook":"[dramatically]","kata":"[dramatically]","loop":"[curious]","zahlen":"[calmly]","turm":"[serious]","etage":"[surprised]","licht":"[nervous]","fenster":"[serious]","weg":"[sarcastically]",
        "hunger":"[dramatically]","essen":"[urgent]","verrueckt":"[excited]","frei":"[warmly]","twist":"[serious]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}
build(slug, title, L, SC, HUD, IA, SFX)
p = Path("/home/user/tiktok-videos/videos") / slug
prompt = " ".join(f"{TAGS.get(i, '')} " + re.sub(r"[*^~]", "", " ".join(ch)) for i, ch, _ in L).replace("  ", " ").strip()
(p / "script_v3.txt").write_text(prompt + "\n", encoding="utf-8")
json.dump({"key": 1}, open(p / ".hookkey.json", "w"))
print(len(prompt), len(re.sub(r"\[[^\]]*\]", "", prompt).split())); print(prompt)
