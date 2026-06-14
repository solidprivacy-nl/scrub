"""Streamlit renderer for the bounded side-by-side review surface.

The side-by-side review surface shows source text on the left and processed text
on the right. Highlights are visual-only. Scrolling is synchronized by default.
The returned model is report-only and is not used to change review-table,
replacement, export, Scrub Key or reinsert behavior.
"""

from __future__ import annotations

from html import escape
from typing import Any

import streamlit as st
import streamlit.components.v1 as components

from review_highlight_toggle_panel_ui import build_preview_text
from side_by_side_review import build_side_by_side_review_model


SIDE_BY_SIDE_REVIEW_PANE_HEIGHT = 320
SIDE_BY_SIDE_REVIEW_COMPONENT_HEIGHT = 410

_SYNC_SCROLL_COMPONENT_CSS = f"""
<style>
.sp-sync-scroll-wrapper {{
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #111827;
}}
.sp-sync-scroll-grid {{
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: 1.25rem;
    align-items: start;
}}
.sp-sync-scroll-title {{
    display: flex;
    justify-content: space-between;
    gap: 0.75rem;
    align-items: baseline;
    margin: 0 0 0.45rem 0;
}}
.sp-sync-scroll-title strong {{
    font-size: 1rem;
}}
.sp-sync-scroll-legend {{
    color: #6b7280;
    font-size: 0.86rem;
}}
.sp-sync-scroll-pane {{
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
.sp-sync-scroll-footer {{
    margin-top: 0.6rem;
    color: #6b7280;
    font-size: 0.86rem;
}}
</style>
""".strip()


def _highlighted_processed_inner_html(processed_text: str, highlight_spans: list[tuple[int, int]]) -> str:
    """Return escaped inner HTML for the processed pane only."""

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
    return "".join(parts)


def _side_by_side_sync_scroll_html(*, source_text: str, processed_text: str, processed_html: str, show_markers: bool) -> str:
    """Build escaped HTML for synchronized side-by-side scrolling."""

    source_html = escape(source_text)
    processed_legend = "Geel = vervangen of gemaskeerde waarde" if show_markers else "Verwerkte tekst"
    return f"""
{_SYNC_SCROLL_COMPONENT_CSS}
<div class="sp-sync-scroll-wrapper">
  <div class="sp-sync-scroll-grid" aria-label="side-by-side review panes">
    <section>
      <div class="sp-sync-scroll-title">
        <strong>Brontekst</strong>
        <span class="sp-sync-scroll-legend">Originele tekst</span>
      </div>
      <div id="sourcePane" class="sp-sync-scroll-pane" tabindex="0" aria-label="Brontekst">{source_html}</div>
    </section>
    <section>
      <div class="sp-sync-scroll-title">
        <strong>Verwerkte tekst</strong>
        <span class="sp-sync-scroll-legend">{escape(processed_legend)}</span>
      </div>
      <div id="processedPane" class="sp-sync-scroll-pane" tabindex="0" aria-label="Verwerkte tekst">{processed_html}</div>
    </section>
  </div>
  <div class="sp-sync-scroll-footer">
    De panelen scrollen synchroon. Bij grote tekstverschillen kan de visuele uitlijning iets afwijken.
  </div>
</div>
<script>
(function () {{
  const sourcePane = document.getElementById('sourcePane');
  const processedPane = document.getElementById('processedPane');
  let isSyncing = false;

  function scrollRatio(element) {{
    const maxScroll = element.scrollHeight - element.clientHeight;
    if (maxScroll <= 0) {{
      return 0;
    }}
    return element.scrollTop / maxScroll;
  }}

  function setScrollRatio(element, ratio) {{
    const maxScroll = element.scrollHeight - element.clientHeight;
    element.scrollTop = ratio * maxScroll;
  }}

  function syncScroll(fromPane, toPane) {{
    if (isSyncing) {{
      return;
    }}
    isSyncing = true;
    window.requestAnimationFrame(function () {{
      setScrollRatio(toPane, scrollRatio(fromPane));
      isSyncing = false;
    }});
  }}

  sourcePane.addEventListener('scroll', function () {{
    syncScroll(sourcePane, processedPane);
  }});

  processedPane.addEventListener('scroll', function () {{
    syncScroll(processedPane, sourcePane);
  }});
}}());
</script>
""".strip()


def render_side_by_side_review_panel(*, source_text: str, edited_replacements_df: Any) -> dict[str, Any]:
    """Render a small source/processed comparison surface."""

    processed_text = build_preview_text(source_text, edited_replacements_df)

    st.subheader("Controleer de tekst")
    st.caption("Vergelijk links de brontekst met rechts de verwerkte tekst. De vervangtabel blijft leidend.")
    st.caption(
        "side-by-side review · table-first baseline · visual-only highlights · "
        "no Scrub Key writes · no export/download changes · no reinsert behavior change"
    )

    show_markers = st.checkbox(
        "Markeringen tonen",
        value=True,
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
    processed_html = (
        _highlighted_processed_inner_html(
            model["processed_pane"]["text"],
            model["processed_pane"]["highlight_spans"],
        )
        if show_markers and model["processed_pane"]["highlight_spans"]
        else escape(model["processed_pane"]["text"])
    )

    components.html(
        _side_by_side_sync_scroll_html(
            source_text=model["source_pane"]["text"],
            processed_text=model["processed_pane"]["text"],
            processed_html=processed_html,
            show_markers=bool(show_markers and model["processed_pane"]["highlight_spans"]),
        ),
        height=SIDE_BY_SIDE_REVIEW_COMPONENT_HEIGHT,
        scrolling=False,
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
        "synchronized_scroll_implementation": True,
        "sync_scroll_percentage_based": True,
        "sync_scroll_always_on": True,
        "sync_scroll_visible_checkbox": False,
        "custom_component_rendering": False,
        "uses_streamlit_components_html": True,
        "pane_height": SIDE_BY_SIDE_REVIEW_PANE_HEIGHT,
        "compact_legend": compact_legend,
        "model": model,
    }
