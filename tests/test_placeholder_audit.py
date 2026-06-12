from inspect import signature

from placeholder_audit import audit_placeholders, detect_placeholder_like_tokens
from placeholder_validation import compute_integrity_token
from scrub_key import build_scrub_key
from scrub_key_reinsert import reinsert_from_scrub_key


SYNTHETIC_ROWS = [
    {
        "original_value": "BETROKKENE-TEST-A",
        "placeholder": "[PERSOON_1]",
        "entity_type": "PERSON",
        "type_label": "Naam",
        "source": "detected",
        "review_status": "auto_detected",
        "include": True,
        "timestamp": "2026-06-12T10:00:00Z",
    }
]


def _scrub_key():
    return build_scrub_key(SYNTHETIC_ROWS, document_label="WP33 synthetisch testdossier")


def _robust(entity="PERSON", counter="0001"):
    return f"[[SP_{entity}_{counter}_{compute_integrity_token(entity, counter)}]]"


def test_existing_legacy_reinsert_still_works():
    result = reinsert_from_scrub_key("Aanwezig: [PERSOON_1].", _scrub_key())
    assert result["text"] == "Aanwezig: BETROKKENE-TEST-A."
    assert result["replacement_count"] == 1
    assert result["unknown_placeholders"] == []


def test_unknown_legacy_placeholder_remains_visible_in_audit():
    audit = audit_placeholders("Bekend [PERSOON_1], onbekend [ONBEKEND_1].", ["[PERSOON_1]"])
    assert audit["legacy_placeholders"] == ["[PERSOON_1]", "[ONBEKEND_1]"]
    assert audit["unknown_placeholder_like_tokens"] == ["[ONBEKEND_1]"]
    assert audit["placeholder_format_summary"]["unknown_placeholder_like_count"] == 1


def test_valid_robust_placeholder_is_classified():
    placeholder = _robust("PERSON", "0001")
    audit = audit_placeholders(f"Token {placeholder} blijft staan.")
    assert audit["robust_placeholders"] == [placeholder]
    assert audit["malformed_robust_placeholders"] == []
    assert audit["placeholder_validation_issues"] == []


def test_malformed_robust_placeholder_is_reported_without_repair():
    token = "[[XX_PERSON_0001_ABCD]]"
    audit = audit_placeholders(f"Geen repair: {token}")
    assert audit["malformed_robust_placeholders"] == [token]
    assert audit["placeholder_validation_issues"][0]["placeholder"] == token
    assert "invalid_prefix" in audit["placeholder_validation_issues"][0]["issues"]


def test_truncated_robust_placeholder_is_reported():
    token = "[[SP_PERSON_0001_ABCD]"
    audit = audit_placeholders(f"Afgekapt: {token}")
    assert audit["malformed_robust_placeholders"] == [token]
    issues = audit["placeholder_validation_issues"][0]["issues"]
    assert "missing_closing_double_bracket" in issues


def test_integrity_mismatch_is_reported():
    expected = compute_integrity_token("PERSON", "0001")
    wrong = "FFFF" if expected != "FFFF" else "0000"
    token = f"[[SP_PERSON_0001_{wrong}]]"
    audit = audit_placeholders(token)
    assert audit["integrity_failed_placeholders"] == [token]
    issues = audit["placeholder_validation_issues"][0]["issues"]
    assert "integrity_mismatch" in issues


def test_unknown_placeholder_like_token_is_reported():
    token = "{{SP:PERSON:0001:A7F3}}"
    audit = audit_placeholders(f"Alternatief token {token}")
    assert audit["unknown_placeholder_like_tokens"] == [token]
    assert audit["placeholder_validation_issues"][0]["kind"] == "unknown_placeholder_like"


def test_plain_text_without_placeholders_has_empty_audit():
    audit = audit_placeholders("Gewone synthetische tekst zonder tokens.")
    assert audit["observed_placeholder_like_tokens"] == []
    assert audit["legacy_placeholders"] == []
    assert audit["robust_placeholders"] == []
    assert audit["placeholder_validation_issues"] == []
    assert audit["placeholder_format_summary"]["observed_placeholder_like_count"] == 0


def test_integrity_validation_needs_no_original_sensitive_value():
    assert "original_value" not in signature(audit_placeholders).parameters
    placeholder = _robust("CASE_NUMBER", "0002")
    audit = audit_placeholders(placeholder, expected_placeholders=[placeholder])
    assert audit["robust_placeholders"] == [placeholder]
    assert audit["placeholder_validation_issues"] == []


def test_detect_placeholder_like_tokens_is_conservative_and_ordered():
    tokens = detect_placeholder_like_tokens("[PERSOON_1] [PERSOON_1] [[SP_PERSON_0001_ABCD] tekst")
    assert tokens == ["[PERSOON_1]", "[[SP_PERSON_0001_ABCD]"]
