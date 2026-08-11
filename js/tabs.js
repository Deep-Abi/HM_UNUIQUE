/**
 * tabs.js
 * Sub-category tab strip on category pages. Currently switches the
 * visual active state and scrolls the selected tab into view within
 * its own contained row (never the page). It does NOT yet filter the
 * product grid: only one sub-category's real product data (name,
 * description, specs) has been approved from the concept PDF per
 * category — the other sub-categories are shown as a preview of the
 * full taxonomy, not as clickable content switches with fabricated
 * products behind them. See documents/PHASE-4-CATEGORY-PAGES-REPORT.md
 * for the full explanation. Wiring real per-tab filtering here is a
 * one-function change (`selectTab`) once that data exists.
 */

function selectTab(tabsEl, selectedButton) {
  tabsEl.querySelectorAll(".category-tabs__item").forEach((btn) => {
    const isSelected = btn === selectedButton;
    btn.classList.toggle("is-active", isSelected);
    if (isSelected) {
      btn.setAttribute("aria-current", "true");
    } else {
      btn.removeAttribute("aria-current");
    }
  });

  selectedButton.scrollIntoView({
    behavior: "smooth",
    inline: "center",
    block: "nearest",
  });
}

export function initTabs() {
  document.querySelectorAll("[data-tabs]").forEach((tabsEl) => {
    tabsEl.addEventListener("click", (event) => {
      const button = event.target.closest(".category-tabs__item");
      if (!button || !tabsEl.contains(button)) return;
      selectTab(tabsEl, button);
    });
  });
}
