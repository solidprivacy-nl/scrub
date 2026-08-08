## 2026-08-08 16:55 Europe/Amsterdam — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — repair after blind-assurance FAIL

Status: `RELEASE_CANDIDATE_READY` only after a fresh exact-head full-suite run; fresh independent assurance remains mandatory.

Independent assurance on prior head `2b04ca6260bddee07fbcf901239cee2955bd6dc7` returned `FAIL` because switching `Standaard → Expert` could silently reset an explicitly selected Zorg profile to the hard-coded Expert default Juridisch. The same repair cycle reviewed operator, threshold, entity selection, allow/deny lists and analyzer configuration as processing-affecting state.

Repair:
- Standard and Expert now hydrate the same persisted processing settings;
- entering Expert no longer uses a hard-coded recognition-profile or operator default when a valid current choice exists;
- returning to Standard rehydrates the Standard profile widget from the shared processing state;
- threshold, entity selection, allow/deny lists and analyzer/model settings are preserved across presentation-only switches;
- deterministic processing-generation synchronization now runs in both presentation modes;
- presentation-only switching with unchanged settings preserves valid downstream lineage;
- a real processing-affecting Expert change invalidates processed/review/export lineage fail-closed;
- Standard still refuses unsupported Expert-only operators without silently rewriting them.

Regression evidence before administrative finalization:
- GitHub Actions Tests run #2229 / ID `31263099583`, job `93116829430`;
- PR merge candidate `bd3c404f7075d86620272bf28c9a5192006e8209`;
- `python -m pytest -q tests` → `1235 passed in 14.48s`;
- new coverage explicitly includes Standard Zorg → Expert → Standard state preservation and real-change invalidation.

Protected semantics unchanged:
- recognizers/profile rules and threshold meaning;
- review-table/include authority and direct masking;
- export bytes, filenames and MIME types;
- Scrub Key, reinsert and audit semantics;
- dependencies and local/cloud processing boundary;
- mandatory human review.

A fresh exact-head regression is required after this administrative closeout, followed by a new blind `governance_release_assurance` review. The later Premium Input Stage package remains blocked.

---

## 2026-08-08 15:28 Europe/Amsterdam — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION — release candidate prepared

Status: `RELEASE_CANDIDATE_READY`; final exact-head CI and fresh independent assurance required before merge.

Purpose:
- move the merged Premium staged-workspace architecture from helper/state primitives into the production Streamlit shell;
- make Standard behave as one persistent document workspace with `Toevoegen → Controleren → Downloaden` and exactly one dominant stage;
- preserve Expert and all existing processing/review/export/Scrub Key/reinsert/audit semantics.

Implemented:
- global `Anonimiseren | Terugzetten` and `Standaard | Expert` controls;
- persistent application-panel stage headers with active/completed/future states;
- compact completed summaries and passive future stages;
- primary `Document verwerken` and `Controle afronden` progression actions;
- explicit earlier-stage return;
- deterministic processing lineage and fail-closed downstream invalidation;
- current-generation analysis cache to prevent silent recognition reruns during stage navigation;
- cached review rows; reopening a completed Review invalidates Download until Review is explicitly completed again;
- Standard hides the permanent settings sidebar while Expert retains advanced controls;
- Standard does not silently modify Expert-only `highlight`/`synthesize` operator choices;
- legacy runtime source patch exits for the direct Premium shell, preventing the retired form/two-mode UI from being re-injected at startup.

Files added:
- `premium_streamlit_state.py`;
- `premium_streamlit_shell_ui.py`;
- `tests/test_premium_streamlit_state.py`;
- `tests/test_premium_app_shell_streamlit_integration.py`;
- implementation claim and handover.

Files changed:
- `premium_app_shell.py`;
- `presidio_streamlit.py`;
- `fix_streamlit_nested_expanders.py`;
- source-level UI contract tests updated where literal expectations described the retired shell;
- `WORKPACKAGES.md`, `CHANGELOG.md`, `RELEASE_NOTES.md` for closeout administration.

Validation:
- clean runtime/product head `0e1a5fbb3d6c3b8f8293779e598ececd6ea4aa1d`;
- GitHub Actions Tests #2200 / run `31259576962`, job `93108182555`;
- `python -m pytest -q tests` → `1225 passed in 12.55s`;
- final post-administration exact-head full regression still required before assurance;
- Hugging Face sync and live app verification are pending after PASS/merge because runtime UI changed.

Intentionally unchanged:
- recognizers/profile rules and threshold meaning;
- replacement/include authority and direct masking semantics;
- export bytes, filenames and MIME types;
- Scrub Key schema/binding/lifecycle;
- reinsert and audit semantics;
- dependencies and cloud/local-processing boundary;
- mandatory human review.

Next gate:
- freeze final exact head after this administrative closeout;
- full GitHub Actions regression;
- fresh blind `SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY`;
- no merge and no Input Stage work before independent PASS.

---

## 2026-08-08 Europe/Amsterdam — SCRUB-WP_PREMIUM_STAGED_WORKSPACE_DECISION_FREEZE — staged workspace architecture candidate

Status: `IMPLEMENTATION_IN_PROGRESS`; exact-head CI and independent assurance required before merge.

Purpose:
- convert the coordinator-approved first-principles comparison of three routed screens versus a one-page staged workspace into a binding Premium UI architecture decision;
- intervene before PR #85 enters production `presidio_streamlit.py` integration;
- make the Premium staged-workspace sequence the authoritative active execution queue.

Decision:
```text
One document. One workspace. Three stages. One active task.

Toevoegen → Controleren → Downloaden
```

Binding Standard behavior:
- all three stage headers remain in one persistent page/workspace;
- exactly one stage is expanded/dominant at a time;
- completed stages collapse to compact status summaries;
- future stages remain visible but passive;
- successful completion auto-advances to the next stage;
- deliberate return to an earlier stage remains possible;
- processing-affecting earlier changes invalidate processed/review/export lineage fail-closed;
- three separate routed pages are rejected for these core stages;
- a classic nested-expander form is also rejected as the default Standard pattern.

First-principles rationale:
- Scrub is an iterative document-review workflow, not a strictly linear checkout;
- the interface should represent document state rather than page navigation;
- the staged workspace preserves one-task-at-a-time focus while retaining document identity, progress, correction context and visible trust state;
- it aligns directly with the merged `premium_core_flow_state.py` generation/invalidation model and reduces routing/state-restoration complexity in Streamlit.

Current PR #85 consequence:
- PR #85 is amended, not discarded;
- current pure `premium_app_shell.py` helper work remains reusable;
- production Streamlit integration is gated until this decision is independently assured and incorporated;
- PR #85 must add/test completed/future/active panels, compact summaries, auto-progression hooks, prior-stage return/edit and no-three-page semantics before production integration.

Files added/changed in the candidate:
- added `PREMIUM_STAGED_WORKSPACE_DECISION.md`;
- updated `ROADMAP.md`;
- updated `WORKPACKAGES.md` with an authoritative current Premium queue while retaining older content as historical records;
- updated `DECISION_LOG.md` with D043;
- updated `CHANGELOG.md`;
- added `tests/test_premium_staged_workspace_decision.py`;
- added implementation claim and handover administration.

Validation boundary:
- documentation/architecture/contract-only package;
- no production Streamlit or runtime product behavior changes;
- no recognizer, threshold, replacement, review authority, export bytes/names/MIME, Scrub Key, reinsert, audit, dependency or Hugging Face behavior changes;
- Hugging Face sync: not applicable;
- app verification: not applicable;
- exact-head GitHub Actions and independent `governance_release_assurance` remain required before merge.

---

## 2026-08-07 Europe/Amsterdam — Issue #70 Actions evidence recovery repair

Status: `RELEASE_CANDIDATE_READY`; independent exact-head assurance pending.

- Replaced PR #73's expired 2026-06-17 carrier dependency with a purpose-built read-only no-op carrier workflow.
- Demonstrated current connector executability: carrier run `31216068355` was rerun successfully as attempt 2; latest rerun job `92989859101` concluded `success`.
- Full PR regression run `31216068325` / #2115 passed all `1170` tests in `11.00s` using the unchanged `python -m pytest -q tests` command.
- Strengthened the workflow contract tests to freeze carrier safety, rerun gating, default-branch checkout semantics and unchanged full-suite behavior.
- No recognizer, review, replacement, export, Scrub Key, reinsert, UI, document-processing, dependency or Hugging Face product behavior changed.
- Fresh blind `governance_release_assurance` remains mandatory for the final exact PR head before merge; issue #70 stays open until independent exact-main post-merge evidence is confirmed.

## 2026-08-06 21:30 Europe/Amsterdam — SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY / SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY

Status: both initial assurance decisions `PASS`; PR #69 merged unchanged; post-action closeout remains `ACTION_EXECUTED_UNVERIFIED` because no distinct Actions push run on the actual merged SHA was observable.

Purpose:
- independently reconstruct and decide the two verification packages under issue #70;
- preserve the blind-review boundary before reading implementation handovers, claims or conclusions;
- merge the passing candidate without assurance-side repair;
- record separate verification claims and handovers.

Assurance decisions:
- `SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION_VERIFY`: `PASS`;
- `SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION_VERIFY`: `PASS`.

Action and evidence:
- candidate head: `41bf09abe3966ae40a51c526d162c57a824557e8`;
- tested merge candidate: `13d55b6d74ad6f31446e16bcad0794abea32f9e7`;
- raw run #2105 / ID `31091265208`: `1165 passed in 12.41s`;
- actual merge commit: `07cf12d0cfa57dd81bd2c964cb081e5f8f8c4f71`;
- actual and tested merge candidates have identical parents and identical tree `4c993cbed86eade252cec6799f7dae5919b84085`;
- candidate repairs: none.

Files added:
- `workpackage_claims/scrub_wp_two_role_governance_adoption_verify.md`;
- `workpackage_claims/scrub_wp_processed_text_selection_cross_flow_regression_verify.md`;
- `handover/workpackages/20260806_2130_two_role_governance_adoption_verify.md`;
- `handover/workpackages/20260806_2130_processed_text_selection_cross_flow_regression_verify.md`.

