status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — Fix corpus email-domain validator domain handling
started timestamp: 2026-06-17 09:20 Europe/Amsterdam
completed timestamp: 2026-06-17 09:34 Europe/Amsterdam
scope: tests-only repair after GitHub Actions failure
boundaries: no product UI, no recognizer changes, no pattern fixes, no export, no Scrub Key, no reinsert changes, no production gate

final commit SHA or PR link: 222ebb87b448b24e249ce882e34430776f3e1a72
handover path: handover/workpackages/20260617_0920_recall_benchmark_runner_email_domain_test_fix.md

files changed:
- tests/test_recall_gold_label_corpus_seed.py
- workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX.md
- handover/workpackages/20260617_0920_recall_benchmark_runner_email_domain_test_fix.md
- CHANGELOG.md
- WORKPACKAGES.md

product-code changes: none

tests/checks:
- GitHub Actions screenshot first showed failure in tests/test_recall_gold_label_corpus_seed.py::test_seed_corpus_uses_reserved_example_email_domain_only because the regex captured sentence-final punctuation.
- First repair changed the regex to avoid trailing punctuation.
- Follow-up GitHub Actions screenshot showed the assertion itself was still wrong: `sami.elamrani@example.test` ends with `@example.test`, not `.example.test`.
- Final repair checks the domain after `@` equals `example.test`.
- Local tests not runnable in this environment because no local GitHub working tree is available.
- GitHub Actions should be used as final execution proof.

GitHub Actions status: pending after final repair commit.
Hugging Face sync status: pending after final repair commit.
app verification status: not required; tests-only repair and no app behavior changed.

remaining gaps:
- Need coordinator/GitHub Actions verification for final repair commit.

next recommended step: wait for Tests and Sync to Hugging Face Space for commit 222ebb87b448b24e249ce882e34430776f3e1a72. If green, update status evidence. If still red, inspect the next failure before starting any new workpackage.
