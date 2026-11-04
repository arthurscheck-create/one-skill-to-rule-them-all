# Skripte für Serie 1 (Videos 03–07). Erzeugt timing.js je Projekt.
import json, sys, re
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

# ---------------- 03 Erde stoppt ----------------
build("03-erde-stoppt", "Was wäre, wenn die Erde für 5 Sekunden aufhört, sich zu drehen?", [
 ("hook", ["Was wäre, wenn die Erde für fünf Sekunden aufhört, sich zu drehen?"], True),
 ("loop", ["Und die fünfte Sekunde", "ist die ^schlimmste.^"], False),
 ("strasse", ["Du stehst", "ganz normal", "auf der Straße."], False),
 ("speed", ["Aber in Wahrheit", "rast du gerade", "mit über ^tausend^", "^Kilometern^", "pro Stunde", "durchs All."], False),
 ("sek1", ["^Sekunde eins.^"], False),
 ("stop", ["Die Erde", "bleibt *stehen.*", "Du *nicht.*"], False),
 ("fliegen", ["Alles, was nicht", "festgeschraubt ist,", "schießt nach Osten.", "Menschen, Autos,", "ganze Häuser."], False),
 ("sek2", ["^Sekunde zwei.^"], False),
 ("wind", ["Die Luft", "rast weiter.", "Ein *Sturm,*", "stärker als", "jeder Hurrikan."], False),
 ("sek3", ["^Sekunde drei.^"], False),
 ("meer", ["Die Ozeane", "schwappen", "aus ihren Becken.", "Riesige *Tsunamis*", "rollen auf", "die Küsten zu."], False),
 ("sek4", ["^Sekunde vier.^"], False),
 ("beben", ["*Erdbeben*", "und Vulkane", "auf der ganzen Welt."], False),
 ("sek5", ["Und dann:", "^Sekunde fünf.^"], False),
 ("dreht", ["Die Erde", "dreht sich wieder.", "Und alles", "wird ein *zweites Mal*", "herumgeschleudert."], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("fakt", ["Die Erde", "wird wirklich", "*langsamer.*", "Jeder Tag", "wird ein winziges", "bisschen ~länger.~"], False),
 ("frage", ["Hättest du das gewusst?"], True),
 ("komm", ["Schreib es in die Kommentare."], True),
], [("s1","hook",-0.3),("s2","strasse",-0.2),("s3","sek1",-0.2),("s4","fliegen",-0.2),("s5","sek2",-0.2),("s6","sek3",-0.2),("s7","sek4",-0.2),("s8","sek5",-0.2),("s9","verrueckt",-0.2),("s10","frage",-0.3)],
 {"show": F("strasse",-0.2), "hide": F("frage",-0.3), "label": "ERDE DREHT WIEDER IN", "unit": "", "sub": "WAS WÄRE WENN · FIKTION", "chipLabel": "DREHUNG",
  "countdown": {"from": 5, "fmt": "s.mmm", "start": F("sek1",-0.2), "end": F("dreht",0.0)},
  "steps": [{"at":"strasse","off":-0.2,"value":0,"chip":100},{"at":"stop","off":0,"value":0,"chip":0},{"at":"dreht","off":0,"value":0,"chip":100}]},
 [{"type":"follow","at":"meer","off":0.3,"dur":2.8,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"fakt","off":0.3,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB'S IN DIE KOMMENTARE"}],
 [{"type":"riser","at":"sek1","off":-1.2},{"type":"boom","at":"stop","off":0},{"type":"rise","at":"fakt","off":0,"dur":3},{"type":"boom","at":"dreht","off":0},{"type":"ding","at":"frage","off":-0.2}])

# ---------------- 04 Männer verschwinden ----------------
build("04-maenner-weg", "Was wäre, wenn alle Männer auf der Erde für immer verschwinden?", [
 ("hook", ["Was wäre, wenn alle Männer auf der Erde für immer verschwinden?"], True),
 ("loop", ["Und am Ende", "entscheidet sich,", "ob die Menschheit", "^überlebt.^"], False),
 ("sek1", ["^Sekunde eins.^"], False),
 ("weg", ["Über ^vier Milliarden^", "Menschen", "sind *weg.*"], False),
 ("autos", ["Autos ohne Fahrer", "*krachen* ineinander."], False),
 ("piloten", ["Flugzeuge", "verlieren ihre Piloten.", "Über ^neunzig Prozent^", "sind Männer."], False),
 ("std1", ["^Stunde eins.^"], False),
 ("bau", ["Baustellen", "stehen *still.*", "Kaum ein Lkw", "fährt mehr."], False),
 ("tag1", ["^Tag eins.^"], False),
 ("jobs", ["Strom, Müllabfuhr,", "Feuerwehr.", "Diese Jobs", "machen bisher", "fast nur Männer."], False),
 ("woche", ["^Eine Woche später.^"], False),
 ("frauen", ["Die Frauen", "übernehmen.", "Und vieles", "läuft ~wieder.~"], False),
 ("monate", ["Aber in", "^neun Monaten^", "kommen die", "*letzten Babys*", "zur Welt."], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("samen", ["In Samenbanken", "lagern", "tiefgekühlte Proben.", "Damit könnte", "die Menschheit", "~weitermachen.~"], False),
 ("jungs", ["Und die Hälfte", "dieser Babys", "wären wieder", "^Jungs.^"], False),
 ("frage", ["Würde die Menschheit überleben?"], True),
 ("komm", ["Schreib A, B oder C in die Kommentare."], True),
], [("s1","hook",-0.3),("s2","sek1",-0.2),("s3","autos",-0.2),("s4","piloten",-0.2),("s5","std1",-0.2),("s6","tag1",-0.2),("s7","woche",-0.2),("s8","monate",-0.2),("s9","verrueckt",-0.2),("s10","frage",-0.3)],
 {"show": F("sek1",-0.2), "hide": F("frage",-0.3), "label": "OHNE MÄNNER SEIT", "unit": "TAGE", "sub": "WAS WÄRE WENN · FIKTION", "chipLabel": "BEVÖLKERUNG",
  "steps": [{"at":"sek1","off":-0.2,"value":0,"chip":100},{"at":"weg","off":0.4,"value":0,"chip":49},{"at":"tag1","off":-0.2,"value":1,"chip":49},{"at":"woche","off":-0.2,"value":7,"chip":49},{"at":"monate","off":0.2,"value":270,"chip":49}]},
 [{"type":"follow","at":"jobs","off":0.3,"dur":2.8,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"samen","off":0.4,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB A, B ODER C"}],
 [{"type":"riser","at":"sek1","off":-1.2},{"type":"boom","at":"weg","off":0},{"type":"glitch","at":"autos","off":0.6},{"type":"heartbeat","at":"monate","off":0,"dur":2.5},{"type":"rise","at":"samen","off":0,"dur":3},{"type":"ding","at":"frage","off":-0.2}])

# ---------------- 05 Asteroid Berlin ----------------
build("05-asteroid-berlin", "Was wäre, wenn ein Asteroid mitten in Berlin einschlägt?", [
 ("hook", ["Was wäre, wenn ein Asteroid mitten in Berlin einschlägt?"], True),
 ("loop", ["Wie weit du", "weg sein musst,", "um zu ^überleben,^", "erfährst du", "am Ende."], False),
 ("alex", ["Du stehst", "am Alexanderplatz.", "Am Himmel:", "ein ^heller Punkt.^"], False),
 ("gross", ["Er ist so groß", "wie ein ^Fußballfeld.^"], False),
 ("schnell", ["Und zwanzig", "Kilometer schnell.", "^Pro Sekunde.^"], False),
 ("zehn", ["^Zehn Sekunden^", "vorher."], False),
 ("hell", ["Er wird", "*heller*", "als die Sonne."], False),
 ("einschlag", ["*Einschlag.*"], False),
 ("feuer", ["Ein Feuerball,", "so heiß", "wie die Oberfläche", "der Sonne."], False),
 ("wucht", ["Die Wucht", "von mehreren", "^tausend Atombomben.^"], False),
 ("krater", ["Ein Krater,", "über einen", "Kilometer breit.", "Genau dort,", "wo der Fernsehturm", "*stand.*"], False),
 ("druck", ["Die Druckwelle", "reißt im Umkreis", "von ^zehn Kilometern^", "*alles* um."], False),
 ("potsdam", ["Selbst in Potsdam", "zerspringen", "noch die Fenster."], False),
 ("sicher", ["Um sicher zu sein,", "müsstest du", "mindestens", "^fünfzig Kilometer^", "weg sein."], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("nasa", ["Die NASA", "hat schon getestet,", "einen Asteroiden", "abzulenken.", "Und es hat", "~funktioniert.~"], False),
 ("frage", ["Was würdest du als Erstes tun?"], True),
 ("komm", ["Schreib A, B oder C in die Kommentare."], True),
], [("s1","hook",-0.3),("s2","alex",-0.2),("s3","gross",-0.2),("s4","zehn",-0.2),("s5","einschlag",-0.15),("s6","wucht",-0.2),("s7","druck",-0.2),("s8","sicher",-0.2),("s9","verrueckt",-0.2),("s10","frage",-0.3)],
 {"show": F("alex",-0.2), "hide": F("einschlag",0.0), "label": "EINSCHLAG IN", "unit": "", "sub": "BERLIN · FIKTION", "chipLabel": "ENTFERNUNG",
  "countdown": {"from": 60, "fmt": "mm:ss", "start": F("alex",-0.2), "end": F("einschlag",0.0)},
  "steps": []},
 [{"type":"follow","at":"druck","off":0.3,"dur":2.8,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"nasa","off":0.4,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB A, B ODER C"}],
 [{"type":"riser","at":"zehn","off":-0.3},{"type":"boom","at":"einschlag","off":0},{"type":"boom","at":"druck","off":0.2},{"type":"glitch","at":"potsdam","off":0.5},{"type":"rise","at":"nasa","off":0,"dur":3},{"type":"ding","at":"frage","off":-0.2}])

# ---------------- 06 Sonne verschwindet ----------------
build("06-sonne-weg", "Was wäre, wenn die Sonne plötzlich verschwindet?", [
 ("hook", ["Was wäre, wenn die Sonne plötzlich verschwindet?"], True),
 ("loop", ["Und es gibt", "einen Ort", "auf der Erde,", "an dem das Leben", "^weitergeht.^"], False),
 ("nichts", ["Erst mal", "merkst du", "*gar nichts.*"], False),
 ("licht", ["Das Licht", "der Sonne", "braucht ^acht Minuten^", "bis zu uns.", "Sie scheint", "einfach weiter."], False),
 ("min8", ["^Minute acht.^"], False),
 ("dunkel", ["Dann:", "*Dunkelheit.*", "Auch der Mond", "geht aus.", "Er leuchtet nur", "durch die Sonne."], False),
 ("schleuder", ["Die Erde", "fliegt geradeaus", "ins All.", "Wie ein Stein", "aus einer Schleuder."], False),
 ("tag1", ["^Tag eins.^"], False),
 ("pflanzen", ["Pflanzen", "bekommen", "kein Licht mehr.", "Sie fangen an", "zu *sterben.*"], False),
 ("woche", ["^Eine Woche.^"], False),
 ("kalt", ["Minus", "^fünfzehn Grad.^", "Überall", "auf der Erde."], False),
 ("jahr", ["^Ein Jahr.^"], False),
 ("eis", ["Minus", "^siebzig Grad.^", "Die Ozeane", "frieren von oben", "*zu.*"], False),
 ("aber", ["Aber", "tief unten", "am Meeresgrund,"], False),
 ("quellen", ["an heißen Quellen,", "gibt es Leben,", "das gar ~keine Sonne~", "braucht."], False),
 ("frage", ["Was würdest du in deinen letzten acht Minuten Licht machen?"], True),
 ("komm", ["Schreib es in die Kommentare."], True),
], [("s1","hook",-0.3),("s2","nichts",-0.2),("s3","min8",-0.2),("s4","schleuder",-0.2),("s5","tag1",-0.2),("s6","woche",-0.2),("s7","jahr",-0.2),("s8","aber",-0.2),("s10","frage",-0.3)],
 {"show": F("nichts",-0.2), "hide": F("dunkel",0.6), "label": "LICHT ERREICHT DICH NOCH", "unit": "", "sub": "WAS WÄRE WENN · FIKTION", "chipLabel": "LICHT",
  "countdown": {"from": 500, "fmt": "mm:ss", "start": F("nichts",-0.2), "end": F("dunkel",0.2)},
  "steps": [{"at":"nichts","off":-0.2,"value":0,"chip":100},{"at":"dunkel","off":0.2,"value":0,"chip":0}]},
 [{"type":"follow","at":"pflanzen","off":0.3,"dur":2.8,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"quellen","off":0.3,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB'S IN DIE KOMMENTARE"}],
 [{"type":"riser","at":"min8","off":-1.2},{"type":"boom","at":"dunkel","off":0.2},{"type":"heartbeat","at":"kalt","off":0,"dur":2.5},{"type":"rise","at":"quellen","off":0,"dur":3},{"type":"ding","at":"frage","off":-0.2}])

# ---------------- 07 Schwerkraft weg ----------------
build("07-schwerkraft-weg", "Was wäre, wenn die Schwerkraft für 5 Sekunden verschwindet?", [
 ("hook", ["Was wäre, wenn die Schwerkraft für fünf Sekunden verschwindet?"], True),
 ("loop", ["Gefährlich wird es", "erst,", "wenn sie ^zurückkommt.^"], False),
 ("sek1", ["^Sekunde eins.^"], False),
 ("sofa", ["Du sitzt", "auf dem Sofa.", "Nichts passiert.", "*Noch.*"], False),
 ("luft", ["Aber die Luft", "wird nicht mehr", "festgehalten.", "Sie strömt", "nach oben", "ins *All.*"], False),
 ("ohren", ["Deine Ohren", "*knacken.*"], False),
 ("sek2", ["^Sekunde zwei.^"], False),
 ("aufstehen", ["Du stehst auf", "und *hebst ab.*", "Ein kleiner Schritt,", "und du schwebst", "zur Decke."], False),
 ("sek3", ["^Sekunde drei.^"], False),
 ("trampolin", ["Ein Kind", "auf dem Trampolin", "fliegt *höher*", "als das Haus."], False),
 ("sek4", ["^Sekunde vier.^"], False),
 ("alles", ["Wasser, Bälle,", "Vögel, Staub.", "Alles treibt", "nach oben."], False),
 ("sek5", ["^Sekunde fünf.^"], False),
 ("zurueck", ["Die Schwerkraft", "ist zurück.", "Und alles,", "was oben ist,", "*kracht* wieder runter."], False),
 ("verrueckt", ["Und das", "^Verrückte?^"], False),
 ("iss", ["Auf der Raumstation", "gibt es fast", "genauso viel", "Schwerkraft", "wie hier."], False),
 ("fallen", ["Die Astronauten", "schweben nur,", "weil sie ständig", "um die Erde", "~fallen.~"], False),
 ("frage", ["Was würdest du in den fünf Sekunden machen?"], True),
 ("komm", ["Schreib A, B oder C in die Kommentare."], True),
], [("s1","hook",-0.3),("s2","sek1",-0.2),("s3","luft",-0.2),("s4","sek2",-0.2),("s5","sek3",-0.2),("s6","sek4",-0.2),("s7","sek5",-0.2),("s8","verrueckt",-0.2),("s10","frage",-0.3)],
 {"show": F("sek1",-0.2), "hide": F("frage",-0.3), "label": "SCHWERKRAFT ZURÜCK IN", "unit": "", "sub": "WAS WÄRE WENN · FIKTION", "chipLabel": "SCHWERKRAFT",
  "countdown": {"from": 5, "fmt": "s.mmm", "start": F("sek1",-0.2), "end": F("zurueck",0.0)},
  "steps": [{"at":"sek1","off":-0.2,"value":0,"chip":0},{"at":"zurueck","off":0,"value":0,"chip":100}]},
 [{"type":"follow","at":"trampolin","off":0.3,"dur":2.8,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
  {"type":"like","at":"fallen","off":0.2,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
  {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB A, B ODER C"}],
 [{"type":"riser","at":"sek1","off":-1.2},{"type":"glitch","at":"ohren","off":0.2},{"type":"boom","at":"zurueck","off":0.4},{"type":"rise","at":"fallen","off":0,"dur":3},{"type":"ding","at":"frage","off":-0.2}])
