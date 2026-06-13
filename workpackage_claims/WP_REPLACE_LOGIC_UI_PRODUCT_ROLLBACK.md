# Workpackage claim — WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK

status: completed
repository: solidprivacy-nl/scrub
workpackage title: WP_REPLACE_LOGIC_UI_PRODUCT_ROLLBACK — Hide non-intuitive replacement helper panel from main UI
started timestamp: 2026-06-13T15:25:00+02:00
completed timestamp: 2026-06-13T15:25:00+02:00
coordinator feedback: Replacement decision helper works technically, but is not intuitive/user-friendly and makes the workflow more complex.
scope: Hide/remove the replacement decision helper panel from the normal Scrub Legal user flow while preserving helper and contract work for later redesign.

final commit SHA or PR link: edff443d093a72bdec9cc5964181f3164cbf46a0
handover path: handover/workpackages/20260613_1525_replace_logic_ui_product_rollback.md
tests/checks: Updated `tests/test_replace_logic_ui_patch.py`. No shell/pytest/py_compile execution available through ChatGPT GitHub connector. Expected checks: `python -m py_compile presidio_streamlit.py`; `python -m py_compile serial_review_panel_ui.py`; `pytest tests/test_replace_logic_ui_patch.py`; `pytest tests/test_replace_logic_ui_contract.py tests/test_replacement_decision.py`; full `pytest`.
GitHub Actions status: Unknown at claim completion time; verify CI for final rollback commit.
Hugging Face sync status: Unknown at claim completion time; verify sync after Actions.
app verification status: Pending and required because UI/runtime behavior changed.
next recommended step: Verify Actions/sync and request app screenshot. Later: WP_REPLACE_LOGIC_UI_REDESIGN_PLAN only after separate coordinator approval.
