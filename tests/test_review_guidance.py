from review_guidance import (
    AI_USAGE_GUIDANCE,
    CANDIDATE_GUIDANCE,
    EXPORT_GUIDANCE,
    FOCUS_FILTER_GUIDANCE,
    REVIEW_INTRO_GUIDANCE,
    TECHNICAL_DETAILS_GUIDANCE,
    review_guidance_items,
    review_guidance_markdown,
)


def test_review_guidance_explains_checked_rows_are_exported():
    assert "Alleen aangevinkte" in REVIEW_INTRO_GUIDANCE
    assert "exporteert" in REVIEW_INTRO_GUIDANCE


def test_candidate_guidance_explains_manual_review():
    assert "Controle nodig" in CANDIDATE_GUIDANCE
    assert "niet automatisch" in CANDIDATE_GUIDANCE
    assert "handmatig" in CANDIDATE_GUIDANCE


def test_focus_filter_guidance_explains_filter_is_not_export_scope():
    assert "focusfilter" in FOCUS_FILTER_GUIDANCE.lower()
    assert "volledige vervangtabel" in FOCUS_FILTER_GUIDANCE
    assert "export" in FOCUS_FILTER_GUIDANCE


def test_technical_details_guidance_keeps_audit_view_non_primary():
    assert "Technische details" in TECHNICAL_DETAILS_GUIDANCE
    assert "normaal gebruik" in TECHNICAL_DETAILS_GUIDANCE


def test_ai_and_export_guidance_keep_user_control_explicit():
    assert "Gebruik AI pas" in AI_USAGE_GUIDANCE
    assert "Scrub Key" in AI_USAGE_GUIDANCE
    assert "handmatige controle" in EXPORT_GUIDANCE


def test_review_guidance_markdown_contains_all_items_as_bullets():
    items = review_guidance_items()
    markdown = review_guidance_markdown()
    assert len(items) == 5
    for item in items:
        assert f"- {item}" in markdown
