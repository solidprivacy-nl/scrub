# Changelog — SolidPrivacy Scrub

## WP26 — Scrub Key encryption/lifecycle specification

Status: completed security/lifecycle-specification-only.

Purpose:

- Define Scrub Key lifecycle states, retention/deletion expectations and protection options.
- Treat the Scrub Key as sensitive re-identification data following WP25.
- Specify MVP handling versus later professional/local desktop protection without implementing encryption.

Files added:

- `SCRUB_KEY_LIFECYCLE_SPEC.md`
- `handover/workpackages/20260610_0015_scrub_key_lifecycle_spec.md`

Files changed:

- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main lifecycle decisions:

- Scrub Key lifecycle states are creation, download/export, local storage, import/reload, active use, sharing risk, expiry and deletion.
- Loss of the key or future passphrase means Scrub cannot deterministically restore original values.
- Tampering can restore wrong values and corrupt legal/care meaning; future protected formats should include integrity protection.
- MVP recommendation is warning-only plus explicit lifecycle guidance and protected-local-file guidance.
- Encrypted local files, local vault / managed key store, key recovery and schema/container changes are later professional/local desktop options that require separate implementation workpackages.
- Audit/logging should record lifecycle events and counts, but not original values, passphrases, encryption keys or full mappings.

Validation status:

- Documentation/security lifecycle review only.
- Required control files, WP25 threat model, WP58 consolidation and existing Scrub Key helper/import/reinsert files were read.
- No tests run; no code or test files were changed.
- GitHub Actions: to be checked after final handover commit.
- Hugging Face sync: to be checked after final handover commit.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No encryption implemented.
- No Scrub Key JSON schema migration.
- No import/export behavior changed.
- No reinsert behavior changed.
- No UI changed.
- No helper logic changed.
- No dependencies changed.
- No tests added or changed.
- No secrets or real data stored.

Next recommended step:

- `WP27 — Scrub Key warning UX plan`.
- Alternative next step depending on consolidation: `WP29 — Scrub Key secure import/export tests`.

## WP58 — Parallel specification consolidation and next execution queue

Status: completed documentation/planning-only.

Purpose:

- Consolidate WP19, WP25, WP30 and WP35 into one coherent next execution queue.
- Reconcile dependencies between recall benchmarking, Scrub Key lifecycle, placeholder robustness and DOCX hidden-content hygiene.
- Decide what can run in parallel now and what must remain blocked.

Files added:

- `PARALLEL_SPEC_CONSOLIDATION_WP58.md`
- `handover/workpackages/20260609_2345_parallel_spec_consolidation_wp58.md`

Files changed:

- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Consolidation decisions:

- Next recommended parallel set: `WP20`, `WP26`, `WP31`, `WP45`.
- If only one worker is available, start with `WP20 — Synthetic messy Dutch legal/zorg benchmark corpus`, because false negatives remain the highest product risk.
- `WP26 — Scrub Key encryption/lifecycle specification` can run in parallel with WP20 because it is specification-only and separate from detection benchmarking.
- `WP31 — LLM-resistant placeholder format proposal` can run in parallel because it is proposal-only and must not implement placeholder migration.
- `WP45 — Local runtime architecture plan` can run in parallel because it is architecture/planning-only and addresses the cloud-demo trust gap.
- `WP36 — DOCX metadata cleaner helper` remains blocked until a tighter metadata-only/helper-only/no-export-semantics boundary is approved.
- Optional lower-risk parallel candidates remain `WP50`, `WP56` and `WP57` if worker capacity exists.

Validation status:

- Documentation/planning review only.
- Required control files, four specification outputs and four handovers were read.
- No tests run; no code or test files were changed.
- GitHub Actions: not checked at changelog update time.
- Hugging Face sync: not checked at changelog update time.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No code changed.
- No tests added or changed.
- No UI changed.
- No dependencies changed.
- No recognizer logic changed.
- No Scrub Key encryption implemented.
- No Scrub Key schema migration.
- No placeholder migration.
- No DOCX cleaner implemented.
- No export behavior changed.
- No real data added.
- No cloud processing added.
- No roadmap change made.
- No release notes change made because there was no user-facing product capability change.

Next recommended step:

- Start the next parallel worker set:
  - `WP20 — Synthetic messy Dutch legal/zorg benchmark corpus`.
  - `WP26 — Scrub Key encryption/lifecycle specification`.
  - `WP31 — LLM-resistant placeholder format proposal`.
  - `WP45 — Local runtime architecture plan`.

## WP35 — DOCX hidden content risk review

Status: completed document-hygiene/specification-only.

Purpose:

