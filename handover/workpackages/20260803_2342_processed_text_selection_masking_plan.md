# Handover — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN

Repository worked in: `solidprivacy-nl/scrub`  
Workpackage title: Processed-text selection masking feasibility and implementation plan  
Status: completed as planning; GitHub Actions pending

## Summary

Assessed the requested document-centric correction flow:

```text
select unmasked value in Verwerkte tekst
→ right-click
→ choose masking type
→ add through existing manual replacement path
```

The direction is technically feasible and recommended, provided the first version remains `all_exact` only and routes every accepted action through server-side validation, the current document-scoped manual-row helper, the existing replacement table, bound placeholders and the unchanged export/Scrub Key/reinsert paths.

The current `components.html` renderer is static and cannot return mutation events. The recommended implementation is a small bidirectional Streamlit v1 custom component on the currently pinned Streamlit 1.39 stack. A Streamlit upgrade, rich editor and occurrence-specific replacement are explicitly excluded from the first line.

## Files added

- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `tests/test_processed_text_selection_masking_plan.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_plan.md`
- `handover/workpackages/20260803_2342_processed_text_selection_masking_plan.md`

## Files changed

- `ROADMAP.md` — bounded candidate review-UX line and sequential gate
- `WORKPACKAGES.md` — planning result and proposed implementation sequence
- `CHANGELOG.md` — planning evidence and boundaries
- `RISK_REGISTER.md` — false-negative, interface and audit implications
- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md` — clarification that the earlier no-click boundary applied to the completed phase and is not an implementation authorization for the new proposal

## Tests

Added documentation/architecture contracts covering:

- planning-only status and explicit approval gate;
- review table remains authoritative;
- `all_exact` first-version scope;
- occurrence-specific replacement deferred to a span-aware architecture project;
- bidirectional component and server-authoritative validation;
- no combined Streamlit upgrade;
- grounding in current static component and Streamlit 1.39 lock;
- reuse of `build_manual_mask_row` and document binding;
- collision, replay and stale-event guards;
- no external data path or browser persistence;
- unchanged Scrub Key, export and reinsert semantics;
- six sequential follow-up workpackages.

## Validation status

- GitHub Actions: pending planning PR.
- Hugging Face sync: not functionally relevant; documentation/tests only.
- App verification: not applicable; no UI or runtime behavior changed.

## GitHub Actions status

Pending.

## Hugging Face sync status

Not functionally relevant.

## App verification status

Not applicable.

## Remaining risks

- The decisive technical risk remains reliable text-offset mapping and event handling in a bidirectional browser component around existing highlight nodes.
- The current global string-replacement model can affect embedded substrings; the quick path must block collisions before integration.
- Right-click is not sufficiently discoverable or accessible without keyboard and visible fallbacks.
- A custom menu replaces the native browser menu only for valid selections and must not weaken normal browser behavior elsewhere.
- Occurrence-specific masking remains unresolved and explicitly deferred.
- No implementation is authorized by this plan.

## Next recommended step

Discuss and explicitly approve or amend the eight proposed decisions in `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`. If approved, start only:

```text
SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT
```

Do not start the component or UI integration directly.
