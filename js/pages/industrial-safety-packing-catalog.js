/**
 * industrial-safety-packing-catalog.js
 * Page-specific script for the Industrial Safety & Packing Materials page.
 * Same reusable architecture as the other category scripts (a CATALOG data
 * object, one render function, one transition function, one click-delegation
 * listener, one quote-modal pre-fill listener).
 *
 * NO PRODUCT DATA EXISTS YET. The seven groups below are PROVISIONAL grouping
 * labels, not verified inventory, and every group has an empty `products`
 * array, so each tab renders an honest "coming soon" panel with an image
 * placeholder. When approved products are supplied, add them to a group's
 * `products` array ({ name, specs: [[label, value], ...] }) and the grid
 * renders cards for them instead (no catalogue PDF is linked: none exists).
 *
 * Written as a classic (non-module) script, wrapped in an IIFE, so it runs
 * correctly even when the page is opened directly from disk (file://).
 */
(function () {
  "use strict";

const CATALOG = {
  "personal-protective-equipment": {
    label: "Personal Protective Equipment",
    heading: "Personal Protective Equipment",
    description: "Our product listing for this group is being prepared. Contact us for availability and details.",
    products: [],
  },

  "safety-footwear-head-protection": {
    label: "Safety Footwear &amp; Head Protection",
    heading: "Safety Footwear &amp; Head Protection",
    description: "Our product listing for this group is being prepared. Contact us for availability and details.",
    products: [],
  },

  "eye-face-hearing-protection": {
    label: "Eye, Face &amp; Hearing Protection",
    heading: "Eye, Face &amp; Hearing Protection",
    description: "Our product listing for this group is being prepared. Contact us for availability and details.",
    products: [],
  },

  "workplace-safety-signage": {
    label: "Workplace Safety &amp; Signage",
    heading: "Workplace Safety &amp; Signage",
    description: "Our product listing for this group is being prepared. Contact us for availability and details.",
    products: [],
  },

  "tapes-adhesives": {
    label: "Tapes &amp; Adhesives",
    heading: "Tapes &amp; Adhesives",
    description: "Our product listing for this group is being prepared. Contact us for availability and details.",
    products: [],
  },

  "wrapping-cushioning-materials": {
    label: "Wrapping &amp; Cushioning Materials",
    heading: "Wrapping &amp; Cushioning Materials",
    description: "Our product listing for this group is being prepared. Contact us for availability and details.",
    products: [],
  },

  "boxes-strapping-packing-accessories": {
    label: "Boxes, Strapping &amp; Packing Accessories",
    heading: "Boxes, Strapping &amp; Packing Accessories",
    description: "Our product listing for this group is being prepared. Contact us for availability and details.",
    products: [],
  },
};

const QUOTE_CATEGORY_VALUE = "safety-packing";

function placeholderMarkup(label, ratioClass) {
  return `<div class="aspect-box ${ratioClass}" role="img" aria-label="${label} image — placeholder, pending approved photography">
                <div class="img-placeholder"><i class="fa-regular fa-image" aria-hidden="true"></i></div>
              </div>`;
}

function renderSpecs(specs) {
  return specs
    .map(
      ([label, value]) =>
        `<li><i class="fa-solid fa-check" aria-hidden="true"></i><span><strong>${label}:</strong> ${value}</span></li>`
    )
    .join("\n");
}

function renderProductCard(product, categoryLabel) {
  return `<article class="card card--hover product-card">
            <div class="product-card__media">
              ${placeholderMarkup(product.name, "aspect-box--square")}
            </div>
            <h3 class="product-card__title">${product.name}</h3>
            <ul class="card__specs">
${renderSpecs(product.specs || [])}
            </ul>
            <div class="card__actions">
              <button type="button" class="btn btn--primary btn--sm" data-modal-open="quote" data-catalog-quote-trigger data-product-name="${product.name}">Request Quote</button>
            </div>
          </article>`;
}

function renderEmptyState(category) {
  return `<div class="catalog-empty" data-catalog-empty>
            <div class="catalog-empty__media">
              ${placeholderMarkup(category.label, "aspect-box--wide")}
            </div>
            <div class="catalog-empty__body">
              <h3 class="catalog-empty__title">Products coming soon</h3>
              <p>We have not published products for ${category.label} yet. Contact us to discuss your requirements.</p>
              <div class="catalog-empty__actions">
                <button type="button" class="btn btn--primary" data-modal-open="quote" data-catalog-quote-trigger data-product-name="${category.label}">Request a Quote</button>
                <a class="btn btn--outline" href="contact.html">Contact Us</a>
              </div>
            </div>
          </div>`;
}

function renderCategory(categoryKey, els) {
  const category = CATALOG[categoryKey];
  if (!category) return;

  els.heading.innerHTML = category.heading;
  els.description.innerHTML = category.description;
  els.grid.innerHTML = category.products.length
    ? category.products.map((p) => renderProductCard(p, category.label)).join("\n")
    : renderEmptyState(category);

  if (els.inlineTitle) {
    els.inlineTitle.innerHTML = `Looking for ${category.label}?`;
  }
}

function transitionToCategory(categoryKey, els) {
  const FADE_MS = 180;
  const fadeTargets = [els.grid, els.heading, els.description, els.inlineTitle].filter(Boolean);

  fadeTargets.forEach((el) => {
    el.style.transition = `opacity ${FADE_MS}ms ease`;
    el.style.opacity = "0";
  });

  window.setTimeout(() => {
    renderCategory(categoryKey, els);
    fadeTargets.forEach((el) => {
      el.style.opacity = "1";
    });
  }, FADE_MS);
}

function initQuotePrefill(getActiveCategoryLabel) {
  const categoryField = document.getElementById("quote-category");
  const productField = document.getElementById("quote-product");
  if (!categoryField || !productField) return;

  document.addEventListener("click", (event) => {
    const trigger = event.target.closest("[data-catalog-quote-trigger]");
    if (!trigger) return;

    categoryField.value = QUOTE_CATEGORY_VALUE;

    const productName = trigger.dataset.productName;
    productField.value = productName || getActiveCategoryLabel();
  });
}

function initSafetyPackingCatalog() {
  const tabsEl = document.querySelector("[data-catalog-tabs]");
  const heading = document.querySelector("[data-catalog-heading]");
  const description = document.querySelector("[data-catalog-description]");
  const grid = document.querySelector("[data-catalog-grid]");
  const inlineTitle = document.querySelector("[data-catalog-inline-title]");

  if (!tabsEl || !heading || !description || !grid) return;

  const els = { heading, description, grid, inlineTitle };
  let activeCategory = tabsEl.querySelector(".category-tabs__item.is-active")?.dataset.category
    || Object.keys(CATALOG)[0];

  renderCategory(activeCategory, els);
  initQuotePrefill(() => CATALOG[activeCategory].label.replace(/&amp;/g, "&"));

  const tabButtons = () => Array.from(tabsEl.querySelectorAll(".category-tabs__item"));

  function setActiveTab(categoryKey) {
    let activeButton = null;
    tabButtons().forEach((btn) => {
      const isSelected = btn.dataset.category === categoryKey;
      btn.classList.toggle("is-active", isSelected);
      if (isSelected) {
        btn.setAttribute("aria-current", "true");
        activeButton = btn;
      } else {
        btn.removeAttribute("aria-current");
      }
    });
    return activeButton;
  }

  tabsEl.addEventListener("click", (event) => {
    const button = event.target.closest(".category-tabs__item");
    if (!button || !tabsEl.contains(button)) return;

    const categoryKey = button.dataset.category;
    if (!categoryKey || categoryKey === activeCategory || !CATALOG[categoryKey]) return;

    setActiveTab(categoryKey);
    activeCategory = categoryKey;
    transitionToCategory(categoryKey, els);

    try {
      button.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    } catch (err) {
      /* no-op — scrolling is cosmetic only, never block on it */
    }
  });

  // Direct links: pages/industrial-safety-packing.html#<group key> (the
  // homepage's three Safety & Packing cards use these) open that group. The
  // fragment is the same key as the tab's data-category. Anything that is not
  // a known key (for example #main-content from the skip link) is ignored, so
  // the page keeps its first group and the browser's own anchor behaviour.
  const keyFromHash = () => {
    let raw = window.location.hash.replace(/^#/, "");
    try {
      raw = decodeURIComponent(raw);
    } catch (err) {
      /* malformed escape: treat as unknown */
    }
    return Object.prototype.hasOwnProperty.call(CATALOG, raw) ? raw : null;
  };

  function revealActiveGroup(button, smooth) {
    // Centre the active tab inside the strip first (the strip scrolls sideways
    // on narrow screens), THEN bring the strip's own section to just under the
    // sticky header (the root scroll-padding-top covers the header). The order
    // matters: a second scrollIntoView would cancel a smooth one still running.
    // Arriving from another page jumps straight there; a hash change on the
    // open page scrolls smoothly. Reduced motion always jumps.
    const reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    // "instant" (not "auto"): the root has scroll-behavior: smooth, which "auto" would follow.
    const behavior = smooth && !reduced ? "smooth" : "instant";
    try {
      button.scrollIntoView({ behavior: "instant", inline: "center", block: "nearest" });
      (tabsEl.closest("section") || tabsEl).scrollIntoView({ behavior, block: "start" });
    } catch (err) {
      /* no-op — scrolling is cosmetic only, never block on it */
    }
  }

  function openGroupFromHash(smooth) {
    const key = keyFromHash();
    if (!key) return;
    const button = setActiveTab(key);
    if (!button) return;
    if (key !== activeCategory) {
      activeCategory = key;
      renderCategory(key, els);
    }
    revealActiveGroup(button, smooth === true);
    return button;
  }

  const landedOn = openGroupFromHash(false);
  if (landedOn) {
    // Layout above the strip can still settle (web fonts) once the page has
    // loaded; re-align once, unless the visitor has already moved on.
    const hashAtLanding = window.location.hash;
    window.addEventListener(
      "load",
      () => {
        if (window.location.hash === hashAtLanding && !window.__hmUserScrolled) revealActiveGroup(landedOn, false);
      },
      { once: true }
    );
    const markScrolled = () => {
      window.__hmUserScrolled = true;
    };
    ["wheel", "touchstart", "keydown", "mousedown"].forEach((ev) =>
      window.addEventListener(ev, markScrolled, { once: true, passive: true })
    );
  }
  window.addEventListener("hashchange", () => openGroupFromHash(true));
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initSafetyPackingCatalog);
} else {
  initSafetyPackingCatalog();
}
})();
