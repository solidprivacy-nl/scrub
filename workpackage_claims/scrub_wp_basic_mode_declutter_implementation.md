# Workpackage Claim — SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: blocked / implementation not started

Start timestamp: 2026-07-04 00:00 UTC
Blocked timestamp: 2026-07-04 00:00 UTC

## Workpackage title

SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION — Make Basiscontrole materially cleaner while preserving Expertcontrole

## Scope

Visible UI implementation. Make `Basiscontrole` materially cleaner than the first mode-split implementation while preserving full `Expertcontrole`. Mode switching changes visibility/grouping only.

## Allowed files

Implementation:

- presidio_streamlit.py
- side_by_side_review_panel_ui.py

Tests:

- tests/test_basic_mode_declutter_implementation.py
- tests/test_basic_mode_declutter_contracts.py
- tests/test_basic_expert_review_mode_implementation.py
- tests/test_basic_expert_review_mode_contracts.py
- tests/test_review_surface_simplification_implementation.py
- tests/test_secondary_control_grouping_polish_implementation.py
- tests/test_export_download_ux_contracts.py
- tests/test_export_download_ux_implementation.py

Documentation/status:

- RELEASE_NOTES.md
- CHANGELOG.md
- WORKPACKAGES.md
- workpackage_claims/scrub_wp_basic_mode_declutter_implementation.md
- handover/workpackages/YYYYMMDD_HHMM_basic_mode_declutter_implementation.md

## Validation policy

Visible UI behavior changes require source-level tests, PR validation/GitHub Actions, Hugging Face sync and live app verification.

## Blocker

Implementation requires a targeted patch to `presidio_streamlit.py`. The available GitHub write tool can update files only by full-file replacement, not by applying a small diff/patch. Because `presidio_streamlit.py` is large and safety-critical, applying a generated full-file replacement from the connector session would create unnecessary risk of accidental product-code drift.

No runtime/startup patch, CSS hack, or wrapper approach was introduced because that would violate the package boundaries and the project safety rules.

## Validation status

- Required project documents were read.
- Precondition verified: `SCRUB-WP_BASIC_MODE_DECLUTTER_CONTRACT_TESTS` is merged.
- Existing branch inspected: `scrub-basic-mode-declutter-implementation`.
- Current review/export source area inspected.
- Product code changed: no.
- Tests added: no.
- GitHub Actions: not applicable; no PR opened.
- Hugging Face sync: not applicable.
- App verification: not applicable.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking, hidden export gate or old replacement decision helper panel.

## Handover path

handover/workpackages/20260704_0000_basic_mode_declutter_implementation_blocked.md

## Next recommended step

Continue this package with a worker/tooling setup that can apply a small source patch to `presidio_streamlit.py` safely, such as local git or a connector action that supports unified diffs. Do not implement via full-file rewrite or runtime patching.
