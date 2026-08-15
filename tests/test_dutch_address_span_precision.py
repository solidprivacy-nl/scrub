from presidio_analyzer import RecognizerResult

from dutch_address_span_precision import tighten_dutch_address_results
from dutch_recognizers import get_dutch_entity_names, get_dutch_recognizers


LIVE_CONTEXTS = [
    "Beschrijving Polderweg 8",
    "De inspectie bezoekt Polderweg 8",
    "Nu Polderweg 8 de",
    "Op Polderweg 8",
    "Polderweg 8 een",
    "Polderweg 8 en",
    "Polderweg 8 in",
    "Polderweg 8 is",
    "Polderweg 8 na",
    "Polderweg 8 op",
]


def _raw_address_results(text: str):
    entities = get_dutch_entity_names(include_legal=True)
    results = []
    for recognizer in get_dutch_recognizers(supported_language="en"):
        if "NL_ADDRESS" not in getattr(recognizer, "supported_entities", []):
            continue
        if hasattr(recognizer, "load"):
            recognizer.load()
        results.extend(recognizer.analyze(text, entities=entities, nlp_artifacts=None))
    return [result for result in results if result.entity_type == "NL_ADDRESS"]


def _values(text: str, results):
    return [text[result.start : result.end] for result in results]


def test_live_polderweg_contexts_resolve_to_exact_address_only():
    for text in LIVE_CONTEXTS:
        raw = _raw_address_results(text)
        assert raw, f"baseline recognizer unexpectedly missed address in: {text!r}"
        resolved = tighten_dutch_address_results(text, raw)
        values = _values(text, resolved)
        assert "Polderweg 8" in values, (text, values)
        assert all(value == "Polderweg 8" for value in values), (text, values)


def test_house_number_does_not_absorb_short_adjacent_words():
    for suffix in ("een", "en", "in", "is", "na", "op", "de"):
        text = f"Polderweg 8 {suffix}"
        broad = RecognizerResult(entity_type="NL_ADDRESS", start=0, end=len(text), score=0.66)
        [resolved] = tighten_dutch_address_results(text, [broad])
        assert text[resolved.start : resolved.end] == "Polderweg 8"


def test_legitimate_prefix_address_with_postcode_and_city_is_preserved():
    text = "Verweerder woont aan Laan van Meerdervoort 55, 2517 AM Den Haag."
    start = text.index("Laan")
    end = text.index(".")
    broad = RecognizerResult(entity_type="NL_ADDRESS", start=start, end=end, score=0.70)
    [resolved] = tighten_dutch_address_results(text, [broad])
    assert text[resolved.start : resolved.end] == "Laan van Meerdervoort 55, 2517 AM Den Haag"


def test_common_suffix_street_forms_remain_detectable():
    examples = (
        "Polderweg 8",
        "Kerkstraat 12A",
        "Nieuwe Kerkstraat 14",
        "Westersingel 101-2",
    )
    for address in examples:
        broad = RecognizerResult(entity_type="NL_ADDRESS", start=0, end=len(address), score=0.66)
        [resolved] = tighten_dutch_address_results(address, [broad])
        assert address[resolved.start : resolved.end] == address


def test_unknown_address_shape_is_preserved_fail_safe_instead_of_dropped():
    text = "Onbekende adresvorm 42"
    original = RecognizerResult(entity_type="NL_ADDRESS", start=0, end=len(text), score=0.66)
    [resolved] = tighten_dutch_address_results(text, [original])
    assert resolved.start == original.start
    assert resolved.end == original.end


def test_non_address_results_are_untouched():
    text = "Polderweg 8"
    original = RecognizerResult(entity_type="LOCATION", start=0, end=len(text), score=0.7)
    [resolved] = tighten_dutch_address_results(text, [original])
    assert resolved is original
