# Handover — WP_RECALL_PERSON_NAME_COVERAGE_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_PERSON_NAME_COVERAGE_TESTS — Add diagnostic tests for remaining PERSON-name recall gaps`

Status: completed and verified as tests/documentation-only.

## Summary

Added diagnostic tests for the PERSON-name coverage gap inventory.

The tests preserve the known gap inventory and context categories without requiring current recognizers to pass all PERSON examples. This package does not fix the gaps and does not add thresholds, gates or product claims.

## Files added

- `tests/test_recall_person_name_coverage_diagnostics.py`
- `handover/workpackages/20260618_0822_recall_person_name_coverage_tests.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_TESTS.md`

## Files changed

- `RECALL_PERSON_NAME_COVERAGE_REVIEW.md`
- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_TESTS.md`

## Product-code changes

None.

## Recognizer changes

None.

## Candidate scanner changes

None.

## Runner/report changes

None.

## Tests added/updated

Added:

```text
tests/test_recall_person_name_coverage_diagnostics.py
```

Coverage:

- gap inventory names are documented in `RECALL_PERSON_NAME_COVERAGE_REVIEW.md`;
- gap names remain grounded in synthetic corpus source text or gold sidecars;
- relevant PERSON labels remain required direct identifiers;
- acceptable entity types include `PERSON` or `NL_LEGAL_PARTY_NAME` where appropriate;
- context categories have examples;
- disallowed product claims only appear as explicit non-claim/disallowed boundaries;
- no active PERSON coverage enforcement/gate was introduced.

## Tests/checks run

Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.

Coordinator screenshot evidence confirms:

```text
Tests #1253 for commit 0927bec — green
Sync to Hugging Face Space #1264 for commit 0927bec — green
Hugging Face Space app — running without Script execution error
```

Earlier red runs for commit `9930663` were superseded by later green commits after documentation/non-claim boundary updates.

## Validation status

Verified by coordinator screenshot evidence.

## GitHub Actions status

Verified green by coordinator screenshot evidence.

```text
Tests #1253 for commit 0927bec — green
```

## Hugging Face sync status

Verified green by coordinator screenshot evidence.

```text
Sync to Hugging Face Space #1264 for commit 0927bec — green
```

## App verification status

Verified healthy by coordinator screenshot evidence. The Hugging Face Space is running without Script execution error.

No app verification was functionally required because no app behavior changed.

## Summary of diagnostic test coverage

The tests make the PERSON-name gap inventory testable without changing the product or demanding full recognition yet.

The tested inventory includes:

```text
Hassan El Amrani
Mila van Dijk
Ahmed El Idrissi
Bakker
Sara El Idrissi
Youssef Ait Ben
Fatima Zahra
Lina de Vries
Omar Ben Salah
Nora El Yassini
Tariq de Jong
Noor van Dijk
Sami El Amrani
Jansen
Fatima El Amrani
```

The tested context categories include:

```text
arabic_moroccan_style_multi_token
dutch_tussenvoegsel_name
first_name_plus_surname
single_surname
professional_title_context
care_role_context
legal_role_context
name_near_contact_data
name_near_care_or_legal_reference
```

## Remaining risks

- PERSON-name false-negative risk now has diagnostic test coverage but remains unfixed.
- No recognizer implementation was added.
- No candidate scanner fallback was added.
- Single-surname detection remains ambiguous.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

## Next recommended step

Recommended next package after separate coordinator approval:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN
```

Then consider:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS
```

Do not start follow-up work automatically.
