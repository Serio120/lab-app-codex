import json

from video_studio.pipeline import Studio


def test_create_production_has_requested_duration_and_word_captions(tmp_path):
    studio = Studio()
    production = studio.create("un plátano solitario encuentra un amigo", duration=60)
    assert production.duration_seconds == 60
    assert len(production.scenes) == 3
    assert production.word_cues[0].start == 0
    assert production.word_cues[-1].end == 60
    studio.write_captions(production, tmp_path / "captions.srt")
    assert "-->" in (tmp_path / "captions.srt").read_text()
    production.write(tmp_path)
    assert json.loads((tmp_path / "production.json").read_text())["title"]


def test_youtube_reference_is_retained():
    production = Studio().create("computación cuántica", reference_url="https://youtu.be/example")
    assert production.reference_style["source"] == "https://youtu.be/example"
