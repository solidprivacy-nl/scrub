# WP28C app evidence — Scrub Key warning UI

Repository: `solidprivacy-nl/scrub`

Status: partial app evidence recorded.

## Evidence source

The coordinator provided a screenshot of the running Hugging Face app in mode:

```text
Originele waarden terugzetten
```

The screenshot itself is not stored in this repository.

## Observed in screenshot

The screenshot shows the Scrub Key / reinsert warning and acknowledgement flow in the running app:

- Scrub Key loading section is visible.
- Scrub Key warning text is visible.
- Acknowledgement checkbox before validating/loading the Scrub Key is visible.
- Original-values reinsert section is visible.
- TXT, DOCX and PDF-to-TXT reinsert warning sections are visible.
- DOCX limitation warning is visible.
- PDF-to-TXT limitation warning is visible.
- Reinsert buttons are gated by acknowledgement/input state.

## Interpretation

This is useful partial app evidence for WP28C warning/acknowledgement behavior in reinsert mode.

This screenshot does not verify WP42D, because the app is in reinsert mode and the static highlight preview is expected only in the anonymization review flow.

## Remaining verification needs

WP28C still needs full closeout evidence if not already provided elsewhere:

- GitHub Actions status for the relevant implementation commit.
- Hugging Face sync status.
- App verification for all warning/acknowledgement surfaces expected by WP28C.

## Recommended status

```text
WP28C — partial app evidence recorded for reinsert warning/acknowledgement UI.
```
