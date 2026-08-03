# Handover — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: Freeze the processed-text selection masking interaction and safety contract  
Status: completed; GitHub Actions green

## Summary

Converted the approved selection-driven correction direction into an exact, machine-readable implementation contract before any runtime or UI mutation.

The contract freezes a two-stage protocol:

```text
inspect_selection
→ server validates selection, counts exact occurrences and classifies impact
→ component shows server-owned count and allowed types
→ commit_manual_mask
→ server revalidates and creates one normal manual replacement row
```

Version one remains `all_exact` only. One to five safe occurrences can be committed directly after type selection, six to twenty require explicit confirmation, and more than twenty are routed to the detailed manual/table path. Embedded substrings, nested replacement terms, marked-range intersections, stale views, replayed events and invalid UTF-16 offsets fail closed.

## Files added

- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `test_cases/processed_text_selection_masking/contract.json`
- `tests/test_processed_text_selection_masking_contract.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_contract.md`
- `handover/workpackages/20260804_0009_processed_text_selection_masking_contract.md`

## Files changed

- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `tests/test_processed_text_selection_masking_plan.py`

## Tests

Added contract tests for:

- approval and `all_exact` scope;
- two-stage inspect/commit actions;
- payload, selection and replay limits;
- event, document-scope and hash formats;
- non-overlapping occurrence thresholds;
- eight stable quick-type mappings;
- manual-selection row semantics;
- embedded/nested/marked collision blocking;
- replay, stale-state and single-use inspections;
- visible and keyboard fallbacks;
- no external network, browser persistence or frontend mutation authority;
- sequential gate to the pure action model only.

Aligned the earlier planning test with the approved contract state after the governance transition.

## Validation status

- Governance operator applied; standard workflow restored and temporary operator removed.
- Clean PR run #1954: **1027 tests passed in 11.48s**.
- The prior clean run #1953 had one stale planning-status assertion while 1026 tests passed; no runtime defect was involved.
- Hugging Face sync: not functionally relevant; specification/tests only.
- App verification: not applicable; no runtime or UI behavior changed.

## GitHub Actions status

Green on run #1954 — 1027 passed in 11.48s. A final status-only PR regression follows this handover update.

## Hugging Face sync status

Not functionally relevant.

## App verification status

Not applicable.

## Remaining risks

- The contract is not yet an implementation.
- UTF-16/Unicode conversion, collision analysis and replay handling must be proven in the pure action model.
- The later browser component must preserve selection state across Streamlit reruns.
- The manual form and review table must remain available through live app verification.
- Occurrence-specific masking remains a separate span-aware architecture project.

## Next recommended step

After merge, claim and implement only:

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL
```

Keep it Streamlit-free and browser-free.
