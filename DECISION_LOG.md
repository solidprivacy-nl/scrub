# SolidPrivacy Scrub — Current Decision Log

This file records **accepted decisions that remain materially binding on current/future product work**.

Detailed pre-convergence decision history remains recoverable from exact baseline:

```text
54c73e0ebf5a3a3ed7039a50596fb57694add3cd
```

Git and `CHANGELOG.md` are the historical provenance layers. This file must not become another implementation-history ledger.

---

## D044 — 2026-09-04 — Repository Convergence before further normal feature development; Scrub Private becomes the active future production line

Status: **accepted strategic/architecture direction; implementation of the bootstrap candidate remains subject to normal independent assurance**

Decision:

```text
Pause normal new feature development.

Preserve exact current source by SHA
→ reconstruct active/reachable current truth
→ classify CANONICAL / RECONCILE / RETIRE / VARIANT-SPECIFIC
→ remove only proven debt
→ reconcile current documentation/issues/evidence authority
→ verify one clean baseline
→ after convergence, continue main as Scrub Private
→ finish Private-oriented application behavior on Hugging Face with synthetic data
→ add production Private Service controls
→ external assurance
→ pilot Legal first, then Zorg based on evidence.
```

Reasons:

- current repository contains mature functionality that must not be rebuilt from stale assumptions;
- canonical docs/workpackages/issues contain multiple generations of status and local-first deployment assumptions;
- active technical legacy and valid-but-hosted-incompatible functionality must be distinguished before removal;
- version control preserves prior/full-feature functionality more safely than an in-repository source clone;
- the shortest path to the business outcome is to clean current truth first, then adapt only the trust boundary required by Scrub Private.

Binding consequences:

- exact Git SHA is preservation authority; optional tags are only human-readable markers;
- no `/app_v2`, `/scrub-new`, duplicate Streamlit main or other source clone;
- `ROADMAP.md` contains five strategic stages only;
- `WORKPACKAGES.md` contains one current executable queue only;
- the temporary convergence debt ledger is not a new permanent source of truth;
- no cleanup refactor is justified by aesthetics alone;
- no new Evidence Framework; reconcile/reuse existing synthetic/benchmark/E2E/security evidence;
- human review and existing privacy/safety semantics remain binding;
- Hugging Face is a synthetic/approved-test application-validation environment, not confidential-production infrastructure assurance;
- Local/offline capability remains recoverable/deferred and is not the active delivery line;
- after `SCRUB_REPOSITORY_CONVERGED`, `main` becomes the active Scrub Private development line.

Scrub Private content-plane direction:

```text
no intentional persistent customer document content
no content-bearing ordinary application logs
no document-content backup
no third-party document-processing egress
minimal non-document control-plane persistence only when a real service requirement justifies it
```

This decision does not itself remove current replacement-memory or external-processing functionality. Those are variant-specific candidates for a later, separately assured Private adaptation after the clean baseline.

---

## D043 — 2026-08-08 — Premium Standard is a single-page staged document workspace

Status: accepted and implemented direction; preserve unless current runtime evidence justifies change.

Decision:

```text
One document. One workspace. Three stages. One active task.

Toevoegen → Controleren → Downloaden
```

Binding behavior:

- all three stages remain represented in one workspace;
- exactly one Standard stage is dominant at a time;
- completed stages collapse to compact summaries;
- future stages are visible but passive;
- successful completion advances safely;
- explicit return to earlier stages is allowed;
- processing-affecting changes invalidate downstream review/export state fail-closed;
- Standard is lower cognitive load, not lower safety;
- three routed pages and a nested-expander long form are rejected as the Standard core-flow target.

---

## D042 — 2026-08-06 — Separate implementation from blind independent release assurance

Status: accepted and binding governance decision.

Decision:

```text
implementation_operations
→ identifiable exact candidate
→ governance_release_assurance fresh blind reconstruction
→ PASS | FAIL | INDETERMINATE
→ authorized action
→ independent post-action confirmation
```

Implementation may not certify its own consequential candidate. Assurance may not repair what it reviews and may not read implementation conclusions before its initial verdict.

---

## D041 — 2026-08-05 — Application-wide Standard/Expert premium core-flow shell

Status: accepted and implemented direction.

Decision:

- top-level `Anonimiseren | Terugzetten` workflows;
- global `Standaard | Expert` presentation;
- Standard uses the staged `Toevoegen → Controleren → Downloaden` workspace;
- Expert operates over the same authoritative source/processing/review state;
- presentation-only switching must not silently change profile/settings, reprocess or reset valid state;
- human review and export/Scrub Key/reinsert semantics are not weakened by presentation simplification.

---

## D040 — 2026-08-04 — Server-authoritative direct masking from processed text

Status: accepted and implemented product decision.

Decision:

