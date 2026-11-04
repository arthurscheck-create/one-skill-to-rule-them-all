---
name: tiktok-video
description: Erstellt deutsche TikTok-Videos (9:16, 1080x1920, 40–90 s) im Flat-Vector-"Was wäre wenn"/Survival-Erklärstil komplett im Code mit HyperFrames (HTML + GSAP → MP4). Verwenden, wenn der Nutzer ein neues Video, ein Thema, einen Titel ("Was würde passieren, wenn…", "Du hast X Minuten…", "Warum…") oder eine Änderung an einem bestehenden Video im Ordner tiktok-videos/videos/ möchte.
---

# TikTok-Videos im Code (HyperFrames)

Jedes Video wird **vollständig im Code** gebaut: Illustrationen als SVG, Animation mit GSAP,
Rendern mit HyperFrames zu MP4. **Sprache immer Deutsch** (Skript, Untertitel, HUD, Schilder).

Arbeitsverzeichnis: Ordner `tiktok-videos/` im Repo `arthurscheck-create/one-skill-to-rule-them-all`
(Branch `tiktok-videos`). In einer neuen Session zuerst einrichten:
```bash
cd <repo>/tiktok-videos && npm i            # hyperframes@0.9.11 + gsap
ls ~/.claude/skills/tiktok-video || cp -r .claude/skills/tiktok-video ~/.claude/skills/
```
Alle Pfade unten sind relativ zu diesem Ordner.

```
shared/lib/        Engine (engine.js), Figuren (cast.js), Stil (style.css), gsap.min.js, fonts/
templates/         index.template.html + timing.template.js  (Startpunkt für neue Videos)
tools/             new_video.sh · build_sfx.py · add_voice.py · render.sh
videos/<slug>/     ein Projekt pro Video (index.html, timing.js, lib/, assets/)
videos/01-keiner-arbeitet/   ← REFERENZPROJEKT: vollständiges Beispiel mit 12 Szenen
output/            fertige MP4s
```

## 1. Stil der Vorlagen (genau so nachbauen)

Referenzbild: `references/eigenes-video-01-kontaktbogen.jpg` (eigenes Video 1 = verbindlicher
Maßstab). **Vor jedem neuen Video ansehen.** (Standbilder der fremden Vorlagen werden aus
Urheberrechtsgründen nicht im öffentlichen Repo gespeichert; die Beschreibung unten genügt.)

Standardstil = **Flat-Vector-Survival** (Vorlage "Du hast 38 Minuten"):
- **Look:** dunkle Nacht-Palette (Navy `#1b1936`, Lila `#3b2b63`), warme Fensterlichter `#ffd27a`,
  flache Formen mit weichen Verläufen, Vignette, leichtes Korn. Figuren: runder Kopf, große
  weiße Augen, rote Wangen, Hoodie. Du-Perspektive.
- **Untertitel:** Montserrat 900, VERSALIEN, weiß mit dicker dunkler Kontur (14 px) und
  Schlagschatten, 92 px, mittig bei y≈1255. **1–3 Wörter pro Einblendung**, Pop-in
  (scale 0.7→1, back.out). Schlüsselwörter farbig: `*rot*` = Gefahr/Negation,
  `^gelb^` = Zeitmarken/Zahlen/Begriffe, `~grün~` = gute Wendung.
- **HUD oben** (y≈225): rotes Panel mit Label ("⚠ OHNE ARBEIT SEIT"), großer roter Zähler
  ("072 STD"), Mini-Zeile "WAS WÄRE WENN · FIKTION"; darunter ein Status-Chip
  ("VERSORGUNG 61%"), der grün→gelb→rot wechselt. Sprünge zeigen "+47 STD" in Gelb.
  Entspricht "EINSCHLAG IN 37:54" + "FREIE PLÄTZE 2 988" der Vorlage.
- **Schnitt:** harte Schnitte alle 2–5 s, Punch-in (scale 1.12→1) + kurzer weißer Blitz +
  Whoosh, danach langsamer Zoom (Drift) in jeder Szene.
- **Keine** TikTok-Logos, Handles oder "AI-generated"-Hinweise einbauen: das blendet TikTok
  beim Download selbst ein (das war in den Vorlagen der Fall).

Alternativstile nur auf Wunsch: *Erklär-Flat* (Strichmännchen, Nachtblau, Kurvendiagramme,
zweizeilige Überschrift oben weiß + farbig) oder *Low-Poly-3D* (Three.js, Serifenschrift,
kursive Untertitel, Millisekunden-Countdown links). Dann nach der Beschreibung oben bauen.

## 2. Skript-Aufbau (Pflicht)

Ziel-Länge laut Nutzer (Standard 50 s ≈ 110–125 Wörter). Kurze Sätze, Du-Form, Präsens.

