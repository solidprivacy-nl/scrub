from pathlib import Path


SOURCE = Path("presidio_streamlit.py").read_text(encoding="utf-8")


def test_expert_profile_operator_and_threshold_hydrate_from_persisted_processing_state():
    assert 'stored_profile_label(' in SOURCE
    assert 'stored_operator_value(' in SOURCE
    assert 'stored_threshold(' in SOURCE
    assert 'key="premium_profile_expert_widget"' in SOURCE
    assert 'key="premium_operator_expert_widget"' in SOURCE
    assert 'key="premium_threshold_expert_widget"' in SOURCE
    assert '"Controlemodus",\n        list(PROFILE_OPTIONS.keys()),\n        index=1,' not in SOURCE


def test_standard_profile_widget_is_rehydrated_when_returning_from_expert():
    assert 'entering_standard = presentation_mode_changed and is_premium_standard' in SOURCE
    assert 'st.session_state["premium_profile_standard_widget"] = profile_label' in SOURCE


def test_entity_and_analyzer_settings_hydrate_in_expert():
    assert 'stored_entities(' in SOURCE
    assert 'st.session_state["premium_entities_expert_widget"] = list(entity_defaults)' in SOURCE
    assert 'stored_analyzer_params(' in SOURCE
    assert 'analyzer_model_label(' in SOURCE
    assert 'stored_string_list(st.session_state, ALLOW_LIST_KEY)' in SOURCE
    assert 'stored_string_list(st.session_state, DENY_LIST_KEY)' in SOURCE


def test_processing_generation_is_synchronized_in_both_presentation_modes():
    sync_call = 'premium_state, processing_inputs_changed = synchronize_processing_generation('
    assert sync_call in SOURCE
    sync_position = SOURCE.index(sync_call)
    standard_action_position = SOURCE.index('if is_premium_standard and st_operator not in ("highlight", "synthesize"):')
    assert sync_position < standard_action_position
    assert 'if processing_inputs_changed:\n        st.session_state.pop("_premium_cached_review_rows", None)' in SOURCE


def test_processing_settings_are_persisted_from_expert_without_silent_standard_coercion():
    assert 'persist_processing_settings(' in SOURCE
    assert 'profile_label=profile_label' in SOURCE
    assert 'operator=st_operator' in SOURCE
    assert 'threshold=st_threshold' in SOURCE
    assert 'entities=st_entities' in SOURCE
    assert 'allow_list=st_allow_list' in SOURCE
    assert 'deny_list=st_deny_list' in SOURCE
    assert 'analyzer_params=analyzer_params' in SOURCE
