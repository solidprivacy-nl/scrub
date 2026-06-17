# Handover — WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — Fix corpus email-domain validator domain handling`

Status: completed as tests-only repair.

## Summary

GitHub Actions screenshots showed `tests/test_recall_gold_label_corpus_seed.py::test_seed_corpus_uses_reserved_example_email_domain_only` failing.

First failure:

```text
sami.elamrani@example.test.
```

Root cause: the validator regex captured sentence-final punctuation in text fixtures.

First repair:

```text
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]*[A-Za-z0-9]
```

Second failure:

```text
sami.elamrani@example.test
```

Root cause: the assertion checked `email.endswith(".example.test")`, but a normal reserved-domain email ends with `@example.test`, not `.example.test`.

Final repair: split on `@` and require the domain to equal `example.test`.

## Files added

- `workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX.md`
- `handover/workpackages/20260617_0920_recall_benchmark_runner_email_domain_test_fix.md`

## Files changed

- `tests/test_recall_gold_label_corpus_seed.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX.md`
- `handover/workpackages/20260617_0920_recall_benchmark_runner_email_domain_test_fix.md`

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

Static review completed.

The regex now avoids sentence-final punctuation, and the assertion now validates the email domain after `@`:

```text
_, domain = email.rsplit("@", 1)
assert domain == "example.test"
```

## GitHub Actions status

Pending after final repair commit `222ebb87b448b24e249ce882e34430776f3e1a72`.

## Hugging Face sync status

Pending after final repair commit.

## App verification status

Not required. This is tests-only and does not change app behavior.

## Remaining risks

- The final repair still needs GitHub Actions confirmation.
- If tests remain red, inspect the next failure before starting a new workpackage.

## Next recommended step

Wait for GitHub Actions Tests and Sync to Hugging Face Space for repair commit `222ebb87b448b24e249ce882e34430776f3e1a72`.
