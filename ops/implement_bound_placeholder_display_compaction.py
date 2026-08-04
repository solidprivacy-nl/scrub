from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Required anchor missing in {path}: {old[:120]!r}")
    target.write_text(text.replace(old, new, 1), encoding="utf-8")


patch(
    "frontend/processed_text_selection_component/component.js",
    """  let processedText = \"\";\n  let highlightSpans = [];\n  let currentSelection = null;\n""",
    """  let processedText = \"\";\n  let highlightSpans = [];\n  let renderedProcessedSegments = [];\n  let selectionProtectedSpans = [];\n  let currentSelection = null;\n""",
)

patch(
    "frontend/processed_text_selection_component/component.js",
    """  function renderProcessedText(text, spans) {\n    clearElement(processedPane);\n    Core.buildTextSegments(text, spans).forEach(function (segment) {\n      if (segment.marked) {\n        const marker = document.createElement(\"mark\");\n        marker.className = \"sp-highlight\";\n        marker.setAttribute(\"aria-label\", \"gemarkeerde vervanging\");\n        marker.dataset.startUtf16 = String(segment.start_utf16);\n        marker.dataset.endUtf16 = String(segment.end_utf16);\n        appendSafeText(marker, segment.text);\n        processedPane.appendChild(marker);\n      } else {\n        appendSafeText(processedPane, segment.text);\n      }\n    });\n  }\n""",
    """  function renderProcessedText(text, spans) {\n    clearElement(processedPane);\n    renderedProcessedSegments = Core.buildDisplayTextSegments(text, spans);\n    selectionProtectedSpans = Core.protectedSpansFromDisplaySegments(renderedProcessedSegments);\n    renderedProcessedSegments.forEach(function (segment, index) {\n      const element = document.createElement(segment.marked ? \"mark\" : \"span\");\n      element.className = segment.marked\n        ? \"sp-highlight sp-processed-segment\"\n        : \"sp-processed-segment\";\n      if (segment.compacted) {\n        element.classList.add(\"sp-compact-placeholder\");\n        element.title = `Volledige gebonden placeholder: ${segment.full_placeholder}`;\n        element.setAttribute(\n          \"aria-label\",\n          `Gebonden placeholder, compact weergegeven als ${segment.display_text}`,\n        );\n      } else if (segment.marked) {\n        element.setAttribute(\"aria-label\", \"gemarkeerde vervanging\");\n      }\n      element.dataset.segmentIndex = String(index);\n      element.dataset.startUtf16 = String(segment.start_utf16);\n      element.dataset.endUtf16 = String(segment.end_utf16);\n      appendSafeText(element, segment.display_text);\n      processedPane.appendChild(element);\n    });\n  }\n""",
)

patch(
    "frontend/processed_text_selection_component/component.js",
    """  function domUtf16Offset(rootElement, container, offset) {\n    if (!nodeWithin(rootElement, container)) {\n      throw new Error(\"selection endpoint is outside processed text\");\n    }\n    const range = document.createRange();\n    range.selectNodeContents(rootElement);\n    range.setEnd(container, offset);\n    return range.toString().length;\n  }\n""",
    """  function domUtf16Offset(rootElement, container, offset) {\n    if (!nodeWithin(rootElement, container)) {\n      throw new Error(\"selection endpoint is outside processed text\");\n    }\n    if (container === rootElement) {\n      if (!Number.isInteger(offset) || offset < 0 || offset > rootElement.childNodes.length) {\n        throw new Error(\"selection endpoint is outside processed text\");\n      }\n      if (offset === 0) {\n        return 0;\n      }\n      if (offset >= renderedProcessedSegments.length) {\n        return processedText.length;\n      }\n      return renderedProcessedSegments[offset - 1].end_utf16;\n    }\n    const candidate = container.nodeType === Node.TEXT_NODE ? container.parentElement : container;\n    const segmentElement = candidate && candidate.closest\n      ? candidate.closest(\"[data-segment-index]\")\n      : null;\n    if (!segmentElement || !rootElement.contains(segmentElement)) {\n      throw new Error(\"selection endpoint has no source segment\");\n    }\n    const segmentIndex = Number(segmentElement.dataset.segmentIndex);\n    const range = document.createRange();\n    range.selectNodeContents(segmentElement);\n    range.setEnd(container, offset);\n    return Core.utf16OffsetFromDisplaySegments(\n      renderedProcessedSegments,\n      segmentIndex,\n      range.toString().length,\n    );\n  }\n""",
)

patch(
    "frontend/processed_text_selection_component/component.js",
    """    return Core.selectionFromOffsets(processedText, highlightSpans, start, end);\n""",
    """    return Core.selectionFromOffsets(processedText, selectionProtectedSpans, start, end);\n""",
)

patch(
    "frontend/processed_text_selection_component/component.js",
    """    processedLegend.textContent = highlightSpans.length\n      ? \"Geel = vervangen of gemaskeerde waarde\"\n      : \"Verwerkte tekst\";\n""",
    """    const compactedCount = renderedProcessedSegments.filter(function (segment) {\n      return segment.compacted;\n    }).length;\n    if (highlightSpans.length && compactedCount) {\n      processedLegend.textContent = \"Geel = vervangen; documentcode compact weergegeven\";\n    } else if (highlightSpans.length) {\n      processedLegend.textContent = \"Geel = vervangen of gemaskeerde waarde\";\n    } else if (compactedCount) {\n      processedLegend.textContent = \"Documentcode compact weergegeven\";\n    } else {\n      processedLegend.textContent = \"Verwerkte tekst\";\n    }\n""",
)

