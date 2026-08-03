# Workpackage claim — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-care-profile-long-form-synthetic-corpus`  
Claimed: 2026-08-03 22:17 Europe/Amsterdam  
Status: completed and app-verified after GitHub Actions and Hugging Face synchronization verification

## Goal

Replace the short visible synthetic care examples with longer, structured variants that give testers more realistic review context while preserving all existing identifiers, policy buckets and clinical-meaning safeguards.

## Scope

- retain the eight stable care-document families, names and IDs;
- retain every existing `replace`, `review_selected`, `preserve`, `audit_only` and `ambiguity_traps` contract;
- add substantial synthetic care narrative with document-type-specific sections;
- keep added narrative free of new names, identifiers, dates, addresses, telephone numbers, e-mail addresses and organizations;
- add tests for length, structure, contract preservation and UI exposure;
- update changelog, release notes, workpackages and handover.

## Validation

- initial PR run #1923: 1001 passed, two new test-contract failures;
- corrected PR run #1924: 1003 passed in 11.57s;
- final clean PR run #1926: 1003 passed in 11.51s;
- deployment verification run #1931: both runtime files matched Hugging Face byte-for-byte, Streamlit health returned HTTP 200 / `ok`, and 1003 tests passed in 11.35s;
- coordinator/user app verification confirmed at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`

## Boundaries

- synthetic data only;
- no recognizer, threshold or profile-policy change;
- no review-table, export, Scrub Key or reinsert semantic change;
- no cloud processing or dependency change;
- human review remains mandatory;
- visible example content changes, so Hugging Face sync and app verification are required after merge.
