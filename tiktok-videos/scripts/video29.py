# Video 29: Einen Tag lang Dexter (dramatischer Hook, v3-Stimme) – keine Gewaltdarstellung, Realitäts-Check am Ende
import importlib.util, json, re
from pathlib import Path
spec = importlib.util.spec_from_file_location("b2", "/home/user/tiktok-videos/scripts/batch2_lib.py"); b2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b2)
build, F = b2.build, b2.F
slug, title = "29-einen-tag-dexter", "Was wäre, wenn du einen Tag lang Dexter wärst?"
L = [
 ("hook", ["Du bist einen Tag Dexter."], True),
 ("kata", ["Und keiner", "kennt dein *Geheimnis.*"], False),
 ("loop", ["Am Ende siehst du,", "wie lange", "es ^wirklich^ geheim bleibt."], False),
 ("m7", ["^Sieben Uhr.^", "Du bringst Donuts mit", "und lächelst."], False),
 ("job", ["Du analysierst", "^Blutspuren^", "für die Polizei."], False),
 ("spur", ["Ist ein Tropfen ^rund,^", "fiel er gerade.", "Ist er ^länglich,^", "kam er schräg."], False),
 ("m18", ["^Achtzehn Uhr.^", "Jetzt meldet sich", "dein *dunkler Begleiter.*"], False),
 ("code", ["Dein Kodex:", "Nur wer selbst", "Schlimmes getan hat,", "landet auf", "deiner *Liste.*"], False),
 ("psych", ["Gar nicht so selten:", "Etwa ^einer von hundert^", "Menschen hat", "starke Merkmale", "von Psychopathie."], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("real", ["Im echten Leben", "fliegst du *schnell* auf.", "In Deutschland", "werden über", "^neunzig Prozent^", "aller Morde aufgeklärt."], False),
 ("dna", ["Du verlierst", "jeden Tag", "^Hunderte Millionen^", "Hautzellen.", "Schon ^zehn^ davon", "können reichen", "für ein *DNA-Profil.*"], False),
 ("ende", ["Dein Geheimnis", "hält nur", "im ^Fernsehen.^"], False),
 ("frage", ["Wärst du gern einen Tag Dexter?"], True),
 ("komm", ["Schreib A, B oder C."], True),
 ("folg", ["Und folg mir. Ich verrate es keinem."], True),
]
SC = [("s1","hook",-0.3),("s2","m7",-0.2),("s3","job",-0.2),("s4","spur",-0.2),("s5","m18",-0.2),("s6","code",-0.2),("s7","psych",-0.2),("s8","verrueckt",-0.2),("s9","dna",-0.2),("s10","ende",-0.2),("s11","frage",-0.05)]
HUD = {"show":F("m7",-0.2),"hide":F("frage",-0.05),"label":"UHRZEIT","unit":"","sub":"DOPPELLEBEN · FIKTION","chipLabel":"TARNUNG",
  "steps":[{"at":"m7","off":-0.2,"value":0,"chip":100},{"at":"m18","off":0.5,"value":0,"chip":80},{"at":"code","off":1,"value":0,"chip":60},{"at":"real","off":1,"value":0,"chip":20},{"at":"dna","off":2,"value":0,"chip":5}]}
IA = [{"type":"follow","at":"code","off":1.0,"dur":2.6,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
      {"type":"like","at":"dna","off":1.2,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
      {"type":"comment","at":"komm","off":0,"dur":1.7,"text":"SCHREIB A, B ODER C"},
      {"type":"follow","at":"folg","off":0,"dur":2.6,"text":"FOLG MIR – <span class='y'>PSST …</span>"}]
SFX = [{"type":"riser","at":"hook","off":0},{"type":"ding","at":"m7","off":0},{"type":"drip","at":"job","off":1.0},{"type":"drip","at":"spur","off":0.3},{"type":"drip","at":"spur","off":1.6},
       {"type":"heartbeat","at":"m18","off":0.6,"dur":3},{"type":"ding","at":"psych","off":1},{"type":"ding","at":"verrueckt","off":0},{"type":"alarm","at":"real","off":0.6,"dur":1.5},{"type":"rise","at":"dna","off":0.5,"dur":3},{"type":"ding","at":"frage","off":-0.2}]
TAGS = {"hook":"[whispers]","kata":"[dramatically]","loop":"[curious]","m7":"[calmly]","job":"[calmly]","spur":"[curious]","m18":"[whispers]","code":"[serious]","psych":"[surprised]",
        "verrueckt":"[excited]","real":"[serious]","dna":"[dramatically]","ende":"[mischievously]","frage":"[curious]","komm":"[warmly]","folg":"[whispers]"}
build(slug, title, L, SC, HUD, IA, SFX)
p = Path("/home/user/tiktok-videos/videos") / slug
prompt = " ".join(f"{TAGS.get(i, '')} " + re.sub(r"[*^~]", "", " ".join(ch)) for i, ch, _ in L).replace("  ", " ").strip()
(p / "script_v3.txt").write_text(prompt + "\n", encoding="utf-8")
print(len(prompt), len(re.sub(r"\[[^\]]*\]", "", prompt).split())); print(prompt)
