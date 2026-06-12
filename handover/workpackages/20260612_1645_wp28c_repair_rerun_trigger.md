# WP28C repair rerun trigger

Repository: `solidprivacy-nl/scrub`

Purpose: trigger a fresh Tests run after the current repository state includes the WP28C warning acknowledgement test repair.

Current repair already present:

```text
tests/test_scrub_key_warning_acknowledgement_ui.py now reads both fix_streamlit_pdf_text_reinsert.py and presidio_streamlit.py for helper visibility checks.
```

No code, UI, helper logic, export/reinsert behavior, dependency, schema, runtime behavior or real data changed in this trigger commit.

Next step: check the new Tests and Sync runs for this commit. If green, proceed with WP28C app verification and then WP28C-CLOSEOUT.
