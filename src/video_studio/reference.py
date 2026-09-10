from __future__ import annotations

from urllib.parse import urlparse


def analyze_youtube_reference(url: str) -> dict[str, str]:
    """Return safe, high-level creative signals from a YouTube URL.

    Downloading or copying the source audiovisual work is deliberately out of
    scope. An optional yt-dlp integration can later enrich this with public
    metadata and user-supplied notes.
    """
    parsed = urlparse(url)
    if parsed.netloc not in {"youtube.com", "www.youtube.com", "youtu.be"}:
        raise ValueError("reference URL must be a YouTube link")
    return {
        "source": url,
        "guidance": "Use only high-level pacing and editorial observations; create original assets, script, and sound.",
        "suggested_pacing": "dynamic three-act pacing",
    }