1. **Hook (0–3,5 s):** Titelfrage als großer Titel in der Untertitel-Zone + gelbe Unterzeile
   ("⚠ WIE LANGE HÄLT DIE STADT DURCH?"). Szene zeigt sofort das Problem.
2. **Zeitsprünge mit Eskalation:** "Stunde eins." → "Tag zwei." → "Tag drei." → "Tag sieben."
   Jeder Sprung = neue Szene + HUD-Zähler springt + Status-Chip sinkt.
   Jede Stufe eine konkrete, sichtbare Folge (Bus fällt aus, Kasse leer, Regale leer,
   Stromausfall, kein Wasser, kein Netz, Müll/Ratten).
3. **Wendung (~75 %):** "Und das Verrückte?" + überraschende Erkenntnis (grün).
4. **CTA-Abstimmung (letzte 6 s):** Frage + 4 Optionen A–D + "SCHREIB A, B, C ODER D IN DIE
   KOMMENTARE" + Countdown-Ring. Optional "TEIL 2"-Cliffhanger.

## 3. Arbeitsablauf

```bash
cd tiktok-videos
tools/new_video.sh 02-<slug> "Titel"         # Projekt aus Vorlage anlegen
```
1. **Skript** schreiben, dann `videos/<slug>/timing.js` füllen:
   - `lines`: ein Eintrag pro Satz mit `id`, `t0`, `t1` (Schätzung: ~2,6 Wörter/s,
     0,3–0,4 s Pause), `chunks` (1–3 Wörter, mit Farb-Markup), `noCap` für Hook/CTA.
   - `scenes`: Szenenwechsel relativ zu Satz-IDs (`{"id":"s3","at":"kasse","off":-0.2}`).
   - `hud.steps`: Zählerwerte/Chip-Prozente relativ zu Satz-IDs.
   - `sfx`: Ereignis-Sounds (`alarm riser boom flicker drip glitch rats rise ding`).
   **Alle Animationszeiten in index.html immer über `at("id", off)` / `end("id")` angeben**,
   nie als feste Sekunden. Dann synchronisiert sich alles automatisch, wenn die Stimme kommt.
2. **Szenen** in `index.html` bauen: je Szene
   `<section class="scene" id="sX"><div class="cam"><div class="drift"><svg class="art" viewBox="0 0 1080 1920">…`.
   Wiederverwendbar aus `cast.js`: `E.person(g,{x,y,s,face,arms,shirt,hair,pants,flip})`
   (faces: worried, shock, smirk, neutral · arms: down, phone, box, bag) und
   `E.use(g,"rat"|"bag"|"truck"|"tower",x,y,s)`. Skylines/Regale/Fenster per Schleife mit
   `E.rng(seed)` erzeugen. Bildkomposition: wichtige Motive zwischen y≈450 und 1200,
   Untertitel-Zone 1255–1515 und HUD-Zone 200–430 frei von wichtigen Texten halten.
   Das Referenzprojekt `videos/01-keiner-arbeitet/index.html` zeigt jede Technik.
3. **Stimme** (deutsch) über **ElevenLabs**, aktuelle Standardstimme
   **`rDmv3mOhK6TnhYWckFaD`** ("Felix Serenitas – German Top Voice", vom Nutzer gewählt;
   frühere Stimme `bFv4VX9jlZxtKnEa6UWs` "Arthur Holm"). Modell `eleven_multilingual_v2`.
   Eine andere Stimme nur, wenn der Nutzer es sagt.
   **Weg A – ElevenLabs-Connector (11LBS, Credits des Nutzers), Standard:**
   1. `creative_create_flow` → `creative_generate_speech` (voice_id, Skript als prompt;
      2 Takes à ~710 Credits pro 50 s) → `creative_get_flow_run_status` pollen.
   2. Take wählen, der am besten in die Zieldauer passt; `content_url` mit curl nach
      `assets/` laden (Netzfreigabe `elevenlabsusercontent.com` ist eingerichtet).
   3. `python3 tools/add_voice.py videos/<slug> assets/take.mp3 --min-duration 50 --fit 50 --tail 1.8`
      (kopiert nach voice.*, beschleunigt bei Bedarf max. 1,15x, trägt `<audio>` ein).
   4. **Wortgenau synchronisieren (immer machen, kostet 0 Credits):** gewählten Take mit
      `creative_add_flow_asset_node` (modality audio, generation_id) auf den Flow legen,
      `creative_transcribe_audio` (eleven_scribe_v1, connect_from = diese node_id), pollen,
      `words_download_url` nach `assets/<take>_words.json` laden, dann
      `python3 tools/align_words.py videos/<slug> assets/<take>_words.json --source assets/take.mp3`.
      Muss "0 Abweichungen" melden; sonst Skript-Chunks an den gesprochenen Text anpassen.
      (Die reine Pausen-Erkennung von add_voice.py ordnet bei manchen Stimmen falsch zu.)
   **Weg B – API-Schlüssel (`ELEVENLABS_API_KEY`), wortgenau:**
   ```bash
   python3 tools/elevenlabs_tts.py videos/<slug> --min-duration 50 --fit 50
   ```
   Das liest den Sprechertext direkt aus `timing.js` (Text der `chunks` = gesprochener Text,
   also Zahlen/Abkürzungen so schreiben, wie sie gesprochen werden sollen), holt Audio +
   Zeichen-Zeitstempel und setzt `t0/t1` und `chunkStarts` **wortgenau**. `--reuse` wendet ein
   vorhandenes Alignment erneut an (ohne neue Kosten). Braucht `ELEVENLABS_API_KEY` in der
   Umgebung und Netzfreigabe für `api.elevenlabs.io`. Andere Stimme nur, wenn der Nutzer es
   sagt (`--voice <id>`). Fallback ohne Zeitstempel: `tools/add_voice.py` (Pausen-Erkennung).
