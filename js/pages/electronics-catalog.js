/**
 * electronics-catalog.js
 * Page-specific script for the Electronics Components product page.
 * Same reusable architecture as electricals-catalog.js (see that file
 * for the full explanation of the pattern) — a data object, one
 * render function, one transition function, one click-delegation
 * listener, one quote-modal pre-fill listener.
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
  "passive-components": {
    label: "Passive Components",
    heading: "Popular Passive Components",
    description: "Resistors, capacitors and inductors for reliable circuit design and prototyping.",
    products: [
      { name: "Metal Film Resistor 1/4W", specs: [["Power Rating", "1/4W"], ["Tolerance", "&plusmn;1%"], ["Resistance Range", "1&Omega; &ndash; 10M&Omega;"], ["Application", "General Purpose Circuits"]] },
      { name: "Aluminium Electrolytic Capacitor 470&mu;F", specs: [["Capacitance", "470&mu;F"], ["Voltage Rating", "25V &ndash; 450V"], ["Type", "Radial Leaded"], ["Application", "Power Supply Filtering"]] },
      { name: "Ceramic Disc Capacitor 100nF", specs: [["Capacitance", "100nF"], ["Voltage Rating", "50V"], ["Dielectric", "X7R"], ["Application", "Decoupling &amp; Bypass"]] },
      { name: "Wirewound Power Resistor 10W", specs: [["Power Rating", "10W"], ["Tolerance", "&plusmn;5%"], ["Resistance Range", "0.1&Omega; &ndash; 10k&Omega;"], ["Application", "High-Power Circuits"]] },
      { name: "Ferrite Bead Inductor", specs: [["Impedance", "600&Omega; @ 100MHz"], ["Current Rating", "Up to 3A"], ["Mounting", "SMD / Through-Hole"], ["Application", "EMI Noise Suppression"]] },
      { name: "Trimmer Potentiometer 10k&Omega;", specs: [["Resistance", "10k&Omega;"], ["Type", "Single-Turn Cermet"], ["Mounting", "PCB Through-Hole"], ["Application", "Circuit Calibration"]] },
      { name: "Tantalum Capacitor 10&mu;F", specs: [["Capacitance", "10&mu;F"], ["Voltage Rating", "16V &ndash; 35V"], ["Type", "SMD Chip"], ["Application", "Compact Power Filtering"]] },
    ],
  },

  "active-components": {
    label: "Active Components",
    heading: "Popular Active Components",
    description: "Transistors, diodes and amplifiers for switching, amplification and signal control.",
    products: [
      { name: "NPN Transistor BC547", specs: [["Type", "NPN"], ["Voltage", "Up to 45V"], ["Current", "Up to 100mA"], ["Application", "General Switching &amp; Amplification"]] },
      { name: "Power MOSFET IRF540", specs: [["Type", "N-Channel MOSFET"], ["Voltage", "100V"], ["Current", "Up to 33A"], ["Application", "High-Current Switching"]] },
      { name: "Operational Amplifier LM358", specs: [["Type", "Dual Op-Amp"], ["Supply Voltage", "3V &ndash; 32V"], ["Package", "DIP-8 / SOIC-8"], ["Application", "Signal Amplification"]] },
      { name: "Schottky Diode 1N5819", specs: [["Type", "Schottky Barrier"], ["Voltage", "40V"], ["Current", "1A"], ["Application", "Fast Switching &amp; Rectification"]] },
      { name: "Zener Diode 5.1V", specs: [["Type", "Zener"], ["Voltage", "5.1V"], ["Power Rating", "0.5W"], ["Application", "Voltage Regulation"]] },
      { name: "PNP Transistor BC557", specs: [["Type", "PNP"], ["Voltage", "Up to 45V"], ["Current", "Up to 100mA"], ["Application", "General Switching &amp; Amplification"]] },
      { name: "Voltage Comparator LM393", specs: [["Type", "Dual Comparator"], ["Supply Voltage", "2V &ndash; 36V"], ["Package", "DIP-8 / SOIC-8"], ["Application", "Signal Comparison &amp; Threshold Detection"]] },
    ],
  },

  "semiconductors": {
    label: "Semiconductors",
    heading: "Popular Semiconductors",
    description: "Integrated circuits, microcontrollers and regulators for embedded and analog designs.",
    products: [
      { name: "Voltage Regulator IC 7805", specs: [["Type", "Linear Regulator"], ["Output Voltage", "5V"], ["Current", "Up to 1.5A"], ["Application", "Fixed-Voltage Power Supply"]] },
      { name: "8-Bit Microcontroller ATmega328", specs: [["Type", "AVR Microcontroller"], ["Flash Memory", "32KB"], ["I/O Pins", "23"], ["Application", "Embedded Control Systems"]] },
      { name: "Timer IC NE555", specs: [["Type", "Precision Timer"], ["Supply Voltage", "4.5V &ndash; 16V"], ["Package", "DIP-8 / SOIC-8"], ["Application", "Pulse &amp; Oscillator Circuits"]] },
      { name: "Logic Gate IC 74HC08", specs: [["Type", "Quad 2-Input AND Gate"], ["Supply Voltage", "2V &ndash; 6V"], ["Package", "DIP-14 / SOIC-14"], ["Application", "Digital Logic Circuits"]] },
      { name: "EEPROM Memory IC 24LC256", specs: [["Type", "Serial EEPROM"], ["Capacity", "256Kbit"], ["Interface", "I2C"], ["Application", "Non-Volatile Data Storage"]] },
      { name: "Optocoupler PC817", specs: [["Type", "Phototransistor Optocoupler"], ["Isolation Voltage", "5000V"], ["Package", "DIP-4"], ["Application", "Signal Isolation"]] },
      { name: "Motor Driver IC L293D", specs: [["Type", "Dual H-Bridge Driver"], ["Output Current", "Up to 600mA per channel"], ["Package", "DIP-16"], ["Application", "DC Motor Control"]] },
    ],
  },

  "connectors": {
    label: "Connectors",
    heading: "Popular Connectors",
    description: "Board-to-board, wire-to-board and I/O connectors for reliable circuit interconnection.",
    products: [
      { name: "Pin Header 2.54mm (40-Way)", specs: [["Pitch", "2.54mm"], ["Ways", "40"], ["Type", "Straight Male Header"], ["Application", "PCB Board Interconnection"]] },
      { name: "JST-XH Connector 2-Pin", specs: [["Pitch", "2.5mm"], ["Ways", "2"], ["Rating", "3A, 250V"], ["Application", "Battery &amp; Wire Connection"]] },
      { name: "USB Type-C Connector (SMD)", specs: [["Type", "USB-C Receptacle"], ["Mounting", "SMD"], ["Current Rating", "Up to 3A"], ["Application", "Power &amp; Data Connectivity"]] },
      { name: "DB9 D-Sub Connector", specs: [["Type", "9-Pin D-Sub"], ["Mounting", "Panel Mount"], ["Rating", "5A per contact"], ["Application", "Serial Communication"]] },
      { name: "Screw Terminal Block 5.08mm", specs: [["Pitch", "5.08mm"], ["Ways", "2 &ndash; 12"], ["Rating", "15A, 300V"], ["Application", "Wire Termination"]] },
      { name: "RJ45 Connector (Shielded)", specs: [["Type", "8P8C Shielded"], ["Mounting", "Through-Hole"], ["Category", "Cat6"], ["Application", "Ethernet Connectivity"]] },
      { name: "Micro USB Connector (SMD)", specs: [["Type", "Micro-USB B Receptacle"], ["Mounting", "SMD"], ["Current Rating", "Up to 1.8A"], ["Application", "Power &amp; Data Connectivity"]] },
    ],
  },

  "sensors": {
    label: "Sensors",
    heading: "Popular Sensors",
    description: "Temperature, proximity and environmental sensors for measurement and automation applications.",
    products: [
      { name: "Temperature Sensor DS18B20", specs: [["Type", "Digital Temperature Sensor"], ["Range", "-55&deg;C to +125&deg;C"], ["Interface", "1-Wire"], ["Application", "Temperature Monitoring"]] },
      { name: "PIR Motion Sensor", specs: [["Type", "Passive Infrared"], ["Detection Range", "Up to 7m"], ["Supply Voltage", "5V &ndash; 20V"], ["Application", "Motion Detection &amp; Security"]] },
      { name: "Ultrasonic Distance Sensor HC-SR04", specs: [["Type", "Ultrasonic Rangefinder"], ["Range", "2cm &ndash; 400cm"], ["Supply Voltage", "5V"], ["Application", "Distance Measurement"]] },
      { name: "Humidity &amp; Temperature Sensor DHT22", specs: [["Type", "Digital Combo Sensor"], ["Humidity Range", "0% &ndash; 100% RH"], ["Temperature Range", "-40&deg;C to +80&deg;C"], ["Application", "Environmental Monitoring"]] },
      { name: "Inductive Proximity Sensor", specs: [["Type", "Inductive"], ["Sensing Range", "0 &ndash; 8mm"], ["Supply Voltage", "10V &ndash; 30V DC"], ["Application", "Metal Object Detection"]] },
      { name: "Gas Sensor MQ-2", specs: [["Type", "Combustible Gas Sensor"], ["Detects", "LPG, Smoke, Methane"], ["Supply Voltage", "5V"], ["Application", "Gas Leak Detection"]] },
      { name: "Load Cell (Weight Sensor) 5kg", specs: [["Type", "Strain Gauge Load Cell"], ["Capacity", "5kg"], ["Output", "Analog mV/V"], ["Application", "Weight Measurement"]] },
    ],
  },

  "circuit-protection": {
    label: "Circuit Protection",
    heading: "Popular Circuit Protection",
    description: "Fuses, varistors and protection devices to safeguard sensitive electronic circuits.",
    products: [
      { name: "Glass Fuse 5x20mm (1A)", specs: [["Rating", "1A"], ["Type", "Fast-Blow Glass Fuse"], ["Size", "5mm x 20mm"], ["Application", "Overcurrent Protection"]] },
      { name: "Resettable Fuse (PTC) 500mA", specs: [["Rating", "500mA Hold Current"], ["Type", "Polyswitch / PTC"], ["Mounting", "PCB Through-Hole"], ["Application", "Resettable Overcurrent Protection"]] },
      { name: "Metal Oxide Varistor (MOV)", specs: [["Voltage Rating", "275V AC"], ["Type", "Radial Leaded MOV"], ["Energy Rating", "Up to 40 Joules"], ["Application", "Surge &amp; Transient Protection"]] },
      { name: "TVS Diode (Transient Suppressor)", specs: [["Voltage Rating", "5V &ndash; 36V"], ["Type", "Unidirectional TVS"], ["Package", "SMD / DO-214"], ["Application", "ESD &amp; Surge Protection"]] },
      { name: "Blade Fuse (Automotive) 15A", specs: [["Rating", "15A"], ["Type", "Standard Blade Fuse"], ["Colour Code", "Blue"], ["Application", "Automotive Circuit Protection"]] },
      { name: "Circuit Breaker (Miniature, PCB Mount)", specs: [["Rating", "2A &ndash; 10A"], ["Type", "Thermal, Resettable"], ["Mounting", "PCB / Panel"], ["Application", "Equipment Overcurrent Protection"]] },
      { name: "Gas Discharge Tube (GDT)", specs: [["Voltage Rating", "90V &ndash; 600V"], ["Type", "2-Electrode GDT"], ["Package", "Radial Leaded"], ["Application", "Lightning &amp; Surge Protection"]] },
    ],
  },

  "development-boards": {
    label: "Development Boards",
    heading: "Popular Development Boards",
    description: "Microcontroller and prototyping boards for rapid embedded development and testing.",
    products: [
      { name: "Arduino Uno Compatible Board", specs: [["Microcontroller", "ATmega328P"], ["I/O Pins", "14 Digital, 6 Analog"], ["Interface", "USB"], ["Application", "General Prototyping"]] },
      { name: "ESP32 Development Board", specs: [["Microcontroller", "Dual-Core ESP32"], ["Connectivity", "Wi-Fi + Bluetooth"], ["I/O Pins", "30+"], ["Application", "IoT &amp; Wireless Projects"]] },
      { name: "Raspberry Pi Pico Board", specs: [["Microcontroller", "RP2040 Dual-Core"], ["I/O Pins", "26 GPIO"], ["Interface", "USB, SPI, I2C"], ["Application", "Embedded Computing"]] },
      { name: "Breadboard (Full Size)", specs: [["Tie Points", "830"], ["Type", "Solderless Prototyping"], ["Size", "Full Size"], ["Application", "Circuit Prototyping"]] },
      { name: "STM32 Nucleo Board", specs: [["Microcontroller", "STM32 ARM Cortex-M"], ["I/O Pins", "Up to 114"], ["Interface", "USB, ST-Link"], ["Application", "Advanced Embedded Development"]] },
      { name: "Jumper Wire Set (M-M, M-F, F-F)", specs: [["Length", "20cm"], ["Type", "Dupont Jumper Wires"], ["Pack Size", "120 pcs (assorted)"], ["Application", "Breadboard Prototyping"]] },
      { name: "USB Logic Analyzer (8-Channel)", specs: [["Channels", "8"], ["Sample Rate", "Up to 24MHz"], ["Interface", "USB"], ["Application", "Digital Signal Debugging"]] },
    ],
  },
};

const CATALOGUE_PDF_HREF = "../assets/catalogue/electronics-catalogue.pdf";

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
    els.inlineTitle.textContent = `Looking for more ${category.label} products?`;
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

    categoryField.value = "electronics";

    const productName = trigger.dataset.productName;
    productField.value = productName || getActiveCategoryLabel();
  });
}

function initElectronicsCatalog() {
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
  initQuotePrefill(() => CATALOG[activeCategory].label);

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
  document.addEventListener("DOMContentLoaded", initElectronicsCatalog);
} else {
  initElectronicsCatalog();
}
})();
