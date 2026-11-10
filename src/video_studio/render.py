from __future__ import annotations

from pathlib import Path
import shutil
import subprocess

from .models import Production


def _escape_filter_path(path: Path) -> str:
    """Escape a path used inside a single-quoted FFmpeg filter option."""
    return str(path).replace("\\", "\\\\").replace(":", "\\:").replace("'", "'\\''")


def render_preview(production: Production, output: Path) -> Path:
    """Render a title-card smoke test, not a finished scene-based video."""
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("FFmpeg is required for rendering; install ffmpeg and retry")

    output.parent.mkdir(parents=True, exist_ok=True)
    title_file = output.with_name(f"{output.stem}.title.txt")
    title_file.write_text(production.title, encoding="utf-8")
    escaped_title_path = _escape_filter_path(title_file)

    command = [
        ffmpeg,
        "-y",
        "-f",
        "lavfi",
        "-i",
        f"color=c=1d3557:s=1280x720:d={production.duration_seconds}",
        "-vf",
        (
            f"drawtext=textfile='{escaped_title_path}':expansion=none:"
            "fontcolor=white:fontsize=42:x=(w-text_w)/2:y=(h-text_h)/2"
        ),
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(output),
    ]
    subprocess.run(command, check=True, capture_output=True, text=True)
    return output
