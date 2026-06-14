"""Streamlit renderer for the bounded side-by-side review surface.

WP_SIDE_BY_SIDE_REVIEW_IMPLEMENTATION exposes the helper model from
``side_by_side_review.py`` as a small UI surface:

    Brontekst links | Verwerkte tekst rechts
                    | optional visual-only highlights in the right pane

This renderer does not implement synchronized scrolling, does not use a custom
component, does not mutate the review table, does not change replacement
behavior, does not write Scrub Key data, does not change export/download
behavior, does not change reinsert behavior, does not add dependencies, does not
call cloud services and does not use real data.
"""

from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st

from review_highlight_toggle_panel_ui import build_preview_text
from side_by_side_review import build_side_by_side_review_model


SIDE_BY_SIDE_REVIEW_PANE_HEIGHT = 320

_SIDE_BY_SIDE_CSS = f"""
<style>
.sp-side-by-side-review-pane {{
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    border-radius: 0.5rem;
    box-sizing: border-box;
    height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px;
    max-height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px;
    min-height: {SIDE_BY_SIDE_REVIEW_PANE_HEIGHT}px;
    overflow-y: auto;
    padding: 0.75rem;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    line-height: 1.45;
}}
.sp-side-by-side-highlight-token {{
    background: #fef3c7;
    border: 1px solid #f59e0b;
    border-radius: 0.25rem;
    padding: 0.05rem 0.15rem;
}}
</style>
""".strip()


def _highlighted_processed_html(processed_text: str, highlight_spans: list[tuple[int, int]]) -> str:
    """Return escaped static HTML for the processed pane only.

    The document text is escaped before wrapping exact already-computed spans.
    No repeated visible inline label is inserted; a compact legend in the UI
    explains the marker meaning once.
    """

    parts: list[str] = []
    cursor = 0
    for start, end in highlight_spans:
        parts.append(escape(processed_text[cursor:start]))
        parts.append(
            '<mark class="sp-side-by-side-highlight-token" aria-label="gemarkeerde vervanging">'
            f"{escape(processed_text[start:end])}"
            "</mark>"
        )
        cursor = end
    parts.append(escape(processed_text[cursor:]))
    return f'{_SIDE_BY_SIDE_CSS}\n<div class="sp-side-by-side-review-pane">{"".join(parts)}</div>'


def render_side_by_side_review_panel(*, source_text: str, edited_replacements_df: Any) -> dict[str, Any]:
    """Render a small source/processed comparison surface.

    The returned model is report-only. It is not used to mutate replacement rows,
    export payloads, Scrub Key state or reinsert behavior.
    """

    processed_text = build_preview_text(source_text, edited_replacements_df)

    st.subheader("Controleer de tekst")
    st.caption("Vergelijk links de brontekst met rechts de verwerkte tekst. De vervangtabel blijft leidend.")
    st.caption(
        "side-by-side review · table-first baseline · visual-only highlights · "
        "no Scrub Key writes · no export/download changes · no reinsert behavior change"
    )

    show_markers = st.checkbox(
        "Markeringen tonen in verwerkte tekst",
        value=False,
        key="side_by_side_review_show_markers",
        help="Alleen visuele hulp. Wijzigt niets aan de vervangtabel, export, Scrub Key of terugzetten.",
    )

    model = build_side_by_side_review_model(
        source_text=source_text,
        processed_text=processed_text,
        review_rows=edited_replacements_df,
        highlights_enabled=show_markers,
    )
    compact_legend = model["compact_legend"]

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("**Brontekst**")
        st.text_area(
            label="Brontekst",
            value=model["source_pane"]["text"],
            height=SIDE_BY_SIDE_REVIEW_PANE_HEIGHT,
            key="side_by_side_review_source_text",
            disabled=True,
        )

    with right_column:
        st.markdown("**Verwerkte tekst**")
        if show_markers and model["processed_pane"]["highlight_spans"]:
            st.caption("Geel = vervangen of gemaskeerde waarde")
            st.markdown(
                _highlighted_processed_html(
                    model["processed_pane"]["text"],
                    model["processed_pane"]["highlight_spans"],
                ),
                unsafe_allow_html=True,
            )
        else:
            if show_markers:
                st.caption("Geen gemarkeerde vervangingen beschikbaar in deze verwerkte tekst.")
            st.text_area(
                label="Verwerkte tekst",
                value=model["processed_pane"]["text"],
                height=SIDE_BY_SIDE_REVIEW_PANE_HEIGHT,
                key="side_by_side_review_processed_text",
                disabled=True,
            )

    st.caption("Alleen visuele hulp. Must not change source text, review table state, export payloads, Scrub Key state or reinsert behavior.")
    st.caption(model["review_table"]["copy"])

    return {
        "report_only": True,
        "visual_only": True,
        "mutation_allowed": False,
        "review_table_mutation": False,
        "replacement_mutation": False,
        "scrub_key_writes": False,
        "export_download_behavior_change": False,
        "reinsert_behavior_change": False,
        "synchronized_scroll_implementation": False,
        "custom_component_rendering": False,
        "pane_height": SIDE_BY_SIDE_REVIEW_PANE_HEIGHT,
        "processed_pane_scrolls_independently": True,
        "compact_legend": compact_legend,
        "model": model,
    }
