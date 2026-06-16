status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY
started timestamp: 2026-06-17 00:32 Europe/Amsterdam
completed timestamp: 2026-06-17 00:32 Europe/Amsterdam
scope: verify Dutch legal recall pattern fixes
boundaries: verification-only; no product-code, UI, export, Scrub Key or reinsert changes

final commit SHA or PR link: 5efd75ba8155f72dd334043ae6575794835f2c17
verified pattern-fix commit SHA: 77090c5d7cba75bc30d49a77a56116e37a78b0fc
additional verified test commit SHA: 440bd27c4e02006c231fbb61a38567a8635d783f
pattern-fix closeout claim SHA: 5345912f62e83ea49d55884c6b4bd6c5da50d5f2
handover path: handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md

files added:
- workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md
- handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md

files changed:
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md

product-code changes in this verify package: none

tests/checks:
- Local clone/test execution failed because the container cannot resolve github.com.
- Static GitHub connector review completed for candidate_scanner.py, tests/test_dutch_legal_recall_gap_baseline.py, review/export tests, claims and handovers.
- Commit comparison confirmed pattern-fix production/helper change is limited to candidate_scanner.py.
- GitHub connector returned no combined statuses and no workflow runs for checked pattern-fix commits.

GitHub Actions status: unknown from this worker.
Hugging Face sync status: unknown from this worker.
app verification status: not performed; HF sync could not be confirmed green.

fixed gaps verified:
- Legal reference and Rechtspraak-like case/role reference coverage is present in the baseline test.
- Client/dossier/zaak reference coverage is present in the baseline test.
- CLM reference is asserted not to be PHONE in the baseline test.
- Generic legal role words are asserted not to be PERSON values.
- Over-masking guard keeps legal role structure readable in the baseline test.

remaining gaps:
- No local pytest execution evidence from this worker.
- No GitHub Actions/HF sync evidence from this worker.
- No live app verification from this worker.
- Candidate surfacing does not prove complete automatic recognizer classification for every Dutch legal reference type.

remaining risks:
- CI or runtime may still expose issues static review cannot catch.
- Helper-level candidate surfacing requires human review.
- Broader recall/precision scorecard and gold-label corpus work remain future work.

next recommended step: do not automatically start another pattern round. If coordinator verifies GitHub Actions/HF externally, record evidence only. If real verification exposes remaining gaps, use a separately approved WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2.
