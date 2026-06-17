status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — Fix corpus email-domain validator punctuation handling
started timestamp: 2026-06-17 09:20 Europe/Amsterdam
completed timestamp: 2026-06-17 09:20 Europe/Amsterdam
scope: tests-only repair after GitHub Actions failure
boundaries: no product UI, no recognizer changes, no pattern fixes, no export, no Scrub Key, no reinsert changes, no production gate

final commit SHA or PR link: 151749e4e4f19d3eaeffce52b1b83a807e15df5c
handover path: handover/workpackages/20260617_0920_recall_benchmark_runner_email_domain_test_fix.md

files changed:
- tests/test_recall_gold_label_corpus_seed.py
- workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX.md
- handover/workpackages/20260617_0920_recall_benchmark_runner_email_domain_test_fix.md

product-code changes: none

tests/checks:
- GitHub Actions screenshot showed failure in tests/test_recall_gold_label_corpus_seed.py::test_seed_corpus_uses_reserved_example_email_domain_only.
- Failure cause: regex captured sentence-final punctuation in email fixtures, for example `sami.elamrani@example.test.`.
- Fixed validator regex to require the email match to end on an alphanumeric domain character.
- Local tests not runnable in this environment because no local GitHub working tree is available.
- GitHub Actions should be used as final execution proof.

GitHub Actions status: pending after repair commit.
Hugging Face sync status: pending after repair commit.
app verification status: not required; tests-only repair and no app behavior changed.

remaining gaps:
- Need coordinator/GitHub Actions verification for repair commit.

next recommended step: wait for Tests and Sync to Hugging Face Space for commit 151749e4e4f19d3eaeffce52b1b83a807e15df5c. If green, update status evidence. If still red, inspect the next failure before starting any new workpackage.
