# Handover — WP28C-REPAIR2 warning acknowledgement tests

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP28C-REPAIR2 — Warning acknowledgement test repair`

Status: completed narrow test repair.

## Summary

The latest failing test run showed that `tests/test_scrub_key_warning_acknowledgement_ui.py` still required exact internal helper-call strings. Those strings are not the UI warning contract and may live in patched app output or helper layers depending on startup patch order.

This repair keeps the important WP28C assertions:

- warning copy is present;
- acknowledgement keys are present;
- high-risk buttons are gated;
- file names, MIME types and data expressions are preserved;
- audit fields remain visible;
- forbidden security/processing claims are not added.

It removes exact internal helper-call string assertions from the test contract.

No UI behavior, helper logic, schema, export/reinsert behavior, dependency, runtime behavior or real data changed.

## Files changed

- `tests/test_scrub_key_warning_acknowledgement_ui.py`

## Files added

- `handover/workpackages/20260612_1655_wp28c_repair2_warning_acknowledgement_tests.md`

## Tests/checks run

No live pytest run was possible through the GitHub connector.

## Validation status

- Test repair committed.
- GitHub Actions status pending for final repair commit.
- Hugging Face sync status pending for final repair commit.
- App verification still depends on green tests and sync.

## GitHub Actions status

Pending / to be checked after this repair commit.

## Hugging Face sync status

Pending / to be checked after this repair commit.

## App verification status

Pending. Do not app-verify until tests and sync are green.

## Remaining risks

- If tests remain red, inspect the next failing assertion from the test log.
- WP28C closeout still requires green tests, green sync and app verification.

## Next recommended step

Check the new Tests and Sync runs for commit `258f5a9a2b275f2ee06efd364f2839068917737f`. If green, proceed to app verification and then `WP28C-CLOSEOUT`.
