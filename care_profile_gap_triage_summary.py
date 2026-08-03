"""Compact summary projection for the Zorgfilter v1 gap triage."""

from __future__ import annotations

from typing import Any, Dict

from care_profile_gap_triage import build_care_profile_gap_triage


def build_care_profile_gap_triage_summary() -> Dict[str, Any]:
    """Return the reproducible triage summary without the 81 detailed rows."""

    report = build_care_profile_gap_triage()
    return {
        key: value
        for key, value in report.items()
        if key != "items"
    }
