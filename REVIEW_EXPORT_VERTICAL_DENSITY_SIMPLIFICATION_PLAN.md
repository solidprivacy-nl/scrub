# Review / Export vertical density simplification plan

Workpackage: `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_PLAN`

Repository: `solidprivacy-nl/scrub`

Status: planning-only / ready for contract tests

## 1. Current observed Review/Export density problem

After `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION`, the primary Anonimiseren flow is now conceptually correct and visually clearer:

```text
1. Voeg document of tekst toe
2. Controleer resultaat
3. Exporteer resultaat
```

Live verification showed that the duplicate input surface is resolved. The remaining issue is vertical density in `2. Controleer resultaat` and `3. Exporteer resultaat`. The page is safer and more coherent than before, but still feels tall and form-like because several explanatory captions, controls, collapsed detail sections and download controls are stacked vertically.

### 1.1 Review density in `2. Controleer resultaat`

Current Review density comes from a useful but still tall sequence:

- section intro copy under `2. Controleer resultaat`;
- `Controleweergave` with `Basiscontrole` / `Expertcontrole` radio;
- helper copy under the radio;
- `Markeringen tonen` near the side-by-side review;
- side-by-side `Brontekst` / `Verwerkte tekst` review panels;
- explanatory copy below the panels;
- `Meer controleopties` heading and supporting copy;
- `Gemiste waarde toevoegen` collapsed control;
- `Details aanpassen — vervangtabel` collapsed control;
- replacement count/status alert.

Each element has a safety purpose, but the cumulative vertical stack can make the page feel heavier than the intended MVP workflow. The aim is not to remove controls, but to make the hierarchy clearer and reduce repeated explanation.

### 1.2 Export density in `3. Exporteer resultaat`

Current Export density comes from:

- explanatory copy under `3. Exporteer resultaat`;
- `Document downloaden` label;
- three stacked primary download buttons;
- `Scrub Key downloaden` accordion;
- `Audit en technische bestanden` accordion;
- `DOCX hygiene audit` accordion.

The current separation between normal document downloads, Scrub Key and audit files is important. The density issue should therefore be solved through compact grouping and copy compression, not by merging output types or changing export semantics.

## 2. Product goal

Make Review and Export feel calmer, shorter and less form-like while preserving the full safety model.

The user must still be able to:

- compare original and processed text;
- toggle visual markings;
- add missed values;
- inspect and edit the replacement table;
- access Scrub Key export and its warning context;
- access audit and technical files;
- access DOCX hygiene audit;
- export the same outputs with unchanged payloads, filenames and MIME types.

The final user-facing flow should remain:

```text
1. Voeg document of tekst toe
2. Controleer resultaat
3. Exporteer resultaat
```

The Review step remains the main safety step. The Export step remains a download step, not a new decision gate.

## 3. Non-goals

This planning package and the next implementation line must explicitly exclude:

- recognizer changes;
- replacement logic changes;
- review table semantics changes;
- export content changes;
- download filename changes;
- MIME type changes;
- Scrub Key JSON changes;
- reinsert behavior changes;
- DOCX/PDF parsing changes;
- runtime/startup patching;
- custom HTML components;
- synchronized scrolling changes;
- full document editor;
- cloud document processing;
- AI document processing;
- hiding safety controls entirely.

No product code is changed by this plan.

## 4. Risk analysis

This UX line sits directly on the safety boundary between a calmer interface and a reliable privacy review workflow.

### R1 — Controls become too hidden

If the simplification hides controls too aggressively, users may miss the manual correction path or the replacement table. This would weaken the mitigation for missed sensitive data.

Mitigation:

- keep `2. Controleer resultaat` visible;
- keep side-by-side review visible by default;
- keep `Markeringen tonen` visible;
- keep `Gemiste waarde toevoegen` and `Details aanpassen — vervangtabel` accessible in the primary Review area;
- contract-test all control labels before implementation.

### R2 — Review reliability weakens

The review table remains source of truth and fallback. Basiscontrole / Expertcontrole must stay a visibility and density choice only. It must not change recognizer behavior, replacement logic, export output, Scrub Key JSON, reinsert behavior or audit generation.

