# Audio Transcription Module

This module implements the Audio Transcription stage of the Lightweight Audio–Subtitle Mismatch Flagging Tool.

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
```
## Requirements
Python 3.10+
FFmpeg installed and added to PATH

Install Python dependencies:

pip install -r requirements.txt

Verify FFmpeg installation:

ffmpeg -version

## Running the Module

Run the transcription pipeline using:

python audio_transcription/main.py --input audio_transcription/sample_input/sample.mp4 --model tiny

You can also use other Whisper models:

--model base
--model small

##Output

The module generates:

1. JSON Output
[
  {
    "start": 0.0,
    "end": 5.0,
    "text": "Hello, this is a testing video."
  }
]
2. SRT Subtitle Output
1
00:00:00,000 --> 00:00:05,000
Hello, this is a testing video.

## Technologies Used
Python
OpenAI Whisper
FFmpeg
## Current Limitations
-Accuracy depends on audio quality
-Whisper Tiny model may produce rough segment boundaries
-Currently optimized for short demo clips
## Future Improvements
-Add automatic language detection
-Add confidence scoring for segments
-Integrate with subtitle OCR module
-Connect with mismatch detection pipeline