Files changed:
- `WORKPACKAGES.md`;
- `CHANGELOG.md`.

Validation:
- implementation handovers and claims were opened only after the two initial decisions and were administratively complete;
- no distinct GitHub Actions push run on merged SHA `07cf12d0cfa57dd81bd2c964cb081e5f8f8c4f71` was observable at closeout-writing time, so `OUTCOME_CONFIRMED` is not claimed;
- Hugging Face sync: not applicable because no runtime file changed and all changed paths are ignored by the sync workflow;
- app verification: not applicable because no UI behavior changed.

Intentionally not changed:
- candidate source, tests or candidate head;
- production Python, Streamlit, frontend, runtime, dependency or deployment behavior;
- recognizers, review semantics, exports, Scrub Key, reinsert or audit semantics;
- human-review and local-processing boundaries.

## 2026-08-06 11:37 Europe/Amsterdam — SCRUB-WP_TWO_ROLE_GOVERNANCE_ADOPTION / SCRUB-WP_PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION

Status: implementation `RELEASE_CANDIDATE_READY`; GitHub Actions PR #69 run #2097 green (`1165 passed in 9.62s`); independent governance assurance pending.

Purpose:
- adopt the Weekly ETF donor's canonical implementation-versus-release-assurance model for Scrub;
- strengthen it with a blind-review boundary so the assurance worker does not read implementation conclusions before its initial decision;
- add end-to-end synthetic regression evidence from processed-text selection commit through exports, bound Scrub Key, TXT/DOCX reinsert and audit outputs.

Files added:
- `control/PROJECT_GOVERNANCE_BOOTSTRAP.md`;
- `control/SCRUB_RELEASE_ASSURANCE_CONTRACT_V1.md`;
- `PROCESSED_TEXT_SELECTION_CROSS_FLOW_REGRESSION.md`;
- `tests/test_processed_text_selection_cross_flow_regression.py`;
- implementation claim and handover files.

Files changed:
- `PROJECT_PROMPT.md`;
- `PROJECT_PROMPT_SHORT.md`;
- `ROADMAP.md`;
- `WORKPACKAGES.md`;
- `DECISION_LOG.md`;
- `CHANGELOG.md`.

Regression coverage:
- selection-created row provenance, binding, all-exact occurrence count and authoritative include state;
- processed text/TXT export;
- original-DOCX replacement path;
- schema-1.1 bound Scrub Key generation and fail-closed custom-text behavior;
- verified TXT and DOCX reinsert;
- replacement CSV and scrub-report audit evidence;
- local-only/no-AI/no-cloud metadata.

Validation:
- local execution unavailable in this connector-only session;
- GitHub Actions PR #69 run #2097: `1165 passed in 9.62s`;
- independent governance decisions deliberately not issued by implementation.

Intentionally not changed:
- production Python/Streamlit behavior;
- recognizers, profiles, thresholds or review decisions;
- export bytes, filenames or MIME types;
- Scrub Key schema/binding or reinsert semantics;
- audit semantics, dependencies, runtime or Hugging Face app behavior.

## 2026-08-05 10:49 Europe/Amsterdam — SCRUB-WP_PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN

Status: completed planning/design-only.

Purpose:
- Convert new live-app UX evidence into a structural interface strategy rather than another isolated decluttering patch.

Result:
- added `PREMIUM_CORE_FLOW_UI_REALIGNMENT_PLAN.md`;
- documented the gap between the implemented review-local Basic/Expert split and an application-wide presentation model;
- defined top-level Anonymize/Reinsert workflows;
- defined global Standard/Expert visibility and grouping;
- defined one-active-stage `Toevoegen → Controleren → Downloaden` behavior;
- defined no permanent settings sidebar in Standard;
- defined one recommended document download with other formats, Scrub Key and audit evidence secondary;
- sequenced contract, pure state model, app shell, input, review, export, Expert parity and app verification packages;
- added planning contract tests;
- changed no runtime product behavior.

Intentionally not changed:
- Streamlit product code;
- recognizers, profiles, replacement logic or review decisions;
- export payloads, filenames or MIME types;
- Scrub Key or reinsert semantics;
- runtime, dependencies or cloud-processing boundaries.

## 2026-08-05 10:49 Europe/Amsterdam — SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION_APP_VERIFY_CLOSEOUT

Status: completed; deployment and live app verification green.

Validation:
- PR #66 merged as `74b7a15ee74f6330f7fc37892b65246c1a61afaf`;
- final run #2080: 1155 tests passed in 12.44s;
- deployment run #2082: 4/4 files exact, Space health `ok`, root HTTP 200, frontend tests passed and 1155 tests passed in 11.49s;
- coordinator/user confirmed shorter replacement codes are visible and working.

Intentionally not changed:
- full bound tokens in exports;
- 80-bit binding entropy;
- Scrub Key, reinsert or export semantics;
- human-review and production-readiness boundaries.

## 2026-08-04 22:22 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_APP_VERIFY_CLOSEOUT

Status: completed; deployment and live app verification green.

Purpose:
- Close the processed-text selection integration after independent deployment checks and coordinator/user browser verification.

Validation:
- PR #63 merged as `53fad202ae88a97b1ea476a9c3ba787932cd62ae`;
- final merge-candidate run #2051: 1146 tests passed in 11.59s;
- independent deployment run #2064: 11/11 runtime/component files matched Hugging Face, Space health was `ok`, root returned HTTP 200, frontend tests passed, and 1146 Python tests passed in 11.47s;
- coordinator/user confirmed `Het werkt.` with a deployed-app screenshot.

Observed follow-up:
- bound placeholders remain safe but visually noisy because the same 80-bit binding ID is repeated;
- four-character binding IDs are rejected as an unsafe weakening;
- display-only compaction is routed to `SCRUB-WP_BOUND_PLACEHOLDER_DISPLAY_COMPACTION`.

Intentionally not changed:
- product code, placeholder grammar and binding entropy;
- export, Scrub Key, reinsert, recognizers, profiles or dependencies;
- production-readiness and human-review boundaries.

## 2026-08-04 01:34 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION

Status: completed in GitHub; deployment and app verification pending.

Purpose:
- Make direct selection in `Verwerkte tekst` a safe input route into the existing manual replacement-table path.

Files added:
- `processed_text_selection_integration.py`
- `tests/test_processed_text_selection_integration.py`
- `tests/test_processed_text_selection_table_integration_contract.py`
- `PROCESSED_TEXT_SELECTION_TABLE_INTEGRATION.md`
- `workpackage_claims/scrub_wp_processed_text_selection_table_integration.md`
- `handover/workpackages/20260804_0134_processed_text_selection_table_integration.md`

Files changed:
- `processed_text_selection_component.py`
- `side_by_side_review_panel_ui.py`
- `presidio_streamlit.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Implementation:
- promoted the local component wrapper while retaining the isolated spike alias;
- added interactive review with environment-controlled and exception-safe static fallback;
- added server-protected spans independent of marker visibility;
- processed inspect/commit only after the editable table and before serial review/export;
- appended one bound normal manual row through document-scoped `manual_mask_rows`;
- added immediate reruns, feedback and safe one-step undo;
- blocked undo when the visible table row was subsequently edited;
- retained the full review table and existing manual form.

Validation:
- cleanup run #2044: frontend component tests passed; two obsolete phase-status assertions failed in Python only;
- final clean PR run #2047: 1146 Python tests passed in 11.97s;
- Hugging Face sync and live app verification pending.

Intentionally not changed:
- all-exact version-one scope;
- export formats, filenames, MIME or download behavior;
- Scrub Key schema, binding, digest, warning or lifecycle;
- reinsert semantics;
- recognizers, profiles, thresholds or dependencies;
- external network, telemetry, browser persistence or cloud processing.

## 2026-08-04 01:00 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE

Status: completed; technical validation green.

Purpose:
- Prove the browser/component layer before connecting selection events to the production replacement table.

Files added:
- `processed_text_selection_component.py`
- `processed_text_selection_component_spike_demo.py`
- `frontend/processed_text_selection_component/index.html`
- `frontend/processed_text_selection_component/styles.css`
- `frontend/processed_text_selection_component/streamlit_bridge.js`
- `frontend/processed_text_selection_component/component_core.js`
- `frontend/processed_text_selection_component/component.js`
- `frontend/processed_text_selection_component/NOTICE.md`
- `tests/test_processed_text_selection_component_spike.py`
- `tests/frontend/processed_text_selection_component_core.test.js`
- `PROCESSED_TEXT_SELECTION_COMPONENT_SPIKE.md`
- `workpackage_claims/scrub_wp_processed_text_selection_component_spike.md`
- `handover/workpackages/20260804_0100_processed_text_selection_component_spike.md`

Files changed:
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`

Implementation:
- local lazy Streamlit Components v1 wrapper on pinned Streamlit 1.39;
- Python code-point highlight validation and conversion to UTF-16 browser offsets;
- safe text-node rendering and marked segments;
- DOM selection offsets across plain and marked text nodes;
- synchronized scrolling and scroll restoration;
- right-click, keyboard and visible selection entry points;
- accessible type/confirmation menu;
- inspect event, server result and commit-intent transport;
- standalone synthetic inspection-only demo;
- no runtime build step, external assets, network, storage or telemetry.

Validation:
- run #1977: 1126 tests passed in 13.83s;
- Streamlit 1.39 smoke run #1979: 1126 tests passed in 13.79s;
- AppTest completed without script exceptions;
- local server health `ok`, root HTML and startup log checks passed;
- clean post-governance standard run #1989: 1126 tests passed in 10.87s.

Intentionally not changed:
- `presidio_streamlit.py` and production side-by-side renderer;
- replacement table, exports, Scrub Key or reinsert;
- recognizers, profiles, dependencies or cloud processing;
- occurrence-specific masking.

## 2026-08-04 00:30 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL

Status: completed; validation green.

