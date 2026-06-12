# WP42D-INVESTIGATE — Static highlight preview panel not visible

Repository: `solidprivacy-nl/scrub`

Status: diagnosis completed; no fix implemented.

## Trigger

Coordinator-provided app verification screenshot showed the existing Scrub Legal review flow and replacement table, but did not show the expected panel:

```text
Documentvoorbeeld met markeringen — experimenteel
```

The screenshot itself was not stored in the repository.

## What was inspected

Files reviewed through the GitHub connector:

```text
fix_streamlit_static_highlight_preview.py
presidio_streamlit.py
fix_streamlit_nested_expanders.py
Dockerfile
```

## Findings

### 1. The preview is not present in the raw app source

`presidio_streamlit.py` does not contain the static highlight preview panel in source form.

That is expected for WP42D because the feature was implemented as a startup patch.

### 2. The WP42D startup patch exists

`fix_streamlit_static_highlight_preview.py` exists and contains the expected panel label:

```text
Documentvoorbeeld met markeringen — experimenteel
```

It also contains the intended safety gates:

```text
safe_to_render
read_only
non_authoritative
mutation_allowed=False
export_blocking=False
scrub_key_changes=False
```

### 3. Dockerfile contains the patch command

The repository `Dockerfile` runs:

```text
python fix_streamlit_nested_expanders.py && python fix_streamlit_pdf_text_reinsert.py && python fix_streamlit_static_highlight_preview.py && streamlit run presidio_streamlit.py ...
```

So the repository version intends to run the static highlight patch after the existing Streamlit patches and before app startup.

### 4. The running app appears to have older patch behavior but not WP42D behavior

The screenshot shows existing review UI features such as the replacement table and technical-details expander.

However, it does not show the WP42D preview expander.

Because the WP42D patch inserts a visible collapsed expander before the data editor, the expected label should be visible if the running app used the patched source.

## Most likely diagnosis

The running Hugging Face app is probably not using the WP42D-patched runtime yet.

Most likely causes, in order:

1. Hugging Face sync/build has not deployed the commit containing `fix_streamlit_static_highlight_preview.py` and the updated `Dockerfile` command.
2. The Space is running an older cached container build.
3. The startup command used by the running Space differs from the repository `Dockerfile` command.
4. Less likely: the WP42D patch target does not match the runtime-mutated `presidio_streamlit.py` after earlier patches.

## Why patch-target mismatch is less likely but still possible

`fix_streamlit_static_highlight_preview.py` inserts the preview by matching a block produced by `fix_streamlit_nested_expanders.py`.

Connector inspection shows that the expected anchor block exists in the earlier patch script.

Still, this has not been proven by executing the full startup patch chain in the live container, so a patch-chain contract test or fail-fast diagnostic would be useful.

## Recommended next step

Recommended package:

```text
WP42D-FIX — Static highlight preview deployment/patch-chain hardening
```

Suggested fix direction:

1. Add a patch-chain contract test that validates the WP42D insertion target against the upstream patch output.
2. Add a visible or logged patch marker so a worker can confirm whether the WP42D patch ran.
3. Make the WP42D patch fail loudly or report a clear diagnostic if its insertion target is not found.
4. Only after tests are green, verify Hugging Face sync and app behavior again.

## Non-changes

This investigation did not change:

- UI behavior;
- Streamlit app source;
- Docker runtime behavior;
- export/download behavior;
- Scrub Key behavior;
- reinsert behavior;
- helper behavior;
- dependencies;
- cloud processing;
- real-data fixtures.
