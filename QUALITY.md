# Source and annotation quality

Our manuscript, **In-Context Learning for Embodied Agents: Methods, Benchmarks, and Open Challenges**, defines the website’s framing, context forms, and deployment roles. The external **In-Context Learning for Robots: Methods and Applications** supplies the preserved 412-reference inventory. These are different works, with separate authorship, numbering, and page citations.

## Evidence layers

| Layer | Authority | Interpretation limit |
| --- | --- | --- |
| Conceptual structure | Our manuscript, Figure 2 and sections II–VII | Forms and roles are independent axes |
| Manuscript mapping | Figure 2, p. 4; identity matches to bibliography pp. 13–15 | 38 of the 412 records are explicitly mapped; other mappings are pending |
| Additional roadmap examples | 29 works in our manuscript outside the external inventory | Recorded separately, including RoboSSM; never silently excluded from our framework |
| Reference coverage | All external references 1–412, with full citations and page links | Inclusion does not mean every work is a fixed-weight ICL method |
| Original classification | External Appendix A, pp. 96–97 | External metadata; not our taxonomy |
| Dates | External Appendix A first public year, otherwise bibliography year | Publication and first public release can differ |
| Reading notes | 21 notes grounded in external PDF passages | Separate from the manuscript roadmap assignments |
| Context amounts | Explicit amounts supported by external passages | Unknown means unannotated, not zero |

[Source identities and checksums](data/sources.json), [our roadmap mapping](data/manuscript-mapping.json), [external inventory](data/survey-references.json), and [external annotation audit](data/survey-annotations.json) record the provenance. The external survey is public on [arXiv](https://arxiv.org/abs/2609.36012), and page links point to its v1 PDF. Our manuscript is not yet public.

## Scientific boundaries

Context conditioning alone does not demonstrate learning. Our manuscript distinguishes task specification, state representation, and behavior specification. Self-built context describes how evidence is obtained. Gradient-free, update-optional, and update-dependent configurations must be identified separately; RICL appears in two configurations in the roadmap.

Empty form or role fields mean the roadmap has not supplied that assignment. A mapped work may appear only under broader domains or evaluation. No categories, experimental results, physical evaluations, or deployment regimes are inferred from titles or inclusion alone.

Bibliographic links are transcribed from source PDFs; current availability is not independently guaranteed. Reading notes report source claims; this project has not replicated the experiments.

## Checks

The build verifies both PDF checksums and keeps their public filenames distinct. Tests protect the complete 412-record inventory, manuscript mapping, source links, framework placement, and deterministic outputs. Human review remains necessary for new classifications and scientific claims.
