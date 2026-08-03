# Handover — SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: Prove the non-mutating processed-text selection component  
Status: implemented; governance closeout and final clean regression pending

## Summary

Implemented an isolated, local, bidirectional Streamlit Components v1 spike for direct text selection in `Verwerkte tekst`.

The proof provides:

- source and processed panes;
- server-supplied highlight spans;
- explicit Python-codepoint to browser UTF-16 conversion;
- exact DOM selection offsets across plain and `<mark>` text nodes;
- synchronized percentage-based scrolling;
- right-click, Shift+F10, Context Menu key and visible `Masker selectie` entry points;
- accessible custom menu navigation and ARIA feedback;
- bounded `inspect_selection` event transport;
- server inspection result display;
- bounded `commit_manual_mask` intent transport;
- standalone synthetic demo using the real inspect action model.

The spike remains non-mutating. The demo never imports or calls `commit_manual_mask`, never creates a replacement row and is not imported by the production app.

## Files added

- `processed_text_selection_component.py`
- `processed_text_selection_component_spike_demo.py`
- `frontend/processed_text_selection_component/index.html`
- `frontend/processed_text_selection_component/styles.css`
- `frontend/processed_text_selection_component/streamlit_bridge.js`
- `frontend/processed_text_selection_component/component_core.js`
- `frontend/processed_text_selection_component/component.js`
- `frontend/processed_text_selection_component/NOTICE.md`
- `tests/test_processed_text_selection_component_spike.py`
- `tests/frontend/processed_text_selection_component_core.test.js`
- `PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE.md`
- `workpackage_claims/scrub_wp_processed_text_selection_component_spike.md`
- `handover/workpackages/20260804_0100_processed_text_selection_component_spike.md`

## Files changed

- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

No production UI file is changed.

## Tests

Python tests cover:

- local assets and lazy Streamlit import;
- Python-to-UTF-16 highlight conversion, including an emoji before a mark;
- invalid, overlapping and out-of-range spans;
- JSON component arguments and non-mutating boundaries;
- no production imports;
- demo inspection-only behavior;
- no external network, browser persistence, unsafe HTML or dynamic-code path;
- minimal Streamlit v1 protocol messages;
- accessible context-menu and keyboard behavior;
- stale inspection-result protection.

Dependency-free Node tests cover:

- UTF-16 boundaries and surrogate-pair rejection;
- marked/plain segmentation;
- offsets after marked nodes;
- whitespace-adjusted selections;
- marked-range intersections;
- inspect and commit-intent event envelopes;
- scroll synchronization math and viewport clamping.

## Validation status

- Initial standard PR run #1977: **1126 tests passed in 13.83s**.
- Dedicated Streamlit 1.39 smoke run #1979:
  - **1126 tests passed in 13.79s**;
  - `streamlit.testing.v1.AppTest` completed without script exceptions;
  - local headless server started successfully;
  - `_stcore/health` returned `ok`;
  - root application HTML and startup log checks passed.
- Governance closeout and final standard regression: pending.
- Hugging Face sync: not functionally relevant because the production app does not import the spike.
- App verification: not applicable because the production UI is unchanged.

## GitHub Actions status

Green on standard run #1977 and dedicated Streamlit smoke run #1979. Final clean standard run pending after workflow restoration and governance closeout.

## Hugging Face sync status

Not functionally relevant in this isolated spike.

## App verification status

Not applicable. No production renderer, review table or main Streamlit flow is changed.

## Remaining risks

- The spike does not yet add rows to the production replacement table.
- Browser behavior still requires live verification in Edge, Chrome and Firefox after production integration.
- Streamlit rerun/focus behavior must be verified in the deployed app after the integration package.
- The integration must retain the static renderer and manual form as rollback/fallback until cross-flow and app verification are green.
- Export, Scrub Key and reinsert must be tested after a real selection-created row.
- Occurrence-specific masking remains out of scope.

## Next recommended step

After merge, claim:

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION
```

This will be the first production UI mutation package. It must remain sequential, use the existing action model and document-scoped manual-row state, preserve the review table as source of truth and require GitHub Actions, Hugging Face synchronization and live app verification.