Purpose:
- Implement the server-authoritative selection action model before any browser or Streamlit integration.

Files added:
- `selection_mask_action.py`
- `tests/test_selection_mask_action.py`
- `PROCESSED_TEXT_SELECTION_MASKING_ACTION_MODEL.md`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_action_model.md`
- `handover/workpackages/20260804_0030_processed_text_selection_masking_action_model.md`

Files changed:
- `manual_mask_entry.py`
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`

Implementation:
- strict schema/action/event/scope/hash/payload parsing;
- exact UTF-16-to-Python index conversion and surrogate-pair rejection;
- quick-selection length, line, control, placeholder and marked-range checks;
- exact occurrence and Unicode-aware embedded-token analysis;
- duplicate and nested included-replacement collision guards;
- ready, confirmation-required and blocked inspection results;
- bounded replay state and opaque single-use inspections;
- commit-time revalidation of document, binding, source, processed text, replacement table and impact;
- existing document-bound manual-row construction for eight internal quick types;
- stable manual action records and fail-closed undo.

Validation:
- initial run #1957 failed from one local event-ID assignment defect and one overly literal test; no safety boundary was weakened;
- corrected run #1961: 1106 tests passed in 10.66s;
- clean standard run #1970: 1106 tests passed in 10.71s.

Intentionally not changed:
- visible manual form options;
- Streamlit, browser component or session state;
- review-table and export/download flows;
- Scrub Key, reinsert, recognizers, profiles or cloud processing;
- occurrence-specific masking or dependencies.

## 2026-08-04 00:09 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_CONTRACT

Status: completed; validation green.

Purpose:
- Convert the approved processed-text selection direction into an exact implementation contract before product code changes.

Files added:
- `PROCESSED_TEXT_SELECTION_MASKING_CONTRACT.md`
- `test_cases/processed_text_selection_masking/contract.json`
- `tests/test_processed_text_selection_masking_contract.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_contract.md`
- `handover/workpackages/20260804_0009_processed_text_selection_masking_contract.md`

Files changed:
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Contract result:
- froze a two-stage `inspect_selection` / `commit_manual_mask` protocol so occurrence impact is server-derived before commitment;
- froze all-exact scope, UTF-16 offset semantics and strict stale/replay handling;
- froze 1–5 ready, 6–20 confirmation-required and >20 blocked impact bands;
- froze 160-code-point single-line selections and an 8192-byte payload cap;
- froze eight broad quick types with server-owned entity and placeholder mappings;
- froze embedded-substring, nested replacement and marked-range collision blocking;
- froze visible, right-click and keyboard access plus one-step undo behavior;
- froze no-network, no-browser-persistence, escaped-rendering and fail-closed boundaries;
- authorized only the pure action-model package next.

Validation:
- machine-readable contract fixture and contract tests added;
- clean contract run #1954: 1027 tests passed in 11.48s;
- Hugging Face sync not functionally relevant;
- app verification not applicable because no runtime behavior changed.

Intentionally not changed:
- `manual_mask_entry.py`, `presidio_streamlit.py` or side-by-side renderer;
- Streamlit/dependency versions or Docker runtime;
- review table, export, Scrub Key or reinsert semantics;
- recognizers, profiles, cloud processing or product claims.

## 2026-08-03 23:42 Europe/Amsterdam — SCRUB-WP_PROCESSED_TEXT_SELECTION_MASKING_PLAN

Status: completed as planning; validation green.

Purpose:
- Assess a document-centric path for correcting missed sensitive values directly from the processed-text pane.

Files added:
- `PROCESSED_TEXT_SELECTION_MASKING_PLAN.md`
- `tests/test_processed_text_selection_masking_plan.py`
- `workpackage_claims/scrub_wp_processed_text_selection_masking_plan.md`
- `handover/workpackages/20260803_2342_processed_text_selection_masking_plan.md`

Files changed:
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `SIDE_BY_SIDE_REVIEW_UX_DIRECTION.md`

Planning result:
- confirmed that the current static `components.html` pane cannot return a supported mutation event;
- recommended a bounded bidirectional Streamlit v1 custom component on the current Streamlit 1.39 stack;
- routed accepted actions through server-side validation and the existing `build_manual_mask_row` path;
- kept the review table authoritative and the manual form available as fallback;
- limited version one to all exact occurrences and deferred occurrence-specific masking to a separate span-aware architecture line;
- defined quick type choices, occurrence-impact warnings, collision blocking, event replay/stale-view protection, scroll restoration, undo, accessibility, XSS and no-external-network requirements;
- defined six sequential test-first implementation workpackages.

Validation:
- documentation/architecture contract tests added;
- PR #59 run #1937: 1015 tests passed in 11.64s;
- one final clean regression follows the status-only update;
- Hugging Face sync not functionally relevant;
- app verification not applicable because no product behavior changed.

Intentionally not changed:
- `presidio_streamlit.py`, side-by-side renderer or manual mask helper;
- Streamlit/dependency versions or Docker runtime;
- replacement table, export, Scrub Key or reinsert semantics;
- recognizers, profiles, cloud processing or product claims.

## 2026-08-03 23:26 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS_APP_VERIFY_CLOSEOUT

Status: completed; final documentation-only regression pending.

Purpose:
- Close the long-form synthetic Zorgfilter corpus after technical deployment verification and coordinator/user app confirmation.

Files added:
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus_app_verify_closeout.md`
- `handover/workpackages/20260803_2326_care_profile_long_form_synthetic_corpus_app_verify_closeout.md`

Files changed:
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md`
- `handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Validation evidence:
- final clean PR #56 run #1926: 1003 tests passed in 11.51s;
- deployment verification run #1931: exact GitHub/Hugging Face matches for both runtime files, health HTTP 200 / `ok`, and 1003 tests passed in 11.35s;
- coordinator/user confirmation at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`

Intentionally not changed:
- product code, synthetic corpus content, UI, recognizers or profile behavior;
- replacement table, export, Scrub Key or reinsert semantics;
- dependencies, cloud processing or product claims.

## 2026-08-03 22:17 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS

Status: completed, synchronized and app-verified.

Purpose:
- Give Zorgfilter testers realistic long-form care documents instead of examples that stop after one short clinical paragraph.

Files added:
- `care_test_example_expansions.py`
- `tests/test_care_profile_long_form_corpus.py`
- `CARE_PROFILE_LONG_FORM_SYNTHETIC_CORPUS.md`
- `workpackage_claims/scrub_wp_care_profile_long_form_synthetic_corpus.md`
- `handover/workpackages/20260803_2217_care_profile_long_form_synthetic_corpus.md`

Files changed:
- `care_test_examples.py`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Implementation result:
- retained all eight stable care-document IDs, names, sectors and document types;
- retained every replace, review-selected, preserve, audit-only and ambiguity-trap contract;
- appended five document-specific sections and at least two hundred words of synthetic care context to every example;
- kept the additions free of digits and new names, identifiers, dates, addresses, contact details, organizations and locations;
- exposed the expanded texts through the existing Zorgfilter example selector without changing the selector or Streamlit flow;
- added tests for length, structure, non-mutation, identity-marker absence, exact expected-value occurrence and UI-adapter parity.

Validation:
- final clean PR run #1926: 1003 tests passed in 11.51s;
- deployment verification run #1931: both runtime files matched Hugging Face byte-for-byte, Space health returned HTTP 200 / `ok`, and 1003 tests passed in 11.35s;
- coordinator/user app verification confirmed at 2026-08-03 23:26 Europe/Amsterdam: `Alles werkt.`

Intentionally not changed:
- recognizers, thresholds, profile composition or collision precedence;
- review selection or replacement-table behavior;
- export filenames, MIME types or formats;
- Scrub Key schema, binding, warnings or lifecycle;
- reinsert behavior, dependencies, cloud processing or production claims.

## 2026-08-03 19:12 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_APP_VERIFY

Status: completed and app-verified after technical deployment verification.

Purpose:
- Independently verify that the merged Zorgfilter integration reached Hugging Face before requesting human app verification.

Files added:
- `CARE_PROFILE_APP_VERIFICATION.md`
- `output/validation/care_profile_hf_sync_verification.json`
- `tests/test_care_profile_hf_sync_verification.py`
- `workpackage_claims/scrub_wp_care_profile_app_verify.md`
- `handover/workpackages/20260803_1912_care_profile_app_verify.md`

Verification result:
- compared twelve relevant GitHub and Hugging Face files byte-for-byte;
- verified equal SHA-256 values for all twelve files;
- verified correctly scoped Zorgfilter markers;
- verified Streamlit health `HTTP 200 / ok` and root HTTP 200;
- corrected an initial verification false negative caused by two marker groups being checked in the wrong modules;
- recorded coordinator/user confirmation `alles groen` at 2026-08-03 20:35 Europe/Amsterdam;
- confirmed all nine visible verification checks and retained the non-production/human-review boundary.

Validation context:
- UI integration final run #1885 passed: 986 tests;
- cross-profile matrix final run #1906 passed: 995 tests;
- verification-only run #1908 passed 998 tests; final closeout run #1909 passed 998 tests in 10.45s.

Intentionally not changed:
- product code, recognizers, profile behavior or UI;
- review, export, Scrub Key or reinsert semantics;
- runtime dependencies, cloud processing or production claims.

## 2026-08-03 18:58 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX

Status: completed and regression-green.

Purpose:
- Add deterministic evidence that the new Care profile remains isolated from Legal and General profiles and preserves clinical meaning.

Files added:
- `care_profile_cross_profile_matrix.py`
- `CARE_PROFILE_CROSS_PROFILE_REGRESSION_MATRIX.md`
- `tests/test_care_profile_cross_profile_matrix.py`
- `output/validation/care_profile_cross_profile_matrix.json`
- `workpackage_claims/scrub_wp_care_profile_cross_profile_regression_matrix.md`
- `handover/workpackages/20260803_1858_care_profile_cross_profile_regression_matrix.md`

