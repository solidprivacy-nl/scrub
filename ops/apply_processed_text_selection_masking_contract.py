from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-08-04 00:09 Europe/Amsterdam"


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one match in {path}, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend_once(path: str, marker: str, entry: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if marker in text:
        raise RuntimeError(f"Entry already present in {path}: {marker}")
    target.write_text(entry.rstrip() + "\n\n" + text, encoding="utf-8")


replace_once(
    "PROCESSED_TEXT_SELECTION_MASKING_PLAN.md",
    "Status: planning and discussion only  ",
    "Status: approved product direction; implementation contract frozen  ",
)
replace_once(
    "PROCESSED_TEXT_SELECTION_MASKING_PLAN.md",
    "This plan does not authorize implementation. It creates a bounded workpackage sequence for discussion and explicit approval.",
    "The coordinator approved this direction at 2026-08-04 00:09 Europe/Amsterdam, including the all-exact version-one boundary. `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md` now freezes the two-stage inspect/commit protocol and authorizes only the pure action-model package next.",
)

replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-03 — Zorgfilter v1 is app-verified, and direct selection-driven correction in the processed-text pane is recorded as a candidate review-UX line; implementation remains sequential, test-gated and subject to explicit coordinator approval.",
    "Last roadmap strategy update: 2026-08-04 — direct selection-driven correction in the processed-text pane is approved with an all-exact version-one boundary; the interaction contract is frozen and implementation proceeds sequentially through a pure action model before any browser component or UI integration.",
)
replace_once(
    "ROADMAP.md",
    "This candidate line does not displace the active Phase 6 queue. No implementation package starts until the coordinator explicitly approves the plan and contract scope.",
    "The coordinator approved the direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam. The contract package is completed as the first gate. The next permitted package is the Streamlit-free and browser-free action model; component and UI work remain sequentially gated and do not displace the active Phase 6 queue.",
)

prepend_once(
    "WORKPACKAGES.md",
    "SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT

Status: implemented; GitHub Actions pending.

Approval evidence:
- coordinator/user approved the proposed direction and all-exact version-one boundary at 2026-08-04 00:09 Europe/Amsterdam.

Goal:
- Freeze the exact interaction, event, safety, privacy and sequencing contract before action-model or component implementation.

Contract result:

```text
Protocol: inspect_selection → server impact result → commit_manual_mask
Scope: all exact occurrences only
1–5 safe occurrences: ready
6–20 safe occurrences: explicit confirmation required
>20 occurrences: blocked from quick path
Selection maximum: 160 Unicode code points, one line
Offset unit: UTF-16 code units
Payload maximum: 8192 UTF-8 bytes
Replay history: 128 event IDs per document
Quick types: 8 stable machine keys
Embedded/nested/marked collisions: fail closed
Review table source of truth: preserved
Manual form fallback: preserved
Export/Scrub Key/reinsert semantics: unchanged
```

Files added:
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `test_cases/processed_text_selection_masking/contract.json`
- `tests/test_processed_text_selection_masking_contract.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_contract.md`
- `handover/workpackages/20260804_0009_processed_text_selection_masking_contract.md`

Files changed:
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Next permitted package:
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL`

Boundaries:
- specification and contract tests only;
- no runtime, Streamlit, browser component, review-table or export-flow change;
- no occurrence-specific replacement or Streamlit upgrade;
- no Scrub Key, reinsert, recognizer, profile or cloud-processing change.
''',
)

prepend_once(
    "CHANGELOG.md",
    "SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT

Status: implemented; validation pending.

Purpose:
- Convert the approved processed-text selection direction into an exact implementation contract before product code changes.

Files added:
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `test_cases/processed_text_selection_masking/contract.json`
- `tests/test_processed_text_selection_masking_contract.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_contract.md`
- `handover/workpackages/20260804_0009_processed_text_selection_masking_contract.md`

Files changed:
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Contract result:
- froze a two-stage `inspect_selection` / `commit_manual_mask` protocol so occurrence impact is server-derived before commitment;
- froze all-exact scope, UTF-16 offset semantics and strict stale/replay handling;
- froze 1–5 ready, 6–20 confirmation-required and >20 blocked impact bands;
- froze 160-code-point single-line selections and an 8192-byte payload cap;
- froze eight broad quick types with server-owned entity and placeholder mappings;
- froze embedded-substring, nested replacement and marked-range collision blocking;
- froze visible, right-click and keyboard access plus one-step undo behavior;
- froze no-network, no-browser-persistence, escaped-rendering and fail-closed boundaries;
- authorized only the pure action-model package next.

Validation:
- machine-readable contract fixture and contract tests added;
- full GitHub Actions pending;
- Hugging Face sync not functionally relevant;
- app verification not applicable because no runtime behavior changed.

Intentionally not changed:
- `manual_mask_entry.py`, `presidio_streamlit.py` or side-by-side renderer;
- Streamlit/dependency versions or Docker runtime;
- review table, export, Scrub Key or reinsert semantics;
- recognizers, profiles, cloud processing or product claims.
''',
)

replace_once(
    "RISK_REGISTER.md",
    "A selection-driven processed-text correction path is now specified as a candidate usability mitigation, but it remains planning-only and may not bypass server validation or the authoritative replacement table.",
    "A selection-driven processed-text correction path is approved with an all-exact version-one boundary. Its frozen contract requires a two-stage server-authoritative inspect/commit protocol and may not bypass validation or the authoritative replacement table.",
)
replace_once(
    "RISK_REGISTER.md",
    "- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN` specifies a possible select/right-click/type route into the same manual row path, with the table retained as source of truth and implementation still gated.",
    "- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT` freezes the approved select/right-click/type route into the same manual row path, with the table retained as source of truth and component/UI integration still sequentially gated.",
)
replace_once(
    "RISK_REGISTER.md",
    "- The proposed in-text selection interaction requires a bidirectional custom component, exact-occurrence impact disclosure, embedded-substring collision guards, replay/stale-event protection and a manual-form rollback path before it can be promoted.",
    "- The approved in-text selection interaction now has frozen exact-occurrence bands, collision guards, replay/stale-event protection and rollback requirements; the pure action model and non-mutating component spike must prove these boundaries before promotion.",
)
replace_once(
    "RISK_REGISTER.md",
    "- A future selection-driven route may reduce navigation friction, but every accepted action must still become a visible normal replacement-table row and must not mutate export or Scrub Key state directly from the browser component.",
    "- The approved selection-driven route may reduce navigation friction, but every accepted action must still become a visible normal replacement-table row and must not mutate export or Scrub Key state directly from the browser component.",
)

