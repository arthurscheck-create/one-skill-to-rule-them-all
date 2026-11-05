# Skript + Timing für Video 15 (Rückwärtsgang bei 100 km/h). Dramatischer Hook (v3), Folgen-Satz am Ende.
import importlib.util
spec = importlib.util.spec_from_file_location("b2", "/home/user/tiktok-videos/scripts/batch2_lib.py"); b2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b2)
build, F = b2.build, b2.F
build("15-rueckwaertsgang", "Was passiert, wenn du bei 100 km/h in den Rückwärtsgang schaltest?", [
 ("hook", ["Hundert Sachen. Rückwärtsgang rein."], True),
 ("kata", ["Das kann", "dein Getriebe", "*zerfetzen.*"], False),
 ("loop", ["Und am Ende", "zeige ich dir ein Auto,", "das rückwärts", "fast ^dreihundert^ fährt."], False),
 ("fall1", ["^Fall eins:^", "Automatik."], False),
 ("auto", ["Du ziehst den Hebel", "auf R.", "Und meistens passiert:", "*gar nichts.*", "Der Computer blockiert", "und schaltet einfach", "auf ~Neutral.~"], False),
 ("fall2", ["^Fall zwei:^", "Schaltwagen.", "Und hier", "wird es *brutal.*"], False),
 ("schalt", ["Der Rückwärtsgang", "ist oft", "nicht synchronisiert.", "Du hörst nur", "ein lautes *Krachen.*", "Mit Gewalt", "brechen die Zähne", "der Zahnräder ab."], False),
 ("kupplung", ["Und lässt du dann", "die Kupplung kommen,", "können die Räder", "*blockieren.*", "Bei Tempo hundert", "heißt das:", "Schleudern."], False),
 ("fall3", ["^Fall drei:^", "Elektroauto."], False),
 ("elektro", ["Der Motor", "dreht sich einfach", "andersherum.", "Doch die Software", "sagt: *Nein.*"], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("rekord", ["Ein Elektro-Supersportwagen", "fuhr rückwärts", "über ~zweihundertsiebzig~", "Kilometer pro Stunde.", "Weltrekord."], False),
 ("frage", ["Was würde dein Auto machen?"], True),
 ("komm", ["Schreib A, B oder C in die Kommentare."], True),
 ("folg", ["Und folg mir. Bevor du es selbst ausprobierst."], True),
], [("s1","hook",-0.3),("s2","fall1",-0.2),("s3","fall2",-0.2),("s4","kupplung",-0.2),("s5","fall3",-0.2),("s6","verrueckt",-0.2),("s7","frage",-0.05)],
 {"show": F("fall1",-0.2), "hide": F("frage",-0.05), "label": "TEMPO", "unit": "KM/H", "sub": "WAS WÄRE WENN · NICHT NACHMACHEN", "chipLabel": "GETRIEBE",
  "steps": [{"at":"fall1","off":-0.2,"value":100,"chip":100},{"at":"auto","off":1.2,"value":100,"chip":95},{"at":"schalt","off":2.6,"value":100,"chip":40},
            {"at":"schalt","off":4.6,"value":100,"chip":10},{"at":"kupplung","off":2.0,"value":60,"chip":0},{"at":"fall3","off":-0.2,"value":100,"chip":100},
            {"at":"rekord","off":1.2,"value":275,"chip":100}]},
 [{"type":"save","at":"auto","off":2.0,"dur":2.6,"text":"SPEICHER DAS FÜR DEINE <span class='y'>FAHRSTUNDE</span>"},
  {"type":"follow","at":"kupplung","off":1.0,"dur":2.6,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"rekord","off":1.5,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB A, B ODER C"},
  {"type":"follow","at":"folg","off":0,"dur":2.6,"text":"FOLG MIR – <span class='y'>VOLLGAS</span>"}],
 [{"type":"riser","at":"hook","off":0.0},{"type":"glitch","at":"auto","off":1.2},{"type":"ding","at":"fall1","off":0},{"type":"alarm","at":"auto","off":2.3,"dur":1.2},
  {"type":"glitch","at":"schalt","off":2.4},{"type":"glitch","at":"schalt","off":3.0},{"type":"boom","at":"schalt","off":4.4},{"type":"heartbeat","at":"kupplung","off":1.0,"dur":2.5},
  {"type":"ding","at":"fall3","off":0},{"type":"alarm","at":"elektro","off":2.4,"dur":1.0},{"type":"rise","at":"rekord","off":0.5,"dur":3},{"type":"ding","at":"frage","off":-0.2}])
