"""Streamlit renderer for the side-by-side review surface.

The source remains read-only. The processed pane can emit bounded selection
inspect/commit-intent events through the local component. Server-side callers
remain authoritative for validation and row mutation. The previous static HTML
renderer remains available as an environment-controlled and exception fallback.
"""

from __future__ import annotations

from html import escape
import os
from typing import Any, Mapping

import streamlit as st
import streamlit.components.v1 as components

from bound_placeholder_display import build_bound_placeholder_display_segments
from processed_text_selection_component import (
    render_processed_text_selection_component,
)
from review_highlight_toggle_panel_ui import build_preview_text
from selection_mask_action import processed_text_hash
from side_by_side_review import build_side_by_side_review_model


SIDE_BY_SIDE_REVIEW_PANE_HEIGHT = 320
SIDE_BY_SIDE_REVIEW_COMPONENT_HEIGHT = 410
BASIC_REVIEW_MODE = "Basiscontrole"
EXPERT_REVIEW_MODE = "Expertcontrole"
REVIEW_MODE_OPTIONS = [BASIC_REVIEW_MODE, EXPERT_REVIEW_MODE]
INTERACTIVE_COMPONENT_ENV = "PROCESSED_TEXT_SELECTION_COMPONENT_ENABLED"

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


def interactive_selection_component_enabled() -> bool:
    """Return the deploy-time rollback switch for the interactive component."""

    value = os.environ.get(INTERACTIVE_COMPONENT_ENV, "true").strip().lower()
    return value not in {"0", "false", "no", "off", "disabled"}


def _highlighted_processed_inner_html(
    processed_text: str,
    highlight_spans: list[tuple[int, int]],
) -> str:
    """Return lossless compact display HTML for the static fallback pane."""

    parts: list[str] = []
    for segment in build_bound_placeholder_display_segments(processed_text, highlight_spans):
        display_text = escape(str(segment["display_text"]))
        full_placeholder = str(segment["full_placeholder"])
        compact_attributes = ""
        compact_class = ""
        if segment["compacted"]:
            compact_class = " sp-compact-placeholder"
            compact_attributes = (
                f' title="Volledige gebonden placeholder: {escape(full_placeholder)}"'
                f' aria-label="Gebonden placeholder, compact weergegeven als {display_text}"'
            )
        if segment["highlighted"]:
            parts.append(
                f'<mark class="sp-side-by-side-highlight-token{compact_class}"'
                f'{compact_attributes}>{display_text}</mark>'
            )
        elif segment["compacted"]:
            parts.append(
                f'<span class="sp-compact-placeholder"{compact_attributes}>'
                f'{display_text}</span>'
            )
        else:
            parts.append(display_text)
    return "".join(parts)


def _side_by_side_sync_scroll_html(
    *,
    source_text: str,
    processed_text: str,
    processed_html: str,
    show_markers: bool,
) -> str:
    """Build escaped HTML for the synchronized static fallback."""

    source_html = escape(source_text)
    compacted = any(
        segment["compacted"]
        for segment in build_bound_placeholder_display_segments(processed_text, [])
    )
    if show_markers and compacted:
        processed_legend = "Geel = vervangen; documentcode compact weergegeven"
    elif show_markers:
        processed_legend = "Geel = vervangen of gemaskeerde waarde"
    elif compacted:
        processed_legend = "Documentcode compact weergegeven"
    else:
        processed_legend = "Verwerkte tekst"
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
    De panelen scrollen samen. Bij grote tekstverschillen kan de uitlijning iets afwijken.
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


def _render_static_fallback(
    *,
    source_text: str,
    processed_text: str,
    highlight_spans: list[tuple[int, int]],
    show_markers: bool,
) -> None:
    processed_html = _highlighted_processed_inner_html(
        processed_text,
        highlight_spans if show_markers else [],
    )
    components.html(
        _side_by_side_sync_scroll_html(
            source_text=source_text,
            processed_text=processed_text,
            processed_html=processed_html,
            show_markers=bool(show_markers and highlight_spans),
        ),
        height=SIDE_BY_SIDE_REVIEW_COMPONENT_HEIGHT,
        scrolling=False,
    )


def render_review_mode_selector() -> str:
    """Render the Basiscontrole / Expertcontrole visibility selector."""

    review_mode = st.radio(
        "Controleweergave",
        REVIEW_MODE_OPTIONS,
        index=0,
        horizontal=True,
        key="solidprivacy_review_mode",
        help=(
            "Basiscontrole toont de kern van controleren en downloaden. "
            "Expertcontrole toont alle detail-, audit- en technische controles. "
            "Deze keuze wijzigt alleen zichtbaarheid en groepering."
        ),
    )
    if review_mode == BASIC_REVIEW_MODE:
        st.caption(
            "Basiscontrole: controleer de gemarkeerde tekst, voeg gemiste waarden toe als dat nodig is, "
            "en download daarna veilig."
        )
    else:
        st.caption(
            "Expertcontrole: alle detailcontroles, auditinformatie en technische hulpmiddelen blijven beschikbaar."
        )
    return str(review_mode)


