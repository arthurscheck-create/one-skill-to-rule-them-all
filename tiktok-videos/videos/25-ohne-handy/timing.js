window.TIMING = {
  "title": "Was passiert, wenn du 30 Tage kein Handy benutzt?",
  "duration": 44.71,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.151,
      "t1": 1.798,
      "chunks": [
        "Dreißig Tage. Kein Handy."
      ],
      "noCap": true,
      "chunkStarts": [
        0.151
      ]
    },
    {
      "id": "loop",
      "t0": 2.031,
      "t1": 6.336,
      "chunks": [
        "Klingt unmöglich?",
        "Am Ende siehst du,",
        "was das mit deinem",
        "^Kopf^ macht."
      ],
      "chunkStarts": [
        2.031,
        3.132,
        4.32,
        5.266
      ]
    },
    {
      "id": "t1",
      "t0": 6.568,
      "t1": 7.03,
      "chunks": [
        "^Tag eins.^"
      ],
      "chunkStarts": [
        6.568
      ]
    },
    {
      "id": "griff",
      "t0": 7.263,
      "t1": 11.955,
      "chunks": [
        "Deine Hand greift",
        "ständig in die Tasche.",
        "Du glaubst,",
        "es *vibriert.*",
        "Dabei liegt es",
        "zu Hause."
      ],
      "chunkStarts": [
        7.263,
        7.872,
        8.802,
        9.464,
        10.327,
        11.035
      ]
    },
    {
      "id": "t3",
      "t0": 12.188,
      "t1": 12.668,
      "chunks": [
        "^Tag drei.^"
      ],
      "chunkStarts": [
        12.188
      ]
    },
    {
      "id": "leer",
      "t0": 12.901,
      "t1": 18.195,
      "chunks": [
        "Dir ist",
        "*langweilig.*",
        "Richtig langweilig.",
        "Und genau dann",
        "fängst du an,",
        "wieder nachzudenken."
      ],
      "chunkStarts": [
        12.901,
        13.16,
        13.963,
        15.405,
        16.397,
        17.229
      ]
    },
    {
      "id": "w2",
      "t0": 18.428,
      "t1": 19.18,
      "chunks": [
        "^Zwei Wochen später.^"
      ],
      "chunkStarts": [
        18.428
      ]
    },
    {
      "id": "studie",
      "t0": 19.412,
      "t1": 26.399,
      "chunks": [
        "In einer Studie",
        "blockierten Menschen",
        "nur das Internet",
        "auf dem Handy.",
        "Nach zwei Wochen",
        "konnten sie sich",
        "~besser konzentrieren.~",
        "Und fühlten sich besser."
      ],
      "chunkStarts": [
        19.412,
        20.043,
        20.818,
        21.655,
        22.517,
        23.36,
        24.016,
        25.159
      ]
    },
    {
      "id": "w3",
      "t0": 26.632,
      "t1": 27.136,
      "chunks": [
        "^Drei Wochen.^"
      ],
      "chunkStarts": [
        26.632
      ]
    },
    {
      "id": "schlaf",
      "t0": 27.368,
      "t1": 31.347,
      "chunks": [
        "In einem anderen Versuch",
        "hatten Menschen",
        "über ^zwanzig Prozent^",
        "weniger Schlafprobleme."
      ],
      "chunkStarts": [
        27.368,
        28.326,
        29.164,
        30.27
      ]
    },
    {
      "id": "verrueckt",
      "t0": 31.58,
      "t1": 32.347,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        31.58,
        31.82
      ]
    },
    {
      "id": "aufgeben",
      "t0": 32.735,
      "t1": 34.506,
      "chunks": [
        "Ein Drittel",
        "hat vorher",
        "*aufgegeben.*"
      ],
      "chunkStarts": [
        32.735,
        33.235,
        33.948
      ]
    },
    {
      "id": "frage",
      "t0": 34.739,
      "t1": 36.258,
      "chunks": [
        "Würdest du dreißig Tage schaffen?"
      ],
      "noCap": true,
      "chunkStarts": [
        34.739
      ]
    },
    {
      "id": "komm",
      "t0": 36.646,
      "t1": 38.828,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        36.646
      ]
    },
    {
      "id": "folg",
      "t0": 39.06,
      "t1": 42.064,
      "chunks": [
        "Und folg mir. Solange du noch ein Handy hast."
      ],
      "noCap": true,
      "chunkStarts": [
        39.06
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
      "at": "t3",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "w2",
      "off": -0.2
    },
    {
      "id": "s5",
      "at": "w3",
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
    "label": "OHNE HANDY",
    "unit": "",
    "sub": "DIGITAL DETOX",
    "chipLabel": "FOKUS",
    "steps": [
      {
        "at": "t1",
        "off": -0.2,
        "value": 0,
        "chip": 40
      },
      {
        "at": "t3",
        "off": 0,
        "value": 0,
        "chip": 30
      },
      {
        "at": "w2",
        "off": 0,
        "value": 0,
        "chip": 70
      },
      {
        "at": "w3",
        "off": 0,
        "value": 0,
        "chip": 85
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "leer",
      "off": 0.4,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "aufgeben",
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
      "text": "FOLG MIR – <span class='y'>NOCH KURZ</span>"
    }
  ],
  "sfx": [
    {
      "type": "ding",
      "at": "t1",
      "off": 0
    },
    {
      "type": "drip",
      "at": "griff",
      "off": 2
    },
    {
      "type": "drip",
      "at": "griff",
      "off": 2.4
    },
    {
      "type": "ding",
      "at": "t3",
      "off": 0
    },
    {
      "type": "ding",
      "at": "w2",
      "off": 0
    },
    {
      "type": "rise",
      "at": "studie",
      "off": 3,
      "dur": 3
    },
    {
      "type": "ding",
      "at": "w3",
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
    }
  ]
};
