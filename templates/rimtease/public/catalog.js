export function matchesMod(mod, query, category, dependency) {
  const terms = query.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  return terms.every(term => mod.search.toLocaleLowerCase().includes(term))
    && (!category || mod.category === category)
    && (!dependency || mod.dependencies.split(" ").includes(dependency));
}

export function initCatalog() {
  const catalog = document.querySelector(".rt-catalog");
  if (catalog) {
    // Preserve previously shared dialogue links after moving to real pages.
    const legacy = location.hash.match(/^#mod-(core|body|themes)$/);
    if (legacy) {
      location.replace(new URL(`mods/${legacy[1]}.html`, location.href));
      return;
    }
    const cards = [...catalog.querySelectorAll("[data-mod-card]")];
    const query = catalog.querySelector("#mod-search");
    const category = catalog.querySelector("#mod-category");
    const dependency = catalog.querySelector("#mod-dependency");
    const controls = { q: query, category, dependency };
    const filter = () => {
      let visible = 0;
      for (const card of cards) {
        card.hidden = !matchesMod(card.dataset, query.value, category.value, dependency.value);
        if (!card.hidden) visible++;
      }
      catalog.querySelector("#mod-count").textContent = visible + (visible === 1 ? " mod" : " mods");
      catalog.querySelector(".rt-catalog-empty").hidden = visible !== 0;
      catalog.querySelectorAll("[data-mod-group]").forEach(group => {
        group.hidden = !group.querySelector("[data-mod-card]:not([hidden])");
      });
      const url = new URL(location.href);
      for (const [key, control] of Object.entries(controls)) {
        if (control.value) url.searchParams.set(key, control.value);
        else url.searchParams.delete(key);
      }
      history.replaceState(null, "", url);
      // Carry catalogue filters through dependency pages without local storage.
      for (const link of catalog.querySelectorAll("[data-mod-link]")) {
        const target = new URL(link.href);
        target.search = url.search;
        link.href = target.href;
      }
    };
    const params = new URLSearchParams(location.search);
    for (const [key, control] of Object.entries(controls)) {
      control.value = params.get(key) || "";
      control.addEventListener(key === "q" ? "input" : "change", filter);
    }
    catalog.querySelector("form").addEventListener("submit", event => event.preventDefault());
    catalog.querySelector("[data-reset-filters]").addEventListener("click", () => {
      query.value = category.value = dependency.value = "";
      filter();
      query.focus();
    });
    window.addEventListener("pageshow", filter);
    filter();
  }

  const page = document.querySelector(".rt-mod-page");
  if (!page) return;
  const context = new URLSearchParams();
  const params = new URLSearchParams(location.search);
  for (const key of ["q", "category", "dependency"]) {
    if (params.get(key)) context.set(key, params.get(key));
  }
  for (const link of page.querySelectorAll("[data-catalog-back], [data-mod-link]")) {
    const url = new URL(link.href);
    url.search = context.toString();
    link.href = url.href;
  }
  page.addEventListener("click", event => {
    const button = event.target.closest("[data-feature]");
    if (!button) return;
    page.querySelectorAll("[data-feature]").forEach(item =>
      item.setAttribute("aria-pressed", String(item.dataset.feature === button.dataset.feature)));
    page.querySelectorAll("[data-feature-copy]").forEach(copy =>
      copy.hidden = copy.dataset.featureCopy !== button.dataset.feature);
  });
}
