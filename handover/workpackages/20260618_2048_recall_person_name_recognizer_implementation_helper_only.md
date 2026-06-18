# Handover — WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY — Implement safe helper-level PERSON-name recognition improvements`

Status: completed and verified.

## Summary

Implemented a small contract-backed helper for role/title PERSON-name recognition.

The helper returns value-only PERSON-name spans for strong role/title context examples such as `arts Bakker`, `getuige Fatima El Amrani`, `cliënt Youssef Ait Ben`, `verpleegkundige Sara El Idrissi`, `mantelzorger Fatima Zahra`, `mr. Lina de Vries` and `mr. Noor van Dijk`.

This package does not change the Streamlit UI, export/download, Scrub Key, reinsert, candidate scanner, runner/report semantics, thresholds, production gates or product claims.

A follow-up fix changed the helper regex so only the role/title cue is case-insensitive. The name-value tokens remain uppercase-sensitive. This prevents lowercase sentence words after the name from being swallowed into the value span.

## Files added

- `person_name_recognizer_helper.py`
- `tests/test_recall_person_name_recognizer_implementation.py`
- `handover/workpackages/20260618_2048_recall_person_name_recognizer_implementation_helper_only.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY.md`

## Files changed

- `person_name_recognizer_helper.py`
- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY.md`

## Product-code changes

A new helper module was added and then tightened:

```text
person_name_recognizer_helper.py
```

No Streamlit UI flow and no export/download/Scrub Key/reinsert behavior changed.

## Recognizer implementation summary

Implemented helper-level matching for contract-backed strong role/title contexts:

- role/title cue + bounded name-value regex;
- role/title cue is case-insensitive;
- name-value tokens remain uppercase-sensitive;
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

Coordinator screenshot evidence showed the first implementation attempt had failing tests. The most likely cause was global `re.IGNORECASE` in `person_name_recognizer_helper.py`, which could let lowercase sentence words become part of a name-value span. The helper was fixed by scoping case-insensitivity to the role/title cue only.

Coordinator screenshot evidence now confirms:

```text
Tests #1292 for commit d4e063d — green
Sync to Hugging Face Space #1303 for commit d4e063d — green
Hugging Face Space app — running without Script execution error
```

## Validation status

Verified by coordinator screenshot evidence.

## GitHub Actions status

Verified green by coordinator screenshot evidence.

```text
Tests #1292 for commit d4e063d — green
```

## Hugging Face sync status

Verified green by coordinator screenshot evidence.

```text
Sync to Hugging Face Space #1303 for commit d4e063d — green
```

## App verification status

Verified healthy by coordinator screenshot evidence. The Hugging Face Space is running without Script execution error.

No app behavior change was expected because the helper is not wired into the Streamlit recognizer setup in this package.

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
