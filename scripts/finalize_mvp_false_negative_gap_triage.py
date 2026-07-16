from __future__ import annotations

import json
import re
from pathlib import Path


TRIAGE = Path("output/validation/mvp_phase6_false_negative_gap_triage.json")
CHANGELOG = Path("CHANGELOG.md")
WORKPACKAGES = Path("WORKPACKAGES.md")
DECISION_LOG = Path("DECISION_LOG.md")
RISK_REGISTER = Path("RISK_REGISTER.md")
CLAIM = Path("workpackage_claims/scrub_wp_mvp_false_negative_gap_triage.md")
HANDOVER = Path("handover/workpackages/20260717_2208_mvp_false_negative_gap_triage.md")

STAMP = "2026-07-17 22:08 Europe/Amsterdam"
PACKAGE = "SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE"


def triage() -> dict:
    data = json.loads(TRIAGE.read_text(encoding="utf-8"))
    if data.get("schema") != "solidprivacy.mvp_phase6_gap_triage":
        raise RuntimeError("Unexpected gap-triage schema")
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

- Classify every evidence gap from the first Phase 6 synthetic validation report.
- Decide whether the evidence justifies recognizer or threshold changes.
- Route document-fidelity and product-boundary findings to the correct next package.

Files added:

- `MVP_PHASE6_FALSE_NEGATIVE_GAP_TRIAGE.md`
- `{TRIAGE}`
- `tests/test_mvp_phase6_false_negative_gap_triage.py`
- `{HANDOVER}`

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `{CLAIM}`

Triage result:

- Input evidence gaps: {data['input_evidence_gap_count']}.
- Reproducible detection false negatives: {data['detection_false_negative_count']}.
- Misclassifications: {data['misclassification_count']}.
- Legal-role over-masking findings: {data['role_over_masking_count']}.
- Recognizer fix required: `{str(data['recognizer_fix_required']).lower()}`.
- Next package: `{data['next_recommended_package']}`.

Decision:

- The DOCX finding is a header/footer reinsert and fidelity-scope issue, not a detection failure.
- The PDF finding is the approved restored-TXT-only/no-OCR product boundary, not a detection failure.
- No recognizer implementation package is opened from this evidence.

Intentionally not changed:

- product recognizers or thresholds;
- replacement semantics;
- document processing or reinsert behavior;
- export, Scrub Key or audit semantics;
- UI, runtime or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.

---

'''
    prepend_if_missing(CHANGELOG, heading, entry)


def update_workpackages(data: dict) -> None:
    heading = f"## {STAMP} — {PACKAGE}"
    entry = f'''{heading}

Status: completed / ready for PR verification.

Summary:
- Classified all {data['input_evidence_gap_count']} evidence items from the Phase 6 synthetic matrix.
- Confirmed that the corrected matrix contains no reproducible false negative, misclassification or role-over-masking result that justifies recognizer changes.
- Routed the DOCX header/footer reinsert limitation and PDF restored-TXT-only boundary to `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.
- Recorded the `.invalid` fixture correction so it cannot reappear as a false product gap.
- No product code or behavior changed.

Validation:
- Machine-readable triage must match every evidence gap in the source report.
- Recognizer fix required: false.
- Production readiness: false.
- Human review remains required.
- GitHub Actions pending final PR validation.
- App verification not applicable.

Active next package:
- `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.

'''
    prepend_if_missing(WORKPACKAGES, heading, entry)


def update_decision_log() -> None:
    heading = "## 2026-07-17 — D029 — Current Phase 6 matrix does not justify a recognizer fix"
    entry = f'''{heading}

Status: accepted evidence-routing decision

Decision:

```text
Do not open a recognizer or threshold implementation package from the first corrected Phase 6 synthetic matrix.
```

Reason:

- The corrected matrix contains no reproducible detection false negative, misclassification or legal-role over-masking evidence.
- The DOCX result concerns header/footer reinsert fidelity and helper scope.
- The PDF result reflects the approved restored-TXT-only/no-OCR product boundary.
- Treating either item as a recognizer problem would target the wrong layer and weaken evidence discipline.

Consequences:

