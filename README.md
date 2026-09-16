# Econ Research Skills

**Current version:** `v0.3.0`  
**Maintenance status:** Actively maintained  
**Last updated:** 2026-09-16  
**Source of truth:** GitHub `main`

A growing collection of reusable AI skills for economics research, from research design and empirical analysis to academic writing, causal inference, project workflows, and future macroeconometric and quantitative-method modules.

## Skills

| Skill | Purpose |
| --- | --- |
| `econ-research-design` | Develop and stress-test economics research questions, literature positioning, evidence strategies, contributions, and preference-elicitation designs. |
| `causal-inference` | Design and audit causal identification strategies, estimands, inference, and implementation choices. |
| `econ-descriptive-analysis` | Produce research-design-oriented descriptive analysis, diagnostics, and figures, including relative-time parallel-trends protocols. |
| `econ-project-workflow` | Organize reproducible, auditable, performance-aware economics research projects across Stata, Python, R, Julia, and mixed-language workflows. |
| `econ-paper-writer` | Draft and revise source-grounded economics prose and LaTeX while preserving research meaning. |
| `seminar-companion` | Find the latest working-paper version, open with Title / Research Question / Empirical Methodology / Data / Main Evidence, and follow academic seminars live. |

## Architecture

The library is organized by research function rather than by estimator, programming language, or narrow method.

- `econ-research-design` is the upstream research-design layer. It frames questions, maps evidence strategies, positions literature, and routes specialized methodological work.
- `causal-inference` handles identification, estimands, estimator-design fit, inference, and causal-method audits.
- `econ-descriptive-analysis` handles graph-first pre-regression diagnostics, sample support, trends, raw DID/DDD patterns, and descriptive event-time evidence.
- `econ-project-workflow` governs repository architecture, data lifecycle, project entrypoints, performance, reproducibility, validation, outputs, and implementation backends. Stata-specific conventions live under its references rather than as a separate top-level skill.
- `econ-paper-writer` handles source-grounded writing and editing without silently redesigning the research.
- `seminar-companion` is a cross-cutting live workflow layer that can route deeper methodological and implementation questions to the relevant skill.

Detailed methods or implementation backends that do not require their own top-level workflow should live as references under the most natural parent skill. For example, preference elicitation is maintained under `econ-research-design/references/preference-elicitation.md`, and Stata implementation conventions are maintained under `econ-project-workflow/references/stata.md`.

## Repository structure

Each skill follows the ChatGPT Skills directory convention:

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/    # optional
└── assets/        # optional
```

`SKILL.md` is the entry point. Supporting references contain domain-specific protocols and backend guidance; assets contain reusable templates or icons.

## Versioning and maintenance

The repository uses a lightweight Semantic Versioning convention.

- During `0.x` development, **MINOR** versions may include architectural changes or top-level skill renames while the library is still stabilizing.
- During `0.x` development, **PATCH** versions cover bug fixes, documentation corrections, routing refinements, and other non-breaking maintenance.
- Starting with `1.0.0`, **MAJOR** versions will indicate breaking changes to skill names, interfaces, or core workflow assumptions; **MINOR** versions will add backward-compatible capabilities; **PATCH** versions will remain for fixes and maintenance.

The machine-readable current version is stored in [`VERSION`](VERSION). Significant changes are recorded in [`CHANGELOG.md`](CHANGELOG.md).

The first formally versioned release is `v0.2.0`. Earlier repository history predates formal versioning and is retained through Git history rather than retroactively assigning release numbers.

Methodological references and implementation-backend references are updateable snapshots rather than a frozen canon. When recency matters, skills should verify current papers, publication status, regulatory guidance, software documentation, and package behavior before giving method-specific advice.

## Design principles

These skills are intended to make economics research workflows more explicit and reproducible. Across modules, they emphasize estimand-first reasoning, source verification, transparent assumptions, research-design diagnostics, auditable code, calibrated claims, stable data-flow semantics, and clean boundaries between research design, causal inference, implementation, and writing.

Prefer a small number of well-separated top-level skills over one skill per estimator, language, or task. Add a new top-level skill only when the workflow, mental model, inputs, and outputs are materially distinct from existing modules.

## Planned expansion

The library is designed to grow beyond the current applied-micro and reduced-form workflow. Likely future top-level modules include quantitative structural economics and macroeconometrics. Additional implementation backends such as Python, R, and Julia should normally be added as references under `econ-project-workflow` unless they eventually require a genuinely distinct workflow.

## License

No license has been added yet. Public visibility allows the repository to be read, but reuse rights remain reserved unless a license is added later.
