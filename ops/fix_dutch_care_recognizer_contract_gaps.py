from pathlib import Path

path = Path("dutch_care_recognizers.py")
text = path.read_text(encoding="utf-8")

replacements = {
    'r"cl[iië]ntnummer|clientnummer|cl[iië]ntnr\\.?|clientnr\\. ?",':
        'r"cli[eë]ntnummer|clientnummer|cli[eë]ntnr\\.?|clientnr\\.?",',
    'r"behandelnummer|zorgtrajectnummer|behandelnr\\.?|trajectnummer",':
        'r"behandelnummer|zorgtrajectnummer|receptnummer|behandelnr\\.?|trajectnummer",',
    'r"zorgincidentnummer|medicatiefoutnummer",':
        'r"zorgincidentnummer|incidentnummer|medicatiefoutnummer",',
}
for old, new in replacements.items():
    if old not in text:
        raise RuntimeError(f"Expected recognizer source not found: {old}")
    text = text.replace(old, new, 1)

anchor = '''        (
            "labelled_practice_phrase",
            rf"(?P<value>praktijk\\s+(?-i:[A-ZÀ-ÖØ-Þ])[^,\\.\\r\\n]{{1,60}}?)"
            rf"(?=\\s*(?:,|\\.|\\r?$))",
        ),
'''
addition = '''        (
            "location_line_lowercase_care_organization",
            r"\\blocatie\\s*:\\s*(?P<value>(?:woonzorgcentrum|zorgcentrum|"
            r"verpleeghuis|ziekenhuis|zorggroep)\\s+"
            r"(?-i:[A-ZÀ-ÖØ-Þ])[^,\\.\\r\\n]{1,60}?)"
            r"(?=\\s*,\\s*(?:woonlocatie|locatie|afdeling|team|kamer|bed|appartement)\\b)",
        ),
''' + anchor
if anchor not in text:
    raise RuntimeError("Organization pattern insertion anchor not found")
text = text.replace(anchor, addition, 1)

path.write_text(text, encoding="utf-8")
Path("ops/fix_dutch_care_recognizer_contract_gaps.py").unlink(missing_ok=True)
Path(".github/workflows/fix-dutch-care-recognizer-contract-gaps.yml").unlink(missing_ok=True)
