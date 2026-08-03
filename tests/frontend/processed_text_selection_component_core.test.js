"use strict";

const assert = require("node:assert/strict");
const path = require("node:path");

const corePath = path.resolve(
  __dirname,
  "../../frontend/processed_text_selection_component/component_core.js",
);
const Core = require(corePath);

function test(name, callback) {
  try {
    callback();
    process.stdout.write(`ok - ${name}\n`);
  } catch (error) {
    process.stderr.write(`not ok - ${name}\n`);
    throw error;
  }
}

test("UTF-16 boundaries reject the middle of a surrogate pair", function () {
  const text = "A😀B";
  assert.equal(text.length, 4);
  assert.equal(Core.isUtf16Boundary(text, 0), true);
  assert.equal(Core.isUtf16Boundary(text, 1), true);
  assert.equal(Core.isUtf16Boundary(text, 2), false);
  assert.equal(Core.isUtf16Boundary(text, 3), true);
  assert.equal(Core.isUtf16Boundary(text, 4), true);
});

test("highlight spans and segments use UTF-16 coordinates", function () {
  const text = "A😀BCDEF";
  const spans = Core.normalizeUtf16Spans(text, [[3, 5]]);
  assert.deepEqual(spans, [[3, 5]]);
  assert.deepEqual(Core.buildTextSegments(text, spans), [
    { text: "A😀", marked: false, start_utf16: 0, end_utf16: 3 },
    { text: "BC", marked: true, start_utf16: 3, end_utf16: 5 },
    { text: "DEF", marked: false, start_utf16: 5, end_utf16: 8 },
  ]);
  assert.throws(
    function () {
      Core.normalizeUtf16Spans(text, [[1, 2]]);
    },
    /surrogate pair/,
  );
});

test("segment offsets remain correct after marked text nodes", function () {
  const segments = Core.buildTextSegments("A😀BCDEF", [[3, 5]]);
  assert.equal(Core.utf16OffsetFromSegments(segments, 0, 1), 1);
  assert.equal(Core.utf16OffsetFromSegments(segments, 1, 2), 5);
  assert.equal(Core.utf16OffsetFromSegments(segments, 2, 1), 6);
  assert.throws(
    function () {
      Core.utf16OffsetFromSegments([{ text: "😀" }], 0, 1);
    },
    /surrogate pair/,
  );
});

test("selection trimming adjusts UTF-16 offsets", function () {
  const text = "A😀  SYNTHETIC-ALFA  Z";
  const start = 3;
  const end = text.length - 1;
  const selection = Core.selectionFromOffsets(text, [], start, end);
  assert.deepEqual(selection, {
    text: "SYNTHETIC-ALFA",
    start_utf16: 5,
    end_utf16: 19,
    intersects_marked_content: false,
  });
});

test("selection reports overlap with a marked node", function () {
  const text = "A😀BCDEF";
  assert.deepEqual(Core.selectionFromOffsets(text, [[3, 5]], 4, 7), {
    text: "CDE",
    start_utf16: 4,
    end_utf16: 7,
    intersects_marked_content: true,
  });
  assert.equal(Core.intersectsMarkedSpan(5, 8, [[3, 5]]), false);
  assert.equal(Core.intersectsMarkedSpan(4, 8, [[3, 5]]), true);
});

test("event IDs satisfy the frozen contract with deterministic crypto", function () {
  const fakeCrypto = {
    getRandomValues(bytes) {
      for (let index = 0; index < bytes.length; index += 1) {
        bytes[index] = index;
      }
      return bytes;
    },
  };
  const eventId = Core.makeEventId("inspect", fakeCrypto);
  assert.equal(eventId, "inspect_000102030405060708090a0b");
  assert.match(eventId, Core.EVENT_ID_PATTERN);
});

test("inspect event matches the action-model envelope", function () {
  const event = Core.buildInspectEvent(
    {
      document_scope_key: "0123456789abcdef",
      processed_text_hash: "a".repeat(64),
      component_contract: {
        schema_version: 1,
        inspect_action: "inspect_selection",
      },
    },
    {
      text: "SYNTHETIC-ALFA",
      start_utf16: 4,
      end_utf16: 18,
      intersects_marked_content: false,
    },
    {
      source_scroll_ratio: 0.25,
      processed_scroll_ratio: 0.5,
    },
    "inspect_000102030405060708090a0b",
  );
  assert.deepEqual(event, {
    schema_version: 1,
    action: "inspect_selection",
    event_id: "inspect_000102030405060708090a0b",
    document_scope_key: "0123456789abcdef",
    processed_text_hash: "a".repeat(64),
    selection: {
      text: "SYNTHETIC-ALFA",
      start_utf16: 4,
      end_utf16: 18,
      intersects_marked_content: false,
    },
    ui_state: {
      source_scroll_ratio: 0.25,
      processed_scroll_ratio: 0.5,
    },
  });
});

test("commit intent uses only server inspection data and a quick type", function () {
  const event = Core.buildCommitEvent(
    {
      inspection_id: "inspection_synthetic_0001",
      requested_scope: "all_exact",
      confirmation_token: "confirmation_synthetic_0001",
    },
    "organization",
    "commit_000102030405060708090a0b",
  );
  assert.deepEqual(event, {
    schema_version: 1,
    action: "commit_manual_mask",
    event_id: "commit_000102030405060708090a0b",
    inspection_id: "inspection_synthetic_0001",
    requested_type: "organization",
    requested_scope: "all_exact",
    confirmation_token: "confirmation_synthetic_0001",
  });
  assert.throws(
    function () {
      Core.buildCommitEvent({ inspection_id: "inspection" }, "unknown", "commit_000102030405060708090a0b");
    },
    /unknown quick type/,
  );
});

test("scroll ratios and menu positions are bounded", function () {
  assert.equal(Core.scrollRatio(50, 200, 100), 0.5);
  assert.equal(Core.scrollRatio(50, 100, 100), 0);
  assert.equal(Core.scrollTopForRatio(0.75, 300, 100), 150);
  assert.deepEqual(Core.clampMenuPosition(990, 790, 200, 200, 1000, 800, 8), {
    x: 792,
    y: 592,
  });
});

process.stdout.write("processed-text selection component core tests passed\n");
