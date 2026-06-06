import re

from candidate_scanner import CASE_NUMBER_VALUE_RE_PART
from test_cases.legal_regression_cases import CASE_NUMBER_EXAMPLES


def test_known_case_number_shapes_match_core_case_number_regex():
    pattern = re.compile(rf"^{CASE_NUMBER_VALUE_RE_PART}$")
    for value in CASE_NUMBER_EXAMPLES:
        assert pattern.match(value), f"Case number shape should match: {value}"
