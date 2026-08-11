/**
 * modal.js
 * A single generic modal engine (open/close/focus-trap/escape-key/
 * scroll-lock) that both the Request a Quote modal and the Thank You
 * modal are built on top of, per the Phase 1 architecture. No modal
 * behavior is duplicated between the two.
 */

const FOCUSABLE_SELECTOR =
  'a[href], button:not([disabled]), textarea, input, select, [tabindex]:not([tabindex="-1"])';

class Modal {
  /**
   * @param {HTMLElement} overlayEl - the .modal-overlay element
   */
  constructor(overlayEl) {
    this.overlay = overlayEl;
    this.modal = overlayEl.querySelector(".modal");
    this.lastFocusedElement = null;
    this.focusables = null;

    this.handleKeydown = this.handleKeydown.bind(this);
    this.close = this.close.bind(this);

    this.overlay.querySelectorAll("[data-modal-close]").forEach((btn) => {
      btn.addEventListener("click", this.close);
    });

    // Clicking the overlay itself (outside the modal box) closes it
    this.overlay.addEventListener("click", (event) => {
      if (event.target === this.overlay) this.close();
    });
  }

  open() {
    this.lastFocusedElement = document.activeElement;
    this.overlay.classList.add("is-open");
    this.overlay.setAttribute("aria-hidden", "false");
    document.body.classList.add("scroll-locked");
    document.addEventListener("keydown", this.handleKeydown);

    // Cache the focusable list once per open, rather than re-querying
    // the DOM on every Tab keypress in trapFocus() below.
    this.focusables = Array.from(this.modal.querySelectorAll(FOCUSABLE_SELECTOR));
    this.focusables[0]?.focus();
  }

  close() {
    this.overlay.classList.remove("is-open");
    this.overlay.setAttribute("aria-hidden", "true");
    document.body.classList.remove("scroll-locked");
    document.removeEventListener("keydown", this.handleKeydown);
    this.focusables = null;
    this.lastFocusedElement?.focus();
  }

  handleKeydown(event) {
    if (event.key === "Escape") {
      this.close();
      return;
    }
    if (event.key === "Tab") {
      this.trapFocus(event);
    }
  }

  trapFocus(event) {
    if (!this.focusables || this.focusables.length === 0) return;

    const first = this.focusables[0];
    const last = this.focusables[this.focusables.length - 1];

    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }
}

// Registry so other modules (forms.js) can open/close modals by key
// without re-querying the DOM themselves.
const modalRegistry = new Map();

/** Finds the overlay element for `overlaySelector` and registers a Modal instance under `key`. */
function registerModal(key, overlaySelector) {
  const overlayEl = document.querySelector(overlaySelector);
  if (!overlayEl) return;
  modalRegistry.set(key, new Modal(overlayEl));
}

/** Opens the registered modal matching `key` (no-op if not found/registered). */
export function openModal(key) {
  modalRegistry.get(key)?.open();
}

/** Closes the registered modal matching `key` (no-op if not found/registered). */
export function closeModal(key) {
  modalRegistry.get(key)?.close();
}

/**
 * Wires up every [data-modal-open] trigger on the page (the header's
 * Request a Quote button, the mobile drawer CTA, product card "View
 * Details" buttons, secondary CTA buttons, etc.) to open the matching
 * modal — via a single delegated listener on document rather than one
 * listener per trigger. This scales to however many trigger buttons a
 * page ends up with (Phase 4's category pages will each add several
 * per product card) with no extra listener cost, and also means any
 * trigger element could be added to the DOM later without needing to
 * re-run this wiring.
 */
function initModalTriggers() {
  document.addEventListener("click", (event) => {
    const trigger = event.target.closest("[data-modal-open]");
    if (!trigger) return;
    event.preventDefault();
    openModal(trigger.dataset.modalOpen);
  });
}

export function initModals() {
  registerModal("quote", "[data-modal='quote']");
  registerModal("thank-you", "[data-modal='thank-you']");
  initModalTriggers();
}
