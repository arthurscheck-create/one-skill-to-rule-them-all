window.TIMING = {
  "title": "Was passiert, wenn du im All den Helm abnimmst?",
  "duration": 46.28,
  "voice": "assets/voice.mp3",
  "lines": [
    {
      "id": "hook",
      "t0": 0.167,
      "t1": 1.814,
      "chunks": [
        "Du nimmst im All den Helm ab."
      ],
      "noCap": true,
      "chunkStarts": [
        0.167
      ]
    },
    {
      "id": "kata",
      "t0": 2.048,
      "t1": 5.242,
      "chunks": [
        "Explodierst du jetzt?",
        "Nein.",
        "Es ist *schlimmer.*"
      ],
      "chunkStarts": [
        2.048,
        3.22,
        4.116
      ]
    },
    {
      "id": "loop",
      "t0": 5.477,
      "t1": 8.74,
      "chunks": [
        "Am Ende erfährst du,",
        "wie lange du",
        "^wirklich^ überlebst."
      ],
      "chunkStarts": [
        5.477,
        6.582,
        7.238
      ]
    },
    {
      "id": "s1",
      "t0": 8.974,
      "t1": 9.628,
      "chunks": [
        "^Sekunde eins.^"
      ],
      "chunkStarts": [
        8.974
      ]
    },
    {
      "id": "luft",
      "t0": 9.862,
      "t1": 13.568,
      "chunks": [
        "Die Luft schießt",
        "aus deiner Lunge.",
        "Halt sie bloß *nicht* an.",
        "Sonst reißt sie."
      ],
      "chunkStarts": [
        9.862,
        10.535,
        11.348,
        12.654
      ]
    },
    {
      "id": "s5",
      "t0": 13.803,
      "t1": 14.385,
      "chunks": [
        "^Sekunde fünf.^"
      ],
      "chunkStarts": [
        13.803
      ]
    },
    {
      "id": "kochen",
      "t0": 14.619,
      "t1": 19.701,
      "chunks": [
        "Die Spucke auf deiner Zunge",
        "fängt an zu ~blubbern.~",
        "Ohne Luftdruck",
        "kocht Wasser",
        "schon bei Körpertemperatur."
      ],
      "chunkStarts": [
        14.619,
        15.604,
        16.783,
        17.637,
        18.294
      ]
    },
    {
      "id": "s10",
      "t0": 19.936,
      "t1": 20.784,
      "chunks": [
        "^Sekunde zehn.^"
      ],
      "chunkStarts": [
        19.936
      ]
    },
    {
      "id": "haut",
      "t0": 20.998,
      "t1": 25.543,
      "chunks": [
        "Dein Körper schwillt an.",
        "Aber deine Haut hält.",
        "Dann wird dir",
        "*schwarz vor Augen.*"
      ],
      "chunkStarts": [
        20.998,
        22.604,
        24.005,
        24.636
      ]
    },
    {
      "id": "verrueckt",
      "t0": 25.778,
      "t1": 26.482,
      "chunks": [
        "Und das",
        "^Verrückte?^"
      ],
      "chunkStarts": [
        25.778,
        26.013
      ]
    },
    {
      "id": "nasa",
      "t0": 26.873,
      "t1": 35.989,
      "chunks": [
        "Das ist einem Menschen",
        "wirklich passiert.",
        "Bei einem NASA-Test",
        "verlor sein Anzug die Luft.",
        "Nach rund ^vierzehn Sekunden^",
        "war er bewusstlos.",
        "Und er hat ~überlebt.~"
      ],
      "chunkStarts": [
        26.873,
        27.837,
        29.023,
        30.141,
        31.661,
        32.971,
        34.222
      ]
    },
    {
      "id": "frage",
      "t0": 36.224,
      "t1": 37.608,
      "chunks": [
        "Würdest du ins All fliegen?"
      ],
      "noCap": true,
      "chunkStarts": [
        36.224
      ]
    },
    {
      "id": "komm",
      "t0": 37.998,
      "t1": 40.45,
      "chunks": [
        "Schreib A, B oder C in die Kommentare."
      ],
      "noCap": true,
      "chunkStarts": [
        37.998
      ]
    },
    {
      "id": "folg",
      "t0": 40.684,
      "t1": 43.633,
      "chunks": [
        "Und folg mir. Bevor dir die Luft ausgeht."
      ],
      "noCap": true,
      "chunkStarts": [
        40.684
      ]
    }
  ],
  "scenes": [
    {
      "id": "sc1",
      "at": "hook",
      "off": -0.3
    },
    {
      "id": "sc2",
      "at": "s1",
      "off": -0.2
    },
    {
      "id": "sc3",
      "at": "s5",
      "off": -0.2
    },
    {
      "id": "sc4",
      "at": "s10",
      "off": -0.2
    },
    {
      "id": "sc5",
      "at": "verrueckt",
      "off": -0.2
    },
    {
      "id": "sc6",
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
    "label": "BEWUSSTSEIN NOCH",
    "unit": "",
    "sub": "VAKUUM · OHNE HELM",
    "chipLabel": "SAUERSTOFF",
    "countdown": {
      "from": 15,
      "fmt": "s.mmm",
      "start": {
        "at": "s1",
        "off": -0.2
      },
      "end": {
        "at": "verrueckt",
        "off": -0.3
      }
    },
    "steps": [
      {
        "at": "s1",
        "off": -0.2,
        "value": 0,
        "chip": 100
      },
      {
        "at": "luft",
        "off": 1,
        "value": 0,
        "chip": 60
      },
      {
        "at": "s5",
        "off": 0,
        "value": 0,
        "chip": 40
      },
      {
        "at": "s10",
        "off": 0,
        "value": 0,
        "chip": 15
      },
      {
        "at": "haut",
        "off": 2.5,
        "value": 0,
        "chip": 0
      },
      {
        "at": "nasa",
        "off": 4.5,
        "value": 0,
        "chip": 100
      }
    ]
  },
  "interact": [
    {
      "type": "follow",
      "at": "kochen",
      "off": 0.4,
      "dur": 2.6,
      "text": "FOLG FÜR MEHR <span class='y'>SZENARIEN</span>"
    },
    {
      "type": "like",
      "at": "nasa",
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
      "text": "FOLG MIR – <span class='y'>ATME WEITER</span>"
    }
  ],
  "sfx": [
    {
      "type": "riser",
      "at": "hook",
      "off": 0
    },
    {
      "type": "glitch",
      "at": "luft",
      "off": 0
    },
    {
      "type": "heartbeat",
      "at": "s5",
      "off": 0,
      "dur": 4
    },
    {
      "type": "heartbeat",
      "at": "s10",
      "off": 0,
      "dur": 3
    },
    {
      "type": "ding",
      "at": "verrueckt",
      "off": 0
    },
    {
      "type": "rise",
      "at": "nasa",
      "off": 3.5,
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
      "off": 2.068
    }
  ]
};
