/* paper-writer landing — chat demo player + copy buttons. No dependencies. */
(function () {
  "use strict";

  document.documentElement.classList.add("js");

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var target = document.querySelector(btn.getAttribute("data-copy"));
      if (!target) return;
      var text = target.innerText.replace(/^\$ /gm, "");
      navigator.clipboard.writeText(text).then(function () {
        var old = btn.textContent;
        btn.textContent = btn.getAttribute("data-copied-label") || "Copied";
        setTimeout(function () { btn.textContent = old; }, 1400);
      });
    });
  });

  var chat = document.querySelector("[data-chat]");
  if (!chat) return;

  var msgs = Array.prototype.slice.call(chat.querySelectorAll(".chat-msg"));
  var replayBtn = chat.parentElement.querySelector(".chat-replay");
  var timers = [];
  var started = false;

  function clearTimers() {
    timers.forEach(function (t) { clearTimeout(t); });
    timers = [];
  }

  function later(fn, ms) { timers.push(setTimeout(fn, ms)); }

  function showAll() {
    msgs.forEach(function (m) {
      m.classList.add("is-on");
      var b = m.querySelector(".chat-bubble");
      if (b && b.__fullHTML) b.innerHTML = b.__fullHTML;
    });
  }

  function typeInto(bubble, done) {
    var full = bubble.__fullText;
    bubble.textContent = "";
    var caret = document.createElement("span");
    caret.className = "chat-caret";
    bubble.appendChild(caret);
    var i = 0;
    (function tick() {
      if (i <= full.length) {
        if (bubble.firstChild && bubble.firstChild !== caret) {
          bubble.removeChild(bubble.firstChild);
        }
        bubble.insertBefore(document.createTextNode(full.slice(0, i)), caret);
        i += 1;
        later(tick, 26 + Math.random() * 34);
      } else {
        caret.remove();
        done();
      }
    })();
  }

  function play() {
    clearTimers();
    msgs.forEach(function (m) {
      m.classList.remove("is-on");
      var b = m.querySelector(".chat-bubble");
      if (b) {
        if (!b.__fullHTML) {
          b.__fullHTML = b.innerHTML;
          b.__fullText = b.textContent;
        }
        b.innerHTML = "";
      }
    });
    if (reduceMotion) { showAll(); return; }

    var idx = 0;
    (function next() {
      if (idx >= msgs.length) return;
      var m = msgs[idx];
      var bubble = m.querySelector(".chat-bubble");
      var isUser = m.classList.contains("chat-msg-user");
      idx += 1;
      m.classList.add("is-on");
      if (isUser) {
        typeInto(bubble, function () { later(next, 500); });
      } else {
        later(function () {
          bubble.innerHTML = bubble.__fullHTML;
          later(next, 900 + Math.min(bubble.__fullText.length * 6, 2200));
        }, 550);
      }
    })();
  }

  if (replayBtn) replayBtn.addEventListener("click", play);

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && !started) {
          started = true;
          play();
          io.disconnect();
        }
      });
    }, { threshold: 0.3 });
    io.observe(chat);
  } else {
    play();
  }
})();
