from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match in {path}, found {count}: {old[:120]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


replace_once(
    "presidio_streamlit.py",
    '''from manual_mask_entry import (
    MANUAL_MASK_TYPE_OPTIONS,
    build_manual_mask_row,
    build_manual_placeholder,
    manual_mask_document_key,
    validate_manual_mask_input,
)
''',
    '''from manual_mask_entry import (
    MANUAL_MASK_TYPE_OPTIONS,
    build_manual_mask_row,
    build_manual_placeholder,
    manual_mask_document_key,
    validate_manual_mask_input,
)
from processed_text_selection_integration import (
    handle_selection_component_event,
    latest_selection_action,
    selection_feedback,
    selection_inspection_result,
    selection_scroll_restore,
    undo_latest_selection_action,
)
''',
)

replace_once(
    "presidio_streamlit.py",
    '''        side_by_side_review_state = render_side_by_side_review_panel(
            source_text=st_text,
            edited_replacements_df=replacement_editor_df,
        )
        review_mode = side_by_side_review_state.get("review_mode", "Basiscontrole")
''',
    '''        selection_inspection = selection_inspection_result(
            st.session_state,
            document_scope_key,
        )
        restore_source_scroll, restore_processed_scroll = selection_scroll_restore(
            st.session_state,
            document_scope_key,
        )
        side_by_side_review_state = render_side_by_side_review_panel(
            source_text=st_text,
            edited_replacements_df=replacement_editor_df,
            document_scope_key=document_scope_key,
            inspection_result=selection_inspection,
            restore_source_scroll_ratio=restore_source_scroll,
            restore_processed_scroll_ratio=restore_processed_scroll,
        )

        selection_event = side_by_side_review_state.get("component_event")
        selection_outcome = handle_selection_component_event(
            st.session_state,
            selection_event,
            source_text=st_text,
            processed_text=side_by_side_review_state.get("processed_text", ""),
            document_scope_key=document_scope_key,
            document_binding_id=document_binding_id,
            existing_rows=replacement_editor_df,
            marked_ranges=side_by_side_review_state.get("highlight_spans", ()),
        )
        if selection_outcome.rerun_required:
            st.rerun()

        selection_notice = selection_feedback(st.session_state, document_scope_key)
        selection_notice_level = str(selection_notice.get("level", ""))
        selection_notice_message = str(selection_notice.get("message", ""))
        if selection_notice_message:
            if selection_notice_level == "success":
                st.success(selection_notice_message)
            elif selection_notice_level == "warning":
                st.warning(selection_notice_message)
            else:
                st.info(selection_notice_message)

        if latest_selection_action(st.session_state, document_scope_key) is not None:
            if st.button(
                "Laatste maskering uit tekstselectie ongedaan maken",
                key=f"undo_processed_text_selection_{document_scope_key}",
            ):
                undo_outcome = undo_latest_selection_action(
                    st.session_state,
                    document_scope_key=document_scope_key,
                )
                if undo_outcome.rerun_required:
                    st.rerun()
                if undo_outcome.message:
                    st.warning(undo_outcome.message)

        review_mode = side_by_side_review_state.get("review_mode", "Basiscontrole")
''',
)

replace_once(
    "frontend/processed_text_selection_component/component.js",
    '''  const contextMenu = document.getElementById("contextMenu");
  const statusRegion = document.getElementById("statusRegion");
''',
    '''  const contextMenu = document.getElementById("contextMenu");
  const statusRegion = document.getElementById("statusRegion");
  const componentRoot = document.getElementById("componentRoot");
  const componentFooter = document.getElementById("componentFooter");
''',
)

replace_once(
    "frontend/processed_text_selection_component/component.js",
    '''    statusRegion.textContent = "Maskeringskeuze is als niet-muterend intent-event verstuurd.";
    closeMenu();
    Bridge.setComponentValue(event);
''',
    '''    const contract = currentArgs.component_contract || {};
    statusRegion.textContent = contract.non_mutating_spike
      ? "Maskeringskeuze is als niet-muterend intent-event verstuurd."
      : "Maskering wordt veilig toegevoegd…";
    closeMenu();
    Bridge.setComponentValue(event);
''',
)

replace_once(
    "frontend/processed_text_selection_component/component.js",
    '''    currentArgs = args || {};
    processedText = Core.asText(currentArgs.processed_text);
''',
    '''    currentArgs = args || {};
    const contract = currentArgs.component_contract || {};
    const nonMutatingSpike = Boolean(contract.non_mutating_spike);
    if (componentRoot) {
      componentRoot.setAttribute(
        "aria-label",
        nonMutatingSpike
          ? "Niet-muterende selectiecomponent"
          : "Tekstselectie voor handmatige maskering",
      );
    }
    if (componentFooter) {
      componentFooter.textContent = nonMutatingSpike
        ? "De panelen scrollen samen. Deze componentproef wijzigt geen vervangtabel of document."
        : "De panelen scrollen samen. Maskeringen worden pas na servercontrole toegevoegd.";
    }
    processedText = Core.asText(currentArgs.processed_text);
''',
)
