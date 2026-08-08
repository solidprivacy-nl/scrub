"""Pure state model for the premium Scrub core flow.

This module is deliberately presentation-only. It does not invoke recognizers,
mutate replacement decisions, generate exports, or change Scrub Key semantics.
"""
from dataclasses import dataclass, replace
from enum import Enum
from typing import Optional, Sequence


class Workflow(str, Enum):
    ANONYMIZE = "anonymize"
    REINSERT = "reinsert"


class PresentationMode(str, Enum):
    STANDARD = "standard"
    EXPERT = "expert"


class Stage(str, Enum):
    ADD = "add"
    REVIEW = "review"
    DOWNLOAD = "download"


@dataclass(frozen=True)
class CoreFlowState:
    workflow: Workflow = Workflow.ANONYMIZE
    presentation_mode: PresentationMode = PresentationMode.STANDARD
    stage: Stage = Stage.ADD
    source_generation: Optional[str] = None
    processed_generation: Optional[str] = None
    reviewed_generation: Optional[str] = None
    export_generation: Optional[str] = None

    def with_presentation_mode(self, mode: PresentationMode) -> "CoreFlowState":
        """Visibility-only transition; all processing lineage is preserved."""
        return replace(self, presentation_mode=mode)

    def with_workflow(self, workflow: Workflow) -> "CoreFlowState":
        """Top-level workflow navigation fails closed to the input stage.

        Processing lineage is workflow-local, so it is not carried into another
        workflow. Returning to the same workflow is a no-op.
        """
        if workflow == self.workflow:
            return self
        return CoreFlowState(workflow=workflow, presentation_mode=self.presentation_mode)

    def with_source(self, generation: str) -> "CoreFlowState":
        """A new/edited source invalidates every downstream generation."""
        if not generation:
            raise ValueError("source generation is required")
        return replace(
            self,
            stage=Stage.ADD,
            source_generation=generation,
            processed_generation=None,
            reviewed_generation=None,
            export_generation=None,
        )

    def with_processed_result(self, generation: str) -> "CoreFlowState":
        """Bind a valid processing result to the current source and enter review."""
        if self.source_generation is None or generation != self.source_generation:
            raise ValueError("processed result must match current source generation")
        return replace(
            self,
            stage=Stage.REVIEW,
            processed_generation=generation,
            reviewed_generation=None,
            export_generation=None,
        )

    def invalidate_for_processing_change(self) -> "CoreFlowState":
        """Profile/threshold changes that affect processing fail closed to Add."""
        return replace(
            self,
            stage=Stage.ADD,
            processed_generation=None,
            reviewed_generation=None,
            export_generation=None,
        )

    def with_presentation_only_change(self) -> "CoreFlowState":
        """Explicit no-op for settings that do not affect processing."""
        return self

    def complete_review(self) -> "CoreFlowState":
        """Enter Download only when review is for the current processing lineage."""
        generation = self.processed_generation
        if generation is None or generation != self.source_generation:
            raise ValueError("current processing lineage is not reviewable")
        return replace(
            self,
            stage=Stage.DOWNLOAD,
            reviewed_generation=generation,
            export_generation=generation,
        )

    @property
    def export_is_current(self) -> bool:
        generation = self.source_generation
        return (
            generation is not None
            and self.stage == Stage.DOWNLOAD
            and self.processed_generation == generation
            and self.reviewed_generation == generation
            and self.export_generation == generation
        )


def recommended_download(source_kind: str, eligible_outputs: Sequence[str]) -> Optional[str]:
    """Choose visual priority only from already-eligible cleaned outputs.

    Values are logical existing-output identities, not new output formats.
    Sensitive/secondary outputs such as the Scrub Key never become the dominant
    recommended download merely because no cleaned document is eligible.
    """
    eligible = tuple(eligible_outputs)
    preference = {
        "docx": ("cleaned_docx", "cleaned_txt"),
        "txt": ("cleaned_txt",),
        "text": ("cleaned_txt",),
        "pdf": ("cleaned_pdf", "cleaned_docx", "cleaned_txt"),
    }.get(source_kind.lower(), ())
    for candidate in preference:
        if candidate in eligible:
            return candidate
    return None
