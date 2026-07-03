# Workpackage Claim — SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION

Repository: solidprivacy-nl/scrub

Status: in_progress

Start timestamp: 2026-07-03 00:00 UTC

## Workpackage title

SCRUB-WP_BASIC_EXPERT_REVIEW_MODE_IMPLEMENTATION — Implement Basiscontrole / Expertcontrole visibility split

## Scope

Small visible UI implementation of the Basiscontrole / Expertcontrole review mode split. Basiscontrole becomes the default lower-cognitive-load mode; Expertcontrole exposes the fuller current review/audit machinery. Mode switching changes visibility/grouping only.

## Allowed files

Implementation:

- presidio_streamlit.py

Tests:

- tests/test_basic_expert_review_mode_implementation.py
- tests/test_basic_expert_review_mode_contracts.py

Documentation/status:

- RELEASE_NOTES.md
- CHANGELOG.md if safe
- WORKPACKAGES.md if safe
- workpackage_claims/scrub_wp_basic_expert_review_mode_implementation.md
- handover/workpackages/YYYYMMDD_HHMM_basic_expert_review_mode_implementation.md

## Validation policy

Visible UI behavior changes require source-level tests, PR validation/GitHub Actions, Hugging Face sync and live app verification. Do not change processing, export, Scrub Key, reinsert, recognizer, benchmark, runtime/startup or dependency semantics.

## Boundaries

No replacement logic changes. No export content, filename or MIME changes. No Scrub Key JSON/meaning changes. No reinsert, recognizer, benchmark, runtime/startup or dependency changes. No cloud, AI, OCR, restored PDF, PDF-to-DOCX, click-to-mark, advanced editor, full-document marking or hidden export gate.
