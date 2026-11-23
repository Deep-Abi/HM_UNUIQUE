/**
 * forms.js
 * Client-side validation and submit handling for the Request a Quote modal form and the
 * Contact page form.
 *
 * Submission goes to the enquiry Worker configured in js/enquiry-config.js. This module is
 * strictly truthful about delivery state:
 *  - with no endpoint configured nothing is sent, no success is shown and entries are kept;
 *  - success happens ONLY after the server answers {ok:true, accepted:true}. Contact form: thank-you popup
 *    + persistent inline confirmation. Request a Quote: thank-you inside the dialog, auto-close, then a
 *    persistent page confirmation (quote-success.js);
 *  - on any failure the entries are kept and a retry message is shown;
 *  - repeated submission is blocked while a request is in flight, and one idempotency key is
 *    reused for retries of the same enquiry so the server can drop duplicates.
 */

import { ENQUIRY_ENDPOINT } from "./enquiry-config.js";
import { showEnquiryPopup } from "./enquiry-popup.js";
import { showQuoteSuccess } from "./quote-success.js";

const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PHONE_PATTERN = /^[0-9+\-\s()]{7,15}$/;

const REQUEST_TIMEOUT_MS = 20000;
const PAGE_LOADED_AT = Date.now();

const CONTACT_FALLBACK_HTML =
  'call us at <a href="tel:+919710181944">+91 97101 81944</a> or email ' +
  '<a href="mailto:business@hmunique.com">business<wbr>@hmunique.com</a>';

const UNAVAILABLE_MESSAGE_HTML =
  'Online submission isn’t connected yet, so this enquiry has <strong>not</strong> been sent. ' +
  `Please ${CONTACT_FALLBACK_HTML} instead — your details below have been kept so you don’t need to re-enter them.`;
const RETRY_MESSAGE_HTML =
  `We couldn’t send your enquiry just now, so it has <strong>not</strong> been received. Your details have been kept — please try again in a moment, or ${CONTACT_FALLBACK_HTML}.`;
const RATE_LIMITED_MESSAGE_HTML =
  `Too many enquiries have been sent from this connection recently. Please wait a few minutes and try again, or ${CONTACT_FALLBACK_HTML}.`;
const VALIDATION_MESSAGE_HTML = "Please check the highlighted fields and try again. Your other details have been kept.";

/** Finds the error message element associated with a field's `.form-field` wrapper. */
function getFieldErrorMessage(field) {
  const wrapper = field.closest(".form-field");
  return wrapper ? wrapper.querySelector(".form-field__error-msg") : null;
}

/**
 * Applies/clears the invalid state for a single field: the error-styled
 * wrapper class, aria-invalid, and an aria-describedby link to the
 * field's error message (preserving any other ids already present).
 */
function setFieldInvalidState(field, isValid) {
  const wrapper = field.closest(".form-field");
  wrapper?.classList.toggle("form-field--error", !isValid);
  field.setAttribute("aria-invalid", isValid ? "false" : "true");

  const errorMsg = getFieldErrorMessage(field);
  if (!errorMsg) return;

  if (!errorMsg.id) {
    const base = field.id || field.name || "field";
    errorMsg.id = `${base}-error`;
  }

  const describedBy = (field.getAttribute("aria-describedby") || "")
    .split(/\s+/)
    .filter((id) => id && id !== errorMsg.id);

  if (!isValid) describedBy.push(errorMsg.id);

  if (describedBy.length) {
    field.setAttribute("aria-describedby", describedBy.join(" "));
  } else {
    field.removeAttribute("aria-describedby");
  }
}

/**
 * Validates a single field based on its data attributes.
 * Supported: data-required, data-type="email|phone"
 * Required checkboxes are validated via `.checked`, not `.value`
 * (an unchecked checkbox's value is still its "on" string).
 */
function validateField(field) {
  const isCheckbox = field.type === "checkbox";
  let isValid = true;

  if (isCheckbox) {
    if (field.hasAttribute("data-required") && !field.checked) {
      isValid = false;
    }
  } else {
    const value = field.value.trim();

    if (field.hasAttribute("data-required") && value === "") {
      isValid = false;
    }

    if (isValid && field.dataset.type === "email" && value !== "") {
      isValid = EMAIL_PATTERN.test(value);
    }

    if (isValid && field.dataset.type === "phone" && value !== "") {
      isValid = PHONE_PATTERN.test(value);
    }
  }

  setFieldInvalidState(field, isValid);
  return isValid;
}

