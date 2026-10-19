# Econ Research Skills

**Current version:** `v0.4.10`

**Maintenance status:** Actively maintained

**Last updated:** 2026-10-20

**Source of truth:** GitHub `main`

Reusable AI skills for economics research: research design, causal inference, descriptive analysis, structural and quantitative modeling, reproducible project workflows, academic writing, and seminar support.

## Skills

| Skill | Purpose |
| --- | --- |
| [econ-research-design](econ-research-design/SKILL.md) | Develop and stress-test research questions, literature positioning, evidence strategies, contributions, and preference-elicitation designs. |
| [causal-inference](causal-inference/SKILL.md) | Design and audit causal identification, estimands, inference, and implementation choices. |
| [econ-descriptive-analysis](econ-descriptive-analysis/SKILL.md) | Produce graph-first descriptive analysis, sample diagnostics, and relative-time parallel-trends figures. |
| [econ-structural-research](econ-structural-research/SKILL.md) | Specify and identify structural models, estimate or calibrate parameters, validate solvers, and audit counterfactuals and welfare. |
| [econ-project-workflow](econ-project-workflow/SKILL.md) | Organize reproducible economics projects across Stata, Python, R, Julia, and mixed-language workflows. |
| [econ-paper-writer](econ-paper-writer/SKILL.md) | Draft and revise source-grounded economics prose and LaTeX while preserving the author's substantive meaning. |
| [seminar-companion](seminar-companion/SKILL.md) | Find the newest available paper version, provide an opening research briefing, and support live seminar discussion. |

## Architecture and boundaries

Organize by research function, not by individual estimator, language, or dataset.

- **Research design** frames the economic uncertainty, evidence strategy, and relative contribution. It is conversational by default, not an unsolicited proposal generator.
- **Causal inference** evaluates identifying variation and assumptions. It does not infer causality from statistical significance or an estimator's label.
- **Descriptive analysis** diagnoses patterns and sample support. It does not promote descriptive differences into causal effects.
- **Structural research** addresses primitives, identification, solution validation, equilibrium feedback, counterfactuals, and welfare. It does not treat fit as identification or force every question into a structural model.
- **Project workflow** governs data lifecycle, entrypoints, validation, performance, and outputs. Preserve immutable raw data and auditable transformations.
- **Paper writing** preserves source-grounded research meaning. Writing execution is not permission to silently redesign the study.
- **Seminar support** is a live cross-cutting workflow, with deeper methodological work handled by the relevant module.

Detailed methods and implementation conventions belong under their natural parent. For example, [preference elicitation](econ-research-design/references/preference-elicitation.md) lives under research design and [Stata conventions](econ-project-workflow/references/stata.md) under project workflow. Keep a small number of distinct top-level modules.

## Repository structure

