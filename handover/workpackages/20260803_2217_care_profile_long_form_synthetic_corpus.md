# Handover — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS

Repository: `solidprivacy-nl/scrub`  
Workpackage title: Long-form synthetic Zorgfilter corpus  
Status: implemented; validation pending

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

- `care_test_examples.py` — integration pending operator execution
- `WORKPACKAGES.md` — governance entry pending operator execution
- `CHANGELOG.md` — implementation entry pending operator execution
- `RELEASE_NOTES.md` — user-facing entry pending operator execution
- `RISK_REGISTER.md` — bounded evidence update pending operator execution

## Tests

Added contracts for:

- exact coverage of the eight stable case IDs;
- at least two hundred added words per example;
- five added section headings per example;
- no digits or new obvious identity markers in the additions;
- non-mutating expansion behavior;
- minimum total visible length of two hundred fifty words;
- one occurrence of every existing expected sensitive value;
- preservation of all clinical phrases;
- parity between corpus text and the current UI adapter.

## Validation status

- GitHub Actions: pending
- Hugging Face sync: pending merge
- App verification: pending after sync because visible example content changed

## Remaining risks

- Longer synthetic examples improve tester context but do not establish production recall or precision.
- Generic NER remains model-dependent.
- Human review remains mandatory.
- No runtime, export, Scrub Key or reinsert change is authorized by this package.

## Next recommended step

Run the integration operator, execute the full regression suite, open a PR, merge only when Actions are green, verify Hugging Face synchronization and request focused live app verification of the eight longer care examples.
