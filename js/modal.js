/**
 * modal.js
 * A single generic modal engine (open/close/focus-trap/escape-key/
 * scroll-lock) for the Request a Quote dialog. It announces its lifecycle
 * with "modal:open" / "modal:close" events on the overlay element, which
 * quote-success.js uses to show and clean up the post-submission state.
 */

// Broad tag/attribute match only — every exclusion (disabled,
// negative tabindex, hidden input, invisible, inert) is applied as a
// separate, explicit check in getVisibleFocusables() below, rather
// than folded into this selector string, so each rule stays testable
// and correct on its own (in particular, `:not([disabled])` alone
// would miss a control that's disabled only because it sits inside a
// disabled <fieldset>, and `:not([tabindex="-1"])` alone would miss
// tabindex="-2" or a tabindex set via the JS property rather than the
// attribute).
const FOCUSABLE_SELECTOR = "a[href], button, textarea, input, select, [tabindex]";

/**
 * Elements matching FOCUSABLE_SELECTOR that are actually focusable
 * and reachable right now. Excludes, in order:
 * - Negative tabindex (`el.tabIndex < 0`) — covers tabindex="-1",
 *   tabindex="-2", and a tabindex set via the `.tabIndex` JS property
 *   rather than the HTML attribute, none of which a plain attribute
 *   selector like `:not([tabindex="-1"])` would catch.
 * - Disabled controls (`el.matches(":disabled")`) — the `:disabled`
 *   pseudo-class is true for a control with its own `disabled`
 *   attribute AND for one that's merely a descendant of a disabled
 *   `<fieldset>` (per the HTML "disabled state" algorithm), so this
 *   one check covers both without walking up for `<fieldset>`s by hand.
 * - `<input type="hidden">` — never meant to be focusable; checked
 *   explicitly rather than relying only on layout, since a hidden
 *   input could in principle still report a client rect in some
 *   browser quirk.
 * - Anything inside an `inert` ancestor — `inert` elements can still
 *   have non-zero client rects and non-"hidden" computed visibility
 *   (inert only removes interactivity, not layout), so neither of the
 *   other checks would catch it on their own.
 * - Computed `visibility: hidden` or `visibility: collapse` — unlike
 *   `display: none`, an invisible element of this kind still has
 *   non-zero client rects, so getClientRects() alone would wrongly
 *   keep it in the trap.
 * - Anything without a rendered client rect at all (getClientRects()
 *   — reliable regardless of position, unlike offsetParent, which
 *   browsers can report as null for position:fixed elements like this
 *   modal box itself) — catches `display: none`, a `hidden` ancestor,
 *   zero-size layout, and anything else not actually laid out.
 *
 * Called fresh on every Tab keypress (see trapFocus) rather than
 * cached once at open(), so a control that becomes focusable after
 * open (e.g. the submission-error message's "call us" link, hidden
 * until a failed submit reveals it) is included immediately instead
 * of only after the modal is reopened.
 */
function getVisibleFocusables(root) {
  return Array.from(root.querySelectorAll(FOCUSABLE_SELECTOR)).filter((el) => {
    if (el.tabIndex < 0) return false;
    if (el.matches(":disabled")) return false;
    if (el.tagName === "INPUT" && el.type === "hidden") return false;
    if (el.closest("[inert]")) return false;
    const visibility = getComputedStyle(el).visibility;
    if (visibility === "hidden" || visibility === "collapse") return false;
    if (el.getClientRects().length === 0) return false;
    return true;
  });
}

// Counts how many modals are currently open, so the background can be
// made inert as soon as the first one opens and restored only once
// the last one closes (covers the quote -> thank-you handoff, where
// one briefly opens right after the other closes).
let openModalCount = 0;

// Elements that setBackgroundInert(true) itself switched to inert,
// recorded so the matching setBackgroundInert(false) only reverts
// those — never an element that was already inert for a reason the
// modal system doesn't own, such as the mobile nav drawer and its
// overlay while the drawer is closed (navigation.js sets inert=true
// on them permanently whenever the drawer isn't open). Without this,
// restoring every background child to inert=false unconditionally
// would wrongly reopen the closed drawer to keyboard focus/AT once a
// modal closes.
const backgroundInertOwned = new Set();

function setBackgroundInert(isInert) {
  if (isInert) {
    Array.from(document.body.children).forEach((el) => {
      // The enquiry confirmation popup must stay reachable while a dialog is open.
      if (el.classList.contains("modal-overlay") || el.tagName === "SCRIPT" || el.hasAttribute("data-enquiry-popup")) return;
      if (!el.inert) {
        el.inert = true;
        backgroundInertOwned.add(el);
      }
    });
  } else {
    backgroundInertOwned.forEach((el) => {
      el.inert = false;
    });
    backgroundInertOwned.clear();
  }
}

class Modal {
  /**
   * @param {HTMLElement} overlayEl - the .modal-overlay element
   */
  constructor(overlayEl) {
    this.overlay = overlayEl;
    this.modal = overlayEl.querySelector(".modal");
    this.lastFocusedElement = null;

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

    openModalCount += 1;
    setBackgroundInert(true);

    getVisibleFocusables(this.modal)[0]?.focus();
    this.overlay.dispatchEvent(new CustomEvent("modal:open"));
  }

  close() {
    this.overlay.classList.remove("is-open");
    this.overlay.setAttribute("aria-hidden", "true");
    document.body.classList.remove("scroll-locked");
    document.removeEventListener("keydown", this.handleKeydown);

    openModalCount = Math.max(0, openModalCount - 1);
    if (openModalCount === 0) setBackgroundInert(false);

    // Only restore focus to a target that's still actually there and
    // visible (e.g. not a control that was hidden/removed meanwhile).
    const canRestore =
      this.lastFocusedElement &&
      document.contains(this.lastFocusedElement) &&
      this.lastFocusedElement.getClientRects().length > 0;
    if (canRestore) this.lastFocusedElement.focus();
    this.lastFocusedElement = null;
    this.overlay.dispatchEvent(new CustomEvent("modal:close"));
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
    // Recalculated on every Tab press rather than cached at open(),
    // so a control that becomes visible/hidden/disabled while the
    // modal is open (e.g. the unavailable-submission message's phone
    // and email links, hidden until a submit attempt reveals them)
    // is reflected in the trap boundary immediately.
    const focusables = getVisibleFocusables(this.modal);
    if (focusables.length === 0) return;

    const first = focusables[0];
    const last = focusables[focusables.length - 1];

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
