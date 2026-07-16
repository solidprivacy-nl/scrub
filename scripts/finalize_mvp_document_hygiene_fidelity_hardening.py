from __future__ import annotations

import json
import re
from pathlib import Path


REPORT = Path(
    "output/validation/mvp_phase6_document_hygiene_fidelity_hardening_report.json"
)
CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
RELEASE_NOTES = Path("RELEASE_NOTES.md")
DECISION_LOG = Path("DECISION_LOG.md")
RISK_REGISTER = Path("RISK_REGISTER.md")
CLAIM = Path(
    "workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md"
)
HANDOVER = Path(
    "handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md"
)

STAMP = "2026-07-17 22:30 Europe/Amsterdam"
PACKAGE = "SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING"


def report() -> dict:
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    if data.get("schema") != (
        "solidprivacy.mvp_phase6_document_fidelity_hardening_report"
    ):
        raise RuntimeError("Unexpected document-fidelity report schema")
    return data


def prepend_if_missing(path: Path, heading: str, entry: str) -> None:
    text = path.read_text(encoding="utf-8")
    if heading not in text:
        path.write_text(entry + text, encoding="utf-8")


def update_changelog(data: dict) -> None:
    heading = f"## 2026-07-17 — {PACKAGE}"
    entry = f'''{heading}

Status: completed / ready for PR verification.

Purpose:

- Resolve the reproducible DOCX header/footer reinsert fidelity gap from the Phase 6 matrix.
- Preserve DOCX hygiene visibility and explicit unsupported-part boundaries.
- Keep the PDF restored-TXT-only/no-OCR boundary unchanged.

Files added:

- `mvp_document_fidelity_report.py`
- `scripts/run_mvp_document_hygiene_fidelity_report.py`
- `tests/test_mvp_document_hygiene_fidelity_hardening.py`
- `tests/test_mvp_document_fidelity_report.py`
- `{REPORT}`
- `{HANDOVER}`

Files changed:

- `scrub_key_document_reinsert.py`
- `mvp_phase6_document_cases.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `{CLAIM}`

Implementation result:

- DOCX body paragraphs and tables remain supported.
- `word/header*.xml` and `word/footer*.xml` text nodes are now restored deterministically.
- The synthetic header/footer residual-placeholder finding is resolved: `{str(data['docx_header_footer_reinsert_resolved']).lower()}`.
- Resolved findings: {data['resolved_finding_count']}.
- Remaining findings: {data['remaining_finding_count']}.
- The remaining finding is the explicit PDF restored-TXT-only/no-OCR product boundary.

Intentionally not changed:

- recognizers, thresholds or replacement semantics;
- Scrub Key schema or lifecycle;
- DOCX comments, tracked-change-only parts, footnotes/endnotes, text boxes or metadata;
- split-placeholder support across Word text nodes;
- export filenames or MIME types;
- restored PDF or OCR support;
- Streamlit UI, runtime or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

---

'''
    prepend_if_missing(CHANGELOG, heading, entry)


def update_workpackages(data: dict) -> None:
    heading = f"## {STAMP} — {PACKAGE}"
    entry = f'''{heading}

Status: completed / ready for PR verification.

Summary:
- Extended deterministic DOCX reinsert from `word/document.xml` to existing `word/header*.xml` and `word/footer*.xml` text nodes.
- Preserved body/table behavior and unrelated OOXML package parts.
- Kept comments, tracked-change-only parts, footnotes/endnotes, text boxes, metadata and split placeholders explicitly unsupported.
- Regenerated current Phase 6 evidence without overwriting the historical baseline/triage artifacts.
- Resolved the DOCX header/footer finding and retained the PDF TXT-only/no-OCR boundary.

Validation:
- DOCX header/footer resolution: {data['docx_header_footer_reinsert_resolved']}.
- Resolved findings: {data['resolved_finding_count']}.
- Remaining findings: {data['remaining_finding_count']}.
- Production readiness: false.
- Human review remains required.
- GitHub Actions pending final PR validation.
- Hugging Face sync required after merge because reinsert behavior changed.
- Live app verification required for the DOCX reinsert path after sync.

Active next package after verification:
- `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

'''
    prepend_if_missing(WORKPACKAGES, heading, entry)


def update_release_notes() -> None:
    heading = "## 2026-07-17 — DOCX-herstel omvat nu kop- en voetteksten"
    entry = f'''{heading}

- Bij het terugzetten van originele waarden in een DOCX worden nu ook bestaande kop- en voetteksten meegenomen.
- Hoofdtekst en tabellen blijven ondersteund.
- Opmerkingen, alleen-in-wijzigingen aanwezige tekst, voetnoten/eindnoten, tekstvakken, metadata en placeholders die over meerdere Word-tekstnodes zijn verdeeld, blijven buiten deze versie.
- PDF-herstel blijft beperkt tot herstelde TXT; OCR en een hersteld PDF-bestand zijn niet toegevoegd.

---

'''
    prepend_if_missing(RELEASE_NOTES, heading, entry)


