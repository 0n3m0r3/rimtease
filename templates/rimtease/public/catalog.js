export function matchesMod(mod, query, category, dependency) {
  const terms = query.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  return terms.every(term => mod.search.toLocaleLowerCase().includes(term))
    && (!category || mod.category === category)
    && (!dependency || (mod.requiresBody === "true") === (dependency === "body"));
}

export function initCatalog() {
  const catalog = document.querySelector(".rt-catalog");
  const redirect = document.querySelector("[data-catalog-redirect]");
  if (redirect) {
    location.replace(redirect.href);
    return;
  }
  if (!catalog) return;
  const cards = [...catalog.querySelectorAll("[data-mod-card]")];
  const query = catalog.querySelector("#mod-search");
  const category = catalog.querySelector("#mod-category");
  const dependency = catalog.querySelector("#mod-dependency");
  const count = catalog.querySelector("#mod-count");
  const empty = catalog.querySelector(".rt-catalog-empty");
  const dialog = catalog.querySelector("#mod-dialog");
  const content = dialog.querySelector(".rt-dialog-content");
  let opener;

  const filter = () => {
    let visible = 0;
    for (const card of cards) {
      card.hidden = !matchesMod(card.dataset, query.value, category.value, dependency.value);
      if (!card.hidden) visible++;
    }
    count.textContent = visible + (visible === 1 ? " mod" : " mods");
    empty.hidden = visible !== 0;
  };
  catalog.querySelector("form").addEventListener("submit", event => event.preventDefault());
  query.addEventListener("input", filter);
  category.addEventListener("change", filter);
  dependency.addEventListener("change", filter);

  const open = id => {
    const template = catalog.querySelector("#mod-" + id);
    if (!(template instanceof HTMLTemplateElement)) return;
    content.replaceChildren(template.content.cloneNode(true));
    if (!dialog.open) dialog.showModal();
    dialog.scrollTop = 0;
    dialog.querySelector("[data-close-mod]").focus({ preventScroll: true });
  };
  const route = () => {
    const match = location.hash.match(/^#mod-(core|body|themes)$/);
    if (match) open(match[1]);
    else if (dialog.open) dialog.close();
  };
  catalog.addEventListener("click", event => {
    const target = event.target.closest("button");
    if (!target) return;
    if (target.hasAttribute("data-open-mod")) {
      if (!dialog.open) opener = target;
      const id = target.dataset.openMod;
      if (location.hash === "#mod-" + id) open(id);
      else location.hash = "mod-" + id;
    }
    if (target.hasAttribute("data-close-mod")) dialog.close();
    if (target.hasAttribute("data-reset-filters")) {
      query.value = category.value = dependency.value = "";
      filter();
      query.focus();
    }
    if (target.hasAttribute("data-feature")) {
      const selected = target.dataset.feature;
      dialog.querySelectorAll("[data-feature]").forEach(button =>
        button.setAttribute("aria-pressed", String(button.dataset.feature === selected)));
      dialog.querySelectorAll("[data-feature-copy]").forEach(copy =>
        copy.hidden = copy.dataset.featureCopy !== selected);
    }
    if (target.hasAttribute("data-install-mod")) {
      const panel = dialog.querySelector(".rt-install-panel");
      panel.hidden = false;
      panel.scrollIntoView({ behavior: "instant", block: "nearest" });
    }
  });
  dialog.addEventListener("click", event => {
    if (event.target === dialog) {
      const bounds = dialog.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right ||
          event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
    }
  });
  dialog.addEventListener("close", () => {
    if (location.hash.startsWith("#mod-")) history.replaceState(null, "", location.pathname + location.search);
    if (opener?.isConnected) opener.focus({ preventScroll: true });
  });
  window.addEventListener("hashchange", route);
  route();
}
