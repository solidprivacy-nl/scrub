# SolidPrivacy Scrub — Decision Log

This file records accepted strategic, product and architecture decisions.

---

## 2026-06-09 — D001 — Roadmap becomes risk-driven

Status: accepted

Decision:

```text
The roadmap is no longer primarily a feature ladder. It is risk-driven, with false negatives, Scrub Key safety, hidden document content, local-first trust and review UX treated as higher-priority than batch/CLI/extra format support.
```

Rationale:

A scrubber has asymmetric failure costs. A false positive is inconvenient; a false negative may cause the privacy incident the product is meant to prevent.

Implications:

- Finish and verify open WP18 work first.
- Then prioritize trust/recall benchmark and Scrub Key security.
- Do not proceed to batch/CLI before single-document trust is credible.

---

## 2026-06-09 — D002 — PDF support remains TXT-only unless separately approved

Status: accepted

Decision:

```text
PDF support is limited to local text-based PDF extraction to restored TXT output. Scrub does not offer restored PDF output, OCR, PDF-to-DOCX reconstruction or layout reconstruction.
```

Rationale:

PDF reconstruction and OCR add high privacy, correctness and expectation risks. Text-based extraction can be useful if presented with strong limitations and audit output.

Implications:

- WP18 must remain PDF-to-restored-TXT only.
- No future worker may add restored PDF output unless a separate strategy decision approves it.

---

## 2026-06-09 — D003 — Scrub Key is sensitive re-identification data

Status: accepted

Decision:

```text
The Scrub Key must be treated as sensitive data because it maps placeholders back to real confidential values.
```

Rationale:

The Scrub Key can re-identify a scrubbed document. It is a useful control mechanism and also a concentrated privacy risk.

Implications:

- Add Scrub Key threat model.
- Add lifecycle/expiry/delete policy.
- Review encryption/protection options before implementation.

---

## 2026-06-09 — D004 — Streamlit remains prototype/demo layer, not assumed final review UI

Status: accepted

Decision:

```text
Streamlit can remain the prototype and demo UI, but the final professional review experience may require a document-centric frontend separate from Streamlit.
```

Rationale:

Legal/care users review documents, not only tables of detected spans. Inline highlight review, click-to-mark and side-by-side review may exceed Streamlit's natural strengths.

Implications:

- Add document-centric review UX phase.
- Evaluate Streamlit feasibility before heavy review UI investment.
- Keep Python core reusable independent of final UI.

---

## 2026-06-09 — D005 — Documentation is split into internal and user-facing layers

Status: accepted

Decision:

```text
CHANGELOG.md remains an internal workpackage implementation log. RELEASE_NOTES.md is used for user-facing product capability changes. WORKPACKAGES.md remains execution queue. ROADMAP.md remains strategic risk-driven direction.
```

Rationale:

The existing changelog was useful for AI-worker governance but too process-heavy for product users.

Implications:

- Add or maintain RELEASE_NOTES.md.
- Keep handover files for worker detail.
- Avoid turning ROADMAP.md into commit history.

---

## 2026-06-09 — D006 — Workers should self-check Actions/sync where possible

Status: accepted

Decision:

```text
Workers should check GitHub Actions and GitHub-to-Hugging-Face sync status themselves where connector permissions allow, instead of relying first on coordinator screenshots.
```

Rationale:

The coordinator should not have to manually check every Actions/sync result. Worker autonomy speeds development and reduces handover friction.

Implications:

- Add STATUS_MONITORING_RUNBOOK.md.
- Do not ask the coordinator for app verification until Actions/sync are green.
- Ask the coordinator only when permissions prevent checking or when subjective app verification is required.
