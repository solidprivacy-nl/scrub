# Handover — WP39 Clean DOCX export policy

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP39 — Clean DOCX export policy`

Status: completed policy/tests/documentation-only.

## Summary

WP39 added a clean DOCX export policy. The policy states that current DOCX output must not be described as a clean DOCX export and defines warning/report policy, future blocking candidates and minimum requirements before any clean-DOCX claim.

This work is policy-only. It does not implement a DOCX cleaner, remove comments, remove/accept tracked changes, block export, change export semantics, change DOCX reinsert behavior, change Streamlit UI, change Scrub Key schema, add dependencies, add cloud processing or add real data.

## Files added

- `CLEAN_DOCX_EXPORT_POLICY.md`
- `tests/test_clean_docx_export_policy.py`
- `workpackage_claims/WP39_clean_docx_export_policy.md`
- `handover/workpackages/20260612_1915_clean_docx_export_policy.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `RISK_REGISTER.md`

## Tests added/updated

Added:

```text
tests/test_clean_docx_export_policy.py
```

The tests verify:

- current DOCX output cannot be called clean DOCX export;
- current export semantics and no-blocking boundary are preserved;
- warning/report rules exist for supported findings and invalid DOCX;
- minimum requirements before clean-export claims are documented;
- no cleaner/UI/export behavior is implemented by the policy;
- no real personal data examples are used.

## Tests/checks run

No tests were run in the live GitHub checkout because the ChatGPT GitHub connector does not provide shell execution in the checked-out repository.

Expected targeted validation:

```text
pytest tests/test_clean_docx_export_policy.py
```

Expected related regression validation:

```text
pytest tests/test_clean_docx_export_policy.py tests/test_docx_hygiene_audit.py tests/test_docx_hidden_content_extractor.py tests/test_docx_residual_placeholder_comments_risk.py tests/test_scrub_key_document_reinsert.py
```

## Validation status

- Required start sequence was followed from GitHub `main`.
- WP39 claim was checked and created before changes.
- Current DOCX hygiene line status was inspected.
- Policy/test/documentation-only boundaries were preserved.
- No real data was added.

## GitHub Actions status

- Pending / not verified through connector at handover time.
- The final commits should be validated by GitHub Actions.

## Hugging Face sync status

- Not applicable for app behavior. WP39 does not change UI/runtime behavior in the Hugging Face Space.
- Repository sync status may still be checked by normal project monitoring.

## App verification status

- Not applicable; no UI behavior changed.

## Remaining risks

- Current DOCX output is still not a clean DOCX export.
- No DOCX cleaner exists yet.
- No comments/tracked-changes removal exists yet.
- No export blocking implementation exists yet.
- WP38 audit output is not yet surfaced in product UI.
- Metadata, footnotes, endnotes, text boxes, shapes, charts, embedded objects and custom XML remain future scope.

## Next recommended step

- `WP40 — Document-centric review UX specification`.
- Alternative DOCX-specific follow-up: `WP39B — DOCX hygiene audit UI planning`.

## Intentionally not changed

- No DOCX cleaner implemented.
- No comments/tracked-changes removal implemented.
- No export blocking implemented.
- No export semantics changed.
- No DOCX reinsert behavior changed.
- No Streamlit UI changed.
- No Scrub Key schema changed.
- No dependency change.
- No real data added.
- No cloud processing added.