patch(
    "side_by_side_review_panel_ui.py",
    """import streamlit.components.v1 as components\n\nfrom processed_text_selection_component import (\n""",
    """import streamlit.components.v1 as components\n\nfrom bound_placeholder_display import build_bound_placeholder_display_segments\nfrom processed_text_selection_component import (\n""",
)

patch(
    "side_by_side_review_panel_ui.py",
    """.sp-side-by-side-highlight-token {\n    background: #fef3c7;\n    border: 1px solid #f59e0b;\n    border-radius: 0.25rem;\n    padding: 0.05rem 0.15rem;\n}\n""",
    """.sp-side-by-side-highlight-token {\n    background: #fef3c7;\n    border: 1px solid #f59e0b;\n    border-radius: 0.25rem;\n    padding: 0.05rem 0.15rem;\n}\n.sp-compact-placeholder {\n    border-bottom: 1px dotted #94a3b8;\n    cursor: help;\n}\n""",
)

patch(
    "side_by_side_review_panel_ui.py",
    '''def _highlighted_processed_inner_html(\n    processed_text: str,\n    highlight_spans: list[tuple[int, int]],\n) -> str:\n    """Return escaped inner HTML for the static fallback processed pane."""\n\n    parts: list[str] = []\n    cursor = 0\n    for start, end in highlight_spans:\n        parts.append(escape(processed_text[cursor:start]))\n        parts.append(\n            '<mark class="sp-side-by-side-highlight-token" aria-label="gemarkeerde vervanging">'\n            f"{escape(processed_text[start:end])}"\n            "</mark>"\n        )\n        cursor = end\n    parts.append(escape(processed_text[cursor:]))\n    return "".join(parts)\n''',
    '''def _highlighted_processed_inner_html(\n    processed_text: str,\n    highlight_spans: list[tuple[int, int]],\n) -> str:\n    """Return lossless compact display HTML for the static fallback pane."""\n\n    parts: list[str] = []\n    for segment in build_bound_placeholder_display_segments(processed_text, highlight_spans):\n        display_text = escape(str(segment["display_text"]))\n        full_placeholder = str(segment["full_placeholder"])\n        compact_attributes = ""\n        compact_class = ""\n        if segment["compacted"]:\n            compact_class = " sp-compact-placeholder"\n            compact_attributes = (\n                f' title="Volledige gebonden placeholder: {escape(full_placeholder)}"'\n                f' aria-label="Gebonden placeholder, compact weergegeven als {display_text}"'\n            )\n        if segment["highlighted"]:\n            parts.append(\n                f'<mark class="sp-side-by-side-highlight-token{compact_class}"'\n                f'{compact_attributes}>{display_text}</mark>'\n            )\n        elif segment["compacted"]:\n            parts.append(\n                f'<span class="sp-compact-placeholder"{compact_attributes}>'\n                f'{display_text}</span>'\n            )\n        else:\n            parts.append(display_text)\n    return "".join(parts)\n''',
)

patch(
    "side_by_side_review_panel_ui.py",
    """    processed_legend = \"Geel = vervangen of gemaskeerde waarde\" if show_markers else \"Verwerkte tekst\"\n""",
    """    compacted = any(\n        segment[\"compacted\"]\n        for segment in build_bound_placeholder_display_segments(processed_text, [])\n    )\n    if show_markers and compacted:\n        processed_legend = \"Geel = vervangen; documentcode compact weergegeven\"\n    elif show_markers:\n        processed_legend = \"Geel = vervangen of gemaskeerde waarde\"\n    elif compacted:\n        processed_legend = \"Documentcode compact weergegeven\"\n    else:\n        processed_legend = \"Verwerkte tekst\"\n""",
)

patch(
    "side_by_side_review_panel_ui.py",
    """    processed_html = (\n        _highlighted_processed_inner_html(processed_text, highlight_spans)\n        if show_markers and highlight_spans\n        else escape(processed_text)\n    )\n""",
    """    processed_html = _highlighted_processed_inner_html(\n        processed_text,\n        highlight_spans if show_markers else [],\n    )\n""",
)

patch(
    "side_by_side_review_panel_ui.py",
    """        \"component_environment_switch\": INTERACTIVE_COMPONENT_ENV,\n        \"pane_height\": SIDE_BY_SIDE_REVIEW_PANE_HEIGHT,\n""",
    """        \"component_environment_switch\": INTERACTIVE_COMPONENT_ENV,\n        \"bound_placeholder_display_compaction\": True,\n        \"bound_placeholder_source_tokens_unchanged\": True,\n        \"bound_placeholder_binding_entropy_changed\": False,\n        \"pane_height\": SIDE_BY_SIDE_REVIEW_PANE_HEIGHT,\n""",
)

(ROOT / "ops/implement_bound_placeholder_display_compaction.py").unlink()
(ROOT / ".github/workflows/bound_placeholder_display_compaction.yml").unlink()
