"""Column configuration for the Scrub review table.

The main editing table should stay readable for legal users. Technical audit
fields remain available, but are separated from the primary edit workflow.
"""

MAIN_REVIEW_COLUMNS = [
    "include",
    "remember",
    "review_status_label",
    "find",
    "replace_with",
    "type_label",
    "confidence",
]

TECHNICAL_REVIEW_COLUMNS = [
    "source_label",
    "reason",
    "context",
    "entity_type",
    "score",
    "source",
    "review_status",
    "review_order",
]

TECHNICAL_DISPLAY_COLUMNS = [
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


def _available_column_set(available_columns):
    """Return a set of available columns without boolean-testing pandas Index.

    Pandas Index objects intentionally do not define truthiness. Code such as
    `available_columns or []` raises: "The truth value of a Index is ambiguous".
    The Streamlit app passes `replacement_editor_df.columns`, so this helper must
    handle any iterable column container explicitly.
    """
    if available_columns is None:
        return set()
    return set(list(available_columns))


def existing_columns(columns, available_columns):
    available = _available_column_set(available_columns)
    return [column for column in columns if column in available]


def main_review_columns(available_columns):
    return existing_columns(MAIN_REVIEW_COLUMNS, available_columns)


def technical_display_columns(available_columns):
    return existing_columns(TECHNICAL_DISPLAY_COLUMNS, available_columns)


def hidden_technical_columns(available_columns):
    return existing_columns(TECHNICAL_REVIEW_COLUMNS, available_columns)
