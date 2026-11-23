/**
 * navigation.js
 * Owns everything related to the header: the mobile navigation drawer
 * (hamburger toggle + accordion Products submenu), the desktop
 * Products mega-dropdown (hover on pointer devices, tap/click on
 * touch and keyboard), and marking the current page's nav link as
 * active.
 *
 * This module only wires up behavior against the shared header/mobile
 * nav markup that is identical on every page — see
 * documents/component-reference.md for the canonical HTML.
 */

// Matches every element FOCUSABLE_SELECTOR in modal.js treats as
// focusable. Kept as its own local constant (navigation.js and
// modal.js stay independent, self-contained modules per the project's
// existing architecture) rather than importing across modules.
const FOCUSABLE_SELECTOR =
  'a[href], button:not([disabled]), textarea, input, select, [tabindex]:not([tabindex="-1"])';

/** Elements that are actually visible/reachable right now — excludes
 * anything inside a `hidden` ancestor, `display:none`, or detached
 * from layout (getClientRects() is empty for all of those, regardless
 * of positioning, which a plain offsetParent check is not reliable
 * for on position:fixed elements like the drawer/modals). */
function getVisibleFocusables(root) {
  return Array.from(root.querySelectorAll(FOCUSABLE_SELECTOR)).filter(
    (el) => el.getClientRects().length > 0
  );
}

// The actual CSS breakpoint where the hamburger/drawer hands off to
// the desktop primary nav (see css/responsive.css, Laptop tier).
const DESKTOP_NAV_QUERY = "(min-width: 992px)";

