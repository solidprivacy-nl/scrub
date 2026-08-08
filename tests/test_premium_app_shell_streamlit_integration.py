from pathlib import Path
import ast


SOURCE = Path("presidio_streamlit.py").read_text(encoding="utf-8")
SHELL_UI = Path("premium_streamlit_shell_ui.py").read_text(encoding="utf-8")
LEGACY_PATCH = Path("fix_streamlit_nested_expanders.py").read_text(encoding="utf-8")


def test_premium_streamlit_source_remains_syntactically_valid():
    ast.parse(SOURCE)


def test_standard_shell_is_global_and_sidebar_starts_collapsed():
    assert 'initial_sidebar_state="collapsed"' in SOURCE
    assert '["Anonimiseren", "Terugzetten"]' in SOURCE
    assert '["Standaard", "Expert"]' in SOURCE
    assert 'if premium_workflow is Workflow.REINSERT:' in SOURCE
    assert 'if is_premium_expert:\n    st.sidebar.header(APP_TITLE)' in SOURCE


def test_standard_uses_three_persistent_stage_headers_without_routed_pages():
    assert 'render_stage_header(premium_state, Stage.ADD)' in SOURCE
    assert 'render_stage_header(premium_state, Stage.REVIEW)' in SOURCE
    assert 'render_stage_header(premium_state, Stage.DOWNLOAD)' in SOURCE
    assert 'st.switch_page' not in SOURCE
    assert 'st.Page(' not in SOURCE
    assert 'st.navigation(' not in SOURCE
    assert 'with st.container(border=True):' in SHELL_UI
    assert 'st.expander' not in SHELL_UI


def test_standard_processing_and_review_actions_drive_auto_progression():
    assert '"Document verwerken"' in SOURCE
    assert 'mark_processing_complete(' in SOURCE
    assert '"Controle afronden"' in SOURCE
    assert 'mark_review_complete(st.session_state)' in SOURCE
    assert 'synchronize_processing_generation(' in SOURCE


def test_non_active_standard_stage_content_is_cached_not_rendered_in_parallel():
    assert 'show_add_workspace = is_premium_expert or stage_is_active(premium_state, Stage.ADD)' in SOURCE
    assert 'show_review_workspace = is_premium_expert or stage_is_active(premium_state, Stage.REVIEW)' in SOURCE
    assert '_premium_cached_review_rows' in SOURCE
    assert 'render_stage_header(premium_state, Stage.DOWNLOAD)\n            st.stop()' in SOURCE


def test_standard_stage_navigation_reuses_current_generation_analysis_instead_of_reprocessing():
    assert 'get_cached_analysis_results(' in SOURCE
    assert 'cache_analysis_results(' in SOURCE
    assert 'if cached_analysis_results is not None:' in SOURCE
    assert 'if is_premium_standard and not stage_is_active(premium_state, Stage.ADD):' in SOURCE


def test_review_reopen_uses_cached_authoritative_rows_and_requires_recompletion():
    assert 'cached_review_rows = st.session_state.get("_premium_cached_review_rows")' in SOURCE
    assert 'edited_replacements_df.to_dict("records")' in SOURCE
    assert 'mark_review_complete(st.session_state)' in SOURCE


def test_standard_never_silently_rewrites_expert_only_operator_choice():
    assert 'if not standard_operator_is_supported(st_operator):' in SOURCE
    assert 'Standaard wijzigt deze Expert-instelling niet automatisch.' in SOURCE
    guard_start = SOURCE.index('if not standard_operator_is_supported(st_operator):')
    guard_end = SOURCE.index('st_threshold_default =', guard_start)
    guard_block = SOURCE[guard_start:guard_end]
    assert 'st_operator =' not in guard_block
    assert 'st.stop()' in guard_block


def test_legacy_runtime_patch_cannot_reinject_retired_form_ui_into_premium_source():
    assert 'if "premium_streamlit_shell_ui" in text:' in LEGACY_PATCH
    assert 'raise SystemExit(0)' in LEGACY_PATCH


def test_existing_export_and_scrub_key_payload_contracts_are_not_rewritten():
    assert 'file_name="opgeschoonde_tekst.txt"' in SOURCE
    assert 'mime="text/plain"' in SOURCE
    assert 'file_name="solidprivacy_scrub_key.json"' in SOURCE
    assert 'mime="application/json"' in SOURCE
    assert 'build_bound_scrub_key(' in SOURCE
    assert 'validate_bound_scrub_key(scrub_key)' in SOURCE