4. **Prüfen:** `cd videos/<slug> && npx hyperframes check` (Fehler beheben; Warnungen
   `line_unread` bei Wort-Untertiteln sind stilbedingt ok) und
   `npx hyperframes snapshot --no-end --at 1.5,5,9,...` → **jeden Kontaktbogen ansehen**,
   besonders Überlappungen mit HUD/Untertiteln.
5. **Rendern:** `tools/render.sh videos/<slug>` → `output/<slug>.mp4` (~2,5 min für 50 s).
   Danach Kontaktbogen aus dem MP4 ziehen und kontrollieren, dann dem Nutzer schicken.

## 4. Fallstricke (bereits einmal passiert)

- **Kein CDN:** gsap und die Schrift kommen aus `lib/` (jsdelivr ist im Netz gesperrt).
  Neue Schriften lokal als woff2 in `shared/lib/fonts/` ablegen.
- **Zähler/Text, der sich ändert, nur über `E.clock(tl, t => …)`** als reine Funktion der
  Zeit setzen. `onUpdate`-Tweens oder `tl.set(textContent)` zeigen beim Springen falsche Werte.
- **`fromTo` rendert sofort** (immediateRender): Mehrere `fromTo` auf dasselbe Element ab
  dem zweiten mit `immediateRender:false`, sonst steht der Startwert schon ab Sekunde 0
  (z. B. war der Blitz-Overlay dauerhaft halb sichtbar).
- **SVG mit `transform`-Attribut nicht direkt mit x/y animieren**, sonst überschreibt GSAP
  die Translation und das Element springt. In ein leeres `<g>` wrappen und den Wrapper animieren.
- Kein `Math.random`/`Date.now`, nur `E.rng(seed)`. Alles muss seekbar sein.
- Texte im Hook: max. 3 Zeilen à ~14 Zeichen bei 90 px, sonst bricht es um und überlappt.
- Ist ein Download-Host gesperrt (z. B. `elevenlabsusercontent.com`): den Nutzer Schritt für
  Schritt durch Umgebungsmenü → Edit → Network access → Allowed domains führen; die Freigabe
  greift sofort in der laufenden Session. Nie nach Schlüsseln im Chat fragen.
- `tools/render.sh` mit eigenem Ausgabepfad: absolute Pfade oder relativ zum Aufrufort.
- Container ist flüchtig: fertige Videos und Projekte dem Nutzer schicken bzw. in ein Repo pushen.

## 5. Abgabe (immer alles davon)

1. MP4 aus `output/` per SendUserFile schicken.
2. **Immer eine Posting-Beschreibung + Hashtags** mitliefern (vom Nutzer gewünscht), direkt
   kopierbar im Chat und als `output/<slug>_posting.txt` (+ Kopie `videos/<slug>/posting.txt`):
   - Beschreibung: 2–3 Zeilen, Deutsch, Hook-Frage + 1–2 Eskalations-Details als Teaser
     (Auflösung nicht verraten) + Kommentar-Aufruf passend zur CTA (A/B/C/D), 2–4 Emojis.
   - Hashtags: 8–10, gemischt aus Nische (#waswärewenn #gedankenexperiment #szenario),
     Thema (z. B. #stromausfall) und Reichweite (#wissen #lernenmittiktok #fakten #fürdich #fyp).
3. Kurz: welche Stimme/welcher Take, wie viele Credits verbraucht, Dauer.
4. Projekt in den Branch `tiktok-videos` von `one-skill-to-rule-them-all` pushen.
Auf Deutsch antworten.
