import os
import argparse
import whisper

from audio.extractor import extract_audio
from utils.writer import save_json, save_srt

def main():
    parser = argparse.ArgumentParser(description="Audio Transcription using Whisper")
    parser.add_argument("--input", required=True, help="Input video/audio file")
    parser.add_argument("--model", default="base", help="tiny, base, small")
    parser.add_argument("--language", default=None, help="Language code (hi, en)")
    parser.add_argument("--output_dir", default="output")

    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    input_file = args.input

    # Step 1: Extract audio if video
    if input_file.endswith(".mp4"):
        print("Extracting audio...")
        audio_path = extract_audio(input_file)
    else:
        audio_path = input_file

    # Step 2: Load model
    print(f"Loading model: {args.model}")
    model = whisper.load_model(args.model)

    # Step 3: Transcribe
    print("Transcribing...")
    result = model.transcribe(audio_path, language=args.language)
    segments = result["segments"]

    # Step 4: Save outputs
    json_path = os.path.join(args.output_dir, "transcript.json")
    srt_path = os.path.join(args.output_dir, "transcript.srt")

    save_json(segments, json_path)
    save_srt(segments, srt_path)

    print("\n✅ Done!")
    print(f"Saved: {json_path}")
    print(f"Saved: {srt_path}")

if __name__ == "__main__":
    main()