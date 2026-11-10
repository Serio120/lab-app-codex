from __future__ import annotations

from urllib.parse import urlparse


ALLOWED_HOSTS = {"youtube.com", "www.youtube.com", "youtu.be"}


def analyze_youtube_reference(url: str) -> dict[str, str]:
    """Validate a YouTube URL and retain it as an editorial reference only.

    This function does not fetch, inspect, download, or analyze the video.
    """
    parsed = urlparse(url)
    try:
        hostname = parsed.hostname
    except ValueError:
        hostname = None

    if (
        parsed.scheme not in {"http", "https"}
        or hostname not in ALLOWED_HOSTS
        or parsed.username is not None
        or parsed.password is not None
    ):
        raise ValueError("reference URL must be an HTTP(S) YouTube link")

    return {
        "source": url,
        "guidance": (
            "Use only high-level editorial guidance supplied by the user; "
            "create original assets, script, and sound."
        ),
        "suggested_pacing": "dynamic three-act pacing",
    }
