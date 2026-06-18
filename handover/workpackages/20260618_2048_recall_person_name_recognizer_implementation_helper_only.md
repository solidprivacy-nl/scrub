# Handover — WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY — Implement safe helper-level PERSON-name recognition improvements`

Status: completed, pending GitHub Actions/HF verification.

## Summary

Implemented a small contract-backed helper for role/title PERSON-name recognition.

The helper returns value-only PERSON-name spans for strong role/title context examples such as `arts Bakker`, `getuige Fatima El Amrani`, `cliënt Youssef Ait Ben`, `verpleegkundige Sara El Idrissi`, `mantelzorger Fatima Zahra`, `mr. Lina de Vries` and `mr. Noor van Dijk`.

This package does not change the Streamlit UI, export/download, Scrub Key, reinsert, candidate scanner, runner/report semantics, thresholds, production gates or product claims.

## Files added

- `person_name_recognizer_helper.py`
- `tests/test_recall_person_name_recognizer_implementation.py`
- `handover/workpackages/20260618_2048_recall_person_name_recognizer_implementation_helper_only.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY.md` pending final claim closeout update after this handover file

## Product-code changes

A new helper module was added:

```text
person_name_recognizer_helper.py
```

No Streamlit UI flow and no export/download/Scrub Key/reinsert behavior changed.

## Recognizer implementation summary

Implemented helper-level matching for contract-backed strong role/title contexts:

- role/title cue + bounded name-value regex;
- returns only the named value span;
- preserves role/context words;
- no broad capitalization-based matching;
- no hard recognizer match for candidate-only weak contexts;
- negative cases are expected to remain unmatched.

Entity type returned by the helper:

```text
NL_LEGAL_PARTY_NAME
```

Important boundary:

```text
This helper is not registered into the Streamlit app recognizer setup in this package.
```

## Candidate scanner changes

None.

## Runner/report changes

None.

## Tests added/updated

Added:

```text
tests/test_recall_person_name_recognizer_implementation.py
```

Test coverage:

- positive contract cases are recognized as value-only spans;
- preserve terms are not included in matched spans;
- negative contract cases do not produce PERSON-name matches;
- single-surname matching is limited to strong role/title context;
- candidate-only weak contexts are not treated as hard recognizer matches.

## Tests/checks run

Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.

Required checks:

```text
python -m pytest -q tests/test_recall_person_name_recognizer_contracts.py
python -m pytest -q tests/test_recall_person_name_recognizer_implementation.py
python -m pytest -q tests/test_recall_person_name_coverage_diagnostics.py
python -m pytest -q tests/test_recall_gold_label_corpus_seed.py
```

Recommended broader checks:

```text
python -m pytest -q tests/test_recall_benchmark_runner_minimal.py
python -m pytest -q
python -m py_compile person_name_recognizer_helper.py
python -m py_compile dutch_recognizers.py
python -m py_compile candidate_scanner.py
python -m py_compile presidio_streamlit.py
git diff --check
```

## Validation status

Implementation and tests added. Awaiting GitHub Actions verification.

## GitHub Actions status

Pending/unknown at handover time.

## Hugging Face sync status

Pending/unknown at handover time.

## App verification status

Pending smoke verification after green Actions/HF sync.

No app behavior change is expected because the helper is not wired into the Streamlit recognizer setup in this package, but a smoke check is still recommended because a Python helper file was added.

## Remaining risks

- PERSON-name false-negative risk is only partially mitigated for contract-backed role/title helper cases.
- The helper is not yet benchmark-reviewed against the diagnostic artifact.
- The helper is not registered into the app recognizer setup in this package.
- Candidate-only weak contexts remain not automatic.
- Single-surname matching remains high-risk and must stay bounded by strong context.
- Human review remains necessary.
- No threshold or production gate exists.
- Product claims remain blocked.

## Next recommended step

After green tests, HF sync and app smoke:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW
```

Do not start follow-up work automatically.
