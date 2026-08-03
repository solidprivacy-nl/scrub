# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-processed-text-selection-masking-action-model`  
Claimed: 2026-08-04 00:30 Europe/Amsterdam  
Status: implemented; corrected GitHub Actions run green; final clean regression pending

## Dependency gate

- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT` completed and merged through PR #60 as `23cb5d667461f84a01e96ee007b2ef10bd2e6b40`.
- Clean contract regression: run #1954, 1027 tests passed in 11.48s.
- Coordinator approved the all-exact version-one direction.

## Goal

Implement and adversarially test a pure Python, Streamlit-free and browser-free action model for the frozen two-stage processed-text selection masking contract.

## Scope

- strict parsing and validation of inspect and commit events;
- UTF-16 code-unit offset conversion without surrogate splitting;
- single-line/length/control/letter-number/placeholder selection validation;
- exact non-overlapping occurrence analysis;
- Unicode-aware embedded-token collision analysis;
- exact/nested replacement-rule collision analysis;
- marked processed-range overlap checks;
- ready/confirmation-required/blocked impact classification;
- opaque inspection records and confirmation tokens;
- replay and single-use inspection lifecycle helpers;
- commit-time revalidation;
- adapter to the existing document-bound manual-row builder;
- stable manual action IDs and one-step undo model;
- extensive synthetic and adversarial tests.

## Boundaries

- no Streamlit imports or session-state integration;
- no browser component or JavaScript;
- no `presidio_streamlit.py`, side-by-side UI, review table or export/download flow change;
- no occurrence-specific replacement;
- no Streamlit/dependency upgrade;
- no Scrub Key, reinsert, recognizer, profile or cloud-processing change;
- the helper returns decisions and rows; callers remain responsible for document-scoped storage and reruns.
