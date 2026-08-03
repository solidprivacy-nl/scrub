from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-08-04 00:30 Europe/Amsterdam"


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
    "Status: approved implementation contract  ",
    "Status: approved contract; pure action model implemented and test-gated",
)
replace_once(
    "PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md",
    "The action model must remain Streamlit-free and browser-free. A component spike starts only after the pure action model and its adversarial tests are green.",
    "The action model is implemented in `selection_mask_action.py` and passed the full adversarial regression. The next permitted package is the non-mutating component spike; table or Streamlit integration remains prohibited until that proof is green.",
)

replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-04 — direct selection-driven correction in the processed-text pane is approved with an all-exact version-one boundary; the interaction contract is frozen and implementation proceeds sequentially through a pure action model before any browser component or UI integration.",
    "Last roadmap strategy update: 2026-08-04 — the all-exact processed-text selection contract and pure server-authoritative action model are complete; the next gated step is a non-mutating browser-component spike before any review-table or Streamlit integration.",
)
replace_once(
    "ROADMAP.md",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract package is completed as the first gate. The next permitted package is the Streamlit-free and browser-free action model; component and UI work remain sequentially gated and do not displace the active Phase 6 queue.",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract and Streamlit-free action-model packages are complete. The next permitted package is a non-mutating component spike that must prove rendering, UTF-16 offset transport, menu accessibility and replay-safe bidirectional events before any table or `presidio_streamlit.py` integration. This line remains sequential and does not displace the active Phase 6 queue.",
)

prepend_once(
    "WORKPACKAGES.md",
    "## 2026-08-04 00:30 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL

Status: implemented; final clean GitHub Actions regression pending.

Dependency:
- contract package merged through PR #60 as `23cb5d667461f84a01e96ee007b2ef10bd2e6b40`.

Goal:
- Implement a pure Python, Streamlit-free and browser-free action model for the approved two-stage selection masking contract.

Implementation result:

```text
Inspect/commit event parsing: implemented
UTF-16 conversion and split-surrogate rejection: implemented
Selection validity and placeholder blocking: implemented
Exact non-overlapping occurrence count: implemented
Unicode embedded-token collision guard: implemented
Nested replacement conflict guard: implemented
1–5 / 6–20 / >20 impact bands: implemented
Replay history and single-use inspections: implemented
Commit-time source/processed/binding/table revalidation: implemented
Bound manual row adapter: implemented
Stable action ID and one-step undo: implemented
Streamlit/browser integration: not included
```

Files added:
- `selection_mask_action.py`
- `tests/test_selection_mask_action.py`
- `PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL.md`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_action_model.md`
- `handover/workpackages/20260804_0030_processed_text_selection_masking_action_model.md`

Files changed:
- `manual_mask_entry.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

Validation:
- initial run #1957 exposed one missing local event-ID assignment and one overly literal source-text assertion;
- corrected run #1961: 1106 tests passed in 10.66s;
- final clean regression pending after governance updates.

Next permitted package:
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE`

Boundaries:
- no Streamlit/session-state or browser component;
- no `presidio_streamlit.py`, review-table, export, Scrub Key or reinsert change;
- no occurrence-specific replacement or dependency upgrade.
''',
)

prepend_once(
    "CHANGELOG.md",
    "## 2026-08-04 00:30 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL

Status: implemented; final clean validation pending.

Purpose:
- Implement the server-authoritative selection action model before any browser or Streamlit integration.

Files added:
- `selection_mask_action.py`
- `tests/test_selection_mask_action.py`
- `PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL.md`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_action_model.md`
- `handover/workpackages/20260804_0030_processed_text_selection_masking_action_model.md`

Files changed:
- `manual_mask_entry.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`

Implementation:
- strict schema/action/event/scope/hash/payload parsing;
- exact UTF-16-to-Python index conversion and surrogate-pair rejection;
- quick-selection length, line, control, placeholder and marked-range checks;
- exact occurrence and Unicode-aware embedded-token analysis;
- duplicate and nested included-replacement collision guards;
- ready, confirmation-required and blocked inspection results;
- bounded replay state and opaque single-use inspections;
- commit-time revalidation of document, binding, source, processed text, replacement table and impact;
- existing document-bound manual-row construction for eight internal quick types;
- stable manual action records and fail-closed undo.

Validation:
- initial run #1957 failed from one local event-ID assignment defect and one overly literal test; no safety boundary was weakened;
- corrected run #1961: 1106 tests passed in 10.66s;
- final clean standard regression pending.

Intentionally not changed:
- visible manual form options;
- Streamlit, browser component or session state;
- review-table and export/download flows;
- Scrub Key, reinsert, recognizers, profiles or cloud processing;
- occurrence-specific masking or dependencies.
''',
)

replace_once(
    "RISK_REGISTER.md",
    "Its frozen contract requires a two-stage server-authoritative inspect/commit protocol and may not bypass validation or the authoritative replacement table.",
    "Its frozen contract and pure action model require a two-stage server-authoritative inspect/commit protocol and may not bypass validation or the authoritative replacement table. The model now proves UTF-16 selection validation, exact impact bands, Unicode collision blocking, stale/replay rejection, bound manual-row construction and fail-closed undo without connecting to the UI.",
)
replace_once(
    "RISK_REGISTER.md",
    "- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT` freezes the approved select/right-click/type route into the same manual row path, with the table retained as source of truth and component/UI integration still sequentially gated.",
    "- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT` freezes the approved route, and `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL` implements its pure server-authoritative validation and row-construction logic; the table remains source of truth and component/UI integration remains sequentially gated.",
)
replace_once(
    "RISK_REGISTER.md",
    "- The approved in-text selection interaction now has frozen exact-occurrence bands, collision guards, replay/stale-event protection and rollback requirements; the pure action model and non-mutating component spike must prove these boundaries before promotion.",
    "- The pure action model now proves exact-occurrence bands, Unicode collision guards, replay/stale-event protection and safe undo. The remaining high-risk gate is a non-mutating component spike proving text-node offsets, accessible menu behavior and replay-safe bidirectional transport before promotion.",
)
replace_once(
    "workpackage_claims/scrub_wp_processed_text_selection_masking_action_model.md",
    "Status: in_progress",
    "Status: implemented; corrected GitHub Actions run green; final clean regression pending",
)
