(function (global) {
  "use strict";

  const API_VERSION = 1;
  const RENDER_EVENT = "streamlit:render";
  const listeners = new Set();
  let ready = false;
  let lastFrameHeight = null;

  function send(type, data) {
    global.parent.postMessage(
      Object.assign(
        {
          isStreamlitMessage: true,
          type: type,
        },
        data || {},
      ),
      "*",
    );
  }

  function onMessage(event) {
    if (!event || !event.data || event.data.type !== RENDER_EVENT) {
      return;
    }
    const detail = {
      args: event.data.args || {},
      disabled: Boolean(event.data.disabled),
      theme: event.data.theme || null,
    };
    listeners.forEach(function (listener) {
      listener(detail);
    });
  }

  function setComponentReady() {
    if (!ready) {
      global.addEventListener("message", onMessage);
      ready = true;
    }
    send("streamlit:componentReady", { apiVersion: API_VERSION });
  }

  function setFrameHeight(height) {
    const nextHeight = Number.isFinite(height)
      ? Math.max(0, Math.round(height))
      : Math.max(0, Math.round(document.body.scrollHeight));
    if (nextHeight === lastFrameHeight) {
      return;
    }
    lastFrameHeight = nextHeight;
    send("streamlit:setFrameHeight", { height: nextHeight });
  }

  function setComponentValue(value) {
    send("streamlit:setComponentValue", {
      value: value,
      dataType: "json",
    });
  }

  function onRender(listener) {
    if (typeof listener !== "function") {
      throw new TypeError("render listener must be a function");
    }
    listeners.add(listener);
    return function () {
      listeners.delete(listener);
    };
  }

  global.SolidPrivacyStreamlitBridge = Object.freeze({
    API_VERSION: API_VERSION,
    RENDER_EVENT: RENDER_EVENT,
    onRender: onRender,
    setComponentReady: setComponentReady,
    setFrameHeight: setFrameHeight,
    setComponentValue: setComponentValue,
  });
})(window);
