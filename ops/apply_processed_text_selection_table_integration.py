from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match in {path}, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def insert_after_import(path: str, import_startswith: str, insertion: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if insertion.strip() in text:
        raise RuntimeError(f"Import insertion already present in {path}")
    lines = text.splitlines(keepends=True)
    start = next(
        (index for index, line in enumerate(lines) if line.startswith(import_startswith)),
        None,
    )
    if start is None:
        raise RuntimeError(f"Import anchor not found in {path}: {import_startswith}")
    end = start
    if "(" in lines[start] and ")" not in lines[start]:
        while end + 1 < len(lines):
            end += 1
            if lines[end].lstrip().startswith(")"):
                break
        else:
            raise RuntimeError(f"Unclosed import block in {path}: {import_startswith}")
    lines.insert(end + 1, insertion.rstrip() + "\n")
    target.write_text("".join(lines), encoding="utf-8")


insert_after_import(
    "presidio_streamlit.py",
    "from side_by_side_review_panel_ui import",
    '''from processed_text_selection_integration import (
    clear_selection_feedback,
    handle_selection_component_event,
    latest_selection_action,
    selection_feedback,
    selection_inspection_result,
    selection_scroll_restore,
    undo_latest_selection_action,
)''',
)

replace_once(
    "presidio_streamlit.py",
    '''    side_by_side_state = render_side_by_side_review_panel(
        source_text=st_text,
        edited_replacements_df=replacement_editor_df,
    )
    review_mode = side_by_side_state["review_mode"]
    basic_review_mode = review_mode == BASIC_REVIEW_MODE
''',
    '''    selection_inspection = selection_inspection_result(
        st.session_state,
        document_scope_key,
    )
    restore_source_scroll, restore_processed_scroll = selection_scroll_restore(
        st.session_state,
        document_scope_key,
    )
    side_by_side_state = render_side_by_side_review_panel(
        source_text=st_text,
        edited_replacements_df=replacement_editor_df,
        document_scope_key=document_scope_key,
        inspection_result=selection_inspection,
        restore_source_scroll_ratio=restore_source_scroll,
        restore_processed_scroll_ratio=restore_processed_scroll,
    )
    selection_component_event = side_by_side_state.get("component_event")
    current_selection_feedback = selection_feedback(
        st.session_state,
        document_scope_key,
    )
    if current_selection_feedback:
        feedback_level = str(current_selection_feedback.get("level", "info"))
        feedback_message = str(current_selection_feedback.get("message", ""))
        if feedback_message:
            if feedback_level == "success":
                st.success(feedback_message)
            elif feedback_level == "warning":
                st.warning(feedback_message)
            else:
                st.info(feedback_message)
        clear_selection_feedback(st.session_state, document_scope_key)

    undo_selection_requested = False
    if latest_selection_action(st.session_state, document_scope_key) is not None:
        undo_selection_requested = st.button(
            "Ongedaan maken",
            key=f"processed_text_selection_undo_{document_scope_key}",
            help=(
                "Verwijder alleen de meest recente ongewijzigde maskering die via "
                "een tekstselectie is toegevoegd."
            ),
        )

    review_mode = side_by_side_state["review_mode"]
    basic_review_mode = review_mode == BASIC_REVIEW_MODE
''',
)

replace_once(
    "presidio_streamlit.py",
    '''    save_remembered_replacements(edited_replacements_df)

    serial_review_state = render_serial_review_panel(
''',
    '''    save_remembered_replacements(edited_replacements_df)

    if undo_selection_requested:
        undo_outcome = undo_latest_selection_action(
            st.session_state,
            document_scope_key=document_scope_key,
            current_review_rows=edited_replacements_df,
        )
        if undo_outcome.rerun_required:
            st.rerun()
        if undo_outcome.message:
            st.warning(undo_outcome.message)

    selection_outcome = handle_selection_component_event(
        st.session_state,
        selection_component_event,
        source_text=st_text,
        processed_text=side_by_side_state["processed_text"],
        document_scope_key=document_scope_key,
        document_binding_id=document_binding_id,
        existing_rows=edited_replacements_df,
        marked_ranges=tuple(
            side_by_side_state.get(
                "protected_highlight_spans",
                side_by_side_state.get("highlight_spans", ()),
            )
        ),
    )
    if selection_outcome.rerun_required:
        st.rerun()

    serial_review_state = render_serial_review_panel(
''',
)

replace_once(
    "side_by_side_review_panel_ui.py",
    '''    model = build_side_by_side_review_model(
        source_text=source_text,
        processed_text=processed_text,
        review_rows=edited_replacements_df,
        highlights_enabled=show_markers,
    )
    compact_legend = model["compact_legend"]
    highlight_spans = list(model["processed_pane"]["highlight_spans"])
''',
    '''    model = build_side_by_side_review_model(
        source_text=source_text,
        processed_text=processed_text,
        review_rows=edited_replacements_df,
        highlights_enabled=show_markers,
    )
    protected_model = (
        model
        if show_markers
        else build_side_by_side_review_model(
            source_text=source_text,
            processed_text=processed_text,
            review_rows=edited_replacements_df,
            highlights_enabled=True,
        )
    )
    compact_legend = model["compact_legend"]
    highlight_spans = list(model["processed_pane"]["highlight_spans"])
    protected_highlight_spans = list(
        protected_model["processed_pane"]["highlight_spans"]
    )
''',
)

replace_once(
    "side_by_side_review_panel_ui.py",
    '''        "highlight_spans": highlight_spans,
        "review_mode": review_mode,
''',
    '''        "highlight_spans": highlight_spans,
        "protected_highlight_spans": protected_highlight_spans,
        "review_mode": review_mode,
''',
)
