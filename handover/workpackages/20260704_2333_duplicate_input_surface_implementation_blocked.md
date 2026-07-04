# Handover — SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION

Repository worked in: solidprivacy-nl/scrub

## Workpackage title

SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION — Remove duplicate upload/input presentation while preserving ingestion behavior

## Status

Blocked before product edit.

## Files added

- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_implementation.md`
- `handover/workpackages/20260704_2333_duplicate_input_surface_implementation_blocked.md`

## Files changed

- `workpackage_claims/scrub_wp_duplicate_input_surface_simplification_implementation.md`

No product implementation files were changed.

## Tests/checks

- PR #22 contract-test package was merged first.
- Direct source around the input section in `presidio_streamlit.py` was inspected through the GitHub connector.
- No implementation tests were run because no product edit was made.

## Validation status

Blocked before implementation validation.

The inspected input section currently contains one direct source heading:

```python
st.subheader("1. Voeg document of tekst toe")
```

and the existing input path remains:

- `uploaded_file = st.file_uploader(...)`
- `uploaded_file_type = None`
- `input_text = "".join(demo_text)`
- optional synthetic legal example selection
- uploaded file override through `uploaded_file_to_text(uploaded_file)`
- final editable `st_text = st.text_area(...)`

## GitHub Actions status

- PR #22 Tests were green before merge.
- PR #22 was merged to `main` with merge SHA `9f3277f9f860c06f70e28604ea0189cd3396610d`.
- No workflow runs were visible yet for the merge commit through the connector at the time of this handover.

## Hugging Face sync status

Unknown / pending. No workflow runs were visible yet for the merge commit through the connector.

## App verification status

Not applicable for the blocked implementation branch. No UI behavior changed.

## Blocker

The GitHub connector can fetch large files only as truncated views in this chat interface, while GitHub contents updates require a complete replacement body for `presidio_streamlit.py`. The local execution sandbox cannot clone GitHub because DNS resolution for `github.com` fails. A direct-source edit would therefore risk partially overwriting the app file.

## Remaining risks

- The duplicate visible input surface remains unresolved in the live app.
- The implementation still needs to be completed in an environment that can safely edit the full `presidio_streamlit.py` file.
- Because current direct source already shows one static input heading, the implementation should verify whether the live duplicate is caused by visual grouping, stale runtime state, or another runtime/source mismatch.

## Next recommended step

Continue `SCRUB-WP_DUPLICATE_INPUT_SURFACE_SIMPLIFICATION_IMPLEMENTATION` in GitHub Codespaces or a local clone, using the merged contract tests as guardrails. Keep the implementation narrow: direct-source UI grouping/removal only, no startup patching, no upload/export/Scrub Key/reinsert semantics changes.
