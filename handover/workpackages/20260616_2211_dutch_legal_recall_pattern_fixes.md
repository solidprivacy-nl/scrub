# Handover — WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES — Improve Dutch legal recall patterns based on documented gap tests`

Status: completed as targeted helper-level detection improvement.

## Summary

Implemented a narrow Dutch Legal candidate-scanner improvement and converted the Dutch legal recall baseline from known-gap xfail tests to direct helper-level assertions for this first fixed round.

The product behavior changed only in the review-candidate helper layer: more reference-like values can be surfaced for human review when the automatic recognizer stack misses them. No UI, export, Scrub Key, reinsert, startup, Docker or dependency behavior changed.

## Files added

- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES.md`
- `handover/workpackages/20260616_2211_dutch_legal_recall_pattern_fixes.md`

## Files changed

- `candidate_scanner.py`
- `tests/test_dutch_legal_recall_gap_baseline.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES.md` pending final closeout update after this handover file

## Patterns/entities adjusted

Changed `candidate_scanner.py` only:

- Added context-bound case-number scanning for values with spaces.
- Added context cues: `rolnummer`, `rolnr`, `client`, `cliënt`, `camera`, `incident`, `reparatie`.
- Kept the scanner as a review/audit helper, not an automatic redaction layer.

## Tests/checks run

Required local commands were attempted but could not run because the container cannot resolve `github.com` for a local clone:

```text
python -m py_compile presidio_streamlit.py
python -m pytest -q tests/test_dutch_legal_recall_gap_baseline.py
```

Static repository checks through GitHub connector:

- Confirmed `WP_DUTCH_LEGAL_RECALL_GAP_TESTS` is completed before starting.
- Confirmed no prior in-progress claim existed before starting.
- Read required control files and relevant helper/test files.

## Xfail tests converted to pass

The baseline file no longer uses `pytest.mark.xfail` for this first fixed round. Converted to normal assertions:

- `test_legal_reference_numbers_are_detectable`
- `test_clm_reference_must_not_be_phone_number`
- `test_client_dossier_and_zaak_numbers_are_detectable`
- `test_rechtspraak_like_rolnummers_are_detectable`
- `test_role_words_alone_are_not_detected_as_person_values`
- `test_overmasking_does_not_remove_legal_role_structure`

Expected normal baseline tests retained:

- `test_synthetic_gap_fixture_contains_required_legal_references`
- `test_synthetic_role_fixture_contains_only_generic_role_words`

## Fixed / improved gaps

Improved at helper/review-candidate level:

- Numeric court role reference shape.
- `ARN 26/4412`-style case reference shape.
- Client/dossier/zaak reference values when surrounded by Dutch legal/admin context.
- Extra context cues for camera, incident and repair references.
- Generic legal role words remain preserved in baseline tests.

## Remaining gaps

- This package improves candidate visibility; it does not prove complete automatic recognizer classification for every Dutch legal reference type.
- Local pytest/py_compile could not run here.
- GitHub Actions and Hugging Face sync must provide final execution evidence.
- Broader production recall/precision thresholds and gold sidecars remain future work.

## Validation status

- Product-code change is limited to `candidate_scanner.py`.
- Tests updated in `tests/test_dutch_legal_recall_gap_baseline.py`.
- No UI/export/Scrub Key/reinsert/startup/dependency changes were made.
- Final test validation is pending GitHub Actions visibility.

## GitHub Actions status

Unknown at handover time; connector status visibility for direct-push commits has been incomplete in this repo.

## Hugging Face sync status

Unknown at handover time. App verification is not required unless CI/HF exposes unexpected runtime impact.

## App verification status

Not required by scope. No UI behavior changed.

## Remaining risks

- Helper-level candidate surfacing still requires human review.
- Some recognizer-level entity labels may remain less specific than desired until a later narrow recognizer round.
- Local execution was blocked by network/DNS, so CI should be treated as source of truth.

## Next recommended step

Do not automatically continue into another pattern round.

Recommended next package after separate coordinator approval:

```text
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY
```

If verification shows remaining gaps, use a later separate package:

```text
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2
```