- Route both findings to `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.
- Preserve current recognizer and threshold behavior.
- Keep the PDF limitation explicit; do not infer OCR or restored-PDF authorization.
- Preserve human review and the no-production-readiness-claim boundary.

Evidence:

- `{TRIAGE}`
- `output/validation/mvp_phase6_synthetic_validation_report.json`

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
            raise RuntimeError("Decision log header anchor not found")
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
        "The first machine-readable matrix baseline is stored in `output/validation/mvp_phase6_synthetic_validation_report.json` with 3 synthetic cases and 2 recorded evidence gaps or known limitations.",
        "Triage confirms that neither remaining item is a detection false negative, so no recognizer fix is justified by this bounded baseline.",
        "R1 triage decision",
    )
    text = append_sentence_once(
        text,
        "The Phase 6 synthetic DOCX case now records header/footer findings and the existing main-document-only reinsert boundary as reproducible evidence for the document-hygiene hardening package.",
        "Gap triage classifies this as document fidelity and reinsert scope and routes it to `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.",
        "R4 triage route",
    )
    text = append_sentence_once(
        text,
        "The Phase 6 text-based PDF case verifies the current restored-TXT-only path and explicitly records that restored PDF and OCR are unsupported.",
        "Gap triage retains this as an explicit product boundary and does not authorize OCR or restored-PDF work.",
        "R7 triage route",
    )
    text = append_sentence_once(
        text,
        "The Phase 6 synthetic matrix is now the evidence source for `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE`; only reproducible under-detection, misclassification or role-over-masking findings may open a subsequent fix package.",
        "The first triage found none of those categories; recognizer behavior remains unchanged.",
        "R9 triage result",
    )
    RISK_REGISTER.write_text(text, encoding="utf-8")


def update_claim(data: dict) -> None:
    claim = CLAIM.read_text(encoding="utf-8")
    claim = re.sub(
        r"^Status: .+$",
        "Status: completed / ready for PR verification",
        claim,
        count=1,
        flags=re.MULTILINE,
    )
    if "Triage result:" not in claim:
        claim += f'''\n\nTriage result:\n- Completed at: {STAMP}\n- Input evidence gaps: {data['input_evidence_gap_count']}\n- Detection false negatives: {data['detection_false_negative_count']}\n- Recognizer fix required: {str(data['recognizer_fix_required']).lower()}\n- Triage artifact: `{TRIAGE}`\n- Handover: `{HANDOVER}`\n- Next package: `{data['next_recommended_package']}`\n'''
    CLAIM.write_text(claim, encoding="utf-8")


def write_handover(data: dict) -> None:
    HANDOVER.parent.mkdir(parents=True, exist_ok=True)
    HANDOVER.write_text(
        f'''# Handover — {PACKAGE}

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

{PACKAGE}

## Status

Completed / ready for PR verification.

## Files added

- `MVP_PHASE6_FALSE_NEGATIVE_GAP_TRIAGE.md`
- `{TRIAGE}`
- `tests/test_mvp_phase6_false_negative_gap_triage.py`
- `{HANDOVER}`

## Files changed

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `{CLAIM}`

## Tests

- Triage schema and product-claim boundaries.
- One-to-one coverage of source evidence gaps.
- No recognizer-fix claim without detection evidence.
- Correct routing of DOCX and PDF findings.
- Methodology correction and human-review boundary.

## Validation status

- Input gaps: {data['input_evidence_gap_count']}.
- Detection false negatives: {data['detection_false_negative_count']}.
- Misclassifications: {data['misclassification_count']}.
- Role over-masking findings: {data['role_over_masking_count']}.
- Recognizer fix required: {data['recognizer_fix_required']}.
- Product code changed: no.

## GitHub Actions status

Pending final PR validation.

## Hugging Face sync status

Not functionally relevant; no app code or UI changed.

## App verification status

Not applicable.

## Remaining risks

- The synthetic matrix remains bounded and is not a production recall/precision benchmark.
- DOCX header/footer reinsert fidelity remains unresolved.
- PDF remains restored TXT only, without OCR or restored PDF output.
- Human review remains mandatory.

## Next recommended step

Start `{data['next_recommended_package']}`.
''',
        encoding="utf-8",
    )


def main() -> None:
    data = triage()
    update_changelog(data)
    update_workpackages(data)
    update_decision_log()
    update_risk_register()
    update_claim(data)
    write_handover(data)
    print(
        f"Finalized {PACKAGE}: {data['input_evidence_gap_count']} input gaps, "
        f"recognizer_fix_required={data['recognizer_fix_required']}."
    )


if __name__ == "__main__":
    main()
