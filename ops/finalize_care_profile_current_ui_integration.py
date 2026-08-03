from __future__ import annotations

from pathlib import Path


TIMESTAMP = "2026-08-03 18:28 Europe/Amsterdam"
WP = "SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION"


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def prepend_once(path: str, marker: str, block: str) -> None:
    current = read(path)
    if marker not in current:
        write(path, block.rstrip() + "\n\n" + current)


def update_roadmap() -> None:
    path = "ROADMAP.md"
    text = read(path)
    anchor = (
        "Central profile configuration is now implemented without changing the live UI. "
        "The current three options remain exact, while future Streamlit and desktop "
        "four-profile orders, thresholds, entity groups, care policy actions and fifteen "
        "exact-span precedence winners are frozen. Care recognizer registration and visible "
        "UI integration remain the next gated package."
    )
    addition = anchor + (
        "\n\nThe current Streamlit integration is now implemented and regression-green. "
        "`Zorgcontrole — streng` is added without silently becoming the default; the existing "
        "Legal profile remains initially selected. Sixteen care recognizers, central entity "
        "composition, exact-span precedence, eight synthetic examples and conservative unchecked "
        "care candidates are wired into the current flow. Review-selected care detections remain "
        "selected but show `Controle nodig`. Export, Scrub Key and reinsert semantics are unchanged. "
        "The next gates are cross-profile regression, deployment sync and live app verification."
    )
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("ROADMAP integration anchor not found")
        write(path, text.replace(anchor, addition, 1))


def update_workpackages() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: implemented and regression-green; merge, sync and deployed app verification pending.

Goal:
- Register and expose the approved Zorgfilter v1 profile in the current Streamlit flow without changing export, Scrub Key or reinsert semantics.

Result:

```text
Visible profiles: 4
Default profile: Juridische controle — streng
Dedicated care recognizers registered: 16
Synthetic care examples: 8
Care candidates: review-only and unchecked
Review-selected detections: selected by default, status Controle nodig
GitHub Actions run #1877: 983 tests passed
Export semantics changed: false
Scrub Key semantics changed: false
Reinsert semantics changed: false
Production ready: false
```

Implementation:
- central profile configuration drives labels, thresholds and entity composition;
- exact-span care/legacy and AGB/BSN collision resolution runs before the replacement table;
- conservative strongly-labelled care candidate scanner added;
- user-facing care labels, placeholders and generalized product copy added;
- Legal remains the initial default and no profile changes silently;
- clinical meaning remains a preservation target.

Evidence:
- `CARE_PROFILE_CURRENT_UI_INTEGRATION.md`
- `output/validation/care_profile_current_ui_integration.json`
- `handover/workpackages/20260803_1828_care_profile_current_ui_integration.md`

Active next package:
- `SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX`

Required later gate:
- `SCRUB-WP_CARE_PROFILE_APP_VERIFY` after merge and deployment sync.

Boundaries:
- human review remains required;
- synthetic evidence does not prove production recall or precision;
- no cloud document processing or new dependency;
- no export filename, MIME type, Scrub Key schema/binding or reinsert behavior change.
"""
    prepend_once("WORKPACKAGES.md", marker, block)


def update_changelog() -> None:
    marker = f"## {TIMESTAMP} — {WP}"
    block = f"""## {TIMESTAMP} — {WP}

Status: implemented and regression-tested; deployment verification pending.

Purpose:
- Promote the approved Zorgfilter profile into the current Streamlit/analyzer flow after policy, corpus, recognizer and profile-configuration gates passed.

Files added:
- `care_candidate_scanner.py`
- `profile_ui_support.py`
- `CARE_PROFILE_CURRENT_UI_INTEGRATION.md`
- `output/validation/care_profile_current_ui_integration.json`
- `tests/test_care_candidate_scanner.py`
- `tests/test_profile_ui_support.py`
- `tests/test_presidio_helpers_care_registration.py`
- `tests/test_care_profile_current_ui_integration_snapshot.py`
- `workpackage_claims/scrub_wp_care_profile_current_ui_integration.md`
- `handover/workpackages/20260803_1828_care_profile_current_ui_integration.md`

