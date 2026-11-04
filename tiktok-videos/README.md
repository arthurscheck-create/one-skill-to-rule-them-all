# TikTok-Videos (HyperFrames)

Deutsche TikTok-Videos komplett im Code. Anleitung: `.claude/skills/tiktok-video/SKILL.md`.

    tools/new_video.sh 02-thema "Titel"                       # neues Projekt
    python3 tools/add_voice.py videos/02-thema voice.wav --min-duration 50 --fit 50
    tools/render.sh videos/02-thema                           # → output/02-thema.mp4

Voraussetzungen: Node ≥ 22, FFmpeg, Python 3 + numpy, `npm i` (hyperframes@0.9.11, gsap).
