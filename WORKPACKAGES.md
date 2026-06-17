# SolidPrivacy Scrub — Workpackages

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Repository: `solidprivacy-nl/scrub`.

## Required workpackage claim check

Before starting implementation or documentation changes, check:

```text
workpackage_claims/
```

If a claim file for the same workpackage exists with status `in_progress`, stop and report that another worker has already claimed the package.

If no claim exists, create a new claim file before changing code, tests, UI, export, schema or shared documentation. Use `GitHub.create_file` so a duplicate claim fails instead of silently overwriting another worker.

When done, update the same claim file to `completed` and include the final commit/PR, handover path, tests/checks and next step.

## Current status

```text
WP28C — completed after Actions/HF/app verification for Scrub Key warning/reinsert acknowledgement UI.
WP35-WP39 — DOCX hygiene line completed through clean-DOCX export policy.
WP39D — completed after Actions/HF/app verification; DOCX hygiene audit UI is report-only and app-verified.
WP_REVIEW_HIGHLIGHT_TOGGLE_IMPLEMENTATION — completed after Actions/HF/app verification.
WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK_VERIFY — completed after Actions/HF/app verification; hidden replacement helper panel closeout completed.
WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION — completed after Actions/HF/app verification; first bounded source/processed side-by-side review surface is live.
WP_SIDE_BY_SIDE_REVIEW_HEIGHT_FIX — completed after Actions/HF/app verification; equal-height side-by-side panes with local processed-pane scrolling are live.
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_PROTOTYPE — completed isolated prototype-only concept and visually approved by coordinator.
WP_SIDE_BY_SIDE_REVIEW_SYNC_SCROLL_IMPLEMENTATION — completed after later app verification evidence; synchronized scrolling remains active by default.
WP_SIDE_BY_SIDE_REVIEW_CONSOLIDATION_DUTCH_SAMPLE — completed after later app verification evidence; one central side-by-side review is live with Dutch synthetic legal demo text.
WP_REVIEW_SURFACE_CONTROL_CLEANUP — completed after later Actions/HF/app verification evidence; markers default on, marker label shortened, visible sync-scroll checkbox removed.
WP_REVIEW_SURFACE_CONTROL_CLEANUP_TEST_REPAIR — completed after Actions/HF verification; stale assertions repaired after marker/sync-control cleanup.
WP_REVIEW_SURFACE_DUPLICATE_HEADING_CLEANUP — completed after Actions/HF/app verification by coordinator screenshot evidence; duplicate internal `Controleer de tekst` heading removed from the central side-by-side component.
WP_REVIEW_TABLE_COLLAPSIBLE_CONTRACT_TESTS — completed after Actions/HF verification.
WP_REVIEW_TABLE_COLLAPSIBLE_CANDIDATE_FILE — completed as inactive candidate file, later promoted and removed by cleanup.
WP_REVIEW_TABLE_COLLAPSIBLE_PROMOTE_VERIFY — completed after promotion/app verification; normal app flow now shows `Vervangtabel controleren — <items> items` as collapsed review-table section.
WP_REVIEW_TABLE_COLLAPSIBLE_ARTIFACT_CLEANUP — completed; temporary candidate/helper artifacts removed after verified promotion.
WP_DUTCH_LEGAL_RECALL_GAP_TESTS — completed; tests-only baseline for known Dutch legal recall gaps.
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES — completed; targeted candidate-scanner pattern fixes for Dutch legal references.
WP_DUTCH_LEGAL_RECALL_PATTERN_FIXES_VERIFY — completed after coordinator Actions/HF/app verification evidence.
WP_RECALL_SCORECARD_REFRESH — completed; recall/precision scorecard refreshed after Dutch legal recall fixes.
WP_RECALL_GOLD_LABEL_CORPUS_SEED — completed; synthetic gold-label corpus seed added for future recall/precision benchmarking.
WP_RECALL_GOLD_LABEL_CORPUS_EXPAND — completed; synthetic gold-label corpus expanded for future recall/precision benchmarking.
WP_RECALL_BENCHMARK_RUNNER_MINIMAL — completed; minimal diagnostic recall/precision runner added for synthetic gold-label corpus.
WP_RECALL_BENCHMARK_RUNNER_EMAIL_DOMAIN_TEST_FIX — completed and coordinator-verified; corpus email-domain validator domain handling repaired after Actions failure.
WP_RECALL_BENCHMARK_REPORT_ARTIFACT — completed and coordinator-verified; diagnostic recall benchmark report helper, workflow and artifact documentation added.
WP_RECALL_BENCHMARK_REPORT_REVIEW — completed; first diagnostic report artifact reviewed and follow-up recommendation recorded.
WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX — completed; diagnostic report mapping/counting cleanup added.
WP_SERIAL_REVIEW_UI — completed and app-verified after Actions/sync verification.
```