function initMobileDrawer() {
  const toggle = document.querySelector("[data-nav-toggle]");
  const drawer = document.querySelector("[data-mobile-nav]");
  const overlay = document.querySelector("[data-mobile-nav-overlay]");
  const closeBtn = document.querySelector("[data-mobile-nav-close]");

  if (!toggle || !drawer || !overlay) return;

  let lastFocusedElement = null;

  // Keeps the closed drawer out of both the tab order and the
  // accessibility tree, not just visually off-screen (the CSS only
  // translates it off-canvas, which alone leaves it keyboard-reachable
  // and exposed to assistive tech). Starts applied, since the drawer
  // begins closed.
  drawer.inert = true;
  drawer.setAttribute("aria-hidden", "true");
  overlay.inert = true;

  // Stage 7A: while the drawer is open the rest of the page is made inert
  // (keyboard AND assistive-tech browsing), not only trapped by the Tab
  // handler below. Only elements this code switched to inert are restored,
  // so the closed drawer/overlay and anything modal.js owns are untouched.
  const pageInertOwned = new Set();
  const setPageInert = (isInert) => {
    if (isInert) {
      Array.from(document.body.children).forEach((el) => {
        if (
          el === drawer ||
          el === overlay ||
          el.tagName === "SCRIPT" ||
          el.classList.contains("modal-overlay") ||
          el.inert
        ) return;
        el.inert = true;
        pageInertOwned.add(el);
      });
    } else {
      pageInertOwned.forEach((el) => { el.inert = false; });
      pageInertOwned.clear();
    }
  };

  const openDrawer = () => {
    lastFocusedElement = document.activeElement;

    drawer.classList.add("is-open");
    overlay.classList.add("is-open");
    toggle.classList.add("is-active");
    toggle.setAttribute("aria-expanded", "true");
    document.body.classList.add("scroll-locked");

    drawer.inert = false;
    drawer.removeAttribute("aria-hidden");
    overlay.inert = false;
    setPageInert(true);

    // Move focus inside the drawer once it's interactive again.
    const firstFocusable = getVisibleFocusables(drawer)[0];
    (closeBtn || firstFocusable)?.focus();
  };

  const closeDrawer = ({ restoreFocus = true } = {}) => {
    drawer.classList.remove("is-open");
    overlay.classList.remove("is-open");
    toggle.classList.remove("is-active");
    toggle.setAttribute("aria-expanded", "false");
    document.body.classList.remove("scroll-locked");

    drawer.inert = true;
    drawer.setAttribute("aria-hidden", "true");
    overlay.inert = true;
    setPageInert(false);

    if (restoreFocus) {
      // Only restore focus to the opening control if it's still a
      // sensible target (present, visible) — e.g. not mid-resize.
      const canRestore =
        lastFocusedElement &&
        document.contains(lastFocusedElement) &&
        lastFocusedElement.getClientRects().length > 0;
      (canRestore ? lastFocusedElement : toggle)?.focus();
    }
    lastFocusedElement = null;
  };

  toggle.addEventListener("click", () => {
    const isOpen = drawer.classList.contains("is-open");
    isOpen ? closeDrawer() : openDrawer();
  });

  overlay.addEventListener("click", () => closeDrawer());
  closeBtn?.addEventListener("click", () => closeDrawer());

  // Keep keyboard focus inside the drawer while it's open.
  drawer.addEventListener("keydown", (event) => {
    if (event.key !== "Tab" || !drawer.classList.contains("is-open")) return;

    const focusables = getVisibleFocusables(drawer);
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
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && drawer.classList.contains("is-open")) {
      closeDrawer();
    }
  });

  // Accordion behavior for the Products submenu inside the drawer
  const submenuToggle = drawer.querySelector("[data-mobile-submenu-toggle]");
  const submenuItem = submenuToggle?.closest("[data-mobile-nav-item]");

  submenuToggle?.addEventListener("click", () => {
    const isExpanded = submenuItem.classList.toggle("mobile-nav__item--expanded");
    submenuToggle.setAttribute("aria-expanded", String(isExpanded));
  });

  // Drawer-to-quote transition: the drawer's own "Request a Quote"
  // button also carries [data-modal-open="quote"], which modal.js's
  // single delegated document click listener (initModalTriggers) will
  // open generically. This listener is bound directly on the button,
  // so — since DOM events bubble target-first — it runs before that
  // delegated listener on the same click, letting it move focus to a
  // control that stays visible (the hamburger toggle) and close the
  // drawer first, so the quote modal doesn't open behind/inside a
  // still-open drawer, scroll-lock isn't fought over by both, and the
  // modal's own close() later restores focus to the toggle instead of
  // a now-hidden drawer button.
  const drawerQuoteTrigger = drawer.querySelector('[data-modal-open="quote"]');
  drawerQuoteTrigger?.addEventListener("click", () => {
    // Stage 7A: close first (which lifts the page-wide inert), THEN move
    // focus -- an inert toggle cannot take focus.
    closeDrawer({ restoreFocus: false });
    toggle.focus();
  });

  // Breakpoint transitions: if the viewport crosses into the desktop
  // nav layout while the drawer is open, drop its open/overlay/focus-
  // trap/scroll-lock state immediately rather than leaving it stuck
  // (the hamburger that owns it is hidden by CSS at this width, so
  // there would be no way to close it otherwise). Returning to mobile
  // afterward then finds a normal, closed drawer. Driven off the same
  // breakpoint the CSS itself switches on, not a separate guess.
  const desktopQuery = window.matchMedia(DESKTOP_NAV_QUERY);
  const handleBreakpointChange = () => {
    if (drawer.classList.contains("is-open")) {
      closeDrawer({ restoreFocus: false });
    }
  };
  (desktopQuery.addEventListener
    ? desktopQuery.addEventListener("change", handleBreakpointChange)
    : desktopQuery.addListener(handleBreakpointChange)); // Safari <14 fallback
}

