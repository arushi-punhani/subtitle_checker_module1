# Audio Transcription Module

This module implements the Audio Transcription stage of the Lightweight Audio–Subtitle Mismatch Flagging Tool for DMP 2026.

The pipeline accepts a video/audio file as input, extracts the audio track, and generates timestamped transcriptions using OpenAI Whisper. The generated outputs can later be used for subtitle comparison and mismatch detection.

---

## Features

- Accepts `.mp4` video input
- Automatically extracts audio using FFmpeg
- Generates timestamped transcriptions using Whisper
- Exports output in:
  - JSON format
  - SRT subtitle format
- Modular project structure for future pipeline integration

---

## Project Structure

```text
audio_transcription/
├── audio/
│   └── extractor.py
├── utils/
│   ├── formatter.py
│   └── writer.py
├── sample_input/
│   └── sample.mp4
├── output/
│   ├── transcript.json
│   └── transcript.srt
├── main.py
└── README.md
