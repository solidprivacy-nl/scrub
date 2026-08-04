# Workpackage claim — SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION

Repository: `solidprivacy-nl/scrub`  
Branch: `scrub-processed-text-selection-table-integration`  
Claimed: 2026-08-04 01:34 Europe/Amsterdam  
Status: completed in GitHub; deployment synchronization and app verification pending

## Dependency gate

- Contract merged through PR #60.
- Pure action model merged through PR #61.
- Non-mutating component spike merged through PR #62 as `671393d4fd3c030d8144369c7fb95297e4c15e92`.
- Final spike regression #1994: 1126 tests passed in 12.28s.

## Goal

Integrate the approved select → inspect → choose type → add row flow into the production side-by-side review path while preserving the authoritative review table, current manual form, static-renderer rollback, document binding and unchanged export/Scrub Key/reinsert semantics.

## Scope

- add a pure integration/session adapter before touching the UI;
- promote the isolated component wrapper to a production-capable render entry point while retaining the spike alias;
- integrate the component into `side_by_side_review_panel_ui.py` behind a document-scoped rollback/fallback switch;
- return raw component events and server-owned preview/highlight context to `presidio_streamlit.py`;
- process inspect events through `inspect_selection` and rerun before export controls;
- process commit events through `commit_manual_mask`, append one normal row to the existing document-scoped `manual_mask_rows`, and rerun immediately;
- retain `Gemiste waarde toevoegen` and the full review table;
- implement one-step undo for the most recent selection-created row;
- preserve review mode and marker controls;
- add unit, integration and Streamlit contract tests;
- verify GitHub Actions, GitHub-to-Hugging-Face sync and live app behavior.

## Boundaries

- all exact occurrences only;
- no occurrence-specific replacement;
- no export filename, MIME, format or mapping change;
- no Scrub Key schema/binding/lifecycle change;
- no reinsert semantic change;
- no recognizer, profile, threshold or dependency upgrade;
- no external assets, telemetry, network calls or browser persistence;
- static renderer and manual form remain available as rollback/fallback through app verification;
- this is the only active worker touching the central review flow.