A user may select a missed sensitive value in processed text, but browser selection is only an input event. The server validates scope, offsets, exact occurrences, collisions and stale/replay state before creating one normal document-bound manual replacement row.

The review table/authoritative review state remains source of truth. Direct masking may not write Scrub Keys or exports independently.

---

## D039 — 2026-08-03 — Zorg profile with clinical-context preservation

Status: accepted and implemented product decision.

Decision:

- direct patient/client identity and date of birth: replace;
- other exact care dates/provider identity and dedicated care identifiers: review according to policy, selected by default where defined;
- diagnosis, medication, dosage, laboratory results, observations and clinically meaningful context: preserve;
- rare indirect-identification risk: surface for review/audit rather than blindly destroying clinical meaning;
- synthetic corpus/evidence and human review remain mandatory; no production-safety claim from corpus scores alone.

---

## D038 — 2026-08-03 — Local desktop packaging is a deferred product option, not current execution authority

Status: historical decision retained only where still applicable.

The previously selected signed Tauri/PyInstaller local packaging direction remains recoverable if Local becomes an active product requirement later.

D044 supersedes its roadmap priority. Installer work is not part of the current execution line.

---

## D037 — 2026-07-28 — Validate document/key binding before every reinsert replacement

Status: accepted and binding safety decision.

Decision:

Validate the complete supported document text surface against the supplied Scrub Key before restoring any original value. Bound mismatch, mixed binding, missing binding or invalid mapping digest fails closed with zero replacements. Legacy unbound behavior remains explicitly unverified where supported.

---

## D036 — 2026-07-27 — Preserve intentional custom replacement text; fail verified key export rather than silently rewriting it

Status: accepted and binding review/export decision.

Decision:

Do not silently convert arbitrary user-chosen replacement text into bound placeholders merely to make Scrub Key export succeed. Preserve the reviewed replacement decision and fail visibly/block verified key export when a fully bound mapping cannot be established.

---

## D035 — 2026-07-27 — Implement Scrub Key binding in pure model first, then integrate sequentially

Status: accepted implementation/safety pattern; completed historically.

Decision remains relevant as a precedent: safety-critical shared placeholder/key/reinsert changes should be isolated in pure/testable helpers before sequential integration into export/reinsert when new changes are genuinely required.

---

## D034 — 2026-07-27 — Bound-placeholder and mapping-digest contract

Status: accepted and implemented safety contract.

Binding direction:

- document-specific binding ID in automatic/manual bound placeholders;
- schema-1.1 bound key direction;
- canonical SHA-256 mapping digest;
- explicit legacy-unbound compatibility state;
- mismatch/mixed/missing/digest-invalid bound states fail closed before replacement.

Do not shorten or mutate authoritative bound tokens merely for visual convenience; compact aliases are presentation-only.

---

## D033 — 2026-07-27 — Document-specific placeholder namespaces bind new Scrub Keys to their document

Status: accepted and implemented architecture decision.

Each new bound Scrub Key/document uses one locally generated non-sensitive binding ID carried by automatic/manual placeholders and the corresponding key. A mapping digest complements this for accidental corruption detection. The binding token, not filenames/labels/content heuristics, is the cross-format document/key association.

Legacy unbound keys remain explicitly distinguishable and must not be silently reinterpreted as verified bound matches.

---

## D031 — 2026-07-27 — Reinsert is document-first and automatically processes valid source/key inputs

Status: accepted and implemented UX/safety decision.

Current reinsert direction:

```text
source document/text
→ corresponding Scrub Key
→ deterministic validation/reinsert
→ restored download
```

Source type recognition and structural key validation may run automatically when valid inputs are present. Do not reintroduce redundant hidden confirmation buttons/checkboxes merely to create a sense of safety. Keep the meaningful confidentiality acknowledgement at the restored-output boundary and fail invalid/ambiguous keys visibly.

---

## D030 — 2026-07-17 — Supported DOCX reinsert includes body, tables, headers and footers

Status: accepted and implemented document-fidelity decision.

Restore supported placeholders in existing `word/document.xml`, `word/header*.xml` and `word/footer*.xml` text nodes. Do not imply support for comments, tracked-change-only parts, footnotes/endnotes, text boxes, metadata or split placeholders unless a separate evidence-backed package adds and verifies that support.

---

## D021 — 2026-06-14 — Unified side-by-side review is the target review surface

Status: accepted and still materially binding product/UX decision.

The main review experience centers on source text/document versus processed/checked text. Highlights are a visual aid, not an alternate mutation authority. The authoritative review table/state remains the fallback/source of truth, and future review work should avoid proliferating duplicate helper panels.

This direction is implemented within the later D041/D043 Premium staged workspace.

---

# Current decision discipline

New decisions belong here only when they remain materially binding on current/future work.

Do not copy workpackage status, test runs or implementation narrative into this file.

If a decision is superseded, mark the superseding decision explicitly rather than leaving two competing current rules.
