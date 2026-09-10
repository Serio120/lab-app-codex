from __future__ import annotations

from pathlib import Path
import re

from .models import Production, Scene, WordCue
from .reference import analyze_youtube_reference


class Studio:
    """Coordinates research, writing, asset direction, audio, captions, and render."""

    def create(self, brief: str, *, duration: int = 60, reference_url: str | None = None) -> Production:
        if not brief.strip():
            raise ValueError("brief cannot be empty")
        if duration < 3:
            raise ValueError("duration must be at least 3 seconds")
        style = analyze_youtube_reference(reference_url) if reference_url else {}
        topic = self._topic(brief)
        scene_count = 3
        scene_duration = duration / scene_count
        scenes = [
            Scene(1, scene_duration, f"Establishing shot for {topic}; original cinematic composition", f"Everything begins with a question. This is {topic}.", "curious ambient"),
            Scene(2, scene_duration, f"Character or central idea explores {topic}; clear visual storytelling", f"Step by step, the impossible becomes something we can understand.", "warm uplifting"),
            Scene(3, duration - scene_duration * 2, f"Hopeful final image about {topic}; original, memorable ending", f"And that is where the next story begins.", "inspiring resolution"),
        ]
        production = Production(brief=brief, title=f"A story about {topic}", scenes=scenes,
                                research=[f"Validate factual claims about {topic} before publishing."], reference_style=style)
        production.word_cues = self._word_cues(production)
        return production

    @staticmethod
    def _topic(brief: str) -> str:
        cleaned = re.sub(r"\s+", " ", brief).strip().rstrip(".!?")
        return cleaned[:90]

    @staticmethod
    def _word_cues(production: Production) -> list[WordCue]:
        words = re.findall(r"[^\s]+", production.narration)
        step = production.duration_seconds / max(1, len(words))
        return [WordCue(word, round(index * step, 3), round((index + 1) * step, 3)) for index, word in enumerate(words)]

    def write_captions(self, production: Production, path: Path) -> Path:
        def stamp(seconds: float) -> str:
            ms = round(seconds * 1000)
            h, ms = divmod(ms, 3_600_000); m, ms = divmod(ms, 60_000); s, ms = divmod(ms, 1_000)
            return f"{h:02}:{m:02}:{s:02},{ms:03}"
        path.write_text("\n\n".join(f"{i}\n{stamp(c.start)} --> {stamp(c.end)}\n{c.word}" for i, c in enumerate(production.word_cues, 1)), encoding="utf-8")
        return path
