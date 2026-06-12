# Handover — WP28C MVP Scrub Key warning/acknowledgement UI implementation

Repository worked in: `solidprivacy-nl/scrub`

Workpackage title: `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`

Status: implemented; pending GitHub Actions, Hugging Face sync and app verification.

## Summary

Implemented MVP Scrub Key warning and acknowledgement gating for high-risk Scrub Key and reinsert UI actions.

The implementation uses the existing post-patch layer `fix_streamlit_pdf_text_reinsert.py`, which runs after `fix_streamlit_nested_expanders.py`, so the already-injected Scrub Key/reinsert UI can be gated without changing helper logic.

Acknowledgement gating was added for:

- Scrub Key JSON download/export;
- Scrub Key import/load;
- pasted-text reinsert;
- TXT reinsert;
- DOCX reinsert;
- PDF-to-TXT reinsert;
- restored pasted-text download;
- restored TXT download;
- restored DOCX download;
- restored TXT-from-PDF download.

Warnings were added for Scrub Key storage, Downloads/local storage, loss-of-key, external AI/e-mail sharing risk and restored-output confidentiality.

## Files added

- `tests/test_scrub_key_warning_acknowledgement_ui.py`
- `handover/workpackages/20260612_1545_mvp_scrub_key_warning_acknowledgement_ui.md`

## Files changed

- `fix_streamlit_pdf_text_reinsert.py`
- `RELEASE_NOTES.md`
- `CHANGELOG.md`
- `WORKPACKAGES.md`
- `RISK_REGISTER.md`
- `workpackage_claims/WP28C_mvp_scrub_key_warning_acknowledgement_ui.md`

## Tests/checks run

No executable tests were run in the exact GitHub checkout because the ChatGPT GitHub connector does not provide shell execution.

Added static regression tests in:

```text
tests/test_scrub_key_warning_acknowledgement_ui.py
```

The tests cover:

- warning copy placement;
- acknowledgement state keys;
- disabled buttons before acknowledgement;
- preserved Scrub Key JSON data, filename and MIME type;
- preserved restored output data, filenames and MIME types;
- existing helper calls and audit fields remaining present;
- absence of encryption, automatic deletion, expiry blocking, schema migration, cloud calls, key vault/recovery claims or export semantic rewiring.

GitHub Actions should validate the committed final files.

## Validation status

- Required start sequence was read.
- WP28C claim was checked before implementation and was already assigned to this ChatGPT webinterface worker.
- No second active WP28C claim was visible.
- No direct edit to `presidio_streamlit.py`.
- No helper logic changed.
- No Scrub Key schema migration.
- No import/export semantic change after acknowledgement.
- No reinsert semantic change after acknowledgement.
- No restored output bytes, filenames or MIME types changed after acknowledgement.
- No encryption implementation.
- No automatic deletion.
- No expiry blocking.
- No hidden recovery.
- No dependency change.
- No real data added.
- No cloud processing added.
- `RELEASE_NOTES.md`, `CHANGELOG.md`, `WORKPACKAGES.md` and `RISK_REGISTER.md` were updated.

## GitHub Actions status

Unknown at handover creation time.

## Hugging Face sync status

Unknown at handover creation time.

## App verification status

Required and pending because UI behavior changed.

Recommended app verification points:

- Scrub Key JSON download is disabled until export acknowledgement is checked.
- Scrub Key import/load is disabled until import acknowledgement is checked.
- Pasted-text/TXT/DOCX/PDF-to-TXT reinsert buttons are disabled until their acknowledgement is checked.
- Restored output download buttons are disabled until download acknowledgement is checked.
- After acknowledgement, JSON content, restored output content, filenames and download types remain unchanged.
- Existing anonymization/export flow still works.
- Existing pasted-text, TXT, DOCX and PDF-to-TXT reinsert flows still work.

## Remaining risks

- GitHub Actions, Hugging Face sync and app verification are still required.
- The implementation is in the startup patch layer, so rendered app behavior must be verified after deployment.
- UI acknowledgements are safety prompts only; they are not encryption, automatic deletion, protected storage, expiry enforcement or managed key recovery.
- Future protected key storage, encryption, lifecycle tooling and local vault work remain separate approved packages.

## Next recommended step

`WP28C-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout`.