def update_decision_log() -> None:
    heading = "## 2026-07-17 — D030 — Restore existing DOCX header and footer text during deterministic reinsert"
    entry = f'''{heading}

Status: accepted implementation decision

Decision:

```text
Extend the existing local deterministic DOCX reinsert helper to process WordprocessingML text nodes in word/header*.xml and word/footer*.xml in addition to word/document.xml.
```

Reason:

- The scrubbed DOCX export already replaces reviewed values in body, table, header and footer paragraphs.
- The Phase 6 matrix showed that reinsert restored body/table values but left header/footer placeholders behind.
- The gap belongs to document fidelity and reinsert scope, not detection or recognizer behavior.

Boundaries:

- Process only existing body, header and footer WordprocessingML text nodes.
- Preserve unrelated OOXML package parts byte-for-byte where they are not rewritten.
- Do not claim support for comments, tracked-change-only parts, footnotes/endnotes, text boxes, metadata or placeholders split across text nodes.
- Do not add OCR or restored-PDF behavior.
- Keep processing local, deterministic and Scrub Key driven.

Evidence:

- `{REPORT}`
- `output/validation/mvp_phase6_false_negative_gap_triage.json`

---

'''
    text = DECISION_LOG.read_text(encoding="utf-8")
    if heading not in text:
        anchor = (
            "# SolidPrivacy Scrub — Decision Log\n\n"
            "This file records accepted strategic, product and architecture decisions.\n\n"
            "---\n\n"
        )
        if anchor not in text:
            raise RuntimeError("Decision log anchor not found")
        DECISION_LOG.write_text(text.replace(anchor, anchor + entry, 1), encoding="utf-8")


def append_sentence_once(text: str, anchor: str, sentence: str, label: str) -> str:
    if sentence in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"{label}: anchor not found")
    return text.replace(anchor, anchor + " " + sentence, 1)


def update_risk_register() -> None:
    text = RISK_REGISTER.read_text(encoding="utf-8")
    text = append_sentence_once(
        text,
        "Gap triage classifies this as document fidelity and reinsert scope and routes it to `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.",
        "The hardening package now restores placeholders in existing DOCX header and footer XML parts while retaining hygiene reporting and explicit unsupported-part warnings.",
        "R4 hardening result",
    )
    text = append_sentence_once(
        text,
        "Gap triage retains this as an explicit product boundary and does not authorize OCR or restored-PDF work.",
        "Document-fidelity hardening preserves that boundary unchanged.",
        "R7 boundary preservation",
    )
    RISK_REGISTER.write_text(text, encoding="utf-8")


def update_claim(data: dict) -> None:
    claim = CLAIM.read_text(encoding="utf-8")
    claim = re.sub(
        r"^Status: .+$",
        "Status: completed / ready for app verification",
        claim,
        count=1,
        flags=re.MULTILINE,
    )
    if "Hardening result:" not in claim:
        claim += f'''\n\nHardening result:\n- Completed at: {STAMP}\n- DOCX header/footer reinsert resolved: {str(data['docx_header_footer_reinsert_resolved']).lower()}\n- Resolved findings: {data['resolved_finding_count']}\n- Remaining findings: {data['remaining_finding_count']}\n- Report: `{REPORT}`\n- Handover: `{HANDOVER}`\n- App verification required after Actions and Hugging Face sync.\n'''
    CLAIM.write_text(claim, encoding="utf-8")


def write_handover(data: dict) -> None:
    HANDOVER.parent.mkdir(parents=True, exist_ok=True)
    HANDOVER.write_text(
        f'''# Handover — {PACKAGE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{PACKAGE}

## Status

Completed / ready for app verification.

## Files added

- `mvp_document_fidelity_report.py`
- `scripts/run_mvp_document_hygiene_fidelity_report.py`
- `tests/test_mvp_document_hygiene_fidelity_hardening.py`
- `tests/test_mvp_document_fidelity_report.py`
- `{REPORT}`
- `{HANDOVER}`

## Files changed

- `scrub_key_document_reinsert.py`
- `mvp_phase6_document_cases.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `{CLAIM}`

## Tests

- Existing TXT/DOCX Scrub Key document-reinsert suite.
- New body/table/header/footer end-to-end DOCX tests.
- OOXML package preservation and malformed-header fail-safe tests.
- Current Phase 6 synthetic matrix tests.
- Fidelity report and PDF-boundary tests.
- Existing DOCX hygiene and document-tool tests.
- Python compilation and `git diff --check`.

## Validation status

- DOCX header/footer finding resolved: {data['docx_header_footer_reinsert_resolved']}.
- Resolved findings: {data['resolved_finding_count']}.
- Remaining findings: {data['remaining_finding_count']}.
- PDF TXT-only/no-OCR boundary preserved: {data['pdf_boundary_preserved']}.
- Local-only deterministic processing retained.
- Human review remains required.
- Production readiness remains false.

## GitHub Actions status

Pending final PR validation.

## Hugging Face sync status

Pending after merge.

## App verification status

Required after sync because DOCX reinsert behavior changed.

## Remaining risks

- Comments, tracked-change-only parts, footnotes/endnotes, text boxes and metadata remain unsupported by reinsert.
- Placeholders split across Word text nodes remain unsupported.
- PDF remains restored TXT only; no OCR or restored PDF output.
- DOCX hygiene audit remains report-only and does not guarantee a clean document.

## Next recommended step

After app verification, start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.
''',
        encoding="utf-8",
    )


def main() -> None:
    data = report()
    update_changelog(data)
    update_workpackages(data)
    update_release_notes()
    update_decision_log()
    update_risk_register()
    update_claim(data)
    write_handover(data)
    print(
        f"Finalized {PACKAGE}: resolved={data['resolved_finding_count']}, "
        f"remaining={data['remaining_finding_count']}."
    )


if __name__ == "__main__":
    main()
