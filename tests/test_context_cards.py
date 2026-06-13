from __future__ import annotations

from context_cards import build_context_card, build_context_cards


SYNTHETIC_TEXT = (
    "SYNTHETIC_A start [PERSOON_1] woont in [PLAATS_1]. "
    "Zaak [ZAAK_1] blijft alleen testcontext."
)


def _card_for(value: str, **overrides):
    start = SYNTHETIC_TEXT.index(value)
    params = {
        "displayed_text": SYNTHETIC_TEXT,
        "start_offset": start,
        "end_offset": start + len(value),
        "source_text": value,
        "entity_type": "PERSON",
        "review_state": "needs_review",
        "replacement_preview": "[PERSOON_X]",
        "source": "synthetic_test",
        "risk_flags": ["synthetic_high_risk"],
        "context_window": 12,
        "occurrence_id": "occ-1",
    }
    params.update(overrides)
    return build_context_card(**params)


def test_valid_context_card_builds_prefix_match_suffix_and_boundaries():
    card = _card_for("[PERSOON_1]")

    assert card["card_type"] == "context_card"
    assert card["occurrence_id"] == "occ-1"
    assert card["match_text"] == "[PERSOON_1]"
    assert card["prefix_text"].endswith(" start ")
    assert card["suffix_text"].startswith(" woont")
    assert card["escaped_match"] == "[PERSOON_1]"
    assert card["entity_type"] == "PERSON"
    assert card["review_state"] == "needs_review"
    assert card["replacement_preview"] == "[PERSOON_X]"
    assert card["source"] == "synthetic_test"
    assert card["offset_valid"] is True
    assert card["validation_errors"] == []
    assert card["report_only"] is True
    assert card["mutation_allowed"] is False
    assert card["export_blocking"] is False
    assert card["scrub_key_changes"] is False
    assert card["automatic_replacement"] is False
    assert card["fuzzy_matching"] is False
    assert card["document_editor_state"] is False


def test_match_at_beginning_of_text_has_empty_prefix():
    text = "[BEGIN_1] staat aan het begin van synthetische tekst."
    card = build_context_card(
        displayed_text=text,
        start_offset=0,
        end_offset=len("[BEGIN_1]"),
        source_text="[BEGIN_1]",
        entity_type="SYNTHETIC_BEGIN",
        review_state="accepted",
        replacement_preview="[BEGIN_REDACTED]",
        source="synthetic_test",
        risk_flags=[],
        context_window=20,
        occurrence_id="begin",
    )

    assert card["offset_valid"] is True
    assert card["prefix_text"] == ""
    assert card["match_text"] == "[BEGIN_1]"
    assert card["suffix_text"].startswith(" staat")


def test_match_at_end_of_text_has_empty_suffix():
    text = "Synthetische tekst eindigt met [EIND_1]"
    start = text.index("[EIND_1]")
    card = build_context_card(
        displayed_text=text,
        start_offset=start,
        end_offset=len(text),
        source_text="[EIND_1]",
        entity_type="SYNTHETIC_END",
        review_state="accepted",
        replacement_preview="[EIND_REDACTED]",
        source="synthetic_test",
        risk_flags=[],
        context_window=20,
        occurrence_id="end",
    )

    assert card["offset_valid"] is True
    assert card["prefix_text"].endswith(" met ")
    assert card["match_text"] == "[EIND_1]"
    assert card["suffix_text"] == ""


def test_context_window_truncates_prefix_and_suffix():
    card = _card_for("[PERSOON_1]", context_window=5)

    assert len(card["prefix_text"]) <= 5
    assert len(card["suffix_text"]) <= 5
    assert card["prefix_text"] == "tart "
    assert card["suffix_text"] == " woon"


def test_invalid_offsets_return_invalid_card_without_crash():
    card = build_context_card(
        displayed_text=SYNTHETIC_TEXT,
        start_offset=-4,
        end_offset=5000,
        source_text="[PERSOON_1]",
        entity_type="PERSON",
        review_state="needs_review",
        replacement_preview="[PERSOON_X]",
        source="synthetic_test",
        risk_flags=[],
        context_window=80,
        occurrence_id="bad-offset",
    )

    assert card["offset_valid"] is False
    assert card["prefix_text"] == ""
    assert card["match_text"] == ""
    assert card["suffix_text"] == ""
    assert "invalid offset range" in card["validation_errors"]
    assert "end_offset outside displayed_text" in card["validation_errors"]
    assert card["report_only"] is True
    assert card["mutation_allowed"] is False


