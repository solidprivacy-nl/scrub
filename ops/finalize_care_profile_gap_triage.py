from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 16:25 Europe/Amsterdam"
WP = "SCRUB-WP_CARE_PROFILE_GAP_TRIAGE"


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    current = read(path)
    if marker not in current:
        write(path, block.rstrip() + "\n\n" + current)


def update_workpackages() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; all current care-corpus expectations classified.

Goal:
- Route every correct, missed or misclassified baseline value to a concrete follow-up mechanism before recognizer implementation.

Result:

```text
Expectations classified: 81/81
Reuse current recognizer: 14
Generic profile dependency: 13
Contextual care review recognizer: 36
Care-specific reclassification: 10
Dedicated care reference recognizer: 5
Care collision guard: 3
Unclassified: 0
```

Key decisions:
- keep address, BIG, BSN, date-of-birth and Dutch-phone recognizers;
- keep generic PERSON and e-mail in the generic local profile layer;
- split broad healthcare/legal references into care-specific policy entities;
- build a context-bound review layer for providers, organizations, locations, room/bed and care-event dates;
- require explicit AGB/BSN precedence and negative medical-number contracts;
- keep diagnosis, medication, dosages, lab values, observations and roles under preservation guards.

Evidence:
- `CARE_PROFILE_GAP_TRIAGE.md`
- `output/validation/care_profile_v1_gap_triage.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS`

Boundaries:
- no recognizer or UI implementation;
- no threshold, export, Scrub Key or reinsert change;
- synthetic data only;
- human review remains required;
- production readiness remains false.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; evidence-driven gap routing implemented.

Purpose:
- Convert the current-engine care baseline into explicit recognizer, profile and collision-prevention contract routes.

Files added:
- `CARE_PROFILE_GAP_TRIAGE.md`
- `care_profile_gap_triage.py`
- `care_profile_gap_triage_summary.py`
- `tests/test_care_profile_gap_triage.py`
- `scripts/generate_care_profile_gap_triage.py`
- `output/validation/care_profile_v1_gap_triage.json`
- `workpackage_claims/scrub_wp_care_profile_gap_triage.md`
- `handover/workpackages/20260803_1625_care_profile_gap_triage.md`

Implementation result:
- classified all 81 expectations with zero unclassified values;
- froze six implementation routes and five contract families;
- separated generic NER dependencies from care-specific rule work;
- routed ten broad-entity matches to care-specific reclassification;
- routed 36 context-dependent values to review-selected recognition;
- made AGB/BSN and medical-number collision guards mandatory;
- preserved clinical-content negative contracts as a first-class requirement.

Validation:
- GitHub Actions pending final PR validation;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- recognizer implementation or registration;
- profile selector, thresholds or entity defaults;
- review, export, Scrub Key or reinsert semantics;
- runtime, dependencies or cloud processing.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    text = read(path)
    anchor = "Generic NER was excluded, so the PERSON and e-mail findings do not represent complete live-app behavior. This evidence increases confidence that dedicated care patterns and review policy are necessary, but does not establish production quality."
    addition = anchor + "\n\nGap triage classified all 81 expectations. The largest unresolved family is contextual review recognition (36 values), followed by generic profile dependencies (13), care-specific reclassification (10), dedicated care references (5) and AGB/numeric collision guards (3). The recognizer contract package must freeze these routes before any care pattern implementation."
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("RISK_REGISTER gap-triage anchor not found")
        text = text.replace(anchor, addition, 1)
        write(path, text)


def update_claim() -> None:
    path = "workpackage_claims/scrub_wp_care_profile_gap_triage.md"
    text = read(path)
    if "Status: in_progress" in text:
        write(path, text.replace("Status: in_progress", "Status: completed", 1))


def main() -> None:
    update_workpackages()
    update_changelog()
    update_risk_register()
    update_claim()

    Path("ops/finalize_care_profile_gap_triage.py").unlink(missing_ok=True)
    Path(".github/workflows/finalize-care-profile-gap-triage.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
