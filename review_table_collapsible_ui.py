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
