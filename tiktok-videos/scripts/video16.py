# Skript + Timing für Video 16 (Fingerknacken). Klassischer Hook (v3-Regeln), Folgen-Satz am Ende.
import importlib.util
spec = importlib.util.spec_from_file_location("b2", "/home/user/tiktok-videos/scripts/batch2_lib.py"); b2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b2)
build, F = b2.build, b2.F
build("16-finger-knacken", "Was passiert, wenn du jeden Tag deine Finger knackst?", [
 ("hook", ["Du knackst jeden Tag deine Finger."], True),
 ("loop", ["Alle sagen:", "Davon kriegst du *Arthrose.*", "Am Ende siehst du,", "was nach ^fünfzig Jahren^", "wirklich passiert."], False),
 ("frage1", ["^Was knackt da eigentlich?^"], False),
 ("blase", ["Nicht deine Knochen.", "Im Gelenk ist Flüssigkeit.", "Ziehst du am Finger,", "sinkt der Druck.", "Und blitzschnell", "entsteht eine ~Gasblase.~", "Das ist das *Knacken.*"], False),
 ("dann", ["^Und dann?^"], False),
 ("pause", ["Musst du warten.", "Erst nach rund", "^zwanzig Minuten^", "knackt derselbe Finger", "wieder."], False),
 ("jahre", ["^Zehn Jahre später.^"], False),
 ("studie", ["Eine Studie", "mit dreihundert Menschen", "fand: Knacker hatten öfter", "*geschwollene Hände*", "und weniger Kraft", "im Griff."], False),
 ("arthrose", ["Aber Arthrose?", "~Kein Unterschied.~"], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("unger", ["Ein Arzt knackte", "fünfzig Jahre lang", "nur die Finger", "seiner *linken* Hand.", "Die rechte", "ließ er in Ruhe.", "Am Ende:", "beide Hände ~gesund.~"], False),
 ("fazit", ["Also: Knacken", "macht keine Arthrose.", "Aber tut es weh,", "geh zum ^Arzt.^"], False),
 ("frage", ["Knackst du auch jeden Tag?"], True),
 ("komm", ["Schreib A, B oder C in die Kommentare."], True),
 ("folg", ["Und folg mir. Bevor du wieder knackst."], True),
], [("s1","hook",-0.3),("s2","frage1",-0.2),("s3","dann",-0.2),("s4","jahre",-0.2),("s5","verrueckt",-0.2),("s6","fazit",-0.2),("s7","frage",-0.05)],
 {"show": F("frage1",-0.2), "hide": F("frage",-0.05), "label": "GEKNACKT", "unit": "MAL", "sub": "PRO FINGER · ZWEIMAL AM TAG", "chipLabel": "GELENK",
  "steps": [{"at":"frage1","off":-0.2,"value":1,"chip":100},{"at":"dann","off":0,"value":2,"chip":100},{"at":"jahre","off":0,"value":7300,"chip":100},
            {"at":"studie","off":2.6,"value":7300,"chip":70},{"at":"arthrose","off":0.6,"value":7300,"chip":90},{"at":"unger","off":1.0,"value":36500,"chip":90},
            {"at":"unger","off":5.5,"value":36500,"chip":100}]},
 [{"type":"save","at":"pause","off":0.5,"dur":2.6,"text":"SCHICK'S DEM <span class='y'>FINGERKNACKER</span>"},
  {"type":"follow","at":"studie","off":0.3,"dur":2.6,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"unger","off":3.0,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB A, B ODER C"},
  {"type":"follow","at":"folg","off":0,"dur":2.6,"text":"FOLG MIR – <span class='y'>KNACK!</span>"}],
 [{"type":"riser","at":"hook","off":0.0},{"type":"ding","at":"frage1","off":0},{"type":"glitch","at":"blase","off":3.4},{"type":"ding","at":"dann","off":0},
  {"type":"heartbeat","at":"studie","off":2.4,"dur":2.0},{"type":"ding","at":"verrueckt","off":0},{"type":"rise","at":"unger","off":3.5,"dur":3},{"type":"ding","at":"frage","off":-0.2}])
