from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 16:52 Europe/Amsterdam"
WP = "SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION"


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
    anchor = "Current-engine baseline evidence is now recorded: 25 of 81 expected replace/review values were found as exact normalized spans, only 14 under the intended entity type, 11 were misclassified and 56 were missed. The bounded custom-rule baseline produced zero overlaps with the designated clinical preserve passages. Generic NER was excluded, so PERSON and e-mail results are not full-app measurements."
    addition = anchor + "\n\nThe dedicated pure recognizer implementation is now green but remains unregistered: sixteen care entities pass 37/37 positive contracts, 16/16 negative/collision contracts and all 54 dedicated expectations in the eight-document corpus, with zero protected-clinical overlaps. The next gate is central profile composition and AGB/BSN precedence before any visible Zorg profile is added."
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("ROADMAP recognizer implementation anchor not found")
        text = text.replace(anchor, addition, 1)
        write(path, text)


def update_workpackages() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; pure recognizers implemented and contract-validated, app registration still closed.

Goal:
- Implement the frozen sixteen-entity Zorgfilter recognizer module without changing current app behavior.

Result:

```text
Dedicated entities: 16
Positive contracts: 37/37 passed
Forbidden positive collisions: 0
Negative/collision contracts: 16/16 passed
Dedicated corpus expectations: 54/54 passed
Protected clinical phrase overlaps: 0
Full regression run #1854: 953 tests passed
App registration: false
```

Implementation:
- `dutch_care_recognizers.py` with value-only Presidio capture results;
- strong-context administrative references and AGB;
- provider-name recognition preserving professional roles;
- labeled organizations and bounded locations;
- room/bed/apartment references;
- care-event dates separated from date of birth;
- no Streamlit, network, AI, cloud or file-write behavior.

Evidence:
- `CARE_RECOGNIZER_IMPLEMENTATION_V1.md`
- `output/validation/care_recognizer_implementation_validation.json`

Active next package:
- `SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR`

Boundaries:
- recognizers are not registered in `presidio_helpers.py` or the UI;
- generic PERSON/e-mail remain generic-profile dependencies;
- AGB/BSN profile-level precedence remains to be validated;
- no export, Scrub Key or reinsert change;
- human review remains required;
- production readiness remains false.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; pure recognizer implementation validated.

Purpose:
- Implement the frozen Zorgfilter recognizer contract without registering it in the current app.

Files added:
- `dutch_care_recognizers.py`
- `care_recognizer_validation.py`
- `CARE_RECOGNIZER_IMPLEMENTATION_V1.md`
- `scripts/generate_care_recognizer_validation.py`
- `tests/test_dutch_care_recognizers.py`
- `tests/test_care_recognizer_validation.py`
- `output/validation/care_recognizer_implementation_validation.json`
- `workpackage_claims/scrub_wp_care_profile_recognizer_implementation.md`
- `handover/workpackages/20260803_1652_care_profile_recognizer_implementation.md`

Implementation result:
- implemented sixteen dedicated, context-bound care entities;
- returned exact value-only Presidio spans with explanations and metadata;
- corrected bounded variants for Dutch client labels, prescription numbers, generic incident labels and lowercase residential-care organization labels;
- passed all frozen positive and negative contracts;
- covered all 54 dedicated corpus expectations with zero protected-clinical overlaps;
- kept app registration explicitly false.

Validation:
- initial run #1850 exposed five bounded missing context variants and no clinical-overmasking failure;
- corrected GitHub Actions run #1854 passed: 953 tests;
- final clean validation pending after governance finalization;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- `presidio_helpers.py`, `presidio_streamlit.py` or current profile behavior;
- thresholds, entity defaults or generic NER;
- review, export, Scrub Key or reinsert semantics;
- runtime, dependencies or cloud processing.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    text = read(path)
    anchor = "The recognizer contract is now frozen with sixteen dedicated entities, 37 positive exact-span cases and 16 negative/collision/preservation cases. Implementation must pass these fixtures before any app registration or UI promotion."
    addition = anchor + "\n\nThe pure recognizer implementation now passes all frozen fixtures and all 54 dedicated corpus expectations with zero protected-clinical overlaps. Risk R10 remains open because generic NER composition, AGB/BSN cross-recognizer precedence, visible profile policy, cross-profile regression and live app verification are not yet complete."
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("RISK_REGISTER recognizer implementation anchor not found")
        text = text.replace(anchor, addition, 1)
        write(path, text)


def update_claim() -> None:
    path = "workpackage_claims/scrub_wp_care_profile_recognizer_implementation.md"
    text = read(path)
    if "Status: in_progress" in text:
        write(path, text.replace("Status: in_progress", "Status: completed", 1))


def main() -> None:
    update_roadmap()
    update_workpackages()
    update_changelog()
    update_risk_register()
    update_claim()

    Path("ops/finalize_care_recognizer_implementation.py").unlink(missing_ok=True)
    Path(".github/workflows/finalize-care-recognizer-implementation.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
