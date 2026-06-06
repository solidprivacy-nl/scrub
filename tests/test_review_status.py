from review_status import (
    AUTO_DETECTED,
    MANUAL,
    NEEDS_REVIEW,
    REMEMBERED,
    review_status_for_source,
    review_status_label,
    review_status_order,
)


def test_review_status_maps_candidate_to_needs_review():
    assert review_status_for_source("candidate", "NL_LEGAL_CASE_NUMBER", 0.7) == NEEDS_REVIEW
    assert review_status_label(NEEDS_REVIEW) == "Controle nodig"


def test_review_status_maps_detected_to_auto_detected():
    assert review_status_for_source("detected", "PERSON", 0.91) == AUTO_DETECTED
    assert review_status_label(AUTO_DETECTED) == "Automatisch vervangen"


def test_review_status_maps_manual_and_remembered_rows():
    assert review_status_for_source("manual", "MANUAL", None) == MANUAL
    assert review_status_for_source("remembered", "REMEMBERED", None) == REMEMBERED
    assert review_status_label(MANUAL) == "Handmatig toegevoegd"
    assert review_status_label(REMEMBERED) == "Onthouden vervanging"


def test_review_status_unknown_source_defaults_to_review():
    assert review_status_for_source("", "UNKNOWN", None) == NEEDS_REVIEW
    assert review_status_for_source(None, None, None) == NEEDS_REVIEW


def test_review_status_sort_order_puts_review_items_first():
    order = [
        review_status_order(REMEMBERED),
        review_status_order(MANUAL),
        review_status_order(AUTO_DETECTED),
        review_status_order(NEEDS_REVIEW),
    ]
    assert order == sorted(order, reverse=True)
    assert review_status_order(NEEDS_REVIEW) < review_status_order(AUTO_DETECTED)
