window.TIMING = {
  "title": "Was passiert, wenn du einen Kaugummi verschluckst?",
  "duration": 46.01,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.104,
      "t1": 1.698,
      "chunks": [
        "Du hast den Kaugummi verschluckt."
      ],
      "noCap": true,
      "chunkStarts": [
        0.104
      ]
    },
    {
      "id": "loop",
      "t0": 1.918,
      "t1": 7.317,
      "chunks": [
        "Bleibt er jetzt",
        "*sieben Jahre* in dir?",
        "Am Ende erfährst du,",
        "wann es wirklich",
        "^gefährlich^ wird."
      ],
      "chunkStarts": [
        1.918,
        2.456,
        4.116,
        5.419,
        6.19
      ]
    },
    {
      "id": "min",
      "t0": 7.537,
      "t1": 8.264,
      "chunks": [
        "^Minute eins.^"
      ],
      "chunkStarts": [
        7.537
      ]
    },
    {
      "id": "magen",
      "t0": 8.484,
      "t1": 15.462,
      "chunks": [
        "Der Kaugummi rutscht",
        "in deinen Magen.",
        "Die Säure löst Zucker",
        "und Aroma.",
        "Aber die Kaumasse?",
        "Die kann dein Körper",
        "*nicht verdauen.*"
      ],
      "chunkStarts": [
        8.484,
        9.293,
        10.074,
        11.406,
        12.323,
        13.8,
        14.671
      ]
    },
    {
      "id": "tage",
      "t0": 15.682,
      "t1": 16.582,
      "chunks": [
        "^Ein paar Tage später.^"
      ],
      "chunkStarts": [
        15.682
      ]
    },
    {
      "id": "weg",
      "t0": 16.802,
      "t1": 23.312,
      "chunks": [
        "Er wandert einfach",
        "durch deinen Darm",
        "und kommt ~ganz normal~",
        "wieder raus.",
        "Ärzte finden",
        "bei Untersuchungen",
        "keine alten Kaugummis."
      ],
      "chunkStarts": [
        16.802,
        17.602,
        18.422,
        19.597,
        20.471,
        21.174,
        21.897
      ]
    },
    {
      "id": "verrueckt",
      "t0": 23.531,
      "t1": 24.432,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        23.531,
        23.817
      ]
    },
    {
      "id": "fall",
      "t0": 24.754,
      "t1": 32.367,
      "chunks": [
        "Ein Junge schluckte",
        "jeden Tag",
        "^fünf bis sieben^ Kaugummis.",
        "Irgendwann saß",
        "eine *Kaugummi-Masse*",
        "in seinem Darm fest.",
        "Ärzte mussten sie",
        "entfernen."
      ],
      "chunkStarts": [
        24.754,
        25.408,
        26.028,
        28.136,
        28.918,
        29.624,
        30.786,
        31.677
      ]
    },
    {
      "id": "fazit",
      "t0": 32.587,
      "t1": 36.511,
      "chunks": [
        "Also:",
        "Einer ist",
        "~kein Problem.~",
        "Viele jeden Tag",
        "*schon.*"
      ],
      "chunkStarts": [
        32.587,
        33.056,
        33.688,
        34.593,
        35.887
      ]
    },
    {
      "id": "frage",
      "t0": 36.731,
      "t1": 38.013,
      "chunks": [
        "Hast du schon mal einen verschluckt?"
      ],
      "noCap": true,
      "chunkStarts": [
        36.731
      ]
    },
    {
      "id": "komm",
      "t0": 38.237,
      "t1": 40.332,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        38.237
      ]
    },
    {
      "id": "folg",
      "t0": 40.551,
      "t1": 43.554,
      "chunks": [
        "Und folg mir. Und spuck ihn lieber aus."
      ],
      "noCap": true,
      "chunkStarts": [
        40.551
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
      "at": "min",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "tage",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "verrueckt",
      "off": -0.2
    },
    {
      "id": "s5",
      "at": "fazit",
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
      "at": "min",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "IM KÖRPER SEIT",
    "unit": "",
    "sub": "KAUGUMMI-CHECK",
    "chipLabel": "MAGEN",
    "steps": [
      {
        "at": "min",
        "off": -0.2,
        "value": 0,
        "chip": 100
      },
      {
        "at": "magen",
        "off": 4,
        "value": 0,
        "chip": 90
      },
      {
        "at": "tage",
        "off": 0,
        "value": 0,
        "chip": 100
      },
      {
        "at": "fall",
        "off": 3,
        "value": 0,
        "chip": 20
      },
      {
        "at": "fazit",
        "off": 1,
        "value": 0,
        "chip": 100
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "weg",
      "off": 0.4,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "fall",
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
      "text": "FOLG MIR – <span class='y'>KAU DRAUF</span>"
    }
  ],
  "sfx": [
    {
      "type": "ding",
      "at": "min",
      "off": 0
    },
    {
      "type": "drip",
      "at": "magen",
      "off": 1
    },
    {
      "type": "drip",
      "at": "magen",
      "off": 1.6
    },
    {
      "type": "ding",
      "at": "tage",
      "off": 0
    },
    {
      "type": "alarm",
      "at": "fall",
      "off": 2.5,
      "dur": 1
    },
    {
      "type": "rise",
      "at": "fazit",
      "off": 0,
      "dur": 2.5
    },
    {
      "type": "ding",
      "at": "frage",
      "off": -0.2
    }
  ]
};
