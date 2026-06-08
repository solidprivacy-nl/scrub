# Handover — WP9 — AI-output / document reinsert workflow UX and architecture review

Repository: `solidprivacy-nl/scrub`  
Status: completed; review-only workpackage

## Summary

WP9 completed the AI-output / document reinsert workflow UX and architecture review.

The review was added in `AI_OUTPUT_REINSERT_WORKFLOW_REVIEW.md` and explicitly challenged the first three obvious ideas:

1. keep only pasted-text reinsert;
2. immediately add broad PDF/DOCX upload reinsert;
3. keep anonymization and de-anonymization in one combined long screen.

Final recommendation:

- Keep pasted-text reinsert as a safe baseline and fallback.
- Do not treat pasted text as the final legal-document workflow.
- Move toward a two-mode interface:
  - `Anonimiseren`;
  - `Originele waarden terugzetten`.
- Add document-level reinsert in phases.
- Prioritize TXT and DOCX before PDF.
- Do not implement full PDF reinsert yet.
- Do not add AI calls.
- Do not add cloud processing.
- Keep implementation local-only, deterministic, helper-first and test-first.

Recommended next implementation workpackage:

```text
WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests
```

## Files added

- `AI_OUTPUT_REINSERT_WORKFLOW_REVIEW.md`
- `handover/workpackages/20260608_0000_ai_output_reinsert_workflow_review.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`

## Tests

- Tests: not applicable; planning/review-only workpackage.
- No tests were added or changed.
- No local test run was required by the WP scope.

## Validation

- Validation status: documentation review completed.
- GitHub Actions: not checked after this docs-only change at handover time.
- Hugging Face sync: not checked after this docs-only change at handover time.
- App verification: not applicable; no UI behavior changed.

## GitHub Actions status

Unknown / not checked after this docs-only change.

## Hugging Face sync status

Unknown / not checked after this docs-only change.

## App verification status

Not applicable; no UI behavior changed.

## Remaining risks

- Document-level DOCX reinsert can damage or miss placeholders if Word run-splitting, tables, headers, footers or unsupported document parts are not handled carefully.
- PDF reinsert remains high-risk because of text extraction, layout reconstruction, scanned PDFs, OCR, metadata and reliability limitations.
- Future UI work should avoid parallel edits to `fix_streamlit_nested_expanders.py`, `presidio_streamlit.py`, export/download flow and shared session state.
- Metadata-clean restored document output is not solved by this review and should remain a separate document hygiene concern.

## Next recommended step

Start:

```text
WP10 — v13.4 TXT/DOCX reinsert foundation helper and tests
```

Recommended WP10 scope:

- helper/test-only first;
- reuse `reinsert_from_scrub_key(...)`;
- add pure TXT and DOCX reinsert foundation;
- use synthetic data only;
- do not edit UI;
- do not edit `fix_streamlit_nested_expanders.py` or `presidio_streamlit.py`;
- do not change export/download semantics;
- do not implement PDF reinsert;
- do not add AI calls;
- do not add cloud processing.
