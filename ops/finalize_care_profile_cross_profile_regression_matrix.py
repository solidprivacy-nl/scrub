from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 18:58 Europe/Amsterdam"
WP = "SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX"


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    current = read(path)
    if marker not in current:
        write(path, block.rstrip() + "\n\n" + current)


def update_roadmap() -> None:
    path = "ROADMAP.md"
    text = read(path)
    anchor = (
        "The current Streamlit integration is now implemented and regression-green. "
        "`Zorgcontrole — streng` is added without silently becoming the default; the existing "
        "Legal profile remains initially selected. Sixteen care recognizers, central entity "
        "composition, exact-span precedence, eight synthetic examples and conservative unchecked "
        "care candidates are wired into the current flow. Review-selected care detections remain "
        "selected but show `Controle nodig`. Export, Scrub Key and reinsert semantics are unchanged. "
        "The next gates are cross-profile regression, deployment sync and live app verification."
    )
    addition = anchor + (
        "\n\nThe deterministic cross-profile regression matrix is now green. Across eight care "
        "document families and twelve legal examples, Care and International retain all 108 "
        "dedicated care expectations, Care/International and Legal/International dedicated-type "
        "parity hold, no dedicated Care or Legal entities leak into the wrong profiles, and no "
        "protected clinical phrase is overlapped. The historical legal metadata remains visible as "
        "132/148 deterministic expectations, sixteen recorded gaps and four negative observations; "
        "these are existing benchmark observations, not hidden or reclassified as Zorg success. "
        "Generic NER remains outside this matrix. The next gate is deployed app verification after "
        "GitHub-to-Hugging-Face sync is confirmed."
    )
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("ROADMAP cross-profile anchor not found")
        write(path, text.replace(anchor, addition, 1))


def update_workpackages() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; deterministic cross-profile gates are green.

Goal:
- Verify that Zorgfilter adds care-specific recognition without contaminating Legal or General profiles or masking protected clinical meaning.

Result:

```text
Profiles evaluated: 4
Care document families: 8
Legal examples: 12
Dedicated Care expectations: 108/108
Hard profile failures: 0
Protected clinical overlaps: 0
Care/International parity: passed
Legal/International parity: passed
Historical legal metadata: 132/148
Recorded historical gaps: 16
Recorded negative observations: 4
Final validated run #1899: 995 tests passed
Generic NER evaluated: false
Production ready: false
```

Evidence:
- `CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX.md`
- `output/validation/care_profile_cross_profile_matrix.json`
- `handover/workpackages/20260803_1858_care_profile_cross_profile_regression_matrix.md`

Active next package:
- `SCRUB-WP_CARE_PROFILE_APP_VERIFY`

Gate status:
- app verification is blocked until GitHub-to-Hugging-Face sync for the merged UI integration is independently confirmed.

Boundaries:
- pure helper/test/evidence package only;
- no Streamlit, review, export, Scrub Key or reinsert change;
- generic NER is model-dependent and deferred to deployed-app observation;
- synthetic data only;
- human review remains required;
- no production-readiness claim.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed and regression-green.

Purpose:
- Add deterministic evidence that the new Care profile remains isolated from Legal and General profiles and preserves clinical meaning.

Files added:
- `care_profile_cross_profile_matrix.py`
- `CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX.md`
- `tests/test_care_profile_cross_profile_matrix.py`
- `output/validation/care_profile_cross_profile_matrix.json`
- `workpackage_claims/scrub_wp_care_profile_cross_profile_regression_matrix.md`
- `handover/workpackages/20260803_1858_care_profile_cross_profile_regression_matrix.md`

Implementation result:
- executed real deterministic Dutch custom recognizers across four configured profiles;
- covered eight care-document families and twelve legal examples;
- verified 108/108 dedicated Care expectations across Care and International;
- verified Care/International and Legal/International dedicated-type parity;
- verified no dedicated Care/Legal leakage into the wrong profiles;
- verified zero overlap with protected clinical phrases;
- separated hard profile gates from historical legal metadata observations;
- preserved sixteen historical legal metadata gaps and four negative observations in the evidence snapshot;
- added snapshot reproducibility checks for all twenty observations.

Validation:
- run #1887 exposed an invalid hard-contract assumption for historical legal metadata;
- run #1888 made all twenty observations explicit;
- run #1890 passed after correcting the methodology: 994 tests;
- run #1897 exposed only an incorrect legal-example count in the snapshot;
- run #1899 passed: 995 tests in 9.56s;
- final clean run pending after governance finalization.

Intentionally not changed:
- current Streamlit UI or profile selector;
- review table, export, Scrub Key or reinsert semantics;
- runtime dependencies, cloud processing or production claims;
- generic NER behavior.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    text = read(path)
    anchor = (
        "The current Streamlit integration now registers the sixteen care recognizers and applies "
        "the central profile policy. Review-selected care detections are selected by default but "
        "visibly marked `Controle nodig`; unresolved strongly labelled references remain unchecked "
        "candidates. Regression run #1877 passed 983 tests and existing export, Scrub Key and "
        "reinsert behavior remains unchanged. Risk R10 remains mitigating because cross-profile "
        "regression, deployment sync, generic-NER observation and live app verification are still pending."
    )
    addition = anchor + (
        "\n\nThe deterministic cross-profile matrix now passes all hard gates: 108/108 dedicated "
        "Care expectations are retained across Care and International, no dedicated Care or Legal "
        "entities leak into the wrong profiles, dedicated-type parity holds, and no protected "
        "clinical phrase is overlapped. Historical legal metadata remains explicitly recorded as "
        "132/148 deterministic expectations, sixteen gaps and four negative observations. Risk R10 "
        "remains mitigating because GitHub-to-Hugging-Face deployment sync, generic-NER behavior and "
        "live app verification are still unconfirmed."
    )
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("RISK_REGISTER cross-profile anchor not found")
        write(path, text.replace(anchor, addition, 1))


def update_claim() -> None:
    path = "workpackage_claims/scrub_wp_care_profile_cross_profile_regression_matrix.md"
    text = read(path)
    if "Status: in_progress" in text:
        text = text.replace("Status: in_progress", "Status: completed", 1)
    write(path, text)


def main() -> None:
    update_roadmap()
    update_workpackages()
    update_changelog()
    update_risk_register()
    update_claim()

    Path("ops/finalize_care_profile_cross_profile_regression_matrix.py").unlink(missing_ok=True)
    Path(".github/workflows/finalize-care-profile-cross-profile-regression-matrix.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
