# Workpackage claim — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-care-profile-long-form-synthetic-corpus`  
Claimed: 2026-08-03 22:17 Europe/Amsterdam  
Status: in_progress

## Goal

Replace the short visible synthetic care examples with longer, structured variants that give testers more realistic review context while preserving all existing identifiers, policy buckets and clinical-meaning safeguards.

## Scope

- retain the eight stable care-document families, names and IDs;
- retain every existing `replace`, `review_selected`, `preserve`, `audit_only` and `ambiguity_traps` contract;
- add substantial synthetic care narrative with document-type-specific sections;
- keep added narrative free of new names, identifiers, dates, addresses, telephone numbers, e-mail addresses and organizations;
- add tests for length, structure, contract preservation and UI exposure;
- update changelog, release notes, workpackages and handover.

## Boundaries

- synthetic data only;
- no recognizer, threshold or profile-policy change;
- no review-table, export, Scrub Key or reinsert semantic change;
- no cloud processing or dependency change;
- human review remains mandatory;
- visible example content changes, so Hugging Face sync and app verification are required after merge.
