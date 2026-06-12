# Workpackage claim — WP36A DOCX residual placeholder and comments risk triage

Repository: `solidprivacy-nl/scrub`

Workpackage: WP36A — DOCX residual placeholder and comments risk triage

Status: completed

Claimed by: `ChatGPT webinterface worker`

Claim created: `2026-06-12`

Completed: `2026-06-12`

Scope completed:

- Triage/document/test-only for DOCX residual placeholders and Word comments/kantlijncommentaren risk.
- No DOCX cleaner implementation.
- No comments/tracked-changes removal implementation.
- No export blocking.
- No export semantics change.
- No Streamlit UI change.
- No real data.
- No cloud processing.

Files added:

```text
DOCX_RESIDUAL_PLACEHOLDER_COMMENTS_TRIAGE.md
tests/test_docx_residual_placeholder_comments_risk.py
handover/workpackages/20260612_1625_docx_residual_placeholder_comments_risk_triage.md
```

Files changed:

```text
WORKPACKAGES.md
CHANGELOG.md
RISK_REGISTER.md
workpackage_claims/WP36A_docx_residual_placeholder_comments_risk_triage.md
```

Validation:

```text
Not run in live GitHub checkout. Validate with GitHub Actions.
```

Expected checks:

```text
pytest tests/test_docx_residual_placeholder_comments_risk.py
pytest tests/test_scrub_key_document_reinsert.py tests/test_docx_residual_placeholder_comments_risk.py
```

Handover path:

```text
handover/workpackages/20260612_1625_docx_residual_placeholder_comments_risk_triage.md
```

Remaining risks:

```text
DOCX residual placeholders and Word comments remain unsolved. No cleaner, comments/tracked-changes removal, export blocking or UI change was implemented.
```

Next recommended step:

```text
WP37 — Headers/footers/comments/tracked-changes extraction helper
```
