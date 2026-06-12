"""Disabled startup patch for the experimental static highlight preview UI.

WP42D-ROLLBACK disables this patch because repeated runtime errors showed that
mutating ``presidio_streamlit.py`` at container startup is too fragile for this
feature. The working table-first interface takes priority.

This file is intentionally a no-op. It is kept only so accidental/manual calls
remain harmless until the highlight preview can be redesigned without startup
source mutation.
"""

from __future__ import annotations

print("Static highlight preview startup patch disabled by WP42D-ROLLBACK.")