Mitigation:

- do not change review table data model or editor key;
- keep `Details aanpassen — vervangtabel` available;
- keep the replacement count/status understandable;
- make implementation source-level and bounded.

### R3 — Missed-value control becomes less discoverable

`Gemiste waarde toevoegen` directly mitigates false negatives by allowing a user-supplied value to enter the existing replacement table before export. Hiding it too deeply would make the UI simpler but less safe.

Mitigation:

- keep the control in the Review step;
- allow copy compression, not removal;
- test for the visible label and manual-mask helper wiring.

### R4 — Scrub Key warning context becomes too weak

The Scrub Key can restore original values. Export density work must not make it look like a normal document download.

Mitigation:

- keep Scrub Key separated from normal TXT/DOCX/PDF downloads;
- preserve warning copy;
- do not change JSON structure, file name, MIME type or acknowledgement semantics.

### R5 — Export semantics accidentally change

A compact export layout could accidentally alter payloads, filenames, MIME types or eligibility.

Mitigation:

- contract-test all primary download labels and filenames/MIME types before implementation;
- implementation should only regroup visible controls;
- no bundle/zip export or combined export package.

### R6 — Nested Streamlit expander issues return

Earlier UI work has been careful around nested expanders and startup patches. A density pass could reintroduce nested Streamlit behavior problems.

Mitigation:

- avoid nested expanders;
- avoid runtime/startup patching;
- use direct source only;
- prefer shallow grouped controls and shorter copy.

### R7 — Simpler appearance reduces safety clarity

A minimal UI can be less trustworthy if users cannot see how to review, correct and audit. The product should feel calmer, not opaque.

Mitigation:

- keep safety-critical labels visible;
- keep audit surfaces accessible as secondary layers;
- use concise status copy instead of removing status copy entirely.

## 5. Recommended UX strategy

Use a conservative, safety-preserving simplification.

Recommended direction:

A. Keep `2. Controleer resultaat` visible as the main safety step.

B. Reduce repeated explanatory copy under the review section.

C. Keep `Basiscontrole` / `Expertcontrole` visible, but shorten supporting text.

D. Keep `Markeringen tonen` visible near the side-by-side review.

E. Keep side-by-side review visible by default.

F. Keep `Meer controleopties`, but make the copy more compact.

G. Keep `Gemiste waarde toevoegen` and `Details aanpassen — vervangtabel` as compact collapsed controls.

H. Consider replacing the replacement-count blue alert with a shorter status line only if safety clarity remains equal. Do not remove the replacement count entirely.

I. In Export, consider a compact `Document downloaden` grouping for the three primary downloads. A row or column layout may reduce vertical height, but must not change payload, filenames or MIME types.

J. Keep `Scrub Key downloaden`, `Audit en technische bestanden` and `DOCX hygiene audit` accessible as secondary collapsed sections.

K. Avoid nested expanders and startup patches.

## 6. Implementation options

### Option A — Copy compression only

Description:

- reduce explanatory captions in Review and Export;
- keep layout structure mostly unchanged;
- preserve all controls in current positions.

Benefits:

- lowest risk;
- easy to review;
- minimal chance of changing behavior.

Costs:

- only modest vertical gain;
- download buttons and review controls still stack in roughly the same way;
- may not fully solve the form-like feel.

Risk profile: low.

### Option B — Compact grouped controls

Description:

- compress repeated Review copy;
- keep main side-by-side review visible;
- keep secondary Review controls grouped more tightly;
- group primary document downloads more compactly;
- leave Scrub Key, audit/technical files and DOCX hygiene audit as secondary collapsed sections;
- preserve all semantics and labels.

Benefits:

- best balance between visible simplification and safety;
- addresses both Review and Export height;
- keeps controls findable;
- fits the current MVP direction.

Costs:

- slightly higher risk than copy-only because layout changes can affect perceived hierarchy;
- needs source-level contract tests first.

Risk profile: moderate but manageable.

Recommendation: **Option B**.

