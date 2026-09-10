from __future__ import annotations

from pathlib import Path
import shutil
import subprocess

from .models import Production


def build_render_command(production: Production, directory: Path, output: Path) -> list[str]:
    """Build the FFmpeg command that turns a production package into an MP4.

    The function is side-effect free so the complete assembly can be tested on
    machines without FFmpeg. Visual assets are held for their scene duration;
    voice is mixed with a quieter looping music bed and word captions are burned
    into the resulting video.
    """
    visuals = sorted((asset for asset in production.assets if asset.kind == "visual"), key=lambda asset: asset.scene_number or 0)
    voice = next((asset for asset in production.assets if asset.kind == "voice"), None)
    music = next((asset for asset in production.assets if asset.kind == "music"), None)
    if len(visuals) != len(production.scenes) or not voice or not music:
        raise ValueError("render requires one visual per scene plus voice and music assets")

    ffmpeg = shutil.which("ffmpeg") or "ffmpeg"
    command = [ffmpeg, "-y"]
    for scene, asset in zip(production.scenes, visuals, strict=True):
        command.extend(["-loop", "1", "-t", str(scene.duration_seconds), "-i", str(directory / asset.path)])
    command.extend(["-i", str(directory / voice.path), "-stream_loop", "-1", "-i", str(directory / music.path)])

    video_labels = "".join(f"[{index}:v]" for index in range(len(visuals)))
    voice_index = len(visuals)
    music_index = voice_index + 1
    captions = directory / "captions.srt"
    caption_path = str(captions).replace("\\", "\\\\").replace(":", "\\:").replace("'", r"\'")
    filters = [
        f"{video_labels}concat=n={len(visuals)}:v=1:a=0[video]",
        f"[video]subtitles='{caption_path}'[vout]",
        f"[{voice_index}:a]volume=1.0[voice]",
        f"[{music_index}:a]volume=0.16[music]",
        "[voice][music]amix=inputs=2:duration=first:dropout_transition=0[aout]",
    ]
    command.extend(["-filter_complex", ";".join(filters), "-map", "[vout]", "-map", "[aout]", "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(output)])
    return command


def render_production(production: Production, directory: Path, output: Path | None = None) -> Path:
    """Render all generated assets into a captioned, shareable MP4."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError("FFmpeg is required for rendering; install ffmpeg and retry")
    output = output or directory / "final.mp4"
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(build_render_command(production, directory, output), check=True, capture_output=True, text=True)
    return output


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
