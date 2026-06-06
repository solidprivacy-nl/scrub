from review_table_config import (
    MAIN_REVIEW_COLUMNS,
    TECHNICAL_REVIEW_COLUMNS,
    hidden_technical_columns,
    main_review_columns,
    technical_display_columns,
)


def test_main_review_columns_are_limited_to_user_facing_edit_fields():
    assert MAIN_REVIEW_COLUMNS == [
        "include",
        "remember",
        "review_status_label",
        "find",
        "replace_with",
        "type_label",
        "confidence",
    ]


def test_technical_columns_are_not_in_main_review_columns():
    for column in TECHNICAL_REVIEW_COLUMNS:
        assert column not in MAIN_REVIEW_COLUMNS


def test_main_review_columns_only_returns_existing_columns():
    available = ["include", "find", "replace_with", "source", "score"]
    assert main_review_columns(available) == ["include", "find", "replace_with"]


def test_technical_display_columns_preserve_audit_fields_when_available():
    available = [
        "review_status_label",
        "find",
        "type_label",
        "source_label",
        "reason",
        "context",
        "entity_type",
        "score",
        "source",
    ]
    assert technical_display_columns(available) == available


def test_hidden_technical_columns_only_returns_existing_technical_columns():
    available = ["include", "source_label", "reason", "score", "replace_with"]
    assert hidden_technical_columns(available) == ["source_label", "reason", "score"]
