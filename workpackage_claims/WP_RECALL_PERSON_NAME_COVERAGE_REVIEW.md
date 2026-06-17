status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_PERSON_NAME_COVERAGE_REVIEW — Review remaining PERSON-name recall gaps in diagnostic benchmark
started timestamp: 2026-06-17 22:23 Europe/Amsterdam
completed timestamp: 2026-06-17 22:23 Europe/Amsterdam
scope: review/planning/documentation-only PERSON-name coverage analysis
boundaries: no product code, no recognizer changes, no candidate scanner changes, no runner/report changes, no UI, no export, no Scrub Key, no reinsert, no thresholds, no gate, no product claim

final commit SHA or PR link: 9cc6f837f90302303e11a5b63a73ec71bc1dc81e
handover path: handover/workpackages/20260617_2223_recall_person_name_coverage_review.md

files added:
- RECALL_PERSON_NAME_COVERAGE_REVIEW.md
- handover/workpackages/20260617_2223_recall_person_name_coverage_review.md
- workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_REVIEW.md

files changed:
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_REVIEW.md

product-code changes: none
recognizer changes: none
candidate scanner changes: none
runner/report changes: none
thresholds enforced: none
production gate: none
product claim: none

effects:
- Classified 14 remaining missed PERSON labels from the cleaned diagnostic artifact.
- Added inventory with context, likely pattern, likely cause, risk and recommended follow-up.
- Classified name types including Dutch tussenvoegsel names, Arabic/Moroccan-style multi-token names, single surnames, care/legal role + name, professional title + name and name-near-contact/reference contexts.
- Recommended tests/contracts before any recognizer implementation.

tests/checks:
- Local tests were not run because this package is review/planning/documentation-only and only markdown/governance files changed.
- git diff --check was not runnable in this connector-only environment.

GitHub Actions status: not applicable for functional validation; documentation-only.
Hugging Face sync status: unknown at closeout time.
app verification status: not required; no app behavior changed.

remaining risks:
- PERSON-name false-negative risk is analyzed but not fixed.
- No recognizer implementation was added.
- No candidate scanner fallback was added.
- Single-surname detection remains ambiguous.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

next recommended step: WP_RECALL_PERSON_NAME_COVERAGE_TESTS after separate coordinator approval. Alternative if design should come first: WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN. Do not start follow-up work automatically.
