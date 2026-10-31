/**
 * forms.js
 * Client-side validation and submit handling for the Request a Quote
 * modal form and the Contact page form.
 *
 * No submission backend/email service is configured for this project
 * yet. This module is intentionally kept truthful about that: with
 * SUBMIT_ENDPOINT left unset, submitForm() never fabricates a success
 * response, the success modal never opens, entered values are never
 * cleared, and the person sees an honest "not sent yet" message instead.
 * Once a real endpoint/email service is approved, set SUBMIT_ENDPOINT
 * and fill in the real submission call inside submitForm() below —
 * nothing else in this file needs to change.
 */

import { openModal, closeModal } from "./modal.js";

const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PHONE_PATTERN = /^[0-9+\-\s()]{7,15}$/;

const SUBMIT_ENDPOINT = null;

const UNAVAILABLE_MESSAGE_HTML =
  'Online submission isn’t connected yet, so this enquiry has <strong>not</strong> been sent. ' +
  'Please call us at <a href="tel:+919710181944">+91 97101 81944</a> or email ' +
  '<a href="mailto:hmunitecenterprises02@gmail.com">hmunitecenterprises02@gmail.com</a> instead — ' +
  'your details below have been kept so you don’t need to re-enter them.';

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

/**
 * Submission is not wired to a real service in this project yet.
 * Returns a truthful, never-fabricated result: `{ ok: false,
 * unavailable: true }` whenever SUBMIT_ENDPOINT is unset, so the caller
 * can tell "not sent" apart from a genuine send failure. Once an
 * approved endpoint exists, fill in the real request here.
 */
async function submitForm(formEl) {
  if (!SUBMIT_ENDPOINT) {
    return { ok: false, unavailable: true };
  }

  const formData = new FormData(formEl);
  const payload = Object.fromEntries(formData.entries());
  const response = await fetch(SUBMIT_ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return { ok: response.ok };
}

function setSubmitLoadingState(submitBtn, isLoading) {
  if (!submitBtn) return;
  submitBtn.disabled = isLoading;
  submitBtn.classList.toggle("is-loading", isLoading);
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

    try {
      const result = await submitForm(formEl);

      if (result.ok) {
        // Only a real, confirmed acceptance resets the form and opens
        // the success modal.
        clearFormErrors(formEl);
        formEl.reset();
        if (options.closeModalKey) closeModal(options.closeModalKey);
        if (options.openModalKey) openModal(options.openModalKey);
      } else if (result.unavailable) {
        setSubmitErrorState(formEl, true, UNAVAILABLE_MESSAGE_HTML);
      } else {
        setSubmitErrorState(formEl, true);
      }
      // Entered values are left untouched on every non-success path.
    } catch (error) {
      setSubmitErrorState(formEl, true);
    } finally {
      setSubmitLoadingState(submitBtn, false);
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
  const quoteForm = document.querySelector("[data-form='quote']");
  if (quoteForm) {
    handleSubmit(quoteForm, { closeModalKey: "quote", openModalKey: "thank-you" });
  }

  const contactForm = document.querySelector("[data-form='contact']");
  if (contactForm) {
    handleSubmit(contactForm, { openModalKey: "thank-you" });
  }
}