def render_side_by_side_review_panel(
    *,
    source_text: str,
    edited_replacements_df: Any,
    document_scope_key: str = "",
    inspection_result: Mapping[str, Any] | None = None,
    restore_source_scroll_ratio: float | None = None,
    restore_processed_scroll_ratio: float | None = None,
) -> dict[str, Any]:
    """Render source/processed review and return any bounded component event."""

    review_mode = render_review_mode_selector()
    processed_text = build_preview_text(source_text, edited_replacements_df)

    st.caption(
        "Controleer links de brontekst en rechts de verwerkte tekst. "
        "Selecteer rechts een gemiste waarde en gebruik de rechtermuisknop of ‘Masker selectie’."
    )

    show_markers = st.checkbox(
        "Markeringen tonen",
        value=True,
        key="side_by_side_review_show_markers",
        help="Visuele hulp bij het controleren; dit wijzigt de vervangtabel, export, Scrub Key of terugzetten niet.",
    )

    model = build_side_by_side_review_model(
        source_text=source_text,
        processed_text=processed_text,
        review_rows=edited_replacements_df,
        highlights_enabled=show_markers,
    )
    compact_legend = model["compact_legend"]
    highlight_spans = list(model["processed_pane"]["highlight_spans"])
    component_event: dict[str, Any] | None = None
    interactive_enabled = bool(document_scope_key and interactive_selection_component_enabled())
    static_fallback_used = not interactive_enabled
    component_error = ""

    if interactive_enabled:
        try:
            component_event = render_processed_text_selection_component(
                source_text=model["source_pane"]["text"],
                processed_text=model["processed_pane"]["text"],
                highlight_spans=highlight_spans,
                document_scope_key=document_scope_key,
                processed_text_hash=processed_text_hash(model["processed_pane"]["text"]),
                inspection_result=inspection_result,
                restore_source_scroll_ratio=restore_source_scroll_ratio,
                restore_processed_scroll_ratio=restore_processed_scroll_ratio,
                key=f"processed_text_selection_{document_scope_key}",
            )
        except Exception as exc:
            component_error = str(exc)
            static_fallback_used = True
            st.warning(
                "Direct selecteren kon niet worden geladen. De eenvoudige reviewweergave en "
                "‘Gemiste waarde toevoegen’ blijven beschikbaar."
            )
            _render_static_fallback(
                source_text=model["source_pane"]["text"],
                processed_text=model["processed_pane"]["text"],
                highlight_spans=highlight_spans,
                show_markers=show_markers,
            )
    else:
        _render_static_fallback(
            source_text=model["source_pane"]["text"],
            processed_text=model["processed_pane"]["text"],
            highlight_spans=highlight_spans,
            show_markers=show_markers,
        )

    st.caption(
        "Twijfel je over een waarde? Selecteer die rechts of gebruik ‘Gemiste waarde toevoegen’. "
        "Elke toevoeging blijft zichtbaar en aanpasbaar in de vervangtabel."
    )
    st.caption(model["review_table"]["copy"])
    st.markdown("#### Meer controleopties")
    st.caption(
        "Aanvullen, detailcontrole en stap-voor-stap controle staan hieronder compact bij elkaar. "
        "Alles staat standaard ingeklapt."
    )

    return {
        "report_only": False,
        "visual_only": False,
        "mutation_allowed": False,
        "component_event": component_event,
        "processed_text": model["processed_pane"]["text"],
        "processed_text_hash": processed_text_hash(model["processed_pane"]["text"]),
        "highlight_spans": highlight_spans,
        "review_mode": review_mode,
        "basic_review_mode_default": BASIC_REVIEW_MODE,
        "expert_review_mode": EXPERT_REVIEW_MODE,
        "mode_switch_visibility_only": True,
        "session_state_key": "solidprivacy_review_mode",
        "review_table_mutation": False,
        "replacement_mutation": False,
        "scrub_key_writes": False,
        "export_download_behavior_change": False,
        "reinsert_behavior_change": False,
        "synchronized_scroll_implementation": True,
        "sync_scroll_percentage_based": True,
        "sync_scroll_always_on": True,
        "sync_scroll_visible_checkbox": False,
        "custom_component_rendering": interactive_enabled and not static_fallback_used,
        "uses_streamlit_components_html": static_fallback_used,
        "interactive_selection_enabled": interactive_enabled,
        "static_fallback_available": True,
        "static_fallback_used": static_fallback_used,
        "component_error": component_error,
        "component_environment_switch": INTERACTIVE_COMPONENT_ENV,
        "bound_placeholder_display_compaction": True,
        "bound_placeholder_source_tokens_unchanged": True,
        "bound_placeholder_binding_entropy_changed": False,
        "pane_height": SIDE_BY_SIDE_REVIEW_PANE_HEIGHT,
        "compact_legend": compact_legend,
        "model": model,
    }
