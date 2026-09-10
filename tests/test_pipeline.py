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


def test_local_asset_generation_writes_a_reproducible_manifest(tmp_path):
    studio = Studio()
    production = studio.create("un anuncio sobre energía limpia", duration=6)
    assets = studio.generate_assets(production, tmp_path)
    assert len(assets) == 5
    assert all((tmp_path / "assets.json").exists() for _ in assets)
    assert all(not asset.path.startswith("/") for asset in assets)
    assert (tmp_path / "assets" / "scene-01.svg").exists()
    assert (tmp_path / "assets" / "voice.wav").exists()
    assert (tmp_path / "assets" / "music.wav").exists()
