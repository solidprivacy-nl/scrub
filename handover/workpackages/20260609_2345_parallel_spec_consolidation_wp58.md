# Handover — WP58 Parallel specification consolidation and next execution queue

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP58 — Parallel specification consolidation and next execution queue`

Status: completed documentation/planning-only.

## Summary

WP58 consolidated the completed outputs of WP19, WP25, WP30 and WP35 into one coherent next execution queue. The consolidation reconciles recall benchmarking, Scrub Key lifecycle, placeholder robustness and DOCX hidden-content hygiene, and defines what can run now, what can run in parallel and what remains blocked.

Final next recommended parallel set:

```text
Worker 1: WP20 — Synthetic messy Dutch legal/zorg benchmark corpus
Worker 2: WP26 — Scrub Key encryption/lifecycle specification
Worker 3: WP31 — LLM-resistant placeholder format proposal
Worker 4: WP45 — Local runtime architecture plan
```

Blocked until later:

```text
WP36 — DOCX metadata cleaner helper
```

Reason: WP36 may affect document/export semantics and should wait until a tighter metadata-only/helper-only/no-export-semantics boundary is approved.

## Files added

- `PARALLEL_SPEC_CONSOLIDATION_WP58.md`
- `handover/workpackages/20260609_2345_parallel_spec_consolidation_wp58.md`

## Files changed

- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Files intentionally not changed

- `ROADMAP.md` — no strategy or phase-order change was needed.
- `RISK_REGISTER.md` — WP58 did not change risk status; existing risks remain active and already point to the relevant mitigation lines.
- `RELEASE_NOTES.md` — no user-facing product capability changed.

## Tests

- No tests run.
- No test files added or changed.
- Reason: WP58 is coordination/documentation/planning-only and did not change code, helper logic, UI, dependencies, export behavior or runtime behavior.

## Validation status

- Required start sequence read: `AGENTS.md`, `PROJECT_PROMPT.md`, `ROADMAP.md`, `WORKPACKAGES.md`, `CHANGELOG.md`.
- Additional control files read: `RISK_REGISTER.md`, `DECISION_LOG.md`, `STATUS_MONITORING_RUNBOOK.md`, `RELEASE_NOTES.md`.
- Completed specification outputs read: `RECALL_BENCHMARK_SPEC.md`, `SCRUB_KEY_THREAT_MODEL.md`, `PLACEHOLDER_ROBUSTNESS_REVIEW.md`, `DOCX_HIDDEN_CONTENT_RISK_REVIEW.md`.
- Four completed handovers read:
  - `handover/workpackages/20260609_2200_recall_benchmark_spec.md`
  - `handover/workpackages/20260609_2258_scrub_key_threat_model.md`
  - `handover/workpackages/20260609_2310_placeholder_robustness_review.md`
  - `handover/workpackages/20260609_2325_docx_hidden_content_risk_review.md`
- Confirmed scope remained documentation/planning-only.
- Confirmed no implementation packages were started.

## Consolidation decisions

- `WP20` should start now and is highest priority if only one worker is available.
- `WP26` can run in parallel with WP20 because it is lifecycle/specification-only and separate from detection benchmarking.
- `WP31` can run in parallel with WP20 and WP26 because it is proposal-only and must not implement placeholder migration.
- `WP45` can run in parallel as architecture/planning-only and addresses the cloud-demo trust gap.
- `WP36` remains blocked because metadata cleaning can affect document/export semantics.
- `WP50`, `WP56` and `WP57` remain optional lower-risk parallel candidates if worker capacity exists.

## GitHub Actions status

- Unknown at handover creation time.
- WP58 is documentation/planning-only and no code or tests changed.
- Connector status lookup should be performed after the final handover commit exists.

## Hugging Face sync status

- Unknown at handover creation time.
- No app/runtime behavior changed.
- Connector status lookup should be performed after the final handover commit exists.

## App verification status

- Not applicable.
- No UI behavior changed.

## Remaining risks

- R1 false negatives remains critical until WP20–WP24 deliver corpus, labels, runner, scorecard and residual-risk reporting.
- R2 Scrub Key leakage remains critical until lifecycle, protection, warning UX, expiry/delete and secure import/export tests exist.
- R3 placeholder corruption remains high until robust format proposal, validation helper, audit hardening and corruption tests exist.
- R4 hidden DOCX content remains high until metadata cleaning, hidden-part extraction, hygiene audit and clean export policy exist.
- R5 cloud-demo trust gap remains high until local runtime architecture and implementation are credible.
- WP36 must remain blocked until helper scope and export/document semantics boundaries are approved.

## Next recommended step

Start the next parallel set:

```text
Worker 1: WP20 — Synthetic messy Dutch legal/zorg benchmark corpus
Worker 2: WP26 — Scrub Key encryption/lifecycle specification
Worker 3: WP31 — LLM-resistant placeholder format proposal
Worker 4: WP45 — Local runtime architecture plan
```
