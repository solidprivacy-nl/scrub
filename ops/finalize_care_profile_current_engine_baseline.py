from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 16:10 Europe/Amsterdam"
WP = "SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE"


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
    anchor = "The existing broad `NL_HEALTHCARE_REFERENCE` category must be assessed and split. Patient numbers, referral references, insurance identifiers and DBC/clinical codes do not share one safe default action."
    addition = anchor + "\n\nCurrent-engine baseline evidence is now recorded: 25 of 81 expected replace/review values were found as exact normalized spans, only 14 under the intended entity type, 11 were misclassified and 56 were missed. The bounded custom-rule baseline produced zero overlaps with the designated clinical preserve passages. Generic NER was excluded, so PERSON and e-mail results are not full-app measurements."
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("ROADMAP care baseline anchor not found")
        text = text.replace(anchor, addition, 1)
        write(path, text)


def update_workpackages() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; corrected current-engine evidence baseline implemented and validated.

Goal:
- Measure the unchanged deterministic Dutch custom recognizers against the eight-document synthetic care corpus before dedicated Zorgfilter recognizers are added.

Result:

```text
Expected replace/review values: 81
Exact normalized spans found: 25 (30.86%)
Correct intended entity type: 14 (17.28%)
Misclassified values: 11
Missed values: 56
Protected clinical phrase overlaps: 0
```

Key evidence:
- strong bounded coverage for addresses, BIG numbers, BSN, dates of birth and Dutch telephone numbers;
- no bounded custom-rule coverage for generic PERSON names, care-provider names, care organizations, exact care-event dates, care locations or room/bed references;
- review-selected layer: 4/42 spans found and 3/42 correctly classified;
- one AGB code collided with BSN recognition;
- broad existing healthcare/legal references find several values but do not express the approved care policy;
- generic NER was excluded and the baseline is not a full-app or production-readiness measurement.

Evidence:
- `CARE_PROFILE_CURRENT_ENGINE_BASELINE.md`
- `output/validation/care_profile_v1_current_engine_baseline.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_GAP_TRIAGE`

Boundaries:
- synthetic data only;
- no recognizer behavior, UI, threshold, export, Scrub Key or reinsert change;
- human review remains required;
- production readiness remains false.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; evidence baseline implemented and validated.

Purpose:
- Establish a corrected, reproducible pre-Zorgfilter measurement for the current deterministic Dutch custom recognizers.

Files added:
- `CARE_PROFILE_CURRENT_ENGINE_BASELINE.md`
- `care_profile_baseline_summary.py`
- `tests/test_care_profile_baseline_summary.py`
- `output/validation/care_profile_v1_current_engine_baseline.json`
- `workpackage_claims/scrub_wp_care_profile_current_engine_baseline.md`
- `handover/workpackages/20260803_1610_care_profile_current_engine_baseline.md`

Files changed:
- `care_profile_baseline.py`
- `scripts/generate_care_profile_baseline.py`
- `tests/test_care_profile_current_engine_baseline.py`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`

Implementation result:
- changed baseline matching from substring containment to exact normalized span equality;
- prevented false AGB coverage from an eight-digit prefix inside a longer BIG number;
- added compact policy/entity/case summaries;
- committed a reproducible JSON evidence artifact;
- documented 25/81 span recall, 14/81 correct-entity recall, 11 misclassifications, 56 misses and zero protected-clinical overlaps.

Validation:
- diagnostic run #1825 produced the evidence while 918 non-diagnostic tests passed;
- final clean GitHub Actions validation required after temporary diagnostics were removed;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- recognizer registration or behavior;
- current profile selector or UI;
- thresholds or entity defaults;
- review, export, Scrub Key and reinsert semantics;
- dependencies, runtime or cloud processing.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    text = read(path)
    anchor = "The current broad `NL_HEALTHCARE_REFERENCE` category is insufficient because it combines patient numbers, referral references, insurance identifiers and DBC/clinical codes under one behavior."
    addition = anchor + "\n\nCurrent bounded baseline evidence:\n\n- 25/81 expected replace/review values were found as exact spans;\n- 14/81 were found under the intended entity type;\n- 11 were misclassified and 56 missed;\n- only 4/42 review-selected values were found;\n- one AGB value collided with BSN recognition;\n- no designated clinical preserve phrase was overlapped by the current custom rules.\n\nGeneric NER was excluded, so the PERSON and e-mail findings do not represent complete live-app behavior. This evidence increases confidence that dedicated care patterns and review policy are necessary, but does not establish production quality."
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("RISK_REGISTER care baseline anchor not found")
        text = text.replace(anchor, addition, 1)
        write(path, text)


def update_claim() -> None:
    path = "workpackage_claims/scrub_wp_care_profile_current_engine_baseline.md"
    text = read(path)
    if "Status: in_progress" in text:
        write(path, text.replace("Status: in_progress", "Status: completed", 1))


def main() -> None:
    update_roadmap()
    update_workpackages()
    update_changelog()
    update_risk_register()
    update_claim()

    Path("ops/finalize_care_profile_current_engine_baseline.py").unlink(missing_ok=True)
    Path(".github/workflows/finalize-care-profile-current-engine-baseline.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