/**
 * Validates every required/typed field in a form, moves focus to the
 * first invalid field (if any), and returns overall validity.
 */
function validateForm(formEl) {
  const fields = formEl.querySelectorAll("[data-required], [data-type]");
  let formIsValid = true;
  let firstInvalidField = null;

  fields.forEach((field) => {
    const fieldIsValid = validateField(field);
    if (!fieldIsValid) {
      formIsValid = false;
      if (!firstInvalidField) firstInvalidField = field;
    }
  });

  if (firstInvalidField) firstInvalidField.focus();

  return formIsValid;
}

/** Clears all field error states and the submission error message. */
function clearFormErrors(formEl) {
  formEl.querySelectorAll(".form-field--error").forEach((wrapper) => {
    wrapper.classList.remove("form-field--error");
  });
  formEl.querySelectorAll("[aria-invalid]").forEach((field) => {
    field.setAttribute("aria-invalid", "false");
  });
  setSubmitErrorState(formEl, false);
}

/** Builds the JSON body: all named fields, the consent flag as a boolean and the anti-spam fields. */
function buildPayload(formEl) {
  const payload = { form: formEl.dataset.form };
  new FormData(formEl).forEach((value, key) => {
    if (typeof value === "string") payload[key] = value;
  });
  const consent = formEl.querySelector('input[name="privacy"]');
  payload.privacy = !!(consent && consent.checked);
  payload.startedAt = PAGE_LOADED_AT;
  payload.submissionId = formEl.dataset.submissionId;
  return payload;
}

function newSubmissionId() {
  if (window.crypto?.randomUUID) return window.crypto.randomUUID();
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0;
    return (c === "x" ? r : (r & 0x3) | 0x8).toString(16);
  });
}

/**
 * Sends the enquiry. Never fabricates success. Returns one of:
 *  {ok:true, acknowledgement}  – the server confirmed it accepted the enquiry
 *  {ok:false, unavailable:true} – no endpoint configured, nothing was sent
 *  {ok:false, kind:"validation", errors} | {kind:"rate_limited"} | {kind:"failed"}
 */
async function submitForm(formEl) {
  if (!ENQUIRY_ENDPOINT) return { ok: false, unavailable: true };

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  try {
    const response = await fetch(ENQUIRY_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(buildPayload(formEl)),
      signal: controller.signal,
    });
    let data = null;
    try { data = await response.json(); } catch (e) { data = null; }

    if (response.ok && data && data.ok === true && data.accepted === true) {
      return { ok: true, acknowledgement: data.acknowledgement || "sent" };
    }
    if (response.status === 400 && data && data.code === "validation") {
      return { ok: false, kind: "validation", errors: data.errors || {} };
    }
    if (response.status === 429) return { ok: false, kind: "rate_limited" };
    return { ok: false, kind: "failed" };
  } catch (error) {
    return { ok: false, kind: "failed" }; // network error, timeout or abort
  } finally {
    clearTimeout(timer);
  }
}

/** Maps server-side field errors onto the form's own inline error states. */
function applyServerErrors(formEl, errors) {
  let first = null;
  Object.keys(errors).forEach((key) => {
    const name = key === "phone" && formEl.querySelector('[name="mobile"]') ? "mobile" : key;
    const field = formEl.querySelector(`[name="${name}"]`);
    if (!field) return;
    setFieldInvalidState(field, false);
    first = first || field;
  });
  if (first) first.focus();
  return !!first;
}

function setSuccessState(formEl, show, acknowledgement) {
  const el = formEl.querySelector("[data-form-success]");
  if (!el) return;
  const note = el.querySelector("[data-form-success-note]");
  if (note) note.hidden = !(show && acknowledgement === "failed");
  el.toggleAttribute("hidden", !show);
}

function setSubmitLoadingState(submitBtn, isLoading) {
  if (!submitBtn) return;
  // aria-disabled (not the disabled attribute) keeps keyboard focus on the button while a request is
  // in flight; repeated activation is blocked by the dataset.submitting guard in handleSubmit().
  submitBtn.setAttribute("aria-disabled", isLoading ? "true" : "false");
  submitBtn.classList.toggle("is-loading", isLoading);
  submitBtn.setAttribute("aria-busy", isLoading ? "true" : "false");
  const label = submitBtn.querySelector("[data-submit-label]");
  if (label) {
    if (isLoading) {
      label.dataset.idleText = label.textContent;
      label.textContent = "Sending…";
    } else if (label.dataset.idleText) {
      label.textContent = label.dataset.idleText;
    }
  }
}

