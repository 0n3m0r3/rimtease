import { initCatalog } from "./catalog.js";

export default {
  defaultTheme: "dark",
  showLightbox(image) {
    return !image.closest(".rt-catalog, a") && image.naturalWidth > 200 && image.naturalHeight > 200;
  },
  start() {
    initCatalog();
    document.querySelector(".navbar-brand")?.insertAdjacentHTML(
      "beforeend", '<span class="rt-nav-status">In development</span>');
    document.querySelector("#logo")?.setAttribute("alt", "");

    // DocFX renders and refreshes these controls after the start hook.
    const navbar = document.querySelector("#navbar");
    const labelControls = () => {
      navbar.querySelectorAll(".icons a[title]").forEach(control => {
        control.setAttribute("aria-label", control.title);
      });
      navbar.querySelectorAll(".icons i").forEach(icon => icon.setAttribute("aria-hidden", "true"));
      const theme = navbar.querySelector(".icons [data-bs-toggle='dropdown']");
      if (theme && !theme.hasAttribute("role")) {
        theme.setAttribute("role", "button");
        theme.setAttribute("tabindex", "0");
        theme.addEventListener("keydown", event => {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            theme.click();
          }
        });
      }
    };
    if (navbar) {
      new MutationObserver(labelControls).observe(navbar, { childList: true, subtree: true });
      labelControls();
    }
  }
};
