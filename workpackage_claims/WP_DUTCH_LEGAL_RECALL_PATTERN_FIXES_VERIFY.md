status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY
started timestamp: 2026-06-17 00:32 Europe/Amsterdam
completed timestamp: 2026-06-17 00:59 Europe/Amsterdam
scope: verify Dutch legal recall pattern fixes
boundaries: verification-only; no product-code, UI, export, Scrub Key or reinsert changes

final commit SHA or PR link: c8443e0456437c506508e0ebc646d903fd6184e2
verified pattern-fix commit SHA: 77090c5d7cba75bc30d49a77a56116e37a78b0fc
additional verified test commit SHA: 440bd27c4e02006c231fbb61a38567a8635d783f
pattern-fix closeout claim SHA: 5345912f62e83ea49d55884c6b4bd6c5da50d5f2
verified closeout commit SHA: e1e44b3cb664f913414ed80baa6086cf207d67f0
handover path: handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md

files added:
- workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md
- handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md

files changed:
- WORKPACKAGES.md
- CHANGELOG.md
- RISK_REGISTER.md
- handover/workpackages/20260617_0032_dutch_legal_recall_pattern_fixes_verify.md
- workpackage_claims/WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY.md

product-code changes in this verify package: none

tests/checks:
- Local clone/test execution failed because the container cannot resolve github.com.
- Static GitHub connector review completed for candidate_scanner.py, tests/test_dutch_legal_recall_gap_baseline.py, review/export tests, claims and handovers.
- Commit comparison confirmed pattern-fix production/helper change is limited to candidate_scanner.py.
- Coordinator screenshot evidence confirms Tests #1115 for commit e1e44b3 succeeded.
- Coordinator screenshot evidence confirms Sync to Hugging Face Space #1116 for commit e1e44b3 succeeded.
- Earlier Sync to Hugging Face Space #1112 for commit ca5cb3f was red, but was superseded by later green sync evidence.

GitHub Actions status: green by coordinator screenshot evidence, Tests #1115 for commit e1e44b3.
Hugging Face sync status: green by coordinator screenshot evidence, Sync to Hugging Face Space #1116 for commit e1e44b3.
app verification status: confirmed by coordinator screenshot evidence.

fixed gaps verified:
- Legal reference and Rechtspraak-like case/role reference coverage is present in the baseline test.
- Client/dossier/zaak reference coverage is present in the baseline test.
- CLM reference is asserted not to be PHONE in the baseline test.
- Generic legal role words are asserted not to be PERSON values.
- Over-masking guard keeps legal role structure readable in the baseline test.

app smoke verification evidence:
- Hugging Face Space running without Script execution error.
- Step 2 side-by-side review visible.
- Step 3 found-data review visible.
- Collapsed Vervangtabel controleren section visible.
- Serial review visible.
- Export/download buttons visible.
- DOCX hygiene audit visible.

remaining gaps:
- Candidate surfacing does not prove complete automatic recognizer classification for every Dutch legal reference type.
- Broader recall/precision scorecard and gold-label corpus work remain future work.

remaining risks:
- Helper-level candidate surfacing requires human review.
- Later app/user testing may still identify new Dutch legal patterns that need a separate approved round.

next recommended step: do not automatically start another pattern round. No immediate extra pattern round is required based on current coordinator verification evidence. If real verification later exposes remaining gaps, use a separately approved WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_ROUND2.
