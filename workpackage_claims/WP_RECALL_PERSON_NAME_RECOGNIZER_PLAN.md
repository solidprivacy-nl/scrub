status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN — Plan safe PERSON-name recognition improvements
started timestamp: 2026-06-18 18:48 Europe/Amsterdam
completed timestamp: 2026-06-18 18:48 Europe/Amsterdam
scope: planning/specification-only PERSON-name recognizer design
boundaries: no product code, no recognizer implementation, no candidate scanner implementation, no runner/report changes, no UI, no export, no Scrub Key, no reinsert, no thresholds, no gate, no product claim

final commit SHA or PR link: 0860c0f1ca07f3aa8c175d406539d1ab3bf597ea
handover path: handover/workpackages/20260618_1848_recall_person_name_recognizer_plan.md

files added:
- RECALL_PERSON_NAME_RECOGNIZER_PLAN.md
- handover/workpackages/20260618_1848_recall_person_name_recognizer_plan.md
- workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN.md

files changed:
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- DECISION_LOG.md
- workpackage_claims/WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN.md

product-code changes: none
recognizer implementation: none
candidate scanner implementation: none
runner/report changes: none
thresholds enforced: none
production gate: none
product claim: none

effects:
- Added safe PERSON-name recognition planning document.
- Defined value-only role/title + name direction, candidate-only weak-context direction, single-surname policy and contract-test-first route.
- Recorded decision that PERSON-name improvement proceeds test-first.

tests/checks:
- Local tests were not run because this package is planning/specification-only and only markdown/governance files changed.
- git diff --check was not runnable in this connector-only environment.

GitHub Actions status: pending/unknown at closeout time.
Hugging Face sync status: pending/unknown at closeout time.
app verification status: not required; no app behavior changed.

remaining risks:
- PERSON-name false-negative risk is planned but not fixed.
- No recognizer implementation was added.
- No candidate scanner fallback was added.
- Single-surname detection remains ambiguous.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

next recommended step: WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS after separate coordinator approval. Do not start follow-up work automatically.
