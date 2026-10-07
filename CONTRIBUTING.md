# Contributing

Read `AGENTS.md` before changing source authority. The user confirmed that **our work is the manuscript *In-Context Learning for Embodied Agents: Methods, Benchmarks, and Open Challenges*** and **the survey *In-Context Learning for Robots: Methods and Applications* (arXiv:2609.36012) is external work**. Neither PDF is kept in this repository. Keep all 412 externally collected works and organize them with our manuscript’s structure.

## Update the conceptual framework

Our manuscript’s Figure 2 and sections II–VII govern the website. The main axes are context form (text, visual, trajectory, multimodal) and context role (task, state, behavior). Deployment updates and self-built context are separate distinctions.

`data/manuscript-mapping.json` records each roadmap example’s manuscript reference number, source pages, forms, roles, and optional identity match to the external inventory. Match works by bibliographic identity, not similar acronyms. A null external reference preserves a manuscript-only example; it does not exclude it from our framework. In particular, RoboSSM is present in our manuscript even though it is absent from the external inventory.

Do not infer assignments for the remaining 374 collected works. Add mappings only after checking supporting evidence, and record their source and scope. Multiple assignments are allowed where supported. Keep reference numbers and page citations specific to their source PDF.

## Correct the external inventory

`data/survey-references.json` retains every external reference [1]–[412], original title, citation, URL, date provenance, bibliography pages, and Appendix A group. Its original groups remain external metadata and must not become our main taxonomy.

1. Identify the external reference and supporting page.
2. Correct extraction logic in `scripts/extract_survey.py` if necessary.
3. Reproduce the inventory and run `python3 scripts/extract_survey.py --check` with PyMuPDF installed.
4. Document source discrepancies rather than silently changing source claims.

The external snapshot includes methods, supporting works, and parameter-adaptation comparisons. Inclusion is not proof of frozen deployment weights. Preserve all 412 works when extending annotations or the manuscript mapping.

## Reading notes

`data/survey-annotations.json` maps the original notes in `data/papers.json` to external references. Its supporting pages refer to the external PDF. The 21 displayed notes remain separate from our manuscript classifications. The two unmatched legacy notes remain in the original data for audit history; RoboSSM also has an explicit manuscript roadmap record.

New notes need a precise source passage and a clear deployment configuration. Record context, action mechanism, update status, evaluation setting, limitations, and context amount only where supported. Avoid invented budgets, physical evaluations, numerical results, or capability labels. Record independent primary-paper reviews separately from survey summaries.

## Daily research agent

A scheduled agent searches for new embodied in-context learning work each morning (America/New_York) and follows `agents/daily-research/INSTRUCTIONS.md`. It writes a Chinese report and a JSON summary to `docs/daily-collection/` and opens a pull request labelled `needs-human-review`. It never edits the collection, the manuscript mapping, or the website sources.

To review a run, open each candidate's arXiv page, set every `decision` in the JSON summary to `accepted`, `rejected`, `deferred`, or `pending`, and merge once CI passes. The website counts pending candidates but never names them. Add an accepted work to the collection in a separate change with recorded evidence.

## Build and validate

```sh
python3 scripts/build_readme.py
python3 -m unittest discover -s tests
node --check site/app.js
python3 scripts/build_site.py
python3 scripts/build_readme.py --check
python3 scripts/build_site.py --check
```

The README’s marked sections (badges, statistics, roadmap tables, daily status, and the reference index), CATALOGUE.md, PROTOCOLS.md, and `_site/` are generated. Edit their sources and regenerate. README content between `<!-- github-only:start -->` and `<!-- github-only:end -->` (banner, badges, images, diagrams) appears on GitHub only and is left out of the website’s README page.

The README images in `assets/readme/` are snapshots. When the counts or the survey map change, rebuild the site, serve `_site/` locally, and run `node scripts/capture_readme_images.js http://127.0.0.1:8765/` (requires Playwright). The README banners (`banner-light.svg`, `banner-dark.svg`), the site’s navigation mark, and `site/favicon.svg` come from the approved brand kit; replace them as files rather than redrawing them. The normal build needs Python 3.11+ and its standard library. Neither PDF is published: external page links point to arXiv v1 of the external survey, and `data/sources.json` records the checksum of each PDF the data was built from. A new PDF version requires review of the source identity, mappings, citations, and checksums together.
