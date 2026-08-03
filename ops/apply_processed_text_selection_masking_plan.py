from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-08-03 23:42 Europe/Amsterdam"


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


def append_once(path: str, marker: str, entry: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if marker in text:
        raise RuntimeError(f"Entry already present in {path}: {marker}")
    target.write_text(text.rstrip() + "\n\n" + entry.rstrip() + "\n", encoding="utf-8")


replace_once(
    "ROADMAP.md",
    "Last roadmap strategy update: 2026-08-03 — Zorgfilter v1 is approved as an evidence-driven profile line; policy and synthetic corpus work may proceed while recognizer and UI integration remain sequential and test-gated.",
    "Last roadmap strategy update: 2026-08-03 — Zorgfilter v1 is app-verified, and direct selection-driven correction in the processed-text pane is recorded as a candidate review-UX line; implementation remains sequential, test-gated and subject to explicit coordinator approval.",
)
replace_once(
    "ROADMAP.md",
    "Recall/benchmark work is reopened only where the synthetic validation matrix exposes a concrete false-negative, misclassification or over-masking gap.",
    '''### Candidate document-centric manual-correction line

Direct usability evidence supports a future correction path in the main processed-text pane:

```text
select an unmasked value
→ right-click
→ choose a masking type
→ add through the existing manual replacement path
```

The recommended first version is bounded to all exact occurrences of the selected value. It must create a normal document-scoped manual row, keep the replacement table authoritative and preserve current bound export, Scrub Key and reinsert semantics. Occurrence-specific replacement, a rich editor and a combined Streamlit upgrade are excluded.

The proposed sequence is:

```text
1. SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT
2. SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL
3. SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE
4. SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION
5. SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION
6. SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY
```

This candidate line does not displace the active Phase 6 queue. No implementation package starts until the coordinator explicitly approves the plan and contract scope.

Recall/benchmark work is reopened only where the synthetic validation matrix exposes a concrete false-negative, misclassification or over-masking gap.''',
)

prepend_once(
    "WORKPACKAGES.md",
    "SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN

Status: completed as planning; GitHub Actions pending.

Goal:
- Determine whether an unmasked value can be selected in `Verwerkte tekst`, classified through a right-click menu and safely added through the existing manual replacement path.

Planning result:

```text
Technically feasible: yes
Recommended component: bidirectional Streamlit v1 custom component
Current static components.html mutation-capable: no
First scope: all exact occurrences only
Only selected occurrence: deferred; requires span-aware architecture
Review table source of truth: preserved
Existing manual form fallback: preserved
Export/Scrub Key/reinsert semantics: unchanged
Implementation authorized: no
```

Files added:
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `tests/test_processed_text_selection_masking_plan.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_plan.md`
- `handover/workpackages/20260803_2342_processed_text_selection_masking_plan.md`

Files changed:
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`

Proposed implementation sequence:
1. `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT`
2. `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL`
3. `SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE`
4. `SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION`
5. `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION`
6. `SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY`

Boundaries:
- planning and documentation only;
- no Streamlit UI, component, helper, dependency or runtime change;
- no occurrence-specific replacement;
- no recognizer, export, Scrub Key, reinsert or cloud-processing change;
- implementation requires explicit coordinator approval after discussion.
''',
)

prepend_once(
    "CHANGELOG.md",
    "SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN",
    f'''## {TIMESTAMP} — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN

Status: completed as planning; validation pending.

Purpose:
- Assess a document-centric path for correcting missed sensitive values directly from the processed-text pane.

Files added:
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `tests/test_processed_text_selection_masking_plan.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_plan.md`
- `handover/workpackages/20260803_2342_processed_text_selection_masking_plan.md`

Files changed:
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`

Planning result:
- confirmed that the current static `components.html` pane cannot return a supported mutation event;
- recommended a bounded bidirectional Streamlit v1 custom component on the current Streamlit 1.39 stack;
- routed accepted actions through server-side validation and the existing `build_manual_mask_row` path;
- kept the review table authoritative and the manual form available as fallback;
- limited version one to all exact occurrences and deferred occurrence-specific masking to a separate span-aware architecture line;
- defined quick type choices, occurrence-impact warnings, collision blocking, event replay/stale-view protection, scroll restoration, undo, accessibility, XSS and no-external-network requirements;
- defined six sequential test-first implementation workpackages.

Validation:
- documentation/architecture contract tests added;
- full GitHub Actions pending;
- Hugging Face sync not functionally relevant;
- app verification not applicable because no product behavior changed.

Intentionally not changed:
- `presidio_streamlit.py`, side-by-side renderer or manual mask helper;
- Streamlit/dependency versions or Docker runtime;
- replacement table, export, Scrub Key or reinsert semantics;
- recognizers, profiles, cloud processing or product claims.
''',
)

replace_once(
    "RISK_REGISTER.md",
    "Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, PERSON-name diagnostic/contract/helper work, planning-only threshold policy and a verified simple manual missed-value entry that adds user-supplied values to the existing replacement table.",
    "Current mitigations include human review, review guidance, diagnostic recall benchmark artifacts, PERSON-name diagnostic/contract/helper work, planning-only threshold policy and a verified simple manual missed-value entry that adds user-supplied values to the existing replacement table. A selection-driven processed-text correction path is now specified as a candidate usability mitigation, but it remains planning-only and may not bypass server validation or the authoritative replacement table.",
)
replace_once(
    "RISK_REGISTER.md",
    "- `WP_MVP_FAST_MANUAL_MASK_ENTRY` adds a verified simple user-facing path to add missed values to the existing replacement table.",
    "- `WP_MVP_FAST_MANUAL_MASK_ENTRY` adds a verified simple user-facing path to add missed values to the existing replacement table.\n- `SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN` specifies a possible select/right-click/type route into the same manual row path, with the table retained as source of truth and implementation still gated.",
)
replace_once(
    "RISK_REGISTER.md",
    "- Additional copy polish may still be needed, but it should remain separate and small.",
    "- Additional copy polish may still be needed, but it should remain separate and small.\n- The proposed in-text selection interaction requires a bidirectional custom component, exact-occurrence impact disclosure, embedded-substring collision guards, replay/stale-event protection and a manual-form rollback path before it can be promoted.",
)
replace_once(
    "RISK_REGISTER.md",
    "- The verified manual missed-value entry is intentionally placed in the primary review path because it directly supports faster anonymization.",
    "- The verified manual missed-value entry is intentionally placed in the primary review path because it directly supports faster anonymization.\n- A future selection-driven route may reduce navigation friction, but every accepted action must still become a visible normal replacement-table row and must not mutate export or Scrub Key state directly from the browser component.",
)

append_once(
    "SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md",
    "## 14. 2026-08-03 planning clarification — selection-driven manual correction",
    '''## 14. 2026-08-03 planning clarification — selection-driven manual correction

The earlier `no click-to-mark` boundary applied to the completed first side-by-side review phase. It prevented a fragile mutation mechanism from being added before the read-only comparison surface and manual correction path were stable.

Direct user evidence now supports evaluating a separate bounded interaction:

```text
select an unmasked value in Verwerkte tekst
→ right-click
→ choose a masking type
→ add a normal manual row
```

The companion `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md` specifies the only recommended first-version direction:

- bidirectional component event, not parent-DOM or query-parameter hacks;
- server-authoritative validation;
- all exact occurrences only;
- existing document-scoped manual row and bound placeholder path;
- replacement table remains source of truth and fallback;
- manual form remains available;
- no occurrence-specific model, rich editor, Streamlit upgrade, export, Scrub Key or reinsert change;
- implementation requires explicit coordinator approval and sequential contract/action-model/component/integration packages.

This clarification records a candidate next direction. It does not authorize UI implementation and does not retroactively change the safety boundaries of the completed side-by-side package.
''',
)

replace_once(
    "workpackage_claims/scrub_wp_processed_text_selection_masking_plan.md",
    "Status: in_progress",
    "Status: completed as planning; GitHub Actions pending",
)