Implementation result:
- executed real deterministic Dutch custom recognizers across four configured profiles;
- covered eight care-document families and twelve legal examples;
- verified 108/108 dedicated Care expectations across Care and International;
- verified Care/International and Legal/International dedicated-type parity;
- verified no dedicated Care/Legal leakage into the wrong profiles;
- verified zero overlap with protected clinical phrases;
- separated hard profile gates from historical legal metadata observations;
- preserved sixteen historical legal metadata gaps and four negative observations in the evidence snapshot;
- added snapshot reproducibility checks for all twenty observations.

Validation:
- run #1887 exposed an invalid hard-contract assumption for historical legal metadata;
- run #1888 made all twenty observations explicit;
- run #1890 passed after correcting the methodology: 994 tests;
- run #1897 exposed only an incorrect legal-example count in the snapshot;
- run #1899 passed: 995 tests in 9.56s;
- final clean run #1906 passed: 995 tests in 9.96s.

Intentionally not changed:
- current Streamlit UI or profile selector;
- review table, export, Scrub Key or reinsert semantics;
- runtime dependencies, cloud processing or production claims;
- generic NER behavior.

## 2026-08-03 18:28 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_CURRENT_UI_INTEGRATION

Status: completed, deployed and app-verified.

Purpose:
- Promote the approved Zorgfilter profile into the current Streamlit/analyzer flow after policy, corpus, recognizer and profile-configuration gates passed.

Files added:
- `care_candidate_scanner.py`
- `profile_ui_support.py`
- `CARE_PROFILE_CURRENT_UI_INTEGRATION.md`
- `output/validation/care_profile_current_ui_integration.json`
- `tests/test_care_candidate_scanner.py`
- `tests/test_profile_ui_support.py`
- `tests/test_presidio_helpers_care_registration.py`
- `tests/test_care_profile_current_ui_integration_snapshot.py`
- `workpackage_claims/scrub_wp_care_profile_current_ui_integration.md`
- `handover/workpackages/20260803_1828_care_profile_current_ui_integration.md`

Files changed:
- `presidio_helpers.py`
- `presidio_streamlit.py`
- `document_tools.py`
- `display_labels_nl.py`
- `ui_texts_nl.py`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `RISK_REGISTER.md`

Implementation result:
- registered sixteen dedicated care recognizers;
- added `Zorgcontrole — streng` while preserving the existing three labels and Legal default;
- centralized thresholds, profile descriptions and default entity composition;
- applied profile-level exact-span collision resolution;
- added eight synthetic care examples and a conservative unchecked candidate layer;
- aligned review-selected care detections to `Controle nodig` while keeping them selected;
- added care display labels and stable placeholders;
- generalized app copy from Legal-only to professional Legal/Zorg use;
- preserved review table, export, Scrub Key and reinsert semantics.

Validation:
- run #1876 failed only because the new registration test imported optional Streamlit dependencies absent from lean CI;
- test isolation was corrected without changing runtime code or dependencies;
- run #1877 passed: 983 tests in 9.69s;
- final clean integration run #1885 passed: 986 tests;
- Hugging Face synchronization verified byte-for-byte for 12/12 relevant files;
- deployed app verification confirmed `alles groen` by the coordinator/user.

Intentionally not changed:
- export filenames, MIME types and document formats;
- Scrub Key schema, binding, warnings or lifecycle;
- TXT/DOCX/PDF-to-TXT reinsert semantics;
- cloud processing, runtime dependencies or production claims;
- broad free-text medical scanning.

## 2026-08-03 17:12 Europe/Amsterdam — SCRUB-WP_RECOGNITION_PROFILE_CONFIGURATION_REFACTOR

Status: completed; pure recognition-profile configuration implemented.

Purpose:
- Replace scattered future profile branching with one tested source of truth before exposing Zorg in the current UI.

Files added:
- `recognition_profiles.py`
- `recognition_profile_validation.py`
- `RECOGNITION_PROFILE_CONFIGURATION.md`
- `tests/test_recognition_profiles.py`
- `tests/test_recognition_profile_validation.py`
- `output/validation/recognition_profile_configuration.json`
- `workpackage_claims/scrub_wp_recognition_profile_configuration_refactor.md`
- `handover/workpackages/20260803_1712_recognition_profile_configuration_refactor.md`

Implementation result:
- preserved the exact current three-profile order and labels;
- defined the future Streamlit and desktop four-profile orders;
- centralized thresholds, entity groups, candidate/example direction and Care policy actions;
- added deterministic exact-span precedence for fifteen care-specific winners;
- kept partial overlaps and all non-Care profile results unchanged;
- kept live UI and care recognizer registration explicitly false.

Validation:
- initial GitHub Actions run #1865 passed: 965 tests;
- final clean validation pending after governance finalization;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- `presidio_streamlit.py`, `presidio_helpers.py` or current analyzer registration;
- visible profile selector, thresholds or entity defaults;
- review, export, Scrub Key or reinsert semantics;
- runtime, dependencies or cloud processing.

## 2026-08-03 16:52 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_RECOGNIZER_IMPLEMENTATION

Status: completed; pure recognizer implementation validated.

Purpose:
- Implement the frozen Zorgfilter recognizer contract without registering it in the current app.

Files added:
- `dutch_care_recognizers.py`
- `care_recognizer_validation.py`
- `CARE_RECOGNIZER_IMPLEMENTATION_V1.md`
- `scripts/generate_care_recognizer_validation.py`
- `tests/test_dutch_care_recognizers.py`
- `tests/test_care_recognizer_validation.py`
- `output/validation/care_recognizer_implementation_validation.json`
- `workpackage_claims/scrub_wp_care_profile_recognizer_implementation.md`
- `handover/workpackages/20260803_1652_care_profile_recognizer_implementation.md`

Implementation result:
- implemented sixteen dedicated, context-bound care entities;
- returned exact value-only Presidio spans with explanations and metadata;
- corrected bounded variants for Dutch client labels, prescription numbers, generic incident labels and lowercase residential-care organization labels;
- passed all frozen positive and negative contracts;
- covered all 54 dedicated corpus expectations with zero protected-clinical overlaps;
- kept app registration explicitly false.

Validation:
- initial run #1850 exposed five bounded missing context variants and no clinical-overmasking failure;
- corrected GitHub Actions run #1854 passed: 953 tests;
- final clean validation pending after governance finalization;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- `presidio_helpers.py`, `presidio_streamlit.py` or current profile behavior;
- thresholds, entity defaults or generic NER;
- review, export, Scrub Key or reinsert semantics;
- runtime, dependencies or cloud processing.

## 2026-08-03 16:34 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_RECOGNIZER_CONTRACT_TESTS

Status: completed; test/specification contract frozen.

Purpose:
- Define dedicated Zorgfilter recognizer behavior before writing implementation code.

Files added:
- `CARE_RECOGNIZER_CONTRACT_V1.md`
- `care_recognizer_contracts.py`
- `care_recognizer_contract_summary.py`
- `tests/test_care_recognizer_contracts.py`
- `scripts/generate_care_recognizer_contract_summary.py`
- `output/validation/care_recognizer_contract_v1_summary.json`
- `workpackage_claims/scrub_wp_care_profile_recognizer_contract_tests.md`
- `handover/workpackages/20260803_1634_care_profile_recognizer_contract_tests.md`

Implementation result:
- froze sixteen dedicated care entities and the future pure helper API;
- added 37 positive exact-span fixtures;
- added 16 negative/collision/clinical-preservation fixtures;
- froze replace/review-selected policy alignment;
- froze care-event/date-of-birth and AGB/BSN precedence;
- kept generic PERSON/e-mail outside the dedicated care module.

Validation:
- GitHub Actions pending final PR validation;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- recognizer implementation or registration;
- current profile selector, thresholds or entity defaults;
- review, export, Scrub Key and reinsert semantics;
- runtime, dependencies or cloud processing.

## 2026-08-03 16:25 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_GAP_TRIAGE

Status: completed; evidence-driven gap routing implemented.

Purpose:
- Convert the current-engine care baseline into explicit recognizer, profile and collision-prevention contract routes.

Files added:
- `CARE_PROFILE_GAP_TRIAGE.md`
- `care_profile_gap_triage.py`
- `care_profile_gap_triage_summary.py`
- `tests/test_care_profile_gap_triage.py`
- `scripts/generate_care_profile_gap_triage.py`
- `output/validation/care_profile_v1_gap_triage.json`
- `workpackage_claims/scrub_wp_care_profile_gap_triage.md`
- `handover/workpackages/20260803_1625_care_profile_gap_triage.md`

Implementation result:
- classified all 81 expectations with zero unclassified values;
- froze six implementation routes and five contract families;
- separated generic NER dependencies from care-specific rule work;
- routed ten broad-entity matches to care-specific reclassification;
- routed 36 context-dependent values to review-selected recognition;
- made AGB/BSN and medical-number collision guards mandatory;
- preserved clinical-content negative contracts as a first-class requirement.

Validation:
- GitHub Actions pending final PR validation;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- recognizer implementation or registration;
- profile selector, thresholds or entity defaults;
- review, export, Scrub Key or reinsert semantics;
- runtime, dependencies or cloud processing.

## 2026-08-03 16:10 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_CURRENT_ENGINE_BASELINE

Status: completed; evidence baseline implemented and validated.

Purpose:
- Establish a corrected, reproducible pre-Zorgfilter measurement for the current deterministic Dutch custom recognizers.

Files added:
- `CARE_PROFILE_CURRENT_ENGINE_BASELINE.md`
- `care_profile_baseline_summary.py`
- `tests/test_care_profile_baseline_summary.py`
- `output/validation/care_profile_v1_current_engine_baseline.json`
- `workpackage_claims/scrub_wp_care_profile_current_engine_baseline.md`
- `handover/workpackages/20260803_1610_care_profile_current_engine_baseline.md`

Files changed:
- `care_profile_baseline.py`
- `scripts/generate_care_profile_baseline.py`
- `tests/test_care_profile_current_engine_baseline.py`
- `ROADMAP.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`

