(function (global, factory) {
  "use strict";

  const api = factory();
  if (typeof module !== "undefined" && module.exports) {
    module.exports = api;
  }
  global.SolidPrivacySelectionCore = api;
})(typeof window !== "undefined" ? window : globalThis, function () {
  "use strict";

  const EVENT_ID_PATTERN = /^[A-Za-z0-9_-]{16,80}$/;
  const BOUND_PLACEHOLDER_PATTERN = /^\[([A-Z][A-Z0-9_]*?)_(B[A-Z2-7]{16})(?:_(HANDMATIG))?_(\d{2,})\]$/;
  const BOUND_PLACEHOLDER_GLOBAL_PATTERN = /\[([A-Z][A-Z0-9_]*?)_(B[A-Z2-7]{16})(?:_(HANDMATIG))?_(\d{2,})\]/g;
  const QUICK_TYPE_LABELS = Object.freeze({
    person: "Persoon",
    organization: "Organisatie",
    location: "Adres of locatie",
    email: "E-mailadres",
    phone: "Telefoonnummer",
    date_time: "Datum of tijd",
    reference: "Nummer of referentie",
    other: "Overige waarde",
  });

  function asText(value) {
    return value == null ? "" : String(value);
  }

  function isHighSurrogate(code) {
    return code >= 0xd800 && code <= 0xdbff;
  }

  function isLowSurrogate(code) {
    return code >= 0xdc00 && code <= 0xdfff;
  }

  function isUtf16Boundary(text, offset) {
    const value = asText(text);
    if (!Number.isInteger(offset) || offset < 0 || offset > value.length) {
      return false;
    }
    if (offset === 0 || offset === value.length) {
      return true;
    }
    return !(
      isHighSurrogate(value.charCodeAt(offset - 1)) &&
      isLowSurrogate(value.charCodeAt(offset))
    );
  }

  function normalizeUtf16Spans(text, spans) {
    const value = asText(text);
    const normalized = [];
    let previousEnd = 0;
    (Array.isArray(spans) ? spans : []).forEach(function (span) {
      if (!Array.isArray(span) || span.length !== 2) {
        throw new Error("highlight span must contain start and end");
      }
      const start = span[0];
      const end = span[1];
      if (
        !Number.isInteger(start) ||
        !Number.isInteger(end) ||
        start < 0 ||
        end <= start ||
        end > value.length
      ) {
        throw new Error("highlight span falls outside processed text");
      }
      if (!isUtf16Boundary(value, start) || !isUtf16Boundary(value, end)) {
        throw new Error("highlight span splits a surrogate pair");
      }
      if (normalized.length > 0 && start < previousEnd) {
        throw new Error("highlight spans must be sorted and non-overlapping");
      }
      normalized.push([start, end]);
      previousEnd = end;
    });
    return normalized;
  }

  function buildTextSegments(text, spans) {
    const value = asText(text);
    const normalized = normalizeUtf16Spans(value, spans);
    const segments = [];
    let cursor = 0;
    normalized.forEach(function (span) {
      const start = span[0];
      const end = span[1];
      if (start > cursor) {
        segments.push({
          text: value.slice(cursor, start),
          marked: false,
          start_utf16: cursor,
          end_utf16: start,
        });
      }
      segments.push({
        text: value.slice(start, end),
        marked: true,
        start_utf16: start,
        end_utf16: end,
      });
      cursor = end;
    });
    if (cursor < value.length || segments.length === 0) {
      segments.push({
        text: value.slice(cursor),
        marked: false,
        start_utf16: cursor,
        end_utf16: value.length,
      });
    }
    return segments;
  }

  function compactBoundPlaceholderDisplay(value) {
    const text = asText(value);
    const match = text.match(BOUND_PLACEHOLDER_PATTERN);
    if (!match) {
      return text;
    }
    const manual = match[3] ? "_H" : "";
    return `[${match[1]}${manual}_${match[4]}]`;
  }

  function findBoundPlaceholderSpans(text) {
    const value = asText(text);
    const spans = [];
    const pattern = new RegExp(BOUND_PLACEHOLDER_GLOBAL_PATTERN.source, "g");
    let match = pattern.exec(value);
    while (match) {
      spans.push({
        start_utf16: match.index,
        end_utf16: match.index + match[0].length,
        text: match[0],
        display_text: compactBoundPlaceholderDisplay(match[0]),
      });
      match = pattern.exec(value);
    }
    return spans;
  }

  function rangesOverlap(firstStart, firstEnd, secondStart, secondEnd) {
    return firstStart < secondEnd && secondStart < firstEnd;
  }

  function buildDisplayTextSegments(text, spans) {
    const value = asText(text);
    const highlights = normalizeUtf16Spans(value, spans);
    const placeholders = findBoundPlaceholderSpans(value);
    const boundaries = new Set([0, value.length]);
    highlights.forEach(function (span) {
      boundaries.add(span[0]);
      boundaries.add(span[1]);
    });
    placeholders.forEach(function (placeholder) {
      boundaries.add(placeholder.start_utf16);
      boundaries.add(placeholder.end_utf16);
    });
    const ordered = Array.from(boundaries).sort(function (first, second) {
      return first - second;
    });
    const segments = [];
    for (let index = 0; index < ordered.length - 1; index += 1) {
      const start = ordered[index];
      const end = ordered[index + 1];
      if (end <= start) {
        continue;
      }
      const sourceText = value.slice(start, end);
      const placeholder = placeholders.find(function (candidate) {
        return candidate.start_utf16 === start && candidate.end_utf16 === end;
      });
      const highlighted = highlights.some(function (highlight) {
        return rangesOverlap(start, end, highlight[0], highlight[1]);
      });
      const displayText = placeholder ? placeholder.display_text : sourceText;
      segments.push({
        text: sourceText,
        display_text: displayText,
        marked: highlighted,
        protected: highlighted || Boolean(placeholder),
        compacted: Boolean(placeholder) && displayText !== sourceText,
        full_placeholder: placeholder ? placeholder.text : "",
        start_utf16: start,
        end_utf16: end,
      });
    }
    if (!segments.length) {
      segments.push({
        text: "",
        display_text: "",
        marked: false,
        protected: false,
        compacted: false,
        full_placeholder: "",
        start_utf16: 0,
        end_utf16: 0,
      });
    }
    return segments;
  }

  function protectedSpansFromDisplaySegments(segments) {
    const merged = [];
    (Array.isArray(segments) ? segments : []).forEach(function (segment) {
      if (!segment || !segment.protected) {
        return;
      }
      const start = Number(segment.start_utf16);
      const end = Number(segment.end_utf16);
      if (!Number.isInteger(start) || !Number.isInteger(end) || end <= start) {
        throw new Error("protected display segment has invalid source offsets");
      }
      const previous = merged[merged.length - 1];
      if (previous && start <= previous[1]) {
        previous[1] = Math.max(previous[1], end);
      } else {
        merged.push([start, end]);
      }
    });
    return merged;
  }

  function utf16OffsetFromDisplaySegments(segments, targetSegmentIndex, localOffset) {
    if (!Array.isArray(segments) || !Number.isInteger(targetSegmentIndex)) {
      throw new Error("invalid display segment target");
    }
    if (targetSegmentIndex < 0 || targetSegmentIndex >= segments.length) {
      throw new Error("display segment target is outside the component");
    }
    const segment = segments[targetSegmentIndex] || {};
    const displayText = asText(segment.display_text);
    if (!Number.isInteger(localOffset) || localOffset < 0 || localOffset > displayText.length) {
      throw new Error("local display offset is invalid");
    }
    if (!isUtf16Boundary(displayText, localOffset)) {
      throw new Error("local display offset splits a surrogate pair");
    }
    const start = Number(segment.start_utf16);
    const end = Number(segment.end_utf16);
    if (!Number.isInteger(start) || !Number.isInteger(end) || end < start) {
      throw new Error("display segment has invalid source offsets");
    }
    if (!segment.compacted) {
      return start + localOffset;
    }
    if (localOffset === 0 || displayText.length === 0) {
      return start;
    }
    if (localOffset === displayText.length) {
      return end;
    }
    const sourceLength = end - start;
    const proportional = Math.floor((localOffset / displayText.length) * sourceLength);
    return Math.min(end - 1, Math.max(start + 1, start + proportional));
  }

  function intersectsMarkedSpan(start, end, spans) {
    return (Array.isArray(spans) ? spans : []).some(function (span) {
      return rangesOverlap(start, end, Number(span[0]), Number(span[1]));
    });
  }

  function trimOuterWhitespace(text, start, end) {
    const value = asText(text);
    if (!Number.isInteger(start) || !Number.isInteger(end) || start < 0 || end > value.length || end <= start) {
      return null;
    }
    let trimmedStart = start;
    let trimmedEnd = end;
    const leading = value.slice(trimmedStart, trimmedEnd).match(/^\s+/u);
    if (leading) {
      trimmedStart += leading[0].length;
    }
    const trailing = value.slice(trimmedStart, trimmedEnd).match(/\s+$/u);
    if (trailing) {
      trimmedEnd -= trailing[0].length;
    }
    if (trimmedEnd <= trimmedStart) {
      return null;
    }
    if (!isUtf16Boundary(value, trimmedStart) || !isUtf16Boundary(value, trimmedEnd)) {
      return null;
    }
    return {
      text: value.slice(trimmedStart, trimmedEnd),
      start_utf16: trimmedStart,
      end_utf16: trimmedEnd,
    };
  }

  function utf16OffsetFromSegments(segments, targetSegmentIndex, localOffset) {
    if (!Array.isArray(segments) || !Number.isInteger(targetSegmentIndex)) {
      throw new Error("invalid text segment target");
    }
    if (targetSegmentIndex < 0 || targetSegmentIndex >= segments.length) {
      throw new Error("text segment target is outside the component");
    }
    let offset = 0;
    segments.forEach(function (segment, index) {
      const text = asText(segment.text);
      if (index < targetSegmentIndex) {
        offset += text.length;
      }
    });
    const targetText = asText(segments[targetSegmentIndex].text);
    if (!Number.isInteger(localOffset) || localOffset < 0 || localOffset > targetText.length) {
      throw new Error("local text offset is invalid");
    }
    if (!isUtf16Boundary(targetText, localOffset)) {
      throw new Error("local text offset splits a surrogate pair");
    }
    return offset + localOffset;
  }

  function selectionFromOffsets(processedText, highlightSpans, start, end) {
    const value = asText(processedText);
    if (!isUtf16Boundary(value, start) || !isUtf16Boundary(value, end) || end <= start) {
      return null;
    }
    const trimmed = trimOuterWhitespace(value, start, end);
    if (!trimmed) {
      return null;
    }
    const normalizedSpans = normalizeUtf16Spans(value, highlightSpans);
    return {
      text: trimmed.text,
      start_utf16: trimmed.start_utf16,
      end_utf16: trimmed.end_utf16,
      intersects_marked_content: intersectsMarkedSpan(
        trimmed.start_utf16,
        trimmed.end_utf16,
        normalizedSpans,
      ),
    };
  }

  function makeEventId(prefix, cryptoObject, nowValue) {
    const safePrefix = asText(prefix).replace(/[^A-Za-z0-9_-]/g, "_").slice(0, 20) || "event";
    let randomPart = "";
    if (cryptoObject && typeof cryptoObject.getRandomValues === "function") {
      const bytes = new Uint8Array(12);
      cryptoObject.getRandomValues(bytes);
      randomPart = Array.from(bytes, function (value) {
        return value.toString(16).padStart(2, "0");
      }).join("");
    } else {
      const numericNow = Number.isFinite(nowValue) ? nowValue : Date.now();
      randomPart = `${numericNow.toString(36)}_${Math.random().toString(36).slice(2, 14)}`;
    }
    const candidate = `${safePrefix}_${randomPart}`.replace(/[^A-Za-z0-9_-]/g, "_").slice(0, 80);
    return candidate.length >= 16 ? candidate : `${candidate}_0000000000000000`.slice(0, 16);
  }

  function buildInspectEvent(args, selection, uiState, eventId) {
    const contract = (args && args.component_contract) || {};
    const value = {
      schema_version: Number(contract.schema_version || 1),
      action: asText(contract.inspect_action || "inspect_selection"),
      event_id: asText(eventId),
      document_scope_key: asText(args && args.document_scope_key),
      processed_text_hash: asText(args && args.processed_text_hash),
      selection: {
        text: asText(selection && selection.text),
        start_utf16: Number(selection && selection.start_utf16),
        end_utf16: Number(selection && selection.end_utf16),
        intersects_marked_content: Boolean(selection && selection.intersects_marked_content),
      },
      ui_state: {
        source_scroll_ratio: Number((uiState && uiState.source_scroll_ratio) || 0),
        processed_scroll_ratio: Number((uiState && uiState.processed_scroll_ratio) || 0),
      },
    };
    if (!EVENT_ID_PATTERN.test(value.event_id)) {
      throw new Error("generated event ID does not match the contract");
    }
    return value;
  }

  function buildCommitEvent(inspectionResult, requestedType, eventId) {
    const result = inspectionResult || {};
    const typeKey = asText(requestedType);
    if (!Object.prototype.hasOwnProperty.call(QUICK_TYPE_LABELS, typeKey)) {
      throw new Error("unknown quick type");
    }
    const value = {
      schema_version: 1,
      action: "commit_manual_mask",
      event_id: asText(eventId),
      inspection_id: asText(result.inspection_id),
      requested_type: typeKey,
      requested_scope: asText(result.requested_scope || "all_exact"),
      confirmation_token: asText(result.confirmation_token || ""),
    };
    if (!EVENT_ID_PATTERN.test(value.event_id)) {
      throw new Error("generated event ID does not match the contract");
    }
    if (!value.inspection_id) {
      throw new Error("server inspection ID is required");
    }
    return value;
  }

  function scrollRatio(scrollTop, scrollHeight, clientHeight) {
    const maximum = Math.max(0, Number(scrollHeight) - Number(clientHeight));
    if (maximum <= 0) {
      return 0;
    }
    const ratio = Number(scrollTop) / maximum;
    return Math.min(1, Math.max(0, Number.isFinite(ratio) ? ratio : 0));
  }

  function scrollTopForRatio(ratio, scrollHeight, clientHeight) {
    const maximum = Math.max(0, Number(scrollHeight) - Number(clientHeight));
    const safeRatio = Math.min(1, Math.max(0, Number.isFinite(Number(ratio)) ? Number(ratio) : 0));
    return safeRatio * maximum;
  }

  function clampMenuPosition(x, y, menuWidth, menuHeight, viewportWidth, viewportHeight, margin) {
    const safeMargin = Number.isFinite(Number(margin)) ? Math.max(0, Number(margin)) : 8;
    const maximumX = Math.max(safeMargin, Number(viewportWidth) - Number(menuWidth) - safeMargin);
    const maximumY = Math.max(safeMargin, Number(viewportHeight) - Number(menuHeight) - safeMargin);
    return {
      x: Math.min(maximumX, Math.max(safeMargin, Number(x) || 0)),
      y: Math.min(maximumY, Math.max(safeMargin, Number(y) || 0)),
    };
  }

  return Object.freeze({
    EVENT_ID_PATTERN: EVENT_ID_PATTERN,
    BOUND_PLACEHOLDER_PATTERN: BOUND_PLACEHOLDER_PATTERN,
    QUICK_TYPE_LABELS: QUICK_TYPE_LABELS,
    asText: asText,
    isUtf16Boundary: isUtf16Boundary,
    normalizeUtf16Spans: normalizeUtf16Spans,
    buildTextSegments: buildTextSegments,
    compactBoundPlaceholderDisplay: compactBoundPlaceholderDisplay,
    findBoundPlaceholderSpans: findBoundPlaceholderSpans,
    buildDisplayTextSegments: buildDisplayTextSegments,
    protectedSpansFromDisplaySegments: protectedSpansFromDisplaySegments,
    utf16OffsetFromDisplaySegments: utf16OffsetFromDisplaySegments,
    rangesOverlap: rangesOverlap,
    intersectsMarkedSpan: intersectsMarkedSpan,
    trimOuterWhitespace: trimOuterWhitespace,
    utf16OffsetFromSegments: utf16OffsetFromSegments,
    selectionFromOffsets: selectionFromOffsets,
    makeEventId: makeEventId,
    buildInspectEvent: buildInspectEvent,
    buildCommitEvent: buildCommitEvent,
    scrollRatio: scrollRatio,
    scrollTopForRatio: scrollTopForRatio,
    clampMenuPosition: clampMenuPosition,
  });
});
