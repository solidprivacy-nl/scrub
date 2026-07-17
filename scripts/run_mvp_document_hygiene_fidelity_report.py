from __future__ import annotations

import json
from pathlib import Path

from mvp_document_fidelity_report import write_document_fidelity_report
from mvp_phase6_validation_manifest import load_validation_manifest


MANIFEST = Path("test_cases/mvp_phase6/validation_manifest.json")
BASELINE = Path("output/validation/mvp_phase6_synthetic_validation_report.json")
TRIAGE = Path("output/validation/mvp_phase6_false_negative_gap_triage.json")
OUTPUT = Path(
    "output/validation/mvp_phase6_document_hygiene_fidelity_hardening_report.json"
)


def _json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    report = write_document_fidelity_report(
        load_validation_manifest(MANIFEST),
        _json(BASELINE),
        _json(TRIAGE),
        OUTPUT,
    )
    print(
        f"Wrote {OUTPUT}: resolved={report['resolved_finding_count']}, "
        f"remaining={report['remaining_finding_count']}."
    )


if __name__ == "__main__":
    main()
