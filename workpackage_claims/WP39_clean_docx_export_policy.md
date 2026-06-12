# Workpackage claim — WP39 Clean DOCX export policy

Repository: `solidprivacy-nl/scrub`

Workpackage: `WP39 — Clean DOCX export policy`

Status: `completed`

Claimed by: `ChatGPT webinterface worker`

Claim created: `2026-06-12`

Completed: `2026-06-12`

Scope completed: policy/tests/docs only. No cleaner, no removal, no export blocking implementation, no UI change, no export semantics change.

Files added:

```text
CLEAN_DOCX_EXPORT_POLICY.md
tests/test_clean_docx_export_policy.py
handover/workpackages/20260612_1915_clean_docx_export_policy.md
```

Files changed:

```text
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
workpackage_claims/WP39_clean_docx_export_policy.md
```

Validation:

```text
Not run in live GitHub checkout. Validate with GitHub Actions.
```

Expected checks:

```text
pytest tests/test_clean_docx_export_policy.py
pytest tests/test_clean_docx_export_policy.py tests/test_docx_hygiene_audit.py tests/test_docx_hidden_content_extractor.py tests/test_docx_residual_placeholder_comments_risk.py tests/test_scrub_key_document_reinsert.py
```

Handover path:

```text
handover/workpackages/20260612_1915_clean_docx_export_policy.md
```

Remaining risks:

```text
Current DOCX output is not clean DOCX export. No cleaner, removal, export blocking or UI integration was implemented.
```

Next recommended step:

```text
WP40 — Document-centric review UX specification
```
