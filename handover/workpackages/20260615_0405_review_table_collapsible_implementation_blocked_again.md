# Handover — WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION`

Status: blocked again before product-code change.

## What happened

The workpackage was restarted after coordinator approval. The existing claim was changed from `blocked/released` to `in_progress`.

The required implementation touches `presidio_streamlit.py`. The normal `GitHub.update_file` path was attempted for the controlled whole-file replacement, but the tool call was blocked by the safety layer before any product-code change was made.

Because this file is central to review/export flow and a previous worker already warned against unsafe low-level replacement, no forced branch update was performed.

## Files changed

- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_IMPLEMENTATION.md`
- `handover/workpackages/20260615_0405_review_table_collapsible_implementation_blocked_again.md`

## Files not changed

- `presidio_streamlit.py`
- tests
- export/download files
- Scrub Key files
- reinsert files

## Tests/checks run

No tests were run because no product-code implementation was made.

## Validation status

Blocked before implementation.

## GitHub Actions status

Not applicable for product implementation because no product-code change was made.

## Hugging Face sync status

Not applicable for product implementation because no product-code change was made.

## App verification status

Not applicable. UI not changed.

## Remaining risk

The review table remains non-collapsible.

## Next recommended step

Use Codespaces or another worker with a real repository checkout to apply the patch described in:

```text
handover/workpackages/20260615_0315_review_table_collapsible_implementation_repair_blocked.md
```

Required patch:

- wrap the `Controleer gevonden gegevens` review table section in a non-nested `st.expander`;
- include item count in the expander title;
- keep `replacement_editor` and table columns unchanged;
- do not nest `Mogelijke gemiste waarden` inside another expander;
- keep serial review, exports, Scrub Key and reinsert behavior unchanged.
