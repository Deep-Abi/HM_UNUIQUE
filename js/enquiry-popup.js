/**
 * enquiry-popup.js
 * The post-submission "Thank you for your enquiry!" popup for the CONTACT form (the Request a Quote dialog
 * shows the same wording inside itself — see quote-success.js — and never opens this popup). It is shown ONLY
 * by forms.js after the server has confirmed acceptance of an enquiry.
 *
 * Behaviour:
 *  - Opens without moving keyboard focus (announced politely through its live region).
 *  - Auto-closes after ~5 s. The countdown pauses while the pointer is over it or focus is inside
 *    it, so a keyboard / assistive-technology user is never timed out mid-interaction (WCAG 2.2.1).
 *  - Auto-close never moves focus. Only an explicit close (button / Escape) while focus is inside
 *    the popup returns focus to where it was.
 *  - Escape closes the popup first (capture phase) without also closing an open Request a Quote dialog.
 */

import { ENQUIRY_TITLE as TITLE, ENQUIRY_BODY as BODY, SUCCESS_AUTO_CLOSE_MS as AUTO_CLOSE_MS } from "./enquiry-messages.js";

let timer = null;
let remaining = AUTO_CLOSE_MS;
let startedAt = 0;
let previouslyFocused = null;
let bound = false;

function popupEl() {
  return document.querySelector("[data-enquiry-popup]");
}

function startTimer(ms) {
  clearTimeout(timer);
  remaining = ms;
  startedAt = Date.now();
  timer = setTimeout(() => closeEnquiryPopup({ restoreFocus: false }), ms);
}

function pauseTimer() {
  if (!timer) return;
  clearTimeout(timer);
  timer = null;
  remaining = Math.max(1000, remaining - (Date.now() - startedAt));
}

function resumeTimer() {
  const el = popupEl();
  if (!el || el.hidden || timer) return;
  if (el.matches(":hover") || el.contains(document.activeElement)) return;
  startTimer(remaining);
}

function bindOnce(el) {
  if (bound) return;
  bound = true;
  el.addEventListener("mouseenter", pauseTimer);
  el.addEventListener("mouseleave", resumeTimer);
  el.addEventListener("focusin", pauseTimer);
  el.addEventListener("focusout", () => setTimeout(resumeTimer, 0));
  el.querySelector("[data-enquiry-popup-close]")?.addEventListener("click", () => closeEnquiryPopup({ restoreFocus: true }));
  // Capture phase so Escape dismisses the popup only, leaving any open dialog alone.
  document.addEventListener(
    "keydown",
    (event) => {
      if (event.key !== "Escape") return;
      const current = popupEl();
      if (!current || current.hidden) return;
      event.stopImmediatePropagation();
      closeEnquiryPopup({ restoreFocus: current.contains(document.activeElement) });
    },
    true
  );
}

export function showEnquiryPopup() {
  const el = popupEl();
  if (!el) return;
  bindOnce(el);
  previouslyFocused = document.activeElement;
  const text = el.querySelector("[data-enquiry-popup-text]");
  if (text) {
    text.innerHTML = "";
    const t = document.createElement("p");
    t.className = "enquiry-popup__title";
    t.textContent = TITLE;
    const b = document.createElement("p");
    b.className = "enquiry-popup__body";
    b.textContent = BODY;
    el.hidden = false; // un-hide first, then insert text so the live region announces it
    text.append(t, b);
  } else {
    el.hidden = false;
  }
  el.classList.add("is-open");
  startTimer(AUTO_CLOSE_MS);
}

export function closeEnquiryPopup({ restoreFocus = false } = {}) {
  const el = popupEl();
  clearTimeout(timer);
  timer = null;
  if (!el || el.hidden) return;
  const hadFocus = el.contains(document.activeElement);
  el.classList.remove("is-open");
  el.hidden = true;
  const text = el.querySelector("[data-enquiry-popup-text]");
  if (text) text.innerHTML = "";
  // Focus is moved ONLY after an explicit close of a popup that held focus. An automatic close
  // leaves focus exactly where the user has it.
  if (restoreFocus && hadFocus && previouslyFocused && document.contains(previouslyFocused) && previouslyFocused.getClientRects().length) {
    previouslyFocused.focus();
  }
  previouslyFocused = null;
}
