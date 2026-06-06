from candidate_scanner import CONTEXTUAL_VALUE_RE
from test_cases.legal_regression_cases import CASE_NUMBER_EXAMPLES


def test_known_case_number_shapes_match_contextual_reference_value_regex():
    """Case-number values include formal shapes and context-bound admin codes.

    GEM-HLM-2026-2210 is a zaaknummer because the surrounding label says so,
    even though the raw value has a generic administrative-code shape.
    """
    for value in CASE_NUMBER_EXAMPLES:
        assert CONTEXTUAL_VALUE_RE.fullmatch(value), f"Case/reference value shape should match: {value}"
