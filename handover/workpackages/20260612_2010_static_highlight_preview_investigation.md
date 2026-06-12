# Handover — WP42D-INVESTIGATE static highlight preview not visible

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP42D-INVESTIGATE — diagnose why the static highlight preview panel is not visible in the running app`

Status: completed diagnosis-only; no fix implemented.

## Summary

Investigated why the expected static highlight preview panel was not visible in the coordinator-provided Hugging Face app screenshot.

Expected panel label:

```text
Documentvoorbeeld met markeringen — experimenteel
```

Diagnosis:

```text
Most likely the running Hugging Face app is not using the WP42D-patched runtime yet, or the patch-chain needs stronger diagnostics/fail-fast checks.
```

## Files added

- `WP42D_INVESTIGATION_REPORT.md`
- `workpackage_claims/WP42D_INVESTIGATE_static_highlight_preview_not_visible.md`
- `handover/workpackages/20260612_2010_static_highlight_preview_investigation.md`

## Files changed

- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP42D_INVESTIGATE_static_highlight_preview_not_visible.md`

## Tests/checks run

No shell tests were run because the ChatGPT GitHub connector does not provide shell execution.

Connector file review was performed on:

- `fix_streamlit_static_highlight_preview.py`
- `presidio_streamlit.py`
- `fix_streamlit_nested_expanders.py`
- `Dockerfile`

## Validation status

- WP42D patch file exists and contains the expected preview label and safety gates.
- Repository `Dockerfile` includes the static highlight patch command before Streamlit starts.
- Raw `presidio_streamlit.py` does not contain the panel because WP42D is implemented as a startup patch.
- `fix_streamlit_nested_expanders.py` creates the upstream review-table anchor used by the WP42D patch.

## GitHub Actions status

Unknown for final handover commit.

## Hugging Face sync status

Unknown for final handover commit.

## App verification status

Not passed from prior evidence. Expected panel was not visible in the provided screenshot.

## Remaining risks

- Running Space may not be using the latest WP42D-patched runtime.
- Patch-chain diagnostics are not strong enough to prove at app startup whether the panel was inserted.
- No fix has been implemented yet.

## Next recommended step

`WP42D-FIX — Static highlight preview deployment/patch-chain hardening`.
