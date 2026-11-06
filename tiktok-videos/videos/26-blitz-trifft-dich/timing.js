window.TIMING = {
  "title": "Was passiert, wenn dich ein Blitz trifft?",
  "duration": 41.99,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.151,
      "t1": 1.206,
      "chunks": [
        "Der Blitz trifft dich."
      ],
      "noCap": true,
      "chunkStarts": [
        0.151
      ]
    },
    {
      "id": "kata",
      "t0": 1.421,
      "t1": 3.182,
      "chunks": [
        "Heißer als",
        "die Oberfläche der",
        "*Sonne.*"
      ],
      "chunkStarts": [
        1.421,
        1.847,
        2.622
      ]
    },
    {
      "id": "loop",
      "t0": 3.398,
      "t1": 8.369,
      "chunks": [
        "Und trotzdem",
        "überleben ^neun von zehn.^",
        "Am Ende siehst du,",
        "was viele *für immer* mitnehmen."
      ],
      "chunkStarts": [
        3.398,
        3.878,
        5.363,
        6.689
      ]
    },
    {
      "id": "treffer",
      "t0": 8.584,
      "t1": 9.582,
      "chunks": [
        "^Der Einschlag.^"
      ],
      "chunkStarts": [
        8.584
      ]
    },
    {
      "id": "strom",
      "t0": 9.798,
      "t1": 14.299,
      "chunks": [
        "Der Strom rast",
        "meist ~über~ deine Haut.",
        "Nicht durch dich hindurch.",
        "Das rettet",
        "vielen das Leben."
      ],
      "chunkStarts": [
        9.798,
        10.546,
        11.571,
        13.128,
        13.642
      ]
    },
    {
      "id": "herz",
      "t0": 14.514,
      "t1": 19.958,
      "chunks": [
        "Aber er kann",
        "dein Herz",
        "*stoppen.*",
        "Dann zählt",
        "jede Sekunde.",
        "Sofort wiederbeleben",
        "hilft oft."
      ],
      "chunkStarts": [
        14.514,
        15.065,
        15.582,
        16.042,
        16.846,
        17.719,
        18.996
      ]
    },
    {
      "id": "danach",
      "t0": 20.174,
      "t1": 20.932,
      "chunks": [
        "^Die Tage danach.^"
      ],
      "chunkStarts": [
        20.174
      ]
    },
    {
      "id": "figur",
      "t0": 21.147,
      "t1": 26.969,
      "chunks": [
        "Auf deiner Haut",
        "erscheint ein Muster",
        "wie ein ~Farn.~",
        "Eine Lichtenberg-Figur.",
        "Sie verschwindet",
        "meist nach ein paar Tagen."
      ],
      "chunkStarts": [
        21.147,
        21.599,
        22.447,
        23.408,
        25.088,
        25.973
      ]
    },
    {
      "id": "verrueckt",
      "t0": 27.184,
      "t1": 28.028,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        27.184,
        27.368
      ]
    },
    {
      "id": "folgen",
      "t0": 28.335,
      "t1": 32.823,
      "chunks": [
        "Viele Überlebende",
        "hören danach schlechter",
        "oder haben",
        "*Nervenschmerzen.*",
        "Manchmal jahrelang."
      ],
      "chunkStarts": [
        28.335,
        29.128,
        30.228,
        30.67,
        31.689
      ]
    },
    {
      "id": "frage",
      "t0": 33.039,
      "t1": 34.283,
      "chunks": [
        "Wo bist du bei Gewitter?"
      ],
      "noCap": true,
      "chunkStarts": [
        33.039
      ]
    },
    {
      "id": "komm",
      "t0": 34.531,
      "t1": 36.871,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        34.531
      ]
    },
    {
      "id": "folg",
      "t0": 37.086,
      "t1": 39.345,
      "chunks": [
        "Und folg mir. Bevor es donnert."
      ],
      "noCap": true,
      "chunkStarts": [
        37.086
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
      "at": "treffer",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "herz",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "danach",
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
      "at": "treffer",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "TEMPERATUR",
    "unit": "°C",
    "sub": "IM BLITZKANAL",
    "chipLabel": "HERZ",
    "steps": [
      {
        "at": "treffer",
        "off": -0.2,
        "value": 30000,
        "chip": 100
      },
      {
        "at": "herz",
        "off": 1.5,
        "value": 30000,
        "chip": 0
      },
      {
        "at": "herz",
        "off": 4.5,
        "value": 37,
        "chip": 100
      },
      {
        "at": "folgen",
        "off": 2,
        "value": 37,
        "chip": 70
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "strom",
      "off": 0.4,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "folgen",
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
      "text": "FOLG MIR – <span class='y'>GEWITTERFEST</span>"
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
      "at": "treffer",
      "off": 0
    },
    {
      "type": "glitch",
      "at": "treffer",
      "off": 0.1
    },
    {
      "type": "heartbeat",
      "at": "herz",
      "off": 0,
      "dur": 1.5
    },
    {
      "type": "alarm",
      "at": "herz",
      "off": 1.6,
      "dur": 1
    },
    {
      "type": "ding",
      "at": "danach",
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
      "off": 0.426
    }
  ]
};
