/**
 * navigation.js
 * Owns everything related to the header: the mobile navigation drawer
 * (hamburger toggle + accordion Products submenu), the desktop
 * Products mega-dropdown (hover on pointer devices, tap on touch),
 * and marking the current page's nav link as active.
 *
 * This module only wires up behavior against the shared header/mobile
 * nav markup that is identical on every page — see
 * documents/component-reference.md for the canonical HTML.
 */

function initMobileDrawer() {
  const toggle = document.querySelector("[data-nav-toggle]");
  const drawer = document.querySelector("[data-mobile-nav]");
  const overlay = document.querySelector("[data-mobile-nav-overlay]");
  const closeBtn = document.querySelector("[data-mobile-nav-close]");

  if (!toggle || !drawer || !overlay) return;

  const openDrawer = () => {
    drawer.classList.add("is-open");
    overlay.classList.add("is-open");
    toggle.classList.add("is-active");
    toggle.setAttribute("aria-expanded", "true");
    document.body.classList.add("scroll-locked");
  };

  const closeDrawer = () => {
    drawer.classList.remove("is-open");
    overlay.classList.remove("is-open");
    toggle.classList.remove("is-active");
    toggle.setAttribute("aria-expanded", "false");
    document.body.classList.remove("scroll-locked");
  };

  toggle.addEventListener("click", () => {
    const isOpen = drawer.classList.contains("is-open");
    isOpen ? closeDrawer() : openDrawer();
  });

  overlay.addEventListener("click", closeDrawer);
  closeBtn?.addEventListener("click", closeDrawer);

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
}

function initProductsDropdown() {
  const dropdownItem = document.querySelector("[data-nav-dropdown]");
  const trigger = dropdownItem?.querySelector("[data-nav-dropdown-trigger]");

  if (!dropdownItem || !trigger) return;

  const isTouchDevice = window.matchMedia("(hover: none)").matches;

  if (isTouchDevice) {
    // On touch devices the desktop dropdown isn't used (mobile drawer
    // handles Products via its own accordion) — no listener needed.
    return;
  }

  const openDropdown = () => dropdownItem.classList.add("is-open");
  const closeDropdown = () => dropdownItem.classList.remove("is-open");

  dropdownItem.addEventListener("mouseenter", openDropdown);
  dropdownItem.addEventListener("mouseleave", closeDropdown);

  trigger.addEventListener("click", (event) => {
    event.preventDefault();
    dropdownItem.classList.toggle("is-open");
  });

  trigger.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeDropdown();
      trigger.blur();
    }
  });

  document.addEventListener("click", (event) => {
    if (!dropdownItem.contains(event.target)) {
      closeDropdown();
    }
  });
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

export function initNavigation() {
  initMobileDrawer();
  initProductsDropdown();
  initActiveLinkState();
  initHeaderScrollState();
}
