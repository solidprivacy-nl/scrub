# WP42D-FIX4 claim

Workpackage: `WP42D-FIX4 — Static highlight preview stale-block cleanup repair`

Status: `in_progress`

Repository: `solidprivacy-nl/scrub`

Claimed by: `ChatGPT webinterface worker`

Reason: runtime still shows the old broken preview block, likely because a previous startup patch already modified `presidio_streamlit.py` in the running container and the new patch skipped reinsertion when the title was present.

Scope: minimal startup patch cleanup repair. Remove stale inserted preview blocks before inserting the safe no-expander preview. No export, reinsert, Scrub Key, dependency, cloud processing or real-data changes.
