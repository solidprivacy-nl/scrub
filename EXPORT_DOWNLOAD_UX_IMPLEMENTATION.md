# Export/download UX implementation

Workpackage: `WP_EXPORT_DOWNLOAD_UX_IMPLEMENTATION_DIRECT_REPAIR`

Repository: `solidprivacy-nl/scrub`

Status: direct repair implemented, pending verification.

## Summary

The earlier startup-patch route was removed because live app verification showed it did not affect the Hugging Face app.

The grouped export/download UX is now implemented directly in:

```text
presidio_streamlit.py
```

The export section is now:

```text
5. Exporteer resultaat
```

with visible groups:

```text
Document downloaden
Scrub Key
Audit en technische bestanden
```

## Removed route

The failed startup patch file was removed:

```text
fix_streamlit_export_download_ux.py
```

The Dockerfile no longer runs that patch.

## Safety boundaries

Not changed:

```text
export payloads
download bytes
filenames
MIME types
export eligibility
Scrub Key contents
Scrub Key helper logic
reinsert behavior
review table behavior
side-by-side review behavior
serial review behavior
candidate scanner behavior
recognizer behavior
benchmark/report logic
```

## Verification required

Live app verification is required because visible UI changed.

Required live checks:

```text
No Script execution error
Section title says "5. Exporteer resultaat"
Document downloaden group is visible
Scrub Key group is visible and separated
Audit en technische bestanden group is visible
TXT/DOCX/PDF/CSV/report downloads remain available
DOCX hygiene audit remains available
Technical information remains available
```
