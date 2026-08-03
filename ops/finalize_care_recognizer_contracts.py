from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 16:34 Europe/Amsterdam"
WP = "SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS"


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

Status: completed; recognizer contract frozen before implementation.

Goal:
- Freeze exact positive, value-only, policy, collision and clinical-preservation behavior for the dedicated Zorgfilter recognizer module.

Contract result:

```text
Dedicated care entities: 16
Positive exact-span cases: 37
- care-reference/collision cases: 17
- contextual review cases: 20
Negative/collision/preservation cases: 16
Future module: dutch_care_recognizers.py
Public API: get_dutch_care_entity_names, get_dutch_care_recognizers
```

Frozen boundaries:
- generic PERSON and e-mail stay in the generic profile layer;
- care providers, organizations, locations, room/bed and care-event dates use context-bound review recognition;
- AGB requires strong context and must not become BSN;
- labels and professional roles remain readable;
- vital signs, medication, dosages, administration times, lab values, DBC/ICD codes and clinical meaning remain preserved;
- no app registration or UI integration in this package.

Evidence:
- `CARE_RECOGNIZER_CONTRACT_V1.md`
- `output/validation/care_recognizer_contract_v1_summary.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION`

Production readiness: false. Human review remains required.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; test/specification contract frozen.

Purpose:
- Define dedicated Zorgfilter recognizer behavior before writing implementation code.

Files added:
- `CARE_RECOGNIZER_CONTRACT_V1.md`
- `care_recognizer_contracts.py`
- `care_recognizer_contract_summary.py`
- `tests/test_care_recognizer_contracts.py`
- `scripts/generate_care_recognizer_contract_summary.py`
- `output/validation/care_recognizer_contract_v1_summary.json`
- `workpackage_claims/scrub_wp_care_profile_recognizer_contract_tests.md`
- `handover/workpackages/20260803_1634_care_profile_recognizer_contract_tests.md`

Implementation result:
- froze sixteen dedicated care entities and the future pure helper API;
- added 37 positive exact-span fixtures;
- added 16 negative/collision/clinical-preservation fixtures;
- froze replace/review-selected policy alignment;
- froze care-event/date-of-birth and AGB/BSN precedence;
- kept generic PERSON/e-mail outside the dedicated care module.

Validation:
- GitHub Actions pending final PR validation;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- recognizer implementation or registration;
- current profile selector, thresholds or entity defaults;
- review, export, Scrub Key and reinsert semantics;
- runtime, dependencies or cloud processing.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    text = read(path)
    anchor = "Gap triage classified all 81 expectations. The largest unresolved family is contextual review recognition (36 values), followed by generic profile dependencies (13), care-specific reclassification (10), dedicated care references (5) and AGB/numeric collision guards (3). The recognizer contract package must freeze these routes before any care pattern implementation."
    addition = anchor + "\n\nThe recognizer contract is now frozen with sixteen dedicated entities, 37 positive exact-span cases and 16 negative/collision/preservation cases. Implementation must pass these fixtures before any app registration or UI promotion."
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("RISK_REGISTER contract anchor not found")
        text = text.replace(anchor, addition, 1)
        write(path, text)


def update_claim() -> None:
    path = "workpackage_claims/scrub_wp_care_profile_recognizer_contract_tests.md"
    text = read(path)
    if "Status: in_progress" in text:
        write(path, text.replace("Status: in_progress", "Status: completed", 1))


def main() -> None:
    update_workpackages()
    update_changelog()
    update_risk_register()
    update_claim()

    Path("ops/finalize_care_recognizer_contracts.py").unlink(missing_ok=True)
    Path(".github/workflows/finalize-care-recognizer-contracts.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
