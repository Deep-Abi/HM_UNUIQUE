/**
 * main.js
 * Entry point for the site. Initializes every shared module once the
 * DOM is ready. Page-specific modules (js/pages/*.js) are loaded
 * separately, only on the pages that need them, and are added in
 * Phase 3 once page sections exist.
 */

import { initNavigation } from "./navigation.js";
import { initModals } from "./modal.js";
import { initForms } from "./forms.js";
import { initScrollAnimations } from "./animations.js";
import { initLazyLoad } from "./lazyload.js";
import { initSlider } from "./slider.js";
import { initTabs } from "./tabs.js";
import { initFloatingAvoid } from "./floating-avoid.js";

/**
 * Sets the current year in any element with [data-current-year],
 * used by the footer's copyright line.
 */
function initCurrentYear() {
  const targets = document.querySelectorAll("[data-current-year]");
  const year = String(new Date().getFullYear());
  targets.forEach((el) => {
    el.textContent = year;
  });
}

/**
 * Toggles the fixed scroll-to-top button's visibility and, on click,
 * scrolls smoothly back to the top of the page. Shared across every
 * page since the button markup is identical everywhere. Also toggles
 * `.has-scroll-top` on the right-side floating action group so the
 * Call button shifts up and never overlaps the scroll-to-top button
 * once both are visible (see components.css).
 */
function initScrollTop() {
  const btn = document.querySelector("[data-scroll-top]");
  const rightActions = document.querySelector(".floating-actions--right");
  if (!btn) return;

  const SHOW_AFTER_PX = 480;

  const toggleVisibility = () => {
    const isVisible = window.scrollY > SHOW_AFTER_PX;
    btn.classList.toggle("is-visible", isVisible);
    rightActions?.classList.toggle("has-scroll-top", isVisible);
  };

  window.addEventListener("scroll", toggleVisibility, { passive: true });
  toggleVisibility();

  btn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

/** Runs every shared module's init function once the DOM is ready. */
function init() {
  initCurrentYear();
  initScrollTop();
  initNavigation();
  initModals();
  initForms();
  initScrollAnimations();
  initLazyLoad();
  initSlider(); // no-op until a [data-slider] element exists (Phase 3 hero)
  initTabs(); // no-op until a [data-tabs] element exists (Phase 4 category pages)
  initFloatingAvoid(); // no-op until an element has [data-float-avoid] (homepage hero)
}

document.addEventListener("DOMContentLoaded", init);