- Review DOCX hidden content and metadata as leakage risks.
- Define current DOCX support assumptions and the boundary between visible body-text scrubbing, hidden-content scrubbing, metadata cleaning, unsupported-content warnings and future export blocking.
- Define audit requirements plus safe extraction and cleaning sequences before any helper implementation.

Files added:

- `DOCX_HIDDEN_CONTENT_RISK_REVIEW.md`
- `handover/workpackages/20260609_2325_docx_hidden_content_risk_review.md`

Files changed:

- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main risk findings:

- Current DOCX support covers `word/document.xml` text nodes, including normal body paragraphs and tables, but does not provide full DOCX package hygiene.
- Headers, footers, comments, tracked changes, metadata, custom XML, footnotes/endnotes, text boxes/shapes and embedded objects can contain sensitive values outside visible body text.
- Tracked changes are a critical leakage risk because deleted text, author names and timestamps can remain in XML even when not visible in the accepted document view.
- Metadata and custom XML should be treated as separate cleaning problems, not as normal visible-text scrubbing.
- Future audit output should distinguish inspected parts, unsupported parts, cleaning actions, warnings and blocking reasons.
- Blocking export is a product semantics change and must not be introduced silently.

Validation status:

- Documentation/document-hygiene review only.
- No tests run; no code or test files were changed.
- GitHub Actions: not checked at changelog update time.
- Hugging Face sync: not checked at changelog update time.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No DOCX cleaner implemented.
- No DOCX parser changed.
- No export semantics changed.
- No UI changed.
- No tests added or changed.
- No real documents added.
- No cloud processing added.
- No dependency changes made.
- No direct edit to `presidio_streamlit.py`.
- No direct edit to `fix_streamlit_nested_expanders.py`.
- No direct edit to `fix_streamlit_pdf_text_reinsert.py`.

Next recommended step:

- `WP58 — Parallel specification consolidation and next execution queue`.
- After WP58 reconciliation: `WP36 — DOCX metadata cleaner helper`.

## WP30 — Placeholder robustness review

Status: completed architecture/specification-only.

Purpose:

- Review how placeholders survive AI rewriting, translation, summarization and formatting changes.
- Document the current placeholder format and deterministic reinsert assumptions.
- Identify corruption risks and candidate future validation/audit directions before any migration.

Files added:

- `PLACEHOLDER_ROBUSTNESS_REVIEW.md`
- `handover/workpackages/20260609_2310_placeholder_robustness_review.md`

Files changed:

- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main architecture findings:

- Current `[PERSOON_1]`-style placeholders are deterministic and readable, but fragile under AI translation, summarization, punctuation/spacing changes, markdown/HTML formatting and document conversion.
- Current reinsert assumes exact placeholder strings from the Scrub Key mapping.
- Existing audit fields for unknown, duplicate and not-found placeholders are a useful foundation, but do not yet detect checksum failures, near-misses, placeholder deletion or semantic placeholder merges.
- Candidate robust formats such as `[[SP_PERSON_0001_A7F3]]`, `[[SP_BSN_0002_C91B]]` and `[[SP_ADDRESS_0003_D41A]]` remain proposals only.
- Checksum design must avoid deriving visible values from original sensitive data.
- Backward compatibility with legacy placeholders is mandatory.

Validation status:

- Documentation/architecture review only.
- No tests run; no code or test files were changed.
- GitHub Actions: not checked at changelog update time.
- Hugging Face sync: not checked at changelog update time.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No code changed.
- No placeholder migration.
- No placeholder format changed.
- No Scrub Key schema changed.
- No reinsert helper changed.
- No UI changed.
- No AI/cloud integration.
- No tests added or changed.
- No export behavior changed.
- No final placeholder format mandated.

Next recommended step:

- `WP31 — LLM-resistant placeholder format proposal`.

## WP25 — Scrub Key threat model

Status: completed security/specification-only.

Purpose:

- Treat the Scrub Key as sensitive re-identification data.
- Define accidental sharing, local storage, download-folder, e-mail/AI upload, shared-computer, retention, loss-of-key, tampering, malformed-key and import/export risks.
- Clarify the distinction between anonymization, pseudonymization, redaction and reinsert.
- Make clear that Scrub Key-based output is pseudonymized, not fully anonymized, as long as the key exists.

Files added:

- `SCRUB_KEY_THREAT_MODEL.md`
- `handover/workpackages/20260609_2258_scrub_key_threat_model.md`

Files changed:

- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main security findings:

- The Scrub Key contains original confidential values and placeholder mappings, so it can re-identify scrubbed content.
- Accidental sharing, default Downloads storage, e-mail/AI upload, shared-computer use, unmanaged local storage and long retention are critical risks.
- Loss of the Scrub Key prevents deterministic reinsert; tampering or malformed keys can cause incorrect or unsafe reinsert.
- Encryption, lifecycle, expiry/delete and tamper protection require a separate approved specification before implementation.

