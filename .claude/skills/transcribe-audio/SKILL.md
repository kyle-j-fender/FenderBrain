---
name: transcribe-audio
description: Transcribe audio or video recordings to text locally with Whisper (faster-whisper) — nothing is uploaded anywhere. Use whenever the user wants to transcribe, caption, or get notes from a recording (meeting, voice memo, call, interview, lecture), mentions an mp3/wav/m4a/ogg/flac/mp4/webm file, asks for subtitles (SRT/VTT), or asks "can Claude listen to / transcribe this audio". Claude itself cannot read audio files, so use this even if they don't say "Whisper".
---

# Transcribe audio

Claude can't ingest audio directly, so this skill converts the recording to text with a local Whisper model; afterwards Claude can summarize, extract action items, or file the text wherever the project needs it. Everything runs on this machine, which matters because recordings are often sensitive. Only the model weights are downloaded (once, from Hugging Face).

## Workflow

1. Confirm the file path (ask if missing). Check it exists; video files work too.
2. Pick a model — the main speed/accuracy lever:
   - `tiny.en` / `base.en`: fast, rough; fine for clear English and quick checks.
   - `small` (default): good balance on CPU.
   - `medium` / `large-v3`: best accuracy for accents, noise, or jargon; several times slower on CPU. Warn the user before running these on long files.
3. Run the bundled script (it creates its own private venv on first run, so it doesn't touch the project's dependencies):

   ```bash
   python3 <skill-dir>/scripts/transcribe.py <audio> [--model small] [--format txt|srt|vtt|json] [--language en] [--prompt "domain terms"] [--out PATH|-]
   ```

   - Use `--format srt`/`vtt` when timestamps or subtitles are wanted, `json` when you need segments to process.
   - Pass `--prompt` with project vocabulary (product names, acronyms) — Whisper spells these far better when primed.
   - Long files take a while; run in the background and report when done.
4. Read the output and give the user what they asked for (transcript, summary, action items). Whisper can mishear names and numbers and doesn't label speakers — say so when it matters, and flag low-confidence passages rather than silently fixing them.
5. Save the transcript where the project expects it. Don't commit recordings or transcripts of private conversations unless the user asks.

## Notes

- First run needs network access to PyPI and Hugging Face. If those are blocked, say so rather than retrying.
- No GPU is assumed (`int8` on CPU). Override the cache location with `TRANSCRIBE_AUDIO_HOME`.
- No speaker diarization here; if the user needs "who said what", suggest a hosted service or pyannote and explain the tradeoff.
