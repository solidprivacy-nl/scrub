from __future__ import annotations

from pathlib import Path

from mvp_phase6_validation_manifest import load_validation_manifest
from mvp_phase6_validation_report import write_validation_report


MANIFEST = Path("test_cases/mvp_phase6/validation_manifest.json")
OUTPUT = Path("output/validation/mvp_phase6_synthetic_validation_report.json")


def main() -> None:
    manifest = load_validation_manifest(MANIFEST)
    report = write_validation_report(manifest, OUTPUT)
    print(
        f"Wrote {OUTPUT}: {report['case_count']} cases, "
        f"{report['failing_case_count']} failing, "
        f"{report['evidence_gap_count']} evidence gaps."
    )


if __name__ == "__main__":
    main()
