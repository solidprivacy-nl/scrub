#!/usr/bin/env python3
"""Generate the compact machine-readable Zorgfilter gap triage summary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from care_profile_gap_triage_summary import build_care_profile_gap_triage_summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="output/validation/care_profile_v1_gap_triage.json",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            build_care_profile_gap_triage_summary(),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
