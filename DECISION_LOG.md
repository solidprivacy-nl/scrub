# SolidPrivacy Scrub — Decision Log

This file records accepted strategic, product and architecture decisions.

---

## 2026-06-10 — D010 — Scrub Key MVP lifecycle starts warning-first before encryption

Status: accepted

Decision:

```text
Scrub Key lifecycle must be specified before encryption implementation. The MVP may start with warning-only handling plus explicit lifecycle guidance and protected-local-file guidance, but encrypted key files, local vault behavior, key recovery and Scrub Key schema/container changes require separate implementation workpackages.
```

Rationale:

The Scrub Key is sensitive re-identification data. Adding encryption or vault behavior without a lifecycle policy can create new risks: surprise data loss, unclear passphrase recovery, hidden recovery copies, incompatible key formats, import/export confusion and unsupported security claims. A warning-first MVP preserves the current schema and behavior while making risk visible.

Implications:

- WP26 remains security/lifecycle-specification-only.
- WP27 should specify warning UX before user-facing lifecycle changes.
- WP28 should define expiry/delete policy before any automated deletion behavior.
- WP29 should add secure import/export tests before harder protection behavior.
- Scrub Key encryption implementation remains blocked until a separate approved implementation workpackage defines format, migration, passphrase behavior and tamper protection.
- Local vault / managed key-store behavior remains a later professional/local desktop option, not an MVP change.

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

---

## 2026-06-09 — D007 — Scrub Key encryption and lifecycle require separate approved specification

Status: accepted

Decision:

```text
Scrub Key encryption, expiry, deletion, key-vault behavior and schema/format migration must not be implemented ad hoc. They require a separate approved encryption/lifecycle specification workpackage before implementation.
```

Rationale:

The Scrub Key is sensitive re-identification data. Protection choices such as passphrase encryption, OS keychain storage, authenticated encryption, deletion reminders and lifecycle states affect user trust, data loss risk, backward compatibility and import/export semantics.

Implications:

- WP25 remains threat-model/specification-only.
- WP26 should define the Scrub Key encryption/lifecycle specification before any encryption implementation.
- No worker should silently change Scrub Key JSON schema, import/export semantics or storage behavior while implementing unrelated work.
- Loss-of-key and loss-of-passphrase behavior must be specified before encryption is added.

---

## 2026-06-09 — D008 — Placeholder robustness must be additive and validation-led

Status: accepted

Decision:

```text
Placeholder robustness for AI roundtrip must be handled through an explicit proposal and validation/audit path before any placeholder migration. Future robust formats are proposals only until accepted, and legacy placeholders must remain restorable until a separate compatibility/migration decision says otherwise.
```

Rationale:

Current reinsert is deterministic and exact-match based. This is safe, but placeholders can be corrupted by AI rewriting, translation, summarization, punctuation changes, markdown/HTML formatting and document conversion. A stronger placeholder format may help, but changing placeholder semantics too early could break existing scrubbed documents and Scrub Keys.

Implications:

- WP30 remains architecture/specification-only.
- WP31 should propose and compare an LLM-resistant placeholder format without implementing migration.
- WP32 should define/implement validation or checksum helpers only after the format proposal is accepted.
- Legacy placeholders such as `[PERSOON_1]` must remain part of the compatibility plan.
- Placeholder repair must not silently guess original intent; unknown, missing, changed and near-miss placeholders should be visible in audit output.

---

## 2026-06-09 — D009 — WP58 next execution queue after parallel specifications

Status: accepted

Decision:

```text
After consolidating WP19, WP25, WP30 and WP35, the next safe parallel execution queue is WP20, WP26, WP31 and WP45. WP36 remains blocked until a tighter DOCX metadata-cleaner helper boundary is approved, because DOCX cleaning may affect document and export semantics.
```

Rationale:

WP19 confirms false negatives remain the highest product risk, so WP20 should start the synthetic benchmark corpus. WP25, WP30 and WP45 are separable specification/architecture tracks that do not touch the same UI or export flow. WP35 identifies serious DOCX hygiene risks, but metadata cleaning and clean-export claims need tighter boundaries before implementation.

Implications:

- WP20 may create synthetic benchmark corpus artifacts but must not change recognizer logic.
- WP26 may specify Scrub Key lifecycle/protection but must not implement encryption or schema migration.
- WP31 may propose an LLM-resistant placeholder format but must not implement placeholder migration or reinsert changes.
- WP45 may plan local runtime architecture but must not implement packaging or runtime changes.
- WP36 must not start as an implementation package until its metadata-only/helper-only/no-export-semantics boundary is approved.
- WP50, WP56 and WP57 remain lower-risk optional parallel candidates if worker capacity exists.
