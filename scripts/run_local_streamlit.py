"""Run the SolidPrivacy Scrub Streamlit app on localhost.

This launcher mirrors the existing container startup patches, then starts the
current Streamlit app without changing app behavior, export semantics, or
reinsert semantics.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
APP_FILE = "presidio_streamlit.py"
STARTUP_PATCHES = (
    "fix_streamlit_nested_expanders.py",
    "fix_streamlit_pdf_text_reinsert.py",
)


def run_checked(command: list[str]) -> None:
    subprocess.run(command, cwd=REPO_ROOT, check=True)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Launch SolidPrivacy Scrub locally with Streamlit.",
    )
    parser.add_argument(
        "--address",
        default="127.0.0.1",
        help="Bind address for the local Streamlit server. Default: 127.0.0.1.",
    )
    parser.add_argument(
        "--port",
        default="8501",
        help="Port for the local Streamlit server. Default: 8501.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    for patch in STARTUP_PATCHES:
        run_checked([sys.executable, patch])

    streamlit_command = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        APP_FILE,
        "--server.address",
        args.address,
        "--server.port",
        str(args.port),
        "--server.headless",
        "true",
        "--browser.gatherUsageStats",
        "false",
    ]
    run_checked(streamlit_command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
