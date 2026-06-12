# Workpackage claim — WP28C MVP Scrub Key warning/acknowledgement UI implementation

Repository: `solidprivacy-nl/scrub`

Workpackage: `WP28C — MVP Scrub Key warning/acknowledgement UI implementation`

Status: `completed`

Claimed by: `ChatGPT webinterface worker`

Claim created: `2026-06-12`

Completion status: `implemented; pending GitHub Actions, Hugging Face sync and app verification`

Final implementation commit sequence includes:

- `a817bd11368319cac34aa5e969852046bed19249` — UI post-patch implementation.
- `b584a9d2bc545904143d1bbdc7529b60e95cec7a` — static warning acknowledgement UI tests.
- `cd2c83ed9f70d741316bff60637ac027756f4289` — release notes update.
- `5e8f4938548e5e8d8528e1b38165e8fc78af5107` — changelog update.
- `7ea64b1076ab167138132cfeb5efabd846b6f1ba` — workpackages status update.
- `f70710336641e4c70eceb380b2e972071fd9bd6e` — risk register update.
- `266b5d5d09fbb5cadd7a2e80001a05dff253bfce` — handover file.

Handover path:

`handover/workpackages/20260612_1545_mvp_scrub_key_warning_acknowledgement_ui.md`

Tests/checks:

- Added `tests/test_scrub_key_warning_acknowledgement_ui.py`.
- Exact checkout tests could not be run through the ChatGPT GitHub connector.
- GitHub Actions should validate the committed final files.

Validation status:

- No duplicate WP28C claim was visible before implementation.
- No helper logic changed.
- No Scrub Key schema migration.
- No import/export or reinsert semantic change after acknowledgement.
- No output byte, filename or MIME type change after acknowledgement.
- No encryption, automatic deletion, expiry blocking, hidden recovery, dependency change, real data or cloud processing added.

Remaining risks:

- GitHub Actions, Hugging Face sync and app verification are still required.
- UI acknowledgements are safety prompts only, not protected storage or encryption.

Next recommended step:

`WP28C-VERIFY — GitHub Actions, Hugging Face sync and app verification closeout`.
