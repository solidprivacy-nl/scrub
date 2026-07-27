from __future__ import annotations

import json
from pathlib import Path

from mvp_scrub_key_roundtrip_validation import run_roundtrip_validation


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/validation/mvp_scrub_key_roundtrip_validation_report.json"


def main() -> int:
    report = run_roundtrip_validation()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "case_count": report["case_count"],
                "failed_case_count": report["failed_case_count"],
                "finding_count": report["finding_count"],
                "critical_finding_count": report["critical_finding_count"],
                "next_workpackage": report["next_workpackage"],
            },
            sort_keys=True,
        )
    )
    return 0 if report["validation_complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
