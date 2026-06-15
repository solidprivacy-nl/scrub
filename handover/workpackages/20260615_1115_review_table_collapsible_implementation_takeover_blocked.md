# Handover — WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION takeover blocked

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION — Make “Controleer gevonden gegevens” collapsible while preserving review table role`

Status: blocked during coordinator-approved takeover.

## Context

The coordinator could not find the original active worker and asked whether this workpackage could be taken over.

The existing claim was reused rather than creating a duplicate claim.

## What was attempted

- Required project files and relevant review-table contract files were read.
- The current `presidio_streamlit.py` review-table section was inspected.
- The contract confirmed that the review table must remain the source of truth/fallback and keep `replacement_editor`, `include`, `remember`, `find` and `replace_with`.
- A small helper file was added as an initial non-runtime artifact:
  - `review_table_collapsible_ui.py`

## Why implementation is blocked

The safe product implementation requires changing the central review-table section in `presidio_streamlit.py`.

Through the ChatGPT GitHub connector, the full current `presidio_streamlit.py` content could not be safely retrieved and replaced as a complete file without risking an accidental overwrite of unrelated review/export/Scrub Key/reinsert code.

Alternative routes were considered and rejected:

- adding another startup source patch;
- changing Docker startup commands;
- monkeypatching Streamlit globally from another UI module.

Those routes would increase runtime fragility and conflict with the current direction to avoid unsafe startup mutation and hidden UI side effects.

## Files added

- `review_table_collapsible_ui.py`
- `handover/workpackages/20260615_1115_review_table_collapsible_implementation_takeover_blocked.md`

## Files changed

- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION.md` should be updated to blocked/released after this handover.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

No runtime UI implementation was completed.

## Validation status

Blocked before production UI change.

## GitHub Actions status

Not applicable for a completed implementation because the implementation was not safely completed.

## Hugging Face sync status

Not applicable for a completed implementation because the implementation was not safely completed.

## App verification status

Not applicable. No completed runtime UI change is available to verify.

## Remaining risks

- `review_table_collapsible_ui.py` is present as a helper artifact but is not wired into production UI.
- `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION` still requires a worker with safe full-file edit capability or a clean branch/PR workflow that can apply and review the `presidio_streamlit.py` patch.
- The review table is still visually open in the normal app flow until a safe implementation lands.

## Next recommended step

Use a worker/environment that can safely edit `presidio_streamlit.py` as a complete file and run tests.

Required implementation shape:

```text
3. Controleer gevonden gegevens
- collapsible/expander-based review table area
- review table remains source of truth/fallback
- replacement_editor key preserved
- include/remember/find/replace_with preserved
- no export/download, Scrub Key, reinsert or replacement behavior changes
```

Do not use startup source mutation, global monkeypatching, or hidden side effects for this UI change.