Each skill has a standalone entrypoint and optional supporting material:

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/    # optional, loaded as needed
└── assets/        # optional
```

`SKILL.md` contains the operating instructions. `agents/openai.yaml` provides presentation metadata for compatible OpenAI skill surfaces; Hermes primarily discovers `SKILL.md`. References contain detailed protocols; assets contain templates or icons. Platform-specific metadata does not imply all platforms expose the same tools.

Repository maintenance files are kept outside skill bundles:

- [VERSION](VERSION): machine-readable library version.
- [CHANGELOG.md](CHANGELOG.md): significant behavior and architecture changes.
- [CONTRIBUTING.md](CONTRIBUTING.md): maintenance and synchronization rules.
- [scripts/validate_repository.py](scripts/validate_repository.py): packaging checks.
- [tests/test_validate_repository.py](tests/test_validate_repository.py): regression tests for those checks.

## Installation and use

These are reusable instructions, not model weights or a training dataset. Installing a skill makes it discoverable; the assistant loads its entrypoint and relevant references when the task requires them. It does not permanently load every document into every conversation.

### Hermes

On the machine that owns the intended Hermes profile, install a skill with:

```bash
hermes -p <profile> skills install Trojon99/econ-research-skills/econ-research-design --category research
```

Replace `<profile>` with the actual profile ID. Repeat using any skill slug listed above. Before replacing an existing installation, back up and compare local changes; do not force-overwrite a locally customized skill without reviewing the differences. Follow the security scan and confirmation prompts. Do not install into a remote research-execution machine merely because the assistant's terminal happens to run there.

The skills are at the repository root, not under `skills/`; do not assume a registry tap's default `skills/` path will discover them. Direct skill identifiers avoid that ambiguity.

After installation, verify each skill is discoverable with `skills_list` and readable with `skill_view`, including linked reference files. Use the installed skill through natural-language tasks; supporting references should be loaded selectively.

### Other skill-compatible assistants

Install the complete skill directory, not just `SKILL.md`, using the platform's supported workflow. Keep relative reference and asset paths intact. Where an instruction names a Hermes tool, use the platform's equivalent permitted capability rather than inventing that tool API.

## Versioning and maintenance

The library uses lightweight Semantic Versioning:

- During `0.x`, MINOR releases may add modules or change architecture and naming.
- During `0.x`, PATCH releases cover non-breaking corrections and refinements.
- Starting with `1.0.0`, MAJOR indicates breaking changes, MINOR backward-compatible additions, and PATCH fixes.

Keep README, `VERSION`, and the newest changelog entry consistent. The first formally versioned release is `v0.2.0`; earlier history remains in Git without retroactively assigned versions.

Run the local packaging checks from the repository root:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

These checks assess metadata consistency, skill packaging, catalog coverage, and local inline Markdown links. They do not validate external URLs, citations, methodological correctness, solver convergence, or economic identification. Verify those separately when relevant.

## Incremental frontier references

Optional, provisional full-text-grounded lessons are available for [sensitive-outcome measurement](causal-inference/references/nber-frontier.md) and [approximate estimation and allocation-policy counterfactuals](econ-structural-research/references/nber-frontier.md). See the [weekly review workflow](econ-research-design/references/weekly-nber-idea-refresh.md) for coverage, reading boundaries, and evidence gates. Public synchronization follows the owner authorization and checks in [CONTRIBUTING.md](CONTRIBUTING.md); local project overlays and preferences remain local.

## Applied-method references

Bounded applied lessons are available for [estimands and inference](causal-inference/references/applied-estimand-inference.md), [nonlinear binned functions](econ-descriptive-analysis/references/nonlinear-binned-functions.md), and [evidence to equilibrium](econ-structural-research/references/evidence-to-equilibrium.md). These distinguish complete tutorial reading from selected primary-source checks; software execution and full proof audits are not claimed.

For forwarded research articles, the [article-intake protocol](econ-project-workflow/references/research-article-intake.md) separates genuine reading, canonical knowledge-base filing, evidence-gated skill promotion, and privacy-preserving GitHub maintenance.


Applied audit coverage also includes [DID targets and trend sensitivity](causal-inference/references/did-target-sensitivity.md), [IV identification](causal-inference/references/iv-identification-audit.md), [RD running-variable support](causal-inference/references/rd-running-variable-audit.md), [synthetic controls](causal-inference/references/synthetic-control-audit.md), [sample/transform auditing](econ-project-workflow/references/sample-transform-audit.md), and [measurement/sensitivity design](econ-research-design/references/measurement-sensitivity-audit.md). Transparent exploratory analysis remains supported; tutorial reading and documentation checks are not code execution or comprehensive method certification.


Targeted references additionally cover [panel/dynamic DML](causal-inference/references/dml-panel-audit.md), [mediation estimands](causal-inference/references/mediation-estimands-audit.md), [AI text measurement](econ-research-design/references/text-measurement-inference.md), [bounded and quantile outcomes](econ-descriptive-analysis/references/bounded-quantile-outcomes.md), and [common-factor panel inference](causal-inference/references/common-factor-panel-audit.md). Existing DID and applied-estimand references integrate outcome-scale and treatment-version lessons without replacing local project supplements.

## Incremental knowledge learning

For supplied articles, books and chapters, use the [shared distillation protocol](econ-project-workflow/references/knowledge-distillation.md): register actual source/edition scope, read a coherent part, extract candidates, check critical support, compare with existing knowledge, integrate or defer, and verify the receipt. Conceptual knowledge goes into subject references; repeatable decisions go into skills; original sources, private project implications and reading records stay local. Chapter completion is not complete-book reading.

Use the [empty ledger](econ-project-workflow/templates/learning-ledger.json), [field contract](econ-project-workflow/templates/learning-ledger.schema.json) and [topic-note template](econ-project-workflow/templates/topic-knowledge-note.md). The source and lesson lifecycle supports candidates, rechecks, explicit conflicts and replacement rather than append-only summaries. No vault writes or schedules are created implicitly.

Check a task ledger through the permitted terminal:

```bash
python3 econ-project-workflow/scripts/validate_learning_ledger.py /authorized/task/learning-ledger.json
```

Replace the illustrative path with the actual authorized task file. Add `--root /authorized/repository` to check promotion targets against the selected checkout. This read-only helper validates declarations, identifiers, cross-references and target containment; it does not read sources, execute tutorial code or prove a claim true. Keep real task ledgers outside public Git.

[Behavior cases](evaluations/README.md) test reasoning only when actually run and reviewed. The GitHub workflow runs packaging and ledger integrity checks, not research ingestion, external LLM calls or scientific certification.


Further model and implementation coverage includes [spatial-equilibrium-implementation](econ-structural-research/references/spatial-equilibrium-implementation.md), [dsge-solver-audit](econ-structural-research/references/dsge-solver-audit.md), [production-function-identification](econ-structural-research/references/production-function-identification.md), [frontier-efficiency-audit](econ-structural-research/references/frontier-efficiency-audit.md), [discrete-choice-identification](econ-structural-research/references/discrete-choice-identification.md), [dynamic-panel-moments](causal-inference/references/dynamic-panel-moments.md), [matching-weighting-audit](causal-inference/references/matching-weighting-audit.md), [survival-riskset-audit](causal-inference/references/survival-riskset-audit.md). Lessons are integrated by topic, with unresolved claims retained outside the public bundle; primary-source checks are scoped and source software has not been executed.

## Research principles

Prioritize accuracy, skepticism, reproducibility, explicit reasoning, and verifiable sources. Preserve exact samples and economic objects; distinguish description, correlation, identification, maintained assumptions, and interpretation. Never invent citations, data access, statistics, or computation results. Use methods proportional to the question. Discussion defaults to Chinese and formal research writing to academic English unless requested otherwise.

Methodological and software references are updateable snapshots, not a frozen canon. Re-verify current papers, publication status, institutional details, and package behavior when recency matters.

## Planned expansion

Structural and quantitative research now has a dedicated workflow. Dedicated macroeconometric guidance remains a possible future extension, not a currently shipped module. Python, R, and Julia implementation guides should normally extend `econ-project-workflow`; Stata currently has the detailed backend reference.

## License

No license has been added. Public visibility permits reading but does not itself grant an open-source reuse license. Any licensing change requires an explicit owner decision.


## Causal and regression foundations

On-demand foundations now cover [causal graphs and adjustment](causal-inference/references/causal-graphs-adjustment.md), [potential outcomes and assignment-based inference](causal-inference/references/potential-outcomes-assignment.md), and [conditional means, projection and inference](econ-descriptive-analysis/references/regression-projection-inference.md). Existing matching, RD, IV, DID/DDD and synthetic-control references integrate bounded conceptual refinements without replacing modern methods or local overlays. Stable textbook definitions and concepts can remain reading-level knowledge; scoped primary checks are distinguished from complete proofs and source-software execution.