### Option C — More aggressive tab/accordion restructuring

Description:

- move Review and/or Export controls into additional tabs or accordions;
- make the default page shorter by hiding larger sets of controls.

Benefits:

- largest potential vertical reduction;
- visually clean default surface.

Costs:

- higher risk of hiding safety controls too much;
- can make users miss manual correction, replacement table or audit tools;
- adds state complexity;
- can reintroduce nested expander problems;
- may conflict with the accepted direction that the side-by-side review remains the main review surface and the replacement table remains source of truth.

Risk profile: high.

Recommendation: not recommended unless screenshots after Options A/B prove the interface is still too dense.

## 7. Proposed next workpackages

### 7.1 `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_CONTRACT_TESTS`

Purpose:

- lock Review and Export safety controls before implementation;
- ensure simplification cannot accidentally remove review, correction, Scrub Key, audit or export surfaces.

Suggested test file:

```text
tests/test_review_export_vertical_density_contracts.py
```

Contracts should assert that source still contains:

- `st.subheader("2. Controleer resultaat")`;
- `st.subheader("3. Exporteer resultaat")`;
- `Basiscontrole`;
- `Expertcontrole`;
- `Markeringen tonen`;
- `render_side_by_side_review_panel`;
- `Gemiste waarde toevoegen`;
- `Details aanpassen — vervangtabel`;
- `Document downloaden`;
- `Download opgeschoonde tekst (.txt)`;
- `Download opgeschoond Word-bestand (.docx)`;
- `Download opgeschoonde PDF (.pdf)`;
- `Scrub Key downloaden`;
- `Audit en technische bestanden`;
- `DOCX hygiene audit`;
- `render_docx_hygiene_audit_panel`.

Contracts should also assert no prohibited markers are introduced:

- `cloud processing`;
- `AI document processing`;
- `new recognizers`;
- `new export gates`;
- `custom HTML component`;
- `synchronized scrolling` as a newly exposed/product-added control;
- `runtime source mutation`.

The test should remain source-level only and should not import Streamlit or `presidio_streamlit`.

### 7.2 `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_IMPLEMENTATION`

Purpose:

- implement Option B narrowly;
- compress repeated copy and group Review/Export controls more compactly;
- preserve Review, manual missed-value entry, replacement table, Scrub Key, audit and download semantics.

Primary possible files:

- `presidio_streamlit.py`;
- `side_by_side_review_panel_ui.py` only if strictly needed.

Boundaries:

- avoid parallel edits to review table/export flow;
- no runtime/startup patches;
- no export payload, filename or MIME changes;
- no Scrub Key or reinsert behavior changes.

### 7.3 `SCRUB-WP_REVIEW_EXPORT_VERTICAL_DENSITY_SIMPLIFICATION_APP_VERIFY`

Purpose:

- verify live app after GitHub Actions and Hugging Face sync are green;
- confirm the calmer Review/Export flow in the deployed Space.

## 8. Manual app verification checklist

After implementation, verify:

- App starts without Script execution error.
- One coherent input section remains.
- `2. Controleer resultaat` remains visible.
- `Basiscontrole` and `Expertcontrole` remain visible and selectable.
- `Markeringen tonen` remains visible.
- Side-by-side review remains visible.
- `Gemiste waarde toevoegen` remains accessible.
- `Vervangtabel` remains accessible.
- Replacement count/status remains understandable.
- `3. Exporteer resultaat` remains visible.
- TXT/DOCX/PDF downloads remain visible and functional.
- Scrub Key remains accessible.
- Audit and technical files remain accessible.
- DOCX hygiene audit remains accessible.
- No export filenames, MIME types or payloads changed.
- No Scrub Key or reinsert behavior changed.

## 9. Acceptance criteria for this planning package

This planning package is complete when:

- this plan exists;
- no product code, tests or runtime files are changed;
- `CHANGELOG.md` records the planning package;
- `WORKPACKAGES.md` points to the contract-test package as next step;
- the claim is completed;
- a handover is written;
- `git diff --check` equivalent review shows no obvious whitespace problems;
- PR validation is green.
