from inspect import signature

from placeholder_validation import (
    classify_placeholder,
    compute_integrity_token,
    is_legacy_placeholder,
    validate_robust_placeholder,
)


def _robust(entity="PERSON", counter="0001"):
    integrity = compute_integrity_token(entity, counter)
    return f"[[SP_{entity}_{counter}_{integrity}]]"


def test_valid_robust_placeholder_is_parsed():
    placeholder = _robust("PERSON", "0001")
    result = validate_robust_placeholder(placeholder)
    assert result.is_valid is True
    assert result.kind == "robust"
    assert result.entity_type == "PERSON"
    assert result.counter == "0001"
    assert result.integrity == compute_integrity_token("PERSON", "0001")
    assert result.issues == ()


def test_invalid_prefix_is_rejected():
    result = classify_placeholder("[[XX_PERSON_0001_ABCD]]")
    assert result.is_valid is False
    assert result.kind == "malformed_robust"
    assert "invalid_prefix" in result.issues


def test_invalid_entity_is_rejected():
    result = validate_robust_placeholder("[[SP_person_0001_ABCD]]")
    assert result.is_valid is False
    assert result.kind == "malformed_robust"
    assert "invalid_entity" in result.issues


def test_invalid_counter_is_rejected():
    result = validate_robust_placeholder("[[SP_PERSON_001_ABCD]]")
    assert result.is_valid is False
    assert "invalid_counter" in result.issues


def test_zero_counter_is_rejected():
    result = validate_robust_placeholder("[[SP_PERSON_0000_ABCD]]")
    assert result.is_valid is False
    assert "invalid_counter" in result.issues


def test_invalid_integrity_token_shape_is_rejected():
    result = validate_robust_placeholder("[[SP_PERSON_0001_ZZZZ]]")
    assert result.is_valid is False
    assert "invalid_integrity" in result.issues


def test_integrity_mismatch_is_rejected():
    expected = compute_integrity_token("PERSON", "0001")
    wrong = "FFFF" if expected != "FFFF" else "0000"
    result = validate_robust_placeholder(f"[[SP_PERSON_0001_{wrong}]]")
    assert result.is_valid is False
    assert result.expected_integrity == expected
    assert "integrity_mismatch" in result.issues


def test_legacy_placeholder_is_detected_separately():
    result = classify_placeholder("[PERSOON_1]")
    assert is_legacy_placeholder("[PERSOON_1]") is True
    assert result.kind == "legacy"
    assert result.is_valid is True
    assert result.entity_type is None
    assert result.integrity is None


def test_placeholder_like_malformed_string_is_classified():
    result = classify_placeholder("{{SP:PERSON:0001:A7F3}}")
    assert result.kind == "unknown_placeholder_like"
    assert result.is_valid is False


def test_truncated_robust_placeholder_is_rejected():
    result = classify_placeholder("[[SP_PERSON_0001_ABCD]")
    assert result.kind == "malformed_robust"
    assert result.is_valid is False
    assert "missing_closing_double_bracket" in result.issues


def test_ai_mutated_robust_placeholder_is_rejected():
    result = classify_placeholder("[[SP PERSON 0001 ABCD]]")
    assert result.kind == "malformed_robust"
    assert result.is_valid is False
    assert "invalid_prefix" in result.issues


def test_integrity_does_not_use_original_sensitive_values():
    parameters = signature(compute_integrity_token).parameters
    assert "original_value" not in parameters
    assert "sensitive_value" not in parameters
    token_a = compute_integrity_token("PERSON", "0001")
    token_b = compute_integrity_token("PERSON", "0001")
    assert token_a == token_b
    assert "SYNTHETIC" not in token_a
    assert "PERSON" not in token_a