Files changed:
- `presidio_helpers.py`
- `presidio_streamlit.py`
- `document_tools.py`
- `display_labels_nl.py`
- `ui_texts_nl.py`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Implementation result:
- registered sixteen dedicated care recognizers;
- added `Zorgcontrole — streng` while preserving the existing three labels and Legal default;
- centralized thresholds, profile descriptions and default entity composition;
- applied profile-level exact-span collision resolution;
- added eight synthetic care examples and a conservative unchecked candidate layer;
- aligned review-selected care detections to `Controle nodig` while keeping them selected;
- added care display labels and stable placeholders;
- generalized app copy from Legal-only to professional Legal/Zorg use;
- preserved review table, export, Scrub Key and reinsert semantics.

Validation:
- run #1876 failed only because the new registration test imported optional Streamlit dependencies absent from lean CI;
- test isolation was corrected without changing runtime code or dependencies;
- run #1877 passed: 983 tests in 9.69s;
- final clean run pending after governance finalization;
- Hugging Face sync pending merge;
- app verification pending deployment.

Intentionally not changed:
- export filenames, MIME types and document formats;
- Scrub Key schema, binding, warnings or lifecycle;
- TXT/DOCX/PDF-to-TXT reinsert semantics;
- cloud processing, runtime dependencies or production claims;
- broad free-text medical scanning.
"""
    prepend_once("CHANGELOG.md", marker, block)


def update_release_notes() -> None:
    marker = "## 2026-08-03 — Zorgcontrole toegevoegd aan het prototype"
    block = """## 2026-08-03 — Zorgcontrole toegevoegd aan het prototype

- De controlemodus krijgt een vierde keuze: `Zorgcontrole — streng`.
- De bestaande juridische controle blijft de standaardkeuze; Zorg wordt nooit stilzwijgend geactiveerd.
- Zorgcontrole zoekt extra naar patiënt- en cliëntnummers, EPD/ECD- en dossiernummers, verzekerden- en verwijsnummers, laboratorium- en incidentreferenties, zorgverleners, zorgorganisaties, locaties en exacte zorgdata.
- Acht volledig synthetische zorgvoorbeelden zijn beschikbaar om de werking te testen.
- Zorgverlener-, organisatie-, locatie- en zorgdatumregels blijven standaard geselecteerd, maar krijgen zichtbaar de status `Controle nodig`.
- Mogelijke gemiste administratieve zorgreferenties worden alleen als uitgevinkte controlekandidaat toegevoegd.
- Diagnose, medicatie, doseringen, laboratoriumwaarden en observaties blijven een expliciet te behouden onderdeel van de tekst.
- De vervangtabel, documentdownloads, Scrub Key, terugzetten en bestandsformaten zijn niet gewijzigd.
- Menselijke controle blijft noodzakelijk; deze prototypefunctie is geen productiegarantie.

---
"""
    prepend_once("RELEASE_NOTES.md", marker, block)


def update_risk_register() -> None:
    path = "RISK_REGISTER.md"
    text = read(path)
    anchor = (
        "The central profile model now freezes Care composition and exact-span precedence "
        "without changing the live application. Risk R10 remains open until the current app "
        "registers the care recognizers, uses the profile policy, runs cross-profile regression "
        "and passes deployed app verification."
    )
    addition = anchor + (
        "\n\nThe current Streamlit integration now registers the sixteen care recognizers and "
        "applies the central profile policy. Review-selected care detections are selected by "
        "default but visibly marked `Controle nodig`; unresolved strongly labelled references "
        "remain unchecked candidates. Regression run #1877 passed 983 tests and existing export, "
        "Scrub Key and reinsert behavior remains unchanged. Risk R10 remains mitigating because "
        "cross-profile regression, deployment sync, generic-NER observation and live app verification "
        "are still pending."
    )
    if addition not in text:
        if anchor not in text:
            raise RuntimeError("RISK_REGISTER integration anchor not found")
        write(path, text.replace(anchor, addition, 1))


def update_claim() -> None:
    path = "workpackage_claims/scrub_wp_care_profile_current_ui_integration.md"
    text = read(path)
    text = text.replace(
        "Status: in_progress",
        "Status: implemented; merge, sync and app verification pending",
        1,
    )
    write(path, text)


def main() -> None:
    update_roadmap()
    update_workpackages()
    update_changelog()
    update_release_notes()
    update_risk_register()
    update_claim()

    Path("ops/finalize_care_profile_current_ui_integration.py").unlink(missing_ok=True)
    Path(".github/workflows/finalize-care-profile-current-ui-integration.yml").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
