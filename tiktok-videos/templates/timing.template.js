window.TIMING = {
  "title": "__TITLE__",
  "duration": 50,
  "voice": null,
  "lines": [
    {"id": "hook",  "t0": 0.30, "t1": 3.40, "noCap": true, "chunks": ["Hook-Frage als ganzer Satz"]},
    {"id": "b1",    "t0": 3.80, "t1": 4.90, "chunks": ["^Stunde eins.^"]},
    {"id": "b2",    "t0": 5.00, "t1": 7.00, "chunks": ["Kurzer Satz", "mit *Schlüsselwort.*"]},
    {"id": "twist", "t0": 7.40, "t1": 10.0, "chunks": ["Und das", "^Verrückte?^", "~gute Wendung~"]},
    {"id": "cta",   "t0": 10.4, "t1": 12.0, "noCap": true, "chunks": ["Schreib es in die Kommentare."]}
  ],
  "scenes": [
    {"id": "s1", "at": "hook",  "off": -0.30},
    {"id": "s2", "at": "b1",    "off": -0.20},
    {"id": "s9", "at": "cta",   "off": -0.30}
  ],
  "hud": {
    "show": {"at": "b1", "off": -0.20},
    "hide": {"at": "cta", "off": -0.30},
    "label": "OHNE X SEIT", "unit": "STD", "sub": "WAS WÄRE WENN · FIKTION", "chipLabel": "STATUS",
    "steps": [
      {"at": "b1", "off": -0.20, "value": 1,  "chip": 100},
      {"at": "b2", "off": 0.00,  "value": 24, "chip": 40}
    ]
  },
  "interact": [
    {"type": "follow",  "at": "b2",    "off": 0.3,  "dur": 2.6, "text": "FOLG FÜR <span class='y'>TEIL 2</span>"},
    {"type": "like",    "at": "twist", "off": -0.2, "dur": 2.4, "text": "LIKE, WENN DU'S NICHT WUSSTEST"},
    {"type": "comment", "at": "cta",   "off": 0.6,  "dur": 2.4, "text": "SCHREIB'S IN DIE KOMMENTARE"}
  ],
  "sfx": [
    {"type": "riser", "at": "b1", "off": -1.20},
    {"type": "ding",  "at": "cta", "off": -0.20}
  ]
};
