# Handover — WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN — Plan safe PERSON-name recognition improvements`

Status: completed as planning/specification-only.

## Summary

Added a safe, test-first planning document for future PERSON-name recognition improvements.

This work does not implement recognizers, does not change candidate scanner behavior, does not change runner/report behavior, does not change the app, and does not create thresholds, gates or product claims.

## Files added

- `RECALL_PERSON_NAME_RECOGNIZER_PLAN.md`
- `handover/workpackages/20260618_1848_recall_person_name_recognizer_plan.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN.md` pending final claim closeout update after this handover file

## Product-code changes

None.

## Recognizer implementation

None.

## Candidate scanner implementation

None.

## Runner/report changes

None.

## Tests/checks run

Local tests were not run because this package is planning/specification-only and only markdown/governance files changed.

`git diff --check` was not runnable in this connector-only environment.

## Validation status

Documentation/specification completed.

## GitHub Actions status

Pending/unknown at handover time.

## Hugging Face sync status

Pending/unknown at handover time.

## App verification status

Not required. No app behavior changed.

## Summary of recognizer plan

The plan records a safe route for future PERSON-name recognition work:

- value-only matching: mask the name value, not role/context meaning;
- preserve role/context words;
- avoid broad capitalization-based matching;
- treat single-surname handling as high ambiguity;
- require synthetic contract tests before implementation;
- prefer hard recognition only for strong role/title + full-name cases;
- prefer candidate-only behavior for weaker name-near-contact/reference contexts;
- keep review table as source of truth.

Planned strategy options:

```text
Option A — context-bound role/title + name recognizer
Option B — multi-token Dutch/Moroccan name candidate recognizer
Option C — name-near-contact/reference candidate
```

Recommended implementation route:

```text
1. WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS
2. WP_RECALL_PERSON_NAME_RECOGNIZER_IMPLEMENTATION_HELPER_ONLY
3. WP_RECALL_PERSON_NAME_RECOGNIZER_BENCHMARK_REVIEW
4. WP_RECALL_PERSON_NAME_RECOGNIZER_APP_VERIFICATION_CLOSEOUT, only if product behavior/UI later changes
```

## Remaining risks

- PERSON-name false-negative risk is planned but not fixed.
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
WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS
```

Do not start follow-up work automatically.
