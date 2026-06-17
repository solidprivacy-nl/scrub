# Handover — WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — Fix corpus email-domain validator punctuation handling`

Status: completed as tests-only repair.

## Summary

GitHub Actions screenshots showed `tests/test_recall_gold_label_corpus_seed.py::test_seed_corpus_uses_reserved_example_email_domain_only` failing. The validator regex was capturing sentence-final punctuation in text fixtures, for example `sami.elamrani@example.test.` instead of `sami.elamrani@example.test`.

The fix changes the test regex so email matches must end on an alphanumeric domain character. This keeps `.example.test` enforcement intact while allowing normal sentence punctuation after an email address.

## Files added

- `workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX.md`
- `handover/workpackages/20260617_0920_recall_benchmark_runner_email_domain_test_fix.md`

## Files changed

- `tests/test_recall_gold_label_corpus_seed.py`

## Product-code changes

None.

## Tests/checks run

Local tests were not runnable in this environment because no local GitHub working tree is available.

Required follow-up verification:

```text
python -m pytest -q tests/test_recall_gold_label_corpus_seed.py
python -m pytest -q tests/test_recall_benchmark_runner_minimal.py
python -m pytest -q tests
```

GitHub Actions should be used as source of truth for the repair commit.

## Validation status

Static review completed. The failing regex:

```text
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+
```

was replaced with:

```text
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]*[A-Za-z0-9]
```

This prevents trailing punctuation from being included in the matched email.

## GitHub Actions status

Pending after repair commit `151749e4e4f19d3eaeffce52b1b83a807e15df5c`.

## Hugging Face sync status

Pending after repair commit.

## App verification status

Not required. This is tests-only and does not change app behavior.

## Remaining risks

- The repair still needs GitHub Actions confirmation.
- If tests remain red, inspect the next failure before starting a new workpackage.

## Next recommended step

Wait for GitHub Actions Tests and Sync to Hugging Face Space for repair commit `151749e4e4f19d3eaeffce52b1b83a807e15df5c`.
