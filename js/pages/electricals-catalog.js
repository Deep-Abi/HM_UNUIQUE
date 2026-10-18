/**
 * electricals-catalog.js
 * Page-specific script for the Electricals product page.
 *
 * Owns one thing: a static data object describing every Electricals
 * sub-category and its placeholder products, plus a single reusable
 * render function that reads the selected category from that object
 * and updates the heading, description, and product grid in place —
 * no page reload, no navigation, no per-category HTML.
 *
 * This is deliberately written as a generic, reusable pattern (data
 * object + one render function + one click-delegation listener) so
 * the same shape can be copied for Electronics, Hardwares, and
 * Industrial & Commercial Equipment in later phases: only the CATALOG
 * object changes, the rendering/wiring logic does not.
 *
 * All product data below is placeholder content demonstrating the
 * category-switching functionality — not real HM UNIQUE product data.
 *
 * Written as a classic (non-module) script, wrapped in an IIFE, so it
 * runs correctly even when the page is opened directly from disk
 * (file://) rather than through a web server — ES module scripts
 * (type="module") are blocked by the browser's same-origin policy
 * under file://, which would otherwise make this feature silently
 * fail to run with no visible error.
 */
(function () {
  "use strict";

const CATALOG = {
  "wires-cables": {
    label: "Wires &amp; Cables",
    icon: "fa-plug",
    heading: "Popular Wires &amp; Cables",
    description: "Explore our most in-demand wires and cables built for performance and durability.",
    products: [
      {
        name: "FRLS Copper Wire H07Z1-K",
        specs: [
          ["Voltage Rating", "1100V"],
          ["Conductor", "Copper"],
          ["Insulation", "FRLS"],
          ["Available Sizes", "1 sq.mm &ndash; 240 sq.mm"],
          ["Application", "Industrial &amp; Building Wiring"],
        ],
      },
      {
        name: "XLPE Power Cable 1.1KV",
        specs: [
          ["Voltage Rating", "1.1KV"],
          ["Insulation", "XLPE"],
          ["Conductor", "Copper"],
          ["Core", "1 Core to 4 Core"],
          ["Application", "Power Distribution"],
        ],
      },
      {
        name: "Flexible House Wire (FR)",
        specs: [
          ["Voltage Rating", "1100V"],
          ["Insulation", "FR PVC"],
          ["Conductor", "Copper"],
          ["Available Sizes", "1 sq.mm &ndash; 16 sq.mm"],
          ["Application", "Residential Wiring"],
        ],
      },
      {
        name: "Armoured Cable (SWA)",
        specs: [
          ["Voltage Rating", "1.1KV / 3.3KV"],
          ["Insulation", "PVC / XLPE"],
          ["Conductor", "Copper"],
          ["Armouring", "Steel Wire Armour"],
          ["Application", "Outdoor &amp; Underground"],
        ],
      },
      {
        name: "Control Cable (Multi Core)",
        specs: [
          ["Voltage Rating", "1100V"],
          ["Insulation", "PVC"],
          ["Conductor", "Copper"],
          ["Core", "2 Core to 61 Core"],
          ["Application", "Control &amp; Signal Transmission"],
        ],
      },
      {
        name: "Submersible Pump Cable",
        specs: [
          ["Voltage Rating", "1100V"],
          ["Insulation", "PVC"],
          ["Conductor", "Copper"],
          ["Core", "3 Core / 4 Core"],
          ["Application", "Submersible Pumps"],
        ],
      },
      {
        name: "Co-Axial Cable RG6",
        specs: [
          ["Impedance", "75&Omega;"],
          ["Conductor", "Copper-Clad Steel"],
          ["Shielding", "Dual Shielded"],
          ["Length", "90m Coil"],
          ["Application", "TV &amp; Satellite Signal"],
        ],
      },
    ],
  },

  "switches-sockets": {
    label: "Switches &amp; Sockets",
    icon: "fa-toggle-on",
    heading: "Popular Switches &amp; Sockets",
    description: "Modular switches and sockets for residential, commercial and industrial installations.",
    products: [
      {
        name: "Modular Switch 6A (1-Way)",
        specs: [
          ["Rating", "6A, 240V"],
          ["Type", "1-Way Modular"],
          ["Material", "Polycarbonate"],
          ["Finish", "Matte White"],
          ["Application", "General Lighting Circuits"],
        ],
      },
      {
        name: "Universal Socket 6/16A",
        specs: [
          ["Rating", "6/16A, 240V"],
          ["Type", "Combined Universal Socket"],
          ["Shutter", "Child-Safe Shutter"],
          ["Material", "Fire-Retardant PC"],
          ["Application", "General Purpose Outlets"],
        ],
      },
      {
        name: "Industrial Socket 32A",
        specs: [
          ["Rating", "32A, 415V"],
          ["Poles", "3P + N + E"],
          ["Protection", "IP44"],
          ["Material", "Reinforced Nylon"],
          ["Application", "Industrial Power Outlets"],
        ],
      },
      {
        name: "Dimmer Switch 400W",
        specs: [
          ["Rating", "400W, 240V"],
          ["Type", "Rotary Dimmer"],
          ["Compatibility", "Incandescent &amp; LED (dimmable)"],
          ["Material", "Polycarbonate"],
          ["Application", "Ambient Lighting Control"],
        ],
      },
      {
        name: "Weatherproof Switch 16A",
        specs: [
          ["Rating", "16A, 240V"],
          ["Type", "1-Way Weatherproof"],
          ["Protection", "IP55"],
          ["Material", "UV-Stabilised PC"],
          ["Application", "Outdoor &amp; Wet Areas"],
        ],
      },
      {
        name: "TV/Data Socket Outlet",
        specs: [
          ["Type", "Coax + RJ45 Combo"],
          ["Impedance", "75&Omega; (TV)"],
          ["Material", "Fire-Retardant PC"],
          ["Finish", "Matte White"],
          ["Application", "Media &amp; Data Points"],
        ],
      },
      {
        name: "5-Pin Socket with Switch",
        specs: [
          ["Rating", "16A, 240V"],
          ["Type", "Switched Combined Socket"],
          ["Material", "Polycarbonate"],
          ["Finish", "Matte White"],
          ["Application", "General Purpose Outlets"],
        ],
      },
    ],
  },

  "mcb-rccb": {
    label: "MCB &amp; RCCB",
    icon: "fa-bolt",
    heading: "Popular MCB &amp; RCCB",
    description: "Circuit breakers and residual current devices for reliable overload and earth-fault protection.",
    products: [
      {
        name: "Single Pole MCB 32A",
        specs: [
          ["Rating", "32A"],
          ["Breaking Capacity", "10kA"],
          ["Curve Type", "C-Curve"],
          ["Poles", "1P"],
          ["Application", "Circuit Overload Protection"],
        ],
      },
      {
        name: "Double Pole RCCB 40A",
        specs: [
          ["Rating", "40A"],
          ["Sensitivity", "30mA"],
          ["Poles", "2P"],
          ["Breaking Capacity", "10kA"],
          ["Application", "Earth Leakage Protection"],
        ],
      },
      {
        name: "Triple Pole MCB 63A",
        specs: [
          ["Rating", "63A"],
          ["Breaking Capacity", "10kA"],
          ["Curve Type", "C-Curve"],
          ["Poles", "3P"],
          ["Application", "Three-Phase Circuit Protection"],
        ],
      },
      {
        name: "RCBO 32A / 30mA",
        specs: [
          ["Rating", "32A"],
          ["Sensitivity", "30mA"],
          ["Poles", "1P + N"],
          ["Function", "Combined Overload + Earth Leakage"],
          ["Application", "Single Circuit Protection"],
        ],
      },
      {
        name: "Isolator Switch 63A",
        specs: [
          ["Rating", "63A"],
          ["Poles", "4P"],
          ["Type", "Manual Isolator"],
          ["Breaking Capacity", "10kA"],
          ["Application", "Circuit Isolation"],
        ],
      },
      {
        name: "MCB Distribution Box 4-Way",
        specs: [
          ["Ways", "4-Way, Single Phase"],
          ["Material", "ABS Enclosure"],
          ["Protection", "IP40"],
          ["Mounting", "Surface"],
          ["Application", "Compact MCB Housing"],
        ],
      },
      {
        name: "Earth Leakage Circuit Breaker 25A",
        specs: [
          ["Rating", "25A"],
          ["Sensitivity", "100mA"],
          ["Poles", "2P"],
          ["Breaking Capacity", "6kA"],
          ["Application", "Fire &amp; Shock Protection"],
        ],
      },
    ],
  },

  "distribution-boards": {
    label: "Distribution Boards",
    icon: "fa-table-cells",
    heading: "Popular Distribution Boards",
    description: "Metal-clad distribution boards for organised, safe circuit distribution in any installation.",
    products: [
      {
        name: "8-Way SPN Distribution Board",
        specs: [
          ["Ways", "8-Way, Single Phase"],
          ["Material", "CRCA Sheet Steel"],
          ["Protection", "IP43"],
          ["Mounting", "Surface / Flush"],
          ["Application", "Residential &amp; Small Commercial"],
        ],
      },
      {
        name: "12-Way TPN Distribution Board",
        specs: [
          ["Ways", "12-Way, Three Phase"],
          ["Material", "CRCA Sheet Steel"],
          ["Protection", "IP43"],
          ["Mounting", "Surface / Flush"],
          ["Application", "Commercial Installations"],
        ],
      },
      {
        name: "24-Way TPN Distribution Board",
        specs: [
          ["Ways", "24-Way, Three Phase"],
          ["Material", "CRCA Sheet Steel"],
          ["Protection", "IP43"],
          ["Mounting", "Surface"],
          ["Application", "Industrial Installations"],
        ],
      },
      {
        name: "Metering Distribution Board",
        specs: [
          ["Ways", "6-Way, Single Phase"],
          ["Material", "CRCA Sheet Steel"],
          ["Feature", "Integrated Meter Compartment"],
          ["Protection", "IP43"],
          ["Application", "Metered Residential Supply"],
        ],
      },
      {
        name: "Outdoor Distribution Board",
        specs: [
          ["Ways", "12-Way, Three Phase"],
          ["Material", "GRP Enclosure"],
          ["Protection", "IP65"],
          ["Mounting", "Pole / Wall Mount"],
          ["Application", "Outdoor Power Distribution"],
        ],
      },
      {
        name: "Modular Consumer Unit 6-Way",
        specs: [
          ["Ways", "6-Way, Single Phase"],
          ["Material", "Polycarbonate Enclosure"],
          ["Protection", "IP40"],
          ["Mounting", "Flush"],
          ["Application", "Residential Consumer Unit"],
        ],
      },
      {
        name: "18-Way TPN Distribution Board",
        specs: [
          ["Ways", "18-Way, Three Phase"],
          ["Material", "CRCA Sheet Steel"],
          ["Protection", "IP43"],
          ["Mounting", "Surface / Flush"],
          ["Application", "Mid-Size Commercial Installations"],
        ],
      },
    ],
  },

  "lighting-solutions": {
    label: "Lighting Solutions",
    icon: "fa-lightbulb",
    heading: "Popular Lighting Solutions",
    description: "Professional indoor, outdoor and industrial lighting solutions designed for commercial and industrial applications.",
    products: [
      {
        name: "LED High Bay Light 150W",
        specs: [
          ["Power", "150W"],
          ["Lumen Output", "18,000 lm"],
          ["Voltage", "100&ndash;277V"],
          ["IP Rating", "IP65"],
          ["Application", "Industrial &amp; Warehouse Lighting"],
        ],
      },
      {
        name: "LED Street Light 90W",
        specs: [
          ["Power", "90W"],
          ["Lumen Output", "10,800 lm"],
          ["Voltage", "100&ndash;277V"],
          ["IP Rating", "IP66"],
          ["Application", "Roadway &amp; Area Lighting"],
        ],
      },
      {
        name: "LED Panel Light 40W",
        specs: [
          ["Power", "40W"],
          ["Size", "600mm x 600mm"],
          ["Voltage", "220&ndash;240V"],
          ["Colour Temp", "4000K / 6500K"],
          ["Application", "Office &amp; Commercial Interiors"],
        ],
      },
      {
        name: "LED Flood Light 200W",
        specs: [
          ["Power", "200W"],
          ["Lumen Output", "24,000 lm"],
          ["IP Rating", "IP66"],
          ["Beam Angle", "120&deg;"],
          ["Application", "Outdoor &amp; Facade Lighting"],
        ],
      },
      {
        name: "LED Batten Light 20W",
        specs: [
          ["Power", "20W"],
          ["Length", "4 ft"],
          ["Lumen Output", "2,200 lm"],
          ["Colour Temp", "6500K"],
          ["Application", "General Indoor Lighting"],
        ],
      },
      {
        name: "Emergency Exit Light",
        specs: [
          ["Power", "3W LED"],
          ["Backup", "90 Minutes (Battery)"],
          ["Mounting", "Wall / Ceiling"],
          ["Rating", "IP20"],
          ["Application", "Emergency &amp; Exit Signage"],
        ],
      },
      {
        name: "Solar Garden Light",
        specs: [
          ["Power", "5W LED"],
          ["Battery", "Integrated Solar + Li-ion"],
          ["Rating", "IP65"],
          ["Sensor", "Dusk-to-Dawn Auto"],
          ["Application", "Garden &amp; Pathway Lighting"],
        ],
      },
    ],
  },

  "conduits-accessories": {
    label: "Conduits &amp; Accessories",
    icon: "fa-wrench",
    heading: "Popular Conduits &amp; Accessories",
    description: "PVC and metal conduit systems and fittings for safe, organised electrical wiring runs.",
    products: [
      {
        name: "PVC Conduit Pipe 25mm",
        specs: [
          ["Size", "25mm"],
          ["Material", "Rigid PVC"],
          ["Length", "3m per length"],
          ["Rating", "Flame Retardant"],
          ["Application", "Concealed &amp; Surface Wiring"],
        ],
      },
      {
        name: "Flexible Conduit 20mm",
        specs: [
          ["Size", "20mm"],
          ["Material", "PVC Corrugated"],
          ["Length", "25m Coil"],
          ["Rating", "Flame Retardant"],
          ["Application", "Flexible Cable Routing"],
        ],
      },
      {
        name: "Conduit Bend &amp; Coupler Set",
        specs: [
          ["Size", "25mm"],
          ["Material", "Rigid PVC"],
          ["Includes", "Bends, Couplers, Clips"],
          ["Rating", "Flame Retardant"],
          ["Application", "Conduit Line Accessories"],
        ],
      },
      {
        name: "GI Conduit Pipe 25mm",
        specs: [
          ["Size", "25mm"],
          ["Material", "Galvanised Iron"],
          ["Length", "3m per length"],
          ["Finish", "Hot-Dip Galvanised"],
          ["Application", "Heavy-Duty &amp; Outdoor Wiring"],
        ],
      },
      {
        name: "Conduit Junction Box",
        specs: [
          ["Size", "75mm x 75mm"],
          ["Material", "PVC"],
          ["Entries", "4-Way Knockout"],
          ["Rating", "Flame Retardant"],
          ["Application", "Conduit Line Junctions"],
        ],
      },
      {
        name: "Cable Grommets Pack",
        specs: [
          ["Size", "20mm &ndash; 32mm"],
          ["Material", "Rubber"],
          ["Pack Size", "20 pcs"],
          ["Rating", "Flame Retardant"],
          ["Application", "Panel Cable Entry Protection"],
        ],
      },
      {
        name: "PVC Conduit Saddle Clips",
        specs: [
          ["Size", "20mm &ndash; 25mm"],
          ["Material", "PVC"],
          ["Pack Size", "50 pcs"],
          ["Rating", "Flame Retardant"],
          ["Application", "Conduit Surface Fixing"],
        ],
      },
    ],
  },

  "electrical-accessories": {
    label: "Electrical Accessories",
    icon: "fa-box",
    heading: "Popular Electrical Accessories",
    description: "Essential accessories and hardware to complete every electrical installation.",
    products: [
      {
        name: "Cable Gland Set (Brass)",
        specs: [
          ["Size", "20mm &ndash; 32mm"],
          ["Material", "Nickel-Plated Brass"],
          ["Rating", "IP68"],
          ["Includes", "Gland, Locknut, Washer"],
          ["Application", "Cable Entry Sealing"],
        ],
      },
      {
        name: "Cable Ties (Nylon) Pack",
        specs: [
          ["Length", "100mm &ndash; 300mm"],
          ["Material", "UV-Resistant Nylon"],
          ["Tensile Strength", "Up to 50kg"],
          ["Pack Size", "100 pcs"],
          ["Application", "Cable Bundling &amp; Routing"],
        ],
      },
      {
        name: "Insulation Tape (PVC)",
        specs: [
          ["Width", "19mm"],
          ["Length", "10m per roll"],
          ["Material", "PVC Self-Adhesive"],
          ["Rating", "Flame Retardant"],
          ["Application", "Cable Joint Insulation"],
        ],
      },
      {
        name: "Terminal Connector Block",
        specs: [
          ["Rating", "20A, 450V"],
          ["Poles", "12-Way"],
          ["Material", "Polyamide"],
          ["Mounting", "DIN Rail"],
          ["Application", "Wire Termination &amp; Junctions"],
        ],
      },
      {
        name: "Heat Shrink Tubing Set",
        specs: [
          ["Diameter", "3mm &ndash; 12mm"],
          ["Material", "Polyolefin"],
          ["Shrink Ratio", "2:1"],
          ["Pack Size", "10 pcs (assorted)"],
          ["Application", "Cable Joint &amp; Insulation"],
        ],
      },
      {
        name: "MC4 Solar Connector Pair",
        specs: [
          ["Rating", "30A, 1000V DC"],
          ["Type", "MC4 Male/Female Pair"],
          ["Protection", "IP67"],
          ["Material", "PC/PA with Copper Contacts"],
          ["Application", "Solar Panel Wiring"],
        ],
      },
      {
        name: "Cable Lug Set (Copper)",
        specs: [
          ["Size", "1.5 sq.mm &ndash; 50 sq.mm"],
          ["Material", "Tinned Copper"],
          ["Type", "Ring &amp; Fork Lugs"],
          ["Pack Size", "50 pcs (assorted)"],
          ["Application", "Cable Termination"],
        ],
      },
    ],
  },
};

const CATALOGUE_PDF_HREF = "../assets/catalogue/electricals-catalogue.pdf";

/**
 * Builds this category's PDF reference. The Electricals page has one
 * real catalogue file covering every sub-category (there is no
 * separate physical PDF per sub-category yet) — rather than either
 * (a) reusing one identical, undifferentiated link for every category
 * or (b) inventing file paths that don't exist and would 404, each
 * category gets its own URL fragment on the same real file. This is
 * a genuine, non-broken, category-specific reference today, and the
 * one line to change once real per-category catalogues exist.
 */
function catalogueHrefFor(categoryKey) {
  return `${CATALOGUE_PDF_HREF}#${categoryKey}`;
}

/** Builds the specs <ul> markup for one product — identical markup
 * shape to the site's existing static product cards. */
function renderSpecs(specs) {
  return specs
    .map(
      ([label, value]) =>
        `<li><i class="fa-solid fa-check" aria-hidden="true"></i><span><strong>${label}:</strong> ${value}</span></li>`
    )
    .join("\n");
}

/** Builds one product card's markup — identical structure/classes to
 * the site's existing static .product-card markup, so zero new CSS
 * is required. The Request Quote button carries the product's own
 * name in a data attribute so the quote-modal pre-fill listener
 * (below) can identify exactly which product the enquiry is about. */
function renderProductCard(product, categoryKey) {
  // Note: deliberately NOT carrying data-animate="fade-up" here. That
  // attribute drives animations.js's IntersectionObserver-based
  // scroll-reveal, which only scans the page once at load and never
  // re-scans for elements added later — any card rendered dynamically
  // here would inherit [data-animate]'s CSS (opacity: 0) but never
  // receive the .is-visible class that makes it visible again,
  // leaving every dynamically-rendered card permanently invisible.
  // This section already has its own dedicated fade transition
  // (transitionToCategory, below), so no scroll-reveal is needed here.
  return `<article class="card card--hover product-card">
            <div class="product-card__media">
              <div class="aspect-box aspect-box--square" role="img" aria-label="${product.name} product image — placeholder, pending final product photography">
                <div class="img-placeholder"><i class="fa-regular fa-image" aria-hidden="true"></i></div>
              </div>
            </div>
            <h3 class="product-card__title">${product.name}</h3>
            <ul class="card__specs">
${renderSpecs(product.specs)}
            </ul>
            <div class="card__actions">
              <a class="btn btn--outline btn--sm" href="${catalogueHrefFor(categoryKey)}" download>
                <i class="fa-solid fa-download" aria-hidden="true"></i>
                Download PDF
              </a>
              <button type="button" class="btn btn--primary btn--sm" data-modal-open="quote" data-catalog-quote-trigger data-product-name="${product.name}">Request Quote</button>
            </div>
          </article>`;
}

/**
 * Renders one category into the page — heading, description, product
 * grid, AND the two section-level blocks that must stay in sync with
 * it (the "Looking for more products?" prompt and the catalogue
 * download band's heading + PDF link). This is the single reusable
 * render function: every category (current and future) flows through
 * this same path, and every part of what the task calls the "complete
 * product-section structure" is updated together, atomically, so
 * nothing is ever left showing stale content from the previous
 * category or disappears mid-switch.
 */
function renderCategory(categoryKey, els) {
  const category = CATALOG[categoryKey];
  if (!category) return;

  const plainLabel = category.label.replace(/&amp;/g, "&");

  els.heading.innerHTML = category.heading;
  els.description.innerHTML = category.description;
  els.grid.innerHTML = category.products.map((p) => renderProductCard(p, categoryKey)).join("\n");

  if (els.inlineTitle) {
    els.inlineTitle.textContent = `Looking for more ${plainLabel} products?`;
  }
  if (els.catalogueHeading) {
    els.catalogueHeading.innerHTML = `Download Complete<br />${category.label} Catalogue`;
  }
  if (els.cataloguePdf) {
    els.cataloguePdf.setAttribute("href", catalogueHrefFor(categoryKey));
  }
}

/**
 * Fade-out → render → fade-in transition, matching the site's
 * existing lightweight animation vocabulary (CSS opacity transition,
 * no animation library). Re-renders after the fade-out completes so
 * the swap itself is never visible. Only the dynamic product-section
 * elements transition — the rest of the page (hero, nav, footer,
 * stats strip, etc.) never animates.
 */
function transitionToCategory(categoryKey, els) {
  const FADE_MS = 180;
  const fadeTargets = [els.grid, els.heading, els.description, els.inlineTitle, els.catalogueHeading].filter(Boolean);

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

/**
 * Pre-fills the existing Request a Quote modal with this page's
 * context whenever it's opened from inside the dynamic product
 * section — the Product Category select is always "Electricals" on
 * this page, and the optional Product Name field is set to either the
 * specific product clicked (from a product card) or the active
 * category's label (from the section-level "Request a Quote"
 * button, which has no single product in view). This never creates a
 * second modal or duplicates modal.js's own open/close logic — it
 * only fills in fields on the one existing modal before it opens.
 */
function initQuotePrefill(getActiveCategoryLabel) {
  const categoryField = document.getElementById("quote-category");
  const productField = document.getElementById("quote-product");
  if (!categoryField || !productField) return;

  document.addEventListener("click", (event) => {
    const trigger = event.target.closest("[data-catalog-quote-trigger]");
    if (!trigger) return;

    categoryField.value = "electricals";

    const productName = trigger.dataset.productName;
    productField.value = productName || getActiveCategoryLabel();
  });
}

function initElectricalsCatalog() {
  const tabsEl = document.querySelector("[data-catalog-tabs]");
  const heading = document.querySelector("[data-catalog-heading]");
  const description = document.querySelector("[data-catalog-description]");
  const grid = document.querySelector("[data-catalog-grid]");
  const inlineTitle = document.querySelector("[data-catalog-inline-title]");
  const catalogueHeading = document.querySelector("[data-catalog-catalogue-heading]");
  const cataloguePdf = document.querySelector("[data-catalog-catalogue-pdf]");

  if (!tabsEl || !heading || !description || !grid) return;

  const els = { heading, description, grid, inlineTitle, catalogueHeading, cataloguePdf };
  let activeCategory = tabsEl.querySelector(".category-tabs__item.is-active")?.dataset.category
    || Object.keys(CATALOG)[0];

  // Product cards, the catalogue band, and the "looking for more
  // products" prompt are all rendered/synced by JavaScript on load,
  // per the task's requirement that the complete section — not just
  // the cards — reflects the default category immediately.
  renderCategory(activeCategory, els);
  initQuotePrefill(() => CATALOG[activeCategory].label.replace(/&amp;/g, "&"));

  tabsEl.addEventListener("click", (event) => {
    const button = event.target.closest(".category-tabs__item");
    if (!button || !tabsEl.contains(button)) return;

    const categoryKey = button.dataset.category;
    if (!categoryKey || categoryKey === activeCategory || !CATALOG[categoryKey]) return;

    tabsEl.querySelectorAll(".category-tabs__item").forEach((btn) => {
      const isSelected = btn === button;
      btn.classList.toggle("is-active", isSelected);
      if (isSelected) {
        btn.setAttribute("aria-current", "true");
      } else {
        btn.removeAttribute("aria-current");
      }
    });

    // Core functionality (re-rendering the product grid) happens
    // first and unconditionally. The scroll-into-view below is a
    // cosmetic nicety only — wrapped defensively so that if it's
    // ever unavailable or throws in some environment, it can never
    // prevent the actual category switch from completing.
    activeCategory = categoryKey;
    transitionToCategory(categoryKey, els);

    try {
      button.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    } catch (err) {
      /* no-op — scrolling is cosmetic only, never block on it */
    }
  });
}

// Classic scripts (no type="module") don't wait for DOMContentLoaded
// automatically the way modules effectively do when placed at the
// end of <body> — the browser may already be past that event by the
// time this script (loaded with `defer`) runs, or not, depending on
// timing. Handle both cases explicitly.
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initElectricalsCatalog);
} else {
  initElectricalsCatalog();
}
})();
