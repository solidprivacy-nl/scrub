# Handover — WP36A DOCX residual placeholder and comments risk triage

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP36A — DOCX residual placeholder and comments risk triage`

Status: completed triage/test/documentation-only.

## Summary

WP36A records the app-verification finding that DOCX restored output can still contain residual placeholders such as `[PERSOON_01]`, and that Word comments / kantlijncommentaren are outside the current DOCX scrub/reinsert flow.

This was treated as a high-risk document hygiene issue, not a cosmetic bug. The package adds a triage document and synthetic tests that make the current limitation visible without implementing a cleaner, removing comments, blocking export or changing export/reinsert semantics.

## Files added

- `DOCX_RESIDUAL_PLACEHOLDER_COMMENTS_TRIAGE.md`
- `tests/test_docx_residual_placeholder_comments_risk.py`
- `workpackage_claims/WP36A_docx_residual_placeholder_comments_risk_triage.md`
- `handover/workpackages/20260612_1625_docx_residual_placeholder_comments_risk_triage.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests added/updated

Added:

```text
tests/test_docx_residual_placeholder_comments_risk.py
```

The tests use synthetic data only and cover:

- residual placeholder mismatch `[PERSOON_01]` remains visible when the Scrub Key maps only `[PERSOON_1]`;
- unresolved placeholder audit fields remain visible;
- `word/comments.xml` is copied through unchanged by the current DOCX reinsert helper;
- current DOCX limitations still list comments/unsupported parts;
- the triage document records the issue as high-risk and explicitly does not implement a cleaner/export/UI fix;
- no real names or real identifiers are included.

## Tests/checks run

No tests were run in the live GitHub checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository.

Expected targeted validation:

```text
pytest tests/test_docx_residual_placeholder_comments_risk.py
```

Expected related regression validation:

```text
pytest tests/test_scrub_key_document_reinsert.py tests/test_docx_residual_placeholder_comments_risk.py
```

## Validation status

- Required start sequence was followed from GitHub `main`.
- WP36A claim was checked and created before changes.
- Existing DOCX hidden-content risk review and DOCX reinsert helper behavior were inspected.
- Triage/test/documentation-only boundaries were preserved.
- No real data was added.

## GitHub Actions status

- Pending / not verified through connector at handover time.
- The final commits should be validated by GitHub Actions.

## Hugging Face sync status

- Not applicable for app behavior. WP36A does not change UI/runtime behavior in the Hugging Face Space.
- Repository sync status may still be checked by normal project monitoring.

## App verification status

- App-verification finding was supplied by the coordinator/user and recorded.
- No new app verification is required for this workpackage because no UI or runtime behavior changed.

## Remaining risks

- DOCX restored output can still contain residual placeholders when placeholders are mismatched, split across runs or absent from the Scrub Key.
- Word comments/kantlijncommentaren remain outside current processing and can contain sensitive data.
- Comments, tracked changes, headers, footers, metadata and other hidden content still need extraction/audit support.
- No DOCX cleaner, comment removal or export-blocking policy exists yet.
- Current tests make the risk visible but do not fix it.

## Next recommended step

- `WP37 — Headers/footers/comments/tracked-changes extraction helper`.

## Intentionally not changed

- No DOCX cleaner implemented.
- No comments/tracked-changes removal implemented.
- No export blocking.
- No export semantics changed.
- No Streamlit UI changed.
- No helper behavior changed.
- No Scrub Key schema changed.
- No real data added.
- No cloud processing added.
