# Zorgfilter v1 — cross-profile regression matrix

Status: completed and regression-green; merge pending.

## Purpose

This matrix verifies that the new Care profile adds care-specific detection without contaminating the existing Legal or General Dutch profiles and without damaging protected clinical meaning.

The matrix executes the repository's deterministic Dutch custom recognizers. Generic NER is deliberately excluded because its behavior depends on the selected model and must be observed separately in the deployed app.

## Profiles

```text
Zorgcontrole — streng
Juridische controle — streng
Algemene Nederlandse controle
Algemene internationale controle
```

## Synthetic scope

- 8 care-document families;
- 12 existing legal examples;
- 16 dedicated care entities;
- shared Dutch identity recognizers;
- dedicated legal recognizers;
- exact-span collision precedence;
- care replace/review-selected policy;
- protected clinical passages.

## Hard-gate results

```text
Dedicated care expectations in Care + International: 108/108
Hard profile failures:                              0
Protected clinical phrase overlaps:                 0
Care ↔ International dedicated-care parity:         passed
Legal ↔ International dedicated-legal parity:       passed
Care entity leakage into Legal/General:              none
Legal entity leakage into Care/General:              none
```

The matrix therefore found no cross-profile regression caused by the Zorgfilter integration.

## Recorded legal observations

The historical metadata in `legal_test_examples.py` is not a pure deterministic recognizer contract. It combines custom-rule expectations, generic-NER expectations and older negative assumptions. It is retained as evidence rather than silently ignored:

```text
Historical legal metadata expectations: 148
Observed by deterministic custom rules:  132
Recorded gaps:                            16
Recorded negative observations:            4
Total observations:                        20
```

The sixteen gaps consist of `NL_CLIENT_NUMBER` and `NL_LEGAL_PARTY_NAME` expectations in selected legal examples. The four negative observations concern a synthetic BSN that is correctly recognized by the shared Dutch identity layer despite historical `should_not_contain` metadata.

These observations are not introduced by Zorgfilter. They remain visible for later legal benchmark or generic-NER work.

## Evidence

Machine-readable snapshot:

```text
output/validation/care_profile_cross_profile_matrix.json
```

The test suite rebuilds the matrix and compares its summary and all twenty observations with the committed snapshot.

Final validated run before governance closeout:

```text
GitHub Actions run #1899
995 tests passed
```

## Boundaries

- no Streamlit or UI change;
- no review-table change;
- no export, Scrub Key or reinsert change;
- no cloud processing or new runtime dependency;
- synthetic data only;
- generic NER not evaluated;
- human review remains mandatory;
- no production-readiness claim.

## Next gate

`SCRUB-WP_CARE_PROFILE_APP_VERIFY` after GitHub-to-Hugging-Face sync can be verified.
