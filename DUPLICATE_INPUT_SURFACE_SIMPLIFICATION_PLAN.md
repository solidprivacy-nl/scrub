# Duplicate input surface simplification plan

Workpackage: `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_PLAN`

Repository: `solidprivacy-nl/scrub`

Status: planning-only / ready for contract tests

## 1. Problem statement

After `SCRUB-WP_BASIC_MODE_DECLUTTER_IMPLEMENTATION`, the review area is calmer, but live app verification still showed two visible `1. Voeg document of tekst toe` upload/input surfaces before the review step. This makes the default flow feel repetitive and less premium before the user reaches `2. Controleer resultaat`.

The desired MVP flow remains:

```text
1. Voeg document of tekst toe
2. Controleer resultaat
3. Exporteer resultaat
```

The next implementation should keep a single coherent input area before review while preserving all existing document ingestion and text-selection behavior.

## 2. Current observed UI issue

Coordinator screenshots after the basic/expert review declutter closeout show:

- the app starts without Script execution error;
- `Basiscontrole` is selected by default;
- the review area is visibly cleaner;
- before the review area, `1. Voeg document of tekst toe` appears twice;
- the first occurrence shows an upload widget only;
- the second occurrence shows the upload/example/text-area flow that is actually used for the anonymization input.

The duplicate visual surface increases cognitive load without adding a new safety control.

## 3. Current source locations in `presidio_streamlit.py`

Current `main` source has one direct static input heading in `presidio_streamlit.py`:

```python
st.subheader("1. Voeg document of tekst toe")
uploaded_file = st.file_uploader(
    "Upload een .txt-, .docx- of tekstgebaseerd .pdf-bestand",
    type=["txt", "docx", "pdf"],
    help="Gebruik in deze publieke prototypeomgeving alleen synthetische of goedgekeurde testdocumenten.",
)
```

The same source section then sets the downstream text-selection state:

```python
uploaded_file_type = None
input_text = "".join(demo_text)
```

For Dutch Legal Strict, the synthetic legal example UI is rendered inside the same source path:

```python
with st.expander("Gebruik een synthetisch juridisch testvoorbeeld", expanded=False):
    sample_name = st.selectbox(...)
    if sample_name != "Geen testvoorbeeld laden" and uploaded_file is None:
        input_text = example_text
```

Uploaded files then override the example/default text:

```python
if uploaded_file is not None:
    input_text, uploaded_file_type = uploaded_file_to_text(uploaded_file)
```

The final editable input text area remains:

```python
st_text = st.text_area(
    label="Plak tekst of controleer de uit het document gehaalde tekst",
    value=input_text,
    height=240,
    key="text_input",
)
```

This means the source already contains the right conceptual flow, but the live UI evidence still shows duplicate visible input presentation. The next implementation should first confirm whether the duplicate comes from:

- a remaining direct-source heading/widget duplication after the current branch is pulled;
- stale or runtime-mutated Space state;
- a startup compatibility patch still mutating `presidio_streamlit.py` in the Hugging Face runtime;
- Streamlit rendering/state interaction around file uploader plus example/text area;
- an older local branch or Space cache running a prior version.

## 4. Product target

Target the simplest visible flow:

```text
1. Voeg document of tekst toe
   - Upload TXT/DOCX/text-based PDF
   - Optional synthetic legal example
   - Paste/edit extracted text

2. Controleer resultaat
   - Side-by-side review
   - Basiscontrole / Expertcontrole
   - Existing correction and review controls

3. Exporteer resultaat
   - Primary document downloads
   - Scrub Key
   - Audit and DOCX hygiene
```

The user should see one input step, not two similar upload areas.

## 5. Non-goals

This line explicitly excludes:

- new OCR;
- PDF-to-DOCX reconstruction;
- cloud processing;
- AI document processing;
- a new upload backend;
- new recognizers;
- new export gates;
- full visual redesign;
- changes to `Basiscontrole` / `Expertcontrole` behavior;
- changes to Scrub Key or reinsert;
- changed export filenames, MIME types or payloads;
- changed document parsing behavior;
- runtime/startup patch rewrites.

## 6. Safety boundaries

The implementation must not change:

- document parsing behavior;
- TXT upload behavior;
- DOCX upload behavior;
- PDF text extraction behavior;
- synthetic legal example behavior;
- manual pasted-text behavior;
- recognizer logic;
- replacement logic;
- review table semantics;
- export behavior;
- download filenames;
- download MIME types;
- Scrub Key semantics;
- reinsert behavior;
- runtime/startup behavior;
- dependencies.

The implementation may change only the visible grouping/heading structure of the existing input surface.

## 7. Recommended implementation strategy

Use option A: one unified input section with upload, example selector and text area under the single existing heading.

