"""Standalone wrapper for the non-mutating processed-text selection component spike.

This module is not imported by the production Streamlit application. It proves
that the existing Streamlit 1.39 v1 component API can transport bounded inspect
and commit-intent events without changing replacement-table, export, Scrub Key
or reinsert state.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


COMPONENT_NAME = "solidprivacy_processed_text_selection_spike"
COMPONENT_HEIGHT = 500
FRONTEND_DIR = Path(__file__).resolve().parent / "frontend" / "processed_text_selection_component"


def normalize_highlight_spans(
    text: str,
    spans: Iterable[Sequence[int]] | None,
) -> tuple[tuple[int, int], ...]:
    """Validate and normalize non-overlapping Python-codepoint highlight spans."""

    normalized: list[tuple[int, int]] = []
    previous_end = 0
    for raw_span in spans or ():
        if not isinstance(raw_span, Sequence) or isinstance(raw_span, (str, bytes)):
            raise ValueError("highlight span must be a two-item sequence")
        if len(raw_span) != 2:
            raise ValueError("highlight span must contain start and end")
        start, end = raw_span
        if isinstance(start, bool) or isinstance(end, bool):
            raise ValueError("highlight span offsets must be integers")
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("highlight span offsets must be integers")
        if start < 0 or end <= start or end > len(text):
            raise ValueError("highlight span falls outside processed text")
        if normalized and start < previous_end:
            raise ValueError("highlight spans must be sorted and non-overlapping")
        normalized.append((start, end))
        previous_end = end
    return tuple(normalized)


def build_component_args(
    *,
    source_text: str,
    processed_text: str,
    highlight_spans: Iterable[Sequence[int]] | None,
    document_scope_key: str,
    processed_text_hash: str,
    inspection_result: Mapping[str, Any] | None = None,
    restore_source_scroll_ratio: float | None = None,
    restore_processed_scroll_ratio: float | None = None,
) -> dict[str, Any]:
    """Build the JSON-only argument object passed to the frontend component."""

    normalized_spans = normalize_highlight_spans(processed_text, highlight_spans)
    return {
        "source_text": str(source_text),
        "processed_text": str(processed_text),
        "highlight_spans": [list(span) for span in normalized_spans],
        "document_scope_key": str(document_scope_key),
        "processed_text_hash": str(processed_text_hash),
        "inspection_result": dict(inspection_result or {}),
        "restore_source_scroll_ratio": restore_source_scroll_ratio,
        "restore_processed_scroll_ratio": restore_processed_scroll_ratio,
        "component_contract": {
            "schema_version": 1,
            "inspect_action": "inspect_selection",
            "commit_action": "commit_manual_mask",
            "requested_scope": "all_exact",
            "non_mutating_spike": True,
        },
    }


@lru_cache(maxsize=1)
def _declare_component():
    """Declare the local v1 component lazily so pure tests need no Streamlit."""

    import streamlit.components.v1 as components

    if not FRONTEND_DIR.is_dir():
        raise RuntimeError(f"Component frontend directory is missing: {FRONTEND_DIR}")
    return components.declare_component(COMPONENT_NAME, path=str(FRONTEND_DIR))


def render_processed_text_selection_component_spike(
    *,
    source_text: str,
    processed_text: str,
    highlight_spans: Iterable[Sequence[int]] | None,
    document_scope_key: str,
    processed_text_hash: str,
    inspection_result: Mapping[str, Any] | None = None,
    restore_source_scroll_ratio: float | None = None,
    restore_processed_scroll_ratio: float | None = None,
    key: str | None = None,
) -> dict[str, Any] | None:
    """Render the spike and return its raw inspect or commit-intent event.

    The wrapper does not call the action model and does not mutate any table or
    session state. The standalone demo decides how to display returned events.
    """

    component = _declare_component()
    args = build_component_args(
        source_text=source_text,
        processed_text=processed_text,
        highlight_spans=highlight_spans,
        document_scope_key=document_scope_key,
        processed_text_hash=processed_text_hash,
        inspection_result=inspection_result,
        restore_source_scroll_ratio=restore_source_scroll_ratio,
        restore_processed_scroll_ratio=restore_processed_scroll_ratio,
    )
    value = component(**args, key=key, default=None)
    return dict(value) if isinstance(value, Mapping) else None


def component_spike_contract() -> dict[str, Any]:
    """Return machine-readable proof boundaries for tests and handover."""

    return {
        "component_name": COMPONENT_NAME,
        "api": "streamlit_components_v1",
        "frontend_path": str(FRONTEND_DIR),
        "local_assets_only": True,
        "runtime_build_step": False,
        "bidirectional": True,
        "renders_source_and_processed": True,
        "synchronized_scroll": True,
        "selection_offset_unit": "utf16_code_units",
        "context_menu": True,
        "visible_fallback": "Masker selectie",
        "keyboard_fallbacks": ["Shift+F10", "ContextMenu"],
        "emits_inspect_event": True,
        "displays_server_inspection": True,
        "emits_commit_intent": True,
        "calls_commit_action_model": False,
        "replacement_table_mutation": False,
        "session_state_mutation": False,
        "export_change": False,
        "scrub_key_change": False,
        "reinsert_change": False,
        "production_renderer_integration": False,
    }
