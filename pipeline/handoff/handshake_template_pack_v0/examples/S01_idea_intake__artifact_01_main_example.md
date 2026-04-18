# Idea Strategist — Main Output

## Executive summary
- Product: Windows Whisper transcriber with minimal-distraction UI
- Target user: neurodivergent knowledge workers who get overwhelmed by noisy UIs
- Primary value: fast local transcription + clean export

## Problem statement
Users need a **quiet, low-friction** way to transcribe audio locally on Windows without accounts, clutter, or complex settings.

## MVP scope (P0)
- Import audio file (mp3/wav/m4a)
- Choose language (auto / DE / EN)
- Transcribe locally
- Basic editor (minimal) + export to TXT/MD/SRT
- Progress + error states
- Simple settings: model size, output format, save location

## Out of scope (P1+)
- Cloud sync, accounts
- Team collaboration
- Advanced diarization
- Full DAW-style editing

## Constraints
- Windows-first
- Lightweight; minimal dependencies
- Privacy-first (local processing)
- ND-friendly defaults: low visual noise, predictable layout, minimal animations

## Decisions made
- MVP is single-user, offline-first.

## Open questions
- Best backend choice for speed/quality tradeoff on typical hardware?

## Risks
- CPU performance may hurt UX; mitigation: model selection + streaming progress.
