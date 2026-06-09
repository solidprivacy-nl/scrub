# Handover — WP16C Roadmap status reconciliation after v13.8 and PDF helper line

Repository: solidprivacy-nl/scrub  
Status: completed documentation-only update

## Summary

Updated the project documentation to align the roadmap with the current implementation state after v13.8, WP15 and WP16/WP16-FIX.

The roadmap no longer presents v12 as the current active line or v13 as only a future strategic phase. It now records that v12 Review UX is completed, v13 Scrub Key/Reinsert is implemented through pasted-text, TXT and DOCX reinsert, WP15 is completed as PDF reliability review, and WP16/WP16-FIX delivered a helper-only text-based PDF extraction path to restored TXT output.

The roadmap now identifies WP16B as the next closeout step and WP17 as a future planning-only step for PDF text extraction reinsert UI.

## Files added

- `handover/workpackages/20260609_0030_roadmap_status_reconciliation.md`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- No tests added or changed.
- Tests not run; not applicable for documentation-only update.

## Validation

- GitHub Actions: not required unless documentation checks run.
- Hugging Face sync: not functionally relevant; no app behavior changed.
- App verification: not applicable; no UI behavior changed.

## Notes / risks

- This workpackage did not close WP16/WP16-FIX. It only recorded coordinator green evidence and aligned roadmap status.
- WP16B is still required as formal verification closeout before moving to WP17.
- No code, UI, tests, dependencies, OCR, PDF output, AI/cloud behavior, export semantics or Scrub Key import/export behavior were changed.

## Next recommended step

- WP16B — Text-based PDF extraction helper spike verification and closeout.
