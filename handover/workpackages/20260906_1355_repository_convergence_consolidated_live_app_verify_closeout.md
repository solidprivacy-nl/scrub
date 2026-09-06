# Handover — SCRUB-WP_REPOSITORY_CONVERGENCE_CONSOLIDATED_LIVE_APP_VERIFY_CLOSEOUT

**Observed at:** 2026-09-06 13:55 CEST (Europe/Amsterdam)  
**Role:** `governance_release_assurance`  
**Repository:** `solidprivacy-nl/scrub`  
**Assurance issue:** #129  
**Parent product-facing gate:** #96  
**Assurance branch:** `assurance/wp05-live-app-verify-20260906-1355`  
**GitHub main at review start and final readback:** `a0fe29306a1f6875058d511466513f7ddb550760`  
**Status:** `GOVERNANCE_INDETERMINATE`

## Formal verdict

```text
SCRUB-WP_REPOSITORY_CONVERGENCE_CONSOLIDATED_LIVE_APP_VERIFY_CLOSEOUT: INDETERMINATE
```

No product/runtime/source repair was performed. This assurance does not authorize WP-CONVERGENCE-FINAL, `SCRUB_REPOSITORY_CONVERGED`, Stage 2, or Scrub Private implementation.

## Blind-first reconstruction

Before the initial verdict, current governed state was reconstructed independently from GitHub source of truth using the current `main` SHA and the canonical controls:

- `PROJECT_PROMPT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`
- current issue #96 and assurance issue #129
- current source/tests implementing the relevant state, marker/placeholder and Dutch-address contracts
- raw current-main GitHub Actions and Hugging Face synchronization evidence

The current PR #104/#108/#111 history was inspected to identify the relevant repair surfaces. While locating PR #111 changed files, the GitHub PR-files endpoint incidentally returned the patch of an implementation handover among the changed files. That returned handover text was excluded from correctness evidence and did not affect the verdict. The verdict rests on the canonical controls, current source/tests, raw machine/deployment evidence, and the actual capability of the available live-web environment.

## Deployment/source identity evidence

At review start and final readback, GitHub `main` resolved to:

```text
a0fe29306a1f6875058d511466513f7ddb550760
```

Raw same-SHA machine evidence:

```text
Tests run 34027429725
head_sha=a0fe29306a1f6875058d511466513f7ddb550760
conclusion=success

GitHub → Hugging Face sync run 34027429743
job 101470788494
head_sha=a0fe29306a1f6875058d511466513f7ddb550760
Push main to Hugging Face Space=success
```

The public Hugging Face Space `solidprivacy/scrub` was reachable and reported `Running`. Its application iframe resolved to `https://solidprivacy-scrub.hf.space/`.

The available live-web environment could fetch the public Space and iframe shell, but the iframe exposed only the JavaScript bootstrap message:

```text
You need to enable JavaScript to run this app.
```

Therefore the environment did not expose an interactive JavaScript/Streamlit browser session capable of uploading/pasting a document, pressing controls, editing review state, switching Standard/Expert, downloading exports/Scrub Keys, performing reinsert, or capturing the required application screenshots. A direct target-Space Git commit readback was also not independently obtained. The same-SHA successful GitHub→HF push is strong deployment evidence but is not promoted into a live-behavior PASS.

## Current source contracts independently reconstructed

The current governed source shows the intended contracts needed for the live test, but these are not substituted for deployed observations:

- Standard/Expert presentation operates over generation-bound authoritative source/review state; source/processing generation changes invalidate stale downstream analysis/review state.
- Export remains unavailable until human review is current for the active generation; a real review edit requires explicit re-completion, and source/processing changes require reprocessing.
- Processed-text highlight offsets are calculated against untrimmed document text; scalar review cells are normalized separately.
- Strict document-bound placeholder tokens remain authoritative internally while compact aliases are presentation-only.
- Dutch `NL_ADDRESS` precision narrows only a provably stricter street + house-number subspan and otherwise preserves the broad result fail-safe.
- Scrub Key/document binding and reinsert mismatch behavior remain governed as fail-closed controls.
- Mandatory human review remains binding.

