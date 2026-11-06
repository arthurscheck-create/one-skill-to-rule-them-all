# Serie 3 (Videos 17–26): Skripte, Timing, getaggte v3-Prompts. Dramatisch: 17,19,20,22,23,26 – klassisch: 18,21,24,25.
import importlib.util, json, re
from pathlib import Path
spec = importlib.util.spec_from_file_location("b2", "/home/user/tiktok-videos/scripts/batch2_lib.py"); b2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(b2)
build, F = b2.build, b2.F
V = []  # (slug, title, lines, scenes, hud, interact, sfx, tags, key)
END = lambda q, folg: [("frage", [q], True), ("komm", ["Schreib A, B oder C in die Kommentare."], True), ("folg", [folg], True)]
VR = ("verrueckt", ["Und das", "^Verrückte?^"], False)
def IA(follow_at, like_at, extra=None):
    l = [{"type":"follow","at":follow_at,"off":0.4,"dur":2.6,"text":"FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"},
         {"type":"like","at":like_at,"off":1.5,"dur":2.6,"text":"LIKE, WENN DU'S NICHT WUSSTEST"},
         {"type":"comment","at":"komm","off":0,"dur":2.2,"text":"SCHREIB A, B ODER C"}]
    if extra: l.append(extra)
    return l
FOLGPILL = lambda w: {"type":"follow","at":"folg","off":0,"dur":2.6,"text":f"FOLG MIR – <span class='y'>{w}</span>"}

