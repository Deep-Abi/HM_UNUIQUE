/**
 * forms.js
 * Client-side validation and submit handling for the Request a Quote
 * modal form and the Contact page form. On successful validation this
 * module is the seam where the "Send Email" step from the Phase 1
 * workflow gets wired to an actual endpoint in a later phase — the
 * `submitForm()` function below is intentionally isolated so that
 * swapping in a real request is a one-function change.
 *
 * Workflow implemented here: validate -> (send) -> success animation
 * -> open Thank You modal -> reset form.
 */

import { openModal, closeModal } from "./modal.js";

const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PHONE_PATTERN = /^[0-9+\-\s()]{7,15}$/;

/**
 * Validates a single field based on its data attributes.
 * Supported: data-required, data-type="email|phone"
 */
function validateField(field) {
  const value = field.value.trim();
  const wrapper = field.closest(".form-field");
  let isValid = true;

  if (field.hasAttribute("data-required") && value === "") {
    isValid = false;
  }

  if (isValid && field.dataset.type === "email" && value !== "") {
    isValid = EMAIL_PATTERN.test(value);
  }

  if (isValid && field.dataset.type === "phone" && value !== "") {
    isValid = PHONE_PATTERN.test(value);
  }

  wrapper?.classList.toggle("form-field--error", !isValid);
  return isValid;
}

/** Validates every required/typed field in a form; returns overall validity. */
function validateForm(formEl) {
  const fields = formEl.querySelectorAll("[data-required], [data-type]");
  let formIsValid = true;

  fields.forEach((field) => {
    const fieldIsValid = validateField(field);
    if (!fieldIsValid) formIsValid = false;
  });

  return formIsValid;
}

/**
 * Placeholder submission function. Returns a resolved Promise to keep
 * the calling code async-ready. Replace the body of this function
 * with a real fetch() call to the confirmed email/form endpoint (see
 * Phase 1 Recommendation: "confirm quote/contact form backend"). The
 * payload is already assembled and ready to send — nothing else in
 * this file needs to change once the endpoint is wired up.
 */
function submitForm(formEl) {
  const formData = new FormData(formEl);
  const payload = Object.fromEntries(formData.entries());
  return Promise.resolve({ ok: true, payload });
}

function setSubmitLoadingState(submitBtn, isLoading) {
  if (!submitBtn) return;
  submitBtn.disabled = isLoading;
  submitBtn.classList.toggle("is-loading", isLoading);
}

function setSubmitErrorState(formEl, hasError) {
  const errorEl = formEl.querySelector("[data-form-error]");
  errorEl?.toggleAttribute("hidden", !hasError);
}

function handleSubmit(formEl, options) {
  formEl.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (!validateForm(formEl)) return;

    const submitBtn = formEl.querySelector('[type="submit"]');
    setSubmitLoadingState(submitBtn, true);
    setSubmitErrorState(formEl, false);

    try {
      const result = await submitForm(formEl);
      setSubmitLoadingState(submitBtn, false);

      if (result.ok) {
        formEl.reset();
        if (options.closeModalKey) closeModal(options.closeModalKey);
        if (options.openModalKey) openModal(options.openModalKey);
      } else {
        setSubmitErrorState(formEl, true);
      }
    } catch (error) {
      setSubmitLoadingState(submitBtn, false);
      setSubmitErrorState(formEl, true);
    }
  });

  // Live-validate a field once the user leaves it, so errors clear
  // as soon as they're fixed rather than only on submit.
  formEl.querySelectorAll("[data-required], [data-type]").forEach((field) => {
    field.addEventListener("blur", () => validateField(field));
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
