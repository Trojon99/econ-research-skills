# Weekly NBER Idea Refresh

Use this reference to turn a weekly batch of new NBER working papers into disciplined updates to the user's economics research ideas.

## Separate Scheduling from Research Judgment

Use a scheduled task for recurring retrieval. Invoke `$econ-research-design` in the scheduled-task prompt so the same source, evidence, and contribution rules apply on every run.

Schedule after the official weekly release in the user's named IANA time zone, using wall-clock scheduling rather than a fixed UTC offset so daylight saving does not shift the intended hour. List existing jobs before creating one; verify the saved schedule, enabled state, next occurrence, and delivery target by reading the job back. Distinguish the trigger time from the later report-completion time.

Treat every scheduled execution as a fresh session even when delivery targets an existing Bot Chat. Include the user's fields, source hierarchy, evidence gates, state location, output format, and skill-write permissions in the task prompt. Use previous-output continuity only as an aid; a persistent paper ledger is the authority for coverage and deduplication. Do not assume current uploads or Zotero access are inherited. Launch a first manual test when appropriate and distinguish a launched test from a verified successful report; do not poll asynchronous runs.

## Retrieve the Weekly Batch

Prefer currently available official NBER sources, including:

- the [NBER Working Papers page](https://www.nber.org/papers) and its **New This Week** listing;
- an official [NBER RSS feed](https://back.nber.org/rss/new.xml) for the latest working papers;
- NBER's [weekly-updated Working Papers and Chapters metadata](https://www.nber.org/research/data/nber-working-papers-and-chapters-metadata).

If an endpoint is unavailable, locate the current equivalent on the official `nber.org` domain rather than substituting an unofficial aggregator.

Parse the official full list or XML into a persistent inventory; do not count a truncated extraction, search-result page, or the entire multiweek RSS feed as the current batch. Deduplicate by working-paper number and compute counts in code, comparing with the official batch where possible. Record the batch date and distinguish newly issued papers from revisions.

Keep discovered, abstract-screened, full-text-read, access-blocked, and deferred states separately. Advance completion markers only for completed work; save partial progress and resume the backlog so a timeout does not silently discard unread papers. If persistent last-run state is unavailable, start with the latest official weekly release window and disclose the lack of historical coverage. If the official batch cannot be established, label the scan partial rather than inventing completeness.

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

When whole-batch coverage is requested, screen all newly issued papers at abstract level and save the complete short inventory, then select a manageable set for deep reading according to the configured research priorities. Preserve deployment-specific schedules, fields, and delivery preferences locally rather than embedding them in the public workflow. Use legal NBER access or a verified public author version; label access limits and version differences. Do not imply that every new paper has been read in full.

Retain a paper for deeper analysis when it changes a novelty claim, reveals a close design or mechanism, offers a relevant data or measurement opportunity, challenges an assumption, or exposes an unresolved economic tension. Provide a brief whole-batch thematic overview while reserving detailed discussion for relevant or transferable papers.

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

## Accumulate Transferable Skill Knowledge

1. Read the target skill and its existing references before writing; search for the same lesson and strengthen it rather than duplicating it.
2. Admit a lesson only when the relevant full text has been read and supports the transferable claim. Store the official link, paper number, version, reading level, and supporting section/page when verified. Separate the authors' result from the assistant's generalization; include assumptions, applicability, rival explanations, and remaining limits. A new working paper is not automatically a settled methodological rule.
3. Integrate by knowledge subject into a small set of existing references. Use a topical frontier reference only when the parent has no suitable home; do not create per-paper or per-week files. Add a short entrypoint pointer only when needed. Keep shared evidence gates in the entrypoint or its reference routing; keep deployment-specific user preferences local.
4. Make authorized non-destructive reference updates with `skill_manage`, preserving project-specific local amendments. An owner may explicitly authorize direct commits and normal fast-forward pushes to the maintained branch after source, privacy, packaging, and staged-diff checks pass; otherwise use the agreed review workflow. Authorization does not waive evidence checks or branch protections. Never publish private project details, raw data, complete copyrighted PDFs, credentials, or unrelated local overlays. Keep substantial rewrites of core identification rules and changes to the user's research agenda subject to explicit review. If no evidence qualifies, report no skill change rather than forcing one.
5. Verify the affected reference is readable after writing and report exact files, learned principles, sources, and pending changes. Before public synchronization, work from a clean, up-to-date repository checkout and whitelist the intended public reference files and minimal entrypoint/documentation changes, not the whole profile directory. Recheck source claims and their limitations, run existing repository validation/tests and `git diff --check`, update version/changelog consistently, inspect the staged diff for private paths and identifiers, and use explicit file staging. Do not force-push, weaken protections, or resolve substantive conflicts silently; failed checks keep the update local with a clear report. After push, read the exact remote commit and files back, report the commit URL, and record intentionally retained local differences. Treat packaging/installation checks as distinct from verifying paper claims.

## Report Coverage and Learning

Deliver a concise brief in the requested language with the official batch scope, programmatically verified counts, actual full-text versus abstract coverage, thematic overview, prioritized reading recommendations, bounded research implications, skill changes, and unresolved access/backlog. Keep the complete per-paper inventory in a separate report. Show recommended-but-unread papers distinctly from completed deep readings. Never claim that a dispatched run has already delivered or that accumulated documents retrained the model.

## Preserve User Control

Never replace the baseline idea ledger automatically. Present proposed additions, revisions, collisions, and parking decisions for approval. Carry forward only changes the user accepts or that are explicitly labeled as provisional candidates.

Do not generate an RP, research plan, or long proposal during the weekly run unless explicitly requested. Keep the default output to a concise weekly evidence brief and idea deltas.
