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

Dutch legal recall pattern fixes improve the review-candidate layer for:

- case-number-shaped values with spaces, such as numeric court role references and `ARN 26/4412`-style references;
- contextual codes near `client`, `cliënt`, `camera`, `incident` and `reparatie` context;
- role-word preservation regression checks through direct helper-level tests.

Recall/precision scorecard now records:

- known Dutch legal reference samples from the baseline;
- CLM/phone-number risk reduction;
- role-word and over-masking protection status;
- review/export boundary coverage;
- gold-label corpus seed and expansion status;
- open benchmark risks: no runner, no formal recall/precision thresholds and no broad production safety claim.

Gold-label corpus now includes:

- `corpus/README.md`;
- 4 legal source documents with `.gold.json` sidecars;
- 3 care source documents with `.gold.json` sidecars;
- `tests/test_recall_gold_label_corpus_seed.py` to validate sidecar JSON, source paths, offsets, labels, preserve terms and `.example.test` email domains;
- legal false-positive traps for articles, dates, times, money, page/attachment labels and exhibit labels;
- care role-preservation and mixed care reference examples.

Verification evidence:

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
- Scorecard/corpus packages added benchmark documentation/data/tests only; no product code or user-facing app behavior changed.

Boundaries preserved:

- review table remains source of truth and fallback;
- no replacement behavior change;
- no Scrub Key change;
- no export/download change;
- no reinsert change;
- no dependency change;
- no cloud processing;
- no real data.

## Active / next recommended execution queue

```text
1. Do not start a new feature automatically.
2. No immediate Dutch legal pattern-fix Round2 is required based on current coordinator verification, scorecard refresh and expanded corpus.
3. If quantitative measurement is now desired, consider WP_RECALL_BENCHMARK_RUNNER_MINIMAL after separate approval.
4. If document/export risks now dominate, consider WP_DOCX_HYGIENE_RECALL_FOLLOWUP after separate approval.
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
