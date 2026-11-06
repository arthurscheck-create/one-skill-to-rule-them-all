window.TIMING = {
  "title": "Was passiert, wenn du jeden Tag 5 Tassen Kaffee trinkst?",
  "duration": 46.25,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.105,
      "t1": 2.841,
      "chunks": [
        "Fünf Tassen Kaffee. Jeden Tag."
      ],
      "noCap": true,
      "chunkStarts": [
        0.105
      ]
    },
    {
      "id": "loop",
      "t0": 3.078,
      "t1": 7.522,
      "chunks": [
        "Ist das zu viel?",
        "Am Ende siehst du,",
        "was eine große Studie",
        "^herausgefunden^ hat."
      ],
      "chunkStarts": [
        3.078,
        4.217,
        5.549,
        6.629
      ]
    },
    {
      "id": "tasse1",
      "t0": 7.758,
      "t1": 8.27,
      "chunks": [
        "^Tasse eins.^"
      ],
      "chunkStarts": [
        7.758
      ]
    },
    {
      "id": "wach",
      "t0": 8.507,
      "t1": 12.81,
      "chunks": [
        "Schon nach kurzer Zeit",
        "wirkt das Koffein.",
        "Es blockiert den Stoff,",
        "der dich *müde* macht."
      ],
      "chunkStarts": [
        8.507,
        9.526,
        10.642,
        12.068
      ]
    },
    {
      "id": "tasse3",
      "t0": 13.047,
      "t1": 13.56,
      "chunks": [
        "^Tasse drei.^"
      ],
      "chunkStarts": [
        13.047
      ]
    },
    {
      "id": "herz",
      "t0": 13.796,
      "t1": 16.964,
      "chunks": [
        "Dein Herz schlägt",
        "etwas schneller.",
        "Und du musst",
        "öfter aufs Klo."
      ],
      "chunkStarts": [
        13.796,
        14.669,
        15.385,
        16.206
      ]
    },
    {
      "id": "tasse5",
      "t0": 17.2,
      "t1": 18.163,
      "chunks": [
        "^Tasse fünf.^"
      ],
      "chunkStarts": [
        17.2
      ]
    },
    {
      "id": "grenze",
      "t0": 18.4,
      "t1": 23.967,
      "chunks": [
        "Jetzt bist du",
        "bei rund ^vierhundert^",
        "Milligramm Koffein.",
        "Für gesunde Erwachsene",
        "gilt das noch",
        "als ~unbedenklich.~"
      ],
      "chunkStarts": [
        18.4,
        18.742,
        19.667,
        21.023,
        22.155,
        22.783
      ]
    },
    {
      "id": "schlaf",
      "t0": 24.204,
      "t1": 27.079,
      "chunks": [
        "Aber trinkst du",
        "die letzte Tasse",
        "am Abend,",
        "leidet dein *Schlaf.*"
      ],
      "chunkStarts": [
        24.204,
        24.632,
        25.311,
        26.237
      ]
    },
    {
      "id": "verrueckt",
      "t0": 27.316,
      "t1": 27.96,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        27.316,
        27.549
      ]
    },
    {
      "id": "studie",
      "t0": 28.354,
      "t1": 36.395,
      "chunks": [
        "In einer Studie",
        "mit neunzigtausend Menschen",
        "lebten Kaffeetrinker",
        "im Schnitt sogar",
        "~länger.~",
        "Ob das am Kaffee liegt,",
        "ist aber unklar."
      ],
      "chunkStarts": [
        28.354,
        28.987,
        30.433,
        31.633,
        32.633,
        33.217,
        35.054
      ]
    },
    {
      "id": "frage",
      "t0": 36.632,
      "t1": 37.666,
      "chunks": [
        "Wie viele Tassen trinkst du?"
      ],
      "noCap": true,
      "chunkStarts": [
        36.632
      ]
    },
    {
      "id": "komm",
      "t0": 38.061,
      "t1": 40.156,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        38.061
      ]
    },
    {
      "id": "folg",
      "t0": 40.393,
      "t1": 43.589,
      "chunks": [
        "Und folg mir. Am besten mit einem Kaffee."
      ],
      "noCap": true,
      "chunkStarts": [
        40.393
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
      "at": "tasse1",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "tasse3",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "tasse5",
      "off": -0.2
    },
    {
      "id": "s5",
      "at": "verrueckt",
      "off": -0.2
    },
    {
      "id": "s6",
      "at": "frage",
      "off": -0.05
    }
  ],
  "hud": {
    "show": {
      "at": "tasse1",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "KOFFEIN",
    "unit": "MG",
    "sub": "HEUTE GETRUNKEN",
    "chipLabel": "SCHLAF",
    "steps": [
      {
        "at": "tasse1",
        "off": -0.2,
        "value": 80,
        "chip": 100
      },
      {
        "at": "tasse3",
        "off": 0,
        "value": 240,
        "chip": 90
      },
      {
        "at": "tasse5",
        "off": 0,
        "value": 400,
        "chip": 75
      },
      {
        "at": "schlaf",
        "off": 2,
        "value": 400,
        "chip": 35
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "herz",
      "off": 0.4,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "studie",
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
      "text": "FOLG MIR – <span class='y'>KAFFEEPAUSE</span>"
    }
  ],
  "sfx": [
    {
      "type": "ding",
      "at": "tasse1",
      "off": 0
    },
    {
      "type": "ding",
      "at": "tasse3",
      "off": 0
    },
    {
      "type": "heartbeat",
      "at": "herz",
      "off": 0,
      "dur": 2.5
    },
    {
      "type": "ding",
      "at": "tasse5",
      "off": 0
    },
    {
      "type": "ding",
      "at": "verrueckt",
      "off": 0
    },
    {
      "type": "rise",
      "at": "studie",
      "off": 2,
      "dur": 3
    },
    {
      "type": "ding",
      "at": "frage",
      "off": -0.2
    }
  ]
};
