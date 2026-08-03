# Handover — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS

Repository: `solidprivacy-nl/scrub`  
Workpackage title: Long-form synthetic Zorgfilter corpus  
Status: implemented; GitHub Actions green; Hugging Face sync and app verification pending

## Summary

Expanded the tester-facing Zorgfilter corpus while preserving the eight stable document families and every existing replace, review-selected, preserve, audit-only and ambiguity-trap contract. Each example receives five document-specific sections and more than two hundred words of additional synthetic care context.

The additions deliberately contain no digits and no new names, identifiers, dates, addresses, contact details, organizations or locations. The existing example selector and all product semantics remain unchanged.

## Files added

- `care_test_example_expansions.py`
- `tests/test_care_profile_long_form_corpus.py`
- `CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS.md`
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md`
- `handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md`

## Files changed

- `care_test_examples.py` — applies the long-form additions to all eight stable cases
- `WORKPACKAGES.md` — workpackage and verification gates recorded
- `CHANGELOG.md` — implementation scope and boundaries recorded
- `RELEASE_NOTES.md` — user-facing change documented
- `RISK_REGISTER.md` — bounded long-form corpus evidence added to R10

## Tests

Added contracts for:

- exact coverage of the eight stable case IDs;
- at least two hundred added words per example;
- five added section headings per example;
- no digits or new obvious identity markers in the additions;
- non-mutating expansion behavior;
- minimum total visible length of two hundred fifty words;
- presence of every existing expected sensitive value without duplication by the added narrative;
- preservation of all clinical phrases;
- parity between corpus text and the current UI adapter.

Existing corpus, recognizer, profile-isolation and clinical-preservation tests remain part of the full suite.

## Validation status

- Initial PR run #1923: 1001 tests passed and two new test-contract assertions failed.
- Failure one: the helper test supplied only one of the eight cases while the helper intentionally verifies complete expansion coverage.
- Failure two: an existing AGB code is a textual prefix of an existing BIG number, so raw substring counting was not a valid uniqueness test.
- Both issues were corrected in the new test file only; corpus content and recognizer behavior were unchanged.
- Corrected PR run #1924: **1003 tests passed in 11.57s**.
- Hugging Face sync: pending merge.
- App verification: pending after sync because visible example content changed.

## GitHub Actions status

Green on PR #56 run #1924. One final clean regression is required after this handover/claim status update.

## Hugging Face sync status

Pending merge. Runtime-relevant files are `care_test_examples.py` and the new `care_test_example_expansions.py`.

## App verification status

Pending after Actions and Hugging Face synchronization are green. Required visible checks:

- all eight Zorgfilter examples remain selectable;
- each selected example is materially longer than the previous version;
- the added document sections are visible and readable;
- existing synthetic identifiers remain present for recognition testing;
- no Script execution error is visible.

## Remaining risks

- Longer synthetic examples improve tester context but do not establish production recall or precision.
- Generic NER remains model-dependent.
- Rare-case re-identification and clinical over-masking risk are not eliminated.
- Human review remains mandatory.
- No runtime dependency, export, Scrub Key or reinsert change is authorized by this package.

## Next recommended step

Run the final clean PR regression, merge PR #56 when green, verify GitHub-to-Hugging-Face synchronization and request focused live app verification of the eight longer care examples.