prepend_once(
    "DECISION_LOG.md",
    "D040 — Use a two-stage server-authoritative protocol for direct masking from processed text",
    '''## 2026-08-04 — D040 — Use a two-stage server-authoritative protocol for direct masking from processed text

Status: accepted product, UX and implementation-sequence decision

Decision:

```text
Allow a user to select an unmasked value in Verwerkte tekst, invoke a right-click or visible/keyboard masking action, inspect the server-validated exact-occurrence impact, choose a broad type and create one normal manual replacement row. Version one masks all safe exact occurrences only.
```

Protocol:

```text
inspect_selection
→ server validates UTF-16 offsets, text, document scope, processed hash, collisions and occurrence count
→ ready / confirmation_required / blocked inspection result
→ commit_manual_mask with a current single-use inspection ID
→ server revalidates and creates the bound manual row
```

Safety boundaries:
- one to five safe exact occurrences are ready;
- six to twenty require explicit confirmation;
- more than twenty are blocked from the quick path;
- embedded substrings, nested included replacement terms, marked-range intersections, duplicates, stale views and replays fail closed;
- the review table remains source of truth and `Gemiste waarde toevoegen` remains fallback;
- browser code never creates placeholders, mutates the table, writes a Scrub Key or builds an export;
- no external assets, telemetry, browser persistence or cloud processing;
- no occurrence-specific replacement, rich editor or Streamlit upgrade in this line.

Reason:
- direct correction where a false negative is noticed reduces navigation friction and copying mistakes;
- a server-derived impact step is required because browser-supplied counts and types are untrusted;
- all-exact behavior matches current replacement/export/Scrub Key/reinsert semantics;
- occurrence-specific behavior would require a separate span-aware architecture.

Approved sequence:
1. `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT`
2. `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL`
3. `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE`
4. `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`
5. `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`
6. `SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY`

Evidence:
- coordinator/user approval at 2026-08-04 00:09 Europe/Amsterdam;
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`;
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`;
- `test_cases/processed_text_selection_masking/contract.json`.
''',
)

replace_once(
    "workpackage_claims/scrub_wp_processed_text_selection_masking_contract.md",
    "Status: in_progress",
    "Status: implemented; GitHub Actions pending",
)
