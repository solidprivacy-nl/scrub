# Handover — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH

Repository: solidprivacy-nl/scrub  
Status: implemented planning/contract-tests-only / PR validation pending

## Summary

Prepared the final small UI-polish line for calmer secondary-control grouping. Because the actual implementation likely touches the normal review flow in `presidio_streamlit.py` and nested Streamlit expanders are a known risk, this package records the implementation approach and adds source-level contract tests before UI code changes.

The plan targets a calmer secondary-control area below the visible side-by-side review while preserving manual missed-value entry, replacement table, candidate audit values, focus/filter aid, technical details, serial review, reusable replacements, Scrub Key, export/download and audit/DOCX hygiene controls.

## Files added

- `SECONDARY_CONTROL_GROUPING_POLISH_PLAN.md`
- `tests/test_secondary_control_grouping_polish_contracts.py`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish.md`
- `handover/workpackages/20260703_0000_secondary_control_grouping_polish.md`

## Files changed

- `CHANGELOG.md`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish.md`

## Tests / checks

Added source-level contract tests covering:

- plan existence and target to make secondary controls calmer;
- explicit prohibition on nested Streamlit expanders;
- preservation of side-by-side review and `Markeringen tonen`;
- preservation of manual missed-value entry;
- preservation of replacement table/source-of-truth role;
- preservation of secondary review aids;
- export/Scrub Key/reinsert/audit boundaries;
- no prohibited cloud/AI/OCR/restored-PDF/PDF-to-DOCX/click-to-mark/advanced-editor behavior;
- implementation as a separate next package.

Targeted validation command:

```text
python -m pytest -q tests/test_secondary_control_grouping_polish_contracts.py
```

No product tests were run manually in this connector session.

## Validation

- GitHub Actions: pending after PR.
- Hugging Face sync: not applicable until merge to `main`.
- App verification: not applicable because no UI behavior changed in this planning/contract package.

## Intentionally not changed

- product code;
- Streamlit UI;
- `presidio_streamlit.py`;
- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

## Remaining risks

- The actual visible grouping is not implemented yet.
- The next implementation package must avoid nested expanders.
- The next implementation package will require PR validation, Hugging Face sync and live app verification.

## Next recommended step

Open PR and validate this planning/contract package. If green, merge it and start:

```text
SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION
```

The implementation should be narrow and should touch only the normal review-control grouping area.
