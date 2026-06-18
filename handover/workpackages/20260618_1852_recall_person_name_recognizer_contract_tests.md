# Handover — WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS — Add contract tests for safe future PERSON-name recognition`

Status: completed as tests/specification-only, pending GitHub Actions/HF verification.

## Summary

Added contract fixture, contract tests and specification documentation for safe future PERSON-name recognition behavior.

This package does not implement recognizers, does not change candidate scanner behavior, does not change runner/report behavior, does not change the app, and does not create thresholds, gates or product claims.

## Files added

- `tests/fixtures/person_name_recognizer_contract_cases.json`
- `tests/test_recall_person_name_recognizer_contracts.py`
- `PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md`
- `handover/workpackages/20260618_1852_recall_person_name_recognizer_contract_tests.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md` pending final claim closeout update after this handover file

## Product-code changes

None.

## Recognizer implementation

None.

## Candidate scanner implementation

None.

## Runner/report changes

None.

## Tests added/updated

Added:

```text
tests/test_recall_person_name_recognizer_contracts.py
```

Fixture added:

```text
tests/fixtures/person_name_recognizer_contract_cases.json
```

Contract documentation added:

```text
PERSON_NAME_RECOGNIZER_CONTRACT_TESTS.md
```

## Summary of contract coverage

Contract fixture and tests cover:

- fixture metadata: `contract_only`, synthetic, no product gate, no thresholds, no product claim;
- positive future hard-recognizer cases;
- candidate-only weak-context cases;
- negative cases that must not become PERSON matches;
- explicit single-surname policy for `Bakker` and `Jansen`;
- required preserve terms;
- non-claim boundaries;
- no threshold/gate enforcement.

Positive future hard-recognizer examples include:

```text
arts Bakker
getuige Fatima El Amrani
cliënt Youssef Ait Ben
verpleegkundige Sara El Idrissi
mantelzorger Fatima Zahra
mr. Lina de Vries
mr. Noor van Dijk
```

Candidate-only examples include:

```text
Hassan El Amrani en Mila van Dijk near contact data
Omar Ben Salah near email
Nora El Yassini and Tariq de Jong near legal reference
Sami El Amrani near phone number
```

Negative examples include:

```text
Rechtbank Den Haag
Hof van Discipline
Afdeling Rozenhof 3
Parklaan 188
artikel 7:669 BW
productie 3
bijlage 2
single surname without strong context
```

## Tests/checks run

Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.

Required verification command for GitHub/local runner:

```text
python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py
```

Recommended additional checks:

```text
python -m pytest -q tests/test_recall_person_name_coverage_diagnostics.py
python -m pytest -q tests/test_recall_gold_label_corpus_seed.py
git diff --check
```

## Validation status

Implemented as tests/specification-only. Awaiting GitHub Actions verification.

## GitHub Actions status

Pending/unknown at handover time.

## Hugging Face sync status

Pending/unknown at handover time.

## App verification status

Not required. No app behavior changed.

## Remaining risks

- PERSON-name false-negative risk now has diagnostic and contract test coverage but remains unfixed.
- No recognizer implementation was added.
- No candidate scanner fallback was added.
- Single-surname detection remains ambiguous.
- Broad name matching could over-mask role/context meaning if implemented unsafely.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

## Next recommended step

Recommended next package after separate coordinator approval:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY
```

Then consider:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW
```

Do not start follow-up work automatically.
