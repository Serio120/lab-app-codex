import json
from pathlib import Path

import pytest

from video_studio.pipeline import Studio
from video_studio.reference import analyze_youtube_reference
from video_studio.render import _escape_filter_path


def test_create_production_has_requested_duration_and_word_captions(tmp_path):
    studio = Studio()
    production = studio.create("un plátano solitario encuentra un amigo", duration=60)
    assert production.duration_seconds == 60
    assert len(production.scenes) == 3
    assert production.word_cues[0].start == 0
    assert production.word_cues[-1].end == 60

    captions_path = tmp_path / "nested" / "captions.srt"
    studio.write_captions(production, captions_path)
    assert "-->" in captions_path.read_text(encoding="utf-8")
    production.write(tmp_path)
    assert json.loads((tmp_path / "production.json").read_text(encoding="utf-8"))["title"]


def test_empty_brief_is_rejected():
    with pytest.raises(ValueError, match="brief"):
        Studio().create("   ")


def test_duration_below_minimum_is_rejected():
    with pytest.raises(ValueError, match="duration"):
        Studio().create("demo", duration=2)


@pytest.mark.parametrize(
    "url",
    [
        "https://example.com/video",
        "ftp://youtube.com/video",
        "https://youtube.com.evil.example/video",
        "https://user:password@youtube.com/video",
        "not a URL",
    ],
)
def test_invalid_reference_urls_are_rejected(url):
    with pytest.raises(ValueError, match="YouTube"):
        analyze_youtube_reference(url)


def test_youtube_reference_is_retained():
    url = "https://youtu.be/example"
    assert analyze_youtube_reference(url)["source"] == url


def test_ffmpeg_filter_path_escapes_colons_and_quotes():
    assert _escape_filter_path(Path("folder/it's:here.txt")) == "folder/it'\\''s\\:here.txt"
