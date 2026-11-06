window.TIMING = {
  "title": "Was passiert, wenn du jeden Tag deine Finger knackst?",
  "duration": 53.12,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.15,
      "t1": 1.935,
      "chunks": [
        "Du knackst jeden Tag deine Finger."
      ],
      "noCap": true,
      "chunkStarts": [
        0.15
      ]
    },
    {
      "id": "loop",
      "t0": 2.155,
      "t1": 7.685,
      "chunks": [
        "Alle sagen:",
        "Davon kriegst du *Arthrose.*",
        "Am Ende siehst du,",
        "was nach ^fünfzig Jahren^",
        "wirklich passiert."
      ],
      "chunkStarts": [
        2.155,
        2.779,
        4.502,
        5.661,
        6.661
      ]
    },
    {
      "id": "frage1",
      "t0": 7.905,
      "t1": 9.1,
      "chunks": [
        "^Was knackt da eigentlich?^"
      ],
      "chunkStarts": [
        7.905
      ]
    },
    {
      "id": "blase",
      "t0": 9.466,
      "t1": 17.089,
      "chunks": [
        "Nicht deine Knochen.",
        "Im Gelenk ist Flüssigkeit.",
        "Ziehst du am Finger,",
        "sinkt der Druck.",
        "Und blitzschnell",
        "entsteht eine ~Gasblase.~",
        "Das ist das *Knacken.*"
      ],
      "chunkStarts": [
        9.466,
        10.326,
        12.027,
        13.012,
        13.831,
        14.494,
        15.77
      ]
    },
    {
      "id": "dann",
      "t0": 17.309,
      "t1": 17.977,
      "chunks": [
        "^Und dann?^"
      ],
      "chunkStarts": [
        17.309
      ]
    },
    {
      "id": "pause",
      "t0": 18.343,
      "t1": 21.826,
      "chunks": [
        "Musst du warten.",
        "Erst nach rund",
        "^zwanzig Minuten^",
        "knackt derselbe Finger",
        "wieder."
      ],
      "chunkStarts": [
        18.343,
        19.225,
        19.87,
        20.594,
        21.566
      ]
    },
    {
      "id": "jahre",
      "t0": 22.045,
      "t1": 23.145,
      "chunks": [
        "^Zehn Jahre später.^"
      ],
      "chunkStarts": [
        22.045
      ]
    },
    {
      "id": "studie",
      "t0": 23.365,
      "t1": 28.573,
      "chunks": [
        "Eine Studie",
        "mit dreihundert Menschen",
        "fand: Knacker hatten öfter",
        "*geschwollene Hände*",
        "und weniger Kraft",
        "im Griff."
      ],
      "chunkStarts": [
        23.365,
        23.691,
        24.497,
        26.081,
        26.843,
        27.85
      ]
    },
    {
      "id": "arthrose",
      "t0": 28.793,
      "t1": 30.962,
      "chunks": [
        "Aber Arthrose?",
        "~Kein Unterschied.~"
      ],
      "chunkStarts": [
        28.793,
        29.701
      ]
    },
    {
      "id": "verrueckt",
      "t0": 31.182,
      "t1": 31.79,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        31.182,
        31.35
      ]
    },
    {
      "id": "unger",
      "t0": 31.922,
      "t1": 39.263,
      "chunks": [
        "Ein Arzt knackte",
        "fünfzig Jahre lang",
        "nur die Finger",
        "seiner *linken* Hand.",
        "Die rechte",
        "ließ er in Ruhe.",
        "Am Ende:",
        "beide Hände ~gesund.~"
      ],
      "chunkStarts": [
        31.922,
        33.022,
        33.843,
        34.463,
        35.529,
        35.984,
        37.084,
        37.689
      ]
    },
    {
      "id": "fazit",
      "t0": 39.483,
      "t1": 43.371,
      "chunks": [
        "Also: Knacken",
        "macht keine Arthrose.",
        "Aber tut es weh,",
        "geh zum ^Arzt.^"
      ],
      "chunkStarts": [
        39.483,
        40.343,
        41.815,
        42.535
      ]
    },
    {
      "id": "frage",
      "t0": 43.591,
      "t1": 44.715,
      "chunks": [
        "Knackst du auch jeden Tag?"
      ],
      "noCap": true,
      "chunkStarts": [
        43.591
      ]
    },
    {
      "id": "komm",
      "t0": 44.997,
      "t1": 47.794,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        44.997
      ]
    },
    {
      "id": "folg",
      "t0": 48.014,
      "t1": 50.46,
      "chunks": [
        "Und folg mir. Bevor du wieder knackst."
      ],
      "noCap": true,
      "chunkStarts": [
        48.014
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
      "at": "frage1",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "dann",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "jahre",
      "off": -0.2
    },
    {
      "id": "s5",
      "at": "verrueckt",
      "off": -0.2
    },
    {
      "id": "s6",
      "at": "fazit",
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
      "at": "frage1",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "GEKNACKT",
    "unit": "MAL",
    "sub": "PRO FINGER · ZWEIMAL AM TAG",
    "chipLabel": "GELENK",
    "steps": [
      {
        "at": "frage1",
        "off": -0.2,
        "value": 1,
        "chip": 100
      },
      {
        "at": "dann",
        "off": 0,
        "value": 2,
        "chip": 100
      },
      {
        "at": "jahre",
        "off": 0,
        "value": 7300,
        "chip": 100
      },
      {
        "at": "studie",
        "off": 2.6,
        "value": 7300,
        "chip": 70
      },
      {
        "at": "arthrose",
        "off": 0.6,
        "value": 7300,
        "chip": 90
      },
      {
        "at": "unger",
        "off": 1.0,
        "value": 36500,
        "chip": 90
      },
      {
        "at": "unger",
        "off": 5.5,
        "value": 36500,
        "chip": 100
      }
    ]
  },
  "interact": [
    {
      "type": "save",
      "at": "pause",
      "off": 0.5,
      "dur": 2.6,
      "text": "SCHICK'S DEM <span class='y'>FINGERKNACKER</span>"
    },
    {
      "type": "follow",
      "at": "studie",
      "off": 0.3,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "unger",
      "off": 3.0,
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
      "text": "FOLG MIR – <span class='y'>KNACK!</span>"
    }
  ],
  "sfx": [
    {
      "type": "riser",
      "at": "hook",
      "off": 0.0
    },
    {
      "type": "ding",
      "at": "frage1",
      "off": 0
    },
    {
      "type": "glitch",
      "at": "blase",
      "off": 3.4
    },
    {
      "type": "ding",
      "at": "dann",
      "off": 0
    },
    {
      "type": "heartbeat",
      "at": "studie",
      "off": 2.4,
      "dur": 2.0
    },
    {
      "type": "ding",
      "at": "verrueckt",
      "off": 0
    },
    {
      "type": "rise",
      "at": "unger",
      "off": 3.5,
      "dur": 3
    },
    {
      "type": "ding",
      "at": "frage",
      "off": -0.2
    }
  ]
};