V.append(("17-eis-eingebrochen", "Was passiert, wenn du ins Eis einbrichst?", [
 ("hook", ["Du brichst ins Eis ein."], True),
 ("kata", ["Doch nicht die Kälte", "ist dein", "*größter Feind.*"], False),
 ("loop", ["Am Ende kennst du", "die Regel,", "die dein Leben ^rettet.^"], False),
 ("m1", ["^Minute eins.^"], False),
 ("schock", ["Das eiskalte Wasser", "löst einen *Kälteschock* aus.", "Du schnappst nach Luft", "und atmest viel zu schnell.", "Genau jetzt", "schlucken viele Wasser."], False),
 ("regel1", ["Deshalb:", "^Ruhig atmen.^", "Kopf über Wasser.", "Nach einer Minute", "wird es leichter."], False),
 ("m10", ["^Die nächsten zehn Minuten.^"], False),
 ("muskeln", ["Jetzt hast du noch Kraft.", "Aber nicht lange.", "Die Kälte macht", "Arme und Hände *steif.*", "Darum zurück", "zur Stelle,", "an der du eingebrochen bist.", "Dort hielt das Eis."], False),
 ("raus", ["Arme aufs Eis,", "kräftig strampeln,", "rausrobben.", "Dann ~wegrollen.~", "Nicht aufstehen."], False),
 VR,
 ("stunde", ["Bis du durch Unterkühlung", "bewusstlos wirst,", "dauert es oft", "rund ^eine Stunde.^", "Die meisten sterben", "viel früher.", "Durch *Panik*", "und Erschöpfung."], False),
 ("regel", ["Merk dir:", "^Eins, zehn, eins.^"], False),
 *END("Was würdest du zuerst tun?", "Und folg mir. Bevor der See zufriert."),
], [("s1","hook",-0.3),("s2","m1",-0.2),("s3","m10",-0.2),("s4","raus",-0.2),("s5","verrueckt",-0.2),("s6","regel",-0.2),("s7","frage",-0.05)],
 {"show":F("m1",-0.2),"hide":F("frage",-0.05),"label":"IM EISWASSER","unit":"","sub":"1-10-1-REGEL","chipLabel":"KRAFT",
  "steps":[{"at":"m1","off":-0.2,"value":0,"chip":100},{"at":"schock","off":1.5,"value":0,"chip":60},{"at":"m10","off":0,"value":0,"chip":80},{"at":"muskeln","off":3,"value":0,"chip":35},{"at":"raus","off":3,"value":0,"chip":30},{"at":"regel","off":0,"value":0,"chip":100}]},
 IA("muskeln","stunde",{"type":"save","at":"regel","off":0.2,"dur":2.4,"text":"SPEICHER DIR DIE <span class='y'>REGEL</span>"})+[FOLGPILL("EISKALT")],
 [{"type":"riser","at":"hook","off":0},{"type":"heartbeat","at":"schock","off":0.5,"dur":3},{"type":"ding","at":"regel1","off":0.4},{"type":"alarm","at":"m10","off":0,"dur":1},{"type":"rise","at":"stunde","off":2,"dur":3},{"type":"ding","at":"regel","off":0.4},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[nervous]","kata":"[dramatically]","loop":"[curious]","m1":"[dramatically]","schock":"[breathless]","regel1":"[calmly]","m10":"[serious]","muskeln":"[urgent]","raus":"[firmly]","verrueckt":"[excited]","stunde":"[serious]","regel":"[dramatically]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, 2))

V.append(("18-kaugummi-verschluckt", "Was passiert, wenn du einen Kaugummi verschluckst?", [
 ("hook", ["Du hast den Kaugummi verschluckt."], True),
 ("loop", ["Bleibt er jetzt", "*sieben Jahre* in dir?", "Am Ende erfährst du,", "wann es wirklich", "^gefährlich^ wird."], False),
 ("min", ["^Minute eins.^"], False),
 ("magen", ["Der Kaugummi rutscht", "in deinen Magen.", "Die Säure löst Zucker", "und Aroma.", "Aber die Kaumasse?", "Die kann dein Körper", "*nicht verdauen.*"], False),
 ("tage", ["^Ein paar Tage später.^"], False),
 ("weg", ["Er wandert einfach", "durch deinen Darm", "und kommt ~ganz normal~", "wieder raus.", "Ärzte finden", "bei Untersuchungen", "keine alten Kaugummis."], False),
 VR,
 ("fall", ["Ein Junge schluckte", "jeden Tag", "^fünf bis sieben^ Kaugummis.", "Irgendwann saß", "eine *Kaugummi-Masse*", "in seinem Darm fest.", "Ärzte mussten sie", "entfernen."], False),
 ("fazit", ["Also:", "Einer ist", "~kein Problem.~", "Viele jeden Tag", "*schon.*"], False),
 *END("Hast du schon mal einen verschluckt?", "Und folg mir. Und spuck ihn lieber aus."),
], [("s1","hook",-0.3),("s2","min",-0.2),("s3","tage",-0.2),("s4","verrueckt",-0.2),("s5","fazit",-0.2),("s6","frage",-0.05)],
 {"show":F("min",-0.2),"hide":F("frage",-0.05),"label":"IM KÖRPER SEIT","unit":"","sub":"KAUGUMMI-CHECK","chipLabel":"MAGEN",
  "steps":[{"at":"min","off":-0.2,"value":0,"chip":100},{"at":"magen","off":4,"value":0,"chip":90},{"at":"tage","off":0,"value":0,"chip":100},{"at":"fall","off":3,"value":0,"chip":20},{"at":"fazit","off":1,"value":0,"chip":100}]},
 IA("weg","fall")+[FOLGPILL("KAU DRAUF")],
 [{"type":"ding","at":"min","off":0},{"type":"drip","at":"magen","off":1},{"type":"drip","at":"magen","off":1.6},{"type":"ding","at":"tage","off":0},{"type":"alarm","at":"fall","off":2.5,"dur":1},{"type":"rise","at":"fazit","off":0,"dur":2.5},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[surprised]","loop":"[curious]","min":"[calmly]","magen":"[calmly]","tage":"[curious]","weg":"[amused]","verrueckt":"[excited]","fall":"[serious]","fazit":"[warmly]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, None))

V.append(("19-flugzeugtuer", "Was passiert, wenn du im Flugzeug die Tür öffnest?", [
 ("hook", ["Zehntausend Meter. Du ziehst am Türgriff."], True),
 ("kata", ["Was dann passiert,", "*überrascht* fast jeden."], False),
 ("loop", ["Am Ende erfährst du,", "wann es doch", "^gefährlich^ wird."], False),
 ("zu", ["^Die Tür bewegt sich nicht.^"], False),
 ("druck", ["Im Flugzeug herrscht", "höherer Luftdruck", "als draußen.", "Dieser Druck presst", "die Tür von innen", "fest in den Rahmen."], False),
 ("stopfen", ["Die Tür ist gebaut", "wie ein *Stöpsel.*", "Sie öffnet sich erst", "nach innen.", "Und dagegen drücken", "rund ^zehn Tonnen.^"], False),
 ("mensch", ["Kein Mensch", "schafft das.", "Nicht mal zehn."], False),
 VR,
 ("landung", ["Gefährlich wird es", "erst ~kurz vor der Landung.~", "Dann ist der Druck", "fast ausgeglichen.", "2023 öffnete ein Passagier", "in Südkorea", "eine Tür im Landeanflug.", "Der Wind *peitschte*", "durch die Kabine."], False),
 *END("Würdest du am Notausgang sitzen?", "Und folg mir. Bevor du das nächste Mal fliegst."),
], [("s1","hook",-0.3),("s2","zu",-0.2),("s3","stopfen",-0.2),("s4","verrueckt",-0.2),("s5","frage",-0.05)],
 {"show":F("zu",-0.2),"hide":F("frage",-0.05),"label":"HÖHE","unit":"M","sub":"FLUG · REISEFLUG","chipLabel":"TÜR ZU",
  "steps":[{"at":"zu","off":-0.2,"value":10000,"chip":100},{"at":"landung","off":0.5,"value":10000,"chip":100},{"at":"landung","off":3,"value":200,"chip":25}]},
 IA("stopfen","landung")+[FOLGPILL("ANSCHNALLEN")],
 [{"type":"riser","at":"hook","off":0},{"type":"ding","at":"zu","off":0},{"type":"heartbeat","at":"stopfen","off":2.5,"dur":2},{"type":"ding","at":"verrueckt","off":0},{"type":"alarm","at":"landung","off":4.5,"dur":1.5},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[nervous]","kata":"[dramatically]","loop":"[curious]","zu":"[surprised]","druck":"[calmly]","stopfen":"[serious]","mensch":"[amused]","verrueckt":"[excited]","landung":"[nervous]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, 1))

V.append(("20-helm-im-all", "Was passiert, wenn du im All den Helm abnimmst?", [
 ("hook", ["Du nimmst im All den Helm ab."], True),
 ("kata", ["Explodierst du jetzt?", "Nein.", "Es ist *schlimmer.*"], False),
 ("loop", ["Am Ende erfährst du,", "wie lange du", "^wirklich^ überlebst."], False),
 ("s1", ["^Sekunde eins.^"], False),
 ("luft", ["Die Luft schießt", "aus deiner Lunge.", "Halt sie bloß *nicht* an.", "Sonst reißt sie."], False),
 ("s5", ["^Sekunde fünf.^"], False),
 ("kochen", ["Die Spucke auf deiner Zunge", "fängt an zu ~blubbern.~", "Ohne Luftdruck", "kocht Wasser", "schon bei Körpertemperatur."], False),
 ("s10", ["^Sekunde zehn.^"], False),
 ("haut", ["Dein Körper schwillt an.", "Aber deine Haut hält.", "Dann wird dir", "*schwarz vor Augen.*"], False),
 VR,
 ("nasa", ["Das ist einem Menschen", "wirklich passiert.", "Bei einem NASA-Test", "verlor sein Anzug die Luft.", "Nach rund ^vierzehn Sekunden^", "war er bewusstlos.", "Und er hat ~überlebt.~"], False),
 *END("Würdest du ins All fliegen?", "Und folg mir. Bevor dir die Luft ausgeht."),
], [("sc1","hook",-0.3),("sc2","s1",-0.2),("sc3","s5",-0.2),("sc4","s10",-0.2),("sc5","verrueckt",-0.2),("sc6","frage",-0.05)],
 {"show":F("s1",-0.2),"hide":F("frage",-0.05),"label":"BEWUSSTSEIN NOCH","unit":"","sub":"VAKUUM · OHNE HELM","chipLabel":"SAUERSTOFF",
  "countdown":{"from":15,"fmt":"s.mmm","start":F("s1",-0.2),"end":F("verrueckt",-0.3)},
  "steps":[{"at":"s1","off":-0.2,"value":0,"chip":100},{"at":"luft","off":1,"value":0,"chip":60},{"at":"s5","off":0,"value":0,"chip":40},{"at":"s10","off":0,"value":0,"chip":15},{"at":"haut","off":2.5,"value":0,"chip":0},{"at":"nasa","off":4.5,"value":0,"chip":100}]},
 IA("kochen","nasa")+[FOLGPILL("ATME WEITER")],
 [{"type":"riser","at":"hook","off":0},{"type":"glitch","at":"luft","off":0},{"type":"heartbeat","at":"s5","off":0,"dur":4},{"type":"heartbeat","at":"s10","off":0,"dur":3},{"type":"ding","at":"verrueckt","off":0},{"type":"rise","at":"nasa","off":3.5,"dur":3},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[dramatically]","kata":"[serious]","loop":"[curious]","s1":"[dramatically]","luft":"[urgent]","s5":"[nervous]","kochen":"[surprised]","s10":"[breathless]","haut":"[whispers]","verrueckt":"[excited]","nasa":"[dramatically]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, 2))

V.append(("21-sieben-tage-fasten", "Was passiert, wenn du 7 Tage nichts isst?", [
 ("hook", ["Sieben Tage. Kein Essen."], True),
 ("loop", ["Nur Wasser.", "Und an Tag drei", "passiert etwas", "^Seltsames^ in deinem Körper."], False),
 ("t1", ["^Tag eins.^"], False),
 ("hunger", ["Dein Magen knurrt.", "Dein Körper verbrennt", "seine *Zuckerreserven.*", "Nach rund einem Tag", "sind sie fast leer."], False),
 ("t2", ["^Tag zwei.^"], False),
 ("schwer", ["Du bist müde,", "gereizt,", "und dir ist kalt.", "Auf der Waage", "fehlt schon einiges.", "Aber das ist", "vor allem *Wasser.*"], False),
 ("t3", ["^Tag drei.^"], False),
 ("keto", ["Jetzt schaltet", "dein Körper um.", "Er verbrennt Fett", "und macht daraus", "neue Energie:", "~Ketone.~", "Viele haben sogar", "weniger Hunger."], False),
 ("t7", ["^Tag sieben.^"], False),
 ("ende", ["In einer Studie", "verloren Menschen", "rund ^sechs Kilo.^", "Aber auch", "*Muskeln.*"], False),
 VR,
 ("gefahr", ["Am gefährlichsten", "ist oft nicht das Fasten.", "Sondern das erste", "große *Essen danach.*", "Darum so etwas", "nur mit Arzt."], False),
 *END("Wie lange würdest du durchhalten?", "Und folg mir. Am besten mit vollem Magen."),
], [("s1","hook",-0.3),("s2","t1",-0.2),("s3","t2",-0.2),("s4","t3",-0.2),("s5","t7",-0.2),("s6","verrueckt",-0.2),("s7","frage",-0.05)],
 {"show":F("t1",-0.2),"hide":F("frage",-0.05),"label":"OHNE ESSEN","unit":"","sub":"NUR WASSER · NICHT NACHMACHEN","chipLabel":"ENERGIE",
  "steps":[{"at":"t1","off":-0.2,"value":0,"chip":90},{"at":"hunger","off":3,"value":0,"chip":60},{"at":"t2","off":0,"value":0,"chip":40},{"at":"t3","off":0,"value":0,"chip":45},{"at":"keto","off":3,"value":0,"chip":65},{"at":"t7","off":0,"value":0,"chip":50},{"at":"gefahr","off":2,"value":0,"chip":20}]},
 IA("schwer","gefahr")+[FOLGPILL("GUTEN APPETIT")],
 [{"type":"ding","at":"t1","off":0},{"type":"ding","at":"t2","off":0},{"type":"ding","at":"t3","off":0},{"type":"rise","at":"keto","off":1,"dur":3},{"type":"ding","at":"t7","off":0},{"type":"alarm","at":"gefahr","off":2,"dur":1},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[serious]","loop":"[curious]","t1":"[calmly]","hunger":"[calmly]","t2":"[tired]","schwer":"[tired]","t3":"[curious]","keto":"[excited]","t7":"[serious]","ende":"[serious]","verrueckt":"[excited]","gefahr":"[serious]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, None))

V.append(("22-fahrstuhl-absturz", "Was passiert, wenn das Seil vom Fahrstuhl reißt?", [
 ("hook", ["Das Seil reißt."], True),
 ("kata", ["Und du fällst", "zwanzig Stockwerke", "in die *Tiefe.*"], False),
 ("loop", ["Hilft Springen", "kurz vor dem Aufprall?", "Am Ende kennst du", "die ^Antwort.^"], False),
 ("s1", ["^Sekunde eins.^"], False),
 ("schwerelos", ["Du wirst ~schwerelos.~", "Dein Handy schwebt", "vor deinem Gesicht."], False),
 ("bremse", ["Aber halt.", "Moderne Aufzüge", "hängen an mehreren Seilen.", "Und sie haben", "eine *Fangbremse.*", "Sie krallt sich", "in die Schienen", "und stoppt dich", "nach wenigen Metern."], False),
 ("versagt", ["^Und wenn alles versagt?^"], False),
 ("springen", ["Dann bringt Springen", "*fast nichts.*", "Du bremst dich", "nur ein winziges bisschen.", "Der Boden unter dir", "fällt ja mit."], False),
 VR,
 ("rekord", ["1945 stürzte", "ein Aufzug", "im ^Empire State Building^", "fünfundsiebzig Stockwerke ab.", "Die Frau darin", "~überlebte.~", "Bis heute ein Rekord."], False),
 *END("Fährst du jetzt noch Fahrstuhl?", "Und folg mir. Bevor du die Treppe nimmst."),
], [("s1","hook",-0.3),("s2","s1",-0.2),("s3","bremse",-0.2),("s4","versagt",-0.2),("s5","verrueckt",-0.2),("s6","frage",-0.05)],
 {"show":F("s1",-0.2),"hide":F("frage",-0.05),"label":"STOCKWERK","unit":"","sub":"FREIER FALL","chipLabel":"BREMSE",
  "steps":[{"at":"s1","off":-0.2,"value":20,"chip":0},{"at":"schwerelos","off":1.5,"value":19,"chip":0},{"at":"bremse","off":4,"value":18,"chip":100},{"at":"versagt","off":0,"value":18,"chip":0},{"at":"springen","off":2,"value":1,"chip":0},{"at":"rekord","off":1,"value":75,"chip":0}]},
 IA("bremse","rekord")+[FOLGPILL("NIMM DIE TREPPE")],
 [{"type":"riser","at":"hook","off":0},{"type":"rise","at":"schwerelos","off":0,"dur":2.5},{"type":"glitch","at":"bremse","off":4},{"type":"ding","at":"versagt","off":0},{"type":"boom","at":"springen","off":3},{"type":"ding","at":"verrueckt","off":0},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[shouting]","kata":"[dramatically]","loop":"[curious]","s1":"[nervous]","schwerelos":"[surprised]","bremse":"[calmly]","versagt":"[nervous]","springen":"[serious]","verrueckt":"[excited]","rekord":"[dramatically]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, 2))

V.append(("23-blitz-ins-auto", "Was passiert, wenn der Blitz in dein Auto einschlägt?", [
 ("hook", ["Ein Blitz trifft dein Auto."], True),
 ("kata", ["Mit dreißigtausend Ampere.", "Und du sitzt", "*mittendrin.*"], False),
 ("loop", ["Am Ende erfährst du,", "wann es im Auto", "^doch gefährlich^ wird."], False),
 ("knall", ["^Ein greller Blitz.^", "Ein Knall,", "lauter als jeder Böller."], False),
 ("mythos", ["Viele glauben:", "Die Gummireifen", "schützen dich.", "*Falsch.*"], False),
 ("kaefig", ["Der Strom fließt", "außen über das Metall", "um dich herum", "und springt", "in den Boden.", "Das nennt man", "~Faradayscher Käfig.~"], False),
 ("schaden", ["^Und dein Auto?^", "Lack und Antenne", "können verkohlen.", "Die Elektronik", "kann ausfallen."], False),
 VR,
 ("cabrio", ["Im Cabrio mit Stoffdach", "bist du *nicht* geschützt.", "Und fass im Gewitter", "keine Metallteile an.", "Bleib einfach ~sitzen.~"], False),
 *END("Wo würdest du dich verstecken?", "Und folg mir. Bevor das nächste Gewitter kommt."),
], [("s1","hook",-0.3),("s2","knall",-0.2),("s3","kaefig",-0.2),("s4","schaden",-0.2),("s5","verrueckt",-0.2),("s6","frage",-0.05)],
 {"show":F("knall",-0.2),"hide":F("frage",-0.05),"label":"STROM","unit":"A","sub":"BLITZEINSCHLAG","chipLabel":"SCHUTZ",
  "steps":[{"at":"knall","off":-0.2,"value":30000,"chip":100},{"at":"mythos","off":2,"value":30000,"chip":100},{"at":"kaefig","off":3,"value":0,"chip":100},{"at":"cabrio","off":1,"value":0,"chip":20},{"at":"cabrio","off":4,"value":0,"chip":100}]},
 IA("kaefig","cabrio")+[FOLGPILL("BLEIB SITZEN")],
 [{"type":"riser","at":"hook","off":0},{"type":"boom","at":"knall","off":0.2},{"type":"glitch","at":"knall","off":0.2},{"type":"ding","at":"mythos","off":2.2},{"type":"ding","at":"schaden","off":0},{"type":"ding","at":"verrueckt","off":0},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[nervous]","kata":"[dramatically]","loop":"[curious]","knall":"[shouting]","mythos":"[mischievously]","kaefig":"[calmly]","schaden":"[serious]","verrueckt":"[excited]","cabrio":"[serious]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, 2))

V.append(("24-fuenf-kaffee", "Was passiert, wenn du jeden Tag 5 Tassen Kaffee trinkst?", [
 ("hook", ["Fünf Tassen Kaffee. Jeden Tag."], True),
 ("loop", ["Ist das zu viel?", "Am Ende siehst du,", "was eine große Studie", "^herausgefunden^ hat."], False),
 ("tasse1", ["^Tasse eins.^"], False),
 ("wach", ["Schon nach kurzer Zeit", "wirkt das Koffein.", "Es blockiert den Stoff,", "der dich *müde* macht."], False),
 ("tasse3", ["^Tasse drei.^"], False),
 ("herz", ["Dein Herz schlägt", "etwas schneller.", "Und du musst", "öfter aufs Klo."], False),
 ("tasse5", ["^Tasse fünf.^"], False),
 ("grenze", ["Jetzt bist du", "bei rund ^vierhundert^", "Milligramm Koffein.", "Für gesunde Erwachsene", "gilt das noch", "als ~unbedenklich.~"], False),
 ("schlaf", ["Aber trinkst du", "die letzte Tasse", "am Abend,", "leidet dein *Schlaf.*"], False),
 VR,
 ("studie", ["In einer Studie", "mit neunzigtausend Menschen", "lebten Kaffeetrinker", "im Schnitt sogar", "~länger.~", "Ob das am Kaffee liegt,", "ist aber unklar."], False),
 *END("Wie viele Tassen trinkst du?", "Und folg mir. Am besten mit einem Kaffee."),
], [("s1","hook",-0.3),("s2","tasse1",-0.2),("s3","tasse3",-0.2),("s4","tasse5",-0.2),("s5","verrueckt",-0.2),("s6","frage",-0.05)],
 {"show":F("tasse1",-0.2),"hide":F("frage",-0.05),"label":"KOFFEIN","unit":"MG","sub":"HEUTE GETRUNKEN","chipLabel":"SCHLAF",
  "steps":[{"at":"tasse1","off":-0.2,"value":80,"chip":100},{"at":"tasse3","off":0,"value":240,"chip":90},{"at":"tasse5","off":0,"value":400,"chip":75},{"at":"schlaf","off":2,"value":400,"chip":35}]},
 IA("herz","studie")+[FOLGPILL("KAFFEEPAUSE")],
 [{"type":"ding","at":"tasse1","off":0},{"type":"ding","at":"tasse3","off":0},{"type":"heartbeat","at":"herz","off":0,"dur":2.5},{"type":"ding","at":"tasse5","off":0},{"type":"ding","at":"verrueckt","off":0},{"type":"rise","at":"studie","off":2,"dur":3},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[curious]","loop":"[curious]","tasse1":"[calmly]","wach":"[calmly]","tasse3":"[excited]","herz":"[amused]","tasse5":"[serious]","grenze":"[calmly]","schlaf":"[serious]","verrueckt":"[excited]","studie":"[surprised]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, None))

V.append(("25-ohne-handy", "Was passiert, wenn du 30 Tage kein Handy benutzt?", [
 ("hook", ["Dreißig Tage. Kein Handy."], True),
 ("loop", ["Klingt unmöglich?", "Am Ende siehst du,", "was das mit deinem", "^Kopf^ macht."], False),
 ("t1", ["^Tag eins.^"], False),
 ("griff", ["Deine Hand greift", "ständig in die Tasche.", "Du glaubst,", "es *vibriert.*", "Dabei liegt es", "zu Hause."], False),
 ("t3", ["^Tag drei.^"], False),
 ("leer", ["Dir ist", "*langweilig.*", "Richtig langweilig.", "Und genau dann", "fängst du an,", "wieder nachzudenken."], False),
 ("w2", ["^Zwei Wochen später.^"], False),
 ("studie", ["In einer Studie", "blockierten Menschen", "nur das Internet", "auf dem Handy.", "Nach zwei Wochen", "konnten sie sich", "~besser konzentrieren.~", "Und fühlten sich besser."], False),
 ("w3", ["^Drei Wochen.^"], False),
 ("schlaf", ["In einem anderen Versuch", "hatten Menschen", "über ^zwanzig Prozent^", "weniger Schlafprobleme."], False),
 VR,
 ("aufgeben", ["Ein Drittel", "hat vorher", "*aufgegeben.*"], False),
 *END("Würdest du dreißig Tage schaffen?", "Und folg mir. Solange du noch ein Handy hast."),
], [("s1","hook",-0.3),("s2","t1",-0.2),("s3","t3",-0.2),("s4","w2",-0.2),("s5","w3",-0.2),("s6","verrueckt",-0.2),("s7","frage",-0.05)],
 {"show":F("t1",-0.2),"hide":F("frage",-0.05),"label":"OHNE HANDY","unit":"","sub":"DIGITAL DETOX","chipLabel":"FOKUS",
  "steps":[{"at":"t1","off":-0.2,"value":0,"chip":40},{"at":"t3","off":0,"value":0,"chip":30},{"at":"w2","off":0,"value":0,"chip":70},{"at":"w3","off":0,"value":0,"chip":85}]},
 IA("leer","aufgeben")+[FOLGPILL("NOCH KURZ")],
 [{"type":"ding","at":"t1","off":0},{"type":"drip","at":"griff","off":2},{"type":"drip","at":"griff","off":2.4},{"type":"ding","at":"t3","off":0},{"type":"ding","at":"w2","off":0},{"type":"rise","at":"studie","off":3,"dur":3},{"type":"ding","at":"w3","off":0},{"type":"ding","at":"verrueckt","off":0},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[serious]","loop":"[curious]","t1":"[calmly]","griff":"[nervous]","t3":"[tired]","leer":"[tired]","w2":"[curious]","studie":"[excited]","w3":"[calmly]","schlaf":"[warmly]","verrueckt":"[excited]","aufgeben":"[amused]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, None))

V.append(("26-blitz-trifft-dich", "Was passiert, wenn dich ein Blitz trifft?", [
 ("hook", ["Der Blitz trifft dich."], True),
 ("kata", ["Heißer als", "die Oberfläche der", "*Sonne.*"], False),
 ("loop", ["Und trotzdem", "überleben ^neun von zehn.^", "Am Ende siehst du,", "was viele *für immer* mitnehmen."], False),
 ("treffer", ["^Der Einschlag.^"], False),
 ("strom", ["Der Strom rast", "meist ~über~ deine Haut.", "Nicht durch dich hindurch.", "Das rettet", "vielen das Leben."], False),
 ("herz", ["Aber er kann", "dein Herz", "*stoppen.*", "Dann zählt", "jede Sekunde.", "Sofort wiederbeleben", "hilft oft."], False),
 ("danach", ["^Die Tage danach.^"], False),
 ("figur", ["Auf deiner Haut", "erscheint ein Muster", "wie ein ~Farn.~", "Eine Lichtenberg-Figur.", "Sie verschwindet", "meist nach ein paar Tagen."], False),
 VR,
 ("folgen", ["Viele Überlebende", "hören danach schlechter", "oder haben", "*Nervenschmerzen.*", "Manchmal jahrelang."], False),
 *END("Wo bist du bei Gewitter?", "Und folg mir. Bevor es donnert."),
], [("s1","hook",-0.3),("s2","treffer",-0.2),("s3","herz",-0.2),("s4","danach",-0.2),("s5","verrueckt",-0.2),("s6","frage",-0.05)],
 {"show":F("treffer",-0.2),"hide":F("frage",-0.05),"label":"TEMPERATUR","unit":"°C","sub":"IM BLITZKANAL","chipLabel":"HERZ",
  "steps":[{"at":"treffer","off":-0.2,"value":30000,"chip":100},{"at":"herz","off":1.5,"value":30000,"chip":0},{"at":"herz","off":4.5,"value":37,"chip":100},{"at":"folgen","off":2,"value":37,"chip":70}]},
 IA("strom","folgen")+[FOLGPILL("GEWITTERFEST")],
 [{"type":"riser","at":"hook","off":0},{"type":"boom","at":"treffer","off":0},{"type":"glitch","at":"treffer","off":0.1},{"type":"heartbeat","at":"herz","off":0,"dur":1.5},{"type":"alarm","at":"herz","off":1.6,"dur":1},{"type":"ding","at":"danach","off":0},{"type":"ding","at":"verrueckt","off":0},{"type":"ding","at":"frage","off":-0.2}],
 {"hook":"[shouting]","kata":"[dramatically]","loop":"[curious]","treffer":"[dramatically]","strom":"[calmly]","herz":"[urgent]","danach":"[softly]","figur":"[curious]","verrueckt":"[excited]","folgen":"[serious]","frage":"[curious]","komm":"[warmly]","folg":"[mischievously]"}, 1))

out = {}
for slug, title, L, sc, hud, ia, sfx, tags, key in V:
    build(slug, title, L, sc, hud, ia, sfx)
    p = Path("/home/user/tiktok-videos/videos") / slug
    prompt = " ".join(f"{tags.get(i, '')} " + re.sub(r"[*^~]", "", " ".join(ch)) for i, ch, _ in L).replace("  ", " ").strip()
    (p / "script_v3.txt").write_text(prompt + "\n", encoding="utf-8")
    out[slug] = {"key": key, "chars": len(prompt), "words": len(re.sub(r"\[[^\]]*\]", "", prompt).split())}
json.dump(out, open("/home/user/tiktok-videos/scripts/batch3_meta.json", "w"), indent=1)
print(json.dumps(out, indent=0))
