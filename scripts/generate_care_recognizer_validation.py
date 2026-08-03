#!/usr/bin/env python3
"""Generate the machine-readable Zorgfilter recognizer validation report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from care_recognizer_validation import build_care_recognizer_validation


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="output/validation/care_recognizer_implementation_validation.json",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(build_care_recognizer_validation(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
