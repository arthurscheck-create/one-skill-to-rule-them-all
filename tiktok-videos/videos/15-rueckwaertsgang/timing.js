window.TIMING = {
  "title": "Was passiert, wenn du bei 100 km/h in den Rückwärtsgang schaltest?",
  "duration": 50.12,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.189,
      "t1": 1.556,
      "chunks": [
        "Hundert Sachen. Rückwärtsgang rein."
      ],
      "noCap": true,
      "chunkStarts": [
        0.189
      ]
    },
    {
      "id": "kata",
      "t0": 1.764,
      "t1": 2.975,
      "chunks": [
        "Das kann",
        "dein Getriebe",
        "*zerfetzen.*"
      ],
      "chunkStarts": [
        1.764,
        1.914,
        2.378
      ]
    },
    {
      "id": "loop",
      "t0": 3.183,
      "t1": 6.669,
      "chunks": [
        "Und am Ende",
        "zeige ich dir ein Auto,",
        "das rückwärts",
        "fast ^dreihundert^ fährt."
      ],
      "chunkStarts": [
        3.183,
        3.669,
        4.656,
        5.225
      ]
    },
    {
      "id": "fall1",
      "t0": 6.878,
      "t1": 8.015,
      "chunks": [
        "^Fall eins:^",
        "Automatik."
      ],
      "chunkStarts": [
        6.878,
        7.451
      ]
    },
    {
      "id": "auto",
      "t0": 8.182,
      "t1": 14.806,
      "chunks": [
        "Du ziehst den Hebel",
        "auf R.",
        "Und meistens passiert:",
        "*gar nichts.*",
        "Der Computer blockiert",
        "und schaltet einfach",
        "auf ~Neutral.~"
      ],
      "chunkStarts": [
        8.182,
        9.182,
        9.89,
        10.821,
        11.64,
        12.918,
        13.751
      ]
    },
    {
      "id": "fall2",
      "t0": 14.929,
      "t1": 18.084,
      "chunks": [
        "^Fall zwei:^",
        "Schaltwagen.",
        "Und hier",
        "wird es *brutal.*"
      ],
      "chunkStarts": [
        14.929,
        15.654,
        16.619,
        16.907
      ]
    },
    {
      "id": "schalt",
      "t0": 18.118,
      "t1": 23.863,
      "chunks": [
        "Der Rückwärtsgang",
        "ist oft",
        "nicht synchronisiert.",
        "Du hörst nur",
        "ein lautes *Krachen.*",
        "Mit Gewalt",
        "brechen die Zähne",
        "der Zahnräder ab."
      ],
      "chunkStarts": [
        18.118,
        18.743,
        19.118,
        20.132,
        20.516,
        21.641,
        22.349,
        23.044
      ]
    },
    {
      "id": "kupplung",
      "t0": 24.072,
      "t1": 29.276,
      "chunks": [
        "Und lässt du dann",
        "die Kupplung kommen,",
        "können die Räder",
        "*blockieren.*",
        "Bei Tempo hundert",
        "heißt das:",
        "Schleudern."
      ],
      "chunkStarts": [
        24.072,
        24.585,
        25.59,
        26.206,
        26.891,
        27.635,
        28.21
      ]
    },
    {
      "id": "fall3",
      "t0": 29.425,
      "t1": 30.943,
      "chunks": [
        "^Fall drei:^",
        "Elektroauto."
      ],
      "chunkStarts": [
        29.425,
        29.851
      ]
    },
    {
      "id": "elektro",
      "t0": 31.012,
      "t1": 34.637,
      "chunks": [
        "Der Motor",
        "dreht sich einfach",
        "andersherum.",
        "Doch die Software",
        "sagt: *Nein.*"
      ],
      "chunkStarts": [
        31.012,
        31.54,
        32.26,
        33.154,
        33.676
      ]
    },
    {
      "id": "verrueckt",
      "t0": 34.846,
      "t1": 35.644,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        34.846,
        35.006
      ]
    },
    {
      "id": "rekord",
      "t0": 35.714,
      "t1": 41.367,
      "chunks": [
        "Ein Elektro-Supersportwagen",
        "fuhr rückwärts",
        "über ~zweihundertsiebzig~",
        "Kilometer pro Stunde.",
        "Weltrekord."
      ],
      "chunkStarts": [
        35.714,
        37.367,
        38.244,
        39.311,
        40.533
      ]
    },
    {
      "id": "frage",
      "t0": 41.575,
      "t1": 43.033,
      "chunks": [
        "Was würde dein Auto machen?"
      ],
      "noCap": true,
      "chunkStarts": [
        41.575
      ]
    },
    {
      "id": "komm",
      "t0": 43.081,
      "t1": 45.199,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        43.081
      ]
    },
    {
      "id": "folg",
      "t0": 45.391,
      "t1": 47.46,
      "chunks": [
        "Und folg mir. Bevor du es selbst ausprobierst."
      ],
      "noCap": true,
      "chunkStarts": [
        45.391
      ]
    }
  ],
  "scenes": [
    {
      "id": "s1",
      "at": "hook",
      "off": -0.3
    },
    {
      "id": "s2",
      "at": "fall1",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "fall2",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "kupplung",
      "off": -0.2
    },
    {
      "id": "s5",
      "at": "fall3",
      "off": -0.2
    },
    {
      "id": "s6",
      "at": "verrueckt",
      "off": -0.2
    },
    {
      "id": "s7",
      "at": "frage",
      "off": -0.05
    }
  ],
  "hud": {
    "show": {
      "at": "fall1",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "TEMPO",
    "unit": "KM/H",
    "sub": "WAS WÄRE WENN · NICHT NACHMACHEN",
    "chipLabel": "GETRIEBE",
    "steps": [
      {
        "at": "fall1",
        "off": -0.2,
        "value": 100,
        "chip": 100
      },
      {
        "at": "auto",
        "off": 1.2,
        "value": 100,
        "chip": 95
      },
      {
        "at": "schalt",
        "off": 2.6,
        "value": 100,
        "chip": 40
      },
      {
        "at": "schalt",
        "off": 4.6,
        "value": 100,
        "chip": 10
      },
      {
        "at": "kupplung",
        "off": 2.0,
        "value": 60,
        "chip": 0
      },
      {
        "at": "fall3",
        "off": -0.2,
        "value": 100,
        "chip": 100
      },
      {
        "at": "rekord",
        "off": 1.2,
        "value": 275,
        "chip": 100
      }
    ]
  },
  "interact": [
    {
      "type": "save",
      "at": "auto",
      "off": 2.0,
      "dur": 2.6,
      "text": "SPEICHER DAS FÜR DEINE <span class='y'>FAHRSTUNDE</span>"
    },
    {
      "type": "follow",
      "at": "kupplung",
      "off": 1.0,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "rekord",
      "off": 1.5,
      "dur": 2.6,
      "text": "LIKE, WENN DU'S NICHT WUSSTEST"
    },
    {
      "type": "comment",
      "at": "komm",
      "off": 0,
      "dur": 2.2,
      "text": "SCHREIB A, B ODER C"
    },
    {
      "type": "follow",
      "at": "folg",
      "off": 0,
      "dur": 2.6,
      "text": "FOLG MIR – <span class='y'>VOLLGAS</span>"
    }
  ],
  "sfx": [
    {
      "type": "riser",
      "at": "hook",
      "off": 0.0
    },
    {
      "type": "glitch",
      "at": "auto",
      "off": 1.2
    },
    {
      "type": "ding",
      "at": "fall1",
      "off": 0
    },
    {
      "type": "alarm",
      "at": "auto",
      "off": 2.3,
      "dur": 1.2
    },
    {
      "type": "glitch",
      "at": "schalt",
      "off": 2.4
    },
    {
      "type": "glitch",
      "at": "schalt",
      "off": 3.0
    },
    {
      "type": "boom",
      "at": "schalt",
      "off": 4.4
    },
    {
      "type": "heartbeat",
      "at": "kupplung",
      "off": 1.0,
      "dur": 2.5
    },
    {
      "type": "ding",
      "at": "fall3",
      "off": 0
    },
    {
      "type": "alarm",
      "at": "elektro",
      "off": 2.4,
      "dur": 1.0
    },
    {
      "type": "rise",
      "at": "rekord",
      "off": 0.5,
      "dur": 3
    },
    {
      "type": "ding",
      "at": "frage",
      "off": -0.2
    },
    {
      "type": "boom",
      "at": "kata",
      "off": 0.614
    }
  ]
};
