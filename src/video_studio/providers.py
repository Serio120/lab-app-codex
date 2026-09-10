"""Provider boundary for plugging in LLM, image/video, voice, and music APIs.

Keep API keys in the environment, never in a production manifest.  Concrete cloud
adapters should implement these protocols and persist their returned asset paths.
"""
from __future__ import annotations

from pathlib import Path
from typing import Protocol
import math
import wave


class VisualProvider(Protocol):
    def create_clip(self, prompt: str, duration: float, output: Path) -> Path: ...


class VoiceProvider(Protocol):
    def synthesize(self, text: str, output: Path) -> Path: ...


class MusicProvider(Protocol):
    def search(self, mood: str, duration: float, output: Path) -> Path | None: ...


class LocalVisualProvider:
    """Creates original SVG storyboards for offline demos and automated tests."""
    name = "local-svg"

    def create_clip(self, prompt: str, duration: float, output: Path) -> Path:
        output.parent.mkdir(parents=True, exist_ok=True)
        safe = _xml_escape(prompt[:120])
        output.write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720">'
            '<rect width="100%" height="100%" fill="#172554"/>'
            '<circle cx="640" cy="270" r="120" fill="#fbbf24"/>'
            f'<text x="640" y="500" text-anchor="middle" fill="white" font-size="30">{safe}</text>'
            f'<text x="640" y="550" text-anchor="middle" fill="#bfdbfe" font-size="20">{duration:.1f} seconds</text></svg>',
            encoding="utf-8",
        )
        return output


class LocalVoiceProvider:
    """Writes a quiet tone WAV with deterministic duration; replace with cloud TTS."""
    name = "local-tone-voice"

    def synthesize(self, text: str, output: Path) -> Path:
        duration = max(1.0, len(text.split()) / 2.5)
        return _tone(output, duration, frequency=220, amplitude=350)


class LocalMusicProvider:
    """Writes a low-volume original tone bed; never represents it as licensed music."""
    name = "local-tone-music"

    def search(self, mood: str, duration: float, output: Path) -> Path | None:
        return _tone(output, duration, frequency=110, amplitude=120)


def _tone(output: Path, duration: float, *, frequency: float, amplitude: int) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    sample_rate = 8_000
    frames = int(sample_rate * duration)
    with wave.open(str(output), "w") as audio:
        audio.setparams((1, 2, sample_rate, frames, "NONE", "not compressed"))
        payload = b"".join(int(amplitude * math.sin(2 * math.pi * frequency * index / sample_rate)).to_bytes(2, "little", signed=True) for index in range(frames))
        audio.writeframes(payload)
    return output


def _xml_escape(value: str) -> str:
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
