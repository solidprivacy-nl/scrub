from review_filters import (
    FILTER_LEGAL_REFERENCES,
    FILTER_LOW_CONFIDENCE,
    FILTER_NAMES_ADDRESSES,
    FILTER_NEEDS_REVIEW,
    FILTER_SHOW_ALL,
    filter_review_records,
    row_matches_review_filter,
)


ROWS = [
    {
        "find": "INC-2026-0912",
        "entity_type": "NL_INCIDENT_NUMBER",
        "review_status": "needs_review",
        "review_status_label": "Controle nodig",
        "confidence": "Middel",
        "score": 0.71,
    },
    {
        "find": "Jan Jansen",
        "entity_type": "PERSON",
        "review_status": "auto_detected",
        "review_status_label": "Automatisch vervangen",
        "confidence": "Hoog",
        "score": 0.93,
    },
    {
        "find": "Keizersgracht 123",
        "entity_type": "NL_ADDRESS",
        "review_status": "auto_detected",
        "review_status_label": "Automatisch vervangen",
        "confidence": "Hoog",
        "score": 0.86,
    },
    {
        "find": "mogelijk-zwak",
        "entity_type": "NL_OTHER_REFERENCE",
        "review_status": "needs_review",
        "review_status_label": "Controle nodig",
        "confidence": "Laag",
        "score": 0.42,
    },
]


def _finds(rows):
    return {row["find"] for row in rows}


def test_show_all_filter_returns_all_rows():
    assert filter_review_records(ROWS, FILTER_SHOW_ALL) == ROWS


def test_needs_review_filter_returns_only_review_rows():
    filtered = filter_review_records(ROWS, FILTER_NEEDS_REVIEW)
    assert _finds(filtered) == {"INC-2026-0912", "mogelijk-zwak"}


def test_legal_references_filter_returns_reference_rows():
    filtered = filter_review_records(ROWS, FILTER_LEGAL_REFERENCES)
    assert _finds(filtered) == {"INC-2026-0912", "mogelijk-zwak"}


def test_names_addresses_filter_returns_person_and_address_rows():
    filtered = filter_review_records(ROWS, FILTER_NAMES_ADDRESSES)
    assert _finds(filtered) == {"Jan Jansen", "Keizersgracht 123"}


def test_low_confidence_filter_uses_label_or_score():
    assert row_matches_review_filter(ROWS[-1], FILTER_LOW_CONFIDENCE)
    assert not row_matches_review_filter(ROWS[1], FILTER_LOW_CONFIDENCE)
