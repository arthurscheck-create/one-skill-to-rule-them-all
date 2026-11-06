window.TIMING = {
  "title": "Was passiert, wenn der Blitz in dein Auto einschlägt?",
  "duration": 43.09,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.143,
      "t1": 1.332,
      "chunks": [
        "Ein Blitz trifft dein Auto."
      ],
      "noCap": true,
      "chunkStarts": [
        0.143
      ]
    },
    {
      "id": "kata",
      "t0": 1.57,
      "t1": 5.079,
      "chunks": [
        "Mit dreißigtausend Ampere.",
        "Und du sitzt",
        "*mittendrin.*"
      ],
      "chunkStarts": [
        1.57,
        3.239,
        4.279
      ]
    },
    {
      "id": "loop",
      "t0": 5.316,
      "t1": 8.2,
      "chunks": [
        "Am Ende erfährst du,",
        "wann es im Auto",
        "^doch gefährlich^ wird."
      ],
      "chunkStarts": [
        5.316,
        6.271,
        7.121
      ]
    },
    {
      "id": "knall",
      "t0": 8.438,
      "t1": 11.38,
      "chunks": [
        "^Ein greller Blitz.^",
        "Ein Knall,",
        "lauter als jeder Böller."
      ],
      "chunkStarts": [
        8.438,
        9.485,
        10.28
      ]
    },
    {
      "id": "mythos",
      "t0": 11.618,
      "t1": 14.351,
      "chunks": [
        "Viele glauben:",
        "Die Gummireifen",
        "schützen dich.",
        "*Falsch.*"
      ],
      "chunkStarts": [
        11.618,
        12.274,
        13.114,
        13.844
      ]
    },
    {
      "id": "kaefig",
      "t0": 14.589,
      "t1": 20.572,
      "chunks": [
        "Der Strom fließt",
        "außen über das Metall",
        "um dich herum",
        "und springt",
        "in den Boden.",
        "Das nennt man",
        "~Faradayscher Käfig.~"
      ],
      "chunkStarts": [
        14.589,
        15.37,
        16.511,
        17.368,
        17.886,
        18.772,
        19.43
      ]
    },
    {
      "id": "schaden",
      "t0": 20.81,
      "t1": 25.362,
      "chunks": [
        "^Und dein Auto?^",
        "Lack und Antenne",
        "können verkohlen.",
        "Die Elektronik",
        "kann ausfallen."
      ],
      "chunkStarts": [
        20.81,
        21.631,
        22.86,
        23.712,
        24.638
      ]
    },
    {
      "id": "verrueckt",
      "t0": 25.6,
      "t1": 26.321,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        25.6,
        25.782
      ]
    },
    {
      "id": "cabrio",
      "t0": 26.718,
      "t1": 33.154,
      "chunks": [
        "Im Cabrio mit Stoffdach",
        "bist du *nicht* geschützt.",
        "Und fass im Gewitter",
        "keine Metallteile an.",
        "Bleib einfach ~sitzen.~"
      ],
      "chunkStarts": [
        26.718,
        28.015,
        29.268,
        30.722,
        31.933
      ]
    },
    {
      "id": "frage",
      "t0": 33.392,
      "t1": 34.619,
      "chunks": [
        "Wo würdest du dich verstecken?"
      ],
      "noCap": true,
      "chunkStarts": [
        33.392
      ]
    },
    {
      "id": "komm",
      "t0": 35.015,
      "t1": 37.66,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        35.015
      ]
    },
    {
      "id": "folg",
      "t0": 37.898,
      "t1": 40.454,
      "chunks": [
        "Und folg mir. Bevor das nächste Gewitter kommt."
      ],
      "noCap": true,
      "chunkStarts": [
        37.898
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
      "at": "knall",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "kaefig",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "schaden",
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
      "at": "knall",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "STROM",
    "unit": "A",
    "sub": "BLITZEINSCHLAG",
    "chipLabel": "SCHUTZ",
    "steps": [
      {
        "at": "knall",
        "off": -0.2,
        "value": 30000,
        "chip": 100
      },
      {
        "at": "mythos",
        "off": 2,
        "value": 30000,
        "chip": 100
      },
      {
        "at": "kaefig",
        "off": 3,
        "value": 0,
        "chip": 100
      },
      {
        "at": "cabrio",
        "off": 1,
        "value": 0,
        "chip": 20
      },
      {
        "at": "cabrio",
        "off": 4,
        "value": 0,
        "chip": 100
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "kaefig",
      "off": 0.4,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "cabrio",
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
      "text": "FOLG MIR – <span class='y'>BLEIB SITZEN</span>"
    }
  ],
  "sfx": [
    {
      "type": "riser",
      "at": "hook",
      "off": 0
    },
    {
      "type": "boom",
      "at": "knall",
      "off": 0.2
    },
    {
      "type": "glitch",
      "at": "knall",
      "off": 0.2
    },
    {
      "type": "ding",
      "at": "mythos",
      "off": 2.2
    },
    {
      "type": "ding",
      "at": "schaden",
      "off": 0
    },
    {
      "type": "ding",
      "at": "verrueckt",
      "off": 0
    },
    {
      "type": "ding",
      "at": "frage",
      "off": -0.2
    },
    {
      "type": "boom",
      "at": "kata",
      "off": 2.709
    }
  ]
};
