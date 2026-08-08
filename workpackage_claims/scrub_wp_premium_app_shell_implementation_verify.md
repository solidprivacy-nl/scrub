# Workpackage claim — SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY

Status: completed  
Assurance decision: `FAIL`  
Closeout status: `GOVERNANCE_FAIL`

Claimed: 2026-08-08 Europe/Amsterdam  
Initial decision recorded: 2026-08-08 16:17 Europe/Amsterdam  
Repository: `solidprivacy-nl/scrub`  
Issue: `#90`  
Candidate PR: `#85`  
Candidate base: `d54eb06f9c6fea7c1f36cdb082b475c0d4666507`  
Candidate head: `2b04ca6260bddee07fbcf901239cee2955bd6dc7`  
Tested merge candidate: `ed7728fc85f22026863faab435a00a31a5aa1438`  
Role: `governance_release_assurance`

## Independent decision

`SCRUB-WP_PREMIUM_APP_SHELL_IMPLEMENTATION_VERIFY: FAIL`

The production Streamlit integration does not preserve the active recognition profile across a presentation-only Standard → Expert transition. Standard persists `_premium_profile_label`; Expert initializes `Controlemodus` from hard-coded `index=1`. The authoritative Streamlit profile order places Zorg at index 0 and Juridisch at index 1. A Standard Zorg session can therefore silently become Juridisch solely because the user changes presentation mode.

This violates the binding presentation-only invariant and processing/state-integrity acceptance criteria. Assurance made no repair and did not merge PR #85.

## Machine evidence

Raw Actions evidence was independently inspected:

```text
Tests run #2211 / 31259805641
job 93108743739
head_sha 2b04ca6260bddee07fbcf901239cee2955bd6dc7
checked-out merge candidate ed7728fc85f22026863faab435a00a31a5aa1438
python -m pytest -q tests
1225 passed in 10.32s
conclusion success
```

The suite does not cover the blocking integrated Standard/Expert profile-preservation path.

## Action boundary

- Candidate repair: none by assurance.
- Merge: prohibited for this head.
- Post-merge Actions: not applicable.
- Hugging Face sync: not applicable because no merge/deployment action is authorized.
- App verification: not applicable because no deployment action is authorized.
- Input Stage release: remains gated.

## Next step

Return to `implementation_operations` for a new head that preserves authoritative processing-affecting state across presentation changes and adds integrated regression coverage. The repaired head requires a fresh blind assurance pass.