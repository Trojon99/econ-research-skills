# Economics Writing Style Conventions

## Calibrate genre and audience

Before a substantial draft or rewrite, identify the target genre, venue, audience, length, and purpose. Do not transfer conventions mechanically across genres.

- Present a journal article as completed research only to the extent supported by the supplied evidence.
- Give a job-market or seminar paper enough explanation for readers outside the narrow subfield without turning it into a dissertation chapter.
- Distinguish proposed work from completed findings in a grant proposal.
- Keep revision narration in a response letter rather than the paper itself.
- Explain technical objects for a policy-facing audience without weakening qualifications or changing the estimand.
- Follow an explicit target-journal or user-supplied template before any default in this reference.

## Maximize functional density

Make each sentence ask the question, introduce evidence, define an object, explain a mechanism, interpret a result, qualify a claim, or advance the argument. Remove a sentence only after confirming that it performs none of these functions.

Before drafting or revising a paragraph, identify:

1. its economic object;
2. its comparison or counterfactual;
3. its claim type: fact, estimate, assumption, mechanism, model implication, interpretation, or limitation;
4. its role in the section.

State the paragraph's logical role early. Let each later sentence support, qualify, interpret, or extend what precedes it. Build transitions through the next substantive task rather than repeated generic connectors.

Make relative language recoverable. Whenever an outcome is larger, smaller, increasing, declining, persistent, or changing, name the comparison group, period, outcome, model case, or benchmark.

## Edit by function before diction

Before line-editing a substantial passage, identify what each sentence is doing. Typical functions are: question; institutional or economic setup; data and measurement; variation and identification; model setup or assumption; result; mechanism or intuition; literature relation or contribution; scope or limitation; and reader guidance. A sentence may combine closely related functions, but it should not remain merely because it sounds fluent.

If a paragraph hides its economic point behind setup, generic motivation, or literature narration, fix the order before polishing individual phrases. In abstracts, introduction previews, and results sections, put the question, comparison, or main result early when the supplied evidence supports doing so. In theory sections, establish the economic environment before dense notation. In empirical-strategy sections, make the comparison and source of variation intelligible before relying on an estimator label or equation.

Use verbs that match the inferential object. `Document` is appropriate for descriptive patterns; `estimate` and `identify` require an estimand and the corresponding design strength; `imply` is natural for model results; `is consistent with` is often appropriate for suggestive mechanism evidence. Do not upgrade a verb merely to make the sentence sound stronger.

## Preserve information during revision

Before shortening, polishing, translating, or reorganizing, inventory the content that must survive:

- the main contribution and any strategically necessary secondary contribution;
- the research question, mechanism, and warranted interpretation;
- the data or design feature that supports the claim;
- key magnitudes, units, comparisons, and uncertainty;
- maintained assumptions, limitations, and scope conditions;
- defined terms, citations, notation, and cross-references.

Compress wording before deleting a central analytical object. After rewriting an abstract, introduction, contribution paragraph, results summary, or conclusion, compare it with the source and restore any protected content that disappeared. Do not replace a missing premise, result, or transition with smooth but unsupported prose; mark the gap or request the needed input.

For a local edit, change only what the request requires. For a global edit, check that terminology, claims, section promises, and reported magnitudes remain consistent across the paper.

## Control tone and claims

Use restrained, precise language. Make strong wording earn its place through an estimate, comparison, design feature, model result, or institutional fact.

- Specify the dimension when claiming novelty: setting, data, measurement, identification, mechanism, model, counterfactual, or policy interpretation.
- Avoid promotional superlatives unless the user supplies support and the target genre permits them.
- Replace personal opinion markers with evidence-based statements.
- Use causal verbs only when the stated design warrants them; otherwise use calibrated alternatives such as `is consistent with`, `suggests`, `supports the interpretation`, or `implies in the model`.
- Prefer plain verbs such as `use`, `show`, `estimate`, `compare`, `test`, `discipline`, and `simulate` over inflated packaging.
- Use first person when it identifies the author's action clearly. Do not force an awkward passive construction merely to avoid `I` or `we`.

## Separate results from mechanisms

In a results section, prioritize the estimand, sign, magnitude, unit, benchmark, uncertainty, and economic interpretation. Discuss a mechanism only when the cited table, figure, test, or model exercise bears on that channel.

In a mechanism section, separate the observed pattern, the proposed interpretation, and the evidence for the channel. Treat mechanism evidence as suggestive unless the design directly identifies it.

## Standardize tables and figures

Follow the user's template or target-journal style first. Otherwise:

- use concise sentence-case titles and omit a final period when the convention permits;
- make notes identify the sample, controls, fixed effects, clustering, standard errors, and significance conventions when relevant;
- for structural work, identify calibrated parameters, targeted and untargeted moments, simulation details, or counterfactual definitions when relevant;
- distinguish author calculations, externally sourced data, and reproduced material in source lines;
- never add an unspecified control, estimator, source, or simulation detail merely to make a note look complete.

## Standardize numbers, units, dates, and citations

- Keep units and rounding consistent across prose, equations, tables, and figures.
- Use numerals for years, statistics, sample sizes, parameter estimates, and quantitative results.
- Use `percent` in prose and `%` in compact rendered tables when consistent with the target style. Write `\%` in LaTeX source so the symbol is not parsed as a comment.
- Put spaces around relation signs in prose mathematics when the surrounding LaTeX convention permits.
- Use en dashes for numeric and year ranges in rendered prose; preserve valid LaTeX range conventions in source files.
- Preserve the paper's citation system. For LaTeX, follow the citation commands and bibliography workflow specified in `SKILL.md` and the project template.
- Never invent authors, dates, page numbers, volumes, initials, data details, assumptions, estimates, or reference metadata. Mark unresolved details explicitly.

## Run a final style audit

Verify that every paragraph has a recoverable function, every comparison has a benchmark, every strong claim has support, every quantitative statement has the correct unit, and every citation follows the active system. Compare revised high-value sections with their source text to catch information loss before delivery.
