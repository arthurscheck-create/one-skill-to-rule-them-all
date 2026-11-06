window.TIMING = {
  "title": "Was passiert, wenn du im Flugzeug die Tür öffnest?",
  "duration": 47.24,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.115,
      "t1": 2.427,
      "chunks": [
        "Zehntausend Meter. Du ziehst am Türgriff."
      ],
      "noCap": true,
      "chunkStarts": [
        0.115
      ]
    },
    {
      "id": "kata",
      "t0": 2.657,
      "t1": 5.327,
      "chunks": [
        "Was dann passiert,",
        "*überrascht* fast jeden."
      ],
      "chunkStarts": [
        2.657,
        3.791
      ]
    },
    {
      "id": "loop",
      "t0": 5.558,
      "t1": 8.275,
      "chunks": [
        "Am Ende erfährst du,",
        "wann es doch",
        "^gefährlich^ wird."
      ],
      "chunkStarts": [
        5.558,
        6.665,
        7.553
      ]
    },
    {
      "id": "zu",
      "t0": 8.505,
      "t1": 9.691,
      "chunks": [
        "^Die Tür bewegt sich nicht.^"
      ],
      "chunkStarts": [
        8.505
      ]
    },
    {
      "id": "druck",
      "t0": 9.922,
      "t1": 15.46,
      "chunks": [
        "Im Flugzeug herrscht",
        "höherer Luftdruck",
        "als draußen.",
        "Dieser Druck presst",
        "die Tür von innen",
        "fest in den Rahmen."
      ],
      "chunkStarts": [
        9.922,
        10.75,
        11.466,
        12.179,
        13.263,
        14.182
      ]
    },
    {
      "id": "stopfen",
      "t0": 15.69,
      "t1": 21.482,
      "chunks": [
        "Die Tür ist gebaut",
        "wie ein *Stöpsel.*",
        "Sie öffnet sich erst",
        "nach innen.",
        "Und dagegen drücken",
        "rund ^zehn Tonnen.^"
      ],
      "chunkStarts": [
        15.69,
        16.412,
        17.196,
        18.311,
        19.2,
        20.314
      ]
    },
    {
      "id": "mensch",
      "t0": 21.712,
      "t1": 23.945,
      "chunks": [
        "Kein Mensch",
        "schafft das.",
        "Nicht mal zehn."
      ],
      "chunkStarts": [
        21.712,
        22.24,
        23.11
      ]
    },
    {
      "id": "verrueckt",
      "t0": 24.175,
      "t1": 24.874,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        24.175,
        24.352
      ]
    },
    {
      "id": "landung",
      "t0": 25.258,
      "t1": 36.53,
      "chunks": [
        "Gefährlich wird es",
        "erst ~kurz vor der Landung.~",
        "Dann ist der Druck",
        "fast ausgeglichen.",
        "2023 öffnete ein Passagier",
        "in Südkorea",
        "eine Tür im Landeanflug.",
        "Der Wind *peitschte*",
        "durch die Kabine."
      ],
      "chunkStarts": [
        25.258,
        25.839,
        27.154,
        28.124,
        29.326,
        32.392,
        33.126,
        34.932,
        35.936
      ]
    },
    {
      "id": "frage",
      "t0": 36.76,
      "t1": 38.55,
      "chunks": [
        "Würdest du am Notausgang sitzen?"
      ],
      "noCap": true,
      "chunkStarts": [
        36.76
      ]
    },
    {
      "id": "komm",
      "t0": 38.907,
      "t1": 41.438,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        38.907
      ]
    },
    {
      "id": "folg",
      "t0": 41.668,
      "t1": 44.586,
      "chunks": [
        "Und folg mir. Bevor du das nächste Mal fliegst."
      ],
      "noCap": true,
      "chunkStarts": [
        41.668
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
      "at": "zu",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "stopfen",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "verrueckt",
      "off": -0.2
    },
    {
      "id": "s5",
      "at": "frage",
      "off": -0.05
    }
  ],
  "hud": {
    "show": {
      "at": "zu",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "HÖHE",
    "unit": "M",
    "sub": "FLUG · REISEFLUG",
    "chipLabel": "TÜR ZU",
    "steps": [
      {
        "at": "zu",
        "off": -0.2,
        "value": 10000,
        "chip": 100
      },
      {
        "at": "landung",
        "off": 0.5,
        "value": 10000,
        "chip": 100
      },
      {
        "at": "landung",
        "off": 3,
        "value": 200,
        "chip": 25
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "stopfen",
      "off": 0.4,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "landung",
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
      "text": "FOLG MIR – <span class='y'>ANSCHNALLEN</span>"
    }
  ],
  "sfx": [
    {
      "type": "riser",
      "at": "hook",
      "off": 0
    },
    {
      "type": "ding",
      "at": "zu",
      "off": 0
    },
    {
      "type": "heartbeat",
      "at": "stopfen",
      "off": 2.5,
      "dur": 2
    },
    {
      "type": "ding",
      "at": "verrueckt",
      "off": 0
    },
    {
      "type": "alarm",
      "at": "landung",
      "off": 4.5,
      "dur": 1.5
    },
    {
      "type": "ding",
      "at": "frage",
      "off": -0.2
    },
    {
      "type": "boom",
      "at": "kata",
      "off": 1.134
    }
  ]
};
