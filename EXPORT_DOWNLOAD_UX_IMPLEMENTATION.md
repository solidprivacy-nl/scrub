# Export/download UX implementation

Workpackage: `WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION`

Repository: `solidprivacy-nl/scrub`

Status: implemented, pending verification.

## Summary

Implemented the grouped export/download UX through a startup patch:

```text
fix_streamlit_export_download_ux.py
```

The Hugging Face startup command now runs this patch after the existing nested-expander patch and before Streamlit starts.

This keeps the change small and isolated while preserving existing export semantics.

## User-facing export groups

The export section is changed from:

```text
5. Download opgeschoonde bestanden
```

to:

```text
5. Exporteer resultaat
```

The section now groups controls under:

```text
Document downloaden
Scrub Key
Audit en technische bestanden
```

## Safety boundaries

Not changed:

```text
export payloads
download bytes
filenames
MIME types
export eligibility
Scrub Key contents
Scrub Key creation logic
reinsert behavior
review table behavior
candidate scanner behavior
recognizer behavior
benchmark/report logic
```

Not added:

```text
ZIP export
new bundled package export
new combined export format
new export blocking
new Scrub Key acknowledgement
new gate
product claim
```

## Scrub Key

The Scrub Key appears in its own visible group with this warning:

```text
De Scrub Key kan originele waarden herstellen. Bewaar dit bestand veilig.
```

The JSON content is still produced by the existing `build_scrub_key` and `scrub_key_to_json` helpers.

## Audit and technical files

The audit group keeps these existing outputs available:

```text
Vervangtabel downloaden (.csv)
Scrubrapport downloaden (.txt)
DOCX hygiene audit
Technische informatie
```

The DOCX hygiene audit remains report-only and is not nested inside another Streamlit expander.

## Tests

Implementation tests:

```text
tests/test_export_download_ux_implementation.py
```

Contract tests remain:

```text
tests/test_export_download_ux_contracts.py
```

## Next recommended step

After green Actions, HF sync and app verification:

```text
WP_REVIEW_DEBUG_ELEMENTS_COLLAPSE_PLAN
```

Do not start follow-up work automatically.
