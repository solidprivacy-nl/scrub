from __future__ import annotations

from pathlib import Path


TESTS_WORKFLOW_PATH = Path(".github/workflows/tests.yml")
CARRIER_WORKFLOW_PATH = Path(".github/workflows/issue70-exact-main-evidence-carrier.yml")


def _tests_workflow_text() -> str:
    return TESTS_WORKFLOW_PATH.read_text(encoding="utf-8")


def _carrier_workflow_text() -> str:
    return CARRIER_WORKFLOW_PATH.read_text(encoding="utf-8")


def test_tests_workflow_keeps_standard_and_manual_triggers() -> None:
    workflow = _tests_workflow_text()

    assert "push:\n    branches:\n      - main" in workflow
    assert "  pull_request:\n" in workflow
    assert "  workflow_dispatch:\n" in workflow
    assert "paths:" not in workflow
    assert "paths-ignore:" not in workflow


def test_issue70_recovery_listens_only_to_fresh_noop_carrier_reruns() -> None:
    workflow = _tests_workflow_text()

    assert (
        "  workflow_run:\n    workflows:\n      - Issue70 exact-main evidence carrier"
        in workflow
    )
    assert "    types:\n      - completed" in workflow
    assert "github.event.workflow_run.run_attempt > 1" in workflow
    assert "github.event.workflow_run.conclusion == 'success'" in workflow
    assert "permissions:\n  contents: read" in workflow


def test_issue70_workflow_run_checks_out_exact_default_branch_sha() -> None:
    workflow = _tests_workflow_text()

    # For workflow_run, GitHub sets GITHUB_SHA to the latest commit on the
    # default branch. A ref override here would defeat exact-main evidence.
    assert "uses: actions/checkout@v4" in workflow
    assert "ref:" not in workflow


def test_issue70_recovery_runs_the_unchanged_full_regression_command() -> None:
    workflow = _tests_workflow_text()

    assert "python -m pytest -q tests" in workflow
    assert workflow.count("python -m pytest -q tests") == 1


def test_issue70_carrier_is_noop_read_only_and_non_deploying() -> None:
    carrier = _carrier_workflow_text()

    assert "name: Issue70 exact-main evidence carrier" in carrier
    assert "  pull_request:" in carrier
    assert "permissions:\n  contents: read" in carrier
    assert "name: Safe no-op carrier" in carrier
    assert 'echo "issue70_evidence_carrier=true"' in carrier
    assert 'echo "repository_mutation=false"' in carrier
    assert 'echo "deployment_mutation=false"' in carrier

    forbidden = (
        "contents: write",
        "git push",
        "git commit",
        "actions/checkout",
        "workflow_dispatch:",
        "schedule:",
        "issue_comment:",
        "repository_dispatch:",
        "curl ",
        "gh ",
        "huggingface",
    )
    for token in forbidden:
        assert token not in carrier.lower()
