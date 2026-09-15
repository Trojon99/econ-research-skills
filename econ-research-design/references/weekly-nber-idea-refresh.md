# Weekly NBER Idea Refresh

Use this reference to turn a weekly batch of new NBER working papers into disciplined updates to the user's economics research ideas.

## Separate Scheduling from Research Judgment

Use a scheduled task for recurring retrieval. Invoke `$econ-research-design` in the scheduled-task prompt so the same source, evidence, and contribution rules apply on every run.

Schedule the run after NBER's Monday-morning release in the user's local time zone. Use the existing research chat when the task should retain the user's idea context; use a standalone task only when each digest should be independent.

## Retrieve the Weekly Batch

Prefer currently available official NBER sources, including:

- the [NBER Working Papers page](https://www.nber.org/papers) and its **New This Week** listing;
- an official [NBER RSS feed](https://back.nber.org/rss/new.xml) for the latest working papers;
- NBER's [weekly-updated Working Papers and Chapters metadata](https://www.nber.org/research/data/nber-working-papers-and-chapters-metadata).

If an endpoint is unavailable, locate the current equivalent on the official `nber.org` domain rather than substituting an unofficial aggregator.

Use the release date and working-paper number to avoid reprocessing earlier items. If persistent last-run state is unavailable, define the batch by the most recent official weekly release window and disclose that limitation.

Record for each paper:

- NBER working-paper number;
- verified title and authors;
- release date and official URL;
- program, topic, or JEL code when available;
- abstract-level research question, data or setting, method or model, principal result, and stated contribution;
- access level: metadata, abstract, working-paper text, or another verified version.

Do not claim to have read the paper when only metadata or the abstract is available. Do not infer identifying assumptions, robustness, welfare implications, or detailed contributions from the abstract unless stated there.

## Filter for Relevance

Compare the batch with the user's:

- uploaded materials;
- active and parked research questions;
- stated fields, mechanisms, methods, data, and settings;
- Zotero papers used as anchors.

Retain a paper when it changes a novelty claim, reveals a close design or mechanism, offers a relevant data or measurement opportunity, challenges an assumption, or exposes an unresolved economic tension. Summarize unrelated papers only when the user requests a complete NBER digest.

## Produce Idea Deltas

For every retained paper, classify the effect:

| Delta | Meaning | Required response |
|---|---|---|
| Collision | Direct overlap weakens the active idea | Name the overlapping object and propose repair or parking |
| Refinement | Clarifies the question, mechanism, design, or boundary | State the exact revision and why it improves the idea |
| Extension | Creates a complementary or adjacent test | Verify that the extension changes what economists learn |
| Method/data opportunity | Changes feasibility | Explain the object enabled; do not claim novelty from the tool alone |
| New candidate | Reveals a distinct unresolved tension | State the uncertainty, evidence path, closest work, and largest unknown |
| No material update | Adds context but does not change the idea | Do not force a revision |

Use this compact structure for each material delta:

1. **New paper:** verified citation and link.
2. **What it establishes:** source-backed only.
3. **Idea affected:** the specific active or parked idea.
4. **Delta:** collision, refinement, extension, opportunity, new candidate, or none.
5. **Why:** the economic and literature relationship.
6. **Proposed change:** a bounded revision, clearly labeled as a proposal.
7. **Confidence and missing evidence:** abstract-only, full-text verified, or unresolved.

## Apply a Novelty Check

Do not call an idea new solely because it arose from a new paper. Require:

- a precise economic uncertainty;
- a meaningful difference from verified closest work;
- a mechanism, object, counterfactual, welfare issue, or interpretation that matters;
- a feasible evidence, identification, theory, measurement, or structural path;
- at least one result that would weaken the idea.

Use NBER as a discovery source. Search beyond NBER before asserting novelty or absence from the literature.

## Preserve User Control

Never replace the baseline idea ledger automatically. Present proposed additions, revisions, collisions, and parking decisions for approval. Carry forward only changes the user accepts or that are explicitly labeled as provisional candidates.

Do not generate an RP, research plan, or long proposal during the weekly run unless explicitly requested. Keep the default output to a concise weekly evidence brief and idea deltas.
