from test_cases.legal_regression_cases import CONTEXT_PRESERVATION_EXAMPLES


def test_context_preservation_examples_document_required_contract():
    """These cases define the minimum UX contract for legal readability.

    The scrubber may replace names and identifiers, but role/context words such
    as slachtoffer, minderjarige, verzoeker and BIG-nummer must remain readable.
    This test is intentionally light: it guards the test data contract before the
    full recognizer test harness is added.
    """
    for case in CONTEXT_PRESERVATION_EXAMPLES:
        text = case["text"]
        for word in case["context_words_to_preserve"]:
            assert word in text
        for value in case["sensitive_values"]:
            assert value in text


def test_context_words_are_not_part_of_sensitive_values():
    for case in CONTEXT_PRESERVATION_EXAMPLES:
        for value in case["sensitive_values"]:
            for word in case["context_words_to_preserve"]:
                assert word not in value
