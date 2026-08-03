from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 17:12 Europe/Amsterdam"
WP = "SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR"


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
    anchor = "The dedicated pure recognizer implementation is now green but remains unregistered: sixteen care entities pass 37/37 positive contracts, 16/16 negative/collision contracts and all 54 dedicated expectations in the eight-document corpus, with zero protected-clinical overlaps. The next gate is central profile composition and AGB/BSN precedence before any visible Zorg profile is added."
    addition = anchor + "\n\nCentral profile configuration is now implemented without changing the live UI. The current three options remain exact, while future Streamlit and desktop four-profile orders, thresholds, entity groups, care policy actions and fifteen exact-span precedence winners are frozen. Care recognizer registration and visible UI integration remain the next gated package."
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("ROADMAP profile configuration anchor not found")
        write(path, text.replace(anchor, addition, 1))


def update_workpackages() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; pure four-profile configuration implemented, live integration still closed.

Goal:
- Centralize General Dutch, Care, Legal and International recognition behavior before changing the visible Streamlit selector.

Result:

```text
Profiles defined: 4
Current visible options preserved: 3
Future Streamlit order: Care, Legal, General Dutch, International
Desktop order: General Dutch, Care, Legal, International
Exact-span precedence winners: 15
Initial regression run #1865: 965 tests passed
Live UI changed: false
Care recognizers registered: false
```

Configuration includes:
- stable labels, internal values and thresholds;
- profile-specific entity groups;
- legal/care candidate and example direction;
- approved Care replace versus review-selected policy;
- exact-span AGB-over-BSN and care-specific-over-broad-legacy precedence;
- preservation of partial overlaps and non-Care profile behavior.

Evidence:
- `RECOGNITION_PROFILE_CONFIGURATION.md`
- `output/validation/recognition_profile_configuration.json`

Active next package:
- `SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION`

Boundaries:
- no `presidio_streamlit.py` or `presidio_helpers.py` change;
- no live selector, threshold or entity behavior change;
- no export, Scrub Key or reinsert change;
- human review remains required;
- production readiness remains false.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: completed; pure recognition-profile configuration implemented.

Purpose:
- Replace scattered future profile branching with one tested source of truth before exposing Zorg in the current UI.

Files added:
- `recognition_profiles.py`
- `recognition_profile_validation.py`
- `RECOGNITION_PROFILE_CONFIGURATION.md`
- `tests/test_recognition_profiles.py`
- `tests/test_recognition_profile_validation.py`
- `output/validation/recognition_profile_configuration.json`
- `workpackage_claims/scrub_wp_recognition_profile_configuration_refactor.md`
- `handover/workpackages/20260803_1712_recognition_profile_configuration_refactor.md`

Implementation result:
- preserved the exact current three-profile order and labels;
- defined the future Streamlit and desktop four-profile orders;
- centralized thresholds, entity groups, candidate/example direction and Care policy actions;
- added deterministic exact-span precedence for fifteen care-specific winners;
- kept partial overlaps and all non-Care profile results unchanged;
- kept live UI and care recognizer registration explicitly false.

Validation:
- initial GitHub Actions run #1865 passed: 965 tests;
- final clean validation pending after governance finalization;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- `presidio_streamlit.py`, `presidio_helpers.py` or current analyzer registration;
- visible profile selector, thresholds or entity defaults;
- review, export, Scrub Key or reinsert semantics;
- runtime, dependencies or cloud processing.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    text = read(path)
    anchor = "The pure recognizer implementation now passes all frozen fixtures and all 54 dedicated corpus expectations with zero protected-clinical overlaps. Risk R10 remains open because generic NER composition, AGB/BSN cross-recognizer precedence, visible profile policy, cross-profile regression and live app verification are not yet complete."
    addition = anchor + "\n\nThe central profile model now freezes Care composition and exact-span precedence without changing the live application. Risk R10 remains open until the current app registers the care recognizers, uses the profile policy, runs cross-profile regression and passes deployed app verification."
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("RISK_REGISTER profile configuration anchor not found")
        write(path, text.replace(anchor, addition, 1))


def update_claim() -> None:
    path = "workpackage_claims/scrub_wp_recognition_profile_configuration_refactor.md"
    text = read(path)
    if "Status: in_progress" in text:
        write(path, text.replace("Status: in_progress", "Status: completed", 1))


def main() -> None:
    update_roadmap()
    update_workpackages()
    update_changelog()
    update_risk_register()
    update_claim()

    Path("ops/finalize_recognition_profile_configuration_refactor.py").unlink(missing_ok=True)
    Path(".github/workflows/finalize-recognition-profile-configuration-refactor.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
