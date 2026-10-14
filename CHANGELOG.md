# Changelog

This repository is actively maintained. Significant changes to skill behavior, routing, methodology coverage, or repository structure are recorded here.

The project uses a lightweight Semantic Versioning convention. During `0.x`, MINOR releases may include architectural or naming changes while the skill system is still stabilizing. Starting with `1.0.0`, standard SemVer compatibility rules apply.

## [0.4.2] - 2026-10-14

### Added
- Added applied references synthesizing eight Lianxh tutorials with selected primary-source checks: estimands and inference, nonlinear binned functions, and reduced-form evidence to equilibrium counterfactuals.
- Added minimal on-demand routing in causal inference, descriptive analysis, and structural research without copying deployment-specific entrypoint overlays.

### Boundaries
- Preserved source links, reading levels, identification and software caveats. No software execution, full proof audit, or complete site coverage is claimed.
- Aligned VERSION and README at 0.4.2; no license or local project data changes.

## [0.4.1] - 2026-10-13

### Added
- Added provisional frontier references on sensitive-outcome measurement (NBER w35891), indirect variational inference (w35877), and capacity-constrained allocation counterfactuals (w35893), with source versions, reading scope, support pages, and bounded interpretation.
- Added minimal on-demand routes in causal inference and structural research.

### Changed
- Strengthened the generic weekly NBER workflow with programmatic batch coverage, persistent reading states, explicit full-text/appendix boundaries, and evidence-gated incremental publication. Deployment-specific preferences remain local.
- Documented owner-authorized normal pushes to main after source, privacy, validation, tests, and staged-diff checks; authorization does not bypass protections or substantive review.
- Aligned VERSION and README at 0.4.1. No license change. Packaging checks remain distinct from research-claim verification.

## [0.4.0] - 2026-10-13

Unified empirical and structural research coverage and repository maintenance.

### Added
- Added `econ-structural-research`, adapted from the Economic Research bot's local workflow, for structural identification, calibration and estimation, solver validation, counterfactual closure, and auditable welfare analysis.
- Added its `agents/openai.yaml` presentation metadata.
- Added `CONTRIBUTING.md` with scope, source verification, versioning, validation, and safe synchronization guidance.
- Added `scripts/validate_repository.py` and regression tests for repository metadata and local Markdown-link consistency. These checks validate packaging, not the truth of methodological claims or external citations.

### Changed
- Updated README coverage, module links, installation instructions, and planned expansion.
- Aligned README and `VERSION` at `0.4.0`; corrected the prior README/`VERSION` mismatch.
- Preserved all six existing skill names, entrypoint content, and supporting files.

### Maintenance
- GitHub `main` remains the maintained source of truth. Installing these documents provides reusable instructions, not model retraining or permanently loaded context.
- No license was selected or added; licensing remains an explicit owner decision.

## [0.3.1] - 2026-09-16

HTML results-report presentation refinement.

### Added
- Added `econ-descriptive-analysis/references/html-report-layout.md` for reusable external-facing HTML report structure.
- Standardized a compact navigation card immediately below the report header, with language-matched links for Summary/Figures/Tables/Interpretation Scope/Overall Story.
- Added a functional client-side search field at the far right of the navigation row, including responsive behavior and no external JavaScript dependency.

### Changed
- Updated `econ-descriptive-analysis` so HTML interpretation/showcase reports explicitly load the HTML layout protocol in addition to the result-interpretation protocol.
- Kept the established navigation-row visual composition as the default when an existing report or screenshot provides that pattern.
- Preserved the distinction between internal diagnostic notes and polished external-facing interpretation.

## [0.3.0] - 2026-09-16

Project-workflow architecture expansion.

### Added
- Added `econ-project-workflow` as the language-independent economics research project workflow.
- Added a stable cross-language project contract for `code/`, `data/original/`, `data/work/`, `data/temp/`, `data/output/`, `doc/`, and `log/`.
- Added language-independent guidance for a single project entrypoint, modular stages, data lifecycle, caching, fail-fast validation, reproducibility, cross-language handoffs, and research outputs.
- Added `references/stata.md` as the first detailed implementation backend, preserving the existing Stata performance, validation, output, and coding conventions.
- Added explicit extension points for future Python, R, Julia, and mixed-language backend guidance without creating one top-level skill per language.

### Changed
- Replaced the top-level `stata-project-workflow` skill with `econ-project-workflow`.
- Generalized figure/result review guidance so it is not tied to Stata-generated figures.
- Updated `seminar-companion` routing so implementation/workflow questions across Stata, Python, R, Julia, and mixed-language projects route to `econ-project-workflow`.
- Updated README architecture and versioning rules to reflect the broader workflow layer.

### Migration
- Existing Stata projects should continue using the same folder contract and Stata conventions; those rules now live under `econ-project-workflow/references/stata.md`.
- ChatGPT installations should replace `stata-project-workflow` with the validated `econ-project-workflow` package to avoid duplicate workflow skills.
- GitHub `main` remains the source of truth.

## [0.2.1] - 2026-09-16

Maintenance and synchronization patch.

### Fixed
- Fixed invalid YAML frontmatter in `stata-project-workflow` by quoting the long trigger description so the skill passes the official validator.
- Kept the public Stata workflow generic by referring to the project-designated review benchmark and to collaborators/supervisors rather than project-specific filenames or people.

### Synchronized
- Confirmed `econ-research-design`, `causal-inference`, `econ-descriptive-analysis`, and `econ-paper-writer` are aligned between GitHub and the current ChatGPT skill set.
- Confirmed the GitHub `seminar-companion` includes method routing to causal inference, preference elicitation, descriptive analysis, Stata workflow, and paper writing; the matching validated package is used for ChatGPT-side update.
- GitHub `main` remains the source of truth.

## [0.2.0] - 2026-09-16

First formally versioned release.

### Added
- Added a comprehensive preference-elicitation reference to `econ-research-design`, covering DCE/conjoint analysis, BWS, WTP/WTA, TTO, standard gamble, health-state valuation, preference/scale heterogeneity, validity, and interpretation boundaries.
- Added explicit preference-elicitation routing to `econ-research-design`.
- Added repository-level version and maintenance metadata.

### Changed
- Clarified the intended division of labor across research design, causal inference, descriptive analysis, Stata workflow, paper writing, and seminar support.
- Began standardizing skill metadata and trigger descriptions under the current ChatGPT Skills format.

### Maintenance
- GitHub `main` is the source of truth for the maintained skill library.
- Methodological references are treated as updateable snapshots rather than a frozen canon; current guidance should be re-verified when recency matters.

## Pre-versioning

Before `v0.2.0`, the repository was developed iteratively without formal release numbers. Earlier commits remain available in Git history, but no retrospective semantic-version labels are assigned to them.
