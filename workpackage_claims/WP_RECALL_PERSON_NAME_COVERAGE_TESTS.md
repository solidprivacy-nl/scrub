status: completed_verified
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_PERSON_NAME_COVERAGE_TESTS — Add diagnostic tests for remaining PERSON-name recall gaps
started timestamp: 2026-06-18 08:22 Europe/Amsterdam
completed timestamp: 2026-06-18 08:22 Europe/Amsterdam
verified timestamp: 2026-06-18 08:34 Europe/Amsterdam
scope: tests/documentation-only PERSON-name coverage diagnostics
boundaries: no product code, no recognizer changes, no candidate scanner changes, no runner/report changes, no UI, no export, no Scrub Key, no reinsert, no thresholds, no gate, no product claim

final commit SHA or PR link: 0927beca1470cd30234537bcfb133abd9839fbd5
handover path: handover/workpackages/20260618_0822_recall_person_name_coverage_tests.md

files added:
- tests/test_recall_person_name_coverage_diagnostics.py
- handover/workpackages/20260618_0822_recall_person_name_coverage_tests.md
- workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_TESTS.md

files changed:
- RECALL_PERSON_NAME_COVERAGE_REVIEW.md
- RECALL_PRECISION_SCORECARD.md
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_RECALL_PERSON_NAME_COVERAGE_TESTS.md

product-code changes: none
recognizer changes: none
candidate scanner changes: none
runner/report changes: none
thresholds enforced: none
production gate: none
product claim: none

effects:
- Added diagnostic tests for the PERSON-name gap inventory.
- Tests keep the known gap inventory visible without requiring current recognizers to pass all PERSON examples.
- Tests verify corpus/source grounding, required PERSON labels, context category examples, non-claim boundaries and no enforcement/gate boundary.

tests/checks:
- Added tests/test_recall_person_name_coverage_diagnostics.py.
- Local tests were not run because this environment is connector-only and does not expose a local Git working tree for pytest execution.
- Coordinator screenshot evidence shows final Tests #1253 for commit 0927bec green.
- Earlier red runs for commit 9930663 were superseded by later green commits after documentation/non-claim boundary updates.

GitHub Actions status: verified green by coordinator screenshot evidence. Tests #1253 for commit 0927bec green.
Hugging Face sync status: verified green by coordinator screenshot evidence. Sync to Hugging Face Space #1264 for commit 0927bec green.
app verification status: verified healthy by coordinator screenshot evidence. Hugging Face Space running without Script execution error; no app behavior change was expected.

remaining risks:
- PERSON-name false-negative risk now has diagnostic test coverage but remains unfixed.
- No recognizer implementation was added.
- No candidate scanner fallback was added.
- Single-surname detection remains ambiguous.
- Human review remains necessary.
- No threshold or gate exists.
- Product claims remain blocked.

next recommended step: WP_RECALL_PERSON_NAME_RECOGNIZER_PLAN after separate coordinator approval. Then consider WP_RECALL_PERSON_NAME_RECOGNIZER_CONTRACT_TESTS. Do not start follow-up work automatically.
