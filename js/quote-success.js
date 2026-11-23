/**
 * quote-success.js
 * Success experience for the Request a Quote dialog. Called by forms.js ONLY after the server has
 * confirmed acceptance of the enquiry.
 *
 *  1. The same thank-you content as the Contact popup is shown prominently INSIDE the existing dialog
 *     (no second modal is opened). Focus moves to the thank-you heading, because the submit button that
 *     held it has just been replaced.
 *  2. After ~5 s the dialog closes through the normal modal engine, which restores focus to the control
 *     that opened it. A Close button (and the dialog's own X, Escape, or a click outside) closes it sooner.
 *     The countdown pauses while the pointer is over the dialog.
 *  3. Whenever the dialog closes after a success, a persistent, dismissible confirmation (role="status")
 *     remains on the page outside the dialog, so the result is never lost when the dialog goes away.
 */
import { ENQUIRY_TITLE, ENQUIRY_BODY, ACK_FAILED_NOTE, SUCCESS_AUTO_CLOSE_MS } from "./enquiry-messages.js";
import { closeModal } from "./modal.js";

let timer = null;
let remaining = SUCCESS_AUTO_CLOSE_MS;
let startedAt = 0;
let shownFor = null; // acknowledgement state of the success currently displayed, or null
let confirmationReturnFocus = null;
let bound = false;

const overlay = () => document.querySelector("[data-modal='quote']");

function parts() {
  const o = overlay();
  if (!o) return null;
  const col = o.querySelector(".modal__form-col");
  return {
    overlay: o,
    dialog: o.querySelector(".modal"),
    header: col?.querySelector("[data-quote-header]"),
    form: col?.querySelector("form[data-form='quote']"),
    panel: col?.querySelector("[data-quote-success]"),
  };
}

function startTimer(ms) {
  clearTimeout(timer);
  remaining = ms;
  startedAt = Date.now();
  timer = setTimeout(() => closeModal("quote"), ms);
}
function pauseTimer() {
  if (!timer) return;
  clearTimeout(timer);
  timer = null;
  remaining = Math.max(1000, remaining - (Date.now() - startedAt));
}
function resumeTimer() {
  if (timer || shownFor === null) return;
  startTimer(remaining);
}

/** Puts the dialog back to its normal form view (called whenever the dialog closes). */
function resetDialog() {
  const p = parts();
  clearTimeout(timer);
  timer = null;
  if (!p) return;
  if (p.header) p.header.hidden = false;
  if (p.form) p.form.hidden = false;
  if (p.panel) p.panel.hidden = true;
  p.dialog?.setAttribute("aria-labelledby", "quote-modal-title");
}

function onDialogClosed() {
  const acknowledgement = shownFor;
  shownFor = null;
  resetDialog();
  if (acknowledgement !== null) showEnquiryConfirmation(acknowledgement);
}

function bindOnce(p) {
  if (bound) return;
  bound = true;
  p.overlay.addEventListener("modal:close", onDialogClosed);
  p.overlay.addEventListener("modal:open", () => { shownFor = null; resetDialog(); });
  p.dialog?.addEventListener("mouseenter", () => { if (shownFor !== null) pauseTimer(); });
  p.dialog?.addEventListener("mouseleave", resumeTimer);
}

/** Shows the thank-you panel inside the open Request a Quote dialog. */
export function showQuoteSuccess(acknowledgement = "sent") {
  const p = parts();
  if (!p || !p.panel) return;
  bindOnce(p);

  shownFor = acknowledgement;
  p.panel.querySelector("[data-quote-success-title]").textContent = ENQUIRY_TITLE;
  p.panel.querySelector("[data-quote-success-body]").textContent = ENQUIRY_BODY;
  const note = p.panel.querySelector("[data-quote-success-note]");
  if (note) { note.textContent = ACK_FAILED_NOTE; note.hidden = acknowledgement !== "failed"; }

  if (p.header) p.header.hidden = true;
  if (p.form) p.form.hidden = true;
  p.panel.hidden = false;
  if (p.dialog) p.dialog.scrollTop = 0; // the (taller) form was scrolled; start the thank-you at the top
  p.dialog?.setAttribute("aria-labelledby", "quote-success-title");
  // The submit button that held focus is gone; put focus on the new heading so it is read out.
  p.panel.querySelector("[data-quote-success-title]").focus();
  startTimer(SUCCESS_AUTO_CLOSE_MS);
}

/** Persistent confirmation on the page itself, outside the (now closed) dialog. */
export function showEnquiryConfirmation(acknowledgement = "sent") {
  const el = document.querySelector("[data-enquiry-confirmation]");
  if (!el) return;
  if (!el.dataset.bound) {
    el.dataset.bound = "true";
    el.querySelector("[data-enquiry-confirmation-close]")?.addEventListener("click", hideEnquiryConfirmation);
    el.addEventListener("keydown", (event) => { if (event.key === "Escape") hideEnquiryConfirmation(); });
  }
  const text = el.querySelector("[data-enquiry-confirmation-text]");
  confirmationReturnFocus = document.activeElement;
  el.hidden = false; // un-hide first, then insert the text so the live region announces it
  if (text) {
    text.textContent = "";
    const title = document.createElement("p");
    title.className = "enquiry-confirmation__title";
    title.textContent = ENQUIRY_TITLE;
    const body = document.createElement("p");
    body.className = "enquiry-confirmation__body";
    body.textContent = ENQUIRY_BODY + (acknowledgement === "failed" ? " " + ACK_FAILED_NOTE : "");
    text.append(title, body);
  }
}

export function hideEnquiryConfirmation() {
  const el = document.querySelector("[data-enquiry-confirmation]");
  if (!el || el.hidden) return;
  const hadFocus = el.contains(document.activeElement);
  el.hidden = true;
  const text = el.querySelector("[data-enquiry-confirmation-text]");
  if (text) text.textContent = "";
  if (hadFocus && confirmationReturnFocus && document.contains(confirmationReturnFocus) && confirmationReturnFocus.getClientRects().length) {
    confirmationReturnFocus.focus();
  }
  confirmationReturnFocus = null;
}