Do not introduce tabs/radio in this package unless later screenshots prove a single vertical section is still too visually dense. Tabs/radio add state complexity and can make it less clear which input source is active. A unified section is the least risky because it preserves the current `uploaded_file`, `input_text`, `uploaded_file_type` and `st_text` semantics.

Recommended next implementation steps:

1. Pull latest `main` and inspect the actual runtime source around the input section.
2. Search for every occurrence of:

```text
Voeg document of tekst toe
st.file_uploader(
text_input
Gebruik een synthetisch juridisch testvoorbeeld
```

3. If duplicate source exists, remove the extra visible heading/upload widget and keep one authoritative input section.
4. If source has only one heading but the Space still renders two, inspect startup patch behavior and avoid adding another patch. Prefer direct-source repair and remove or neutralize the stale runtime mutation only if it is proven to be the cause.
5. Keep a single top-level heading:

```python
st.subheader("1. Voeg document of tekst toe")
```

6. Keep existing downstream variables:

```python
uploaded_file
uploaded_file_type
input_text
st_text
```

7. Keep existing precedence:

```text
uploaded file > selected synthetic example/default demo text > pasted/edited text area
```

8. Do not change supported file types:

```python
type=["txt", "docx", "pdf"]
```

9. Do not change `uploaded_file_to_text(uploaded_file)` or document parsing helpers.

## 8. Proposed contract tests for the next WP

Next package: `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS`.

The contract tests should assert:

- exactly one source occurrence of `st.subheader("1. Voeg document of tekst toe")` or an equivalent single input heading;
- no duplicate visible input step heading string;
- upload support for TXT/DOCX/PDF remains present;
- `uploaded_file_to_text(uploaded_file)` remains present;
- `uploaded_file_type` remains present;
- synthetic legal example flow remains present;
- text area for pasted/extracted text remains present;
- `key="text_input"` remains present;
- step order remains `1. Voeg document of tekst toe` -> `2. Controleer resultaat` -> `3. Exporteer resultaat` in source order;
- review/export/Scrub Key strings remain present;
- no runtime/startup patch or dependency change is introduced;
- tests do not import Streamlit or mutate app state.

Suggested test file:

```text
tests/test_duplicate_input_surface_simplification_contracts.py
```

## 9. Proposed implementation WP

After contract tests pass and merge, create:

```text
SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION
```

Implementation scope should be narrow:

- primary file: `presidio_streamlit.py` only;
- tests: contract test file plus one implementation source-level test if needed;
- optional documentation updates: `CHANGELOG.md`, `WORKPACKAGES.md`, handover and claim;
- no helper modules unless a tiny pure helper is clearly safer;
- no startup/runtime patching.

Implementation acceptance criteria:

- live app shows one `1. Voeg document of tekst toe` section;
- the section still supports upload, synthetic example, and paste/edit text;
- review and export sections remain unchanged;
- GitHub Actions green;
- Hugging Face sync green;
- coordinator app verification confirms one coherent input area.

## 10. Manual app verification checklist

After implementation merge and sync, verify in the live Space:

1. App starts without Script execution error.
2. Only one visible `1. Voeg document of tekst toe` section appears in Anonimiseren mode.
3. TXT upload remains visible and functional.
4. DOCX upload remains visible and functional.
5. Text-based PDF upload remains visible and functional within existing limits.
6. Synthetic legal example remains reachable in Dutch Legal Strict mode.
7. Pasted/extracted text area remains visible.
8. Selecting a synthetic example populates the text area when no upload is active.
9. Uploading a file still overrides default/example text.
10. `2. Controleer resultaat` remains visible after input.
11. `Basiscontrole` remains default and visibly cleaner.
12. `Expertcontrole` remains available.
13. `3. Exporteer resultaat` remains visible.
14. Document downloads remain visible.
15. Scrub Key and audit sections remain available.
16. No export/Scrub Key/reinsert/regression is visible.

## 11. Risks and rollback notes

Risks:

- If the duplication is caused by runtime mutation rather than direct source, a direct source edit alone may not remove it.
- If upload/example/text precedence is changed accidentally, users may scrub the wrong text.
- If an implementation hides the text area too aggressively, users lose the final editable review of extracted text before analysis.
- If the implementation uses tabs/radio, Streamlit state may make the active input source less obvious.

Rollback:

- Revert the implementation PR if the live Space loses any input source or changes downstream review/export behavior.
- Do not roll back the basic/expert review declutter unless a direct regression is proven there.
- Keep the plan and contract tests as documentation of the intended single-input target even if implementation requires a follow-up fix.

## Recommended next package

```text
SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_CONTRACT_TESTS
```

This should be test/spec-only and must merge before touching `presidio_streamlit.py`.
