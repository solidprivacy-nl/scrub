"""Machine-readable validation summary for central recognition profiles."""

from __future__ import annotations

from typing import Any, Dict

from recognition_profiles import (
    CARE_EXACT_SPAN_SUPERSEDES,
    CURRENT_VISIBLE_PROFILE_IDS,
    DESKTOP_PROFILE_IDS,
    PROFILE_DEFINITIONS,
    TARGET_STREAMLIT_PROFILE_IDS,
    profile_options,
    profile_snapshot,
    short_profile_options,
)


def build_recognition_profile_validation() -> Dict[str, Any]:
    snapshot = profile_snapshot()
    return {
        "schema_version": "1.0",
        "profile_count": len(PROFILE_DEFINITIONS),
        "current_visible_profile_ids": list(CURRENT_VISIBLE_PROFILE_IDS),
        "current_visible_options": [
            {"label_nl": label, "internal_value": internal_value}
            for label, internal_value in profile_options()
        ],
        "target_streamlit_profile_ids": list(TARGET_STREAMLIT_PROFILE_IDS),
        "target_streamlit_options": [
            {"label_nl": label, "internal_value": internal_value}
            for label, internal_value in profile_options(include_care=True)
        ],
        "desktop_profile_ids": list(DESKTOP_PROFILE_IDS),
        "desktop_short_options": [
            {"label_nl": label, "profile_id": profile_id}
            for label, profile_id in short_profile_options()
        ],
        "exact_span_precedence_winner_count": len(CARE_EXACT_SPAN_SUPERSEDES),
        "profiles": snapshot["profiles"],
        "care_exact_span_supersedes": snapshot["care_exact_span_supersedes"],
        "live_ui_changed": False,
        "care_recognizers_registered": False,
        "production_ready": False,
        "human_review_required": True,
        "next_workpackage": "SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION",
    }
