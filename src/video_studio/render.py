from __future__ import annotations

from pathlib import Path
import shutil
import subprocess

from .models import Production


def render_preview(production: Production, output: Path) -> Path:
    """Render a no-API preview. Replace color inputs with provider clips in production."""
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("FFmpeg is required for rendering; install ffmpeg and retry")
    output.parent.mkdir(parents=True, exist_ok=True)
    # A transparent, inspectable fallback: proves the assembly path without claiming AI assets exist.
    command = [ffmpeg, "-y", "-f", "lavfi", "-i", f"color=c=1d3557:s=1280x720:d={production.duration_seconds}",
               "-vf", f"drawtext=text='{production.title.replace(':', '')}':fontcolor=white:fontsize=42:x=(w-text_w)/2:y=(h-text_h)/2",
               "-c:v", "libx264", "-pix_fmt", "yuv420p", str(output)]
    subprocess.run(command, check=True, capture_output=True, text=True)
    return output
