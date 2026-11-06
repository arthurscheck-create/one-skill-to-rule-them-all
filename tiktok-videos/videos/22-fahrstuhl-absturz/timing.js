window.TIMING = {
  "title": "Was passiert, wenn das Seil vom Fahrstuhl reißt?",
  "duration": 46.56,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.103,
      "t1": 1.086,
      "chunks": [
        "Das Seil reißt."
      ],
      "noCap": true,
      "chunkStarts": [
        0.103
      ]
    },
    {
      "id": "kata",
      "t0": 1.312,
      "t1": 4.08,
      "chunks": [
        "Und du fällst",
        "zwanzig Stockwerke",
        "in die *Tiefe.*"
      ],
      "chunkStarts": [
        1.312,
        1.938,
        3.004
      ]
    },
    {
      "id": "loop",
      "t0": 4.306,
      "t1": 8.22,
      "chunks": [
        "Hilft Springen",
        "kurz vor dem Aufprall?",
        "Am Ende kennst du",
        "die ^Antwort.^"
      ],
      "chunkStarts": [
        4.306,
        4.956,
        6.38,
        7.481
      ]
    },
    {
      "id": "s1",
      "t0": 8.446,
      "t1": 9.008,
      "chunks": [
        "^Sekunde eins.^"
      ],
      "chunkStarts": [
        8.446
      ]
    },
    {
      "id": "schwerelos",
      "t0": 9.234,
      "t1": 12.042,
      "chunks": [
        "Du wirst ~schwerelos.~",
        "Dein Handy schwebt",
        "vor deinem Gesicht."
      ],
      "chunkStarts": [
        9.234,
        10.413,
        11.431
      ]
    },
    {
      "id": "bremse",
      "t0": 12.268,
      "t1": 19.557,
      "chunks": [
        "Aber halt.",
        "Moderne Aufzüge",
        "hängen an mehreren Seilen.",
        "Und sie haben",
        "eine *Fangbremse.*",
        "Sie krallt sich",
        "in die Schienen",
        "und stoppt dich",
        "nach wenigen Metern."
      ],
      "chunkStarts": [
        12.268,
        12.91,
        13.855,
        15.175,
        15.671,
        16.585,
        17.364,
        18.003,
        18.748
      ]
    },
    {
      "id": "versagt",
      "t0": 19.783,
      "t1": 21.208,
      "chunks": [
        "^Und wenn alles versagt?^"
      ],
      "chunkStarts": [
        19.783
      ]
    },
    {
      "id": "springen",
      "t0": 21.585,
      "t1": 27.003,
      "chunks": [
        "Dann bringt Springen",
        "*fast nichts.*",
        "Du bremst dich",
        "nur ein winziges bisschen.",
        "Der Boden unter dir",
        "fällt ja mit."
      ],
      "chunkStarts": [
        21.585,
        22.357,
        23.202,
        23.79,
        25.057,
        26.158
      ]
    },
    {
      "id": "verrueckt",
      "t0": 27.229,
      "t1": 27.795,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        27.229,
        27.403
      ]
    },
    {
      "id": "rekord",
      "t0": 28.172,
      "t1": 36.566,
      "chunks": [
        "1945 stürzte",
        "ein Aufzug",
        "im ^Empire State Building^",
        "fünfundsiebzig Stockwerke ab.",
        "Die Frau darin",
        "~überlebte.~",
        "Bis heute ein Rekord."
      ],
      "chunkStarts": [
        28.172,
        29.719,
        30.292,
        31.498,
        33.278,
        34.322,
        35.043
      ]
    },
    {
      "id": "frage",
      "t0": 36.793,
      "t1": 38.399,
      "chunks": [
        "Fährst du jetzt noch Fahrstuhl?"
      ],
      "noCap": true,
      "chunkStarts": [
        36.793
      ]
    },
    {
      "id": "komm",
      "t0": 38.776,
      "t1": 41.321,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        38.776
      ]
    },
    {
      "id": "folg",
      "t0": 41.548,
      "t1": 43.918,
      "chunks": [
        "Und folg mir. Bevor du die Treppe nimmst."
      ],
      "noCap": true,
      "chunkStarts": [
        41.548
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
      "at": "s1",
      "off": -0.2
    },
    {
      "id": "s3",
      "at": "bremse",
      "off": -0.2
    },
    {
      "id": "s4",
      "at": "versagt",
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
      "at": "s1",
      "off": -0.2
    },
    "hide": {
      "at": "frage",
      "off": -0.05
    },
    "label": "STOCKWERK",
    "unit": "",
    "sub": "FREIER FALL",
    "chipLabel": "BREMSE",
    "steps": [
      {
        "at": "s1",
        "off": -0.2,
        "value": 20,
        "chip": 0
      },
      {
        "at": "schwerelos",
        "off": 1.5,
        "value": 19,
        "chip": 0
      },
      {
        "at": "bremse",
        "off": 4,
        "value": 18,
        "chip": 100
      },
      {
        "at": "versagt",
        "off": 0,
        "value": 18,
        "chip": 0
      },
      {
        "at": "springen",
        "off": 2,
        "value": 1,
        "chip": 0
      },
      {
        "at": "rekord",
        "off": 1,
        "value": 75,
        "chip": 0
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "bremse",
      "off": 0.4,
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
      "text": "FOLG MIR – <span class='y'>NIMM DIE TREPPE</span>"
    }
  ],
  "sfx": [
    {
      "type": "riser",
      "at": "hook",
      "off": 0
    },
    {
      "type": "rise",
      "at": "schwerelos",
      "off": 0,
      "dur": 2.5
    },
    {
      "type": "glitch",
      "at": "bremse",
      "off": 4
    },
    {
      "type": "ding",
      "at": "versagt",
      "off": 0
    },
    {
      "type": "boom",
      "at": "springen",
      "off": 3
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
      "off": 1.692
    }
  ]
};
