"""Startup patch for the experimental static highlight preview UI.

WP42D integrates the existing ``highlight_preview.py`` helper as a small
read-only Streamlit preview panel in the anonymization review flow.

The panel is explicitly non-authoritative. It does not mutate review rows,
change export/download behavior, change Scrub Key behavior, change reinsert
behavior, add dependencies, call cloud services or use real-data fixtures.
"""

from __future__ import annotations

from pathlib import Path

APP_FILE = Path(__file__).with_name("presidio_streamlit.py")
text = APP_FILE.read_text(encoding="utf-8")


def replace_once(source: str, old: str, new: str) -> str:
    if old in source and new not in source:
        return source.replace(old, new, 1)
    return source


# Import the pure helper after the existing post-patches have inserted the
# reinsert imports. The fallback keeps the patch safe if the PDF post-patch is
# not present for any reason.
text = replace_once(
    text,
    'from scrub_key_pdf_text_reinsert import reinsert_pdf_text_bytes\n',
    'from scrub_key_pdf_text_reinsert import reinsert_pdf_text_bytes\n'
    'from highlight_preview import build_static_highlight_preview\n',
)

text = replace_once(
    text,
    'from scrub_key_document_reinsert import reinsert_docx_bytes, reinsert_txt_bytes\n',
    'from scrub_key_document_reinsert import reinsert_docx_bytes, reinsert_txt_bytes\n'
    'from highlight_preview import build_static_highlight_preview\n',
)

