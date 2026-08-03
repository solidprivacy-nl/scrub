from __future__ import annotations

import json
from pathlib import Path

from care_profile_cross_profile_matrix import build_cross_profile_matrix


output = Path("output/validation/care_profile_cross_profile_matrix.json")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(
    json.dumps(build_cross_profile_matrix(), indent=2, ensure_ascii=False, sort_keys=True)
    + "\n",
    encoding="utf-8",
)

Path("ops/generate_care_profile_cross_profile_matrix_artifact.py").unlink(missing_ok=True)
Path(".github/workflows/generate-care-profile-cross-profile-matrix.yml").unlink(missing_ok=True)