def test_label_or_source_mismatch_is_reported_without_fuzzy_matching():
    start = SYNTHETIC_TEXT.index("[PERSOON_1]")
    card = build_context_card(
        displayed_text=SYNTHETIC_TEXT,
        start_offset=start,
        end_offset=start + len("[PERSOON_1]"),
        source_text="[PERSOON_2]",
        label="[PERSOON_1]",
        entity_type="PERSON",
        review_state="needs_review",
        replacement_preview="[PERSOON_X]",
        source="synthetic_test",
        risk_flags=[],
        context_window=20,
        occurrence_id="mismatch",
    )

    assert card["match_text"] == "[PERSOON_1]"
    assert card["offset_valid"] is False
    assert "source_text does not match displayed_text offsets" in card["validation_errors"]
    assert "label does not match source_text" in card["validation_errors"]
    assert card["fuzzy_matching"] is False


def test_html_escaping_for_script_like_synthetic_value():
    text = "SYNTHETIC <script> staat hier veilig."
    start = text.index("<script>")
    card = build_context_card(
        displayed_text=text,
        start_offset=start,
        end_offset=start + len("<script>"),
        source_text="<script>",
        entity_type="SYNTHETIC_HTML",
        review_state="needs_review",
        replacement_preview="<SAFE_PLACEHOLDER>",
        source="synthetic_test",
        risk_flags=["html_escape_check"],
        context_window=20,
        occurrence_id="html",
    )

    assert card["match_text"] == "<script>"
    assert card["escaped_match"] == "&lt;script&gt;"
    assert card["source_text"] == "<script>"
    assert card["escaped_source_text"] == "&lt;script&gt;"
    assert card["replacement_preview"] == "<SAFE_PLACEHOLDER>"
    assert card["escaped_replacement_preview"] == "&lt;SAFE_PLACEHOLDER&gt;"
    assert card["raw_html_allowed"] is False


def test_risk_flags_are_preserved_as_data():
    card = _card_for("[PERSOON_1]", risk_flags=["needs_manual_review", "same_value_multiple_contexts"])

    assert card["risk_flags"] == ["needs_manual_review", "same_value_multiple_contexts"]
    assert "risk_flags" in card


def test_report_only_and_mutation_boundaries_are_locked_for_batch_helper():
    first = SYNTHETIC_TEXT.index("[PERSOON_1]")
    second = SYNTHETIC_TEXT.index("[ZAAK_1]")
    result = build_context_cards(
        [
            {
                "start_offset": first,
                "end_offset": first + len("[PERSOON_1]"),
                "source_text": "[PERSOON_1]",
                "entity_type": "PERSON",
                "review_state": "accepted",
                "replacement_preview": "[PERSOON_X]",
                "source": "synthetic_test",
                "risk_flags": [],
                "occurrence_id": "person",
            },
            {
                "start_offset": second,
                "end_offset": second + len("[ZAAK_1]"),
                "source_text": "[ZAAK_1]",
                "entity_type": "CASE_REFERENCE",
                "review_state": "needs_review",
                "replacement_preview": "[ZAAK_X]",
                "source": "synthetic_test",
                "risk_flags": ["review_context"],
                "occurrence_id": "case",
            },
        ],
        SYNTHETIC_TEXT,
    )

    assert result["total_cards"] == 2
    assert result["invalid_count"] == 0
    assert result["report_only"] is True
    assert result["mutation_allowed"] is False
    assert result["export_blocking"] is False
    assert result["scrub_key_changes"] is False
    assert all(card["report_only"] is True for card in result["cards"])
    assert all(card["mutation_allowed"] is False for card in result["cards"])


def test_synthetic_only_values_are_used_in_tests():
    rendered = repr(_card_for("[PERSOON_1]"))

    assert "synthetic_test" in rendered
    assert "Jan Jansen" not in rendered
    assert "Piet de Vries" not in rendered
    assert "123456782" not in rendered
