(function (global) {
  "use strict";

  const Bridge = global.SolidPrivacyStreamlitBridge;
  const Core = global.SolidPrivacySelectionCore;
  if (!Bridge || !Core) {
    throw new Error("SolidPrivacy component support files are missing");
  }

  const sourcePane = document.getElementById("sourcePane");
  const processedPane = document.getElementById("processedPane");
  const processedLegend = document.getElementById("processedLegend");
  const maskSelectionButton = document.getElementById("maskSelectionButton");
  const contextMenu = document.getElementById("contextMenu");
  const statusRegion = document.getElementById("statusRegion");

  let currentArgs = {};
  let processedText = "";
  let highlightSpans = [];
  let currentSelection = null;
  let lastMenuPosition = { x: 16, y: 16 };
  let lastRenderedInspectionToken = "";
  let isSyncing = false;

  function clearElement(element) {
    element.replaceChildren();
  }

  function appendSafeText(element, text) {
    element.appendChild(document.createTextNode(Core.asText(text)));
  }

  function renderPlainText(element, text) {
    clearElement(element);
    appendSafeText(element, text);
  }

  function renderProcessedText(text, spans) {
    clearElement(processedPane);
    Core.buildTextSegments(text, spans).forEach(function (segment) {
      if (segment.marked) {
        const marker = document.createElement("mark");
        marker.className = "sp-highlight";
        marker.setAttribute("aria-label", "gemarkeerde vervanging");
        marker.dataset.startUtf16 = String(segment.start_utf16);
        marker.dataset.endUtf16 = String(segment.end_utf16);
        appendSafeText(marker, segment.text);
        processedPane.appendChild(marker);
      } else {
        appendSafeText(processedPane, segment.text);
      }
    });
  }

  function getScrollRatio(element) {
    return Core.scrollRatio(element.scrollTop, element.scrollHeight, element.clientHeight);
  }

  function setScrollRatio(element, ratio) {
    element.scrollTop = Core.scrollTopForRatio(ratio, element.scrollHeight, element.clientHeight);
  }

  function syncScroll(fromPane, toPane) {
    if (isSyncing) {
      return;
    }
    isSyncing = true;
    global.requestAnimationFrame(function () {
      setScrollRatio(toPane, getScrollRatio(fromPane));
      isSyncing = false;
    });
  }

  function nodeWithin(rootElement, node) {
    if (!rootElement || !node) {
      return false;
    }
    const candidate = node.nodeType === Node.TEXT_NODE ? node.parentNode : node;
    return node === rootElement || rootElement.contains(candidate);
  }

  function domUtf16Offset(rootElement, container, offset) {
    if (!nodeWithin(rootElement, container)) {
      throw new Error("selection endpoint is outside processed text");
    }
    const range = document.createRange();
    range.selectNodeContents(rootElement);
    range.setEnd(container, offset);
    return range.toString().length;
  }

  function readProcessedSelection() {
    const selection = global.getSelection();
    if (!selection || selection.rangeCount !== 1 || selection.isCollapsed) {
      return null;
    }
    const range = selection.getRangeAt(0);
    if (!nodeWithin(processedPane, range.startContainer) || !nodeWithin(processedPane, range.endContainer)) {
      return null;
    }
    let start;
    let end;
    try {
      start = domUtf16Offset(processedPane, range.startContainer, range.startOffset);
      end = domUtf16Offset(processedPane, range.endContainer, range.endOffset);
    } catch (_error) {
      return null;
    }
    return Core.selectionFromOffsets(processedText, highlightSpans, start, end);
  }

  function updateSelectionState() {
    currentSelection = readProcessedSelection();
    maskSelectionButton.disabled = !currentSelection || currentSelection.intersects_marked_content;
    if (!currentSelection) {
      statusRegion.textContent = "";
    } else if (currentSelection.intersects_marked_content) {
      statusRegion.textContent = "De selectie overlapt met een bestaande maskering.";
    } else {
      statusRegion.textContent = `“${currentSelection.text}” geselecteerd`;
    }
  }

  function closeMenu(options) {
    contextMenu.hidden = true;
    clearElement(contextMenu);
    if (options && options.restoreFocus) {
      processedPane.focus();
    }
  }

  function menuItems() {
    return Array.from(contextMenu.querySelectorAll('[role="menuitem"]:not([aria-disabled="true"])'));
  }

  function focusMenuItem(index) {
    const items = menuItems();
    if (!items.length) {
      return;
    }
    const bounded = ((index % items.length) + items.length) % items.length;
    items[bounded].focus();
  }

  function positionMenu(x, y) {
    contextMenu.hidden = false;
    contextMenu.style.left = "0px";
    contextMenu.style.top = "0px";
    const rect = contextMenu.getBoundingClientRect();
    const position = Core.clampMenuPosition(
      x,
      y,
      rect.width,
      rect.height,
      global.innerWidth,
      global.innerHeight,
      8,
    );
    contextMenu.style.left = `${position.x}px`;
    contextMenu.style.top = `${position.y}px`;
    lastMenuPosition = position;
  }

  function addSummary(text) {
    const summary = document.createElement("div");
    summary.className = "sp-menu-summary";
    summary.textContent = text;
    contextMenu.appendChild(summary);
  }

  function addMenuButton(label, callback, options) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "sp-menu-item";
    button.setAttribute("role", "menuitem");
    button.textContent = label;
    if (options && options.disabled) {
      button.setAttribute("aria-disabled", "true");
      button.disabled = true;
    }
    button.addEventListener("click", function () {
      if (!button.disabled) {
        callback();
      }
    });
    contextMenu.appendChild(button);
    return button;
  }

  function addWarning(text) {
    const warning = document.createElement("div");
    warning.className = "sp-menu-warning";
    warning.textContent = text;
    contextMenu.appendChild(warning);
  }

  function inspectionToken(inspectionResult) {
    const result = inspectionResult || {};
    return String(result.inspection_id || result.event_id || "");
  }

  function inspectionMatchesSelection(inspectionResult) {
    const resultText = String((inspectionResult && inspectionResult.selection_text) || "");
    return !currentSelection || !resultText || resultText === currentSelection.text;
  }

  function isInspectableResult(inspectionResult) {
    const status = String((inspectionResult && inspectionResult.status) || "");
    return Boolean(inspectionToken(inspectionResult)) &&
      ["ready", "confirmation_required", "blocked"].includes(status) &&
      inspectionMatchesSelection(inspectionResult);
  }

  function emitInspectEvent() {
    if (!currentSelection || currentSelection.intersects_marked_content) {
      statusRegion.textContent = "Selecteer een ongemaskeerde waarde in de verwerkte tekst.";
      closeMenu({ restoreFocus: true });
      return;
    }
    const event = Core.buildInspectEvent(
      currentArgs,
      currentSelection,
      {
        source_scroll_ratio: getScrollRatio(sourcePane),
        processed_scroll_ratio: getScrollRatio(processedPane),
      },
      Core.makeEventId("inspect", global.crypto),
    );
    statusRegion.textContent = "Selectie wordt veilig gecontroleerd…";
    closeMenu();
    Bridge.setComponentValue(event);
  }

  function emitCommitIntent(typeKey, inspectionResult) {
    const event = Core.buildCommitEvent(
      inspectionResult,
      typeKey,
      Core.makeEventId("commit", global.crypto),
    );
    statusRegion.textContent = "Maskeringskeuze is als niet-muterend intent-event verstuurd.";
    closeMenu();
    Bridge.setComponentValue(event);
  }

  function renderInspectMenu(x, y) {
    clearElement(contextMenu);
    if (!currentSelection) {
      addSummary("Selecteer eerst een waarde in Verwerkte tekst.");
      addMenuButton("Sluiten", function () {
        closeMenu({ restoreFocus: true });
      });
    } else if (currentSelection.intersects_marked_content) {
      addSummary("Deze selectie overlapt met een bestaande maskering.");
      addMenuButton("Sluiten", function () {
        closeMenu({ restoreFocus: true });
      });
    } else {
      addSummary(`“${currentSelection.text}” geselecteerd`);
      addMenuButton("Selectie veilig inspecteren", emitInspectEvent);
    }
    positionMenu(x, y);
    focusMenuItem(0);
  }

  function renderConfirmationMenu(typeKey, inspectionResult, x, y) {
    clearElement(contextMenu);
    const label = Core.QUICK_TYPE_LABELS[typeKey];
    const count = Number(inspectionResult.occurrence_count || 0);
    addSummary(`“${inspectionResult.selection_text || "selectie"}” — ${count} exacte voorkomens`);
    addWarning(`Alle ${count} exacte voorkomens worden gemaskeerd als ${label}.`);
    addMenuButton(`Bevestig alle ${count} voorkomens`, function () {
      emitCommitIntent(typeKey, inspectionResult);
    });
    addMenuButton("Terug", function () {
      renderInspectionResultMenu(inspectionResult, x, y);
    });
    positionMenu(x, y);
    focusMenuItem(0);
  }

  function renderInspectionResultMenu(inspectionResult, x, y) {
    clearElement(contextMenu);
    const status = String(inspectionResult.status || "blocked");
    const count = Number(inspectionResult.occurrence_count || 0);
    const selectionText = String(
      inspectionResult.selection_text || (currentSelection && currentSelection.text) || "selectie",
    );
    addSummary(`“${selectionText}” — ${inspectionResult.message || `${count} exacte voorkomens`}`);

    if (status === "blocked") {
      addWarning(inspectionResult.message || "Deze selectie kon niet veilig worden toegevoegd.");
      addMenuButton("Sluiten", function () {
        closeMenu({ restoreFocus: true });
      });
    } else {
      const allowed = Array.isArray(inspectionResult.allowed_types)
        ? inspectionResult.allowed_types
        : [];
      allowed.forEach(function (typeKey) {
        if (!Object.prototype.hasOwnProperty.call(Core.QUICK_TYPE_LABELS, typeKey)) {
          return;
        }
        const label = Core.QUICK_TYPE_LABELS[typeKey];
        const buttonLabel = count === 1
          ? `Masker als ${label}`
          : `Masker alle ${count} exacte voorkomens als ${label}`;
        addMenuButton(buttonLabel, function () {
          if (status === "confirmation_required") {
            renderConfirmationMenu(typeKey, inspectionResult, x, y);
          } else {
            emitCommitIntent(typeKey, inspectionResult);
          }
        });
      });
      if (!allowed.length) {
        addWarning("De server heeft geen toegestane maskeringstypen teruggegeven.");
      }
    }
    positionMenu(x, y);
    focusMenuItem(0);
  }

  function openMenuForCurrentState(x, y) {
    const inspectionResult = currentArgs.inspection_result || {};
    if (isInspectableResult(inspectionResult)) {
      renderInspectionResultMenu(inspectionResult, x, y);
    } else {
      renderInspectMenu(x, y);
    }
  }

  function render(args) {
    const sourceScroll = getScrollRatio(sourcePane);
    const processedScroll = getScrollRatio(processedPane);
    currentArgs = args || {};
    processedText = Core.asText(currentArgs.processed_text);
    highlightSpans = Core.normalizeUtf16Spans(processedText, currentArgs.highlight_spans);

    renderPlainText(sourcePane, currentArgs.source_text);
    renderProcessedText(processedText, highlightSpans);
    processedLegend.textContent = highlightSpans.length
      ? "Geel = vervangen of gemaskeerde waarde"
      : "Verwerkte tekst";

    const restoreSource = currentArgs.restore_source_scroll_ratio;
    const restoreProcessed = currentArgs.restore_processed_scroll_ratio;
    global.requestAnimationFrame(function () {
      setScrollRatio(
        sourcePane,
        Number.isFinite(Number(restoreSource)) ? Number(restoreSource) : sourceScroll,
      );
      setScrollRatio(
        processedPane,
        Number.isFinite(Number(restoreProcessed)) ? Number(restoreProcessed) : processedScroll,
      );
    });

    updateSelectionState();
    const inspectionResult = currentArgs.inspection_result || {};
    if (inspectionResult.message) {
      statusRegion.textContent = String(inspectionResult.message);
    }
    const token = inspectionToken(inspectionResult);
    if (token && token !== lastRenderedInspectionToken && isInspectableResult(inspectionResult)) {
      lastRenderedInspectionToken = token;
      global.requestAnimationFrame(function () {
        renderInspectionResultMenu(
          inspectionResult,
          lastMenuPosition.x,
          lastMenuPosition.y,
        );
      });
    }
    Bridge.setFrameHeight(500);
  }

  sourcePane.addEventListener("scroll", function () {
    syncScroll(sourcePane, processedPane);
  });
  processedPane.addEventListener("scroll", function () {
    syncScroll(processedPane, sourcePane);
  });

  document.addEventListener("selectionchange", function () {
    updateSelectionState();
  });

  processedPane.addEventListener("contextmenu", function (event) {
    updateSelectionState();
    if (!currentSelection || currentSelection.intersects_marked_content) {
      return;
    }
    event.preventDefault();
    openMenuForCurrentState(event.clientX, event.clientY);
  });

  processedPane.addEventListener("keydown", function (event) {
    if ((event.shiftKey && event.key === "F10") || event.key === "ContextMenu") {
      updateSelectionState();
      if (currentSelection && !currentSelection.intersects_marked_content) {
        event.preventDefault();
        const rect = processedPane.getBoundingClientRect();
        openMenuForCurrentState(rect.left + Math.min(40, rect.width / 2), rect.top + 40);
      }
    }
  });

  maskSelectionButton.addEventListener("click", function () {
    updateSelectionState();
    const rect = maskSelectionButton.getBoundingClientRect();
    openMenuForCurrentState(rect.left, rect.bottom + 6);
  });

  contextMenu.addEventListener("keydown", function (event) {
    const items = menuItems();
    const currentIndex = items.indexOf(document.activeElement);
    if (event.key === "ArrowDown") {
      event.preventDefault();
      focusMenuItem(currentIndex + 1);
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      focusMenuItem(currentIndex - 1);
    } else if (event.key === "Home") {
      event.preventDefault();
      focusMenuItem(0);
    } else if (event.key === "End") {
      event.preventDefault();
      focusMenuItem(items.length - 1);
    } else if (event.key === "Escape") {
      event.preventDefault();
      closeMenu({ restoreFocus: true });
    }
  });

  document.addEventListener("mousedown", function (event) {
    if (!contextMenu.hidden && !contextMenu.contains(event.target)) {
      closeMenu();
    }
  });

  global.addEventListener("blur", function () {
    closeMenu();
  });

  Bridge.onRender(function (detail) {
    render(detail.args || {});
  });
  Bridge.setComponentReady();
  Bridge.setFrameHeight(500);
})(window);
