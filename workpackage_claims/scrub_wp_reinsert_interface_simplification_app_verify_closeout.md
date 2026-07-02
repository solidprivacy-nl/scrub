# Workpackage Claim — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Repository: solidprivacy-nl/scrub

Status: blocked; awaiting coordinator live app verification

Start timestamp: 2026-07-02 00:00 UTC

## Workpackage title

SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_APP_VERIFY_CLOSEOUT — Verify and close out simplified reinsert interface

## Scope

Verification/closeout-only. No product code, UI, reinsert helper, Scrub Key, export/download, recognizer, benchmark, runtime/startup or dependency changes.

## Decision recorded

Keep SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION. Do not revert. Treat it as product-desired but pending live verification/closeout.

## Repository evidence checked

- PR #7 merged.
- Targeted tests recorded.
- Full-suite evidence recorded.
- Safety boundaries recorded as preserved.
- Direct-source reinsert UI source includes the four-step flow and warning/acknowledgement gates.

## Validation policy

Budget-aware validation. No new GitHub Actions were manually triggered. No tests were rerun because this closeout is documentation/verification-only and no product code changed.

## Blocking condition

Live Hugging Face app verification by the coordinator is still required before marking this package completed.

## Required live app verification checklist

1. Open “Originele waarden terugzetten”.
2. Confirm the visible flow is simplified into four steps:
   - Voeg Scrub Key toe
   - Voeg tekst of document toe
   - Controleer herstelrapport
   - Download herstelde output
3. Confirm Scrub Key warning and acknowledgement gate are still visible.
4. Test pasted-text reinsert with synthetic data.
5. Test TXT reinsert with synthetic data if practical.
6. Test DOCX reinsert with synthetic data if practical.
7. Confirm restored filenames/downloads still make sense.
8. Confirm no restored-PDF/OCR/document-reconstruction promise appears.
9. Confirm no Script execution error appears.

## Handover path

handover/workpackages/20260702_0000_reinsert_interface_simplification_app_verify_closeout.md

## Next recommended step

Coordinator performs live app verification with synthetic data. If it passes, run a documentation-only closeout update. If it fails, create a narrow FIX workpackage based on the exact failed behavior.
