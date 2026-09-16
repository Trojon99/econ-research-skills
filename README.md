# Econ Research Skills

**Current version:** `v0.2.0`  
**Maintenance status:** Actively maintained  
**Last updated:** 2026-09-16  
**Source of truth:** GitHub `main`

A growing collection of reusable AI skills for economics research, from research design and empirical analysis to academic writing, causal inference, Stata workflows, and future macroeconometric and quantitative-method modules.

## Skills

| Skill | Purpose |
| --- | --- |
| `econ-research-design` | Develop and stress-test economics research questions, literature positioning, evidence strategies, contributions, and preference-elicitation designs. |
| `causal-inference` | Design and audit causal identification strategies, estimands, inference, and Stata implementations. |
| `econ-descriptive-analysis` | Produce research-design-oriented descriptive analysis, diagnostics, and figures, including relative-time parallel-trends protocols. |
| `stata-project-workflow` | Organize fast, explicit, reproducible, and auditable Stata research projects. |
| `econ-paper-writer` | Draft and revise source-grounded economics prose and LaTeX while preserving research meaning. |
| `seminar-companion` | Find the latest working-paper version, open with Title / Research Question / Empirical Methodology / Data / Main Evidence, and follow academic seminars live. |

## Architecture

The library is organized by research function rather than by estimator or narrow method.

- `econ-research-design` is the upstream research-design layer. It frames questions, maps evidence strategies, positions literature, and routes specialized methodological work.
- `causal-inference` handles identification, estimands, estimator-design fit, inference, and causal-method audits.
- `econ-descriptive-analysis` handles graph-first pre-regression diagnostics, sample support, trends, raw DID/DDD patterns, and descriptive event-time evidence.
- `stata-project-workflow` governs implementation, project structure, performance, reproducibility, validation, and result-review workflows.
- `econ-paper-writer` handles source-grounded writing and editing without silently redesigning the research.
- `seminar-companion` is a cross-cutting live workflow layer that can route deeper methodological questions to the relevant skill.

Detailed methods that do not require their own top-level skill should live as references under the most natural parent skill. For example, preference elicitation is maintained under `econ-research-design/references/preference-elicitation.md` rather than as a separate top-level skill.

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

`SKILL.md` is the entry point. Supporting references contain domain-specific protocols and methodological guidance; assets contain reusable templates or icons.

## Versioning and maintenance

The repository uses a lightweight Semantic Versioning convention.

- **MAJOR** versions indicate breaking changes to skill names, interfaces, or core workflow assumptions.
- **MINOR** versions add a new top-level skill, a substantial methodological module, or another meaningful capability expansion.
- **PATCH** versions cover bug fixes, documentation corrections, routing refinements, and other non-breaking maintenance.

The machine-readable current version is stored in [`VERSION`](VERSION). Significant changes are recorded in [`CHANGELOG.md`](CHANGELOG.md).

The first formally versioned release is `v0.2.0`. Earlier repository history predates formal versioning and is retained through Git history rather than retroactively assigning release numbers.

Methodological references are updateable snapshots rather than a frozen canon. When recency matters, skills should verify current papers, publication status, regulatory guidance, and software documentation before giving method-specific advice.

## Design principles

These skills are intended to make economics research workflows more explicit and reproducible. Across modules, they emphasize estimand-first reasoning, source verification, transparent assumptions, research-design diagnostics, auditable code, calibrated claims, and clean boundaries between research design, causal inference, implementation, and writing.

Prefer a small number of well-separated top-level skills over one skill per estimator or task. Add a new top-level skill only when the workflow, mental model, inputs, and outputs are materially distinct from existing modules.

## Planned expansion

The library is designed to grow beyond the current applied-micro and reduced-form workflow. Likely future top-level modules include quantitative structural economics and macroeconometrics, with method-specific details kept as references unless they justify a distinct workflow.

## License

No license has been added yet. Public visibility allows the repository to be read, but reuse rights remain reserved unless a license is added later.
