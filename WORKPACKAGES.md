# SolidPrivacy Scrub — Workpackages

## Required start sequence

Read in order:

1. `PROJECT_PROMPT.md`
2. `ROADMAP.md`
3. `WORKPACKAGES.md`
4. `CHANGELOG.md`

Repository: `solidprivacy-nl/scrub`.

Also read when relevant:

- `AGENTS.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `STATUS_MONITORING_RUNBOOK.md`
- `RELEASE_NOTES.md`

## Current status

WP0 through WP13B are complete.

Recent completed line:

```text
WP14 / WP14B / WP14C — v13.8 DOCX reinsert upload/download UI: completed and app-verified.
WP15 — PDF text extraction reliability review only: completed review/specification-only.
WP16 — Text-based PDF extraction helper spike: completed after Actions/sync verification.
WP16-FIX — PDF helper test fix: completed after Actions/sync verification.
WP16B — PDF helper verification closeout: completed closeout-only.
WP17 — PDF text extraction reinsert UI planning: completed planning/specification-only.
WP17B — Roadmap current-status reconciliation after WP17: completed documentation-only.
WP18 — PDF text extraction to restored TXT UI implementation: completed and app-verified after Actions/sync verification.
WP18R — Risk-driven roadmap and operating model reset: completed documentation/governance-only.
WP18-FIX — Fix failing PDF text to TXT UI tests: completed after Actions/sync verification; WP18 app verification completed.
WP18B — PDF text to restored TXT UI app verification closeout: completed closeout-only.
WP18C — Add Codex worker governance instructions: completed documentation/governance-only.
```

## Closed UI line: WP18 PDF text to restored TXT

### WP18 — PDF text extraction to restored TXT UI implementation

Status: completed and app-verified after Actions/sync verification.

Implemented workflow:

```text
Originele waarden terugzetten
→ PDF upload
→ local selectable-text extraction via WP16 helper
→ deterministic Scrub Key reinsert
→ restored TXT preview
→ restored TXT download
→ audit report
```

Preserved boundaries:

- no OCR;
- no restored PDF output;
- no PDF-to-DOCX reconstruction;
- no AI/cloud extraction;
- no layout reconstruction;
- no batch PDF processing;
- no real-data tests;
- no automatic PDF rehydration;
- no changes to existing pasted-text/TXT/DOCX reinsert semantics;
- no changes to existing anonymization/export semantics.

### WP18-FIX — Fix failing PDF text to TXT UI tests

Status: completed after Actions/sync verification; WP18 app verification completed.

Fix summary:

- Updated `tests/test_pdf_text_reinsert_ui_patch.py` only.
- Corrected a brittle test expectation around the triple-quoted `else:` insertion marker.
- No UI code, Dockerfile behavior, helper code, dependencies or feature behavior were changed.

Verification note:

- Connector status lookup for the WP18-FIX commit returned no statuses and no workflow runs.
- WP18B was approved by the coordinator/user as closeout-only after external verification.
- This closeout records coordinator/user evidence that Actions/sync and app verification gates are satisfied.

### WP18B — PDF text to restored TXT UI app verification closeout

Status: completed closeout-only.

Closeout evidence recorded:

- GitHub Actions: green based on coordinator/user closeout approval.
- Hugging Face sync: green based on coordinator/user closeout approval.
- App verification: confirmed by coordinator/user closeout approval.

App verification scope covered:

- `Originele waarden terugzetten` shows the new PDF-to-TXT section;
- `Anonimiseren` does not show the PDF reinsert section;
- a valid Scrub Key can be loaded;
- a text-based PDF with placeholders can be uploaded;
- PDF text can be restored locally to TXT;
- restored TXT preview appears;
- restored TXT download appears;
- audit report appears;
- UI clearly says no OCR, no AI, no cloud and no PDF output;
- scanned/image-only PDFs are rejected or clearly marked unsupported;
- existing pasted-text, TXT and DOCX reinsert still work;
- existing anonymization/export behavior is unchanged.

Files changed in WP18B:

```text
WORKPACKAGES.md
CHANGELOG.md
RELEASE_NOTES.md
handover/workpackages/20260609_1315_pdf_text_to_txt_ui_app_closeout.md
```

No code, tests, dependencies or UI files were changed.

## Governance setup: WP18C Codex worker governance

### WP18C — Add Codex worker governance instructions

Status: completed documentation/governance-only.

Purpose:

- Add repository-level Codex/agent worker instructions.
- Make handover-by-file the default workflow for parallel Codex workers.
- Avoid full handover copy-paste into the coordinator chat when the handover is committed to GitHub.

Files added:

```text
AGENTS.md
handover/workpackages/20260609_1330_codex_worker_governance.md
```

Files changed:

```text
WORKPACKAGES.md
CHANGELOG.md
```

No code, tests, UI, dependencies, runtime behavior or product behavior were changed.

Codex worker rule:

```text
Workers must write full handovers to handover/workpackages/.
Coordinator chat only needs handover path, commit/PR, status and short summary unless commit failed or GitHub access is unavailable.
```

## Active / next recommended workpackages

The WP18 UI line is now closed.

The following workpackages can be prepared and run in parallel because they do not touch the same UI flow:

### WP19 — Recall benchmark specification

Type: specification/test-design.

Purpose:

- Define a benchmark for measuring recall/precision on messy synthetic Dutch legal and care texts.
- Define entity classes, scoring rules, minimum metrics and reporting format.

Likely files:

```text
RECALL_BENCHMARK_SPEC.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_recall_benchmark_spec.md
```

No recognizer logic changes in WP19.

### WP25 — Scrub Key threat model

Type: security review/specification.

Purpose:

- Treat Scrub Key as sensitive re-identification data.
- Define leakage, accidental sharing, lifecycle, expiry/delete and encryption risks.

Likely files:

```text
SCRUB_KEY_THREAT_MODEL.md
RISK_REGISTER.md
DECISION_LOG.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_scrub_key_threat_model.md
```

No encryption implementation in WP25.

### WP30 — Placeholder robustness review

Type: architecture/specification.

Purpose:

- Review how placeholders survive AI rewriting, translation and summarization.
- Propose an LLM-resistant placeholder format and validation direction.

Likely files:

```text
PLACEHOLDER_ROBUSTNESS_REVIEW.md
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_placeholder_robustness_review.md
```

No placeholder format migration in WP30.

### WP35 — DOCX hidden content risk review

Type: document hygiene review/specification.

Purpose:

- Review metadata, comments, tracked changes, headers/footers and hidden document content.
- Define safe extraction/cleaning sequence before helper implementation.

Likely files:

```text
DOCX_HIDDEN_CONTENT_RISK_REVIEW.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_docx_hidden_content_risk_review.md
```

No cleaner implementation in WP35.

### WP45 — Local runtime architecture plan

Type: architecture/specification.

Purpose:

- Bring local-first runtime earlier in the roadmap.
- Compare minimal local Streamlit launcher, PyInstaller, Tauri and Electron paths.

Likely files:

```text
LOCAL_RUNTIME_ARCHITECTURE_PLAN.md
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_local_runtime_architecture_plan.md
```

No packaging implementation in WP45.

### WP50 — Pilot design: Legal vs Zorg

Type: validation/GTM specification.

Purpose:

- Compare first pilot route: Scrub Legal versus Scrub Zorg.
- Define ICP, pilot documents, consent/NDA process, metrics and decision criteria.

Likely files:

```text
PILOT_VALIDATION_PLAN.md
DECISION_LOG.md
RISK_REGISTER.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_pilot_validation_plan.md
```

No real customer data or real documents in repo.

### WP56 — User-facing release notes split and documentation hygiene

Type: documentation.

Purpose:

- Keep `CHANGELOG.md` as internal workpackage log.
- Keep `RELEASE_NOTES.md` as user-facing product capability log.

Likely files:

```text
RELEASE_NOTES.md
CHANGELOG.md
WORKPACKAGES.md
handover/workpackages/YYYYMMDD_HHMM_release_notes_split.md
```

### WP57 — Workflow status monitoring runbook and checks

Type: operations/documentation, optional helper later.

Purpose:

- Reduce dependence on coordinator screenshots.
- Define how workers check GitHub Actions and Hugging Face sync status themselves.
- Define status states and when app verification can start.

Likely files:

```text
STATUS_MONITORING_RUNBOOK.md
WORKPACKAGES.md
CHANGELOG.md
handover/workpackages/YYYYMMDD_HHMM_status_monitoring_runbook.md
```

No GitHub workflow changes unless separately approved.

## Parallelization rules

Safe in parallel after WP18B closeout:

```text
WP19, WP25, WP30, WP35, WP45, WP50, WP56, WP57
```

Do not run in parallel:

- multiple edits to Docker startup patch order;
- multiple edits to `presidio_streamlit.py` or `fix_streamlit_nested_expanders.py`;
- multiple changes to export/download flow;
- implementation work that depends on unresolved specs.

## Documentation model

- `ROADMAP.md`: strategy, risk-driven phase order and architecture.
- `WORKPACKAGES.md`: active queue and dependencies.
- `CHANGELOG.md`: internal workpackage implementation log.
- `RELEASE_NOTES.md`: user-facing product changes.
- `DECISION_LOG.md`: accepted strategic/architecture/product decisions.
- `RISK_REGISTER.md`: active privacy/product/security risks and mitigations.
- `handover/workpackages/`: worker handovers.
