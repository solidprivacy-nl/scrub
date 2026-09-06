# Handover — SCRUB-WP_REPOSITORY_CONVERGENCE_CONSOLIDATED_LIVE_APP_VERIFY_CLOSEOUT dispatch

## Repository worked in

`solidprivacy-nl/scrub`

## Workpackage title

`SCRUB-WP_REPOSITORY_CONVERGENCE_CONSOLIDATED_LIVE_APP_VERIFY_CLOSEOUT`

Role: `implementation_operations` for evidence reconstruction/dispatch  
Parent gate: #96  
Independent verification issue: #129  
Exact governed main at dispatch: `a0fe29306a1f6875058d511466513f7ddb550760`  
Date: 2026-09-06 Europe/Amsterdam

## Status

`IMPLEMENTATION_BLOCKED — no product implementation defect established; actual deployed browser verification requires a browser-capable independent worker/environment.`

No product/runtime/source change is made by this dispatch.

## Completed work

- re-read the canonical current queue after PR #127 PASS/merge;
- confirmed WP-CONVERGENCE-05 / #96 is the sole current Repository Convergence product-facing gate;
- inspected #96 current body/provenance;
- reconstructed the deployed repair contract from merged PR #108 and PR #111 plus current regression tests;
- confirmed current source-level marker/placeholder expectations from `tests/test_review_marker_compaction_live_regression.py`;
- confirmed all recorded `Polderweg 8` contexts and legitimate longer-address preservation from `tests/test_dutch_address_span_precision.py`;
- preserved the distinction between source/AppTest/CI/HF sync evidence and actual deployed UI behavior;
- checked the public HF Space health page: Space reports `Running`;
- attempted the simplest autonomous browser route outside product code, but the local browser runtime in this execution environment has no outgoing network access to the public HF Space;
- verified normal web fetch only reaches the Streamlit JavaScript shell and cannot establish interactive user behavior;
- searched available plugin/connectors for a browser-capable interaction surface; no installed generic browser/computer-use connector is available in this chat;
- created issue #129 as a complete fresh independent browser-capable live verification package;
- added a current evidence/dispatch comment to #96 and deliberately left #96 OPEN.

## Exact starting/deployment evidence

Current governed `main`:

```text
a0fe29306a1f6875058d511466513f7ddb550760
```

PR #127 post-merge evidence supplied and independently recorded by the preceding assurance worker:

```text
Tests run 34027429725 / job 101470788209
1282 passed in 12.72s
SUCCESS

GitHub → Hugging Face sync
34027429743 / job 101470788494
SUCCESS
2d4ab04..a0fe293 HEAD -> main
```

This is machine/deployment evidence only; it does not close #96.

## Reconstructed live acceptance contract

### Standard / Expert and state lineage

- same current source remains authoritative across Standard↔Expert roundtrip;
- review/include decision remains bound to current document/generation;
- stale processed/review state is not reused as current;
- current replacements apply to current source/generation;
- export/Scrub Key controls require current reviewed state;
- reinsert uses correct current key/document and fails visibly for mismatch/mixed identifiers;
- mandatory human review remains required.

### Marker offsets / compact strict bound placeholders

Current regression source requires:

- leading blank lines/whitespace do not shift processed highlight spans;
- highlighted spans identify the complete authoritative strict bound tokens;
- long bound token remains internal while display compacts to forms equivalent to `[ORGANISATIE_02]` / `[LOCATIE_01]`;
- no shifted-marker fragmentation or long-token leakage;
- compact display survives marker/highlight toggle behavior.

### Dutch address precision

Exact recorded live contexts:

```text
Beschrijving Polderweg 8
De inspectie bezoekt Polderweg 8
Nu Polderweg 8 de
Op Polderweg 8
Polderweg 8 een
Polderweg 8 en
Polderweg 8 in
Polderweg 8 is
Polderweg 8 na
Polderweg 8 op
```

Expected privacy-sensitive address span:

```text
Polderweg 8
```

Representative legitimate longer form to preserve coherently:

```text
Laan van Meerdervoort 55, 2517 AM Den Haag
```

## Files added/changed

This worker made no change to product/source/current main.

Outside `main`, this handover branch adds only:

```text
handover/workpackages/20260906_1246_repository_convergence_consolidated_live_app_verify_dispatch.md
```

Administrative GitHub state:

- issue #129 created;
- #96 received one evidence/dispatch comment and remains OPEN.

## Tests

No new code/tests were required or authorized for this dispatch.

Existing relevant current tests inspected:

- `tests/test_review_marker_compaction_live_regression.py`;
- `tests/test_dutch_address_span_precision.py`.

Current exact-main full regression evidence remains:

```text
34027429725 / 101470788209
1282 passed in 12.72s
SUCCESS
```

## Validation status

- source-level repair contracts: reconstructed;
- exact main/deployment evidence: available;
- public HF Space health: Running;
- actual interactive deployed UI verification: **NOT COMPLETE**;
- issue #96: **OPEN / UNPROVEN**;
- independent verification dispatch: #129 OPEN.

## GitHub Actions status

Exact main `a0fe29306a1f6875058d511466513f7ddb550760`: full Tests SUCCESS per run `34027429725`.

## Hugging Face sync status

Exact main sync SUCCESS per run `34027429743`; public Space reports Running.

This does not prove live behavior.

## App verification status

`NOT COMPLETE — #96 remains unproven.`

The current chat environment cannot interact with the deployed Streamlit application:

- ordinary web access returns the JS shell only;
- local Chromium/Playwright environment cannot reach the public internet/HF Space;
- no installed generic remote browser/computer-use connector is available here.

This is a genuine external capability blocker for this worker, not a product failure.

## Remaining risks

1. The consolidated post-repair deployed user-flow remains unobserved.
2. Marker offsets and compact placeholder display must be proven together in the real rendered review pane.
3. `Polderweg 8` span precision must be proven in the deployed app, not inferred from source tests.
4. Standard↔Expert/review/export/reinsert state lineage must be observed live.
5. R1 false negatives, R2 Scrub Key and R10 Zorg remain critical.
6. Live PASS cannot imply perfect anonymisation, perfect recall or production safety.
7. Stage 2 remains blocked.

## Exact blocker

A fresh independent worker with a browser-capable environment that can click/type/upload/download in the public Hugging Face Streamlit Space is required.

No further source change is justified merely to overcome this verification-tool limitation.

## Next recommended step

Execute issue #129 completely as a fresh `governance_release_assurance` worker in a browser-capable environment (for example ChatGPT Work/Cloud Browser or another approved interactive browser surface).

- PASS: record exact live evidence on #96, close #96, write assurance handover, close #129, then stop.
- FAIL: keep #96 open, record exact defect, return smallest root-cause repair to `implementation_operations`.
- INDETERMINATE: keep #96 open and state exact missing browser/deployment evidence.

Do not start `WP-CONVERGENCE-FINAL`, declare `SCRUB_REPOSITORY_CONVERGED`, or start Stage 2 from the WP05 assurance role.
