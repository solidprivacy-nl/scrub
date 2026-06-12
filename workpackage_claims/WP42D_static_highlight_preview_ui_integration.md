# WP42D claim

Workpackage: `WP42D — Static highlight preview UI integration`

Status: `completed`

Repository: `solidprivacy-nl/scrub`

Claimed by: `ChatGPT webinterface worker`

Explicit coordinator approval: user said `Please continue` after WP42D was presented as the next UI step requiring explicit approval.

Scope completed: implemented UI patch/tests; awaiting GitHub Actions, Hugging Face sync and app verification.

Files added:

```text
fix_streamlit_static_highlight_preview.py
tests/test_static_highlight_preview_ui_integration_patch.py
handover/workpackages/20260612_2130_static_highlight_preview_ui_integration.md
```

Files changed:

```text
Dockerfile
WORKPACKAGES.md
CHANGELOG.md
RELEASE_NOTES.md
RISK_REGISTER.md
workpackage_claims/WP42D_static_highlight_preview_ui_integration.md
```

Expected checks:

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py tests/test_highlight_preview.py
```

Validation status:

- No export/download semantics, Scrub Key schema/behavior, reinsert behavior, helper runtime behavior, dependency, cloud processing or real data changed.
- App verification required because UI behavior changed.

Remaining risks:

- New UI patch has not been verified by Actions or app verification.
- The preview remains read-only and non-authoritative.

Next recommended step:

```text
WP42D-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout
```
