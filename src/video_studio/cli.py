from __future__ import annotations

import argparse
from pathlib import Path

from .pipeline import Studio
from .render import render_preview, render_production


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an agent-directed video production package.")
    parser.add_argument("brief", help="Natural-language creative brief")
    parser.add_argument("--duration", type=int, default=60)
    parser.add_argument("--reference-url", help="YouTube reference used for high-level pacing guidance")
    parser.add_argument("--output", type=Path, default=Path("productions/latest"))
    parser.add_argument("--render-preview", action="store_true", help="Render an FFmpeg title-card preview")
    parser.add_argument("--generate-assets", action="store_true", help="Generate local storyboard, voice, and music assets")
    parser.add_argument("--render", action="store_true", help="Render generated assets into final.mp4 with FFmpeg")
    args = parser.parse_args()
    studio = Studio(); production = studio.create(args.brief, duration=args.duration, reference_url=args.reference_url)
    production.write(args.output); studio.write_captions(production, args.output / "captions.srt")
    if args.generate_assets or args.render:
        studio.generate_assets(production, args.output)
        production.write(args.output)
    if args.render:
        try:
            render_production(production, args.output)
        except RuntimeError as error:
            parser.error(str(error))
    if args.render_preview:
        render_preview(production, args.output / "preview.mp4")
    print(f"Created {args.output} ({production.duration_seconds:.0f}s, {len(production.scenes)} scenes)")


if __name__ == "__main__":
    main()