Implementation result:
- changed baseline matching from substring containment to exact normalized span equality;
- prevented false AGB coverage from an eight-digit prefix inside a longer BIG number;
- added compact policy/entity/case summaries;
- committed a reproducible JSON evidence artifact;
- documented 25/81 span recall, 14/81 correct-entity recall, 11 misclassifications, 56 misses and zero protected-clinical overlaps.

Validation:
- diagnostic run #1825 produced the evidence while 918 non-diagnostic tests passed;
- final clean GitHub Actions validation required after temporary diagnostics were removed;
- Hugging Face sync not functionally relevant;
- app verification not applicable.

Intentionally not changed:
- recognizer registration or behavior;
- current profile selector or UI;
- thresholds or entity defaults;
- review, export, Scrub Key and reinsert semantics;
- dependencies, runtime or cloud processing.

## 2026-08-03 15:31 Europe/Amsterdam — SCRUB-WP_CARE_PROFILE_V1_POLICY_AND_CORPUS_FOUNDATION

Status: completed; policy/corpus foundation implemented and validated.

Purpose:
- Create the evidence base for an explicit Dutch Zorg profile without prematurely changing recognizers or the UI.

Files added:
- `CARE_PROFILE_V1_PLAN.md`
- `care_profile_policy.py`
- `care_test_examples.py`
- `care_profile_baseline.py`
- `scripts/generate_care_profile_baseline.py`
- `tests/test_care_profile_policy_contract.py`
- `tests/test_care_profile_corpus_contracts.py`
- `tests/test_care_profile_current_engine_baseline.py`
- `workpackage_claims/scrub_wp_care_profile_v1_policy_and_corpus_foundation.md`

Main changes:
- froze replace/review/preserve/audit-only care policy actions;
- added eight fully synthetic document families;
- separated patient identifiers from provider/location review and clinical content preservation;
- added a deterministic baseline helper for current Dutch custom recognizers;
- made no recognizer or product-UI behavior change.

Validation:
- full GitHub Actions run #1818 passed: 918 tests;
- Hugging Face sync not functionally relevant because no runtime/UI file changed;
- app verification not applicable.

Intentionally not changed:
- current three profile choices;
- recognizer registration or thresholds;
- review table, export, Scrub Key and reinsert semantics;
- runtime, dependencies or cloud processing.

## 2026-08-03 14:47 Europe/Amsterdam — SCRUB-WP_AI_FIRST_DESKTOP_PACKAGING_ROADMAP_ALIGNMENT

Status: completed; roadmap/decision documentation only.

Purpose:
- Incorporate an AI-first cost and authority model into the final local EXE/MSI roadmap while preserving security and release accountability.

Files added:
- `AI_FIRST_DESKTOP_PACKAGING_EXECUTION_MODEL.md`
- `handover/workpackages/20260803_1447_ai_first_desktop_packaging_roadmap_alignment.md`
- `workpackage_claims/scrub_wp_ai_first_desktop_packaging_roadmap_alignment.md`

Files changed:
- `ROADMAP.md`
- `DESKTOP_PACKAGING_DECISION.md`
- `DECISION_LOG.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`

Main changes:
- Phase 9 target refined to signed setup.exe/MSI distribution around a Tauri shell and bundled PyInstaller onedir local engine.
- AI-agent planning assumption recorded: 60–70% first-cycle labor substitution and 75–90% later repetitive release automation.
- Indicative post-agent development/integration budget recorded as EUR 8,000–24,000, excluding retained independent security review and authority costs.
- Human gates retained for signing, release, security claims, UX acceptance and safety-critical semantics.

Validation:
- Documentation markers and phase gates checked by the branch governance operator.
- No product tests required because no product code or runtime changed.
- GitHub Actions: pending PR validation.
- Hugging Face sync: not functionally relevant.
- App verification: not applicable.

Intentionally not changed:
- active Phase 6 execution order;
- installer implementation authorization;
- runtime, UI, dependencies, recognizers, export, Scrub Key or reinsert behavior;
- cloud processing or telemetry behavior.

## 2026-07-28 00:52 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_REINSERT_INTEGRATION

Status: implemented; full GitHub Actions passed; final PR validation pending.

Purpose:
- Prevent a wrong, mixed or accidentally corrupted Scrub Key from restoring values before document/key binding is verified.

Files added:
- `scrub_key_binding_reinsert_status.py`
- `tests/test_scrub_key_binding_reinsert_integration.py`
- `tests/test_scrub_key_binding_reinsert_status.py`
- `tests/test_scrub_key_binding_reinsert_ui.py`
- `output/validation/mvp_scrub_key_binding_reinsert_validation.json`
- `handover/workpackages/20260728_0052_mvp_scrub_key_binding_reinsert_integration.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_reinsert_integration.md`

Files changed:
- `scrub_key_import.py`
- `scrub_key_reinsert.py`
- `scrub_key_document_reinsert.py`
- `reinsert_mode_ui.py`
- `tests/test_scrub_key_binding_model.py`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Implementation result:
- Dual-read import supports structurally valid legacy v1.0 and bound v1.1 keys.
- Binding validation runs before any local deterministic replacement.
- `bound_match` is verified; `legacy_unbound` remains compatible but explicitly unverified.
- Six frozen mismatch/corruption states fail closed with zero replacements.
- DOCX mismatch returns exact original bytes; no partial package is produced.
- Binding status, IDs, digest state and warnings are shown in existing feedback/report surfaces.
- No new source/key execution button or acknowledgement checkbox was added.

Validation:
- Normal full GitHub Actions run #1789 passed.
- Synthetic adversarial coverage spans text, TXT, DOCX body/header/footer and PDF-to-TXT.
- Human review remains required; production readiness remains false.

Intentionally not changed:
- Output filenames or MIME types.
- Supported TXT, DOCX and PDF-to-TXT boundaries.
- Legacy key migration.
- Signing/HMAC, secret storage, cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Complete final PR validation and merge, verify sync, then run `SCRUB-WP_MVP_SCRUB_KEY_BINDING_APP_VERIFY`.

---

## 2026-07-27 20:05 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION

Status: implemented; targeted validation passed; PR verification pending.

Purpose:
- Implement the frozen document/Scrub-Key binding contract as pure helpers before changing shared placeholder generation, export or reinsert behavior.

Files added:
- `scrub_key_binding.py`
- `tests/test_scrub_key_binding_model.py`
- `tests/test_scrub_key_binding_model_validation.py`
- `output/validation/mvp_scrub_key_binding_model_validation.json`
- `handover/workpackages/20260727_2005_mvp_scrub_key_binding_model_implementation.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_model_implementation.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Implementation result:
- Local document binding ID generation supports injected deterministic bytes and normal `secrets` randomness.
- Bound automatic/manual placeholder creation and parsing match the frozen grammar.
- Canonical digest output matches the fixed synthetic SHA-256 fixture.
- Bound key validation checks schema, policies, items, item bindings, duplicates and digest.
- Document/key validation implements `bound_match`, `legacy_unbound`, `binding_mismatch`, `mixed_document_bindings`, `missing_document_binding`, `invalid_mapping_digest`, `invalid_bound_key` and `legacy_key_for_bound_document`.
- Bound failures prohibit replacement; legacy compatibility remains explicitly unverified.
- Inputs remain unmodified.

Intentionally not changed:
- current generic automatic/manual placeholder generation;
- current Scrub Key builder, serializer, export or import integration;
- current reinsert execution helpers or UI;
- filenames or MIME types;
- legacy migration;
- signing/HMAC or secret storage;
- cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_EXPORT_INTEGRATION` after PR validation and merge.

---

## 2026-07-27 19:38 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS

Status: completed; contract frozen; PR validation pending.

Purpose:
- Freeze the bound-placeholder, Scrub Key metadata, mapping-digest, legacy compatibility and fail-closed validation contracts before implementing the model.

Files added:
- `SCRUB_KEY_BINDING_CONTRACT.md`
- `test_cases/mvp_phase6/scrub_key_binding_contract.json`
- `tests/test_mvp_scrub_key_binding_contracts.py`
- `tests/test_mvp_scrub_key_binding_contract_validation.py`
- `output/validation/mvp_scrub_key_binding_contract_validation.json`
- `handover/workpackages/20260727_1938_mvp_scrub_key_binding_contract_tests.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_binding_contract_tests.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Contract result:
- Binding ID grammar: `B[A-Z2-7]{16}`.
- Automatic placeholder grammar: `[LABEL_BINDINGID_INDEX]`.
- Manual placeholder grammar: `[LABEL_BINDINGID_HANDMATIG_INDEX]`.
- Proposed bound key schema: `1.1`; binding version: `1`.
- Canonical digest algorithm: SHA-256.
- Eight binding statuses; six are fail-closed with zero replacements.
- Legacy v1.0 remains explicit unbound compatibility and cannot be used for bound documents.
- Current three-step reinsert UX remains unchanged; no new source/key buttons or checkboxes.
- Product code changed: false.
- Production ready: false; human review required: true.

Intentionally not changed:
- existing product helpers;
- automatic/manual placeholder generation;
- Scrub Key build, validation, serialization or import implementation;
- export or reinsert semantics;
- UI or download behavior;
- signing/HMAC or secret storage;
- cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_MODEL_IMPLEMENTATION` after PR validation and merge.

---

## 2026-07-27 19:18 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE

Status: completed; targeted validation passed; PR verification pending.

Purpose:
- Determine the smallest safe cross-format mitigation for the critical document/Scrub-Key binding gap before changing schema, placeholders, export or reinsert behavior.

Files added:
- `MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE.md`
- `output/validation/mvp_scrub_key_document_binding_gap_triage.json`
- `output/validation/mvp_scrub_key_document_binding_gap_triage_validation.json`
- `tests/test_mvp_scrub_key_document_binding_gap_triage.py`
- `tests/test_mvp_scrub_key_document_binding_gap_triage_validation.py`
- `handover/workpackages/20260727_1918_mvp_scrub_key_document_binding_gap_triage.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_document_binding_gap_triage.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`

