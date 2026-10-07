# Daily research agent

The agent finds new embodied in-context learning work, verifies each candidate against its primary source, and proposes it for human review in a pull request. It never changes the collection, the manuscript mapping, the website sources, or the framework. People decide what enters the collection.

Read `AGENTS.md` before every run. Its source-authority rules apply here: our manuscript defines the framework; the external survey supplies the 412-work inventory and its reference numbers. A new candidate never receives an external survey number, and a framework label on a candidate is only a review suggestion.

## One run

1. **Date and window.** The run date is today in `America/New_York`. The window starts at the `run_date` of the newest `docs/daily-collection/*.json` and ends at the run date. With no earlier report, look back 30 days. Never accept a work dated after the run date.
2. **Baseline for de-duplication.** Ignore arXiv version suffixes and compare by identifier, then by exact title (case-insensitive):
   - `data/survey-references.json` (`arxiv_id`, `title`): the 412-work collection;
   - `data/manuscript-mapping.json` (`title`, `name`): our manuscript's roadmap examples;
   - every candidate in earlier `docs/daily-collection/*.json` files.
   A known work is listed under the de-duplication heading of the report, never as a new candidate.
3. **Search.** Use the arXiv API as the primary, date-sorted source, for example:
   `curl -s "https://export.arxiv.org/api/query?search_query=abs:%22in-context%22+AND+abs:robot&sortBy=submittedDate&sortOrder=descending&max_results=100"`.
   Cover at least: `abs:"in-context" AND abs:robot`; `abs:"in-context learning" AND (abs:embodied OR abs:manipulation OR abs:locomotion OR abs:navigation OR abs:driving OR abs:drone)`; `abs:"in-context imitation"`; `abs:"in-context" AND abs:"vision-language-action"`; `abs:"in-context reinforcement learning"`. Add a web search for the same window as a secondary discovery source. Record every query in the report.
4. **Screen.** Keep a work when its abstract describes an embodied agent that adapts at deployment from context (demonstrations, language, images or video, trajectories, retrieved or self-built experience), or a benchmark or analysis of that ability. Use `priority: "boundary"` when the link to in-context adaptation is uncertain. An extra input alone does not establish learning.
5. **Verify.** Open each kept candidate's arXiv abstract page. Record the exact title, the first authors, the first submission date (UTC), the current version, and what the abstract states. Never rely on a search snippet.
6. **Suggest a classification.** Using our manuscript's framework only:
   - `form`: `text`, `visual`, `trajectory`, `multimodal`, or `null`;
   - `roles`: any of `task`, `state`, `behavior`, or empty when unsupported;
   - `self_built`: `true`, `false`, or `null`;
   - the deployment update regime, in the report text, only where the abstract states it.
   Unknown stays unknown. These are suggestions for reviewers, not mappings.
7. **Write two files.**
   - `docs/daily-collection/YYYY-MM-DD.md`: the report, in Chinese and in the structure of the newest earlier report. Include the window and counts, a `## 待审核候选` table (候选及原始来源 | arXiv 提交日期 / 版本 | 与库内条目的区别、相关性 | 上下文形式 / 部署作用（暂定） | 参数更新证据及审核重点), `## 去重和已知条目检查`, `## 检索记录与覆盖限制`, and a `## 人工审核入口` checklist with one item per candidate.
   - `docs/daily-collection/YYYY-MM-DD.json`: the machine-readable summary described below, every candidate with `"decision": "pending"`.
   When a report for the run date already exists, add a new section to it and append candidates to its JSON. With no new candidates, still write both files: an empty candidate list and the full search log show that the run happened.
8. **Change nothing else.** No edits to `data/`, `site/`, `scripts/`, `tests/`, generated documents, `AGENTS.md`, or this file.
9. **Validate.**
   ```sh
   python3 scripts/build_readme.py --check
   python3 -m unittest discover -s tests
   python3 scripts/build_site.py --output /tmp/daily-site
   python3 scripts/build_site.py --output /tmp/daily-site --check
   ```
   The tests reject malformed summaries, candidates already in the collection or roadmap, repeated candidates, and future dates. Fix only your own report files.
10. **Open a pull request for human review.** Branch `daily/YYYY-MM-DD` from the latest `origin/main`; commit `Daily research run YYYY-MM-DD: N candidates for review`; push the branch; open a pull request into `main` titled `Daily research run YYYY-MM-DD — N candidates (needs human review)`, using `.github/pull_request_template.md`; add the label `needs-human-review`. If a pull request for that date is already open, push to its branch instead. Never merge, approve, enable auto-merge, or push to `main`.
11. **Finish** with the pull request link and a three-line summary: candidates found, boundary cases, and anything a reviewer should check first.

## Summary file

```json
{
  "run_date": "YYYY-MM-DD",
  "timezone": "America/New_York",
  "report": "docs/daily-collection/YYYY-MM-DD.md",
  "note": "Forms and roles are review suggestions from abstracts, not manuscript mappings.",
  "candidates": [
    {
      "name": "Short name used in the report",
      "title": "Exact arXiv title",
      "url": "https://arxiv.org/abs/2610.01234v1",
      "arxiv_id": "2610.01234",
      "submitted": "YYYY-MM-DD",
      "priority": "core | boundary",
      "form": "text | visual | trajectory | multimodal | null",
      "roles": ["task", "state", "behavior"],
      "self_built": null,
      "decision": "pending"
    }
  ]
}
```

## Reviewing a daily pull request

Reviewers open each candidate's arXiv page, then set every `decision` in the JSON to `accepted`, `rejected`, `deferred`, or leave it `pending`, and merge once CI passes. The website counts pending candidates in its agent bar and survey map but never names them. Adding an accepted work to the collection or the manuscript mapping is a separate, reviewed change with recorded evidence.
