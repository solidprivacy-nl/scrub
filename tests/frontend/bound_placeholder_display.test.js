"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");

const Core = require(path.resolve(
  __dirname,
  "../../frontend/processed_text_selection_component/component_core.js",
));

function test(name, callback) {
  try {
    callback();
    process.stdout.write(`ok - ${name}\n`);
  } catch (error) {
    process.stderr.write(`not ok - ${name}\n`);
    throw error;
  }
}

const binding = "BSK732WYQ424ZIEQ6";
const automatic = `[LOCATIE_${binding}_02]`;
const manual = `[EMAIL_${binding}_HANDMATIG_03]`;

test("strict bound tokens receive compact aliases", function () {
  assert.equal(Core.compactBoundPlaceholderDisplay(automatic), "[LOCATIE_02]");
  assert.equal(Core.compactBoundPlaceholderDisplay(manual), "[EMAIL_H_03]");
});

test("legacy, malformed and free values remain unchanged", function () {
  [
    "[LOCATIE_02]",
    "[LOCATIE_BSK732WYQ424ZIEQ6]",
    "[LOCATIE_bsk732wyq424zieq6_02]",
    "[DRAFT]",
    "vrije vervangtekst",
  ].forEach(function (value) {
    assert.equal(Core.compactBoundPlaceholderDisplay(value), value);
  });
});

test("display segments preserve full source coordinates", function () {
  const text = `A😀 ${automatic} daarna ${manual}.`;
  const segments = Core.buildDisplayTextSegments(text, []);
  assert.equal(segments.map((segment) => segment.text).join(""), text);
  assert.equal(
    segments.map((segment) => segment.display_text).join(""),
    "A😀 [LOCATIE_02] daarna [EMAIL_H_03].",
  );
  const compact = segments.filter((segment) => segment.compacted);
  assert.deepEqual(compact.map((segment) => segment.text), [automatic, manual]);
  assert.equal(compact.every((segment) => segment.protected), true);
});

test("offset mapping after a compact token uses the source token length", function () {
  const text = `A ${automatic} einde`;
  const segments = Core.buildDisplayTextSegments(text, []);
  const trailingIndex = segments.findIndex((segment) => segment.text === " einde");
  assert.notEqual(trailingIndex, -1);
  assert.equal(
    Core.utf16OffsetFromDisplaySegments(segments, trailingIndex, 1),
    `A ${automatic} `.length,
  );
});

test("interior compact-token offsets remain inside the protected source span", function () {
  const text = `A ${automatic} Z`;
  const segments = Core.buildDisplayTextSegments(text, []);
  const tokenIndex = segments.findIndex((segment) => segment.compacted);
  const token = segments[tokenIndex];
  const mapped = Core.utf16OffsetFromDisplaySegments(token ? segments : [], tokenIndex, 3);
  assert.ok(mapped > token.start_utf16);
  assert.ok(mapped < token.end_utf16);
  assert.equal(token.protected, true);
});

test("hidden visual markers do not expose compact placeholders to selection", function () {
  const text = `A ${automatic} Z`;
  const segments = Core.buildDisplayTextSegments(text, []);
  const protectedSpans = Core.protectedSpansFromDisplaySegments(segments);
  const token = segments.find((segment) => segment.compacted);
  assert.deepEqual(protectedSpans, [[token.start_utf16, token.end_utf16]]);
  assert.equal(
    Core.selectionFromOffsets(text, protectedSpans, token.start_utf16, token.end_utf16)
      .intersects_marked_content,
    true,
  );
});

process.stdout.write("bound placeholder display frontend tests passed\n");