Triage result:
- Primary MVP threat: accidental wrong-document/key pairing.
- Secondary MVP threat: accidental key corruption.
- Deferred threat: malicious tampering requiring protected signing-key infrastructure.
- Recommended primary control: document-specific non-sensitive binding ID in all placeholders and the key.
- Recommended complementary control: canonical SHA-256 mapping digest.
- Explicitly not sufficient: document labels, filenames, content hashes, placeholder-list hashes or metadata-only binding.
- Legacy v1.0 keys require explicit unbound status and warning; they must not be silently treated as bound.
- Bound-key mismatch, mixed IDs and digest mismatch must fail closed with zero replacements.
- Human review remains required; production readiness remains false.

Intentionally not changed:
- product code or UI;
- Scrub Key schema/version or serialization;
- placeholder generation or grammar;
- export/download or reinsert semantics;
- document processing;
- cloud, AI, OCR or secret storage.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_BINDING_CONTRACT_TESTS` before implementation.

---

## 2026-07-27 18:55 Europe/Amsterdam — SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION

Status: completed; deterministic validation passed; PR verification pending.

Purpose:
- Validate Scrub Key import/reinsert and placeholder roundtrip behavior against adversarial synthetic mutations.
- Record evidence before authorizing any schema, export or reinsert changes.

Files added:
- `test_cases/mvp_phase6/scrub_key_roundtrip_manifest.json`
- `mvp_scrub_key_roundtrip_validation.py`
- `scripts/run_mvp_scrub_key_roundtrip_validation.py`
- `tests/test_mvp_scrub_key_roundtrip_validation.py`
- `tests/test_mvp_scrub_key_roundtrip_report_contract.py`
- `output/validation/mvp_scrub_key_roundtrip_validation_report.json`
- `handover/workpackages/20260727_1855_mvp_scrub_key_roundtrip_validation.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `MVP_PHASE6_EXECUTION_PLAN.md`
- `RISK_REGISTER.md`
- `DECISION_LOG.md`
- `workpackage_claims/scrub_wp_mvp_scrub_key_roundtrip_validation.md`

Validation result:
- 15 synthetic cases; 0 failed cases.
- 1 critical finding: no reliable document/key binding when a wrong valid key reuses the same placeholder namespace.
- 1 medium finding: malformed placeholder mutations outside the grammar are signalled indirectly.
- Existing duplicate, incomplete, invalid, unknown and translated cases fail closed or remain visibly auditable as expected.
- Local-only: true; external AI: false; cloud processing: false.
- Production ready: false; human review required: true.

Intentionally not changed:
- product code or UI;
- Scrub Key schema, mappings, export, storage or lifecycle;
- placeholder grammar or automatic repair;
- reinsert helper semantics;
- filenames, MIME types or audit fields;
- cloud, AI, OCR or restored-PDF behavior.

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_DOCUMENT_BINDING_GAP_TRIAGE` before implementing a fix.

---

## 2026-07-27 18:28 Europe/Amsterdam — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Purpose:
- Record successful live verification of the document-first automatic reinsert workflow.
- Close the evidence-driven UI blocker before continuing Scrub Key roundtrip validation.

Validation result:
- PR #38 merge commit: `390f381c1464883f220716655c5067dadd0bb4c9`.
- Final clean PR GitHub Actions run #1678: passed.
- Full repository suite before merge: 797 passed.
- Hugging Face deployment: confirmed by live testing of the merged three-step workflow.
- App verification: passed; coordinator reported `getest en werkend`.

Verified product boundaries:
- Document/text remains step 1, Scrub Key step 2 and restored download step 3.
- Automatic source recognition, key validation and local deterministic reinsert work as intended.
- One final confidential-output acknowledgement remains at download.
- No Scrub Key schema, helper semantics, export filenames/MIME types, cloud, AI, OCR or restored-PDF behavior changed.
- Human review remains required; no production-readiness claim is made.

Files added:
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`
- `handover/workpackages/20260727_1828_mvp_reinsert_auto_flow_simplification_app_verify_closeout.md`

Files changed:
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md`
- `handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md`

Next recommended step:
- Start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

---

## 2026-07-27 — SCRUB-WP_MVP_REINSERT_AUTO_FLOW_SIMPLIFICATION_IMPLEMENTATION

Status: implemented; full suite passed; final PR validation pending.

Purpose:

- Remove redundant source- and Scrub-Key confirmation steps from the local reinsert workflow after live Phase 6 evidence showed that uploaded inputs looked complete while hidden action gates remained.
- Present the workflow in the user’s natural order: source document/text, corresponding Scrub Key, restored result.
- Preserve a clear confidentiality decision at the final restored-output download boundary.

Files added:

- `reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow.py`
- `tests/test_reinsert_auto_flow_ui.py`
- `handover/workpackages/20260727_1706_mvp_reinsert_auto_flow_simplification_implementation.md`
- `output/validation/mvp_reinsert_auto_flow_validation.json`

Files changed:

- `reinsert_mode_ui.py`
- `tests/test_reinsert_interface_simplification_ui.py`
- `tests/test_mvp_document_fidelity_ui_copy.py`
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `ROADMAP.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md`
- `handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md`
- `workpackage_claims/scrub_wp_mvp_reinsert_auto_flow_simplification_implementation.md`

Implementation result:

- Step 1 is now the source document or pasted text.
- One uploader recognises TXT, DOCX and text-based PDF by extension.
- Step 2 automatically parses and validates the uploaded or pasted Scrub Key.
- Local deterministic reinsert runs automatically once one valid source and one valid key are present.
- Separate source/key acknowledgement checkboxes and execution buttons were removed.
- One final confidentiality acknowledgement remains directly before restored-output download.
- Existing output filenames, MIME types, reinsert helpers, audit fields and explicit DOCX/PDF boundaries are preserved.

Validation:

- Full repository suite: 797 passed.
- Helper dispatch, deterministic request signatures and input precedence are covered.
- Source-level UI contracts verify document-first order, automatic key validation, automatic local reinsert and removal of redundant gates.
- Prior DOCX live verification passed for body, table, header and footer restoration.
- Final GitHub Actions, merge, Hugging Face sync and live app verification remain pending.

Intentionally not changed:

- Scrub Key schema, mappings, lifecycle or storage;
- document replacement or reinsert helper semantics;
- recognizers or thresholds;
- export filenames, MIME types or audit semantics;
- cloud, AI or OCR processing;
- restored-PDF support;
- unsupported DOCX-part boundaries;
- the requirement for human review and a final confidential-output warning.

Next recommended step:

- Complete final PR validation, merge and sync, then live-verify the three-step automatic flow.
- Continue with `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION` after app verification.

---

## 2026-07-17 — SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING

Status: completed / ready for PR verification.

Purpose:

- Resolve the reproducible DOCX header/footer reinsert fidelity gap from the Phase 6 matrix.
- Preserve DOCX hygiene visibility and explicit unsupported-part boundaries.
- Keep the PDF restored-TXT-only/no-OCR boundary unchanged.

Files added:

- `mvp_document_fidelity_report.py`
- `scripts/run_mvp_document_hygiene_fidelity_report.py`
- `tests/test_mvp_document_hygiene_fidelity_hardening.py`
- `tests/test_mvp_document_fidelity_report.py`
- `tests/test_mvp_document_fidelity_ui_copy.py`
- `tests/test_mvp_document_fidelity_pr_final_contracts.py`
- `output/validation/mvp_phase6_document_hygiene_fidelity_hardening_report.json`
- `output/validation/mvp_document_fidelity_pr_validation.json`
- `output/validation/mvp_document_fidelity_pr_validation.log`
- `handover/workpackages/20260717_2230_mvp_document_hygiene_fidelity_hardening.md`

Files changed:

- `scrub_key_document_reinsert.py`
- `reinsert_mode_ui.py`
- `mvp_phase6_document_cases.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_document_hygiene_fidelity_hardening.md`

Implementation result:

- DOCX body paragraphs and tables remain supported.
- `word/header*.xml` and `word/footer*.xml` text nodes are restored deterministically.
- The DOCX reinsert capability copy matches the supported body/table/header/footer scope.
- The synthetic header/footer residual-placeholder finding is resolved: `true`.
- Resolved findings: 1.
- Remaining findings: 1.
- The remaining finding is the explicit PDF restored-TXT-only/no-OCR product boundary.

Intentionally not changed:

- recognizers, thresholds or replacement semantics;
- Scrub Key schema or lifecycle;
- DOCX comments, tracked-change-only parts, footnotes/endnotes, text boxes or metadata;
- split-placeholder support across Word text nodes;
- export filenames or MIME types;
- restored PDF or OCR support;
- Streamlit controls/flow, runtime or dependencies; only capability copy was aligned.

Next recommended step:

- After Actions, sync and app verification, start `SCRUB-WP_MVP_SCRUB_KEY_ROUNDTRIP_VALIDATION`.

---

## 2026-07-17 — Hugging Face Space runtime incident recovery and sync-churn guard

Status: completed and app-verified.

Purpose:

- Restore the Hugging Face Space after it entered an error/rebuild state.
- Diagnose the incident without exposing secrets or changing product behavior.
- Prevent clearly non-runtime-only commits from repeatedly rebuilding the live Space.

Result:

- Sanitized runtime evidence observed the Space first at `BUILDING` and subsequently at `RUNNING`.
- Streamlit started on port 7860 and the Flair model loaded.
- The coordinator confirmed that the application opens again.
- PR #35 added a conservative deployment `paths-ignore` guard while preserving runtime-relevant deployments and manual dispatch.
- Temporary incident recovery/probe workflows and triggers were removed after verification.

Intentionally not changed:

- product code or UI;
- recognizers, thresholds or replacement semantics;
- export, Scrub Key or reinsert semantics;
- dependencies, Dockerfile, hardware or Hugging Face configuration;
- privacy and human-review controls.

Next recommended step:

- Resume PR #33 and the Phase 6 document-fidelity sequence.

---

## 2026-07-17 — SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE

Status: completed / ready for PR verification.

Purpose:

- Classify every evidence gap from the first Phase 6 synthetic validation report.
- Decide whether the evidence justifies recognizer or threshold changes.
- Route document-fidelity and product-boundary findings to the correct next package.

Files added:

- `MVP_PHASE6_FALSE_NEGATIVE_GAP_TRIAGE.md`
- `output/validation/mvp_phase6_false_negative_gap_triage.json`
- `tests/test_mvp_phase6_false_negative_gap_triage.py`
- `handover/workpackages/20260717_2208_mvp_false_negative_gap_triage.md`

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_false_negative_gap_triage.md`

