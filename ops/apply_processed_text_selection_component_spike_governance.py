from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-08-04 01:00 Europe/Amsterdam"


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match in {path}, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend_once(path: str, marker: str, entry: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if marker in text:
        raise RuntimeError(f"Entry already present in {path}: {marker}")
    target.write_text(entry.rstrip() + "\n\n" + text, encoding="utf-8")


replace_once(
    "PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md",
    "Status: approved contract; pure action model implemented and test-gated",
    "Status: approved contract; action model and non-mutating component spike implemented and test-gated",
)
replace_once(
    "PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md",
    "The action model is implemented in `selection_mask_action.py` and passed the full adversarial regression. The next permitted package is the non-mutating component spike; table or Streamlit integration remains prohibited until that proof is green.",
    "The action model is implemented in `selection_mask_action.py`, and the isolated Streamlit v1 component spike proves UTF-16 selection transport, accessible menu behavior and bidirectional inspect/commit intents without product mutation. The next permitted package is sequential table integration; the review table, manual fallback and unchanged export/Scrub Key/reinsert semantics remain mandatory.",
)

replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-04 — the all-exact processed-text selection contract and pure server-authoritative action model are complete; the next gated step is a non-mutating browser-component spike before any review-table or Streamlit integration.",
    "Last roadmap strategy update: 2026-08-04 — the all-exact contract, pure action model and isolated non-mutating Streamlit component spike are complete; the next gated step is sequential production table integration with rollback, synchronization and live app verification requirements.",
)
replace_once(
    "ROADMAP.md",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract and Streamlit-free action-model packages are complete. The next permitted package is a non-mutating component spike that must prove rendering, UTF-16 offset transport, menu accessibility and replay-safe bidirectional events before any table or `presidio_streamlit.py` integration. This line remains sequential and does not displace the active Phase 6 queue.",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract, Streamlit-free action model and isolated non-mutating component spike are complete. The next permitted package is sequential production integration with the existing document-scoped manual-row state and authoritative review table. It must preserve the static/manual rollback path, export/Scrub Key/reinsert semantics, and require GitHub Actions, Hugging Face synchronization and live app verification. This line remains sequential and does not displace the active Phase 6 queue.",
)

prepend_once(
    "WORKPACKAGES.md",
    "## 2026-08-04 01:00 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE

Status: completed; technical validation green.

Dependency:
- action model merged through PR #61 as `3e0e5be9457654d3dfb6e52e0e701a08b438a4d9`.

Goal:
- Prove a local bidirectional Streamlit v1 component can transport safe processed-text selections and server inspection results without mutating production state.

Implementation result:

```text
Local Streamlit v1 wrapper: implemented
Local dependency-free frontend assets: implemented
Python-codepoint → UTF-16 highlight conversion: implemented
Selection offsets across plain/marked nodes: implemented
Synchronized scroll: implemented
Right-click + Shift+F10 + ContextMenu + visible fallback: implemented
Accessible menu and ARIA status: implemented
inspect_selection event: implemented
Server inspection result display: implemented
commit_manual_mask intent: implemented
Actual commit/table mutation: deliberately absent
Production renderer integration: absent
External assets/network/storage/telemetry: absent
```

Files added:
- `processed_text_selection_component.py`
- `processed_text_selection_component_spike_demo.py`
- `frontend/processed_text_selection_component/`
- `tests/test_processed_text_selection_component_spike.py`
- `tests/frontend/processed_text_selection_component_core.test.js`
- `PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE.md`
- `workpackage_claims/scrub_wp_processed_text_selection_component_spike.md`
- `handover/workpackages/20260804_0100_processed_text_selection_component_spike.md`

Files changed:
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Validation:
- standard run #1977: 1126 tests passed in 13.83s;
- dedicated Streamlit 1.39 smoke run #1979: 1126 tests passed in 13.79s;
- AppTest: no script exceptions;
- local server health: `ok`;
- root HTML and startup log checks: passed;
- final clean standard regression pending after governance/workflow restoration.

Next permitted package:
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`

Boundaries:
- no production UI or replacement-table mutation;
- no export, Scrub Key, reinsert, recognizer or profile change;
- no Streamlit upgrade, new runtime dependency or external asset;
- no occurrence-specific masking.
''',
)

prepend_once(
    "CHANGELOG.md",
    "## 2026-08-04 01:00 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE

Status: completed; technical validation green.

Purpose:
- Prove the browser/component layer before connecting selection events to the production replacement table.

Files added:
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

Files changed:
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`

Implementation:
- local lazy Streamlit Components v1 wrapper on pinned Streamlit 1.39;
- Python code-point highlight validation and conversion to UTF-16 browser offsets;
- safe text-node rendering and marked segments;
- DOM selection offsets across plain and marked text nodes;
- synchronized scrolling and scroll restoration;
- right-click, keyboard and visible selection entry points;
- accessible type/confirmation menu;
- inspect event, server result and commit-intent transport;
- standalone synthetic inspection-only demo;
- no runtime build step, external assets, network, storage or telemetry.

Validation:
- run #1977: 1126 tests passed in 13.83s;
- Streamlit 1.39 smoke run #1979: 1126 tests passed in 13.79s;
- AppTest completed without script exceptions;
- local server health `ok`, root HTML and startup log checks passed;
- final clean standard regression pending.

Intentionally not changed:
- `presidio_streamlit.py` and production side-by-side renderer;
- replacement table, exports, Scrub Key or reinsert;
- recognizers, profiles, dependencies or cloud processing;
- occurrence-specific masking.
''',
)

replace_once(
    "RISK_REGISTER.md",
    "Its frozen contract and pure action model require a two-stage server-authoritative inspect/commit protocol and may not bypass validation or the authoritative replacement table. The model now proves UTF-16 selection validation, exact impact bands, Unicode collision blocking, stale/replay rejection, bound manual-row construction and fail-closed undo without connecting to the UI.",
    "Its frozen contract, pure action model and isolated component spike require a two-stage server-authoritative inspect/commit protocol and may not bypass validation or the authoritative replacement table. The model proves UTF-16 selection validation, impact bands, collision/replay/stale protection and safe row construction; the spike proves local bidirectional event transport, accessible menu behavior and correct offsets around marked nodes without product mutation.",
)
replace_once(
    "RISK_REGISTER.md",
    "- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT` freezes the approved route, and `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL` implements its pure server-authoritative validation and row-construction logic; the table remains source of truth and component/UI integration remains sequentially gated.",
    "- The contract freezes the route, the action model implements server-authoritative validation/row construction, and `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE` proves the isolated browser transport. The review table remains source of truth and production integration remains sequentially gated.",
)
replace_once(
    "RISK_REGISTER.md",
    "- The pure action model now proves exact-occurrence bands, Unicode collision guards, replay/stale-event protection and safe undo. The remaining high-risk gate is a non-mutating component spike proving text-node offsets, accessible menu behavior and replay-safe bidirectional transport before promotion.",
    "- The action model and component spike now prove exact-occurrence bands, Unicode collision guards, replay/stale protection, safe undo, text-node offsets and accessible bidirectional transport. The remaining high-risk gate is production table integration with rollback plus cross-flow and live app verification.",
)

replace_once(
    "workpackage_claims/scrub_wp_processed_text_selection_component_spike.md",
    "Status: in_progress",
    "Status: completed; standard and Streamlit smoke validation green; final clean regression pending",
)