static_highlight_preview_block = '''        with st.expander("Documentvoorbeeld met markeringen — experimenteel", expanded=False):
            st.caption("Alleen-lezen voorbeeld. De vervangtabel blijft leidend voor beslissingen, Scrub Key en export.")
            st.caption("Deze preview toont maximaal 40 eerste markeringen in kleine tekstfragmenten. Gebruik de vervangtabel voor definitieve controle.")
            highlight_preview_text = st_text or ""
            highlight_preview_spans = []
            highlight_preview_seen_ranges = set()
            highlight_preview_max_text_length = 5000
            highlight_preview_max_spans = 40
            if len(highlight_preview_text) > highlight_preview_max_text_length:
                st.info("Documentvoorbeeld is uitgeschakeld voor lange tekst. Gebruik de vervangtabel voor controle.")
            else:
                for highlight_preview_index, highlight_preview_row in replacement_editor_df.head(highlight_preview_max_spans).iterrows():
                    highlight_preview_find = str(highlight_preview_row.get("find", "")).strip()
                    if not highlight_preview_find:
                        continue
                    highlight_preview_start = highlight_preview_text.find(highlight_preview_find)
                    if highlight_preview_start < 0:
                        continue
                    highlight_preview_end = highlight_preview_start + len(highlight_preview_find)
                    highlight_preview_range = (highlight_preview_start, highlight_preview_end)
                    if highlight_preview_range in highlight_preview_seen_ranges:
                        continue
                    highlight_preview_seen_ranges.add(highlight_preview_range)
                    highlight_preview_source = str(highlight_preview_row.get("source", "")).strip()
                    highlight_preview_status = str(highlight_preview_row.get("review_status", "")).strip()
                    if highlight_preview_source == "candidate":
                        highlight_preview_category = "candidate_missed_value"
                    elif highlight_preview_source == "manual":
                        highlight_preview_category = "manual_added"
                    elif highlight_preview_status in {"needs_review", "candidate"}:
                        highlight_preview_category = "needs_review"
                    else:
                        highlight_preview_category = "confirmed_sensitive"
                    highlight_preview_spans.append({
                        "span_id": f"preview-{highlight_preview_index}",
                        "row_id": str(highlight_preview_index),
                        "start_offset": highlight_preview_start,
                        "end_offset": highlight_preview_end,
                        "label": highlight_preview_find,
                        "category": highlight_preview_category,
                        "entity_type": str(highlight_preview_row.get("entity_type", "")),
                        "status": highlight_preview_status,
                        "source": highlight_preview_source,
                        "replacement_preview": str(highlight_preview_row.get("replace_with", "")),
                        "reason": str(highlight_preview_row.get("reason", "")),
                        "context_before": "",
                        "context_after": "",
                    })
                highlight_preview_result = build_static_highlight_preview(highlight_preview_text, highlight_preview_spans)
                highlight_preview_gate_ok = (
                    highlight_preview_result.get("safe_to_render") is True
                    and highlight_preview_result.get("read_only") is True
                    and highlight_preview_result.get("non_authoritative") is True
                    and highlight_preview_result.get("mutation_allowed") is False
                    and highlight_preview_result.get("export_blocking") is False
                    and highlight_preview_result.get("scrub_key_changes") is False
                )
                if not highlight_preview_spans:
                    st.info("Geen markeringen beschikbaar voor deze kleine preview. Gebruik de vervangtabel voor controle.")
                elif not highlight_preview_gate_ok:
                    st.warning("Niet alle markeringen konden veilig worden getoond. Gebruik de vervangtabel voor controle.")
                else:
                    highlight_preview_html_parts = []
                    for highlight_preview_segment in highlight_preview_result.get("segments", []):
                        if highlight_preview_segment.get("type") == "highlight":
                            highlight_preview_html_parts.append(
                                '<mark style="padding:0.1rem 0.25rem; border-radius:0.25rem; border:1px solid #d0a000;" '
                                f'title="{highlight_preview_segment.get("category_label", "Markering")}">'
                                f'{highlight_preview_segment.get("escaped_text", "")}'
                                f' <small>[{highlight_preview_segment.get("category_label", "Markering")}]</small>'
                                '</mark>'
                            )
                        else:
                            highlight_preview_html_parts.append(highlight_preview_segment.get("escaped_text", ""))
                    st.markdown(
                        '<div aria-label="Alleen-lezen documentvoorbeeld met markeringen" '
                        'style="line-height:1.9; white-space:pre-wrap; border:1px solid #ddd; padding:0.75rem; border-radius:0.35rem;">'
                        + "".join(highlight_preview_html_parts)
                        + "</div>",
                        unsafe_allow_html=True,
                    )
                    st.caption(highlight_preview_result.get("warning", "Static preview only; the review table remains authoritative."))
                    st.caption(f"{len(highlight_preview_result.get('valid_spans', []))} markering(en) getoond. Niet bepalend voor export.")
                    if highlight_preview_result.get("invalid_spans"):
                        st.warning("Sommige markeringen zijn overgeslagen omdat offsets of labels niet veilig overeenkwamen.")
                    with st.expander("Legenda markeringen", expanded=False):
                        for highlight_preview_category, highlight_preview_label in highlight_preview_result.get("category_labels", {}).items():
                            st.markdown(f"- `{highlight_preview_category}` — {highlight_preview_label}")
'''

text = replace_once(
    text,
    '''        with st.expander("Technische details bij de vervangtabel", expanded=False):
            st.caption(TECHNICAL_DETAILS_GUIDANCE)
            technical_columns = technical_display_columns(replacement_editor_df.columns)
            if technical_columns:
                st.dataframe(replacement_editor_df[technical_columns], use_container_width=True)
            else:
                st.caption("Geen technische detailkolommen beschikbaar.")
        edited_replacements_df = st.data_editor(
''',
    '''        with st.expander("Technische details bij de vervangtabel", expanded=False):
            st.caption(TECHNICAL_DETAILS_GUIDANCE)
            technical_columns = technical_display_columns(replacement_editor_df.columns)
            if technical_columns:
                st.dataframe(replacement_editor_df[technical_columns], use_container_width=True)
            else:
                st.caption("Geen technische detailkolommen beschikbaar.")
'''
    + static_highlight_preview_block
    + '''        edited_replacements_df = st.data_editor(
''',
)

APP_FILE.write_text(text, encoding="utf-8")
