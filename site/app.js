(() => {
  "use strict";

  function initializeCatalogue() {
    const form = document.getElementById("filters");
    const list = document.getElementById("paper-list");
    const dataElement = document.getElementById("paper-data");
    if (!form || !list || !dataElement || form.dataset.enhanced) return;

    let records;
    try {
      records = JSON.parse(dataElement.textContent);
    } catch {
      return; // The complete, server-rendered catalogue remains available.
    }
    if (!Array.isArray(records)) return;

    const search = document.getElementById("search");
    const contextForm = document.getElementById("context-form");
    const contextRole = document.getElementById("context-role");
    const family = document.getElementById("family");
    const scope = document.getElementById("scope");
    const evidence = document.getElementById("evidence");
    const year = document.getElementById("year");
    const sort = document.getElementById("sort");
    const count = document.getElementById("result-count");
    const emptyState = document.getElementById("empty-state");
    const showMore = document.getElementById("show-more");
    if (![search, family, evidence, year, sort, count, emptyState].every(Boolean)) return;

    const normalize = (value) => String(value ?? "")
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/[^\p{L}\p{N}]+/gu, " ")
      .trim();
    const readableLabel = (value) => String(value).replace(/(^|[\s-])\p{L}/gu, (letter) => letter.toUpperCase());
    const cards = new Map(Array.from(list.querySelectorAll(".paper-card[data-id]"), (card) => [card.dataset.id, card]));
    const seen = new Set();
    const papers = records.filter((paper) => {
      if (!paper || typeof paper.id !== "string" || !cards.has(paper.id) || seen.has(paper.id)) return false;
      seen.add(paper.id);
      return true;
    });
    if (!papers.length) return;

    const byId = new Map(papers.map((paper) => [paper.id, paper]));
    const searchable = new Map(papers.map((paper) => {
      const text = normalize([
        paper.title, paper.authors, paper.acronym, paper.id, paper.number, paper.citation,
        paper.context_form_labels, paper.context_role_labels, paper.family, paper.context, paper.action_mechanism, paper.adaptation_target,
      ].flat().filter((value) => value !== undefined && value !== null).join(" "));
      return [paper.id, { text, compact: text.replace(/\s/g, "") }];
    }));

    function populateOptions(select, values, descending = false) {
      const options = [...new Set(values.filter((value) => value !== undefined && value !== null).map(String))];
      options.sort(descending ? (left, right) => Number(right) - Number(left) : (left, right) => left.localeCompare(right));
      // Keep the HTML's descriptive "all" option, and allow safe reinitialization.
      for (const option of Array.from(select.options)) {
        if (option.value) option.remove();
      }
      for (const value of options) {
        const option = document.createElement("option");
        option.value = value;
        option.textContent = readableLabel(value);
        select.append(option);
      }
    }

    const familyGroups = [
      ["Methods and comparisons", ["Context-conditioned policies", "Geometric demonstration transfer", "World-model-based control", "Skill- and agent-based execution"]],
      ["Supporting references", ["Data resources", "Evaluation", "Foundations and surveys", "Training and representations"]],
    ];
    for (const child of Array.from(family.children)) {
      if (child.tagName === "OPTGROUP" || child.value) child.remove();
    }
    const availableFamilies = new Set(papers.map((paper) => paper.family));
    for (const [label, values] of familyGroups) {
      const group = document.createElement("optgroup");
      group.label = label;
      for (const value of values) {
        if (!availableFamilies.has(value)) continue;
        const option = document.createElement("option");
        option.value = value;
        option.textContent = value;
        group.append(option);
      }
      if (group.children.length) family.append(group);
    }
    populateOptions(evidence, papers.filter((paper) => paper.annotated).map((paper) => paper.evidence_tier));
    populateOptions(year, papers.map((paper) => paper.year), true);
    form.dataset.enhanced = "true";
    form.hidden = false;
    document.body.classList.add("js");

    function validOption(select, value, fallback = "") {
      return Array.from(select.options).some((option) => option.value === value) ? value : fallback;
    }

    function restoreFilters() {
      const params = new URL(window.location.href).searchParams;
      search.value = params.get("q") || "";
      contextForm.value = validOption(contextForm, params.get("form") || "");
      contextRole.value = validOption(contextRole, params.get("role") || "");
      family.value = validOption(family, params.get("family") || "");
      if (scope) scope.value = validOption(scope, params.get("scope") || "");
      evidence.value = validOption(evidence, params.get("evidence") || "");
      year.value = validOption(year, params.get("year") || "");
      sort.value = validOption(sort, params.get("sort") || "newest", "newest");
    }

    function saveFilters() {
      const url = new URL(window.location.href);
      const values = {
        q: search.value.trim(),
        form: contextForm.value,
        role: contextRole.value,
        family: family.value,
        scope: scope?.value || "",
        evidence: evidence.value,
        year: year.value,
        sort: sort.value === "newest" ? "" : sort.value,
      };
      for (const [key, value] of Object.entries(values)) {
        if (value) url.searchParams.set(key, value);
        else url.searchParams.delete(key);
      }
      try {
        window.history.replaceState(window.history.state, "", url);
      } catch {
        // Filtering also works when a local preview disallows history changes.
      }
    }

    const pageSize = 24;
    let visibleLimit = pageSize;
    let orderedPapers = [];
    let previousSort = null;
    let matchingPapers = [];

    function renderFilters(persist = true, resetPage = true) {
      if (resetPage) visibleLimit = pageSize;
      const terms = normalize(search.value).split(/\s+/).filter(Boolean);
      const referenceQuery = search.value.trim().match(/^(?:#(\d+)|\[(\d+)\])$/);
      const activeElement = document.activeElement;
      if (previousSort !== sort.value) {
        orderedPapers = [...papers].sort((left, right) => {
          if (sort.value === "title") return left.title.localeCompare(right.title) || left.id.localeCompare(right.id);
          const difference = (Number(left.year) || 0) - (Number(right.year) || 0);
          return (sort.value === "oldest" ? difference : -difference) || Number(left.number) - Number(right.number) || left.id.localeCompare(right.id);
        });
        for (let index = 0; index < orderedPapers.length; index += 1) {
          const card = cards.get(orderedPapers[index].id);
          if (list.children[index] !== card) list.insertBefore(card, list.children[index] || null);
        }
        previousSort = sort.value;
      }
      matchingPapers = orderedPapers.filter((paper) => {
        const indexText = searchable.get(paper.id);
        const matchesScope = !scope?.value
          || (scope.value === "mapped" && paper.framework_mapped === true)
          || (scope.value === "unmapped" && paper.framework_mapped === false)
          || (scope.value === "methods" && paper.is_method === true)
          || (scope.value === "supporting" && paper.is_method === false)
          || (scope.value === "annotated" && paper.annotated === true);
        return matchesScope
          && (!contextForm.value || paper.context_forms.includes(contextForm.value))
          && (!contextRole.value || paper.context_roles.includes(contextRole.value))
          && (!family.value || paper.family === family.value)
          && (!evidence.value || paper.evidence_tier === evidence.value)
          && (!year.value || String(paper.year) === year.value)
          && (referenceQuery
            ? Number(paper.number) === Number(referenceQuery[1] || referenceQuery[2])
            : terms.every((term) => indexText.text.includes(term) || indexText.compact.includes(term)));
      });
      const visiblePapers = matchingPapers.slice(0, showMore ? visibleLimit : matchingPapers.length);
      const visibleIds = new Set(visiblePapers.map((paper) => paper.id));
      for (const [id, card] of cards) {
        const hidden = !visibleIds.has(id);
        if (card.hidden !== hidden) card.hidden = hidden;
      }
      if (activeElement && list.contains(activeElement)) {
        if (activeElement.closest(".paper-card")?.hidden) search.focus({ preventScroll: true });
        else if (document.activeElement !== activeElement) activeElement.focus({ preventScroll: true });
      }
      count.textContent = `Showing ${visiblePapers.length} of ${matchingPapers.length} matching references (${papers.length} total)`;
      emptyState.hidden = matchingPapers.length !== 0;
      if (showMore) {
        const remaining = matchingPapers.length - visiblePapers.length;
        showMore.hidden = remaining <= 0;
        showMore.textContent = `Show ${Math.min(pageSize, remaining)} more references`;
      }
      if (persist) saveFilters();
    }

    function resetFilters(focusSearch = false) {
      search.value = "";
      contextForm.value = "";
      contextRole.value = "";
      family.value = "";
      if (scope) scope.value = "";
      evidence.value = "";
      year.value = "";
      sort.value = "newest";
      renderFilters();
      if (focusSearch) search.focus({ preventScroll: true });
    }

    form.addEventListener("submit", (event) => event.preventDefault());
    search.addEventListener("input", () => renderFilters());
    for (const select of [contextForm, contextRole, family, scope, evidence, year, sort].filter(Boolean)) select.addEventListener("change", () => renderFilters());
    showMore?.addEventListener("click", () => {
      const firstNewPaper = matchingPapers[visibleLimit];
      visibleLimit += pageSize;
      renderFilters(false, false);
      if (firstNewPaper) {
        const card = cards.get(firstNewPaper.id);
        const target = card.querySelector("a[href], input, button");
        target?.focus({ preventScroll: true });
      }
    });
    document.getElementById("reset-filters")?.addEventListener("click", () => resetFilters());
    document.getElementById("clear-search")?.addEventListener("click", () => resetFilters(true));
    window.addEventListener("popstate", () => {
      restoreFilters();
      renderFilters(false);
    });

    document.addEventListener("click", (event) => {
      const link = event.target.closest("a[data-form], a[data-role], a[data-family], a[data-scope]");
      if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      const chosenForm = validOption(contextForm, link.dataset.form);
      const chosenRole = validOption(contextRole, link.dataset.role);
      const chosenFamily = validOption(family, link.dataset.family);
      const chosenScope = scope ? validOption(scope, link.dataset.scope) : "";
      if (!chosenForm && !chosenRole && !chosenFamily && !chosenScope) return;
      event.preventDefault();
      search.value = "";
      contextForm.value = chosenForm;
      contextRole.value = chosenRole;
      family.value = chosenFamily;
      if (scope) scope.value = chosenScope;
      evidence.value = "";
      year.value = "";
      renderFilters();
      // A copied or refreshed conceptual-path URL should reopen the collection.
      try {
        const destination = new URL(window.location.href);
        destination.hash = new URL(link.href).hash || "#catalogue";
        window.history.replaceState(window.history.state, "", destination);
      } catch { /* Filtering still works in restricted local previews. */ }
      form.scrollIntoView({ behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth", block: "start" });
      search.focus({ preventScroll: true });
    });

    restoreFilters();
    renderFilters(false);

    const bar = document.getElementById("compare-bar");
    const comparisonCount = document.getElementById("compare-count");
    const openButton = document.getElementById("open-comparison");
    const clearButton = document.getElementById("clear-comparison");
    const dialog = document.getElementById("comparison-dialog");
    const closeButton = document.getElementById("close-comparison");
    const content = document.getElementById("comparison-content");
    const status = document.getElementById("interaction-status");
    if (![bar, comparisonCount, openButton, clearButton, dialog, closeButton, content].every(Boolean)) return;

    const maximumSelection = 3;
    const selected = new Set();
    const controls = Array.from(list.querySelectorAll("input[data-compare]"));
    let previousFocus = null;
    const missingValue = "Not annotated in this collection";

    function sourceLink(value, label) {
      if (typeof value !== "string") return null;
      let url;
      try { url = new URL(value); } catch { return null; }
      if (!["https:", "http:"].includes(url.protocol)) return null;
      const link = document.createElement("a");
      link.href = url.href;
      link.textContent = label;
      return link;
    }

    function renderComparison() {
      const table = document.createElement("table");
      table.className = "comparison-table";
      const caption = document.createElement("caption");
      caption.textContent = `Comparing ${selected.size} ${selected.size === 1 ? "paper" : "papers"}`;
      table.append(caption);
      const head = document.createElement("thead");
      const headingRow = document.createElement("tr");
      const dimension = document.createElement("th");
      dimension.scope = "col";
      dimension.textContent = "Research dimension";
      headingRow.append(dimension);
      const comparedPapers = Array.from(selected, (id) => byId.get(id));
      for (const paper of comparedPapers) {
        const heading = document.createElement("th");
        heading.scope = "col";
        const title = document.createElement("p");
        title.textContent = `${paper.title} (${paper.year})`;
        const remove = document.createElement("button");
        remove.type = "button";
        remove.className = "comparison-remove";
        remove.dataset.removeComparison = paper.id;
        remove.textContent = "Remove";
        remove.setAttribute("aria-label", `Remove ${paper.title} from comparison`);
        heading.append(title, remove);
        headingRow.append(heading);
      }
      head.append(headingRow);
      table.append(head);
      const body = document.createElement("tbody");
      const dimensions = [
        ["Context form (our roadmap)", "context_form_labels"],
        ["Context role (our roadmap)", "context_role_labels"],
        ["Deployment updates (our roadmap)", "adaptation_regimes"],
        ["External reference number", "number"],
        ["External survey group", "family"],
        ["Year", "year"],
        ["Context", "context"],
        ["Action mechanism", "action_mechanism"],
        ["Adaptation target", "adaptation_target"],
        ["External survey evidence", "evidence_tier"],
        ["Evaluation setting", "setting"],
        ["Test-time weights", "test_time_weights"],
        ["Context budget", "context_budget"],
        ["Limitation", "limitation"],
      ];
      for (const [label, field] of dimensions) {
        const row = document.createElement("tr");
        const heading = document.createElement("th");
        heading.scope = "row";
        heading.textContent = label;
        row.append(heading);
        for (const paper of comparedPapers) {
          const cell = document.createElement("td");
          cell.textContent = (Array.isArray(paper[field]) ? paper[field].join(", ") : paper[field]) || missingValue;
          row.append(cell);
        }
        body.append(row);
      }
      const sourceRow = document.createElement("tr");
      const sourceHeading = document.createElement("th");
      sourceHeading.scope = "row";
      sourceHeading.textContent = "Primary sources";
      sourceRow.append(sourceHeading);
      for (const paper of comparedPapers) {
        const cell = document.createElement("td");
        const links = [
          sourceLink(paper.paper_url, "Read paper"),
          sourceLink(paper.project_url, "Project"),
          sourceLink(paper.survey_url, "External citation"),
        ].filter(Boolean);
        links.forEach((link, index) => {
          if (index) cell.append(document.createTextNode(" · "));
          cell.append(link);
        });
        if (!links.length) cell.textContent = missingValue;
        sourceRow.append(cell);
      }
      body.append(sourceRow);
      table.append(body);
      content.replaceChildren(table);
    }

    function restoreComparisonFocus() {
      const target = previousFocus;
      previousFocus = null;
      if (target?.isConnected && !target.closest("[hidden]") && !target.disabled) target.focus({ preventScroll: true });
      else search.focus({ preventScroll: true });
    }

    function closeComparison() {
      if (!dialog.open) return;
      if (typeof dialog.close === "function") dialog.close();
      else {
        dialog.removeAttribute("open");
        restoreComparisonFocus();
      }
    }

    function updateSelection() {
      const activeElement = document.activeElement;
      for (const control of controls) {
        const valid = byId.has(control.dataset.compare);
        control.checked = selected.has(control.dataset.compare);
        control.disabled = !valid || (!control.checked && selected.size >= maximumSelection);
      }
      bar.hidden = selected.size === 0;
      document.body.classList.toggle("compare-active", selected.size > 0);
      comparisonCount.textContent = `${selected.size} ${selected.size === 1 ? "paper" : "papers"} selected`;
      openButton.disabled = selected.size === 0;
      if (status) status.textContent = selected.size === maximumSelection
        ? "Three papers selected. Remove one to compare another."
        : "";
      if (dialog.open) {
        if (selected.size) renderComparison();
        else closeComparison();
      } else if (bar.hidden && bar.contains(activeElement)) {
        search.focus({ preventScroll: true });
      }
    }

    list.addEventListener("change", (event) => {
      const control = event.target.closest("input[data-compare]");
      if (!control || !byId.has(control.dataset.compare)) return;
      if (control.checked) {
        if (selected.size < maximumSelection || selected.has(control.dataset.compare)) selected.add(control.dataset.compare);
      } else selected.delete(control.dataset.compare);
      updateSelection();
    });
    clearButton.addEventListener("click", () => {
      selected.clear();
      updateSelection();
    });
    openButton.addEventListener("click", () => {
      if (!selected.size || dialog.open) return;
      previousFocus = document.activeElement;
      renderComparison();
      if (typeof dialog.showModal === "function") dialog.showModal();
      else dialog.setAttribute("open", "");
      closeButton.focus({ preventScroll: true });
    });
    closeButton.addEventListener("click", closeComparison);
    dialog.addEventListener("close", restoreComparisonFocus);
    dialog.addEventListener("cancel", (event) => {
      event.preventDefault();
      closeComparison();
    });
    dialog.addEventListener("click", (event) => {
      if (event.target !== dialog) return;
      const bounds = dialog.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) closeComparison();
    });
    dialog.addEventListener("keydown", (event) => {
      // Native dialogs handle Escape and focus trapping; support older previews too.
      if (typeof dialog.showModal === "function") return;
      if (event.key === "Escape") {
        event.preventDefault();
        closeComparison();
      } else if (event.key === "Tab") {
        const focusable = Array.from(dialog.querySelectorAll("a[href], button:not([disabled]), [tabindex='0']"));
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last?.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first?.focus();
        }
      }
    });
    content.addEventListener("click", (event) => {
      const remove = event.target.closest("button[data-remove-comparison]");
      if (!remove) return;
      const previousButtons = Array.from(content.querySelectorAll("button[data-remove-comparison]"));
      const index = previousButtons.indexOf(remove);
      selected.delete(remove.dataset.removeComparison);
      updateSelection();
      if (dialog.open) {
        const remaining = Array.from(content.querySelectorAll("button[data-remove-comparison]"));
        (remaining[Math.min(index, remaining.length - 1)] || closeButton).focus({ preventScroll: true });
      }
    });
    updateSelection();
  }

  function initializeAgentBar() {
    const bar = document.querySelector(".agent-float[data-run-hour]");
    const output = bar?.querySelector("[data-agent-countdown]");
    if (!bar || !output) return;
    const hour = Number(bar.dataset.runHour);
    const zone = bar.dataset.runZone || "America/New_York";
    if (!Number.isInteger(hour) || hour < 0 || hour > 23) return;

    function update() {
      try {
        const now = new Date();
        const parts = new Intl.DateTimeFormat("en-US", { timeZone: zone, hour: "numeric", minute: "numeric", hourCycle: "h23" }).formatToParts(now);
        const minutesNow = Number(parts.find((part) => part.type === "hour").value) * 60 + Number(parts.find((part) => part.type === "minute").value);
        let wait = hour * 60 - minutesNow;
        if (wait <= 0) wait += 24 * 60;
        const next = new Date(now.getTime() + wait * 60000);
        const label = new Intl.DateTimeFormat("en-US", { timeZone: zone, weekday: "short", hour: "numeric", minute: "2-digit", timeZoneName: "short" }).format(next);
        output.textContent = `${label} · in ${Math.floor(wait / 60)}h ${String(wait % 60).padStart(2, "0")}m`;
      } catch {
        // The static schedule text remains when time zones are unavailable.
      }
    }
    update();
    window.setInterval(update, 30000);
  }

  function initialize() {
    initializeAgentBar();
    initializeCatalogue();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initialize, { once: true });
  else initialize();
})();
