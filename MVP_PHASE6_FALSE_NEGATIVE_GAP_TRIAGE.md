# SolidPrivacy Scrub — MVP Phase 6 false-negative gap triage

Status: completed evidence classification; pending PR validation.

Source evidence:

```text
output/validation/mvp_phase6_synthetic_validation_report.json
```

Machine-readable decision:

```text
output/validation/mvp_phase6_false_negative_gap_triage.json
```

## Executive decision

The corrected synthetic matrix does **not** contain a reproducible detection false negative, misclassification or legal-role over-masking result that justifies changing recognizers or thresholds now.

The two remaining evidence items are:

1. a DOCX document-fidelity and reinsert-scope limitation affecting headers and footers;
2. the approved PDF product boundary: restored TXT only, with no restored PDF and no OCR.

Both findings are routed to:

```text
SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING
```

No recognizer fix package should be opened from this triage.

## Classification 1 — DOCX header/footer reinsert

Observed:

- main document body paragraphs and tables are restored;
- placeholders in the synthetic header and footer remain after DOCX reinsert;
- DOCX hygiene audit reports both headers and footers;
- the current helper explicitly processes only `word/document.xml`.

Classification:

```text
document_fidelity_and_reinsert_scope
```

This is not a detection false negative. Sensitive values were replaced in the scrubbed DOCX, but deterministic reinsert does not currently restore header/footer values. The next package must decide how to harden fidelity without weakening hidden-content controls or silently changing export/reinsert semantics.

## Classification 2 — PDF restored-TXT-only boundary

Observed:

- text-based PDF extraction works for the synthetic case;
- scrubbed PDF text can be restored deterministically as TXT;
- restored PDF output is not supported;
- OCR and scanned/image-only PDF support are not approved.

Classification:

```text
document_format_product_boundary
```

This is not a detection false negative. The limitation must remain explicit and should be verified as part of document-fidelity and later residual-risk evidence. No OCR or restored-PDF implementation is authorized by this triage.

## Methodology correction

The first draft used an address ending in `.invalid`. Presidio's standard `EmailRecognizer` did not accept that fixture, which initially looked like a false negative. The matrix was corrected before merge by:

- using IANA-reserved `example.com`;
- including the deterministic standard email recognizer alongside the Dutch recognizer pack;
- regenerating the report;
- verifying that all expected structured values were detected.

The corrected report therefore contains no email false-negative evidence.

## Product-claim boundary

This triage does not establish recall, precision or production readiness. It confirms only that the current bounded synthetic matrix does not justify a recognizer change.

Human review remains mandatory.
