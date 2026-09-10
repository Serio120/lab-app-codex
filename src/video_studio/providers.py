"""Provider boundary for plugging in LLM, image/video, voice, and music APIs.

Keep API keys in the environment, never in a production manifest.  Concrete cloud
adapters should implement these protocols and persist their returned asset paths.
"""
from __future__ import annotations

from pathlib import Path
from typing import Protocol


class VisualProvider(Protocol):
    def create_clip(self, prompt: str, duration: float, output: Path) -> Path: ...


class VoiceProvider(Protocol):
    def synthesize(self, text: str, output: Path) -> Path: ...


class MusicProvider(Protocol):
    def search(self, mood: str, duration: float) -> Path | None: ...
