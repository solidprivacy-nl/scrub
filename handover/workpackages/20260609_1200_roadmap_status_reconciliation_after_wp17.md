# Handover — WP17B — Roadmap current-status reconciliation after WP17

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP17B — Roadmap current-status reconciliation after WP17`

Status: completed documentation-only update.

## Summary

WP17B reconciled `ROADMAP.md` with the current source-of-truth status in `WORKPACKAGES.md` and `CHANGELOG.md` after WP17.

The roadmap no longer points to WP16B/WP17 as active next steps. It now records:

- WP16 / WP16-FIX / WP16B: completed after Actions/sync verification; app verification not applicable.
- WP17: completed planning/specification-only.
- Current next possible step: WP18 — PDF text extraction to restored TXT UI implementation.
- WP18 has not started.
- WP18 must not start unless explicitly approved as a separate implementation workpackage.

## Files added

- `handover/workpackages/20260609_1200_roadmap_status_reconciliation_after_wp17.md`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- Not required; documentation-only reconciliation.

## Validation status

- Edited files were manually checked for internal consistency.
- No code, tests, dependencies, UI or export/download behavior were changed.

## GitHub Actions status

- Not required unless documentation checks run automatically.

## Hugging Face sync status

- Not functionally relevant; no app behavior changed.

## App verification status

- Not applicable; no UI behavior changed.

## Remaining risks

- WP18 is now clearly identified as the next possible workpackage, but it must still receive explicit coordinator approval before implementation starts.
- Future workers must not treat WP18 as implicitly approved.

## Next recommended step

`WP18 — PDF text extraction to restored TXT UI implementation`

WP18 may only start after explicit coordinator approval as a separate implementation workpackage.

Required PDF boundaries to preserve:

- no restored PDF output;
- no OCR;
- no PDF-to-DOCX reconstruction;
- no cloud PDF conversion;
- no AI-based extraction;
- no layout preservation promises;
- no batch PDF processing;
- no real-data PDF test cases;
- no automatic PDF rehydration.
