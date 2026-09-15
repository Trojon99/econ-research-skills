# Econ Research Skills

A growing collection of reusable AI skills for economics research, from research design and empirical analysis to academic writing, causal inference, Stata workflows, and future macroeconometric and quantitative-method modules.

## Skills

| Skill | Purpose |
| --- | --- |
| `econ-research-design` | Develop and stress-test economics research questions, literature positioning, evidence strategies, and contributions. |
| `causal-inference` | Design and audit causal identification strategies, estimands, inference, and Stata implementations. |
| `econ-descriptive-analysis` | Produce research-design-oriented descriptive analysis, diagnostics, and figures, including relative-time parallel-trends protocols. |
| `stata-project-workflow` | Organize fast, explicit, reproducible, and auditable Stata research projects. |
| `econ-paper-writer` | Draft and revise source-grounded economics prose and LaTeX while preserving research meaning. |

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

## Design principles

These skills are intended to make economics research workflows more explicit and reproducible. Across modules, they emphasize estimand-first reasoning, source verification, transparent assumptions, research-design diagnostics, auditable code, and calibrated claims.

Methodological references are snapshots rather than a frozen canon. When recency matters, the skills instruct the model to verify current papers, publication status, and software documentation.

## Planned expansion

The library is designed to grow beyond the current reduced-form workflow. Future modules may cover macroeconometrics, quantitative macroeconomics, structural estimation, model solution and calibration, and other economics research workflows.

## License

No license has been added yet. Public visibility allows the repository to be read, but reuse rights remain reserved unless a license is added later.
