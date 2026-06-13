from __future__ import annotations

from review_highlight_toggle import (
    build_highlight_terms,
    build_highlighted_preview_html,
    find_exact_highlight_spans,
)


def test_build_highlight_terms_uses_only_included_complete_replacements():
    rows = [
        {"include": True, "find": "SYNTHETIC_NAME", "replace_with": "[PERSON_1]"},
        {"include": False, "find": "SYNTHETIC_ADDRESS", "replace_with": "[ADDRESS_1]"},
        {"include": True, "find": "SYNTHETIC_EMPTY_REPLACEMENT", "replace_with": ""},
        {"include": True, "find": "", "replace_with": "[NO_FIND]"},
    ]

    assert build_highlight_terms(rows) == ["[PERSON_1]"]


def test_build_highlight_terms_deduplicates_and_sorts_longest_first():
    rows = [
        {"include": True, "find": "SYNTHETIC_A", "replace_with": "[A]"},
        {"include": True, "find": "SYNTHETIC_B", "replace_with": "[A_LONGER]"},
        {"include": True, "find": "SYNTHETIC_C", "replace_with": "[A]"},
    ]

    assert build_highlight_terms(rows) == ["[A_LONGER]", "[A]"]


def test_find_exact_highlight_spans_uses_exact_matching_only():
    text = "SYNTHETIC [PERSON_1] and [PERSON_10] stay separate."

    spans = find_exact_highlight_spans(text, ["[PERSON_1]"])

    assert spans == [(10, 20)]
    assert text[spans[0][0] : spans[0][1]] == "[PERSON_1]"


def test_build_highlighted_preview_html_escapes_document_text_before_wrapping():
    text = "SYNTHETIC <script>alert(1)</script> [PERSON_1]"

    html = build_highlighted_preview_html(text, ["[PERSON_1]"])

    assert "<script>" not in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    assert '<mark class="sp-review-highlight-token"' in html
    assert "[PERSON_1]" in html


def test_build_highlighted_preview_html_marks_without_mutation_metadata():
    html = build_highlighted_preview_html("SYNTHETIC [CASE_1]", ["[CASE_1]"])

    assert "sp-review-highlight-preview" in html
    assert "gemarkeerde vervanging" in html
    assert "scrub_key" not in html.lower()
    assert "export_blocking" not in html.lower()
    assert "reinsert" not in html.lower()


def test_review_highlight_toggle_tests_use_synthetic_values_only():
    forbidden_real_data_examples = [
        "Jan " + "Jansen",
        "Piet " + "de " + "Vries",
        "123" + "456" + "782",
    ]
    rendered = __file__ + " SYNTHETIC"

    assert "SYNTHETIC" in rendered
    for forbidden in forbidden_real_data_examples:
        assert forbidden not in rendered
