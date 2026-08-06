from __future__ import annotations

from pathlib import Path


WORKFLOW_PATH = Path(".github/workflows/tests.yml")


def _workflow_text() -> str:
    return WORKFLOW_PATH.read_text(encoding="utf-8")


def test_tests_workflow_keeps_standard_and_manual_triggers() -> None:
    workflow = _workflow_text()

    assert "push:\n    branches:\n      - main" in workflow
    assert "  pull_request:\n" in workflow
    assert "  workflow_dispatch:\n" in workflow
    assert "paths:" not in workflow
    assert "paths-ignore:" not in workflow


def test_issue70_fallback_is_narrow_and_default_branch_scoped() -> None:
    workflow = _workflow_text()

    assert "  issue_comment:\n    types:\n      - created" in workflow
    assert "github.event.issue.number == 70" in workflow
    assert "github.event.comment.body == '/run-tests-main'" in workflow
    assert "github.actor == 'market-predictions'" in workflow
    assert "permissions:\n  contents: read" in workflow

    # No ref is supplied to checkout: issue_comment workflows therefore test
    # the exact default-branch commit associated with the workflow run.
    assert "uses: actions/checkout@v4" in workflow
    assert "ref:" not in workflow


def test_issue70_fallback_runs_the_unchanged_full_regression_command() -> None:
    workflow = _workflow_text()

    assert "python -m pytest -q tests" in workflow
    assert workflow.count("python -m pytest -q tests") == 1