## Active product line

```text
Import -> Scrub -> Review -> Replace -> Scrub Key -> Reinsert -> Export -> Audit
```

## Review UX / frontend status

The working baseline remains:

```text
table-first review table = source of truth and fallback
```

The normal app now uses:

```text
1. Voeg document of tekst toe
2. Controleer de tekst: one central side-by-side review surface
3. Controleer gevonden gegevens: review guidance remains visible, while the editable replacement table sits inside the collapsed `Vervangtabel controleren — <items> items` section
4. Serial review / extra review aids
5. Download opgeschoonde bestanden
```

The central review surface keeps:

- a single outer step heading: `2. Controleer de tekst`;
- no duplicate internal `Controleer de tekst` heading inside the side-by-side component;
- brontekst left;
- verwerkte/gecontroleerde tekst right;
- synchronized scrolling as default behavior;
- no visible sync-scroll checkbox;
- visual markers default on;
- review table as source of truth and fallback.

The promoted collapsible review table keeps:

- `3. Controleer gevonden gegevens` visible in the normal app flow;
- the editable `replacement_editor` table under `Vervangtabel controleren — <items> items`;
- collapsed default state with `expanded=False`;
- `include`, `remember`, `find`, `replace_with` controls;
- Dutch labels `Meenemen`, `Onthouden`, `Gevonden tekst`, `Vervangen door`;
- export/download labels unchanged;
- DOCX hygiene audit remains visible.

Temporary candidate/helper artifacts no longer remain in the active repository after cleanup:

- `presidio_streamlit_collapsible_candidate.py` removed;
- `tests/test_review_table_collapsible_candidate_file.py` removed;
- `review_table_collapsible_ui.py` removed.

## Recall/benchmark status

- Dutch legal recall pattern fixes improve review-candidate visibility only; they are not a complete automatic-recognition guarantee.
- Gold-label corpus contains 4 legal source documents and 3 care source documents with `.gold.json` sidecars.
- `tests/test_recall_gold_label_corpus_seed.py` validates sidecar JSON, source paths, offsets, labels, preserve terms and `@example.test` email domains.
- `recall_benchmark_runner.py` loads sidecars, collects recognizer/candidate-scanner predictions when available and reports diagnostic exact/text-normalized/overlap matches.
- `tests/test_recall_benchmark_runner_minimal.py` covers runner loading, normalization, mapping cleanup, deduplication, matching, preserve term hits, known trap hits and JSON-serializable corpus smoke reports.
- `RECALL_BENCHMARK_RUNNER_MINIMAL.md` documents the diagnostic runner and its limitations.
- `recall_benchmark_report.py` writes a diagnostic JSON report and Markdown summary to an explicit output directory.
- `.github/workflows/recall-benchmark-report.yml` generates and uploads `diagnostic-recall-benchmark-report` as a GitHub Actions artifact.
- `tests/test_recall_benchmark_report_artifact.py` covers report metadata, Markdown summary, file writing, no-threshold behavior and CLI smoke output.
- `RECALL_BENCHMARK_REPORT_ARTIFACT.md` documents artifact usage and non-claim boundaries.
- `RECALL_BENCHMARK_REPORT_REVIEW.md` reviews the first artifact output.
- `RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.md` documents the mapping/counting cleanup.

Diagnostic cleanup added:

```text
NL_ADDRESS -> ADDRESS
NL_IBAN -> IBAN
NL_CASE_REFERENCE -> CASE_NUMBER
NL_LEGAL_PARTY_NAME -> PERSON
EMAIL_ADDRESS -> EMAIL
ZORG-CL-* care references accept NL_CLIENT_REFERENCE where appropriate
care department/location labels accept NL_ADDRESS where appropriate
benchmark-only email predictions use source benchmark_builtin
prediction accounting dedupes repeated predictions by text/entity/start/end/source
```

