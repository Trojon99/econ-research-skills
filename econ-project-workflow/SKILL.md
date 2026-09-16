---
name: econ-project-workflow
description: "Economics research project workflow across Stata, Python, R, Julia, and mixed-language projects. Use when ChatGPT creates, edits, organizes, debugs, optimizes, refactors, or audits an economics research repository or analysis pipeline; designs project folders, project entrypoints, data lifecycle, intermediate files, logs, caching, reproducibility, validation, figures/tables, or cross-language handoffs; or reviews code where workflow architecture matters. Preserve the standard project layout code, data/original, data/work, data/temp, data/output, doc, and log unless the user specifies otherwise. Load language-specific backend guidance when available; detailed Stata conventions live in references/stata.md."
---

# Economics Project Workflow

Treat the research project as a reproducible system rather than a collection of scripts. Keep the project architecture stable across programming languages while allowing the implementation backend to change.

## Core priority

Use this priority order:

1. Preserve the correct statistical, economic, and data definitions.
2. Preserve a reproducible and auditable project/data flow.
3. Minimize unnecessary runtime, repeated large-data passes, and duplicated expensive work.
4. Make code and artifacts explicit enough to review and debug.
5. Only then optimize for brevity, abstraction, or stylistic elegance.

Never trade a correct sample, denominator, weight, timing definition, model object, or estimand for speed.

## Stable project contract

Use this project layout by default unless the user explicitly specifies another structure:

```text
project_root/
├── code/
├── data/
│   ├── original/
│   ├── work/
│   ├── temp/
│   └── output/
├── doc/
└── log/
```

Read `references/project-structure.md` when creating, reorganizing, or auditing a project repository.

Keep these meanings stable across languages:

- `code/`: executable research code and orchestration.
- `data/original/`: immutable source data; never overwrite during analysis.
- `data/work/`: meaningful cleaned, merged, analysis-ready, cached, model-ready, or machine-readable supporting data that downstream work depends on.
- `data/temp/`: disposable intermediates that are safe to delete and regenerate.
- `data/output/`: final human-facing figures, tables, reports, and presentation-ready research outputs; do not use it as a general data cache.
- `doc/`: codebooks, questionnaires, technical notes, data manuals, research documentation, and related reference material.
- `log/`: execution logs, diagnostics, and run records.

Do not introduce alternative top-level folders such as `results/`, `processed/`, `figures/`, or `tables/` merely because a language or package defaults to them. Put final human-facing artifacts under `data/output/` and reusable machine-readable products under `data/work/` unless the user explicitly chooses a different convention.

## Use one clear project entrypoint

Every project should have a clear normal entrypoint that can reproduce the intended pipeline.

Examples:

- Stata: `00_master.do`.
- Python: a clear driver such as `run_pipeline.py` or `main.py`.
- R: a clear driver such as `run_pipeline.R`.
- Mixed-language projects: use the simplest orchestration layer that can reliably express dependencies and execution order.

Do not introduce Make, Snakemake, targets, containers, environment managers, or other workflow infrastructure solely for sophistication. Use them only when the user asks or the project has enough cross-language/dependency complexity to justify them.

The entrypoint should define paths/configuration, establish run/rebuild switches when useful, create required folders, open logging, and call substantive modules in dependency order. Keep detailed estimation/model specifications inside their substantive modules rather than turning the entrypoint into a monolith.

## Organize by substantive stage

Separate stages when they have different inputs, outputs, or research responsibilities. Typical stages include:

1. source-data cleaning;
2. core master construction;
3. auxiliary/module merges;
4. variable/sample construction;
5. descriptive analysis and figures;
6. main estimation or model solution;
7. robustness/validation;
8. mechanisms, heterogeneity, counterfactuals, or extensions;
9. paper-facing outputs.

Use ordered filenames when execution order matters. The exact numbering and file extension may vary by language.

Avoid both extremes:

- one enormous script containing the entire research project;
- dozens of tiny files whose boundaries add navigation cost without clarifying data flow or research responsibilities.

## Track inputs, outputs, units, and keys

Start substantive modules with a concise header or docstring that states, when relevant:

- purpose;
- main inputs;
- main outputs;
- unit of observation or model object;
- key/panel/index structure;
- important sample restrictions or dependencies.

Keep these descriptions factual and update them when responsibilities change.

## Data lifecycle and reproducibility

