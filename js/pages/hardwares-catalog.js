/**
 * hardwares-catalog.js
 * Page-specific script for the Hardwares product page. Same reusable
 * architecture as electricals-catalog.js — a data object, one render
 * function, one transition function, one click-delegation listener,
 * one quote-modal pre-fill listener.
 *
 * All product data below is placeholder content demonstrating the
 * category-switching functionality — not real HM UNIQUE product data.
 *
 * Written as a classic (non-module) script, wrapped in an IIFE, so it
 * runs correctly even when the page is opened directly from disk
 * (file://) rather than through a web server.
 */
(function () {
  "use strict";

const CATALOG = {
  "fasteners": {
    label: "Fasteners",
    heading: "Popular Fasteners",
    description: "Bolts, nuts, screws and rivets built for strength and reliable, long-lasting joints.",
    products: [
      { name: "Hex Bolt &amp; Nut M8", specs: [["Material", "Mild Steel"], ["Finish", "Zinc Plated"], ["Size Range", "M6 &ndash; M20"], ["Application", "General Fastening"]] },
      { name: "Stainless Steel Bolt &amp; Nut", specs: [["Material", "SS 304"], ["Type", "Hex Head"], ["Size Range", "M6 &ndash; M20"], ["Application", "Corrosion-Resistant Fastening"]] },
      { name: "Self Drilling Screw", specs: [["Material", "Carbon Steel"], ["Finish", "Zinc Plated"], ["Size Range", "3.5mm &ndash; 6.3mm"], ["Application", "Metal-to-Metal Fixing"]] },
      { name: "Blind Rivet (Pop Rivet)", specs: [["Material", "Aluminium / Steel"], ["Finish", "Natural / Zinc Plated"], ["Size Range", "3.2mm &ndash; 6.4mm"], ["Application", "Sheet Metal Joining"]] },
      { name: "Carriage Bolt M10", specs: [["Material", "Mild Steel"], ["Finish", "Zinc Plated"], ["Head Type", "Round Head, Square Neck"], ["Application", "Wood &amp; Metal Fastening"]] },
      { name: "Wing Nut M8", specs: [["Material", "Stainless Steel"], ["Type", "Hand-Tightening Nut"], ["Size Range", "M4 &ndash; M12"], ["Application", "Tool-Free Fastening"]] },
      { name: "Washer Set (Flat &amp; Spring)", specs: [["Material", "Steel"], ["Finish", "Zinc Plated"], ["Size Range", "M6 &ndash; M20"], ["Application", "Load Distribution &amp; Locking"]] },
    ],
  },

  "hand-tools": {
    label: "Hand Tools",
    heading: "Popular Hand Tools",
    description: "Durable hand tools built for everyday construction, maintenance and workshop use.",
    products: [
      { name: "Claw Hammer 500g", specs: [["Weight", "500g"], ["Handle", "Fibreglass"], ["Head Material", "Forged Steel"], ["Application", "General Carpentry"]] },
      { name: "Adjustable Wrench 10&Prime;", specs: [["Size", "10&Prime;"], ["Material", "Chrome Vanadium Steel"], ["Jaw Capacity", "Up to 30mm"], ["Application", "General Fastening"]] },
      { name: "Screwdriver Set (6-Piece)", specs: [["Pieces", "6"], ["Tip Types", "Phillips &amp; Flat"], ["Handle", "Anti-Slip Grip"], ["Application", "General Assembly"]] },
      { name: "Combination Plier 8&Prime;", specs: [["Size", "8&Prime;"], ["Material", "Drop-Forged Steel"], ["Handle", "Insulated Grip"], ["Application", "Cutting &amp; Gripping"]] },
      { name: "Measuring Tape 5m", specs: [["Length", "5m"], ["Blade Width", "25mm"], ["Case", "Impact-Resistant ABS"], ["Application", "Site Measurement"]] },
      { name: "Spirit Level 24&Prime;", specs: [["Length", "24&Prime;"], ["Material", "Aluminium Frame"], ["Vials", "3 (Level, Plumb, 45&deg;)"], ["Application", "Alignment Checking"]] },
      { name: "Hacksaw Frame with Blade", specs: [["Frame", "Adjustable Steel"], ["Blade Length", "12&Prime;"], ["Handle", "Ergonomic Grip"], ["Application", "Metal &amp; Pipe Cutting"]] },
    ],
  },

  "power-tools": {
    label: "Power Tools",
    heading: "Popular Power Tools",
    description: "Corded and cordless power tools for drilling, cutting and fastening on any job site.",
    products: [
      { name: "Cordless Drill Driver 18V", specs: [["Voltage", "18V Li-ion"], ["Chuck Size", "10mm"], ["Torque Settings", "21+1"], ["Application", "Drilling &amp; Driving"]] },
      { name: "Angle Grinder 4&Prime;", specs: [["Power", "750W"], ["Disc Size", "4&Prime; (100mm)"], ["Speed", "11,000 RPM"], ["Application", "Cutting &amp; Grinding"]] },
      { name: "Rotary Hammer Drill (SDS+)", specs: [["Power", "800W"], ["Chuck Type", "SDS-Plus"], ["Impact Energy", "2.7J"], ["Application", "Concrete Drilling"]] },
      { name: "Circular Saw 7&Prime;", specs: [["Power", "1200W"], ["Blade Size", "7&Prime; (185mm)"], ["Cutting Depth", "Up to 65mm"], ["Application", "Wood &amp; Board Cutting"]] },
      { name: "Jigsaw (Variable Speed)", specs: [["Power", "500W"], ["Stroke Rate", "500 &ndash; 3000 SPM"], ["Cutting Depth", "Up to 65mm (Wood)"], ["Application", "Curved &amp; Straight Cuts"]] },
      { name: "Bench Grinder 6&Prime;", specs: [["Power", "350W"], ["Wheel Size", "6&Prime; (150mm)"], ["Speed", "2850 RPM"], ["Application", "Sharpening &amp; Deburring"]] },
      { name: "Heat Gun (Dual Temperature)", specs: [["Power", "2000W"], ["Temperature", "300&deg;C / 500&deg;C"], ["Airflow", "Dual Setting"], ["Application", "Paint Stripping &amp; Shrink Fitting"]] },
    ],
  },

  "plumbing-fittings": {
    label: "Plumbing Fittings",
    heading: "Popular Plumbing Fittings",
    description: "Valves, taps and fittings for dependable water supply and drainage systems.",
    products: [
      { name: "Ball Valve 1&Prime; (Brass)", specs: [["Size", "1&Prime;"], ["Material", "Brass"], ["Pressure Rating", "PN25"], ["Application", "Water Flow Control"]] },
      { name: "PVC Elbow Fitting 90&deg;", specs: [["Size", "20mm &ndash; 110mm"], ["Material", "uPVC"], ["Angle", "90&deg;"], ["Application", "Pipe Direction Change"]] },
      { name: "Pillar Tap (Chrome Plated)", specs: [["Material", "Brass, Chrome Plated"], ["Type", "Single Pillar Tap"], ["Connection", "1/2&Prime; BSP"], ["Application", "Wash Basin Water Supply"]] },
      { name: "Gate Valve 1&Prime; (Cast Iron)", specs: [["Size", "1&Prime;"], ["Material", "Cast Iron Body"], ["Pressure Rating", "PN16"], ["Application", "Main Line Water Shut-Off"]] },
      { name: "Flexible Hose Pipe (Braided)", specs: [["Length", "30cm &ndash; 100cm"], ["Material", "SS Braided, PVC Core"], ["Connection", "1/2&Prime; BSP"], ["Application", "Tap &amp; Appliance Connection"]] },
      { name: "Foot Valve 1.5&Prime;", specs: [["Size", "1.5&Prime;"], ["Material", "Cast Iron / Plastic"], ["Type", "Non-Return Foot Valve"], ["Application", "Pump Suction Line"]] },
      { name: "PTFE Thread Seal Tape", specs: [["Width", "12mm"], ["Length", "12m Roll"], ["Material", "PTFE"], ["Application", "Threaded Joint Sealing"]] },
    ],
  },

  "pipes-fittings": {
    label: "Pipes &amp; Fittings",
    heading: "Popular Pipes &amp; Fittings",
    description: "PVC, CPVC and GI pipes and fittings for water supply, drainage and industrial piping.",
    products: [
      { name: "uPVC Pipe 4&Prime; (Schedule 40)", specs: [["Size", "4&Prime;"], ["Material", "uPVC"], ["Length", "3m per length"], ["Application", "Drainage &amp; Water Supply"]] },
      { name: "CPVC Hot Water Pipe 1/2&Prime;", specs: [["Size", "1/2&Prime;"], ["Material", "CPVC"], ["Temperature Rating", "Up to 93&deg;C"], ["Application", "Hot Water Plumbing"]] },
      { name: "GI Pipe 1&Prime; (Medium Class)", specs: [["Size", "1&Prime;"], ["Material", "Galvanised Iron"], ["Class", "Medium (B)"], ["Application", "Water Supply &amp; Structural Use"]] },
      { name: "PVC Pipe Coupler", specs: [["Size", "20mm &ndash; 110mm"], ["Material", "uPVC"], ["Type", "Solvent Weld Coupler"], ["Application", "Pipe Joint Connection"]] },
      { name: "SWR Pipe 4&Prime;", specs: [["Size", "4&Prime;"], ["Material", "PVC"], ["Type", "Soil, Waste &amp; Rain Pipe"], ["Application", "Drainage Systems"]] },
      { name: "HDPE Pipe 1&Prime; (PN10)", specs: [["Size", "1&Prime;"], ["Material", "HDPE"], ["Pressure Rating", "PN10"], ["Application", "Underground Water Supply"]] },
      { name: "Pipe Clamp (U-Bolt Type)", specs: [["Size", "1/2&Prime; &ndash; 4&Prime;"], ["Material", "Galvanised Steel"], ["Type", "U-Bolt Pipe Clamp"], ["Application", "Pipe Support &amp; Mounting"]] },
    ],
  },

  "safety-products": {
    label: "Safety Products",
    heading: "Popular Safety Products",
    description: "Personal protective equipment and site safety gear for compliant, secure work environments.",
    products: [
      { name: "Safety Helmet (ABS Shell)", specs: [["Material", "ABS Shell"], ["Standard", "IS 2925 Compliant"], ["Adjustment", "Ratchet Type"], ["Application", "Head Protection"]] },
      { name: "Safety Goggles (Anti-Fog)", specs: [["Lens", "Polycarbonate, Anti-Fog"], ["Standard", "IS 5983 Compliant"], ["Frame", "Adjustable Strap"], ["Application", "Eye Protection"]] },
      { name: "Safety Shoes (Steel Toe)", specs: [["Toe Cap", "Steel Toe"], ["Sole", "PU Double Density"], ["Standard", "IS 15298 Compliant"], ["Application", "Foot Protection"]] },
      { name: "Reflective Safety Vest", specs: [["Material", "Polyester Mesh"], ["Reflective Tape", "2-Inch Width"], ["Colour", "High-Visibility Orange"], ["Application", "Site Visibility"]] },
      { name: "Safety Harness (Full Body)", specs: [["Type", "Full Body Harness"], ["Standard", "IS 3521 Compliant"], ["Attachment", "Dorsal D-Ring"], ["Application", "Fall Protection"]] },
      { name: "Ear Muff (Noise Cancelling)", specs: [["Noise Reduction", "Up to 27dB (SNR)"], ["Type", "Over-the-Head Ear Muff"], ["Cushion", "Foam-Filled"], ["Application", "Hearing Protection"]] },
      { name: "Safety Gloves (Cut-Resistant)", specs: [["Material", "HPPE Knit"], ["Cut Level", "Level 5"], ["Coating", "Nitrile Palm"], ["Application", "Hand Protection"]] },
    ],
  },

  "hardware-accessories": {
    label: "Hardware Accessories",
    heading: "Popular Hardware Accessories",
    description: "General-purpose hardware accessories to complete any installation or repair job.",
    products: [
      { name: "Cable Tie Set (Nylon)", specs: [["Length", "100mm &ndash; 300mm"], ["Material", "UV-Resistant Nylon"], ["Pack Size", "100 pcs"], ["Application", "Cable &amp; Wire Bundling"]] },
      { name: "Storage Hooks (Wall Mount)", specs: [["Material", "Zinc-Plated Steel"], ["Load Rating", "Up to 10kg"], ["Mounting", "Screw-In"], ["Application", "Tool &amp; Equipment Storage"]] },
      { name: "Furniture Leg Levelers", specs: [["Material", "Nylon / Steel"], ["Thread Size", "M8 &ndash; M10"], ["Adjustment Range", "20mm"], ["Application", "Furniture Levelling"]] },
      { name: "Corner Bracket (L-Shape)", specs: [["Material", "Galvanised Steel"], ["Size", "50mm x 50mm"], ["Thickness", "2mm"], ["Application", "Shelf &amp; Frame Reinforcement"]] },
      { name: "Drawer Slide Rail (Ball Bearing)", specs: [["Length", "300mm &ndash; 600mm"], ["Load Rating", "Up to 35kg"], ["Type", "Full Extension"], ["Application", "Drawer &amp; Cabinet Runners"]] },
      { name: "Magnetic Door Catch", specs: [["Material", "Nylon / Metal"], ["Pull Strength", "&asymp; 4kg"], ["Mounting", "Screw-In"], ["Application", "Cabinet Door Retention"]] },
      { name: "Toolbox (Multi-Compartment)", specs: [["Material", "High-Impact Plastic"], ["Compartments", "Multi-Tray"], ["Size", "16&Prime;"], ["Application", "Tool Storage &amp; Transport"]] },
    ],
  },
};

const CATALOGUE_PDF_HREF = "../assets/catalogue/hardwares-catalogue.pdf";

function catalogueHrefFor(categoryKey) {
  return `${CATALOGUE_PDF_HREF}#${categoryKey}`;
}

function renderSpecs(specs) {
  return specs
    .map(
      ([label, value]) =>
        `<li><i class="fa-solid fa-check" aria-hidden="true"></i><span><strong>${label}:</strong> ${value}</span></li>`
    )
    .join("\n");
}

function renderProductCard(product, categoryKey) {
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

/* ---------------------------------------------------------------------
   Nine cards per sub-category (fixed layout: 3 x 3 on desktop).
   Existing sample records come first; every remaining position is a
   clearly labelled placeholder with a stable, position-based internal id
   (data-slot-id, never shown to visitors). Placeholders carry no product
   name, spec, brand, rating, certification, stock claim or document link;
   their Request Quote button deliberately has no data-product-name, so the
   quote form is pre-filled with only the main category and the sub-category
   (see initQuotePrefill) and never submits a placeholder title as a product.
   --------------------------------------------------------------------- */
const CARDS_PER_GROUP = 9;
const SLOT_PAGE = "hardwares";

function slotId(categoryKey, index) {
  return `${SLOT_PAGE}-${categoryKey}-${String(index + 1).padStart(2, "0")}`;
}

function renderPendingCard(categoryKey, category, index) {
  const plainLabel = category.label.replace(/&amp;/g, "&");
  return `<article class="card card--hover product-card product-card--pending" data-slot-id="${slotId(categoryKey, index)}">
            <div class="product-card__media">
              <div class="aspect-box aspect-box--square" role="img" aria-label="${plainLabel} product image &mdash; placeholder, pending approved photography">
                <div class="img-placeholder"><i class="fa-regular fa-image" aria-hidden="true"></i></div>
              </div>
            </div>
            <h3 class="product-card__title">Product details pending</h3>
            <p class="product-card__desc">Contact us for product details.</p>
            <div class="card__actions">
              <a class="btn btn--outline btn--sm" href="contact.html" aria-label="Contact us for ${plainLabel} product details">Contact Us</a>
              <button type="button" class="btn btn--primary btn--sm" data-modal-open="quote" data-catalog-quote-trigger aria-label="Request a quote for ${plainLabel}">Request Quote</button>
            </div>
          </article>`;
}

function renderCardSlot(categoryKey, category, index) {
  const product = category.products[index];
  if (!product) return renderPendingCard(categoryKey, category, index);
  return renderProductCard(product, categoryKey).replace(
    '<article class="card card--hover product-card"',
    `<article class="card card--hover product-card" data-slot-id="${slotId(categoryKey, index)}"`
  );
}

function renderCardGrid(categoryKey, category) {
  const cards = [];
  for (let i = 0; i < CARDS_PER_GROUP; i += 1) cards.push(renderCardSlot(categoryKey, category, i));
  return cards.join("\n");
}


function renderCategory(categoryKey, els) {
  const category = CATALOG[categoryKey];
  if (!category) return;

  els.heading.innerHTML = category.heading;
  els.description.innerHTML = category.description;
  els.grid.innerHTML = renderCardGrid(categoryKey, category);

  if (els.inlineTitle) {
    els.inlineTitle.innerHTML = `Looking for more ${category.label} products?`;
  }
  if (els.catalogueHeading) {
    els.catalogueHeading.innerHTML = `Download Complete<br />${category.label} Catalogue`;
  }
  if (els.cataloguePdf) {
    els.cataloguePdf.setAttribute("href", catalogueHrefFor(categoryKey));
  }
}

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

function initQuotePrefill(getActiveCategoryLabel) {
  const categoryField = document.getElementById("quote-category");
  const productField = document.getElementById("quote-product");
  if (!categoryField || !productField) return;

  document.addEventListener("click", (event) => {
    const trigger = event.target.closest("[data-catalog-quote-trigger]");
    if (!trigger) return;

    categoryField.value = "hardwares";

    const productName = trigger.dataset.productName;
    productField.value = productName || getActiveCategoryLabel();
  });
}

function initHardwaresCatalog() {
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

    activeCategory = categoryKey;
    transitionToCategory(categoryKey, els);

    try {
      button.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    } catch (err) {
      /* no-op — scrolling is cosmetic only, never block on it */
    }
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initHardwaresCatalog);
} else {
  initHardwaresCatalog();
}
})();