Boundaries:

- This is benchmark/report mapping only.
- No product recognizers changed.
- No candidate scanner changed.
- No app behavior changed.
- No thresholds or production gate added.

## Verification evidence

- Promotion branch used by coordinator: `test/collapsible-review-table`.
- Promotion commit: `15f5173c893668566e9d62524ef4d0b5449f37b8` — `Promote collapsible review table candidate`.
- GitHub Actions: `Tests #1074` completed successfully for the promotion commit.
- Coordinator local checks before artifact cleanup:
  - `python -m py_compile presidio_streamlit.py`
  - `python -m pytest -q tests/test_review_table_collapsible_candidate_file.py` — 5 passed before that temporary candidate-file test was removed
  - `python -m pytest -q tests/test_review_table_collapsible_contract.py` — 11 passed
  - `python -m pytest -q tests/test_side_by_side_review_ui_patch.py` — 15 passed
  - `python -m pytest -q tests/test_side_by_side_review_consolidation_dutch_sample.py` — 7 passed
  - `python -m pytest -q tests` — 545 passed
- Coordinator app screenshot confirmed the live app starts and shows the collapsed `Vervangtabel controleren — 16 items` section with side-by-side review, serial review, export/download and DOCX hygiene audit still visible.
- Recall pattern verification coordinator evidence:
  - `Tests #1115` for commit `e1e44b3` completed successfully.
  - `Sync to Hugging Face Space #1116` for commit `e1e44b3` completed successfully.
  - Hugging Face app screenshot shows the Space running without Script execution error.
- Email-domain validator final repair coordinator evidence:
  - `222ebb8` — Tests green.
  - `8c84523` — Tests green / HF sync green.
  - `927a564` — Tests green / HF sync green.
- Diagnostic recall benchmark report artifact coordinator evidence:
  - `a3df5c7` — `Diagnostic recall benchmark report #1` green.
  - `31ee53b` — `Tests #1193` green.
  - `31ee53b` — `Sync to Hugging Face Space #1204` green.
  - Hugging Face app screenshot shows the Space running without Script execution error.
- First artifact review used uploaded `recall_benchmark_report.json` and `recall_benchmark_summary.md` from `diagnostic-recall-benchmark-report`.
- Diagnostic report artifact fix is pending Actions/HF/artifact verification.

Boundaries preserved:

- review table remains source of truth and fallback;
- no replacement behavior change;
- no Scrub Key change;
- no export/download change;
- no reinsert change;
- no dependency change;
- no cloud processing;
- no real data;
- no production threshold or blocking gate.

## Active / next recommended execution queue

```text
1. Do not start a new feature automatically.
2. First verify Tests, Sync to Hugging Face Space and Diagnostic recall benchmark report workflow for WP_RECALL_BENCHMARK_REPORT_ARTIFACT_FIX.
3. Then review the cleaned artifact output with WP_RECALL_BENCHMARK_REPORT_REVIEW_2 after separate approval.
4. Do not start threshold planning yet.
5. Only after cleaned artifact review, consider WP_RECALL_BENCHMARK_THRESHOLDS_PLAN.
6. If document/export risks now dominate, consider WP_DOCX_HYGIENE_RECALL_FOLLOWUP after separate approval.
```

## Blocked work

Do not start yet without separate approval:

```text
new replacement UI implementation
mutating replacement decision implementation
automatic replacement
additional Dutch legal recognizer/pattern rounds
Scrub Key writes
export blocking
click-to-mark
advanced editor
full-document marking
clean DOCX export blocking
DOCX cleaner/removal
production recall/precision gate
```

Also blocked until separate approval or later specs:

- Scrub Key encryption implementation.
- Scrub Key JSON schema migration.
- Placeholder migration.
- Robust placeholder generation in product flow.
- DOCX comment/tracked-change removal.
- Restored PDF output.
- OCR.
- Cloud document processing.
- MSI implementation.
- Broad document-centric Streamlit UI rewrite.
- Separate frontend migration.
- Professional document editor implementation.
- Static highlight preview startup source mutation.
