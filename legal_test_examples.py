"""Small optional smoke test for the Dutch Legal Strict recognizer pack.

Run locally in the Space environment with:
python test_dutch_legal_recognizers.py

This is not required for the Streamlit app to run, but it helps validate that
recognizers can be imported and basic expected entities are available.
"""

from presidio_analyzer import AnalyzerEngine, RecognizerRegistry

from dutch_recognizers import get_dutch_recognizers, get_dutch_entity_names
from legal_test_examples import TEST_CASES


def build_test_analyzer():
    registry = RecognizerRegistry()
    registry.load_predefined_recognizers()
    for recognizer in get_dutch_recognizers(supported_language="en"):
        registry.add_recognizer(recognizer)
    return AnalyzerEngine(registry=registry, supported_languages=["en"])


def main():
    analyzer = build_test_analyzer()
    entities = get_dutch_entity_names(include_legal=True) + [
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "EMAIL_ADDRESS",
        "PHONE_NUMBER",
        "IBAN_CODE",
        "DATE_TIME",
    ]

    failed = []
    for case in TEST_CASES:
        results = analyzer.analyze(
            text=case["text"],
            language="en",
            entities=entities,
            score_threshold=0.25,
        )
        found = {result.entity_type for result in results}
        missing = sorted(set(case.get("should_contain", [])) - found)
        forbidden = sorted(set(case.get("should_not_contain", [])) & found)
        if missing or forbidden:
            failed.append((case["name"], missing, forbidden, sorted(found)))

    if failed:
        for name, missing, forbidden, found in failed:
            print(f"FAILED: {name}")
            print(f"  missing: {missing}")
            print(f"  forbidden: {forbidden}")
            print(f"  found: {found}")
        raise SystemExit(1)

    print(f"OK: {len(TEST_CASES)} Dutch legal recognizer smoke test cases passed.")


if __name__ == "__main__":
    main()
