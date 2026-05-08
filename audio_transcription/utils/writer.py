import json
from utils.formatter import format_timestamp

def save_json(segments, output_path):
    data = []
    for seg in segments:
        data.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip()
        })
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def save_srt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            start = format_timestamp(seg["start"])
            end = format_timestamp(seg["end"])
            text = seg["text"].strip()

            f.write(f"{i}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")