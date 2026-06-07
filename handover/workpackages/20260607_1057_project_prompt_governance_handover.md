# Handover — Project prompt and governance setup

Repository: solidprivacy-nl/scrub  
Status: completed / pending latest Actions confirmation

## Summary

This session established the central governance model for SolidPrivacy Scrub and prepared the project for clean continuation in a fresh chat. The repository now has a full project prompt, a short project prompt for ChatGPT Project Instructions, a central roadmap, a workpackage execution plan, and a handover directory convention.

The current product direction is:

```text
Scrub → Review → Scrub Key → AI → Reinsert → Export → Audit
```

The immediate development line remains v12 Review UX, followed by v13 Scrub Key / Reinsert.

## Repository worked in

- `solidprivacy-nl/scrub`

## Workpackage title

- Project prompt and governance setup
- Related active development line: v12 Review UX

## Work completed before this handover

### v12 Review UX status

- v12.1 Review table status model: completed and user-confirmed.
- v12.2 Review focus filters: completed and GitHub/Hugging Face verified.
- v12.3 Review table simplification: completed and user-confirmed after pandas Index bugfix.
- v12.4 Review guidance text: implemented and user visually confirmed in the app.

### Governance files added

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `PROJECT_PROMPT.md`
- `PROJECT_PROMPT_SHORT.md`

### Handover system established

Workers must write handovers to:

```text
handover/workpackages/
```

Filename format:

```text
handover/workpackages/YYYYMMDD_HHMM_<workpackage_slug>.md
```

This file is the first handover written under that convention.

## Files added

- `PROJECT_PROMPT.md`
- `PROJECT_PROMPT_SHORT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `review_guidance.py`
- `tests/test_review_guidance.py`
- `handover/workpackages/20260607_1057_project_prompt_governance_handover.md`

## Files changed

- `fix_streamlit_nested_expanders.py`
- `WORKPACKAGES.md`

Earlier in the same v12 line, the following files were also added or changed:

- `review_status.py`
- `tests/test_review_status.py`
- `review_filters.py`
- `tests/test_review_filters.py`
- `review_table_config.py`
- `tests/test_review_table_config.py`
- `CHANGELOG.md`

## Tests

Added/updated in this phase:

- `tests/test_review_guidance.py`

Relevant earlier tests in the v12 line:

- `tests/test_review_status.py`
- `tests/test_review_filters.py`
- `tests/test_review_table_config.py`

## Validation status

- GitHub Actions for `Add executable workpackage plan`: green, confirmed by user.
- GitHub to Hugging Face sync for `Add executable workpackage plan`: green, confirmed by user.
- v12.4 app guidance was visually confirmed by user in Hugging Face.
- Latest governance commits `PROJECT_PROMPT.md`, `PROJECT_PROMPT_SHORT.md`, `WORKPACKAGES.md`, and this handover still need final Actions/sync confirmation if not already visible in GitHub Actions.

## GitHub Actions status

Known green:

- Tests #29 for commit `2a3a229`.

Pending/unknown at handover time:

- Actions for commits after `2a3a229`, including project prompt and handover commits.

## Hugging Face sync status

Known green:

- Sync to Hugging Face Space #43 for commit `2a3a229`.

Pending/unknown at handover time:

- Sync for commits after `2a3a229`, including project prompt and handover commits.

## App verification status

Confirmed by user:

- v12.3 simplified review table works.
- v12.4 guidance block appears correctly in the app.
- Review step now shows guidance, explanation expander, focus filter, technical details expander, and simplified table.

## Remaining risks

- `fix_streamlit_nested_expanders.py` is carrying multiple staged UI patches. Future UI work should be sequential and careful.
- `CHANGELOG.md` may need a final update for `PROJECT_PROMPT.md`, `PROJECT_PROMPT_SHORT.md`, and `WORKPACKAGES.md` governance additions if not yet recorded.
- Latest Actions/sync status after this handover should be checked before continuing implementation.
- v12.5 and v12.6 should reuse helper modules and tests before UI integration.

## Next recommended step

1. Confirm latest GitHub Actions and Hugging Face sync after this handover commit.
2. Update `CHANGELOG.md` if governance additions are not yet logged.
3. Continue with `WP2 — v12.5 Final review summary`.
4. Prepare helper module first:
   - `review_summary.py`
   - `tests/test_review_summary.py`
5. Only after tests pass, integrate the summary into the UI above the download/export section.

## Required fresh-chat start sequence

The next worker should start by reading, in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Then continue from `WORKPACKAGES.md`, not from memory.
