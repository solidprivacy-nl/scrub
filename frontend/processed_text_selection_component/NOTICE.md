# Notice — Streamlit component protocol bridge

The local file `streamlit_bridge.js` is an independent minimal implementation of the public Streamlit Components v1 iframe messaging protocol used by this non-mutating spike.

The protocol names and behavior were checked against the official `streamlit-component-lib` project, which is distributed under the Apache License 2.0:

- project: `streamlit/streamlit-component-lib`
- copyright: Streamlit Inc.
- license: Apache License 2.0

No external `streamlit-component-lib` JavaScript bundle is copied, installed or loaded at runtime. The spike keeps the bridge small, local and dependency-free. It sends only:

- `streamlit:componentReady`;
- `streamlit:setFrameHeight`;
- `streamlit:setComponentValue`;

and listens only for:

- `streamlit:render`.

The remainder of the component code is specific to SolidPrivacy Scrub and is covered by the repository's own licensing and governance.