function initProductsDropdown() {
  const dropdownItem = document.querySelector("[data-nav-dropdown]");
  const trigger = dropdownItem?.querySelector("[data-nav-dropdown-trigger]");

  if (!dropdownItem || !trigger) return;

  const openDropdown = () => {
    dropdownItem.classList.add("is-open");
    trigger.setAttribute("aria-expanded", "true");
  };

  const closeDropdown = () => {
    dropdownItem.classList.remove("is-open");
    trigger.setAttribute("aria-expanded", "false");
  };

  // Hover is only wired up for devices that actually have a precise
  // pointer with real hover (a mouse/trackpad). This is distinct from
  // "(hover: none)", which used to bail out of the whole function —
  // and so skipped click/keyboard/outside-dismiss too — for ANY
  // touch-capable device, including touchscreen laptops showing the
  // desktop nav at >=992px. Click/tap and keyboard support below are
  // always wired up, regardless of pointer type.
  const supportsHover = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  if (supportsHover) {
    dropdownItem.addEventListener("mouseenter", openDropdown);
    dropdownItem.addEventListener("mouseleave", closeDropdown);
  }

  trigger.addEventListener("click", (event) => {
    event.preventDefault();
    if (supportsHover) {
      // A real mouse click is physically preceded by the hover that
      // already opened this (mouseenter fires before click), so
      // toggling here would immediately close what hover just opened.
      // Keyboard Enter/Space activation reaches this same click
      // handler with no preceding hover; "open" is the right outcome
      // either way. Closing stays available via mouseleave, Escape,
      // or an outside click.
      openDropdown();
    } else {
      // No hover signal exists on a touch-primary device, so tap must
      // toggle open/closed on its own.
      dropdownItem.classList.contains("is-open") ? closeDropdown() : openDropdown();
    }
  });

  // Escape closes the dropdown however it was opened — including a
  // pure mouse hover, where nothing inside the dropdown ever receives
  // keyboard focus. A listener bound only on dropdownItem would never
  // see that keydown at all (it bubbles from whatever actually has
  // focus, e.g. <body>, not from the hovered-but-unfocused dropdown),
  // so this is bound on document instead. Focus is only moved to the
  // trigger when it was already somewhere inside the dropdown (e.g. a
  // category link reached via Tab) — never blur()ing it away, so
  // keyboard focus stays visibly on-page — and left untouched for a
  // pure hover dismissal, so Escape doesn't unexpectedly steal focus
  // from whatever the mouse-only user was doing.
  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape" || !dropdownItem.classList.contains("is-open")) return;
    closeDropdown();
    if (dropdownItem.contains(document.activeElement)) {
      trigger.focus();
    }
  });

  document.addEventListener("click", (event) => {
    if (!dropdownItem.contains(event.target)) {
      closeDropdown();
    }
  });

  // Breakpoint transitions: the dropdown is desktop-only, so dropping
  // its open state when leaving the desktop nav layout (and whenever
  // the breakpoint changes at all) keeps it from being silently stuck
  // "open" in markup/aria-expanded after a resize with no outside
  // click/Escape to close it.
  const desktopQuery = window.matchMedia(DESKTOP_NAV_QUERY);
  const handleBreakpointChange = () => closeDropdown();
  (desktopQuery.addEventListener
    ? desktopQuery.addEventListener("change", handleBreakpointChange)
    : desktopQuery.addListener(handleBreakpointChange));
}

/**
 * Marks the link matching the current page's URL with
 * aria-current="page" in both the desktop nav and the mobile drawer,
 * as a fallback for any page where the attribute wasn't set manually
 * in the HTML (kept in sync with the `data-nav-key` on <body>).
 */
function initActiveLinkState() {
  const currentKey = document.body.dataset.navKey;
  if (!currentKey) return;

  document
    .querySelectorAll(`[data-nav-key-link="${currentKey}"]`)
    .forEach((link) => link.setAttribute("aria-current", "page"));
}

/**
 * Adds a subtle shadow/compact state to the header once the page has
 * scrolled past the utility bar's height, so the sticky header reads
 * as "elevated" without changing its actual layout.
 */
function initHeaderScrollState() {
  const header = document.querySelector("[data-site-header]");
  if (!header) return;

  const SCROLLED_CLASS = "is-scrolled";
  const THRESHOLD_PX = 24;

  const update = () => {
    header.classList.toggle(SCROLLED_CLASS, window.scrollY > THRESHOLD_PX);
  };

  window.addEventListener("scroll", update, { passive: true });
  update();
}

/**
 * Keeps --header-offset (the root scroll-padding-top) equal to the header's REAL height, so
 * anchor jumps, #group links and keyboard focus scrolling land just below it at every width
 * (the stacked brand makes the header taller than any fixed constant). While the header is not
 * sticky (short landscape screens) there is nothing to clear, so the offset is 0.
 */
function initHeaderOffset() {
  const header = document.querySelector("[data-site-header]");
  if (!header) return;
  const root = document.documentElement;
  const sync = () => {
    const sticky = window.getComputedStyle(header).position === "sticky";
    const px = sticky ? Math.ceil(header.getBoundingClientRect().height) + 8 : 0;
    root.style.setProperty("--header-offset", `${px}px`);
  };
  sync();
  window.addEventListener("resize", sync, { passive: true });
  window.addEventListener("load", sync);
  if (typeof ResizeObserver === "function") new ResizeObserver(sync).observe(header);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(sync).catch(() => {});
}

export function initNavigation() {
  initMobileDrawer();
  initProductsDropdown();
  initActiveLinkState();
  initHeaderScrollState();
  initHeaderOffset();
}
