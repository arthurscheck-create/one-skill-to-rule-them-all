# Video 31: Einen Tag lang Reza (Persischstunden) – klassischer, ernster Hook, offene Frage am Ende, keine Gewalt/NS-Symbole
import importlib.util, json, re
from pathlib import Path
spec = importlib.util.spec_from_file_location("b2", "/home/user/tiktok-videos/scripts/batch2_lib.py"); b2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b2)
build, F = b2.build, b2.F
slug, title = "31-einen-tag-reza", "Was wäre, wenn du einen Tag lang Reza aus „Persischstunden“ wärst?"
L = [
 ("hook", ["Du bist ab heute Reza."], True),
 ("loop", ["Frankreich,", "^neunzehnhundertzweiundvierzig.^", "Am Ende siehst du,", "was aus deiner", "^erfundenen Sprache^ wird."], False),
 ("luege", ["Du bist Jude.", "Aber du sagst,", "du bist ^Perser.^", "Diese Lüge", "rettet dir das Leben."], False),
 ("koch", ["Dann der Befehl:", "Ein Hauptsturmführer", "will ^Persisch^ lernen.", "Von dir."], False),
 ("problem", ["Das Problem:", "Du sprichst", "*kein einziges Wort.*"], False),
 ("erfinden", ["Also erfindest du", "jeden Tag", "^neue Wörter.^"], False),
 ("baum", ["Er fragt:", "Was heißt ^Baum?^", "Du sagst:", "^Radj.^"], False),
 ("gefahr", ["Eine Woche später", "fragt er wieder.", "Vergisst du", "*ein einziges Wort,*", "fliegt alles auf."], False),
 ("trick", ["Dein Trick:", "Du baust die Wörter", "aus den ^Namen^", "der Häftlinge,", "die du ins Lagerbuch", "schreibst."], False),
 ("wende", ["Und am Ende?"], False),
 ("ende", ["Die Akten", "werden *verbrannt.*", "Aber du kennst", "^zweitausendachthundertvierzig^", "Namen auswendig."], False),
 ("mahn", ["Deine erfundene Sprache", "hat sie ~bewahrt.~"], False),
 ("frage", ["Kanntest du diesen Film?"], True),
 ("komm", ["Schreib es in die Kommentare."], True),
 ("folg", ["Und folg mir für mehr Geschichten wie diese."], True),
]
SC = [("s1","hook",-0.3),("s2","luege",-0.2),("s3","koch",-0.2),("s4","problem",-0.2),("s5","baum",-0.2),("s6","gefahr",-0.2),("s7","trick",-0.2),("s8","wende",-0.2),("s9","mahn",-0.2),("s10","frage",-0.05)]
HUD = {"show":F("koch",-0.2),"hide":F("frage",-0.05),"label":"ERFUNDENE WÖRTER","unit":"","sub":"NACH DEM FILM „PERSISCHSTUNDEN“","chipLabel":"TARNUNG",
  "steps":[{"at":"koch","off":-0.2,"value":0,"chip":70},{"at":"problem","off":0.5,"value":0,"chip":30},{"at":"baum","off":1.5,"value":0,"chip":55},{"at":"gefahr","off":1.5,"value":0,"chip":20},{"at":"trick","off":2,"value":0,"chip":80}]}
IA = [{"type":"follow","at":"trick","off":1.0,"dur":2.6,"text":"FOLG FÜR MEHR <span class='y'>GESCHICHTEN</span>"},
      {"type":"comment","at":"komm","off":0,"dur":1.7,"text":"SCHREIB ES IN DIE KOMMENTARE"},
      {"type":"follow","at":"folg","off":0,"dur":2.6,"text":"FOLG MIR – <span class='y'>NIE VERGESSEN</span>"}]
SFX = [{"type":"ding","at":"loop","off":0.2},{"type":"ding","at":"koch","off":0},{"type":"ding","at":"baum","off":2.0},{"type":"heartbeat","at":"gefahr","off":0.8,"dur":3},{"type":"rise","at":"ende","off":1.0,"dur":3},{"type":"ding","at":"frage","off":-0.2}]
TAGS = {"hook":"[serious]","loop":"[softly]","luege":"[serious]","koch":"[nervous]","problem":"[nervous]","erfinden":"[calmly]","baum":"[whispers]","gefahr":"[nervous]","trick":"[calmly]",
        "wende":"[softly]","ende":"[serious]","mahn":"[softly]","frage":"[curious]","komm":"[warmly]","folg":"[warmly]"}
build(slug, title, L, SC, HUD, IA, SFX)
p = Path("/home/user/tiktok-videos/videos") / slug
prompt = " ".join(f"{TAGS.get(i, '')} " + re.sub(r"[*^~]", "", " ".join(ch)) for i, ch, _ in L).replace("  ", " ").strip()
(p / "script_v3.txt").write_text(prompt + "\n", encoding="utf-8")
print(len(prompt), len(re.sub(r"\[[^\]]*\]", "", prompt).split())); print(prompt)
