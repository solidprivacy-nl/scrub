"""Streamlit renderer for the optional review highlight toggle.

The panel is deliberately non-mutating. It builds a preview from the current
review table values and can render escaped HTML with subtle markers for values
that are already present in that preview. It does not write table state, Scrub
Key data, export payloads or reinsert state.
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from review_highlight_toggle import build_highlight_terms, build_highlighted_preview_html


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    try:
        if value != value:  # NaN check without pandas dependency
            return ""
    except Exception:
        pass
    return str(value).strip()


def _safe_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    try:
        if value != value:  # NaN check without pandas dependency
            return False
    except Exception:
        pass
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"true", "1", "yes", "y", "checked", "ja"}


def build_preview_replacements(edited_replacements_df: Any) -> dict[str, str]:
    """Build exact replacement mapping for display preview only."""

    replacements: dict[str, str] = {}
    if edited_replacements_df is None:
        return replacements
    iterator = edited_replacements_df.iterrows() if hasattr(edited_replacements_df, "iterrows") else enumerate(edited_replacements_df)
    for _, row in iterator:
        if not _safe_bool(row.get("include", False)):
            continue
        find_text = _safe_text(row.get("find", ""))
        replace_text = _safe_text(row.get("replace_with", ""))
        if find_text and replace_text:
            replacements[find_text] = replace_text
    return replacements


def build_preview_text(displayed_text: str, edited_replacements_df: Any) -> str:
    """Build the read-only preview text without mutating app state."""

    preview_text = displayed_text or ""
    for find_text, replace_text in build_preview_replacements(edited_replacements_df).items():
        preview_text = preview_text.replace(find_text, replace_text)
    return preview_text


def render_review_highlight_toggle_panel(*, displayed_text: str, edited_replacements_df: Any) -> dict[str, Any]:
    """Render the optional masked-text highlight toggle.

    Returns a report-only state dictionary for tests/handover. The return value
    is not used to mutate export, Scrub Key or reinsert behavior.
    """

    preview_text = build_preview_text(displayed_text, edited_replacements_df)
    terms = build_highlight_terms(edited_replacements_df)

    with st.expander("Voorbeeldtekst met optionele markeringen", expanded=False):
        show_markers = st.checkbox(
            "Markeringen tonen in voorbeeldtekst",
            value=False,
            key="review_highlight_toggle_show_markers",
            help="Alleen een visuele hulp. Wijzigt niets aan vervangtabel, export of Scrub Key.",
        )
        st.caption(
            "Markeringen zijn alleen een visuele hulp. Ze wijzigen niets aan de vervangtabel, "
            "niets aan export en niets aan Scrub Key."
        )
        st.caption(
            "read-only · visual-only · non-mutating · table-first baseline · "
            "no Scrub Key writes · no export/download changes · no reinsert behavior change"
        )

        if show_markers:
            if terms:
                st.markdown(build_highlighted_preview_html(preview_text, terms), unsafe_allow_html=True)
            else:
                st.info("Geen gemarkeerde vervangingen beschikbaar in deze voorbeeldtekst.")
                st.text_area(
                    label="Gecontroleerde voorbeeldtekst",
                    value=preview_text,
                    height=220,
                    key="review_highlight_toggle_empty_preview",
                )
        else:
            st.text_area(
                label="Gecontroleerde voorbeeldtekst",
                value=preview_text,
                height=220,
                key="review_highlight_toggle_plain_preview",
            )

    return {
        "report_only": True,
        "visual_only": True,
        "mutation_allowed": False,
        "table_mutation": False,
        "scrub_key_writes": False,
        "export_download_changes": False,
        "reinsert_behavior_change": False,
        "highlight_terms_count": len(terms),
    }
