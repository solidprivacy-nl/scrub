# Handover — WP_RECALL_PERSON_NAME_COVERAGE_REVIEW

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_PERSON_NAME_COVERAGE_REVIEW — Review remaining PERSON-name recall gaps in diagnostic benchmark`

Status: completed as review/planning/documentation-only.

## Summary

Reviewed and classified the 14 remaining missed `PERSON` labels from the cleaned diagnostic benchmark artifact.

This is not a fix package. It does not change recognizers, candidate scanner, product behavior, runner/report behavior, tests, thresholds or gates.

## Files added

- `RECALL_PERSON_NAME_COVERAGE_REVIEW.md`
- `handover/workpackages/20260617_2223_recall_person_name_coverage_review.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_REVIEW.md`

## Files changed

- `RECALL_PRECISION_SCORECARD.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_REVIEW.md` pending final claim closeout update after this handover file

## Product-code changes

None.

## Recognizer changes

None.

No `dutch_recognizers.py` changes were made.

## Candidate scanner changes

None.

No `candidate_scanner.py` changes were made.

## Runner/report changes

None.

No `recall_benchmark_runner.py`, `recall_benchmark_report.py` or workflow changes were made.

## Tests/checks run

Local tests were not run because this package is review/planning/documentation-only and only markdown/governance files changed.

`git diff --check` was not runnable in this connector-only environment.

## Validation status

Completed by documentation review against existing corpus source/gold sidecars and the cleaned artifact review findings.

## GitHub Actions status

Not applicable for functional validation of this package. Documentation-only.

Connector workflow status may be incomplete for direct-push documentation commits.

## Hugging Face sync status

Unknown at handover time for the final documentation commit.

No app/product behavior changed.

## App verification status

Not required. No app behavior changed.

## Summary of PERSON gaps

The 14 missed `PERSON` labels are classified in `RECALL_PERSON_NAME_COVERAGE_REVIEW.md`.

Main categories:

- Arabic/Moroccan-style multi-token names;
- Dutch names with tussenvoegsels;
- first-name + surname patterns;
- single surnames after roles;
- professional title + name patterns;
- care role + name patterns;
- legal role + name patterns;
- names near phone/email/address;
- names near care/legal references.

Examples:

```text
Hassan El Amrani
Mila van Dijk
Ahmed El Idrissi
Bakker
Sara El Idrissi
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

## Remaining risks

- PERSON-name false-negative risk is analyzed but not fixed.
- No recognizer implementation was added.
- No candidate scanner fallback was added.
- Single-surname detection remains ambiguous.
- Care/legal role words must remain readable while names after them may need masking.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

## Next recommended step

Recommended next package after separate coordinator approval:

```text
WP_RECALL_PERSON_NAME_COVERAGE_TESTS
```

Alternative if design should come first:

```text
WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN
```

Do not start follow-up work automatically.