Validation status:

- Documentation/security review only.
- No tests run; no code or test files were changed.
- GitHub Actions: not checked at changelog update time.
- Hugging Face sync: not checked at changelog update time.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No helper logic changed.
- No Scrub Key JSON schema migration.
- No import/export behavior changed.
- No reinsert behavior changed.
- No UI changed.
- No encryption implemented.
- No dependencies changed.
- No tests added or changed.
- No secrets or real data stored.

Next recommended step:

- `WP26 — Scrub Key encryption/lifecycle specification`.

## WP19 — Recall benchmark specification

Status: completed specification-only.

Purpose:

- Define how Scrub will measure recall and precision on messy synthetic Dutch legal and care documents.
- Make the highest product risk, false negatives / missed sensitive data, measurable before implementing a benchmark runner.
- Define context-preservation expectations so legal and care meaning is not destroyed by over-masking.

Files added:

- `RECALL_BENCHMARK_SPEC.md`
- `handover/workpackages/20260609_2200_recall_benchmark_spec.md`

Files changed:

- `RISK_REGISTER.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main specification decisions:

- The benchmark taxonomy includes `PERSON`, `ADDRESS`, `EMAIL`, `PHONE`, `BSN`, `IBAN`, `DATE`, `NL_POSTCODE`, `CASE_NUMBER`, `DOSSIER_NUMBER`, `CLIENT_NUMBER`, `CLAIM_NUMBER`, `INCIDENT_NUMBER`, `ECLI`, `ORGANIZATION`, `MEDICAL_OR_CARE_REFERENCE` and `ROLE_OR_CONTEXT_TERM_TO_PRESERVE`.
- Gold labels should use zero-based inclusive/exclusive character offsets against synthetic plain-text sources.
- Reporting should include overall, per-domain and per-entity recall/precision, with false-negative, false-positive and context-preservation failure lists.
- Context terms such as `slachtoffer`, `minderjarige`, `verzoeker`, `verweerder`, `eiser`, `rechtbank`, `arts`, `cliënt` and `zorgmedewerker` should not automatically be treated as sensitive values unless identifying context makes them sensitive.
- CI should start as report-only, then add malformed-label failures, regression gates and later accepted per-entity thresholds.

Validation status:

- Documentation/specification review only.
- No tests run; no code or test files were changed.
- GitHub Actions: not checked at changelog update time.
- Hugging Face sync: not checked at changelog update time.
- App verification: not applicable because no UI changed.

Intentionally not changed:

- No recognizer logic changed.
- No benchmark runner implemented.
- No tests added or changed.
- No UI changed.
- No dependencies changed.
- No real data added.
- No export or reinsert behavior changed.

Next recommended step:

- `WP20 — Synthetic messy Dutch legal/zorg benchmark corpus`.

## WP18C — Add Codex worker governance instructions

Status: completed documentation/governance-only.

Purpose:

- Add repository-level worker instructions for Codex/agent execution.
- Make handover-by-file the default process for Codex workers.
- Reduce long handover copy-paste in the coordinator chat while preserving GitHub as source of truth.
- Prepare safe parallel execution of WP19, WP25, WP30 and WP35.

Files added:

- `AGENTS.md`
- `handover/workpackages/20260609_1330_codex_worker_governance.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:

- `AGENTS.md` defines repository scope, required start sequence, safety rules, workpackage discipline, parallelization rules, testing/validation expectations, documentation updates and handover process.
- Codex workers must write full handovers to `handover/workpackages/`.
- Coordinator chat only needs handover path, commit/PR, status and short summary when the handover is committed to GitHub.
- Full handover copy-paste is only required if commit/GitHub access fails, there is a conflict, or the coordinator explicitly asks for it.

## Earlier completed work

- WP18B — PDF text to restored TXT UI app verification closeout.
- WP18-FIX — Fix failing PDF text to TXT UI tests.
- WP18R — Risk-driven roadmap and operating model reset.
- WP18 — PDF text extraction to restored TXT UI implementation.
- WP17B — Roadmap current-status reconciliation after WP17.
- WP17 — PDF text extraction reinsert UI planning only.
- WP16B — Text-based PDF extraction helper spike verification and closeout.
- WP16-FIX — Fix failing PDF text helper tests.
- WP16 — Text-based PDF extraction helper spike, restored TXT output only.
- WP15 — PDF text extraction reliability review only.
- v13.8 DOCX reinsert upload/download UI.
- v13.7 TXT reinsert upload/download UI.
- v13.6 two-mode UI.
- v13.3 deterministic reinsert UI.
- v13 Scrub Key foundation and import/export work.
- v12 Review UX line.