## Synthetic test input prepared but not submitted

Because no interactive Streamlit browser session was available, the approved synthetic test material was not entered into the deployed app. The intended reproducible input was:

```text


Rapport van het inspectiebezoek aan Stichting Voorbeeldzorg, locatie Polderweg 8 in Amsterdam.
De inspectie bezoekt Polderweg 8.
Contactpersoon: Jan Testpersoon.
E-mailadres: jan.testpersoon@example.test.
Telefoon: 0612345678.
Laan van Meerdervoort 55, 2517 AM Den Haag.
```

No real personal, patient, client or employee data and no real Scrub Key were used or stored.

## Live Test results

| Test | Result | Evidence / blocker |
|---|---|---|
| Live Test 1 — Standard ↔ Expert state round-trip | `INDETERMINATE` | Interactive Streamlit controls unavailable; source upload/process/review edit/mode switch could not be executed live. |
| Live Test 2 — Replacement/review lineage | `INDETERMINATE` | Live review UI could not be operated or visually inspected. |
| Live Test 3 — Export / Scrub Key gating | `INDETERMINATE` | Live export/download controls could not be reached or exercised. |
| Live Test 4 — Reinsert fail-closed | `INDETERMINATE` | Matching and deliberately mismatched synthetic key/document pairs could not be submitted through the deployed UI. |
| Live Test 5 — final privacy-focused visual inspection | `INDETERMINATE` | Actual processed/review/export surfaces were not renderable in the available environment. |

Specific required material therefore remains:

```text
marker / leading-whitespace live result: INDETERMINATE
compact placeholder live result: INDETERMINATE
long bound-token leakage/fragmentation live result: INDETERMINATE
Polderweg 8 live result: INDETERMINATE
long Dutch address live result: INDETERMINATE
Standard/Expert state-lineage live result: INDETERMINATE
export/Scrub Key gating live result: INDETERMINATE
reinsert fail-closed live result: INDETERMINATE
mandatory human-review live result: INDETERMINATE
screenshots: unavailable because no interactive JS/Streamlit rendering was exposed
```

No source-level test, CI result, or successful Hugging Face sync is treated as a substitute for these missing live observations.

## Issue handling

Parent issue #96 was confirmed `OPEN` immediately before handover creation and was deliberately not mutated or closed.

Issue #129 remains the active assurance work item because the live evidence required for PASS has not been obtained. No PASS comment was placed on #96.

## Finding / missing evidence

This is not a demonstrated product defect. The assurance blocker is evidence availability:

```text
classification: live-assurance evidence unavailable
severity: release-gate blocking
expected: browser-capable environment executes and observes Live Tests 1–5 on the deployed Space
actual: available environment can fetch the HF shell but cannot execute the JavaScript/Streamlit application UI
impact: #96 cannot legally/governance-wise close; WP-CONVERGENCE-FINAL and Stage 2 remain blocked
```

## Smallest unblock action

Run this same issue #129 from a genuinely browser-capable environment with JavaScript/Streamlit interaction and screenshot capture (for example ChatGPT Work / Cloud Browser where available), against the then-current governed deployed version. Reconfirm current `main` and deployment identity, then execute Live Tests 1–5 exactly as specified using synthetic data. Do not repair product code from the assurance role; if a material live defect appears, return it as a narrow root-cause package to `implementation_operations`.

## Remaining risks / non-claims

R1 false negatives, R2 Scrub Key handling and R10 Zorg remain critical governance risks. R6 review/stale-state assurance remains unclosed because the consolidated deployed live retest is unproven.

This assurance does **not** claim perfect anonymisation, perfect recognizer recall, production safety, provider-level zero retention, or absence of unknown privacy defects. Hugging Face remains an application-validation environment for synthetic/approved data, not the confidential-production trust environment.

## Next authorized step

Only repeat the independent deployed WP05 live verification in an actually interactive browser-capable environment. Do not start WP-CONVERGENCE-FINAL or Stage 2 from this outcome.
