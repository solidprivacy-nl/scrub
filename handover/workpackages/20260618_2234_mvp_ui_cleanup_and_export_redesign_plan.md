# Handover — WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN — Plan MVP interface cleanup and professional export/download flow`

Status: completed as planning/design/specification-only.

## Summary

Created a concrete MVP UI cleanup and export/download redesign plan.

The plan temporarily parks new recall/benchmark follow-up packages unless a concrete blocker appears, and moves the active next direction toward visible product polish: calmer interface, professional export/download grouping and secondary audit/advanced layers for technical details.

No product UI was implemented in this package.

## Files added

- `MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md`
- `handover/workpackages/20260618_2234_mvp_ui_cleanup_and_export_redesign_plan.md`
- `workpackage_claims/WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md`

## Files changed

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/WP_MVP_UI_CLEANUP_AND_EXPORT_REDESIGN_PLAN.md` pending final claim closeout update after this handover file

## Product-code changes

None.

## Streamlit code changes

None.

No changes were made to:

- `presidio_streamlit.py`
- `serial_review_panel_ui.py`
- `fix_streamlit_nested_expanders.py`

## Export semantics changes

None.

No filenames, MIME types, payloads, export eligibility, Scrub Key contents or report contents were changed.

## Scrub Key/reinsert changes

None.

## Recognizer/benchmark changes

None.

## Tests/checks run

No pytest was required because this package is planning/design-only.

`git diff --check` was not runnable in this connector-only environment.

## Validation status

Completed by documentation review and planning against:

- active roadmap/product direction;
- current workpackage queue;
- side-by-side review UX direction;
- replacement UI redesign plan;
- risk register;
- current Streamlit export/review structure inspected read-only.

## GitHub Actions status

Pending/unknown at handover time.

## Hugging Face sync status

Pending/unknown at handover time.

## App verification status

Not required. No app behavior changed.

## Summary of UI/export plan

Planned target information architecture:

```text
1. Document toevoegen
2. Gegevens controleren
3. Export kiezen
4. Audit en risico’s bekijken
```

First implementation should keep numbering low-risk and start with:

```text
5. Exporteer resultaat
```

Target export grouping:

```text
Document downloaden
- Opgeschoonde tekst (.txt)
- Word-document (.docx)
- PDF (.pdf)

Scrub Key
- Separate warning and separate download

Audit en technische bestanden
- Vervangtabel (.csv)
- Scrubrapport (.txt)
- DOCX hygiene audit
- Geavanceerde technische informatie
```

Debug/audit details should move to secondary layers, not disappear.

Recommended copy changes include:

```text
Serial review — experimentele reviewhulp -> Stap voor stap controleren
Download opgeschoonde bestanden -> Exporteer resultaat
Technische details bij de vervangtabel -> Geavanceerde details bij de vervangtabel
Technische herkenningen -> Geavanceerde herkenningsdetails
```

## Remaining risks

- UI/export redesign is planned but not implemented.
- Current app still shows prototype/debug-like labels until follow-up implementation packages run.
- Export/download buttons are still functionally separate until redesigned.
- Audit details must remain available during cleanup.
- Scrub Key must remain visibly sensitive and separate from normal document exports.
- Human review remains necessary.

## Next recommended step

Recommended next package after separate coordinator approval:

```text
WP_EXPORT_DOWNLOAD_UX_CONTRACT_TESTS
```

Then:

```text
WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_IMPLEMENTATION
WP_REVIEW_COPY_POLISH_IMPLEMENTATION
WP_MVP_UI_APP_VERIFICATION_CLOSEOUT
```

Do not start follow-up work automatically.
