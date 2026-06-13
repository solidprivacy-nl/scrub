# Handover — WP42D-ROLLBACK-REPAIR Static preview source cleanup / HF startup repair

Repository: `solidprivacy-nl/scrub`

Workpackage title: `WP42D-ROLLBACK-REPAIR — Static preview source cleanup / HF startup repair`

Status: implemented HF runtime cache-bust and source guard; awaiting GitHub Actions, Hugging Face sync and app verification.

## Summary

Coordinator/user evidence after green GitHub Actions and Hugging Face sync still showed the Hugging Face Space stuck on `Restarting` with a Streamlit script execution error pointing to:

```text
/home/user/app/presidio_streamlit.py line 1081
st.caption("Alleen-lezen voorbeeld. De vervangtabel blijft leidend voor beslissingen, Scrub Key en export.")
```

GitHub `main` no longer contains that stale static-highlight preview caption or helper block in `presidio_streamlit.py`; the file currently ends around the normal table-first app flow and does not have a line 1081. This suggests the Space was still running or rebuilding from a stale mutated runtime image/container state.

The repair therefore does two minimal things:

1. Adds a Dockerfile cache-bust marker before the application `COPY --chown=user . $HOME/app` layer so Hugging Face must build a fresh runtime image.
2. Adds regression tests asserting that `presidio_streamlit.py` does not contain the stale static preview title/caption/helper text.

The experimental static highlight preview remains parked and the startup patch remains disabled/no-op.

## Files added

- `workpackage_claims/WP42D_ROLLBACK_REPAIR_static_preview_source_cleanup.md`
- `handover/workpackages/20260613_0030_wp42d_rollback_source_cleanup_repair.md`

## Files changed

- `Dockerfile`
- `tests/test_static_highlight_preview_ui_integration_patch.py`
- `WORKPACKAGES.md`
- `CHANGELOG.md`
- `workpackage_claims/WP42D_ROLLBACK_REPAIR_static_preview_source_cleanup.md`

## Tests added/updated

Updated `tests/test_static_highlight_preview_ui_integration_patch.py` with:

- `test_app_source_no_longer_contains_static_highlight_preview_block`
- `test_dockerfile_forces_clean_hf_runtime_after_rollback_repair`

## Tests/checks run

The exact updated GitHub checkout could not be executed through the ChatGPT GitHub connector because the connector does not provide shell execution in the checked-out repository.

Expected targeted check:

```text
pytest tests/test_static_highlight_preview_ui_integration_patch.py
```

Expected broader check after targeted pass:

```text
pytest
```

## Validation status

- Static review completed against the coordinator-provided Hugging Face error screenshot.
- GitHub `main` was checked for the stale static preview strings; repository search did not find the stale `Alleen-lezen voorbeeld` / `Documentvoorbeeld met markeringen — experimenteel` strings.
- Dockerfile now contains `SCRUB_ROLLBACK_REPAIR=20260613_0015` before application copy.
- Full validation depends on GitHub Actions and Hugging Face sync after the final repair commit.

## GitHub Actions status

Unknown at handover time. A new run is required for the final repair commit.

## Hugging Face sync status

Unknown at handover time. A new sync is required for the final repair commit.

## App verification status

Pending. The coordinator/user must verify that the Space leaves `Restarting`, no longer shows a script execution error, and starts the normal Scrub Legal table-first interface.

## Intentionally not changed

- No new highlight preview UI.
- No replacement UI implementation.
- No changes to `fix_streamlit_nested_expanders.py`.
- No export/download behavior change.
- No Scrub Key behavior change.
- No reinsert behavior change.
- No dependency change.
- No cloud processing.
- No real-data fixtures.

## Remaining risks

- Hugging Face may still require a manual Factory reboot if its Space runtime remains pinned to a stale failed container despite the Dockerfile cache-bust.
- Static highlight preview UI work remains parked until redesigned without startup source mutation.
- WP28C closeout still requires complete Actions/HF/app verification evidence.

## Next recommended step

1. Verify GitHub Actions for the final repair commit.
2. Verify Hugging Face sync for the final repair commit.
3. Hard refresh the Hugging Face app and confirm the normal Scrub Legal interface starts without the script execution error.
4. If Hugging Face remains stuck after green sync, perform a manual Factory reboot in the Space settings/runtime controls and retry app verification.