// Caches each error element's original (truthful-failure) markup so a
// temporary "unavailable" message can be swapped in and back out again
// without losing the default wording authored in the page.
const defaultErrorHTML = new WeakMap();

/**
 * Shows/hides a form's submission-level error message, distinct from
 * per-field validation messages. `customHTML`, when given, replaces the
 * message content (used for the "submission unavailable" state); it is
 * restored to the page's own default wording afterwards.
 */
function setSubmitErrorState(formEl, hasError, customHTML) {
  const errorEl = formEl.querySelector("[data-form-error]");
  if (!errorEl) return;

  if (!defaultErrorHTML.has(errorEl)) {
    defaultErrorHTML.set(errorEl, errorEl.innerHTML);
  }

  if (hasError) {
    errorEl.innerHTML = customHTML || defaultErrorHTML.get(errorEl);
  }
  errorEl.toggleAttribute("hidden", !hasError);
}

function handleSubmit(formEl, options) {
  formEl.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Guard against a duplicate submit firing while one is pending
    // (in addition to the disabled submit button).
    if (formEl.dataset.submitting === "true") return;

    if (!validateForm(formEl)) return;

    const submitBtn = formEl.querySelector('[type="submit"]');
    formEl.dataset.submitting = "true";
    setSubmitLoadingState(submitBtn, true);
    setSubmitErrorState(formEl, false);

    setSuccessState(formEl, false);
    formEl.setAttribute("aria-busy", "true");

    try {
      const result = await submitForm(formEl);

      if (result.ok) {
        // Only a real, server-confirmed acceptance resets the form and shows success.
        clearFormErrors(formEl);
        formEl.reset();
        formEl.dataset.submissionId = newSubmissionId(); // next enquiry gets its own key
        if (formEl.dataset.form === "quote") {
          // Request a Quote: thank-you shown inside the existing dialog, which then closes itself
          // and leaves a persistent confirmation on the page. No second modal, no popup.
          showQuoteSuccess(result.acknowledgement);
        } else {
          // Contact: 5-second popup, with the inline confirmation remaining in the form area.
          setSuccessState(formEl, true, result.acknowledgement);
          showEnquiryPopup();
        }
      } else if (result.unavailable) {
        setSubmitErrorState(formEl, true, UNAVAILABLE_MESSAGE_HTML);
      } else if (result.kind === "validation") {
        const shown = applyServerErrors(formEl, result.errors);
        setSubmitErrorState(formEl, true, shown ? VALIDATION_MESSAGE_HTML : RETRY_MESSAGE_HTML);
      } else if (result.kind === "rate_limited") {
        setSubmitErrorState(formEl, true, RATE_LIMITED_MESSAGE_HTML);
      } else {
        setSubmitErrorState(formEl, true, RETRY_MESSAGE_HTML);
      }
      // Entered values are left untouched on every non-success path.
    } catch (error) {
      setSubmitErrorState(formEl, true, RETRY_MESSAGE_HTML);
    } finally {
      setSubmitLoadingState(submitBtn, false);
      formEl.removeAttribute("aria-busy");
      formEl.dataset.submitting = "false";
    }
  });

  // Re-validate a field as soon as the person corrects it, so its error
  // clears without waiting for another full submit attempt. Checkboxes
  // and selects correct on "change"; text-type fields correct on "blur".
  formEl.querySelectorAll("[data-required], [data-type]").forEach((field) => {
    const correctionEvent =
      field.type === "checkbox" || field.tagName === "SELECT" ? "change" : "blur";
    field.addEventListener(correctionEvent, () => validateField(field));

    // A field that is ALREADY showing an error also re-checks while it is
    // being typed in, so the error disappears the moment the value becomes
    // valid. Waiting for "blur" meant it vanished at the instant the
    // person pressed the mouse on the next control: the message's height
    // collapsed between mouse-down and mouse-up, the page shifted under
    // the pointer and the click (e.g. on the consent checkbox just below)
    // was lost. No error is ever shown early by this: it only runs for
    // fields that are already marked invalid.
    if (correctionEvent === "blur") {
      field.addEventListener("input", () => {
        if (field.closest(".form-field")?.classList.contains("form-field--error")) {
          validateField(field);
        }
      });
    }
  });
}

export function initForms() {
  document.querySelectorAll("[data-form='quote'], [data-form='contact']").forEach((formEl) => {
    formEl.dataset.submissionId = newSubmissionId();
    handleSubmit(formEl, {});
  });
}
