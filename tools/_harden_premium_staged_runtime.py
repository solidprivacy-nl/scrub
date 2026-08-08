from pathlib import Path
import ast

path = Path("presidio_streamlit.py")
text = path.read_text(encoding="utf-8")

old_imports = '''from premium_streamlit_state import (
    get_core_flow_state,
    mark_processing_complete,
    mark_review_complete,
    processing_generation,
    set_stage_summary,
    synchronize_processing_generation,
    synchronize_shell_choices,
)
'''
new_imports = '''from premium_streamlit_state import (
    cache_analysis_results,
    get_cached_analysis_results,
    get_core_flow_state,
    mark_processing_complete,
    mark_review_complete,
    processing_generation,
    set_stage_summary,
    synchronize_processing_generation,
    synchronize_shell_choices,
)
'''
if old_imports not in text:
    raise SystemExit("premium state import block not found")
text = text.replace(old_imports, new_imports, 1)

old_analysis = '''    analyzer_load_state = st.info("Herkenningsengine starten...")
    analyzer = analyzer_engine(*analyzer_params)
    analyzer_load_state.empty()

    st_analyze_results = analyze(
        *analyzer_params,
        text=st_text,
        entities=st_entities,
        language="en",
        score_threshold=st_threshold,
        return_decision_process=st_return_decision_process,
        allow_list=st_allow_list,
        deny_list=st_deny_list,
    )
    st_analyze_results = resolve_configured_analysis_results(
        st_recognition_profile,
        st_analyze_results,
    )
'''
new_analysis = '''    cached_analysis_results = None
    if is_premium_standard and not stage_is_active(premium_state, Stage.ADD):
        cached_analysis_results = get_cached_analysis_results(
            st.session_state, current_processing_generation
        )

    if cached_analysis_results is not None:
        st_analyze_results = cached_analysis_results
    else:
        analyzer_load_state = st.info("Herkenningsengine starten...")
        analyzer = analyzer_engine(*analyzer_params)
        analyzer_load_state.empty()

        st_analyze_results = analyze(
            *analyzer_params,
            text=st_text,
            entities=st_entities,
            language="en",
            score_threshold=st_threshold,
            return_decision_process=st_return_decision_process,
            allow_list=st_allow_list,
            deny_list=st_deny_list,
        )
        st_analyze_results = resolve_configured_analysis_results(
            st_recognition_profile,
            st_analyze_results,
        )
        if is_premium_standard:
            cache_analysis_results(
                st.session_state,
                current_processing_generation,
                st_analyze_results,
            )
'''
if old_analysis not in text:
    raise SystemExit("analysis block not found")
text = text.replace(old_analysis, new_analysis, 1)

old_df = '''        replacement_editor_df = pd.DataFrame(default_editor_rows)

        if is_premium_standard:
            render_stage_header(premium_state, Stage.REVIEW)
'''
new_df = '''        replacement_editor_df = pd.DataFrame(default_editor_rows)
        if is_premium_standard and stage_is_active(premium_state, Stage.REVIEW):
            cached_review_rows = st.session_state.get("_premium_cached_review_rows")
            if isinstance(cached_review_rows, list) and cached_review_rows:
                cached_review_df = pd.DataFrame(cached_review_rows)
                if "find" in cached_review_df.columns and "find" in replacement_editor_df.columns:
                    cached_find_values = {
                        safe_cell(value) for value in cached_review_df["find"].tolist()
                    }
                    new_rows_df = replacement_editor_df[
                        ~replacement_editor_df["find"].map(safe_cell).isin(cached_find_values)
                    ]
                    replacement_editor_df = pd.concat(
                        [cached_review_df, new_rows_df], ignore_index=True
                    )
                else:
                    replacement_editor_df = cached_review_df

        if is_premium_standard:
            render_stage_header(premium_state, Stage.REVIEW)
'''
if old_df not in text:
    raise SystemExit("review dataframe marker not found")
text = text.replace(old_df, new_df, 1)

old_editor_end = '''                    key="replacement_editor",
                )

            if is_expert_review:
'''
new_editor_end = '''                    key="replacement_editor",
                )
                if is_premium_standard:
                    st.session_state["_premium_cached_review_rows"] = (
                        edited_replacements_df.to_dict("records")
                    )

            if is_expert_review:
'''
if old_editor_end not in text:
    raise SystemExit("review editor end marker not found")
text = text.replace(old_editor_end, new_editor_end, 1)

path.write_text(text, encoding="utf-8")
ast.parse(text)
Path("tools/_harden_premium_staged_runtime.py").unlink()
Path(".github/workflows/premium-staged-runtime-hardening.yml").unlink()
