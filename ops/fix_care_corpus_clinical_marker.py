from pathlib import Path

path = Path("care_test_examples.py")
text = path.read_text(encoding="utf-8")
old = '            "acute nierinsufficiëntie",\n'
new = '            "Hoofddiagnose: acute nierinsufficiëntie",\n'
if old not in text:
    raise RuntimeError("Expected discharge-letter preserve marker not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
Path("ops/fix_care_corpus_clinical_marker.py").unlink(missing_ok=True)
Path(".github/workflows/fix-care-corpus-clinical-marker.yml").unlink(missing_ok=True)
