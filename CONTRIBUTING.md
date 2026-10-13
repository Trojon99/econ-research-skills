# Maintenance Guide

## Scope

Keep GitHub `main` as the maintained source of truth for this library. Preserve stable skill slugs and the root-level skill directory layout. Prefer extending a natural parent reference over creating a skill for every estimator, dataset, language, or project. Add a top-level skill only when its question, workflow, inputs, and outputs are meaningfully distinct.

## Research content

- Preserve estimands, samples, units, timing, uncertainty, and the distinction between evidence and assumptions.
- Never invent citations, data, institutional facts, statistical results, or executed numerical outputs.
- Verify claims against the relevant full source where feasible; label abstract-only review and unresolved facts.
- Keep causal identification, structural identification, numerical validation, description, and writing responsibilities distinct.
- Do not change raw data, credentials, remote execution settings, unrelated profiles, or access iCloud files.
- Avoid project-specific personal paths, identifiers, and private data in public skills. Generalize reusable procedures without removing meaningful constraints.

## Skill packaging

Every skill must contain a UTF-8 `SKILL.md` starting with YAML frontmatter, including `name` and `description`, followed by a nonempty body. Match `name` to the directory slug. Keep trigger descriptions informative; put detailed workflow and method guidance in the body and supporting references.

Preserve the complete skill bundle, including references, templates, assets, and optional presentation metadata. Keep internal links relative and resolvable. Presentation metadata for one platform does not guarantee tool availability on another. Do not assign a new license without the owner's explicit decision.

## Changes and validation

1. Work in a clean checkout and review the base revision and pending changes.
2. Preserve existing skill content unless a substantive edit is intended and explained.
3. For behavior or module changes, update `VERSION`, README version/date and catalog, and the newest changelog entry together. New module additions during `0.x` use a MINOR bump.
4. Run `python3 scripts/validate_repository.py` and `python3 -m unittest discover -s tests -v` from the repository root.
5. Review `git diff --check` and the exact staged diff before committing. Verify remote state after pushing.

The validator checks packaging: version agreement, required entrypoint metadata, unique names and matching slugs, catalog coverage, and local inline Markdown file links. It is not a general YAML parser and does not verify external URLs, reference-style links, anchors, research claims, citations, identification, or computation results. Changes to full YAML or substantive methods require appropriate additional review.

## Safe synchronization into a bot

1. Confirm the target profile's actual owning machine and ID. The assistant's SSH execution host may not own its profile.
2. Back up the target skill bundles and compare them with the selected repository revision.
3. Preserve unrelated skills. If local research improvements are absent upstream, retain them or reconcile them explicitly before replacement.
4. Install through the supported skill manager and respect security scan results; do not bypass blocked scans casually.
5. Verify each entrypoint and all referenced local files are present and readable; record the source commit and any intentionally retained local differences.
6. Skills are on-demand instructions. Read the relevant entrypoint and references for the research task; do not claim installation retrained the language model or validated all economic methods.
7. Keep reusable lessons in the appropriate skill. Maintain repository-controlled improvements in GitHub as well; do not let local edits silently drift from the source of truth.


## Owner-authorized incremental publication

The repository owner may explicitly authorize direct commits and normal fast-forward pushes to `main` for reviewed incremental references and minimal routing or maintenance changes; a PR is not required under that authorization. Without it, use the agreed review workflow. Major changes to core methodological rules require substantive review. Never force-push, weaken branch protections, change licensing, or silently resolve substantive conflicts.

Before publication:

1. Confirm the repository, authenticated account, owner authorization, clean checkout, and current remote base. Back up or record the exact source and target hashes.
2. Whitelist public files. Exclude personal paths, project-specific overlays and benchmarks, private research details, credentials, logs, AppleDouble metadata, raw data, and complete copyrighted papers. Do not upload a profile directory.
3. Review each lesson against the actually read source and support sections/pages. Separate author claims from proposed diagnostics; retain reading scope, assumptions, rival explanations, and limitations. Working-paper evidence is provisional, not consensus.
4. Run repository validation, unit tests, `git diff --check`, and a privacy/secret scan of additions. Inspect the complete staged diff and stage exact paths. Update version, README, and changelog consistently; non-breaking reference refinements normally use PATCH. Packaging tests do not validate economic claims.
5. Commit and push normally only after every gate passes. Stop on failed checks, permission errors, concurrent remote changes requiring review, or conflicts; preserve the proposed update and report the blocker.
6. Read the exact remote commit and changed files back. Record the commit URL, file hashes, checks, and intentionally retained local preferences or overlays. Publishing instructions is not model training.