Triage result:

- Input evidence gaps: 2.
- Reproducible detection false negatives: 0.
- Misclassifications: 0.
- Legal-role over-masking findings: 0.
- Recognizer fix required: `false`.
- Next package: `SCRUB-WP_MVP_DOCUMENT_HYGIENE_FIDELITY_HARDENING`.

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

## 2026-07-17 — SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX

Status: completed / ready for PR verification.

Purpose:

- Establish a repeatable synthetic evidence baseline for the supported MVP workflow.
- Exercise TXT, DOCX and text-based PDF paths across import, review-row replacement, manual addition, Scrub Key creation/validation, deterministic reinsert, export representations and audit evidence.
- Record known limitations and reproducible gaps without weakening tests or making production-readiness claims.

Files added:

- `test_cases/mvp_phase6/validation_manifest.json`
- `mvp_phase6_validation_manifest.py`
- `mvp_phase6_detection_matrix.py`
- `mvp_phase6_workflow_core.py`
- `mvp_phase6_document_cases.py`
- `mvp_phase6_validation_report.py`
- `scripts/run_mvp_phase6_validation_matrix.py`
- `tests/test_mvp_phase6_e2e_synthetic_validation_matrix.py`
- `output/validation/mvp_phase6_synthetic_validation_report.json`
- `handover/workpackages/20260717_2020_mvp_e2e_synthetic_validation_matrix.md`

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_e2e_synthetic_validation_matrix.md`

Validation result:

- Synthetic cases: 3.
- Failing cases: 0.
- Evidence gaps/known limitations: 2.
- Gap categories: known_docx_reinsert_limitation, known_pdf_reinsert_limitation.
- Human review required: `true`.
- Production ready: `false`.
- Local-only validation: `true`.
- External AI/cloud/OCR processing: none.

Methodology correction:

- Standard deterministic Presidio email recognition is included alongside the Dutch recognizer pack, preventing a standard e-mail value from being misclassified as a Dutch-pack false negative.

Intentionally not changed:

- Streamlit UI or review controls;
- recognizers or detection thresholds in product code;
- replacement semantics;
- export payload, filename or MIME semantics;
- Scrub Key schema or lifecycle behavior;
- reinsert semantics;
- document-processing implementation;
- runtime/startup or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_FALSE_NEGATIVE_GAP_TRIAGE` and classify the report evidence before implementing any fix.

---

## 2026-07-17 — SCRUB-WP_MVP_PHASE6_ROADMAP_REALIGNMENT

Status: completed / ready for PR verification.

Purpose:

- Realign the central roadmap after completion and live verification of the MVP UI simplification line.
- Make Phase 6 end-to-end workflow validation and trust hardening the active development line.
- Define an ordered evidence-driven workpackage queue before pilot or packaging work resumes.

Files changed:

- `ROADMAP.md`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `DECISION_LOG.md`
- `RISK_REGISTER.md`
- `workpackage_claims/scrub_wp_mvp_phase6_roadmap_realignment.md`

Files added:

- `MVP_PHASE6_EXECUTION_PLAN.md`
- `handover/workpackages/20260717_2012_mvp_phase6_roadmap_realignment.md`

Main changes:

- The verified UI baseline is no longer the active development focus.
- Phase 6 starts with a synthetic end-to-end validation matrix.
- False-negative, document-hygiene, Scrub Key/roundtrip and audit work must be driven by reproducible evidence.
- Phase 7 pilots and local packaging remain gated.

Validation status:

- Documentation-only package.
- GitHub Actions pending after PR.
- Hugging Face functional sync not applicable.
- App verification not applicable.

Intentionally not changed:

- product code or tests;
- UI behavior;
- recognizers or replacement semantics;
- export payloads, filenames or MIME types;
- Scrub Key JSON or reinsert behavior;
- document processing, runtime/startup or dependencies.

Next recommended step:

- Start `SCRUB-WP_MVP_E2E_SYNTHETIC_VALIDATION_MATRIX` after this realignment is merged.

---

## 2026-07-16 — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Purpose:

- Record live Hugging Face app verification after PR #28 merged.
- Close the manual correction panel density simplification line.
- Confirm the compact layout preserves the existing manual correction workflow.

Verification evidence:

- Coordinator live app screenshot reviewed at 2026-07-16 23:43 Europe/Amsterdam.
- `Gemiste waarde toevoegen` remains collapsed by default and opens without a duplicate internal heading.
- The value, type and replacement controls appear in one compact row.
- The full-width `Toevoegen aan vervangtabel` action remains visible.
- Synthetic value `lantaarnbloem` was added successfully.
- The replacement table shows `lantaarnbloem` with `[WAARDE_HANDMATIG_01]` and status `Handmatig toegevoegd`.
- No Script execution error is visible.
- The live screenshot confirms GitHub-to-Hugging-Face deployment of the merged UI.

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_implementation.md`
- `handover/workpackages/20260716_2040_manual_correction_panel_density_implementation.md`

Files added:

- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_app_verify_closeout.md`
- `handover/workpackages/20260716_2343_manual_correction_panel_density_app_verify_closeout.md`

Intentionally not changed:

- product code or tests;
- recognizer or replacement semantics;
- validation or session-state behavior;
- export payloads, filenames or MIME types;
- Scrub Key JSON or reinsert behavior;
- document processing, startup/runtime or dependencies.

Next recommended step:

- Use the simplified MVP UI with representative synthetic legal documents before approving another UI package.

---

## 2026-07-16 — SCRUB-WP_MANUAL_CORRECTION_PANEL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented; local validation passed.

Purpose:

- Make the existing `Gemiste waarde toevoegen` panel materially shorter and less form-like.
- Remove the duplicate internal heading and group value, type and replacement controls in one compact row.
- Preserve the existing validation, session-state and replacement-table workflow.

Files changed:

- `presidio_streamlit.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_manual_correction_panel_density_simplification_implementation.md`

Files added:

- `tests/test_manual_correction_panel_density_implementation.py`
- `handover/workpackages/20260716_2040_manual_correction_panel_density_implementation.md`

Validation status:

- Required worker validation passed.
- GitHub Actions pending after PR update.
- Hugging Face sync pending after merge.
- Live app verification required because visible UI behavior changed.

Intentionally not changed:

- validation rules or duplicate detection;
- placeholder generation or entity types;
- replacement-row structure or replacement semantics;
- export payloads, filenames or MIME types;
- Scrub Key JSON or warning behavior;
- reinsert behavior;
- recognizers, thresholds, document processing, runtime/startup or dependencies.

Next recommended step:

- Verify PR Actions, merge when green, verify Hugging Face sync and request live app verification.

---

## 2026-07-05 — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_APP_VERIFY_CLOSEOUT

Status: completed and app-verified.

Purpose:

- Record live app verification for `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION`.
- Close the Review/Export vertical-density implementation line after PR #26 merge and live Hugging Face verification.
- Add concise closeout notes for the related plan and contract-test packages that were previously missing from `CHANGELOG.md`.

Verification evidence:

- Coordinator live Hugging Face screenshot reviewed.
- The app starts without Script execution error.
- The input section remains coherent.
- `2. Controleer resultaat` remains visible.
- Basiscontrole / Expertcontrole remain visible.
- `Markeringen tonen` and side-by-side review remain visible.
- `Gemiste waarde toevoegen` and the vervangtabel remain accessible.
- `3. Exporteer resultaat` remains visible.
- TXT/DOCX/PDF downloads are visible in a compact row.
- Scrub Key, audit/technical files and DOCX hygiene audit remain separate and accessible.

Files changed:

- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_implementation.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_app_verify_closeout.md`
- `handover/workpackages/20260705_2213_review_export_vertical_density_implementation.md`
- `handover/workpackages/20260705_2242_review_export_vertical_density_app_verify_closeout.md`

Intentionally not changed:

- product code;
- tests;
- recognizer logic;
- replacement logic;
- export payloads;
- download filenames;
- MIME types;
- Scrub Key JSON;
- reinsert behavior;
- startup/runtime behavior.

Related package closeout:

- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_PLAN` — completed and merged; planning-only.
- `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_CONTRACT_TESTS` — completed and merged; source-level guardrails only.

Next recommended step:

- Decide whether the current MVP UI is good enough for this pass, or start a new separately approved small UI package.

---

## 2026-07-05 — SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Purpose:

- Reduce vertical density in the Review and Export areas after plan and contract-test packages were merged.
- Compress repeated Review helper copy while keeping side-by-side review, marker toggle, manual missed-value entry and replacement table accessible.
- Put the three primary document downloads in a compact three-column layout.
- Keep Scrub Key, audit/technical files and DOCX hygiene audit separate and accessible.

Files changed:

- `presidio_streamlit.py`
- `side_by_side_review_panel_ui.py`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `workpackage_claims/scrub_wp_review_export_vertical_density_simplification_implementation.md`

Files added:

- `handover/workpackages/20260705_2213_review_export_vertical_density_implementation.md`

Validation status:

- Local validation passed.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after sync because visible UI behavior changed.

Intentionally not changed:

- recognizer logic;
- replacement logic;
- review table semantics;
- export payloads;
- download filenames;
- MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- DOCX/PDF parsing;
- startup/runtime behavior;
- dependencies;
- benchmark or recall logic.

Next recommended step:

- Open PR, verify GitHub Actions, merge when green, verify Hugging Face sync, then request live app verification.

---

## 2026-07-05 — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: implemented / local validation passed.

Purpose:

