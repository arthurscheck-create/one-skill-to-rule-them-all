window.TIMING = {
  "title": "Was passiert, wenn du 7 Tage nichts isst?",
  "duration": 49.44,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.152,
      "t1": 1.95,
      "chunks": [
        "Sieben Tage. Kein Essen."
      ],
      "noCap": true,
      "chunkStarts": [
        0.152
      ]
    },
    {
      "id": "loop",
      "t0": 2.178,
      "t1": 6.222,
      "chunks": [
        "Nur Wasser.",
        "Und an Tag drei",
        "passiert etwas",
        "^Seltsames^ in deinem Körper."
      ],
      "chunkStarts": [
        2.178,
        3.062,
        3.956,
        4.608
      ]
    },
    {
      "id": "t1",
      "t0": 6.451,
      "t1": 6.851,
      "chunks": [
        "^Tag eins.^"
      ],
      "chunkStarts": [
        6.451
      ]
    },
    {
      "id": "hunger",
      "t0": 7.079,
      "t1": 12.084,
      "chunks": [
        "Dein Magen knurrt.",
        "Dein Körper verbrennt",
        "seine *Zuckerreserven.*",
        "Nach rund einem Tag",
        "sind sie fast leer."
      ],
      "chunkStarts": [
        7.079,
        7.961,
        8.824,
        10.0,
        10.963
      ]
    },
    {
      "id": "t2",
      "t0": 12.312,
      "t1": 12.712,
      "chunks": [
        "^Tag zwei.^"
      ],
      "chunkStarts": [
        12.312
      ]
    },
    {
      "id": "schwer",
      "t0": 12.941,
      "t1": 18.708,
      "chunks": [
        "Du bist müde,",
        "gereizt,",
        "und dir ist kalt.",
        "Auf der Waage",
        "fehlt schon einiges.",
        "Aber das ist",
        "vor allem *Wasser.*"
      ],
      "chunkStarts": [
        12.941,
        13.669,
        14.443,
        15.388,
        15.997,
        16.935,
        17.657
      ]
    },
    {
      "id": "t3",
      "t0": 18.937,
      "t1": 19.337,
      "chunks": [
        "^Tag drei.^"
      ],
      "chunkStarts": [
        18.937
      ]
    },
    {
      "id": "keto",
      "t0": 19.565,
      "t1": 26.303,
      "chunks": [
        "Jetzt schaltet",
        "dein Körper um.",
        "Er verbrennt Fett",
        "und macht daraus",
        "neue Energie:",
        "~Ketone.~",
        "Viele haben sogar",
        "weniger Hunger."
      ],
      "chunkStarts": [
        19.565,
        20.097,
        20.906,
        21.901,
        22.62,
        23.607,
        24.323,
        25.275
      ]
    },
    {
      "id": "t7",
      "t0": 26.532,
      "t1": 27.248,
      "chunks": [
        "^Tag sieben.^"
      ],
      "chunkStarts": [
        26.532
      ]
    },
    {
      "id": "ende",
      "t0": 27.476,
      "t1": 30.932,
      "chunks": [
        "In einer Studie",
        "verloren Menschen",
        "rund ^sechs Kilo.^",
        "Aber auch",
        "*Muskeln.*"
      ],
      "chunkStarts": [
        27.476,
        28.069,
        28.745,
        29.659,
        30.341
      ]
    },
    {
      "id": "verrueckt",
      "t0": 31.161,
      "t1": 32.037,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        31.161,
        31.336
      ]
    },
    {
      "id": "gefahr",
      "t0": 32.417,
      "t1": 38.781,
      "chunks": [
        "Am gefährlichsten",
        "ist oft nicht das Fasten.",
        "Sondern das erste",
        "große *Essen danach.*",
        "Darum so etwas",
        "nur mit Arzt."
      ],
      "chunkStarts": [
        32.417,
        33.1,
        34.486,
        35.613,
        37.014,
        38.035
      ]
    },
    {
      "id": "frage",
      "t0": 39.01,
      "t1": 40.625,
      "chunks": [
        "Wie lange würdest du durchhalten?"
      ],
      "noCap": true,
      "chunkStarts": [
        39.01
      ]
    },
    {
      "id": "komm",
      "t0": 40.733,
      "t1": 43.49,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        40.733
      ]
    },
    {
      "id": "folg",
      "t0": 43.718,
      "t1": 46.78,
      "chunks": [
        "Und folg mir. Am besten mit vollem Magen."
      ],
      "noCap": true,
      "chunkStarts": [
        43.718
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
      "at": "t1",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "t2",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "t3",
      "off": -0.2
    },
    {
      "id": "s5",
      "at": "t7",
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
      "at": "t1",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "OHNE ESSEN",
    "unit": "",
    "sub": "NUR WASSER · NICHT NACHMACHEN",
    "chipLabel": "ENERGIE",
    "steps": [
      {
        "at": "t1",
        "off": -0.2,
        "value": 0,
        "chip": 90
      },
      {
        "at": "hunger",
        "off": 3,
        "value": 0,
        "chip": 60
      },
      {
        "at": "t2",
        "off": 0,
        "value": 0,
        "chip": 40
      },
      {
        "at": "t3",
        "off": 0,
        "value": 0,
        "chip": 45
      },
      {
        "at": "keto",
        "off": 3,
        "value": 0,
        "chip": 65
      },
      {
        "at": "t7",
        "off": 0,
        "value": 0,
        "chip": 50
      },
      {
        "at": "gefahr",
        "off": 2,
        "value": 0,
        "chip": 20
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "schwer",
      "off": 0.4,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "gefahr",
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
      "text": "FOLG MIR – <span class='y'>GUTEN APPETIT</span>"
    }
  ],
  "sfx": [
    {
      "type": "ding",
      "at": "t1",
      "off": 0
    },
    {
      "type": "ding",
      "at": "t2",
      "off": 0
    },
    {
      "type": "ding",
      "at": "t3",
      "off": 0
    },
    {
      "type": "rise",
      "at": "keto",
      "off": 1,
      "dur": 3
    },
    {
      "type": "ding",
      "at": "t7",
      "off": 0
    },
    {
      "type": "alarm",
      "at": "gefahr",
      "off": 2,
      "dur": 1
    },
    {
      "type": "ding",
      "at": "frage",
      "off": -0.2
    }
  ]
};
