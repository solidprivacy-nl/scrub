from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = "2026-08-03 23:26 Europe/Amsterdam"


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
    "workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md",
    "Status: implemented; GitHub Actions green; Hugging Face sync and app verification pending",
    "Status: completed and app-verified after GitHub Actions and Hugging Face synchronization verification",
)
replace_once(
    "workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md",
    "- final clean PR run pending after governance status update;\n- Hugging Face sync and app verification required after merge.",
    "- final clean PR run #1926: 1003 passed in 11.51s;\n- deployment verification run #1931: both runtime files matched Hugging Face byte-for-byte, Streamlit health returned HTTP 200 / `ok`, and 1003 tests passed in 11.35s;\n- coordinator/user app verification confirmed at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`",
)

replace_once(
    "handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md",
    "Status: implemented; GitHub Actions green; Hugging Face sync and app verification pending",
    "Status: completed and app-verified after GitHub Actions and Hugging Face synchronization verification",
)
replace_once(
    "handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md",
    "- Corrected PR run #1924: **1003 tests passed in 11.57s**.\n- Hugging Face sync: pending merge.\n- App verification: pending after sync because visible example content changed.",
    "- Corrected PR run #1924: **1003 tests passed in 11.57s**.\n- Final clean PR run #1926: **1003 tests passed in 11.51s**.\n- Deployment verification run #1931 confirmed both changed runtime files matched Hugging Face byte-for-byte on the first attempt, Streamlit health returned HTTP 200 / `ok`, and **1003 tests passed in 11.35s**.\n- App verification confirmed by the coordinator/user at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`",
)
replace_once(
    "handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md",
    "Green on PR #56 run #1924. One final clean regression is required after this handover/claim status update.",
    "Green. Final clean PR #56 run #1926 passed 1003 tests in 11.51s; deployment verification run #1931 passed 1003 tests in 11.35s.",
)
replace_once(
    "handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md",
    "Pending merge. Runtime-relevant files are `care_test_examples.py` and the new `care_test_example_expansions.py`.",
    "Green. `care_test_examples.py` and `care_test_example_expansions.py` matched the Hugging Face Space byte-for-byte; health returned HTTP 200 / `ok`.",
)
replace_once(
    "handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md",
    "Pending after Actions and Hugging Face synchronization are green. Required visible checks:\n\n- all eight Zorgfilter examples remain selectable;\n- each selected example is materially longer than the previous version;\n- the added document sections are visible and readable;\n- existing synthetic identifiers remain present for recognition testing;\n- no Script execution error is visible.",
    "Confirmed by the coordinator/user at 2026-08-03 23:26 Europe/Amsterdam with `Alles werkt.` The longer examples and existing review flow work in the deployed app; no further app verification is required for this package.",
)
replace_once(
    "handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md",
    "Run the final clean PR regression, merge PR #56 when green, verify GitHub-to-Hugging-Face synchronization and request focused live app verification of the eight longer care examples.",
    "Package closed. Treat future document-centric review interactions as separate planning and implementation workpackages.",
)

replace_once(
    "WORKPACKAGES.md",
    "Status: implemented; GitHub Actions, Hugging Face sync and app verification pending.",
    "Status: completed and app-verified after GitHub Actions and Hugging Face synchronization verification.",
)
replace_once(
    "WORKPACKAGES.md",
    "Verification gates:\n- long-form corpus and existing care regression tests;\n- full GitHub Actions suite;\n- GitHub-to-Hugging-Face synchronization;\n- coordinator/user verification that all eight Zorgfilter examples are materially longer, structured and readable.",
    "Verification result:\n- final clean PR run #1926: 1003 tests passed in 11.51s;\n- deployment verification run #1931: both runtime files matched Hugging Face byte-for-byte, Space health HTTP 200 / `ok`, and 1003 tests passed in 11.35s;\n- coordinator/user app verification at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`",
)
prepend_once(
    "WORKPACKAGES.md",
    "SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS_APP_VERIFY_CLOSEOUT",
    f'''## {TIMESTAMP} — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS_APP_VERIFY_CLOSEOUT

Status: completed; final documentation-only GitHub Actions confirmation pending.

Goal:
- Record the coordinator/user confirmation that the deployed long-form synthetic Zorgfilter examples work and close the package without changing product behavior.

Evidence:
```text
PR #56 merge: 1244663d3e69a56d6efc825a6fc019ba72d3782a
Final clean PR run #1926: 1003 passed in 11.51s
Deployment verification run #1931: 1003 passed in 11.35s
Runtime files exact on Hugging Face: 2/2
Space health: HTTP 200 / ok
App verification: confirmed — Alles werkt
```

Boundaries:
- closeout-only;
- no product code, UI, corpus, recognizer, profile, export, Scrub Key or reinsert change;
- no production-readiness claim;
- human review remains mandatory.
''',
)

replace_once(
    "CHANGELOG.md",
    "Status: implemented; validation pending.",
    "Status: completed, synchronized and app-verified.",
)
replace_once(
    "CHANGELOG.md",
    "Validation:\n- targeted and full GitHub Actions pending;\n- Hugging Face sync pending after merge;\n- app verification required because visible example content changed.",
    "Validation:\n- final clean PR run #1926: 1003 tests passed in 11.51s;\n- deployment verification run #1931: both runtime files matched Hugging Face byte-for-byte, Space health returned HTTP 200 / `ok`, and 1003 tests passed in 11.35s;\n- coordinator/user app verification confirmed at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`",
)
prepend_once(
    "CHANGELOG.md",
    "SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS_APP_VERIFY_CLOSEOUT",
    f'''## {TIMESTAMP} — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS_APP_VERIFY_CLOSEOUT

Status: completed; final documentation-only regression pending.

Purpose:
- Close the long-form synthetic Zorgfilter corpus after technical deployment verification and coordinator/user app confirmation.

Files added:
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus_app_verify_closeout.md`
- `handover/workpackages/20260803_2326_care_profile_long_form_synthetic_corpus_app_verify_closeout.md`

Files changed:
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md`
- `handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Validation evidence:
- final clean PR #56 run #1926: 1003 tests passed in 11.51s;
- deployment verification run #1931: exact GitHub/Hugging Face matches for both runtime files, health HTTP 200 / `ok`, and 1003 tests passed in 11.35s;
- coordinator/user confirmation at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`

Intentionally not changed:
- product code, synthetic corpus content, UI, recognizers or profile behavior;
- replacement table, export, Scrub Key or reinsert semantics;
- dependencies, cloud processing or product claims.
''',
)

replace_once(
    "workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus_app_verify_closeout.md",
    "Status: in_progress",
    "Status: completed; final documentation-only GitHub Actions confirmation pending",
)
