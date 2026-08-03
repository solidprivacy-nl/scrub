from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-08-03 22:17 Europe/Amsterdam"


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one match in {path}, found {count}: {old!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


def prepend_once(path: str, marker: str, entry: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if marker in text:
        raise RuntimeError(f"Entry already present in {path}: {marker}")
    target.write_text(entry.rstrip() + "\n\n" + text, encoding="utf-8")


replace_once(
    "care_test_examples.py",
    "]\n\n\ndef get_case(case_id: str) -> Dict[str, Any]:",
    "]\n\n\nfrom care_test_example_expansions import expand_case_texts as _expand_case_texts\n\nTEST_CASES = _expand_case_texts(TEST_CASES)\n\n\ndef get_case(case_id: str) -> Dict[str, Any]:",
)

prepend_once(
    "WORKPACKAGES.md",
    "SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS",
    f'''## {TIMESTAMP} — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS

Status: implemented; GitHub Actions, Hugging Face sync and app verification pending.

Goal:
- Replace the short tester-facing care examples with longer, structured synthetic documents while preserving every existing recognition and policy contract.

Implementation result:

```text
Stable care-document families: 8
Added document-specific sections per example: 5
Minimum added narrative per example: 200 words
Minimum total visible length per example: 250 words
New identifying values in additions: 0
Digits in additions: 0
Recognizer/profile policy changed: false
Export/Scrub Key/reinsert semantics changed: false
```

Files added:
- `care_test_example_expansions.py`
- `tests/test_care_profile_long_form_corpus.py`
- `CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS.md`
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md`
- `handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md`

Files changed:
- `care_test_examples.py`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Verification gates:
- long-form corpus and existing care regression tests;
- full GitHub Actions suite;
- GitHub-to-Hugging-Face synchronization;
- coordinator/user verification that all eight Zorgfilter examples are materially longer, structured and readable.

Boundaries:
- synthetic data only;
- no recognizer, threshold, collision or profile-policy change;
- no review-table, export, Scrub Key or reinsert change;
- no dependency or cloud-processing change;
- human review and non-production boundaries remain unchanged.
''',
)

prepend_once(
    "CHANGELOG.md",
    "SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS",
    f'''## {TIMESTAMP} — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS

Status: implemented; validation pending.

Purpose:
- Give Zorgfilter testers realistic long-form care documents instead of examples that stop after one short clinical paragraph.

Files added:
- `care_test_example_expansions.py`
- `tests/test_care_profile_long_form_corpus.py`
- `CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS.md`
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md`
- `handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md`

Files changed:
- `care_test_examples.py`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Implementation result:
- retained all eight stable care-document IDs, names, sectors and document types;
- retained every replace, review-selected, preserve, audit-only and ambiguity-trap contract;
- appended five document-specific sections and at least two hundred words of synthetic care context to every example;
- kept the additions free of digits and new names, identifiers, dates, addresses, contact details, organizations and locations;
- exposed the expanded texts through the existing Zorgfilter example selector without changing the selector or Streamlit flow;
- added tests for length, structure, non-mutation, identity-marker absence, exact expected-value occurrence and UI-adapter parity.

Validation:
- targeted and full GitHub Actions pending;
- Hugging Face sync pending after merge;
- app verification required because visible example content changed.

Intentionally not changed:
- recognizers, thresholds, profile composition or collision precedence;
- review selection or replacement-table behavior;
- export filenames, MIME types or formats;
- Scrub Key schema, binding, warnings or lifecycle;
- reinsert behavior, dependencies, cloud processing or production claims.
''',
)

prepend_once(
    "RELEASE_NOTES.md",
    "Langere synthetische zorgvoorbeelden",
    '''## 2026-08-03 — Langere synthetische zorgvoorbeelden

- De acht voorbeelden onder `Zorgcontrole — streng` bevatten nu langere, realistisch opgebouwde zorgteksten.
- Elk voorbeeld krijgt vijf herkenbare inhoudssecties, bijvoorbeeld observaties, beoordeling, zorgacties en vervolgafspraken.
- De bestaande synthetische namen, nummers en andere testwaarden blijven gelijk, zodat herkenningsresultaten vergelijkbaar blijven.
- De extra tekst introduceert geen nieuwe persoonsnamen, identificatienummers, data, adressen of contactgegevens.
- Diagnose, medicatie, observaties, laboratoriuminformatie en andere klinische betekenis blijven leesbare testcontext.
- Herkenning, vervangtabel, export, Scrub Key en terugzetten zijn niet gewijzigd.
- Menselijke controle blijft noodzakelijk; de voorbeelden zijn synthetische testdocumenten en geen productiebenchmark.

---''',
)

replace_once(
    "RISK_REGISTER.md",
    "\n---\n\n## Product-claim boundary",
    "\nThe tester-facing care corpus now uses long-form structured variants across all eight approved document families. Each addition supplies substantial clinical and workflow context without adding new names, identifiers, dates, addresses, contact details, organizations, locations or digits. This improves usability and preservation testing but does not change recognizer behavior or establish production recall, precision or rare-case safety.\n\n---\n\n## Product-claim boundary",
)

replace_once(
    "workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md",
    "Status: in_progress",
    "Status: implemented; GitHub Actions, Hugging Face sync and app verification pending",
)
