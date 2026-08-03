# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-processed-text-selection-masking-plan`  
Claimed: 2026-08-03 23:42 Europe/Amsterdam  
Status: completed as planning; GitHub Actions green

## Goal

Assess and specify a safe document-centric interaction in which a user selects an unmasked term in `Verwerkte tekst`, opens a context menu with the right mouse button, chooses a masking type, and adds the value through the existing manual replacement path.

## Scope

- analyse current Streamlit, component, replacement-table and export architecture;
- compare feasible implementation options;
- define the recommended UX and event contract;
- define type choices, exact-occurrence semantics and validation;
- define privacy, security, accessibility and failure boundaries;
- define a small test-first implementation sequence;
- add a roadmap anchor for discussion without implementing UI behavior.

## Boundaries

- planning/documentation only;
- no `presidio_streamlit.py`, review component, manual-mask helper or export change;
- no custom component implementation or dependency upgrade;
- no occurrence-specific replacement semantics;
- review table remains source of truth and fallback;
- no Scrub Key, reinsert, recognizer or cloud-processing change;
- implementation requires explicit coordinator approval after discussion.
