/**
 * industrial-catalog.js
 * Page-specific script for the Industrial & Commercial Equipment
 * product page. Same reusable architecture as electricals-catalog.js
 * — a data object, one render function, one transition function, one
 * click-delegation listener, one quote-modal pre-fill listener.
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
  "material-handling-equipment": {
    label: "Material Handling Equipment",
    heading: "Popular Material Handling Equipment",
    description: "Pallet trucks, trolleys and lifting equipment for safe, efficient material movement.",
    products: [
      { name: "Hand Pallet Truck 2.5T", specs: [["Load Capacity", "2.5 Ton"], ["Fork Height", "85mm &ndash; 200mm"], ["Steering Type", "Manual"], ["Application", "Material Handling"]] },
      { name: "Platform Trolley (4-Wheel)", specs: [["Load Capacity", "300kg"], ["Platform Size", "900mm x 600mm"], ["Wheel Type", "PU Castors"], ["Application", "Warehouse Transport"]] },
      { name: "Drum Trolley (Hydraulic)", specs: [["Load Capacity", "350kg"], ["Drum Size", "200L Standard"], ["Lift Type", "Hydraulic Foot Pump"], ["Application", "Drum Handling &amp; Tilting"]] },
      { name: "Stacker (Manual) 1T", specs: [["Load Capacity", "1 Ton"], ["Lift Height", "Up to 1600mm"], ["Operation", "Manual Hydraulic"], ["Application", "Pallet Stacking"]] },
      { name: "Scissor Lift Table (Manual)", specs: [["Load Capacity", "500kg"], ["Lift Height", "Up to 850mm"], ["Operation", "Foot Pump Hydraulic"], ["Application", "Load Height Adjustment"]] },
      { name: "Roll Cage Trolley", specs: [["Load Capacity", "400kg"], ["Size", "800mm x 600mm"], ["Sides", "Folding Mesh"], ["Application", "Bulk Goods Transport"]] },
      { name: "Conveyor Roller (Gravity)", specs: [["Roller Diameter", "50mm"], ["Length", "3m Section"], ["Frame", "Galvanised Steel"], ["Application", "Manual Material Flow"]] },
    ],
  },

  "pumps-motors": {
    label: "Pumps &amp; Motors",
    heading: "Popular Pumps &amp; Motors",
    description: "Centrifugal pumps and industrial motors engineered for reliable fluid transfer and drive applications.",
    products: [
      { name: "Centrifugal Water Pump 1HP", specs: [["Power", "1 HP"], ["Flow Rate", "Up to 150 LPM"], ["Head Range", "Up to 20m"], ["Application", "Water Transfer"]] },
      { name: "Submersible Pump 1.5HP", specs: [["Power", "1.5 HP"], ["Flow Rate", "Up to 200 LPM"], ["Head Range", "Up to 30m"], ["Application", "Borewell &amp; Sump Pumping"]] },
      { name: "Industrial Motor 5HP (3-Phase)", specs: [["Power", "5 HP"], ["Phase", "3-Phase"], ["Speed", "1440 RPM"], ["Application", "Machine Drive"]] },
      { name: "Self-Priming Pump 2HP", specs: [["Power", "2 HP"], ["Flow Rate", "Up to 250 LPM"], ["Head Range", "Up to 25m"], ["Application", "General Purpose Pumping"]] },
      { name: "Gear Motor (Reduction) 1HP", specs: [["Power", "1 HP"], ["Reduction Ratio", "10:1 &ndash; 60:1"], ["Mounting", "Foot / Flange"], ["Application", "Low-Speed High-Torque Drive"]] },
      { name: "Booster Pump 0.5HP", specs: [["Power", "0.5 HP"], ["Flow Rate", "Up to 60 LPM"], ["Head Range", "Up to 15m"], ["Application", "Water Pressure Boosting"]] },
      { name: "Vacuum Pump (Rotary Vane)", specs: [["Power", "0.5 HP"], ["Vacuum Level", "Up to 29.5 inHg"], ["Type", "Oil-Sealed Rotary Vane"], ["Application", "Industrial Vacuum Applications"]] },
    ],
  },

  "electrical-enclosures": {
    label: "Electrical Enclosures",
    heading: "Popular Electrical Enclosures",
    description: "Weatherproof and industrial enclosures for safely housing electrical and control equipment.",
    products: [
      { name: "Metal Enclosure Box (IP65)", specs: [["Size", "300mm x 200mm x 150mm"], ["Material", "CRCA Sheet Steel"], ["Protection", "IP65"], ["Application", "Outdoor Electrical Housing"]] },
      { name: "Polycarbonate Enclosure (IP66)", specs: [["Size", "250mm x 150mm x 100mm"], ["Material", "Polycarbonate"], ["Protection", "IP66"], ["Application", "Corrosive Environment Housing"]] },
      { name: "Junction Box (GI, Weatherproof)", specs: [["Size", "200mm x 200mm x 100mm"], ["Material", "Galvanised Iron"], ["Protection", "IP55"], ["Application", "Cable Junction Housing"]] },
      { name: "Floor Standing Panel Enclosure", specs: [["Size", "800mm x 600mm x 2000mm"], ["Material", "CRCA Sheet Steel"], ["Protection", "IP42"], ["Application", "Control Panel Housing"]] },
      { name: "Wall Mount Cabinet (19&Prime; Rack)", specs: [["Rack Units", "12U"], ["Material", "CRCA Sheet Steel"], ["Protection", "IP54"], ["Application", "Network &amp; Server Equipment"]] },
      { name: "Cable Gland Plate (Enclosure Accessory)", specs: [["Material", "Galvanised Steel"], ["Compatibility", "Standard Enclosures"], ["Entries", "Multiple Knockouts"], ["Application", "Cable Entry Management"]] },
      { name: "Enclosure Cooling Fan Unit", specs: [["Air Flow", "Up to 150 CFM"], ["Voltage", "230V AC"], ["Mounting", "Panel Cut-Out"], ["Application", "Enclosure Thermal Management"]] },
    ],
  },

  "safety-security-equipment": {
    label: "Safety &amp; Security Equipment",
    heading: "Popular Safety &amp; Security Equipment",
    description: "Fire safety, alarm and access equipment for secure, compliant industrial and commercial facilities.",
    products: [
      { name: "Fire Extinguisher (ABC, 4kg)", specs: [["Type", "ABC Dry Powder"], ["Capacity", "4kg"], ["Standard", "IS 15683 Compliant"], ["Application", "Fire Emergency Response"]] },
      { name: "Smoke Detector (Photoelectric)", specs: [["Type", "Photoelectric"], ["Power", "9V Battery / Wired"], ["Coverage", "Up to 40m&sup2;"], ["Application", "Fire Detection"]] },
      { name: "Access Control Reader (RFID)", specs: [["Type", "RFID Card Reader"], ["Read Range", "Up to 5cm"], ["Output", "Wiegand 26/34"], ["Application", "Door Access Control"]] },
      { name: "Emergency Alarm Siren", specs: [["Sound Output", "Up to 120dB"], ["Power", "12V / 230V AC"], ["Type", "Electronic Siren"], ["Application", "Emergency Notification"]] },
      { name: "Fire Hose Reel (Industrial)", specs: [["Hose Length", "30m"], ["Diameter", "25mm"], ["Material", "Rubber-Lined Fabric"], ["Application", "Fire Fighting"]] },
      { name: "Boom Barrier (Automatic)", specs: [["Boom Length", "Up to 4m"], ["Operation", "Motorised Automatic"], ["Cycle Time", "&asymp; 3 &ndash; 6 Seconds"], ["Application", "Vehicle Access Control"]] },
    ],
  },

  "lighting-solutions": {
    label: "Lighting Solutions",
    heading: "Popular Lighting Solutions",
    description: "Industrial and facility lighting engineered for demanding commercial and industrial environments.",
    products: [
      { name: "LED High Bay Light 100W", specs: [["Power", "100W"], ["Lumen Output", "13,000 lm"], ["IP Rating", "IP65"], ["Application", "Warehouse &amp; Factory Lighting"]] },
      { name: "LED Flood Light 150W", specs: [["Power", "150W"], ["Lumen Output", "18,000 lm"], ["IP Rating", "IP66"], ["Application", "Outdoor Facility Lighting"]] },
      { name: "Explosion-Proof LED Light", specs: [["Power", "40W"], ["Certification", "ATEX / IECEx"], ["IP Rating", "IP66"], ["Application", "Hazardous Area Lighting"]] },
      { name: "LED Tube Light (Industrial) 20W", specs: [["Power", "20W"], ["Length", "4 ft"], ["Lumen Output", "2,400 lm"], ["Application", "General Facility Lighting"]] },
      { name: "Solar Street Light (Integrated)", specs: [["Power", "60W LED"], ["Battery", "Integrated Lithium"], ["Sensor", "Dusk-to-Dawn + Motion"], ["Application", "Outdoor Area Lighting"]] },
      { name: "Emergency Bulkhead Light", specs: [["Power", "8W LED"], ["Backup", "90 Minutes"], ["IP Rating", "IP65"], ["Application", "Emergency Exit Lighting"]] },
      { name: "LED Tower Light (Portable)", specs: [["Power", "4 x 300W"], ["Mast Height", "Up to 9m"], ["Power Source", "Diesel Genset / Mains"], ["Application", "Site &amp; Event Lighting"]] },
    ],
  },

  "power-backup-stabilizers": {
    label: "Power Backup &amp; Stabilizers",
    heading: "Popular Power Backup &amp; Stabilizers",
    description: "UPS systems, generators and voltage stabilizers for uninterrupted, protected power supply.",
    products: [
      { name: "Online UPS 3kVA", specs: [["Capacity", "3kVA"], ["Type", "Online Double-Conversion"], ["Backup Time", "Load Dependent"], ["Application", "Critical Equipment Backup"]] },
      { name: "Servo Voltage Stabilizer 5kVA", specs: [["Capacity", "5kVA"], ["Input Voltage", "140V &ndash; 270V"], ["Output Voltage", "230V &plusmn;1%"], ["Application", "Voltage Regulation"]] },
      { name: "Diesel Generator Set 15kVA", specs: [["Capacity", "15kVA"], ["Phase", "3-Phase"], ["Fuel Type", "Diesel"], ["Application", "Standby Power Generation"]] },
      { name: "Battery Bank (Tubular, 150Ah)", specs: [["Capacity", "150Ah"], ["Type", "Tubular Lead-Acid"], ["Voltage", "12V"], ["Application", "UPS &amp; Inverter Backup"]] },
      { name: "Line Interactive UPS 1kVA", specs: [["Capacity", "1kVA"], ["Type", "Line Interactive"], ["Backup Time", "&asymp; 10 &ndash; 15 Minutes"], ["Application", "Office Equipment Backup"]] },
      { name: "Automatic Voltage Regulator (AVR) 10kVA", specs: [["Capacity", "10kVA"], ["Regulation Type", "Servo-Controlled"], ["Output Accuracy", "&plusmn;1%"], ["Application", "Industrial Voltage Stabilization"]] },
      { name: "Isolation Transformer 5kVA", specs: [["Capacity", "5kVA"], ["Type", "Double-Wound Isolation"], ["Ratio", "1:1"], ["Application", "Sensitive Equipment Protection"]] },
    ],
  },

  "cleaning-equipment": {
    label: "Cleaning Equipment",
    heading: "Popular Cleaning Equipment",
    description: "Industrial cleaning machines and equipment for facility maintenance and housekeeping.",
    products: [
      { name: "Industrial Vacuum Cleaner (Wet &amp; Dry)", specs: [["Capacity", "30L"], ["Power", "1400W"], ["Type", "Wet &amp; Dry"], ["Application", "Industrial Floor Cleaning"]] },
      { name: "Floor Scrubber Machine (Walk-Behind)", specs: [["Tank Capacity", "50L"], ["Cleaning Width", "430mm"], ["Power", "Battery Operated"], ["Application", "Large Floor Area Cleaning"]] },
      { name: "High Pressure Washer 150 Bar", specs: [["Pressure", "150 Bar"], ["Flow Rate", "Up to 500 LPH"], ["Power", "2200W"], ["Application", "Heavy-Duty Surface Cleaning"]] },
      { name: "Floor Polisher Machine", specs: [["Pad Size", "400mm"], ["Power", "1500W"], ["Speed", "154 RPM"], ["Application", "Floor Polishing &amp; Buffing"]] },
      { name: "Dust Collector (Industrial)", specs: [["Air Flow", "Up to 1200 CFM"], ["Filter Type", "Cartridge Filter"], ["Bin Capacity", "50L"], ["Application", "Workshop Dust Extraction"]] },
      { name: "Steam Cleaning Machine (Industrial)", specs: [["Boiler Capacity", "5L"], ["Pressure", "Up to 8 Bar"], ["Power", "3000W"], ["Application", "Deep Sanitisation Cleaning"]] },
      { name: "Window Cleaning Kit (Extension Pole)", specs: [["Pole Length", "Up to 6m Extendable"], ["Head Type", "Squeegee + Applicator"], ["Material", "Aluminium Pole"], ["Application", "High-Level Window Cleaning"]] },
    ],
  },
};

const CATALOGUE_PDF_HREF = "../assets/catalogue/industrial-catalogue.pdf";

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

function renderCategory(categoryKey, els) {
  const category = CATALOG[categoryKey];
  if (!category) return;

  els.heading.innerHTML = category.heading;
  els.description.innerHTML = category.description;
  els.grid.innerHTML = category.products.map((p) => renderProductCard(p, categoryKey)).join("\n");

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

    categoryField.value = "industrial";

    const productName = trigger.dataset.productName;
    productField.value = productName || getActiveCategoryLabel();
  });
}

function initIndustrialCatalog() {
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
  document.addEventListener("DOMContentLoaded", initIndustrialCatalog);
} else {
  initIndustrialCatalog();
}
})();