- Resume the duplicate input surface implementation after the connector-only worker was blocked.
- Keep one visible `1. Voeg document of tekst toe` step and group upload, synthetic example selection and pasted/extracted text into one input surface.
- Preserve TXT/DOCX/PDF upload support, synthetic legal examples, pasted/extracted text handling and input precedence.
- Preserve review, export/download, Scrub Key, reinsert, audit and DOCX hygiene behavior.

Files changed:

- `presidio_streamlit.py`
- `tests/test_duplicate_input_surface_simplification_contracts.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_implementation.md`

Files added:

- `handover/workpackages/20260705_0113_duplicate_input_surface_implementation.md`

Validation status:

- Local validation passed:
  - `python -m pytest -q tests/test_duplicate_input_surface_simplification_contracts.py`
  - related UI/export guardrail tests
  - `git diff --check`
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after merge/sync because visible UI grouping changed.

Intentionally not changed:

- document parsing behavior;
- upload backend;
- recognizer logic;
- replacement logic;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- reinsert behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Open PR, verify GitHub Actions, merge when green, verify Hugging Face sync, and request live app verification.

---

## 2026-07-04 — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS

Status: completed / PR validation pending.

Purpose:

- Lock the single-input-surface contract before the duplicate input implementation touches `presidio_streamlit.py`.
- Preserve existing TXT/DOCX/PDF upload support, synthetic legal example support, pasted/extracted text handling and input precedence.
- Preserve review, replacement table, Scrub Key, export/download, audit and DOCX hygiene surfaces.
- Block duplicate-input runtime/startup patching and prohibited scope expansion.

Files added:

- `tests/test_duplicate_input_surface_simplification_contracts.py`
- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_contract_tests.md`
- `handover/workpackages/20260704_2318_duplicate_input_surface_contract_tests.md`

Files changed:

- `WORKPACKAGES.md`
- `CHANGELOG.md`

Validation status:

- Source-level contract tests added.
- GitHub Actions pending after PR.
- Hugging Face sync not applicable until merge.
- App verification not applicable because this package changes no UI behavior.

Intentionally not changed:

- product implementation code;
- Streamlit UI behavior;
- document ingestion behavior;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Review PR validation.
- If green, merge this contract-test package.
- Then start `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION` as the next narrow implementation package.

---

## 2026-07-03 — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION

Status: implemented / PR validation pending.

Purpose:

- Make the secondary review controls under `2. Controleer resultaat` calmer and easier to understand.
- Add a clear `Meer controleopties` grouping cue below the side-by-side review without introducing nested Streamlit expanders.
- Preserve side-by-side review, manual missed-value entry, replacement table, serial review, Scrub Key, export/download, audit and DOCX hygiene controls.

Files changed:

- `side_by_side_review_panel_ui.py`
- `RELEASE_NOTES.md`
- `CHANGELOG.md`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish_implementation.md`

Files added:

- `tests/test_secondary_control_grouping_polish_implementation.py`
- `handover/workpackages/20260703_0000_secondary_control_grouping_polish_implementation.md`

Validation status:

- Source-level implementation tests added.
- GitHub Actions pending after PR.
- Hugging Face sync pending after merge.
- App verification required after merge/sync because visible UI behavior changed.

Intentionally not changed:

- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Review PR validation.
- If green, merge and verify Hugging Face sync.
- Then request coordinator live app verification for the new `Meer controleopties` grouping cue.

---

## 2026-07-03 — SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH

Status: implemented planning/contract-tests-only; PR validation pending.

Purpose:

- Prepare the final small UI-polish step for calmer grouping of secondary review controls.
- Avoid nested Streamlit expanders before touching `presidio_streamlit.py`.
- Preserve side-by-side review, manual missed-value entry, replacement table, serial review, Scrub Key, export/download, audit and DOCX hygiene controls.

Files added:

- `SECONDARY_CONTROL_GROUPING_POLISH_PLAN.md`
- `tests/test_secondary_control_grouping_polish_contracts.py`
- `workpackage_claims/scrub_wp_secondary_control_grouping_polish.md`
- `handover/workpackages/20260703_0000_secondary_control_grouping_polish.md`

Validation status:

- Source-level contract tests added.
- GitHub Actions pending after PR.
- Hugging Face sync not applicable until merge.
- App verification not applicable because no UI behavior changed in this planning/contract step.

Intentionally not changed:

- product code;
- Streamlit UI;
- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Run PR validation for the contract tests.
- If green, merge this plan/contract package.
- Then start `SCRUB-WP_SECONDARY_CONTROL_GROUPING_POLISH_IMPLEMENTATION` as the actual narrow UI implementation.

---

## 2026-07-03 — SCRUB-WP_REVIEW_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Status: completed and app-verified.

Purpose:

- Make the side-by-side review surface calmer and less form-like.
- Keep the source-vs-processed comparison central while pointing users toward the safe download step.
- Preserve review table, manual missed-value entry, serial review, Scrub Key, export/download and audit controls.

Files changed:

- `side_by_side_review_panel_ui.py`
- `tests/test_review_copy_polish_ui.py`
- `tests/test_side_by_side_review_consolidation_dutch_sample.py`
- `tests/test_side_by_side_review_ui_patch.py`
- `WORKPACKAGES.md`
- `RELEASE_NOTES.md`
- `workpackage_claims/scrub_wp_review_surface_simplification_implementation.md`

Files added:

- `tests/test_review_surface_simplification_implementation.py`
- `handover/workpackages/20260703_0000_review_surface_simplification_implementation.md`

Validation status:

- Source-level implementation tests added.
- Related copy-polish and side-by-side tests updated.
- PR #12 initially failed on stale copy expectations; a narrow test-expectation fix was applied.
- PR #12 Tests passed after the narrow fix.
- PR #12 merged to `main`.
- Main Tests for commit `41cf304` passed.
- GitHub to Hugging Face sync for commit `41cf304` passed.
- App verification passed by coordinator screenshot.

Intentionally not changed:

- replacement logic;
- review table data semantics;
- export content;
- download filenames;
- download MIME types;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark logic;
- DOCX/PDF parsing behavior;
- runtime/startup behavior;
- dependencies.

Next recommended step:

- Do not start broader UI/reinsert/export work without a dedicated workpackage.
- Decide whether further secondary-control grouping is desired as a separate small package, or return to recall/benchmark follow-up if product UI is good enough for the current MVP pass.

---

## 2026-06-23 20:52 Europe/Amsterdam — Full-suite validation update — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

## 2026-06-23 — SCRUB-WP_DOCX_SIDE_BY_SIDE_TEXT_ORDER_TRIAGE

- Fixed DOCX plain-text extraction order for side-by-side preview.
- DOCX body paragraphs and tables are now read in document XML order instead of all paragraphs first and all tables afterwards.
- Added synthetic regression coverage for interleaved paragraph/table order.
- Preserved DOCX export, Scrub Key and reinsert semantics.
- Validation: `python -m pytest tests -x -vv` → 649 passed in 102.51s.

- Full suite passed: `python -m pytest tests -x -vv` → 647 passed in 108.30s.
- `git diff --check` passed.
- Local implementation validation complete.
- GitHub Actions, GitHub to Hugging Face sync and live app verification remain pending until PR/merge/sync.

## 2026-06-23 20:43 Europe/Amsterdam — SCRUB-WP_REINSERT_INTERFACE_SIMPLIFICATION_IMPLEMENTATION

- Implemented direct-source reinsert interface simplification.
- Added `reinsert_mode_ui.py` with the visible four-step reinsert flow:
  1. Voeg Scrub Key toe
  2. Voeg tekst of document toe
  3. Controleer herstelrapport
  4. Download herstelde output
- Added a minimal direct hook in `presidio_streamlit.py`.
- Added a no-op guard to `fix_streamlit_pdf_text_reinsert.py` so startup does not mutate the direct-source reinsert UI.
- Preserved Scrub Key warnings, acknowledgement gates, restored download filenames, MIME types and local-only/no-AI/no-cloud/no-OCR/no-restored-PDF boundaries.
- Added `tests/test_reinsert_interface_simplification_ui.py`.

Validation so far:
- `tests/test_reinsert_interface_simplification_ui.py`: 8 passed
- reinsert patch tests: 39 passed
- warning/two-mode UI tests: 23 passed


# Changelog — SolidPrivacy Scrub

## SCRUB-WP_EXECUTION_INTERFACE_SIMPLIFICATION_IMPLEMENTATION_RESTART — Execution interface simplification

Status: completed and verified on `main` via PR #6 (`a34700c`).

Summary:

- Simplified the default Scrub flow toward `1. Voeg document of tekst toe`, `2. Controleer resultaat`, `3. Exporteer resultaat`.
- Edited `presidio_streamlit.py` directly; no startup patch, runtime hook, sitecustomize hook or Dockerfile startup change was added.
- Collapsed secondary controls by default while keeping them available:
  - control-mode explanation;
  - recognition details;
  - review guidance;
  - manual missed-value entry;
  - focus filter / extra control helpers;
  - candidate audit values;
  - replacement table;
  - technical replacement details;
  - step-by-step review;
  - reusable replacements;
  - Scrub Key download;
  - audit/technical downloads.
- Kept side-by-side review visible as the main review surface.
- Kept the replacement table as source of truth and export input.
- Kept primary document downloads visible.

Tests:

- `tests/test_execution_interface_simplification_ui.py` — 6 passed.
- Side-by-side, serial review and replace logic UI tests — 37 passed.
- Export/download contract and implementation tests — 19 passed.
- `git diff --check` — passed.
- Full local test suite — 639 passed.
- PR #6 checks — green.
- Main Tests — green.
- GitHub to Hugging Face sync — green.
- Live app verification — passed by coordinator screenshot on 2026-06-23.

Intentionally not changed:

- export semantics;
- download file contents;
- download filenames;
- Scrub Key JSON semantics;
- Scrub Key warning meaning;
- reinsert behavior;
- recognizer logic;
- benchmark thresholds;
- document processing behavior;
- cloud processing;
- local packaging;
- Dockerfile startup behavior;
- runtime mutation behavior;
