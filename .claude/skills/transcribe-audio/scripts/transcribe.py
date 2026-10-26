#!/usr/bin/env python3
"""Transcribe an audio/video file locally with faster-whisper.

Self-bootstrapping: on first run it creates a private venv under
~/.cache/transcribe-audio/venv, installs faster-whisper there, and re-executes
itself inside it. Nothing is added to the host project's dependencies.

  python3 transcribe.py recording.m4a                  # writes recording.txt
  python3 transcribe.py call.mp3 --model small --format srt
  python3 transcribe.py talk.wav --format json --language en --out -   # stdout
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

VENV = Path(os.environ.get("TRANSCRIBE_AUDIO_HOME", Path.home() / ".cache" / "transcribe-audio")) / "venv"


def bootstrap():
    """Re-run this script inside the private venv, creating it if needed."""
    py = VENV / "bin" / "python"
    if Path(sys.prefix).resolve() == VENV.resolve():
        return
    if not py.exists():
        print("First run: creating venv and installing faster-whisper...", file=sys.stderr)
        subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)
        subprocess.run([str(py), "-m", "pip", "install", "-q", "faster-whisper", "av>=14,<17"], check=True)  # av 17+ breaks faster-whisper's decode_audio
    os.execv(str(py), [str(py), *sys.argv])


def ts(seconds, sep):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def render(segments, info, fmt):
    if fmt == "txt":
        return "\n".join(s.text.strip() for s in segments) + "\n"
    if fmt == "srt":
        return "\n".join(
            f"{i}\n{ts(s.start, ',')} --> {ts(s.end, ',')}\n{s.text.strip()}\n"
            for i, s in enumerate(segments, 1))
    if fmt == "vtt":
        body = "\n".join(f"{ts(s.start, '.')} --> {ts(s.end, '.')}\n{s.text.strip()}\n" for s in segments)
        return "WEBVTT\n\n" + body
    return json.dumps({
        "language": info.language,
        "language_probability": round(info.language_probability, 3),
        "duration": round(info.duration, 2),
        "segments": [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in segments],
    }, indent=2) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio", help="audio or video file (mp3, wav, m4a, ogg, flac, mp4, webm, ...)")
    ap.add_argument("--model", default="small", help="tiny, base, small, medium, large-v3 (+ .en variants for English); default small")
    ap.add_argument("--format", choices=["txt", "srt", "vtt", "json"], default="txt")
    ap.add_argument("--language", help="language code such as en; omit to auto-detect")
    ap.add_argument("--out", help="output path, or - for stdout; default: next to the input with the new extension")
    ap.add_argument("--prompt", help="vocabulary hint, e.g. 'Oracle Fusion, work order, CMMS' to improve jargon accuracy")
    args = ap.parse_args()

    src = Path(args.audio)
    if not src.is_file():
        sys.exit(f"error: no such file: {src}")
    bootstrap()

    from faster_whisper import WhisperModel
    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    gen, info = model.transcribe(str(src), language=args.language, initial_prompt=args.prompt, vad_filter=True)
    segments = list(gen)
    text = render(segments, info, args.format)

    if args.out == "-":
        sys.stdout.write(text)
    else:
        out = Path(args.out) if args.out else src.with_suffix("." + args.format)
        out.write_text(text, encoding="utf-8")
        print(f"wrote {out} ({len(segments)} segments, {info.duration:.0f}s audio, language={info.language})", file=sys.stderr)


if __name__ == "__main__":
    main()
