# Skripte für Serie 2 (Videos 08–10). Erzeugt timing.js + script.txt je Projekt.
import json, re
from pathlib import Path
ROOT = Path("/home/user/tiktok-videos")

def build(slug, title, L, scenes, hud, interact, sfx):
    t = 0.3; lines = []
    for id, ch, nc in L:
        w = len(" ".join(ch).split()); d = w / 2.3 + 0.2
        e = {"id": id, "t0": round(t, 2), "t1": round(t + d, 2), "chunks": ch}
        if nc: e["noCap"] = True
        lines.append(e); t += d + 0.4
    T = {"title": title, "duration": round(t + 2, 2), "voice": None, "lines": lines,
         "scenes": [{"id": s, "at": a, "off": o} for s, a, o in scenes], "hud": hud, "interact": interact, "sfx": sfx}
    p = ROOT / "videos" / slug; p.mkdir(parents=True, exist_ok=True)
    (p / "timing.js").write_text("window.TIMING = " + json.dumps(T, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    text = " ".join(re.sub(r"[*^~]", "", " ".join(l["chunks"])) for l in lines)
    (p / "script.txt").write_text(text + "\n", encoding="utf-8")
    print(f"{slug}: {len(text.split())} Wörter, ~{T['duration']}s")

F = lambda at, off=0.0: {"at": at, "off": off}

# ---------------- 08 Alle springen ----------------
build("08-alle-springen", "Was wäre, wenn alle Menschen gleichzeitig springen?", [
 ("hook", ["Was wäre, wenn alle Menschen auf der Erde gleichzeitig springen?"], True),
 ("loop", ["Das Gefährlichste", "passiert erst", "^nach der Landung.^"], False),
 ("treffen", ["Damit es wirkt,", "müssen alle", "an einem Ort", "stehen."], False),
 ("mallorca", ["Acht Milliarden", "Menschen", "passen dicht gedrängt", "auf eine Fläche", "so groß wie", "^Mallorca.^"], False),
 ("zaehlen", ["^Drei.^", "^Zwei.^", "^Eins.^"], False),
 ("sprung", ["*Sprung!*"], False),
 ("gewicht", ["Zusammen wiegen wir", "rund ^fünfhundert^", "^Millionen Tonnen.^"], False),
 ("erde", ["Aber die Erde", "ist ^zwölf Billionen^", "^Mal^ schwerer."], False),
 ("atom", ["Sie bewegt sich", "weniger als", "die Breite", "eines *Atoms.*"], False),
 ("landung", ["^Die Landung.^"], False),
 ("knall", ["Ein", "*ohrenbetäubender*", "Knall."], False),
 ("beben", ["Messgeräte", "schlagen aus.", "Aber spüren", "kann man das Beben", "~kaum.~"], False),
 ("danach", ["Und jetzt", "kommt das", "*Problem.*"], False),
 ("heim", ["Acht Milliarden", "Menschen", "wollen", "^nach Hause.^"], False),
 ("netz", ["Die Handynetze", "brechen *sofort*", "zusammen."], False),
 ("flug", ["Flughafen und Fähren", "schaffen vielleicht", "^hunderttausend^", "Menschen am Tag."], False),
 ("jahre", ["Bis alle weg sind,", "dauert es", "über ^zweihundert^", "^Jahre.^"], False),
 ("hunger", ["Und schon", "nach wenigen Tagen", "gibt es", "*kein Essen*", "und *kein Wasser*", "mehr."], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("fakt", ["Du bewegst", "die Erde", "bei ~jedem~", "Sprung.", "Auch heute.", "Nur eben", "~winzig~ wenig."], False),
 ("frage", ["Wie würdest du von Mallorca wegkommen?"], True),
 ("komm", ["Schreib es in die Kommentare."], True),
], [("s1","hook",-0.3),("s2","treffen",-0.2),("s3","zaehlen",-0.2),("s4","sprung",-0.15),("s5","gewicht",-0.2),("s6","atom",-0.2),
    ("s7","landung",-0.2),("s8","danach",-0.2),("s9","flug",-0.2),("s10","hunger",-0.2),("s11","verrueckt",-0.2),("s12","frage",-0.3)],
 {"show": F("treffen",-0.2), "hide": F("frage",-0.3), "label": "SPRUNG IN", "unit": "", "sub": "WAS WÄRE WENN · FIKTION", "chipLabel": "SICHERHEIT",
  "countdown": {"from": 3, "fmt": "s.mmm", "start": F("zaehlen",0.0), "end": F("sprung",0.0)},
  "steps": [{"at":"treffen","off":-0.2,"value":0,"chip":100},{"at":"netz","off":0.2,"value":0,"chip":62},{"at":"jahre","off":0.3,"value":0,"chip":35},{"at":"hunger","off":0.4,"value":0,"chip":8}]},
 [{"type":"follow","at":"beben","off":0.3,"dur":2.8,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"fakt","off":0.3,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB'S IN DIE KOMMENTARE"}],
 [{"type":"riser","at":"zaehlen","off":-0.6},{"type":"boom","at":"knall","off":0},{"type":"glitch","at":"netz","off":0.4},
  {"type":"heartbeat","at":"hunger","off":0,"dur":2.5},{"type":"rise","at":"fakt","off":0,"dur":3},{"type":"ding","at":"frage","off":-0.2}])

# ---------------- 09 Nie mehr schlafen ----------------
build("09-nie-schlafen", "Was wäre, wenn niemand mehr schlafen müsste?", [
 ("hook", ["Was wäre, wenn kein Mensch mehr schlafen müsste?"], True),
 ("loop", ["Klingt perfekt.", "Aber am Ende", "verlierst du etwas,", "an das ^keiner denkt.^"], False),
 ("nacht1", ["^Die erste Nacht.^"], False),
 ("wach", ["Es ist ^drei Uhr^", "morgens.", "Und du bist", "~hellwach.~"], False),
 ("zeit", ["Plötzlich hast du", "jeden Tag", "^acht Stunden^", "mehr."], False),
 ("jahr", ["Das sind fast", "^dreitausend^", "^Stunden^", "im Jahr."], False),
 ("leben", ["Über dein Leben", "gewinnst du", "rund", "^fünfundzwanzig^", "^Jahre.^"], False),
 ("woche", ["^Eine Woche später.^"], False),
 ("stadt", ["Die Städte", "schlafen *nie mehr.*", "Supermärkte,", "Schulen, Büros:", "alles hat", "^rund um die Uhr^", "offen."], False),
 ("strom", ["Nachts brennt", "*überall* Licht.", "Der Stromverbrauch", "*explodiert.*"], False),
 ("zimmer", ["Und Schlafzimmer?", "Braucht *keiner*", "mehr."], False),
 ("heute", ["Dabei wäre das", "heute", "*lebensgefährlich.*"], False),
 ("gardner", ["Ein Schüler", "blieb", "^elf Tage^", "wach.", "Am Ende sah er", "Dinge,", "die gar nicht", "*da waren.*"], False),
 ("gehirn", ["Denn im Schlaf", "*putzt* sich", "dein Gehirn.", "Es spült", "Abfallstoffe", "raus."], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("gen", ["Manche Menschen", "brauchen schon heute", "nur", "^sechs Stunden.^", "Wegen eines", "~einzigen Gens.~"], False),
 ("traum", ["Aber ohne Schlaf", "würdest du", "*nie wieder*", "träumen."], False),
 ("frage", ["Wofür würdest du die acht Stunden nutzen?"], True),
 ("komm", ["Schreib A, B oder C in die Kommentare."], True),
], [("s1","hook",-0.3),("s2","nacht1",-0.2),("s3","zeit",-0.2),("s4","leben",-0.2),("s5","woche",-0.2),("s6","strom",-0.2),
    ("s7","zimmer",-0.2),("s8","heute",-0.2),("s9","gehirn",-0.2),("s10","verrueckt",-0.2),("s11","traum",-0.2),("s12","frage",-0.3)],
 {"show": F("nacht1",-0.2), "hide": F("frage",-0.3), "label": "OHNE SCHLAF SEIT", "unit": "TAGE", "sub": "WAS WÄRE WENN · FIKTION", "chipLabel": "FREIZEIT",
  "steps": [{"at":"nacht1","off":-0.2,"value":1,"chip":30},{"at":"zeit","off":0.4,"value":1,"chip":100},{"at":"woche","off":-0.2,"value":7,"chip":100},{"at":"traum","off":0.6,"value":7,"chip":100}]},
 [{"type":"follow","at":"zimmer","off":0.2,"dur":2.8,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"gen","off":0.3,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB A, B ODER C"}],
 [{"type":"alarm","at":"nacht1","off":-0.2},{"type":"ding","at":"zeit","off":0.4},{"type":"flicker","at":"strom","off":0},{"type":"heartbeat","at":"gardner","off":1.0,"dur":2.5},
  {"type":"glitch","at":"gardner","off":2.6},{"type":"rise","at":"gen","off":0,"dur":3},{"type":"boom","at":"traum","off":0.8},{"type":"ding","at":"frage","off":-0.2}])

# ---------------- 10 Atomalarm ----------------
build("10-atomalarm", "Atomalarm: Du hast 10 Minuten – was tust du?", [
 ("hook", ["Atomalarm! Du hast nur zehn Minuten. Was tust du?"], True),
 ("loop", ["Die ^wichtigste Regel^", "kommt ganz", "am Ende."], False),
 ("sirene", ["Die Sirenen heulen.", "^Eine Minute^ lang,", "auf und ab."], False),
 ("handy", ["Dein Handy", "*schrillt.*", "Warnung:", "*Angriff.*"], False),
 ("min9", ["^Noch neun Minuten.^"], False),
 ("auto", ["Ins Auto springen?", "*Falsch.*", "Die Straßen", "sind sofort", "*verstopft.*", "Und ein Auto", "schützt dich *kaum.*"], False),
 ("keller", ["Geh in den", "~Keller.~", "Dicke Wände", "und Erde", "halten die Strahlung", "~ab.~"], False),
 ("innen", ["Kein Keller?", "Dann in einen Raum", "ganz innen", "im Gebäude."], False),
 ("min5", ["^Noch fünf Minuten.^"], False),
 ("fenster", ["Weg von den Fenstern.", "Die Druckwelle", "lässt Glas", "wie *Geschosse*", "durch den Raum fliegen."], False),
 ("zu", ["Fenster und Türen", "^zu.^", "Lüftung", "^aus.^"], False),
 ("vorrat", ["Nimm Wasser", "und ein ^Radio^", "mit Batterien", "mit."], False),
 ("min1", ["^Noch eine Minute.^"], False),
 ("blitz", ["Ein *greller Blitz.*", "Schau *nicht* hin!"], False),
 ("flach", ["Wirf dich ^flach^", "auf den Boden.", "Schütz deinen Kopf."], False),
 ("druck", ["Die Druckwelle", "kommt oft erst", "^Sekunden später.^"], False),
 ("regel", ["Und jetzt", "die ^wichtigste Regel:^"], False),
 ("drinnen", ["Bleib ~drinnen.~", "Mindestens", "^vierundzwanzig^", "^Stunden.^"], False),
 ("fallout", ["Draußen fällt", "radioaktiver *Staub*", "vom Himmel."], False),
 ("sieben", ["Aber schon nach", "^sieben Stunden^", "ist seine Strahlung", "um rund", "^neunzig Prozent^", "~gesunken.~"], False),
 ("raus", ["Wer zu früh", "rausgeht,", "riskiert *alles.*"], False),
 ("frage", ["Wo wärst du in zehn Minuten?"], True),
 ("komm", ["Schreib A, B oder C in die Kommentare."], True),
], [("s1","hook",-0.3),("s2","sirene",-0.2),("s3","handy",-0.2),("s4","auto",-0.2),("s5","keller",-0.2),("s6","innen",-0.2),("s7","fenster",-0.2),
    ("s8","vorrat",-0.2),("s9","blitz",-0.15),("s10","druck",-0.2),("s11","drinnen",-0.2),("s12","sieben",-0.2),("s13","frage",-0.3)],
 {"show": F("sirene",-0.2), "hide": F("frage",-0.3), "label": "EINSCHLAG IN", "unit": "", "sub": "WAS WÄRE WENN · FIKTION", "chipLabel": "SCHUTZ",
  "countdown": {"from": 600, "fmt": "mm:ss", "start": F("sirene",-0.2), "end": F("blitz",0.0)},
  "steps": [{"at":"sirene","off":-0.2,"value":0,"chip":5},{"at":"auto","off":1.2,"value":0,"chip":5},{"at":"keller","off":0.6,"value":0,"chip":65},{"at":"fenster","off":0.6,"value":0,"chip":75},
            {"at":"zu","off":0.6,"value":0,"chip":85},{"at":"drinnen","off":0.4,"value":0,"chip":95}]},
 [{"type":"follow","at":"min5","off":0.1,"dur":2.8,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"save","at":"drinnen","off":0.3,"dur":2.8,"text":"SPEICHER DIR DAS <span class='y'>AB</span>"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB A, B ODER C"}],
 [{"type":"alarm","at":"sirene","off":-0.2},{"type":"alarm","at":"handy","off":0.3},{"type":"riser","at":"min1","off":0},{"type":"boom","at":"blitz","off":0},
  {"type":"boom","at":"druck","off":0.6},{"type":"rise","at":"sieben","off":0,"dur":3},{"type":"ding","at":"frage","off":-0.2}])
