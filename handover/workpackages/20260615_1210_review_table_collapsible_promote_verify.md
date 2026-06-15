# Handover — WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY — Verify promoted collapsible review table in live app`

Status: completed; promoted collapsible review table verified and documented.

## Files added

- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY.md`
- `handover/workpackages/20260615_1210_review_table_collapsible_promote_verify.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY.md`

No product code was changed in this verification package.

## Verification performed

Checked active `presidio_streamlit.py` and confirmed it contains:

- `st.subheader("3. Controleer gevonden gegevens")`
- `Vervangtabel controleren`
- `expanded=False`
- `key="replacement_editor"`
- `include`
- `remember`
- `find`
- `replace_with`
- `Meenemen`
- `Onthouden`
- `Gevonden tekst`
- `Vervangen door`

Confirmed export/download labels remain present:

- `Download opgeschoonde tekst (.txt)`
- `Download vervangtabel (.csv)`
- `Download scrubrapport (.txt)`
- `Download opgeschoond Word-bestand (.docx)`
- `Download opgeschoonde PDF (.pdf)`

Confirmed the promoted app keeps:

- `2. Controleer de tekst` heading;
- side-by-side review;
- `Markeringen tonen`;
- no duplicate `Controleer de tekst` heading;
- `3. Controleer gevonden gegevens` heading;
- collapsed `Vervangtabel controleren — <items> items` review table section;
- serial review;
- export/download;
- DOCX hygiene audit.

## Evidence recorded

Branch used by coordinator:

```text
test/collapsible-review-table
```

Promotion commit:

```text
15f5173c893668566e9d62524ef4d0b5449f37b8 — Promote collapsible review table candidate
```

GitHub Actions:

```text
Tests #1074 — completed successfully for promotion commit 15f5173c893668566e9d62524ef4d0b5449f37b8
```

Coordinator local checks:

```text
python -m py_compile presidio_streamlit.py
python -m pytest -q tests/test_review_table_collapsible_candidate_file.py  # 5 passed
python -m pytest -q tests/test_review_table_collapsible_contract.py        # 11 passed
python -m pytest -q tests/test_side_by_side_review_ui_patch.py             # 15 passed
python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py  # 7 passed
python -m pytest -q tests                                                   # 545 passed
```

Coordinator app verification:

- live app starts without Script execution error;
- screenshot shows `Vervangtabel controleren — 16 items` collapsed;
- review table is not directly open;
- step 3 remains visible;
- export/download and DOCX hygiene audit remain visible.

## Tests/checks run

No shell/pytest execution was available through the ChatGPT GitHub connector.

Checks were verified from coordinator-provided local test evidence plus GitHub Actions lookup for the promotion commit.

## Validation status

Completed/app-verified.

## GitHub Actions status

Green for the promotion commit via `Tests #1074`.

## Hugging Face sync status

Verified by coordinator live-app screenshot evidence. The connector did not expose a separate sync workflow for the promotion commit, but the live Hugging Face app screenshot demonstrates the promoted UI reached the app.

## App verification status

Completed by coordinator screenshot evidence.

## Remaining risks

- The review table remains the source of truth and fallback; the collapsed state reduces visual weight but does not reduce the need for human review.
- Serial review remains visible and may still be visually heavy; make it compacter/collapsible only after separate coordinator approval.
- No click-to-mark, advanced editor or full-document marking has been approved or implemented.

## Next recommended step

Do not start a new feature automatically.

Possible next directions only after separate coordinator approval:

- make Serial review compacter/collapsible;
- or freeze review UX temporarily and return to detection/recall issues.
