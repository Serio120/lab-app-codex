from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
import json


@dataclass
class Scene:
    number: int
    duration_seconds: float
    visual_prompt: str
    narration: str
    music_mood: str


@dataclass
class WordCue:
    word: str
    start: float
    end: float


@dataclass
class Production:
    brief: str
    title: str
    scenes: list[Scene]
    research: list[str] = field(default_factory=list)
    reference_style: dict[str, str] = field(default_factory=dict)
    word_cues: list[WordCue] = field(default_factory=list)

    @property
    def narration(self) -> str:
        return " ".join(scene.narration for scene in self.scenes)

    @property
    def duration_seconds(self) -> float:
        return sum(scene.duration_seconds for scene in self.scenes)

    def write(self, directory: Path) -> Path:
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / "production.json"
        path.write_text(json.dumps(asdict(self), ensure_ascii=False, indent=2), encoding="utf-8")
        return path