Read `references/data-lifecycle-reproducibility.md` whenever the task involves raw-data protection, intermediate files, caching, reruns, randomness, logs, merge/join validation, or cross-language handoffs.

Core rules:

- Treat `data/original/` as read-only.
- Build downstream objects deterministically from source data and code where possible.
- Cache expensive stable products in `data/work/` rather than recomputing them unnecessarily.
- Keep scratch products in `data/temp/` only when they are genuinely disposable.
- Preserve the machine-readable data behind important figures and tables in `data/work/`.
- Restrict observations/variables early only when doing so cannot alter required lags, leads, baselines, transitions, joins, model states, or future-status definitions.
- Set and document seeds for stochastic operations.
- Keep machine-specific absolute paths in the entrypoint/configuration layer rather than scattering them through substantive code.

## Fail fast and validate structural assumptions

Prefer explicit validation near the source of an error.

Check, when relevant:

- required files and variables/columns/objects exist;
- keys are unique at the intended level;
- joins/merges have the expected match structure;
- categories, ranges, dates, and panel order are valid;
- observation/person/entity counts are plausible;
- transition/risk-set definitions are internally consistent;
- weights and missing-value rules are preserved;
- model inputs have valid dimensions/support.

Do not silently discard unexpected join states, duplicate keys, failed assertions, or malformed objects just to let the pipeline continue.

## Optimize the expensive operations

Focus optimization on operations that materially affect runtime or memory:

- repeated full-data scans;
- repeated large-file reads/writes;
- repeated joins/merges of a large master;
- unnecessary reconstruction of stable intermediates;
- deeply nested loops around expensive data operations;
- carrying hundreds of unused variables/columns through later stages.

Prefer bulk/grouped/vectorized operations when they preserve the intended statistical definition. Code repetition is acceptable when it is faster, clearer, and less error-prone than an abstraction that repeatedly scans large data.

## Route to the implementation backend

Identify the language/tool from the files, request, or existing repository conventions.

### Stata

Read `references/stata.md` whenever the project uses `.do`/`.ado` files, Stata commands, Stata merges/weights/macros, or the user requests Stata implementation. Apply the Stata-specific performance and code-style rules in addition to this generic workflow.

### Python, R, Julia, or mixed-language projects

Apply the generic workflow first, then use idiomatic, current practices for the actual language and libraries. Preserve the same folder semantics, entrypoint discipline, validation, data lifecycle, and output contract unless the user has an established project convention that should take precedence.

Do not invent a language-specific house style before the user has one. When repeated patterns become stable and opinionated enough to justify reusable guidance, add a dedicated backend reference rather than bloating this `SKILL.md`.

## Figures, tables, and result-review outputs

Default project contract:

- exploratory/review figures: `.png` unless another format is requested;
- paper/presentation formats: change only when the downstream workflow requires it;
- tables: use a human-readable format appropriate to the user's workflow;
- figure/table source data: `data/work/`;
- final human-facing artifacts: `data/output/`.

When the user asks for a figure/result review HTML, read `references/figure-review-html-benchmark.md` and use `assets/figure-review-template.html`. The report should evaluate the empirical role and interpretation boundary of each figure, not merely display an image gallery.

## Work with the other economics skills

Keep workflow implementation separate from methodological judgment:

- `econ-research-design`: research question, evidence strategy, measurement, contribution, and preference-elicitation design.
- `causal-inference`: estimand, identifying variation, assumptions, estimator-design fit, and inference.
- `econ-descriptive-analysis`: graph-first descriptive diagnostics, sample support, event-time/raw-pattern analysis, and parallel-trends figures.
- `econ-project-workflow`: repository architecture, data flow, implementation, performance, validation, reproducibility, and research-output plumbing.
- `econ-paper-writer`: source-grounded paper prose and LaTeX.

If a coding request reveals a causal-identification or research-design problem, surface it and route the substantive issue to the appropriate skill rather than solving it through code architecture alone.

## Default review behavior

When reviewing an existing research project:

1. reconstruct the project entrypoint and dependency order;
2. map inputs and outputs by stage;
3. verify folder/data-lifecycle semantics;
4. identify correctness and reproducibility risks;
5. identify the largest runtime/I/O bottlenecks;
6. distinguish project-architecture problems from language-specific code problems;
7. recommend the smallest set of structural changes that materially improves the project.

Do not refactor merely for style. Preserve working project conventions unless a change has a clear correctness, performance, reproducibility, or auditability benefit.
