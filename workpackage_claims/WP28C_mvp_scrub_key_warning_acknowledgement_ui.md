# Workpackage claim — WP28C MVP Scrub Key warning/acknowledgement UI implementation

Repository: `solidprivacy-nl/scrub`

Workpackage: `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`

Status: `in_progress`

Claimed by: `ChatGPT webinterface worker`

Claim created: `2026-06-12`

Scope:

- Implement MVP Scrub Key warning and acknowledgement placements from `SCRUB_KEY_WARNING_IMPLEMENTATION_PLAN.md`.
- Preserve exported JSON content, import behavior, reinsert behavior and file download semantics after acknowledgement.

Expected high-risk files/flows:

- `fix_streamlit_nested_expanders.py`
- `tests/test_scrub_key_ui_patch.py`
- `tests/test_two_mode_ui_patch.py`
- `tests/test_txt_reinsert_ui_patch.py`
- `tests/test_docx_reinsert_ui_patch.py`
- Scrub Key export/import/reinsert UI flow
- restored output download flow

Do not parallel edit:

- `fix_streamlit_nested_expanders.py`
- review table flow
- export/download flow
- Scrub Key import/reload flow
- reinsert/download flow

Completion update:

When WP28C is finished, update this file to `completed` and add the final commit or PR, handover path, tests/checks run, validation status, remaining risks and next recommended step.
