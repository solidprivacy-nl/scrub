"""Helpers for review table collapsible presentation."""

from __future__ import annotations

from typing import Any


def review_table_expander_label(data: Any) -> str:
    """Return the label for the collapsed replacement table section."""

    try:
        item_count = len(getattr(data, "index"))
    except Exception:
        try:
            item_count = len(data)
        except Exception:
            item_count = 0
    return f"Vervangtabel controleren — {item_count} items"


def review_table_leading_copy() -> str:
    return "De vervangtabel blijft leidend voor beslissingen en export."


def render_collapsible_review_table(st_module: Any, editor_callable: Any, data: Any, **kwargs: Any) -> Any:
    """Render the existing replacement editor inside a collapsed expander."""

    with st_module.expander(review_table_expander_label(data), expanded=False):
        st_module.caption(review_table_leading_copy())
        return editor_callable(data, **kwargs)
